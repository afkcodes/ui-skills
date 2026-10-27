#!/usr/bin/env python3
"""Render an HTML screen to PNG with headless Chrome at the true layout width.

Usage:
    python3 render.py home.html home.png                     # 1440 wide, full page + first screen
    python3 render.py home.html home.png --width 390         # mobile, laid out at 390 (not 500)
    python3 render.py home.html home.png --width 390 --slices   # also one PNG per screen of scroll
    python3 render.py home.html home-dark.png --width 412 --dark

Writes OUT (the full page), OUT-fold.png (the first screen: what the user sees before scrolling)
and, with --slices, OUT-s02.png, OUT-s03.png ... (each further screen of scroll at full
resolution; the fold is screen 1).

Why not call Chrome directly: headless Chrome will not lay a window out narrower than 500px, so a
390 or 412 render from --window-size is a crop of a 500px layout. This script lays the page out in
an iframe of the exact width and crops the PNG to it. It also forces the light
colour scheme unless --dark is given, because headless Chrome otherwise follows the computer's
appearance setting. A full-page PNG of a tall mobile screen is shrunk when you open it; judge type
and spacing on the fold and the slices.

Wrapper pages go in a new folder in the system temp directory, which the OS clears.
"""
import argparse
import math
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

VIEWPORTS = {360: 800, 390: 844, 393: 852, 402: 874, 412: 915, 430: 932, 768: 1024, 1024: 768,
             1280: 800, 1440: 900, 1920: 1080}
MIN_WINDOW = 500  # headless Chrome's narrowest layout width


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    mac = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if Path(mac).is_file():
        return mac
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        if shutil.which(name):
            return shutil.which(name)
    sys.exit("Chrome not found. Install Google Chrome or set CHROME=/path/to/chrome.")


def crop_png(path, width):
    """Keep the left `width` pixels of a PNG in place (8-bit, non-interlaced, as Chrome writes)."""
    data = path.read_bytes()
    pos, ihdr, idat = 8, None, []
    while pos < len(data):
        n = int.from_bytes(data[pos:pos + 4], "big")
        kind, body = data[pos + 4:pos + 8], data[pos + 8:pos + 8 + n]
        if kind == b"IHDR":
            ihdr = body
        elif kind == b"IDAT":
            idat.append(body)
        pos += 12 + n
    w, h, depth, ctype, _, _, interlace = struct.unpack(">IIBBBBB", ihdr)
    bpp = {0: 1, 2: 3, 4: 2, 6: 4}.get(ctype)
    if depth != 8 or interlace or not bpp or width >= w:
        return False
    raw, stride, keep = zlib.decompress(b"".join(idat)), w * bpp + 1, width * bpp
    prev, rows = bytearray(keep), []
    for y in range(h):
        kind, line = raw[y * stride], bytearray(raw[y * stride + 1:y * stride + 1 + keep])
        # Undo the PNG filter on the kept columns only; each byte depends on its left and upper neighbours.
        if kind == 1:
            for i in range(bpp, keep):
                line[i] = (line[i] + line[i - bpp]) & 255
        elif kind == 2:
            line = bytearray((a + b) & 255 for a, b in zip(line, prev))
        elif kind == 3:
            for i in range(keep):
                left = line[i - bpp] if i >= bpp else 0
                line[i] = (line[i] + ((left + prev[i]) >> 1)) & 255
        elif kind == 4:
            for i in range(keep):
                a = line[i - bpp] if i >= bpp else 0
                b, c = prev[i], (prev[i - bpp] if i >= bpp else 0)
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(b"\0" + bytes(line))
        prev = line

    def chunk(kind, body):
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body))

    head = struct.pack(">IIBBBBB", width, h, 8, ctype, 0, 0, 0)
    path.write_bytes(data[:8] + chunk(b"IHDR", head) + chunk(b"IDAT", zlib.compress(b"".join(rows), 6))
                     + chunk(b"IEND", b""))
    return True


def chrome(args, flags, *extra):
    scheme = "0" if args.dark else "1"  # Blink: 0 = dark, 1 = light
    cmd = [args.chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--allow-file-access-from-files", f"--blink-settings=preferredColorScheme={scheme}",
           f"--virtual-time-budget={args.wait}", *flags, *extra]
    return subprocess.run(cmd, capture_output=True, text=True)


def wrapper(tmp, name, page, width, height, top=0, measure=False):
    """A page holding the screen in an iframe of the exact width; optionally scrolled or measuring."""
    if measure:
        script = ("const d=f.contentDocument.documentElement;const a=d.scrollHeight;"
                  "f.style.height=a+'px';setTimeout(()=>{document.title=a+' '+d.scrollHeight},100);")
    else:
        script = f"f.contentWindow.scrollTo(0,{top});"
    html = (f"<!doctype html><html><head><title>pending</title></head><body style='margin:0'>"
            f"<iframe id=f src='{page.as_uri()}' style='border:0;display:block;width:{width}px;"
            f"height:{height}px'></iframe><script>f.onload=()=>{{{script}}}</script></body></html>")
    path = Path(tmp) / name
    path.write_text(html, encoding="utf-8")
    return path


def shot(args, tmp, name, out, height, top=0):
    wrap = wrapper(tmp, name, args.page, args.width, height, top=top)
    window = max(args.width, MIN_WINDOW)
    chrome(args, [f"--window-size={window},{height}", f"--screenshot={out}"], wrap.as_uri())
    if not out.is_file():
        sys.exit(f"Chrome did not write {out}")
    if args.width < MIN_WINDOW and not crop_png(out, args.width):
        print(f"note: could not crop {out.name}; it is {window}px wide with the "
              f"{args.width}px screen at the left", file=sys.stderr)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--viewport", type=int, help="screen height (default by width: 390 -> 844, 412 -> 915, 1440 -> 900)")
    ap.add_argument("--slices", action="store_true", help="also write one PNG per screen of scroll")
    ap.add_argument("--dark", action="store_true", help="render with prefers-color-scheme: dark")
    ap.add_argument("--wait", type=int, default=8000, help="virtual time budget in ms for fonts and scripts")
    args = ap.parse_args()

    args.page = args.page.resolve()
    args.out = args.out.resolve()
    if not args.page.is_file():
        sys.exit(f"No such page: {args.page}")
    args.chrome = find_chrome()
    viewport = args.viewport or VIEWPORTS.get(args.width, 900)
    tmp = tempfile.mkdtemp(prefix="render-")
    args.out.parent.mkdir(parents=True, exist_ok=True)

    measured = chrome(args, ["--dump-dom"], wrapper(tmp, "measure.html", args.page, args.width,
                                                    viewport, measure=True).as_uri())
    m = re.search(r"<title>(\d+) (\d+)</title>", measured.stdout)
    if not m:
        sys.exit("Could not measure the page (did it load? is it a local .html file?)")
    full, stretched = int(m.group(1)), int(m.group(2))

    stem = args.out.with_suffix("")
    written = [shot(args, tmp, "full.html", args.out, full)]
    written.append(shot(args, tmp, "fold.html", Path(f"{stem}-fold.png"), viewport))
    if args.slices and full > viewport:
        for i in range(1, math.ceil(full / viewport)):
            written.append(shot(args, tmp, f"s{i + 1:02d}.html", Path(f"{stem}-s{i + 1:02d}.png"),
                                viewport, top=i * viewport))

    print(f"{args.page.name} at {args.width} x {viewport} screen, page height {full}px"
          f" ({full / viewport:.1f} screens), {'dark' if args.dark else 'light'}")
    for p in written:
        print(f"  {p}")
    if stretched > full:
        print("warning: the layout grows with the window height (vh units), so the full-page PNG "
              "stretches it; trust the fold and --slices renders", file=sys.stderr)


if __name__ == "__main__":
    main()
