#!/usr/bin/env python3
"""Find reference designs whose review notes match keywords.

Usage:
    python3 find_refs.py payments table status
    python3 find_refs.py --any mobile banking      # match any keyword instead of all
    python3 find_refs.py --list                     # list all entries (number + title)

Searches references/design-notes.md (one '## NNN Title' block per design) and prints the matching
blocks with the path of the image in ../reference/ so you can open it.
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / "references" / "design-notes.md"
PREVIEWS = HERE.parent / "assets" / "previews"          # bundled ~1100px copies, always present
REF_DIR = HERE.parent.parent / "reference"             # optional full-resolution library


def load_blocks():
    text = NOTES.read_text(encoding="utf-8")
    parts = re.split(r"^## (?=\d{3} )", text, flags=re.M)
    blocks = []
    for part in parts[1:]:
        num = int(part[:3])
        title = part.split("\n", 1)[0][4:].strip()
        blocks.append((num, title, part))
    return blocks


def load_image_paths():
    """Map note number -> (preview path, full-res path or None). Uses assets/previews/map.txt
    (number -> reference-relative path) when present; falls back to folder order."""
    previews = {int(p.stem): p for p in PREVIEWS.glob("[0-9][0-9][0-9].jpg")} if PREVIEWS.is_dir() else {}
    mp = PREVIEWS / "map.txt"
    if mp.is_file():
        full = {}
        for line in mp.read_text(encoding="utf-8").splitlines():
            parts = line.strip().split(" ", 1)
            if len(parts) == 2 and parts[0].isdigit():
                cand = REF_DIR / parts[1]
                full[int(parts[0])] = cand if cand.is_file() else None
        return {n: (previews.get(n), full.get(n)) for n in set(previews) | set(full)}
    order = [
        "app-designs/dribbble", "app-designs/behance", "website-designs/dribbble-dashboards",
        "website-designs/dribbble", "website-designs/behance", "website-designs/awwwards",
    ]
    paths = []
    for folder in order:
        d = REF_DIR / folder
        if d.is_dir():
            paths.extend(sorted(p for p in d.iterdir() if p.is_file() and not p.name.startswith(".")))
    full = {i + 1: p for i, p in enumerate(paths)}
    return {n: (previews.get(n), full.get(n)) for n in set(previews) | set(full)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("keywords", nargs="*")
    ap.add_argument("--any", action="store_true", help="match any keyword (default: all)")
    ap.add_argument("--list", action="store_true", help="list all entries")
    ap.add_argument("--full", action="store_true", help="print full note blocks (default: first 6 lines)")
    args = ap.parse_args()

    blocks = load_blocks()
    images = load_image_paths()

    if args.list or not args.keywords:
        for num, title, _ in blocks:
            print(f"{num:03d}  {title}")
        if not args.keywords:
            print("\nPass keywords to search, e.g.: find_refs.py payments table status", file=sys.stderr)
        return

    kws = [k.lower() for k in args.keywords]
    hits = []
    for num, title, body in blocks:
        low = body.lower()
        found = [k for k in kws if k in low]
        ok = bool(found) if args.any else len(found) == len(kws)
        if ok:
            hits.append((len(found), num, title, body))
    hits.sort(key=lambda h: (-h[0], h[1]))

    if not hits:
        print("No matches. Try --any, fewer keywords, or synonyms (chip/badge, table/list, hero/balance).")
        return
    for _, num, title, body in hits:
        preview, full = images.get(num, (None, None))
        print("=" * 78)
        print(f"{num:03d}  {title}")
        if preview:
            print(f"preview: {preview}")
        if full:
            print(f"full-res: {full}")
        lines = body.split("\n")[1:]
        shown = lines if args.full else lines[:6]
        print("\n".join(l for l in shown if l.strip()))
        if not args.full and len(lines) > 6:
            print("  ... (use --full for the whole entry)")
    print("=" * 78)
    print(f"{len(hits)} match(es)")


if __name__ == "__main__":
    main()
