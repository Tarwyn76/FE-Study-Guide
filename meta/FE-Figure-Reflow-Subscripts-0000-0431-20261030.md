# FE Figure Reflow / Subscript Cleanup — 0000–0431

Date: 2026-10-30

## Scope

Retroactive cleanup of the first 432 figures so figures 0000–1403 now use the same production standard.

## Results

- Figures processed: **432 / 432**
- Titles reflowed: **431**
- Genuine below-body caption groups moved upward: **189**
- Pseudo-subscript tokens converted to true SVG subscripts: **27**
- Remaining underscore-based notation: **0**
- Remaining embedded production-ID footers: **0**
- Average canvas-area reduction: **29.42%**
- Minimum reduction: **14.73%**
- Maximum reduction: **56.55%**
- SVG semantic/geometry validation: **432 / 432 PASS**
- PNG integrity validation: **432 / 432 PASS**
- Exact duplicate cleaned SVGs: **0**
- Exact duplicate cleaned PNGs: **0**
- Manual contact-sheet review: **432 / 432 PASS**
- Corrected 0087 tank artwork retained: **PASS**

## Cleanup rules

1. Remove the embedded production footer (`#### • FIG-...`).
2. Convert visible underscore notation such as `F_AB` and `M_O,z` to smaller/lowered SVG subscripts.
3. Reflow the title toward the instructional body.
4. Move only genuine below-body caption blocks upward; panel labels/equations are left in place.
5. Tighten the SVG viewBox around the reflowed content with a safety margin.
6. Regenerate the canonical PNG from the cleaned SVG at 3600 px width.
7. Preserve non-text diagram geometry exactly.

## Technical continuity

This cleanup does not redesign instructional diagrams or alter their numeric/technical content. The previously repaired `0087_FIG-01-18-006` source was used instead of the superseded tank artwork. It retains `V = x²h = 32`, `h = 32/x²`, and the minimum `x = 4 m, h = 2 m, A = 48 m²`.

## Full-library status

With this retroactive pass, all **1,404 figures (0000–1403)** have now received manual visual QA and the revised cleanup standard: production-ID removal, tighter layout/canvas, and true subscript typography where underscore notation existed.
