# FE Exam Blueprint Build Report

## Deliverables

- `meta/tier-review-blueprints.yaml` — 10 tier reviews.
- `meta/exam-blueprints.yaml` — 14 discipline practice-exam blueprints (A/B).
- `meta/fe-exam-specification-ranges.yaml` — current NCEES range snapshot used for authoring.
- `tools/check_tier_review_blueprints.py` — new tier-review validator.
- `tools/check_exam_blueprints.py` — validator-compatible full-exam checker.
- `README.updated.md` — corrects 12 tier reviews to 10 and documents the current timing model.
- corrected `00-01-how-to-use-this-guide.md` timing/count language.

## Full practice exam blueprint totals

| Discipline | Exam A | Exam B | Areas |
|---|---:|---:|---:|
| chemical | 110 | 110 | 17 |
| civil | 110 | 110 | 14 |
| electrical-computer | 110 | 110 | 17 |
| environmental | 110 | 110 | 15 |
| industrial-systems | 110 | 110 | 13 |
| mechanical | 110 | 110 | 14 |
| other-disciplines | 110 | 110 | 14 |

All 14 allocations are integer counts, total exactly 110, and lie inside their NCEES published ranges.

## Tier review totals

| Tier | Chapters | Questions | Working time |
|---|---:|---:|---:|
| 1A | 3 | 20 | 40 min |
| 1B | 12 | 32 | 64 min |
| 1C | 12 | 34 | 68 min |
| 1D | 14 | 38 | 76 min |
| 2A | 10 | 30 | 60 min |
| 2B | 11 | 32 | 64 min |
| 2C | 19 | 45 | 90 min |
| 2D | 18 | 45 | 90 min |
| 2E | 7 | 28 | 56 min |
| 2F | 5 | 20 | 40 min |

Tier-review question counts are guide-designed, not NCEES allocations. Every chapter receives at least one item; remaining questions are weighted by audited concept-atom count.

## Next production step

Author the 10 tier-review item sets first, because they exercise the shared Layer 1/2 content and give reusable item-writing/solution conventions. Then author the 14 110-question discipline exams against `meta/exam-blueprints.yaml`. After the exam files exist, complete the seven route maps and attach each route's Practice A/remediation/Practice B checkpoints.