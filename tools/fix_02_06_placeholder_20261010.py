#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"E:\Documents\GitHub\FE-Study-Guide")
matches = list(root.rglob("02-06-Annual-Worth-Capital-Recovery-and-Gradient-Series.md"))
if len(matches) != 1:
    raise SystemExit(f"Expected one 02-06 chapter, found {len(matches)}: {matches}")

p = matches[0]
text = p.read_text(encoding="utf-8")
old = ("15. First verify the analysis period, interest rate, uniform-series timing, "
       "and whether a gradient begins with the first payment or one period later.")
new = ("15. Establish the analysis period, interest rate, uniform-series timing, "
       "and gradient start point before selecting the annual-worth or gradient factor; "
       "a one-period timing shift changes the equivalent annual result.")

if old not in text:
    raise SystemExit("Target sentence not found; file may already be corrected.")

bak = p.with_suffix(p.suffix + ".bak-placeholder")
if not bak.exists():
    bak.write_text(text, encoding="utf-8")

p.write_text(text.replace(old, new, 1), encoding="utf-8")
print(f"Corrected: {p}")
