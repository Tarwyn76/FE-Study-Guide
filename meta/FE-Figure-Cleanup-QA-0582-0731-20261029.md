# FE Figure Cleanup + QA — 0582–0731

Date: 2026-10-29

## Scope

150 canonical figure pairs, indices 0582 through 0731.

## Alteration method

- SVG is the canonical repair source.
- Removed exactly one production-only footer/index from each SVG.
- Tightened the SVG viewBox around remaining visible instructional content with a controlled safety margin.
- Four long-caption figures (0593, 0656, 0662, 0702) were widened individually after edge-clearance review.
- Preserved all remaining SVG instructional objects exactly after normalizing root canvas geometry.
- Regenerated each PNG from the repaired SVG at 3600 px width.
- Retained the existing indexed filenames.

## Results

- SVG pairs processed: **150/150**
- Embedded production IDs removed: **150/150**
- Instructional SVG objects preserved exactly: **150/150**
- Average outer-canvas area reduction: **15.57%**
- Minimum / maximum area reduction: **5.90% / 26.05%**
- Regenerated PNG integrity: **150/150 PASS**
- Cleaned contact-sheet visual review: **150/150 PASS**
- Figures requiring individual crop adjustment: **4**
- New clipping/layout defects after adjustment: **0**
- New technical-content repair items: **0**
- Independent numerical checks: **120/120 PASS**

The cumulative manual QA ledger now contains **717 unique reviewed figures**.

## Repository placement

Replacement files are packaged at their repository-relative locations:

- `figures/png/0582_...png` through `figures/png/0731_...png`
- `figures/svg/0582_...svg` through `figures/svg/0731_...svg`

No chapter or canonical figure-manifest edits are required because indexed filenames and figure IDs are unchanged.
