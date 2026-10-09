# Consolidated FE Technical Audit Summary

**Audit status:** FAIL  
**Root:** `C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide`  
**Ledger:** `C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\meta\ledger.yaml`  
**Figure manifest:** `C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\figure-manifest.csv`  
**PNG artwork directory:** `C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png`  
**SVG artwork directory:** `C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\svg`  
**Artwork requirement:** `both`  

## Scope

- Selected layers: **1, 2, 3**
- Chapters reviewed: **206 / 206 expected from ledger**
- Concept atoms in selected layers: **1375**
- Worked examples parsed: **1791**
- Display formulas parsed: **6026**
- Answer/practice-solution entries parsed: **6828**
- Figure references reviewed: **1388**
- Source/Handbook atom records reviewed: **1375**
- Simple arithmetic statements checked: **167**

## Figure artwork inventory

- Referenced figures with PNG present: **634 / 1388**
- Referenced figures with SVG present: **634 / 1388**
- Complete artwork sets for mode `both`: **634 / 1388**
- Both PNG and SVG present: **634**
- PNG only: **0**
- SVG only: **0**
- Neither format present: **754**
- Manifest-marked artwork QA verified: **0 / 1388**

## Issue counts

- CRITICAL: **0**
- ERROR: **8**
- WARNING: **1044**
- REVIEW: **557**
- INFO: **1388**

## Interpretation

- **CRITICAL** — chapter/file is unavailable or audit scope is incomplete.
- **ERROR** — concrete defect such as placeholder content, malformed equation, or arithmetic mismatch.
- **WARNING** — likely technical-content weakness requiring correction or close review.
- **REVIEW** — cannot be decided mechanically; requires engineering/editorial verification.
- **INFO** — status note, including artwork not yet generated or generated but not yet technically verified.

## Highest-priority findings

- **ERROR — math_delimiter_mismatch** (01-16): Count of \[ and \] display-math delimiters does not match.
- **ERROR — math_delimiter_mismatch** (01-21): Count of \[ and \] display-math delimiters does not match.
- **ERROR — math_delimiter_mismatch** (01-23): Count of \[ and \] display-math delimiters does not match.
- **ERROR — math_delimiter_mismatch** (01-24): Count of \[ and \] display-math delimiters does not match.
- **ERROR — worked_example_missing_solution** (01-33 / Worked Example 3 — Two-Sided $z$ Test): Worked example has no parsed Solution text.
- **ERROR — worked_example_missing_solution** (01-33 / Worked Example 6 — Chi-Square Variance Test): Worked example has no parsed Solution text.
- **ERROR — worked_example_missing_solution** (01-36 / Worked Example 3 — Cylinder Volume with Standard Uncertainties): Worked example has no parsed Solution text.
- **ERROR — math_delimiter_mismatch** (01-38): Count of \[ and \] display-math delimiters does not match.
- **WARNING — figure_png_duplicate_candidates** (01-01 / FIG-01-01-001): Multiple PNG files map to FIG-01-01-001: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0005_FIG-01-01-001.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-001-order-of-magnitude-number-line.png
- **WARNING — figure_png_duplicate_candidates** (01-01 / FIG-01-01-002): Multiple PNG files map to FIG-01-01-002: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0006_FIG-01-01-002.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-002-complete-si-prefix-ladder.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-002-prefix-ladder.png
- **WARNING — figure_png_duplicate_candidates** (01-01 / FIG-01-01-003): Multiple PNG files map to FIG-01-01-003: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0007_FIG-01-01-003.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-003-prefix-pair-matrix.png
- **WARNING — figure_png_duplicate_candidates** (01-01 / FIG-01-01-004): Multiple PNG files map to FIG-01-01-004: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0008_FIG-01-01-004.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-004-axial-load-area-conversion.png
- **WARNING — figure_png_duplicate_candidates** (01-01 / FIG-01-01-005): Multiple PNG files map to FIG-01-01-005: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0009_FIG-01-01-005.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-005-number-sets.png
- **WARNING — figure_png_duplicate_candidates** (01-01 / FIG-01-01-006): Multiple PNG files map to FIG-01-01-006: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0010_FIG-01-01-006.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-006-prefix-direction.png
- **WARNING — figure_png_duplicate_candidates** (01-01 / FIG-01-01-007): Multiple PNG files map to FIG-01-01-007: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0011_FIG-01-01-007.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-01-007-squared-cubed-prefix.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-001): Multiple PNG files map to FIG-01-02-001: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0012_FIG-01-02-001.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-001-quantity-dimension-unit-pyramid.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-002): Multiple PNG files map to FIG-01-02-002: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0013_FIG-01-02-002.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-002-si-derived-units-tree.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-003): Multiple PNG files map to FIG-01-02-003: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0014_FIG-01-02-003.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-003-pendulum-dimensional-check.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-004): Multiple PNG files map to FIG-01-02-004: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0015_FIG-01-02-004.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-004-factor-label-flowchart.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-005): Multiple PNG files map to FIG-01-02-005: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0016_FIG-01-02-005.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-005-unit-system-comparison.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-006): Multiple PNG files map to FIG-01-02-006: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0017_FIG-01-02-006.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-006-g-versus-gc.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-007): Multiple PNG files map to FIG-01-02-007: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0018_FIG-01-02-007.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-007-newtons-law-three-systems.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-008): Multiple PNG files map to FIG-01-02-008: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0019_FIG-01-02-008.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-008-temperature-scales.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-009): Multiple PNG files map to FIG-01-02-009: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0020_FIG-01-02-009.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-009-temperature-selection-flowchart.png
- **WARNING — figure_png_duplicate_candidates** (01-02 / FIG-01-02-010): Multiple PNG files map to FIG-01-02-010: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0021_FIG-01-02-010.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-02-010-universal-gas-constant.png
- **WARNING — introduced_terms_not_found_in_chapter** (01-02): 1 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — figure_png_duplicate_candidates** (01-03 / FIG-01-03-001): Multiple PNG files map to FIG-01-03-001: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0022_FIG-01-03-001.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-03-001-accuracy-precision-matrix.png
- **WARNING — figure_png_duplicate_candidates** (01-03 / FIG-01-03-002): Multiple PNG files map to FIG-01-03-002: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0023_FIG-01-03-002.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-03-002-significant-figures-flowchart.png
- **WARNING — figure_png_duplicate_candidates** (01-03 / FIG-01-03-003): Multiple PNG files map to FIG-01-03-003: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0024_FIG-01-03-003.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-03-003-catastrophic-cancellation.png
- **WARNING — formula_suspicious_text** (01-03 / formula-24): Formula contains prose-like placeholder text.
- **WARNING — formula_suspicious_text** (01-03 / formula-44): Formula contains prose-like placeholder text.
- **WARNING — formula_suspicious_text** (01-03 / formula-45): Formula contains prose-like placeholder text.
- **WARNING — introduced_terms_not_found_in_chapter** (01-05): 3 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — introduced_terms_not_found_in_chapter** (01-07): 3 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — introduced_terms_not_found_in_chapter** (01-08): 1 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — introduced_terms_not_found_in_chapter** (01-09): 4 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — figure_png_duplicate_candidates** (01-11 / FIG-01-11-001): Multiple PNG files map to FIG-01-11-001: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0048_FIG-01-11-001.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-11-001-unit-circle.png
- **WARNING — figure_png_duplicate_candidates** (01-11 / FIG-01-11-002): Multiple PNG files map to FIG-01-11-002: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0049_FIG-01-11-002.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-11-002-standard-angle-table.png
- **WARNING — figure_png_duplicate_candidates** (01-11 / FIG-01-11-003): Multiple PNG files map to FIG-01-11-003: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0050_FIG-01-11-003.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-11-003-cast-diagram.png
- **WARNING — figure_png_duplicate_candidates** (01-11 / FIG-01-11-004): Multiple PNG files map to FIG-01-11-004: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0051_FIG-01-11-004.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-11-004-right-triangle-soh-cah-toa.png
- **WARNING — figure_png_duplicate_candidates** (01-11 / FIG-01-11-005): Multiple PNG files map to FIG-01-11-005: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0052_FIG-01-11-005.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-11-005-law-of-sines.png
- **WARNING — figure_png_duplicate_candidates** (01-11 / FIG-01-11-006): Multiple PNG files map to FIG-01-11-006: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0053_FIG-01-11-006.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-11-006-force-decomposition.png
- **WARNING — introduced_terms_not_found_in_chapter** (01-11): 1 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — figure_png_duplicate_candidates** (01-12 / FIG-01-12-001): Multiple PNG files map to FIG-01-12-001: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0055_FIG-01-12-001.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-12-001-complex-plane.png
- **WARNING — figure_png_duplicate_candidates** (01-12 / FIG-01-12-002): Multiple PNG files map to FIG-01-12-002: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0056_FIG-01-12-002.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-12-002-rectangular-polar-conversion.png
- **WARNING — figure_png_duplicate_candidates** (01-12 / FIG-01-12-003): Multiple PNG files map to FIG-01-12-003: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0057_FIG-01-12-003.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-12-003-phasor-diagram.png
- **WARNING — introduced_terms_not_found_in_chapter** (01-12): 3 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — figure_png_duplicate_candidates** (01-13 / FIG-01-13-001): Multiple PNG files map to FIG-01-13-001: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0058_FIG-01-13-001.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-13-001-vector-components-3d.png
- **WARNING — figure_png_duplicate_candidates** (01-13 / FIG-01-13-002): Multiple PNG files map to FIG-01-13-002: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0059_FIG-01-13-002.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-13-002-vector-addition.png
- **WARNING — figure_png_duplicate_candidates** (01-13 / FIG-01-13-003): Multiple PNG files map to FIG-01-13-003: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0060_FIG-01-13-003.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-13-003-dot-product-geometry.png
- **WARNING — figure_png_duplicate_candidates** (01-13 / FIG-01-13-004): Multiple PNG files map to FIG-01-13-004: C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\0061_FIG-01-13-004.png; C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide\figures\png\archive\FIG-01-13-004-cross-product-right-hand-rule.png
- **WARNING — introduced_terms_not_found_in_chapter** (01-13): 3 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — introduced_terms_not_found_in_chapter** (01-14): 2 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — formula_suspicious_text** (01-16 / formula-13): Formula contains prose-like placeholder text.
- **WARNING — introduced_terms_not_found_in_chapter** (01-17): 1 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — introduced_terms_not_found_in_chapter** (01-21): 4 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — introduced_terms_not_found_in_chapter** (01-22): 3 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — worked_example_short_solution** (01-22 / Worked Example 9 — Building New Series from Old): Worked solution is only 11 words.
- **WARNING — introduced_terms_not_found_in_chapter** (01-25): 1 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — assessment_explanation_short** (01-27 / answer_key 14): answer key entry 14 is only 2 words.
- **WARNING — assessment_explanation_short** (01-27 / answer_key 15): answer key entry 15 is only 6 words.
- **WARNING — assessment_explanation_short** (01-27 / answer_key 20): answer key entry 20 is only 4 words.
- **WARNING — assessment_explanation_short** (01-28 / answer_key 12): answer key entry 12 is only 4 words.
- **WARNING — introduced_terms_not_found_in_chapter** (01-28): 1 ledger-introduced term(s) were not found verbatim in the chapter.
- **WARNING — numeric_example_without_numeric_result** (01-29 / Worked Example 1 — Identify the Variable Type): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — assessment_explanation_short** (01-30 / answer_key 11): answer key entry 11 is only 6 words.
- **WARNING — numeric_example_without_numeric_result** (01-30 / Worked Example 10 — CLT for a Sum): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — numeric_example_without_numeric_result** (01-30 / Worked Example 3 — Convert a $z$ Threshold Back to Units): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — numeric_example_without_numeric_result** (01-30 / Worked Example 5 — Right Tail): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — worked_example_short_solution** (01-30 / Worked Example 3 — Convert a $z$ Threshold Back to Units): Worked solution is only 10 words.
- **WARNING — worked_example_short_solution** (01-30 / Worked Example 4 — Left Tail): Worked solution is only 13 words.
- **WARNING — worked_example_short_solution** (01-30 / Worked Example 5 — Right Tail): Worked solution is only 16 words.
- **WARNING — worked_example_short_solution** (01-30 / Worked Example 6 — Engineering Tolerance Band): Worked solution is only 8 words.
- **WARNING — assessment_explanation_short** (01-31 / answer_key 22): answer key entry 22 is only 6 words.
- **WARNING — assessment_explanation_short** (01-31 / practice_solutions 8): practice solutions entry 8 is only 5 words.
- **WARNING — numeric_example_without_numeric_result** (01-31 / Worked Example 8 — Interpret Two Chi-Square Critical Values): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — assessment_explanation_short** (01-32 / answer_key 18): answer key entry 18 is only 6 words.
- **WARNING — assessment_explanation_short** (01-32 / practice_solutions 11): practice solutions entry 11 is only 6 words.
- **WARNING — assessment_explanation_short** (01-32 / practice_solutions 7): practice solutions entry 7 is only 5 words.
- **WARNING — formula_suspicious_text** (01-32 / formula-172): Formula contains prose-like placeholder text.
- **WARNING — formula_suspicious_text** (01-32 / formula-2): Formula contains prose-like placeholder text.
- **WARNING — practice_numeric_without_numeric_solution** (01-32 / Practice Problem 5): Practice problem contains numeric data but its solution contains no numeric result.
- **WARNING — numeric_example_without_numeric_result** (01-33 / Worked Example 1 — Translate the Engineering Claim): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — worked_example_short_solution** (01-33 / Worked Example 1 — Translate the Engineering Claim): Worked solution is only 10 words.
- **WARNING — assessment_explanation_short** (01-34 / answer_key 13): answer key entry 13 is only 6 words.
- **WARNING — assessment_explanation_short** (01-34 / answer_key 16): answer key entry 16 is only 6 words.
- **WARNING — assessment_explanation_short** (01-34 / practice_solutions 1): practice solutions entry 1 is only 4 words.
- **WARNING — assessment_explanation_short** (01-34 / practice_solutions 6): practice solutions entry 6 is only 6 words.
- **WARNING — numeric_example_without_numeric_result** (01-34 / Worked Example 2 — Compute the One-Way Sums of Squares): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — numeric_example_without_numeric_result** (01-34 / Worked Example 8 — Choose the Design): Problem contains numeric data, but the parsed solution contains no numeric result.
- **WARNING — worked_example_short_solution** (01-34 / Worked Example 2 — Compute the One-Way Sums of Squares): Worked solution is only 4 words.
- **WARNING — assessment_explanation_short** (01-35 / answer_key 15): answer key entry 15 is only 6 words.
- **WARNING — assessment_explanation_short** (01-36 / answer_key 19): answer key entry 19 is only 6 words.
- **WARNING — assessment_explanation_short** (01-36 / answer_key 25): answer key entry 25 is only 5 words.
- **WARNING — assessment_explanation_short** (01-37 / answer_key 4): answer key entry 4 is only 6 words.
- **WARNING — assessment_explanation_short** (01-37 / practice_solutions 9): practice solutions entry 9 is only 4 words.
- **WARNING — formula_suspicious_text** (01-37 / formula-35): Formula contains prose-like placeholder text.
- **WARNING — formula_suspicious_text** (01-37 / formula-36): Formula contains prose-like placeholder text.
- **WARNING — practice_numeric_without_numeric_solution** (01-37 / Practice Problem 10): Practice problem contains numeric data but its solution contains no numeric result.
- **WARNING — practice_numeric_without_numeric_solution** (01-37 / Practice Problem 9): Practice problem contains numeric data but its solution contains no numeric result.

## Category counts

- `figure_artwork_missing`: 754
- `figure_artwork_not_verified`: 634
- `worked_example_short_solution`: 443
- `assessment_explanation_short`: 331
- `source_split_unresolved`: 247
- `repeated_solution_text`: 191
- `numeric_example_without_numeric_result`: 166
- `worked_example_solution_units`: 57
- `handbook_claim_unverified`: 47
- `figure_png_duplicate_candidates`: 33
- `practice_numeric_without_numeric_solution`: 26
- `few_learning_objectives`: 22
- `introduced_terms_not_found_in_chapter`: 17
- `formula_suspicious_text`: 8
- `figure_description_short`: 7
- `handbook_memorize_claim_unverified`: 6
- `math_delimiter_mismatch`: 5
- `worked_example_missing_solution`: 3

## Recommended review order

1. Resolve CRITICAL and ERROR findings.
2. Replace generic/template worked-example and practice-solution text.
3. Verify every numeric example that lacks a numeric final result or units.
4. Review repeated answer/solution text for copy/template artifacts.
5. Verify Handbook/source claims marked unverified or split_required.
6. Complete missing PNG/SVG artwork pairs, then perform figure engineering QA and update the manifest Status.
7. Manually sample clean chapters for formula/model correctness because automated checks cannot prove engineering validity.

## Important limitation

A PASS from this script means the manuscript passed the implemented technical-content heuristics. It is **not** a certification that every equation, calculation, model assumption, source claim, or figure is technically correct. Final release still requires domain review of formulas, worked examples, practice solutions, and source support.
