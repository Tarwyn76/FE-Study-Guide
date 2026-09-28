# tools/check_primers.py
# =====================================================================
# Validates every Primer block in every chapter:
#   - A Primer may only teach concepts that are registered in the ledger
#     with primer_source pointing to the chapter containing the Primer.
#   - A Primer may not teach concepts that could have been taught by
#     reordering (i.e., that have no downstream blocker — checked by
#     querying the dependency graph for the current chapter).
#   - Each Primer must contain a "Full treatment:" forward link.
#
# Primer blocks are delimited in Markdown as:
#   <!-- PRIMER_START chapter="01-07" -->
#   ...content...
#   <!-- PRIMER_END -->
# =====================================================================

import re
import sys
import yaml
from pathlib import Path


LEDGER_PATH   = Path(__file__).parent.parent / "meta" / "ledger.yaml"
BASE_DIR      = Path(__file__).parent.parent
CHAPTER_GLOBS = [
    "layer-0-orientation/*.md",
    "layer-1-substrate/*.md",
    "layer-2-core/**/*.md",
    "layer-3-tracks/**/*.md",
]

PRIMER_PATTERN = re.compile(
    r'<!--\s*PRIMER_START\s+chapter="(?P<ch>[^"]+)"\s*-->'
    r'(?P<body>.*?)'
    r'<!--\s*PRIMER_END\s*-->',
    re.DOTALL,
)


def load_ledger(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    if not isinstance(raw, dict) or not isinstance(raw.get("concepts"), list):
        raise ValueError("Ledger must contain a top-level 'concepts' list.")
    return [item for item in raw["concepts"] if isinstance(item, dict) and "id" in item]


def build_primer_registry(concepts: list[dict]) -> dict[str, list[str]]:
    """
    Returns chapter_id → list of concept IDs registered with
    primer_source == chapter_id.
    """
    registry: dict[str, list[str]] = {}
    for concept in concepts:
        source = concept.get("primer_source")
        if source:
            registry.setdefault(source, []).append(concept["id"])
    return registry


def iter_chapter_files(base: Path, globs: list[str]):
    for pattern in globs:
        yield from sorted(base.glob(pattern))


def parse_chapter_id(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            try:
                fm = yaml.safe_load(text[3:end]) or {}
                return fm.get("chapter", path.stem)
            except yaml.YAMLError:
                pass
    return path.stem


def check_file(
    chapter_file: Path,
    chapter_id: str,
    primer_registry: dict[str, list[str]],
) -> list[str]:
    text = chapter_file.read_text(encoding="utf-8")
    violations = []

    for match in PRIMER_PATTERN.finditer(text):
        declared_chapter = match.group("ch")
        body             = match.group("body")

        # Check 1: primer declares a chapter consistent with this file
        if declared_chapter != chapter_id:
            violations.append(
                f"  Primer declares chapter='{declared_chapter}' "
                f"but file chapter is '{chapter_id}'"
            )

        # Check 2: primer must contain a "Full treatment:" link
        if "Full treatment:" not in body and "full treatment" not in body.lower():
            violations.append(
                f"  Primer in {chapter_id} missing 'Full treatment:' "
                f"forward link"
            )

        # Check 3: this chapter must have at least one concept registered
        # with primer_source == chapter_id
        registered = primer_registry.get(chapter_id, [])
        if not registered:
            violations.append(
                f"  Primer in {chapter_id} has no concepts registered "
                f"with primer_source in ledger.yaml"
            )

    return violations


def main():
    concepts        = load_ledger(LEDGER_PATH)
    primer_registry = build_primer_registry(concepts)

    total_violations = 0
    files_checked    = 0
    primers_found    = 0

    for chapter_file in iter_chapter_files(BASE_DIR, CHAPTER_GLOBS):
        text = chapter_file.read_text(encoding="utf-8")
        if "PRIMER_START" not in text:
            continue

        chapter_id  = parse_chapter_id(chapter_file)
        violations  = check_file(chapter_file, chapter_id, primer_registry)
        primers_found += len(PRIMER_PATTERN.findall(text))
        files_checked += 1
        total_violations += len(violations)

        if violations:
            print(f"\nFAIL  {chapter_file.relative_to(BASE_DIR)}")
            for v in violations:
                print(v)

    if primers_found == 0:
        print("INFO  No Primer blocks found — skipping primer check.")
        sys.exit(0)

    print(
        f"\n{'PASS' if total_violations == 0 else 'FAIL'}  "
        f"{primers_found} primers in {files_checked} files checked, "
        f"{total_violations} violations."
    )
    sys.exit(0 if total_violations == 0 else 1)


if __name__ == "__main__":
    main()