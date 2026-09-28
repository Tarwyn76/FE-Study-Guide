# FE Supplemental Guide — Updated Validation Report

**Date:** September 28, 2026 (UTC)  
**New material:** Chapters 01-17 through 01-23  
**Overall supplied manuscript:** 26 chapters: 00-01–00-03 and 01-01–01-23  
**Scope:** Read-only validation. Chapter 01-23 is explicitly treated as unfinished.

## Overall result

The newly supplied chapters are not yet integrated into the concept ledger. All 40 concept IDs declared in their front matter are absent from `ledger.yaml`. The current ledger still contains 60 concepts across 22 chapter IDs, including three Layer 2 seed chapters outside the supplied manuscript.

The most immediate manuscript defects are the missing answer key in Chapter 01-21 and the two competing question sets in Chapter 01-22. The available validators do not reliably identify either defect. A successful script exit currently does not establish that a chapter satisfies the README's release requirements.

No chapter, ledger, manifest, or validation-tool source was changed during this audit. Source-file hashes were checked before and after the diagnostic runs.

## Chapter-by-chapter results

Question counts refer to top-level numbered questions, including conceptual, calculation, and multiple-choice questions. Subparts do not count separately. Answer counts establish numbered coverage, not correctness of every answer.

| Chapter | Declared IDs missing from ledger | Inline figures / manifest records | Review questions | Numbered answers | Main finding |
|---|---:|---:|---:|---:|---|
| 01-17 — The Derivative | 5 | 5 / 5 | 31 | 31 | Core chapter sections and answer numbering are present; concept registration and a local teaching-order correction remain. |
| 01-18 — Applications of the Derivative | 5 | 8 / 8 | 32 | 32 | All eight figure records lack placement sections; closing paragraph points to the wrong chapter for the fundamental theorem. |
| 01-19 — Antiderivatives and the Definite Integral | 5 | 6 / 6 | 27 | 27 | Required content sections largely present; closing heading and next-chapter link need standardization. |
| 01-20 — Applications of the Definite Integral | 6 | 8 / 8 | 42 | 42 | Core sections and answer numbering present; chapter closing uses a different heading. |
| 01-21 — Techniques of Integration | 6 | 6 / 6 | 31 | 0 | Missing answer key; next-chapter link incorrectly identifies 01-22 as partial derivatives. |
| 01-22 — Infinite Series and Taylor Expansions | 6 | 6 / 6 | 30 + 30 | 30 | Duplicate Key Terms and Review Questions sections; one key covers the second question set only. |
| 01-23 — Partial Derivatives and Vector Calculus — unfinished | 7 | 7 / 0 | 27 | 27 | Draft has a substantial structure and answer set; all seven concepts and figures remain unregistered. |
| **Total** | **40** | **46 / 39** | **250 numbered occurrences** | **189** | **61 question occurrences lack a corresponding key: 31 in 01-21 and the first 30 in 01-22.** |

The answer text in 01-18 also contains a wrapped sentence beginning `4. Choice D...` inside answer 28. A simple numbered-line counter returns 33; there are actually 32 answer entries. Assessment automation must distinguish answer labels from line-wrapped prose.

## Ledger integration

The missing IDs are:

| Chapter | Missing ID range |
|---|---|
| 01-17 | `MATH-1C-017-01` through `MATH-1C-017-05` |
| 01-18 | `MATH-1C-018-01` through `MATH-1C-018-05` |
| 01-19 | `MATH-1C-019-01` through `MATH-1C-019-05` |
| 01-20 | `MATH-1C-020-01` through `MATH-1C-020-06` |
| 01-21 | `MATH-1C-021-01` through `MATH-1C-021-06` |
| 01-22 | `MATH-1C-022-01` through `MATH-1C-022-06` |
| 01-23 — unfinished | `MATH-1C-023-01` through `MATH-1C-023-07` |

Consequences:

- None of the seven new chapters appears in the generated reading order.
- Their prerequisites, term ownership, notation ownership, assessment counts, and specification mappings cannot be validated against the ledger.
- None of their 46 figure IDs has a concept owner.
- The new chapters have valid YAML front matter, consistent chapter-number/tier ID patterns, and `status: drafted`. These syntactic checks do not establish substantive ledger coverage.

Across all 26 supplied chapters, front matter declares 97 distinct concept IDs. Of these, 57 exist in the ledger and 40 do not. The other three existing ledger records belong to Chapters 02-22–02-24, which were not supplied. Those seed chapters are outside this manuscript-upload scope, rather than missing chapters in the new batch.

## Figures and manifest

The current manifest has 113 unique figure records, all with eight CSV fields. The earlier mixed-width CSV problem is resolved. All 39 figures referenced in 01-17–01-22 have corresponding manifest IDs, with no duplicate IDs in this batch.

Remaining issues:

1. **Chapter 01-23:** `FIG-01-23-001` through `FIG-01-23-007` have descriptive inline references but no manifest rows or ledger owners. This is part of the unfinished chapter's integration work.
2. **Chapter 01-18:** all eight manifest `Section` cells are blank. The new chapter now supplies the evidence needed to populate them:

   | Figure | Current chapter placement |
   |---|---|
   | FIG-01-18-001 | §18.1 — Mean Value Theorem |
   | FIG-01-18-002 | §18.2 — Critical points |
   | FIG-01-18-003 | §18.2 — First derivative test/sign chart |
   | FIG-01-18-004 | §18.3 — Concavity and inflection points |
   | FIG-01-18-005 | §18.5 — Curve sketching |
   | FIG-01-18-006 | §18.6 — Optimization |
   | FIG-01-18-007 | §18.7 — Related rates |
   | FIG-01-18-008 | §18.9 — Linear approximation/differentials |

3. **Metadata consistency:** 58 manifest rows have no priority. Status values include `Needed`, `Drafted`, `drafted`, and `specified`. These need an agreed vocabulary and a rule for optional versus required priority values; no missing priorities were silently filled during this audit.
4. **Image availability:** no image files for the 46 newly referenced figure IDs were found in the supplied/generated figure directories available for this audit. Their IDs, alt text, and placement references can be checked; the rendered images and visual accuracy cannot yet be certified. This does not establish whether additional assets exist in the user's full project elsewhere.

Across the complete 26-chapter snapshot there are **120 distinct inline figure IDs**, **113 manifest IDs**, and **74 concept-owned figure IDs**. The seven manifest omissions are all in 01-23; the 46 ownership omissions are all in 01-17–01-23.

## Confirmed manuscript issues

### Chapter 01-17

- §17.6 differentiates a nested sine expression before §17.7 teaches the sine derivative. The text explicitly says the trig derivatives come later. Under the guide's zero-forward-reference rule, move this application after the trig derivative is taught, or introduce the required derivative before using it. A notice that teaching comes later does not supply the prerequisite.
- The derivation in §17.7 cites bare `§16.8`. The ledger's cross-chapter citation convention requires `01-16 §16.8`.
- Worked Example 1's margin points readers to rules in `§17.4 onward`, but §17.4 covers differentiability; the basic rules begin in §17.5.

### Chapter 01-18

- The final sentence says the inverse relationship between differentiation and integration is proved in Chapter 01-21. The supplied manuscript develops the fundamental theorem in **01-19 §19.5**. Update that handoff.
- The 32 question labels have corresponding answer labels. The extra apparent `4.` in answer 28 is prose, not a thirty-third answer.

### Chapter 01-19

- The closing section is `Where We Go From Here`, rather than the prescribed `What's Next`. Its content exists, so this is a heading-standardization issue.
- Its next link targets `01-20-applications-of-integration.md`, which does not match the supplied Chapter 01-20 filename. Final repository filenames and links need reconciliation.
- Worked Example 10 is titled “Volume Delivered from a Flow Rate,” but the input is a level rate in m/min and the result is a level rise in metres. The body correctly explains that result; the title should describe level rise unless a tank area and volumetric calculation are added.

### Chapter 01-20

- The closing section is `Looking Ahead`, rather than `What's Next`.
- The 42 questions have corresponding answer labels. This audit does not claim to have independently solved all 42 questions.

### Chapter 01-21

- The chapter goes directly from question 31 to `Summary Card`. There is no answer-key section under either the standard or an alternative heading. All 31 questions need answers and explanations.
- `Summary Card` serves as a quick-reference section, but differs from the prescribed heading.
- The final link reads “Chapter 01-22 — Partial Derivatives and Multivariable Calculus” and targets `01-22-partial-derivatives.md`. The actual 01-22 is **Infinite Series and Taylor Expansions**; partial derivatives are in **01-23**.

### Chapter 01-22

- Two `Key Terms` sections and two `Review Questions` sections are present. Both question sets run from 1 to 30, but contain different questions and numerical inputs.
- The single `Answers to Review Questions` section matches the **second** set. For example, first-set question 3 asks for the p-series result, while answer 3 discusses what the integral test does and does not provide—the subject of second-set question 3.
- Additional “Where This Goes Wrong” prose appears immediately after question 30 in the first set, before the second Key Terms section. This is evidence of an incomplete merge between chapter versions.
- In §22.7, the generalization is printed as `relative error of 1 − exp(−t/τ) ≈ t ≈ t/(2τ)`. The linear approximation is **1 − exp(−t/τ) ≈ t/τ**, and its leading relative error is **t/(2τ)**. The displayed wording conflates a dimensional time with a dimensionless approximation/error. Rewrite it as two separate statements.
- The file's `(inc)` marker is consistent with these unresolved issues. It should not be treated as finished simply because only 01-23 was explicitly called unfinished in the latest request.

### Chapter 01-23 — work in progress

- The draft already has seven teaching sections, ten named worked examples, 27 questions, and an answer section numbered 1–27.
- Seven concept records and seven figure records must be integrated when the chapter is ready.
- `Answers to Review Questions`, `Summary Card`, and `Looking Ahead` differ from the prescribed heading names, but the corresponding content is present.
- The local notation banner includes partial derivatives, gradient, divergence, curl, and Lagrange multipliers. None can yet be reconciled with concept records because the chapter has no ledger entries.
- Keep this chapter explicitly in the unfinished review scope. This audit does not certify its technical completeness or release readiness.

## Common structure and notation findings

All seven chapters contain Before You Start, On the Board Today, Learning Objectives, Notation Used Here, As the Handbook States It, Where This Goes Wrong, and Key Terms. All have the conceptual/calculation/multiple-choice review organization, although 01-22 duplicates it.

All seven notation tables use **Symbol / Meaning in this chapter / Notes**. The current notation contract specifies **Symbol / Meaning in this chapter / SI / USCS** and calls for generation from ledger fields. The unit columns are therefore absent under the existing contract. For generic mathematical operators, appropriate entries can state “dimensionless,” “depends on the differentiated quantities,” or “not applicable”; unit-bearing application symbols still need explicit treatment.

There are 86 named worked examples in this batch and no `VERIFY` tags. The explicit five-part example format is not consistently followed: all 86 lack the standard `Approach` label. Many do contain useful checks under labels such as “Check numerically,” “Units check,” or “Verify,” so an exact-label search must not be misreported as absence of all verification prose.

The style guide also contains conflicting assessment conventions: one section prescribes three categories of review questions, while another prescribes separate conceptual review and practice-problem sections. The ledger's current assessment definitions follow the combined review-question total. Resolve that documentation conflict before using it as a strict structural gate.

Handbook page claims and official NCEES specification assignments were not independently verified against their primary publications in this audit. The available files do not include the Handbook PDF or a complete official specification inventory.

## Actual validator results

The unchanged current scripts were run in temporary copies using their expected `tools/`, `meta/`, and chapter-directory layout. One run contained the seven new chapters; a second contained all 26 current supplied chapters. The upload directory itself is flat and is not the repository layout the scripts expect.

| Tool | Observed result | What it establishes |
|---|---|---|
| `build_order.py` | Exit 0; 60 concepts, 22 chapter IDs, no cycle | Only the existing ledger graph was sorted. The seven new chapters were omitted because they have no records. |
| `lint_forward_refs.py` — new batch | Exit 0; “PASS 7 files checked, 0 violations” | **Unreliable pass.** Missing chapters get position 9999; new terms are absent from the definition map. |
| `lint_forward_refs.py` — all supplied chapters | Exit 1; 26 files, 436 reported occurrences | The suite is not clean. These are raw linter findings, not 436 confirmed teaching-order errors. Single-word matching also flags ordinary narrative uses. |
| `check_coverage.py` | Exit 2; 44 existing Layer 1 atoms without `spec_lines` | Existing mappings remain incomplete. The 40 absent new records are not included in that count. |
| `check_item_prereqs.py` | Exit 0 with “No exam files found — skipping” | Exam YAML and route legality were not checked. Markdown chapter review questions are not this tool's input. |
| `check_reference_backlinks.py` | Exit 0 with missing-reference-directory message | Reference-section backlinks were not checked. |
| `check_exam_blueprints.py` | Exit 0 with no-blueprints message | Blueprint totals and allocations were not checked. |
| `verify_examples.py` | Exit 0 with no-VERIFY-tags message | **Zero examples were numerically verified by this tool.** |
| `check_primers.py` | Exit 0 with no-Primer-blocks message | No machine-marked Primer blocks were checked. |

### Remaining tool defects

- The forward-reference linter does not fail when a chapter or its front-matter IDs are absent from the ledger. It uses ledger encounter order rather than the topological order, and it tokenizes individual words rather than matching the many multiword ledger terms. Its apparent pass on this batch is not meaningful proof of the zero-forward-reference requirement.
- The numerical verifier evaluates `result` and then compares against the same field, or assigns the computed result as its own expected answer. Even adding tags would not provide independent answer checking without repairing this logic.
- The current coverage checker counts mappings attached to concepts. It does not load a complete NCEES specification inventory and therefore cannot establish the README's requirement that every official specification line has a chapter. Repeated claims on a specification line may be legitimate many-to-many coverage, rather than duplicates to delete.
- Several tools exit successfully when all relevant input is missing. The release process must distinguish **passed** from **not run / no applicable data**.
- `count_assessments.py`, `lint_ledger.py`, and `lint_style.py` are referenced by the ledger but were not included among the supplied tools. They were not run.

## Correction to the previous repair report

The earlier statement that repairs were complete was too broad. The loader fixes and identifier reconciliation did not establish semantic correctness or a complete validation pass. The current files show:

1. **25 added records remain placeholders.** They have empty introduced-term, symbol, and notation lists. In particular, Chapters 01-14–01-16 cannot satisfy the ledger's Key Terms ownership invariant with those lists empty.
2. **Figure ownership was distributed without matching subject matter.** For example, `FIG-01-02-004` (factor-label conversion) is owned by the temperature-scales atom, while `FIG-01-02-002` (SI derived units) is owned by the factor-label atom. In Chapter 01-14, the cofactor-expansion figure is assigned to the “Matrix Multiplication” atom. Unique ownership alone does not make these assignments correct.
3. **Five of the 13 newly inserted image links do not match the available generated image filenames:**

   | Figure | Inserted filename suffix | Available generated filename suffix |
   |---|---|---|
   | FIG-01-02-001 | `quantity-dimension-unit.png` | `quantity-dimension-unit-pyramid.png` |
   | FIG-01-02-004 | `factor-label-method.png` | `factor-label-flowchart.png` |
   | FIG-01-02-006 | `g-vs-gc.png` | `g-versus-gc.png` |
   | FIG-01-02-007 | `newtons-second-law-unit-systems.png` | `newtons-law-three-systems.png` |
   | FIG-01-02-009 | `temperature-scale-selection.png` | `temperature-selection-flowchart.png` |

   The other eight inserted basenames match available generated assets. Copying the available image set into a `figures/` directory would still leave these five links unresolved unless the links or filenames are corrected. These earlier edits inserted Markdown references; they did not establish a complete, renderable chapter-and-assets package.

These findings were documented, not repaired, during this read-only audit.

## Limited independent numerical spot checks

Independent arithmetic checks of selected examples reproduced:

| Location | Recomputed result |
|---|---|
| 01-19, Worked Example 10 | Level rise 3.890991 m; average level rate 0.324249 m/min, consistent with displayed rounding. |
| 01-21, Worked Example 15 | Peak force 183.9397 N; total impulse 20.0 N·s; fraction delivered by one time constant 26.4241%. |
| 01-22, Worked Example 13 | Level at one minute 0.690832 m; linear approximation error 8.5647%; quadratic approximation error −0.48235%. |

These are limited spot checks. They do not substitute for recomputing all 86 examples or validating every answer key. The confirmed equation wording error in 01-22 remains despite the example's numerical values being consistent.

## Next repair priorities

1. Complete Chapter 01-21's answer key and reconcile Chapter 01-22's duplicate ending before relying on generated assessment totals.
2. Replace placeholder concept content with actual teaching atoms and add the 40 missing records, using the chapter content to assign terms, symbols, prerequisites, and figures. Do not manufacture prerequisites merely to force chapter numbers into order.
3. Add the seven 01-23 figure records, fill 01-18's eight placement sections, and reconcile figure filenames with available image files.
4. Correct the confirmed teaching-order, cross-reference, heading, and equation issues above.
5. Repair validation logic so unregistered chapters fail clearly, absent inputs are not counted as passes, and numerical checks compare independent calculations against stated answers.
6. Populate official specification mappings and verify Handbook references from primary source documents; complete 01-23 before a release-readiness decision.

**Current disposition:** Chapters 01-17–01-20 have substantially complete chapter structures but remain unregistered and unverified. Chapters 01-21 and 01-22 have additional confirmed completion defects. Chapter 01-23 remains explicitly work in progress. The README's all-checks-pass release condition has not been met.
