# FE Figure Reflow / Subscript Cleanup — 0882–1031

Date: 2026-10-30

## Scope

150 canonical figure pairs, indices 0882 through 1031. The later Batch-29 replacement for 0942 / FIG-03-30-001 was used instead of the superseded Batch-19 artwork.

## Results

- Figure pairs processed: **150 / 150**
- Figures containing pseudo-subscript underscores in source: **85**
- Visible underscore tokens converted to true SVG subscripts: **691**
- Remaining underscore text: **0**
- Production-ID footers remaining: **0**
- Titles reflowed: **150**
- Bottom explanatory caption blocks reflowed: **121**
- Semantic text preservation checks: **150 / 150**
- Non-text graphics/path preservation checks: **150 / 150**
- Valid regenerated PNGs: **150 / 150**
- Overall structural passes: **150 / 150**
- Average canvas-area reduction vs. source: **33.35%**
- Canvas-area reduction range: **20.78%–58.72%**

## Cleanup standard

The batch uses the revised figure standard established from FIG-02-27-002:

1. remove the embedded production ID / figure filename footer;
2. convert underscore notation to real smaller/lowered SVG subscripts;
3. pull the title toward the instructional content when excess top whitespace exists;
4. pull explanatory bottom captions upward when excess internal whitespace exists;
5. tighten the final canvas only after internal reflow;
6. preserve all non-text diagram geometry and semantic text;
7. regenerate PNG from the repaired SVG at 3600 px width.

## Repository placement

Replacement files are already packaged under:

- `figures/svg/`
- `figures/png/`

No alternate descriptive filenames are created.
