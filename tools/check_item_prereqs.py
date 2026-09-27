# tools/check_item_prereqs.py
# =====================================================================
# Validates that every question in every quiz, tier review exam, and
# practice exam only requires concepts that are on the discipline's
# route up to and including the chapter being tested.
#
# Each exam/quiz file is expected to contain front matter with:
#   exam_type: test-out | tier-review | practice-A | practice-B
#   discipline: chemical | civil | electrical | environmental |
#               industrial | mechanical | other
#   covers_through_chapter: "02-44"   # last chapter in scope
#   items:
#     - id: Q001
#       requires_concepts: [MATH-1A-002-03, MECH-2C-022-03]
#
# The script fails if any required concept is not in scope.
# =====================================================================

import sys
import yaml
from pathlib import Path


LEDGER_PATH = Path(__file__).parent.parent / "meta" / "ledger.yaml"
EXAM_GLOBS  = [
    "appendices/review-exams/**/*.yaml",
    "appendices/practice-exams/**/*.yaml",
    "appendices/test-out-quizzes/**/*.yaml",
]
BASE_DIR = Path(__file__).parent.parent


def load_ledger(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return [item for item in raw if isinstance(item, dict) and "id" in item]


def build_chapter_position_map(concepts: list[dict]) -> dict[str, int]:
    """chapter_id → integer position based on ledger order."""
    seen: list[str] = []
    seen_set: set[str] = set()
    for c in concepts:
        ch = c.get("chapter", "")
        if ch and ch not in seen_set:
            seen.append(ch)
            seen_set.add(ch)
    return {ch: i for i, ch in enumerate(seen)}


def build_concept_chapter_map(concepts: list[dict]) -> dict[str, str]:
    """concept_id → chapter_id."""
    return {c["id"]: c.get("chapter", "") for c in concepts}


def iter_exam_files(base: Path, globs: list[str]):
    for pattern in globs:
        yield from sorted(base.glob(pattern))


def check_exam_file(
    exam_file: Path,
    concept_chapter_map: dict[str, str],
    chapter_position_map: dict[str, int],
) -> list[str]:
    with exam_file.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not data or "items" not in data:
        return []

    through_chapter    = data.get("covers_through_chapter", "")
    through_position   = chapter_position_map.get(through_chapter, 9999)
    violations = []

    for item in data.get("items", []):
        item_id  = item.get("id", "?")
        requires = item.get("requires_concepts", [])
        for concept_id in requires:
            chapter = concept_chapter_map.get(concept_id)
            if chapter is None:
                violations.append(
                    f"  {item_id}: concept '{concept_id}' not in ledger"
                )
                continue
            pos = chapter_position_map.get(chapter, 9999)
            if pos > through_position:
                violations.append(
                    f"  {item_id}: concept '{concept_id}' (chapter {chapter}, "
                    f"pos {pos}) is beyond exam scope through {through_chapter} "
                    f"(pos {through_position})"
                )

    return violations


def main():
    concepts           = load_ledger(LEDGER_PATH)
    chapter_position_map = build_chapter_position_map(concepts)
    concept_chapter_map  = build_concept_chapter_map(concepts)

    total_violations = 0
    files_checked    = 0

    for exam_file in iter_exam_files(BASE_DIR, EXAM_GLOBS):
        violations = check_exam_file(
            exam_file, concept_chapter_map, chapter_position_map
        )
        files_checked += 1
        if violations:
            total_violations += len(violations)
            print(f"\nFAIL  {exam_file.relative_to(BASE_DIR)}")
            for v in violations:
                print(v)

    if files_checked == 0:
        print("INFO  No exam files found — skipping prerequisite check.")
        sys.exit(0)

    print(
        f"\n{'PASS' if total_violations == 0 else 'FAIL'}  "
        f"{files_checked} exam files checked, {total_violations} violations."
    )
    sys.exit(0 if total_violations == 0 else 1)


if __name__ == "__main__":
    main()