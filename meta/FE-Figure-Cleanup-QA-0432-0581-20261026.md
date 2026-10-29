# FE Figure Cleanup + QA — 0432–0581

Date: 2026-10-26

## Scope

150 canonical figure pairs, indices 0432 through 0581.

## Alteration method

- SVG is the canonical repair source.
- Removed exactly one production-only footer text object matching the indexed figure identifier from each SVG.
- Tightened the SVG viewBox around the remaining visible instructional content with a controlled safety margin.
- Preserved all remaining SVG instructional objects exactly; canonical XML comparison passed for 150/150 figures after normalizing root canvas geometry.
- Regenerated the PNG from the repaired SVG at 3600 px width.
- Retained the existing indexed filenames.

## Results

- SVG pairs processed: **150/150**
- Embedded production IDs removed: **150/150**
- Instructional SVG objects preserved exactly: **150/150**
- Average outer-canvas area reduction: **16.69%**
- Minimum / maximum area reduction: **9.28% / 26.99%**
- Regenerated PNG integrity: **150/150 PASS**
- Cleaned contact-sheet visual review: **150/150 PASS**
- New clipping/layout defects: **0**
- New technical-content repair items: **0**
- Independent numeric checks: **76/76 PASS**
- FE Handbook source-specific checks: **1/1 PASS**

The cumulative manual QA ledger now contains **567 unique reviewed figures** through this run.

## Repository placement

Replacement files are already packaged at their repository-relative locations:

- `figures/png/0432_...png` through `figures/png/0581_...png`
- `figures/svg/0432_...svg` through `figures/svg/0581_...svg`

No chapter files or canonical manifest metadata were changed in this batch.
