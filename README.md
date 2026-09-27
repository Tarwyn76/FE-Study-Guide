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
| Appendices | 12 tier review exams, 14 full practice exams | — |

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