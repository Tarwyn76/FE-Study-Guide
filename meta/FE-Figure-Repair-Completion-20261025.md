# FE Figure Engineering QA — Phase 1 Repair Completion

Date: 2026-10-25

## Status

**PASS — Phase 1 repair queue closed.**

- Original repair-queue findings resolved: **18**
- Additional chapter arithmetic defect discovered and resolved during repair: **1**
- Total resolved repair records: **19**
- Canonical manifest rows retained: **1404**
- New manuscript figure callouts inserted: **13**
  - Chapter 01-02: **10**
  - Chapter 01-03: **3**
- Figure asset aliases supplied for those callouts: **13 PNG + 13 SVG**
- Technical artwork replacements: **FIG-01-18-006 PNG + SVG**
- Inline alt-text fixes: **FIG-03-19-003**, **FIG-03-30-001**
- Manifest metadata fixes: **FIG-00-01-002**, **FIG-01-03-003**, **FIG-03-19-003**, **FIG-03-30-001**

## Technical Corrections

### FIG-01-18-006 — open-top tank optimization
The figure now uses the chapter-correct model throughout:

- Volume: `V = x²h = 32 m³`
- Height relation: `h = 32/x²`
- Area: `A(x) = x² + 128/x`
- Minimum: `x = 4 m`, `h = 2 m`, `A_min = 48 m²`

The plot itself was already correct; the inconsistent tank annotations were repaired in the SVG and the 3600 × 2400 PNG was regenerated from that corrected SVG.

### Chapter 01-03 — intermediate rounding
The chapter now agrees with the figure and correct arithmetic:

- `1.256 × 0.8834 = 1.1095504`
- `1.1095504 / 0.6214 = 1.785565... -> 1.786`
- Early-rounding comparison: `1.110 / 0.6214 = 1.78629... -> 1.786`
- `12.47 × 0.0834 = 1.039998`
- `1.039998 / 0.0031 = 335.483... -> 335`
- Early-rounded denominator: `1.04 / 0.003 = 346.667... -> 347`
- The chapter and manifest explicitly state that the **displayed rounded results** 335 and 347 differ by approximately **3.6%**.

## Integration Repairs

Chapter 01-02 now contains all ten previously missing figure callouts. Chapter 01-03 now contains all three previously missing callouts. Matching chapter-style PNG/SVG filenames are supplied in `figures/`.

The Civil source chapters now have inline alt text that matches the redesigned Batch-29 artwork for reservoir routing and project delivery.

## Verification

- All repair queue rows: `RESOLVED`
- Chapter 01-02 callouts: 10/10 present
- Chapter 01-03 callouts: 3/3 present
- Every newly inserted callout resolves to a supplied PNG asset
- Corrected tank SVG contains no stale `V = x²h = 64`, `h = 64/x²`, or `h = 4` minimum annotation
- Corrected tank PNG dimensions: 3600 × 2400
- Fixed manifest retains 1404 rows and unique figure IDs
- Apply script idempotency test: second application produced `updated files: 0`

## Remaining Figure QA Work

This closes the **identified Phase-1 repair queue**, not the full 1,404-figure manual visual audit. Manual/technical QA should resume with normal figure indices **132–181**.
