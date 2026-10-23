# FE Exam Study Guide

A from-scratch study guide for the NCEES Fundamentals of Engineering exam,
covering all seven discipline-specific exams.

## Design constraints

1. **Zero forward references.** No concept is used before it is taught.
   Enforced by `tools/lint_forward_refs.py`, not by good intentions.
2. **Assumes high school mathematics only.** No prior college coursework.
3. **Skippable but complete.** Every chapter exists for every reader.
   Off-route chapters are visibly marked optional and declare their
   prerequisites so curiosity-driven reading works.

## Structure

| Part | Contents | Chapters |
|------|----------|----------|
| Layer 0 | Orientation, exam format, Handbook navigation | 3 |
| Layer 1 | Mathematical substrate | 41 |
| Layer 2 | Core engineering science, six tiers | 70 |
| Layer 3 | Seven discipline tracks | ~100 |
| Reference | Consolidated formula, symbol, and term lookup | 15 |
| Appendices | 10 tier review exams, 14 full practice exams | — |

## Start here

New readers: [`layer-0-orientation/00-01-how-to-use-this-guide.md`](layer-0-orientation/00-01-how-to-use-this-guide.md)

Choose your reading path: [`routes/`](routes/)

## Source references

- NCEES FE CBT Exam Specifications, effective July 2020 examinations
  (all seven disciplines)
- NCEES *FE Reference Handbook* 10.6, eighth printing, April 2026

> **Verification note.** Exam logistics figures and Handbook page references
> in this guide are drawn from the sources above. Both are revised
> periodically. Before any release, re-verify against current NCEES
> publications. See `meta/verification-log.md`.

## Building and validating

```bash
python tools/build_order.py          # topologically sort ledger → chapter numbers
python tools/lint_forward_refs.py    # fail on any concept used before taught
python tools/check_coverage.py       # every NCEES spec line has a chapter
python tools/check_item_prereqs.py   # every exam item is route-legal
python tools/check_reference_backlinks.py
python tools/check_exam_blueprints.py
python tools/verify_examples.py      # recompute every numeric answer
```

All seven must pass before a chapter is considered done.

## Exam set

The current tier structure contains **10 tiers**: four in Layer 1 (1A–1D) and six in Layer 2 (2A–2F). The guide therefore contains **24 major exams** when complete:

- **10 tier review exams** — one after each tier, 20–45 questions each.
- **14 full practice exams** — Version A and Version B for each of the seven FE disciplines, 110 questions each.

Full practice exams use the current NCEES FE timing model: a **5 hour 55 minute appointment**, including a 2-minute nondisclosure agreement, 8-minute tutorial, **5 hours 20 minutes of exam working time**, and a 25-minute scheduled break.

Blueprints live in:

- `meta/tier-review-blueprints.yaml`
- `meta/exam-blueprints.yaml`
- `meta/fe-exam-specification-ranges.yaml`

Run both blueprint checks before authoring or releasing exam items:

```bash
python tools/check_tier_review_blueprints.py
python tools/check_exam_blueprints.py
```
