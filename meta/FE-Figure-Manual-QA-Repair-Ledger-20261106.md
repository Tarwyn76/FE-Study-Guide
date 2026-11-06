# FE Figure Manual QA Repair Ledger — 2026-11-06

This ledger records 25 human-verified figure corrections. Human QA overrides automated pass/review status.

## Priority summary

- **P1 — 5 confirmed overflow failures:** 0521, 0579, 0583, 0614, 0616.
- **P2 — 7 structural/layout failures:** 0013, 0015, 0018, 0022, 0007, 0008, 0019.
- **P3 — 13 spacing/whitespace corrections:** 0003, 0006, 0009, 0010, 0014, 0017, 0021, 0023, 0024, 0026, 0028, 0029, 0030.

## Validation policy

A repaired figure may be marked PASS only when:
1. no text, image, arrow, line, box, or target is clipped or crosses the canvas;
2. content is centered or intentionally aligned with balanced safe margins;
3. nonfunctional whitespace is materially reduced;
4. line weights and connector geometry are internally consistent;
5. text remains legible and does not overlap other content;
6. no figure number or filename is embedded in the artwork;
7. the repaired PNG and SVG, when both exist, remain visually equivalent.

## Repair classes

**Redraw / redesign:** 0015, 0018, 0022, 0521, 0579, 0583, 0614, 0616.

**Layout adjustment:** 0003, 0006, 0007, 0008, 0009, 0010, 0013, 0014, 0017, 0019, 0021, 0023, 0024, 0026, 0028, 0029, 0030.

The detailed row-level instructions and pass criteria are in `FE-Figure-Manual-QA-Repair-Ledger-20261106.csv`.
