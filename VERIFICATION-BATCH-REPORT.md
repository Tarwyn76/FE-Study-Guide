# Verification Batch Report — Front Matter 00-01 through 00-03

## Scope

- 00-01 — How to Use This Guide
- 00-02 — The Exam and the CBT Format
- 00-03 — Navigating the FE Reference Book

These are the remaining unique numbered chapter IDs in the project library after verification of the 01-, 02-, and available 03-series chapter files.

## Standalone result

- Worked examples: **3**
- Numeric-result candidates: **2**
- Tagged numeric candidates: **1**
- Independent VERIFY checks: **4**
- Curated exclusions: **1**
- Failures: **0**
- Coverage reviews: **0**
- Chapter corrections: **0**

### 00-02 Worked Example 1 checks

The hypothetical pacing example was independently checked for:

- 5 h 20 min = **320 min**
- 320 / 110 = **2.91 min/question** to the displayed precision
- the same average is **2 min 55 s/question** to the nearest second
- four equal time checkpoints are **80 min** apart

All stated values are consistent.

### Curated exclusion

**00-03 Worked Example 2 — When the Answer Is a Table** is classified by the aligned heuristic as numeric because the prompt contains `10^-12` and the word “Find.” Its actual answer is a categorical table lookup: `10^-12` corresponds to the SI prefix **pico**, symbol **p**. A numeric expression cannot independently validate the prefix name, so this candidate is explicitly excluded rather than given a meaningless scalar self-check.

## Cumulative gate — all unique numbered chapters

- Unique numbered chapter IDs: **135**
- Worked examples: **1,127**
- Numeric-result candidates: **539**
- Tagged numeric candidates: **515**
- Independent VERIFY checks: **992**
- VERIFY checks on non-required examples: **22**
- Curated exclusions: **24**
- Failures: **0**
- Coverage reviews: **0**

This cumulative run includes Layer 0 explicitly and normalizes the differing internal layouts of the earlier batch archives before running the strict verifier.

## Corrections

No arithmetic or rounding corrections were required in this batch.
