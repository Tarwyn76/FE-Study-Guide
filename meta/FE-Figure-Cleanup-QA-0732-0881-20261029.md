# FE Figure Cleanup + QA — 0732–0881

Date: 2026-10-29

## Scope

150 canonical figure pairs, indices 0732 through 0881.

## Alteration method

- SVG is the canonical repair source.
- Removed exactly one production-only footer/index from each SVG.
- Tightened the SVG viewBox around remaining visible instructional content with a controlled safety margin.
- Four long-title/caption figures (0798, 0815, 0841, 0880) retained their original horizontal canvas extent after edge review while still receiving vertical whitespace reduction and footer removal.
- Preserved all remaining SVG instructional objects exactly after normalizing root canvas geometry.
- Regenerated each PNG from the repaired SVG at 3600 px width.
- Retained the existing indexed filenames.

## Results

- SVG pairs processed: **150/150**
- Embedded production IDs removed: **150/150**
- Instructional SVG objects preserved exactly: **150/150**
- Average outer-canvas area reduction: **10.22%**
- Minimum / maximum area reduction: **3.55% / 17.24%**
- Regenerated PNG integrity: **150/150 PASS**
- Cleaned contact-sheet visual review: **150/150 PASS**
- Figures requiring individual crop adjustment: **4**
- New clipping/layout defects after adjustment: **0**
- New technical-content repair items: **0**
- Independent numerical checks: **129/129 PASS**

The cumulative manual QA ledger now contains **866 unique reviewed figures**.

## Repository placement

Replacement files are packaged at their repository-relative locations:

- `figures/png/0732_...png` through `figures/png/0881_...png`
- `figures/svg/0732_...svg` through `figures/svg/0881_...svg`

No chapter or canonical figure-manifest edits are required because indexed filenames and figure IDs are unchanged.
