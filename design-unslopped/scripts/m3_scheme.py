#!/usr/bin/env python3
"""Approximate Material 3 colour roles from one seed colour, light and dark, as CSS variables.

Usage:
    python3 m3_scheme.py "#d9653b"            # light and dark schemes as CSS custom properties
    python3 m3_scheme.py "#d9653b" --table    # a table of role, tone and hex instead

Material 3 builds five tonal palettes from the seed (primary, secondary, tertiary, neutral, neutral
variant) and assigns each role a tone: primary is tone 40 in light and 80 in dark, its container 90
and 30, and so on. Tone is CIELAB lightness, which is what makes the on-colour pairs contrast. This
script keeps the tones exact and approximates Material's HCT hue and chroma in CIELAB, so the hexes
are close to Material Theme Builder's but not identical. For production, generate the scheme with
Material Theme Builder (https://material-foundation.github.io/material-theme-builder/) or the
material-color-utilities library and cite it; use this for mockups when neither is to hand.
"""
import argparse
import math

# role: (palette, light tone, dark tone), the classic Material 3 mapping
ROLES = [
    ("primary", "p", 40, 80), ("on-primary", "p", 100, 20),
    ("primary-container", "p", 90, 30), ("on-primary-container", "p", 10, 90),
    ("secondary", "s", 40, 80), ("on-secondary", "s", 100, 20),
    ("secondary-container", "s", 90, 30), ("on-secondary-container", "s", 10, 90),
    ("tertiary", "t", 40, 80), ("on-tertiary", "t", 100, 20),
    ("tertiary-container", "t", 90, 30), ("on-tertiary-container", "t", 10, 90),
    ("error", "e", 40, 80), ("on-error", "e", 100, 20),
    ("error-container", "e", 90, 30), ("on-error-container", "e", 10, 90),
    ("surface", "n", 98, 6), ("on-surface", "n", 10, 90),
    ("surface-container-lowest", "n", 100, 4), ("surface-container-low", "n", 96, 10),
    ("surface-container", "n", 94, 12), ("surface-container-high", "n", 92, 17),
    ("surface-container-highest", "n", 90, 22),
    ("on-surface-variant", "v", 30, 80), ("outline", "v", 50, 60), ("outline-variant", "v", 80, 30),
    ("inverse-surface", "n", 20, 90), ("inverse-on-surface", "n", 95, 20),
    ("inverse-primary", "p", 80, 40),
]


def to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def hex_to_lch(h):
    h = h.lstrip("#")
    r, g, b = (to_linear(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = [t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116 for t in (x, y, z)]
    L, a, bb = 116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])
    return L, math.hypot(a, bb), math.degrees(math.atan2(bb, a)) % 360


def lch_to_rgb(L, C, H):
    a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    inv = lambda t: t ** 3 if t ** 3 > 216 / 24389 else (116 * t - 16) / (24389 / 27)
    x, y, z = inv(fx) * 0.95047, inv(fy), inv(fz) * 1.08883
    r = 3.2406 * x - 1.5372 * y - 0.4986 * z
    g = -0.9689 * x + 1.8758 * y + 0.0415 * z
    bl = 0.0557 * x - 0.2040 * y + 1.0570 * z
    return r, g, bl


def tone_hex(tone, chroma, hue):
    """The colour at this CIELAB lightness and hue, with chroma reduced until it fits sRGB."""
    if tone >= 100:
        return "#ffffff"
    if tone <= 0:
        return "#000000"
    c = chroma
    while c > 0:
        rgb = lch_to_rgb(tone, c, hue)
        if all(-1e-4 <= v <= 1 + 1e-4 for v in rgb):
            break
        c -= 0.5
    rgb = lch_to_rgb(tone, max(c, 0), hue)
    return "#" + "".join(f"{round(min(max(to_srgb(min(max(v, 0), 1)), 0), 1) * 255):02x}" for v in rgb)


def palettes(seed):
    _, c, h = hex_to_lch(seed)
    c = max(c, 30)  # keep a muted seed from collapsing to grey, as Material's tonal-spot scheme does
    # ratios and hue shift read off the baseline scheme (#6750A4 -> #625B71, #7D5260, #B3261E)
    return {"p": (c, h), "s": (c * 0.27, h), "t": (c * 0.39, (h + 53) % 360),
            "n": (4, h), "v": (9, h), "e": (68, 36)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seed", help="seed colour as #rrggbb")
    ap.add_argument("--table", action="store_true", help="print role, tones and hexes as a table")
    args = ap.parse_args()
    pal = palettes(args.seed)
    rows = [(name, lt, dt, tone_hex(lt, *pal[p]), tone_hex(dt, *pal[p])) for name, p, lt, dt in ROLES]
    if args.table:
        print(f"{'role':28} {'light':>13} {'dark':>13}")
        for name, lt, dt, lh, dh in rows:
            print(f"{name:28} {lt:>3} {lh}   {dt:>3} {dh}")
        return
    print(f"/* Approximate M3 scheme from seed {args.seed}; regenerate with Material Theme Builder for production */")
    print(":root {")
    for name, _, _, lh, _ in rows:
        print(f"  --md-sys-color-{name}: {lh};")
    print("}\n@media (prefers-color-scheme: dark) {\n  :root {")
    for name, _, _, _, dh in rows:
        print(f"    --md-sys-color-{name}: {dh};")
    print("  }\n}")


if __name__ == "__main__":
    main()
