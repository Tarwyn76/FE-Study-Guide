# Validation results — September 29, 2026

The four new tools are implemented. All **33 regression tests passed** using
temporary projects. They cover strict loading, dependency validation, question
parsing, answer coverage, duplicate sections, count-update refusal, byte-preserving
updates, backups, competing edits, ownership, style checks, and CLI exit codes.

The tools were also run against the current supplied ledger, 26 current chapter
files, style guide, notation contract, and figure manifest. Input SHA-256 values
were checked before and after: the source files were unchanged. Tests of writing
used temporary fixtures only.

## Results on the supplied guide

| Check | Result | Errors | Warnings |
|---|---|---:|---:|
| Ledger-only ownership and dependency checks | Pass with warnings | 0 | 3 |
| Assessment counts and key structure | Fail: source issues | 2 | 0 |
| Ledger/manuscript/notation/manifest agreement | Fail: source issues | 63 | 11 |
| Mechanical style conventions | Fail: source issues | 250 | 28 |

These are diagnostic counts, not numbers of defective chapters or independent
editorial repairs. For example, one missing notation registry produces one
finding covering many quantities. Passing the tool regression tests does not
mean the manuscript is ready for release.

The loader reads **100 concepts** across 29 chapter IDs, including the three
planned Layer 2 seeds. It validates 204 prerequisite edges. The ledger has 481
unique introduced terms, 89 quantities, 77 notation tokens, and 120 figure IDs.
All 120 supplied inline figure IDs have owners.

## Assessment findings

| Chapter | Review question sets | Answer entries | Finding |
|---|---:|---:|---|
| 01-17 | 31 | 31 | Counts agree |
| 01-18 | 32 | 32 | Wrapped “4. Choice D…” sentence is excluded |
| 01-19 | 27 | 27 | Counts agree |
| 01-20 | 42 | 42 | Counts agree |
| 01-21 | 31 | 0 | Missing answer key |
| 01-22 | 30 + 30 | 30 | Duplicate review sections; count update blocked |
| 01-23 | 27 | 27 | Count structure agrees; chapter remains unfinished |

Across all 26 files there are 742 question occurrences and 681 answer entries.
The difference reflects the missing 31 answers in 01-21 and the additional
30-question set in 01-22. No unambiguous chapter total requires updating. The
tool does not establish which questions an answer explains by meaning.

## Other findings

- The seven 01-23 figures are absent from the 113-row manifest. Eight 01-18
  manifest entries have blank placement sections.
- The actual quantity registry is missing from notation.md; its fenced sample
  banner does not satisfy the registry requirement.
- Glossary checks flag 37 rows repeating prerequisite terms, two unregistered
  labels, 15 chapter-level missing-introduction findings, and 01-22's duplicate
  Key Terms section. These preserve the ledger's stated invariant.
- The ledger-only warnings cover 45 concepts awaiting decomposition, 84 Layer 1
  concepts without official specification mappings, and pending Handbook checks.
- Style checks examined 193 worked examples and found 181 lacking one or more
  required labels. Further findings cover 21 notation banners without the required
  SI/USCS columns, 12 missing collision notes, 11 margin-box format issues,
  10 unresolved bare section citations, nine nonstandard headings, three missing
  sections, two duplicate headings, and one preview-note format issue.
- Twenty-six filename warnings reflect the uploaded names, including `(1)`
  suffixes and capitalization. The remaining two style warnings describe the
  conflicting assessment quotas and the legacy metadata instruction.

The run used explicit chapter selection to exclude old uploaded versions. Missing
chapters outside that selection were therefore not certified. Image files were
not checked: rerun with `--check-assets` in the complete project. Neither source
facts nor mathematical answer correctness were certified.

Detailed file/line diagnostics and inventories are in `validation/*.json`.
`validation/test_results.txt` records the regression-test run, and
`validation/input_sha256.json` identifies the source snapshot. Reproduction
commands and scope limitations are in the package README.
