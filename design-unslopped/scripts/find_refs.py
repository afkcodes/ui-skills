#!/usr/bin/env python3
"""Find reference designs whose review notes match keywords, best match first.

Usage:
    python3 find_refs.py checkout mobile furniture    # ranked: entries matching most keywords first
    python3 find_refs.py "check your answers" gov.uk  # quote a phrase to match the words in order
    python3 find_refs.py --all payments table status  # only entries that match every keyword
    python3 find_refs.py --top 20 settings            # show more results (default 12)
    python3 find_refs.py --list                       # list all entries (number + title)

Searches references/design-notes.md (one '## NNN Title' block per design) and prints the matching
blocks with the path of the preview and the full-size image so you can open them.

Matching is on whole words with light stemming, so "brutalist" finds "NEO-BRUTALISM", "price"
finds "pricing" and "cart" does not find "cartoon". A keyword in the entry's title line scores
more than one in its body. Negative examples are marked [NEGATIVE]: read them for what to avoid,
never as one of the three references.
"""
import argparse
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / "references" / "design-notes.md"
PREVIEWS = HERE.parent / "assets" / "previews"          # bundled ~1100px copies, always present
REF_DIR = HERE.parent.parent / "reference"             # optional full-resolution library

WORD = re.compile(r"[a-z0-9]+")
COMPOUND = re.compile(r"[a-z0-9]+(?:[-.•][a-z0-9]+)+")  # neo-brutalism, gov.uk, GOV•UK
NEGATIVE = re.compile(r"kept as (?:a|the) \**(?:tool-mode )?negative", re.I)


def stem(word):
    """Light suffix stripping, enough to join plurals, -ing and -ist/-ism forms."""
    if len(word) <= 3 or word.isdigit():
        return word
    if word.endswith("ies") and len(word) > 4:
        word = word[:-3] + "y"
    elif word.endswith(("sses", "shes", "ches", "xes", "uses")):
        word = word[:-2]
    elif word.endswith("s") and not word.endswith(("ss", "us", "is")):
        word = word[:-1]
    for suf in ("ist", "ism", "ing", "ed"):
        if word.endswith(suf) and len(word) - len(suf) >= 4:
            word = word[: -len(suf)]
            break
    if word.endswith("e") and len(word) > 4:
        word = word[:-1]
    return word


def tokens(text):
    return [stem(w) for w in WORD.findall(text.lower())]


def compounds(text):
    """Hyphenated or dotted words joined up, so "neobrutalism" finds "neo-brutalism"."""
    return {stem(re.sub(r"[-.•]", "", c)) for c in COMPOUND.findall(text.lower())}


def load_blocks():
    text = NOTES.read_text(encoding="utf-8")
    parts = re.split(r"^## (?=\d{3} )", text, flags=re.M)
    blocks = []
    for part in parts[1:]:
        part = re.split(r"^# ", part, maxsplit=1, flags=re.M)[0]  # drop the next batch's preamble
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


def count(seq, toks, extra):
    """How often the stemmed word sequence appears in toks (plus once if it is a joined compound)."""
    n = len(seq)
    hits = sum(1 for i in range(len(toks) - n + 1) if toks[i:i + n] == seq)
    if not hits and n == 1 and seq[0] in extra:
        hits = 1
    return hits


def score(terms, title, body):
    """(keywords matched, weighted score). A title hit counts 3, body hits add log-scaled weight."""
    t_toks, b_toks = tokens(title), tokens(body)
    t_extra, b_extra = compounds(title), compounds(body)
    matched, total = 0, 0.0
    for seq in terms:
        in_title = count(seq, t_toks, t_extra)
        in_body = count(seq, b_toks, b_extra)
        if in_title or in_body:
            matched += 1
            total += (3 if in_title else 0) + 1 + math.log1p(in_body)
    return matched, total


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("keywords", nargs="*")
    ap.add_argument("--all", action="store_true", help="only entries that match every keyword")
    ap.add_argument("--any", action="store_true", help=argparse.SUPPRESS)  # the default now; kept for old commands
    ap.add_argument("--top", type=int, default=12, help="how many entries to show (default 12; 0 = all)")
    ap.add_argument("--list", action="store_true", help="list all entries")
    ap.add_argument("--full", action="store_true", help="print full note blocks (default: first 6 lines)")
    args = ap.parse_args()

    blocks = load_blocks()
    images = load_image_paths()

    if args.list or not args.keywords:
        for num, title, body in blocks:
            mark = "  [NEGATIVE]" if NEGATIVE.search(body) else ""
            print(f"{num:03d}  {title}{mark}")
        if not args.keywords:
            print("\nPass keywords to search, e.g.: find_refs.py checkout mobile furniture", file=sys.stderr)
        return

    terms = [tokens(k) for k in args.keywords]
    terms = [t for t in terms if t]
    hits = []
    for num, title, body in blocks:
        matched, total = score(terms, title, body)
        if matched and (matched == len(terms) or not args.all):
            hits.append((matched, total, num, title, body))
    hits.sort(key=lambda h: (-h[0], -h[1], h[2]))

    if not hits:
        print("No matches. Try fewer or broader keywords, or synonyms (basket/cart, chip/badge, table/list).")
        return
    shown_hits = hits if args.top <= 0 else hits[:args.top]
    for matched, _, num, title, body in shown_hits:
        preview, full = images.get(num, (None, None))
        mark = "  [NEGATIVE]" if NEGATIVE.search(body) else ""
        print("=" * 78)
        print(f"{num:03d}  {title}{mark}")
        print(f"matches {matched} of {len(terms)} keyword(s)")
        if preview:
            print(f"preview: {preview}")
        if full:
            print(f"full-res: {full}")
        lines = body.rstrip("\n").split("\n")[1:]
        shown = lines if args.full else lines[:6]
        print("\n".join(l for l in shown if l.strip()))
        if not args.full and len(lines) > 6:
            print("  ... (use --full for the whole entry)")
    print("=" * 78)
    more = f", showing the top {len(shown_hits)} (--top 0 for all)" if len(shown_hits) < len(hits) else ""
    print(f"{len(hits)} match(es){more}")


if __name__ == "__main__":
    main()
