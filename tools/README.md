# FE Guide Validation Tools

Four Python files for the current schema-4 concept ledger and Markdown chapters.
Tested against the supplied ledger containing 100 concepts and the 26 current
chapter files, including unfinished Chapter 01-23. The package adds validators;
it does not replace your project README, edit your chapters, or modify the seven
existing tools.

| File | Purpose |
|---|---|
| `tools/ledger_io.py` | Shared strict YAML loader, prerequisite graph validation, chapter discovery, Markdown helpers, and diagnostic output. |
| `tools/lint_ledger.py` | Concept ownership, transitive prerequisites, chapter declarations, Key Terms, notation registry, figure ownership, and optional manifest/asset checks. |
| `tools/count_assessments.py` | Question and answer inventories, duplicate/missing sections, numbering, answer coverage, and generated ledger count comparison. Optional safe count updates. |
| `tools/lint_style.py` | Chapter anatomy, heading conventions, notation banners, example labels, margin boxes, section citations, and figure alt-text checks. |

## Install and run

Use Python 3.10 or later. The verification environment used Python 3.12.14 and
PyYAML 6.0.3. From this extracted package, install the dependency:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Copy the four files in `tools/` into your guide's `tools/` folder together.
Keep this package README separate from your guide README. If Windows uses the
Python launcher, substitute `py` for `python` in these commands.

The default root is the parent of the scripts' `tools/` directory. Defaults are
`meta/ledger.yaml`, `meta/style-guide.md`, and `meta/notation.md`. Chapters are
discovered recursively in `layer-0-orientation`, `layer-1-substrate`,
`layer-2-core`, and `layer-3-tracks`. Filenames must start with `NN-NN-` and end
with `.md`. Planned ledger chapters may lack files; other chapters may not.

From the guide's project root:

```bash
python tools/lint_ledger.py
python tools/count_assessments.py
python tools/lint_style.py
```

To include a figure manifest, supply its actual path:

```bash
python tools/lint_ledger.py --manifest "meta/figure-manifest.csv"
python tools/lint_ledger.py --manifest "meta/figure-manifest.csv" --check-assets
```

`--check-assets` checks local image targets relative to their chapter files.
It does not download remote images or assess their visual or technical quality.
Without this option, figure IDs and ownership are checked, but image existence
is not. Without `--manifest`, manifest comparison is explicitly reported as
not requested.

## Custom paths and chapter subsets

All relative input paths, including `--chapters` globs, resolve against `--root`.
Use double quotes around paths or globs containing spaces or parentheses.
`--chapters` can be repeated to combine selected files or directories. Selecting
files explicitly is a partial check: it does not certify that all manuscript
chapters are present. Duplicate versions of the same chapter cause an input
error; the tools never guess which version you intended.

These commands reproduce the checks on the supplied flat upload folder. Set
`--root` to the directory containing `upload`:

```bash
python tools/count_assessments.py --root "." --ledger "upload/ledger.yaml" --chapters "upload/*(1).md"
python tools/lint_ledger.py --root "." --ledger "upload/ledger.yaml" --chapters "upload/*(1).md" --notation "upload/notation.md" --manifest "upload/figure-manifest(1).csv"
python tools/lint_style.py --root "." --ledger "upload/ledger.yaml" --chapters "upload/*(1).md" --notation "upload/notation.md" --style-guide "upload/style-guide.md"
```

For only the ledger's structure, graph, and ownership:

```bash
python tools/lint_ledger.py --ledger-only
```

This narrower mode does not check manuscript text, notation.md, or the manifest.

## Count updates

The default is read-only. `review_questions` is the combined total of conceptual,
calculation, and multiple-choice questions. `practice_problems` counts a separate
Practice Problems section only. Subparts are not separate questions.

One concept record per chapter holds its total: the record with
`assessment_scope: chapter_total`, or the first concept ID if no explicit owner
exists and all other records already have zero counts. Ambiguous legacy
allocations are errors. Other records carry zero to prevent double counting.

After reviewing the default report, update generated counts with:

```bash
python tools/count_assessments.py --write
```

The operation refuses all selected changes if any assessment or membership
error remains. Missing answer keys, duplicate sections, bad numbering, mismatched
answers, and ambiguous allocations block writing. You can explicitly select a
valid chapter subset while other chapters remain unfinished.

Only the numeric `review_questions` and `practice_problems` scalars are patched.
Comments, ordering, other fields, UTF-8 BOM, and line endings are preserved. A
timestamped `ledger.yaml.bak.<UTC timestamp>` stores the original bytes. A
temporary file is validated before atomic replacement; a lock and byte checks
detect competing updates. YAML anchors/aliases are accepted for read-only
inspection but refused for writing. A no-change run creates no backup.

Chapter 01-22's current count of 60 is two ambiguous 30-question sets. The tool
reports the sets separately and will not certify or rewrite that chapter total
until the duplicate sections are resolved. Counts do not prove answer
correctness or objective coverage.

## Reports and exit codes

Append `--format json` for complete machine-readable diagnostics and statistics.
Text output shows up to 100 findings; use `--max-findings 0` to show all.

| Exit | Meaning |
|---|---|
| 0 | No errors within the requested scope. Warnings may remain. |
| 1 | Validation findings; also warnings when `--strict` is enabled. |
| 2 | Missing, malformed, unsupported, or unsafe inputs. |

`--strict` is useful for a release gate. The normal ledger-only check currently
passes with warnings for pending decomposition, specification mappings, and
Handbook audits. Whole-manuscript checks currently fail for real source issues;
see `VALIDATION_RESULTS.md` and the detailed JSON reports in `validation/`.
Incomplete chapter metadata remains visible and does not suppress findings.

## Adopt the shared loader in existing scripts

The existing scripts are unchanged. To migrate a script that expects a list of
concept dictionaries, remove its old local `load_ledger` implementation and use:

```python
from ledger_io import InputError, load_ledger

try:
    concepts = load_ledger(ledger_path)
except InputError as exc:
    raise SystemExit(f"Ledger input error: {exc}") from exc

print(f"Loaded {len(concepts)} concepts from ledger.")
```

Keep the importing script beside `ledger_io.py`. A later local function named
`load_ledger` would override the import, so remove that definition too. For
graph-aware code, `read_ledger(path)` returns a Ledger with `.concepts`, `.by_id`,
`.order`, and `.ancestors()`.

The loader reads the `concepts` list under the YAML root, validates schema 4,
rejects duplicate keys/IDs, checks legal IDs and field types, and detects missing
prerequisites and cycles. Missing `notes` is allowed; an empty concepts list is
always an error. It does not mutate the loaded source.

## Supported conventions and limits

- Checks encode the supplied authoring contract. Passing a different style-guide
  file does not automatically compile its prose into new rules.
- Chapter structure uses ATX headings (`##`, `###`). Front matter, fenced code,
  and HTML comments are excluded from prose checks. This is a focused parser
  for the supplied chapter format, not a complete CommonMark renderer.
- Assessments use top-level `1.`, `1)`, or bold-number labels. Number continuously
  across review categories. Indent subparts and wrapped plain-list continuations.
  Separate bold paragraphs and plain lists with a blank line. These conventions
  distinguish real answers from wrapped numeric sentences.
- Review keys may use `Answer Key with Explanations`, `Answers to Review Questions`,
  `Review Answers`, or `Review Question Answers`. Practice keys use
  `Practice Problem Solutions`, `Solutions to Practice Problems`, `Practice Answers`,
  or `Answers to Practice Problems`. Combined review/practice keys must be split
  into these separate sections before automatic count updates.
- Images use the manuscript's inline `![description](path)` convention. Prefer
  simple filenames without parentheses; angle-bracket destinations can contain
  spaces. Reference-style images, HTML images, and complex nested link syntax
  are outside this parser's supported format. Image IDs must appear in the alt
  text or target, with descriptive alt text in addition to an ID.
- Quantity tokens and operator notation remain separate. An actual notation
  registry requires Symbol, Meaning, SI, and USCS columns outside fenced samples.
  An optional Ledger token column can distinguish different quantities that
  share a printed symbol. Units and equations still need technical review.
- Glossary ownership follows the existing strict Key Terms-equals-introductions
  invariant, including explicit aliases. It does not silently permit repeated
  prerequisite terms simply to make the current chapters pass.
- The style guide's conflicting assessment quotas are reported, not arbitrarily
  enforced. The current ledger's combined-review convention controls counts.
  Schema 4 governs metadata instead of the older `memorize: true/false` rule.
- Example checks recognize explicit Given, Find, Approach, Solution, and Check
  labels, including Verify, Units check, and Check numerically. They do not
  recompute the mathematics. Section citations are checked for existence, not
  whether the cited explanation supports a claim.
- These scripts cannot certify NCEES facts, Handbook page accuracy, complete
  specification coverage, every unregistered prose use, objective-to-question
  alignment, or numerical answers. They supplement the existing seven checks;
  the known numerical-verifier defect is not repaired by this package.
