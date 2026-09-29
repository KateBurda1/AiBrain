#!/usr/bin/env python3
"""Build a new deck by picking slides from the KB&Co PPT Master Library.

Keeps the master's layouts, fonts, images and brand look. Only the picked
slides survive, in the order given.

Usage:
  python3 build_deck.py "<output.pptx>" 1 2 3 4 5 33 37 38 48
  python3 build_deck.py "<output.pptx>" 1-5 33 37-38 48
  python3 build_deck.py --master "<other.pptx>" "<output.pptx>" 1 3
"""
import sys
from pathlib import Path
from pptx import Presentation

HERE = Path(__file__).resolve().parent
BRAIN = HERE.parent.parent
MASTER = BRAIN / "my-files (knowledge)/ppt Templates used in presentations/KB & Co PPT Library/PPT Master LIbrary.pptx"


def parse_picks(args):
    picks = []
    for a in args:
        if "-" in a:
            lo, hi = (int(x) for x in a.split("-"))
            picks.extend(range(lo, hi + 1))
        else:
            picks.append(int(a))
    return picks


def build(master, out, picks):
    prs = Presentation(str(master))
    sld_ids = prs.slides._sldIdLst
    entries = list(sld_ids)
    n = len(entries)
    bad = [p for p in picks if p < 1 or p > n]
    if bad:
        sys.exit(f"Slide numbers out of range (master has {n}): {bad}")
    if len(set(picks)) != len(picks):
        sys.exit("Each slide can only be picked once. Duplicate it in PowerPoint if you need it twice.")

    keep = [entries[p - 1] for p in picks]
    for e in entries:
        sld_ids.remove(e)
        if e not in keep:
            prs.part.drop_rel(e.rId)
    for e in keep:
        sld_ids.append(e)

    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out))
    print(f"Saved {len(keep)} slides to {out}")


if __name__ == "__main__":
    args = sys.argv[1:]
    master = MASTER
    if args[:1] == ["--master"]:
        master, args = Path(args[1]), args[2:]
    if len(args) < 2:
        sys.exit(__doc__)
    build(master, args[0], parse_picks(args[1:]))
