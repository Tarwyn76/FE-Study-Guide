# Verification Batch 01-31 through 01-40

- Chapters: **10**
- Worked examples: **90**
- Verifier candidates: **25**
- Worked examples receiving independent VERIFY metadata: **25**
- Independent numerical checks: **67**
- Curated symbolic/categorical exclusions: **0**
- Strict failures: **0**
- Coverage reviews: **0**

## Corrections discovered

- **01-38 Worked Example 6 — Third Success on Trial 7:** corrected the negative-binomial probability from **0.0973** to **0.0972**. Independent evaluation gives `15(0.30)^3(0.70)^4 = 0.0972405`, which rounds to 0.0972 at four decimal places.
- **01-40 Worked Example 5 — Capability from R-bar:** corrected the lower-side capability index from **2.067** to **2.068**. Independent evaluation gives `(25.02-24.70) / [3(0.12/2.326)] = 2.067555...`, which rounds to 2.068 at three decimal places.

## Curated exclusions

None were required in this batch. All 25 examples classified by the technical-audit-aligned heuristic as requiring numerical results support meaningful independent scalar checks.

## Verifier update

The restricted safe-function set was extended with deterministic standard-library helpers needed by these statistics chapters:

- `ceil` / `floor` for required-sample-size rounding,
- `comb` / `factorial` for discrete probability distributions,
- `min` / `max` for capability-index checks,
- `norm_ppf`, backed by `statistics.NormalDist().inv_cdf`, for independent standard-normal critical-value verification.

No change was made to the technical-audit-aligned candidate-classification logic.

## Verification method

Every VERIFY expression is recomputed from the problem givens and compared with the chapter's stated result under an explicit tolerance. Multi-part examples receive multiple checks. Statistical table values that are inputs to later arithmetic are treated as stated reference constants unless a standard-library independent calculation is available; standard-normal fractiles are independently checked with `norm_ppf`.

## Cumulative compatibility check

After merging the 01-01–01-05, 01-06–01-10, 01-11–01-20, 01-21–01-30, and 01-31–01-40 verification batches under the updated verifier, the cumulative strict gate passes:

- Worked examples: **337**
- Numeric-result candidates: **220**
- Tagged candidates: **199**
- Independent VERIFY checks: **598**
- Curated exclusions: **21**
- Failures: **0**
- Coverage reviews: **0**
