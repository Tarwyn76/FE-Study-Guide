# tools/check_reference_backlinks.py
# =====================================================================
# Validates the CURRENT FE Study Guide reference/back-matter structure.
#
# Current repository architecture:
#   appendices/formula-index.md
#   appendices/notation-master.md
#   appendices/unit-tables.md
#
# Optional publication-source registers:
#   references/References-and-Sources-Master-Index.md
#   references/Core-Curriculum-References-and-Sources-complete.md
#   references/*-Track-References-and-Sources-complete.md
#
# Historical versions of this checker expected a singular reference/
# directory containing formula entries with "**Taught in:**" links.
# That directory is not part of the current repository architecture.
#
# Checks performed:
#   - Required appendix files exist and are non-empty
#   - All technical chapters (01-xx, 02-xx, 03-xx) are represented in
#     formula-index.md by a chapter heading
#   - Formula IDs are unique
#   - Each formula ID's chapter prefix matches the chapter heading it is under
#   - Every referenced chapter ID exists on disk
#   - notation-master.md chapter references point to existing chapters
#   - unit-tables.md chapter references point to existing chapters
#   - Required structural headings exist in notation/unit appendices
#   - If references/ exists, required master/core registers and the seven
#     discipline-track registers are present and non-empty
#
# Exit behavior:
#   0 = PASS
#   1 = validation failure
#   2 = configuration/input error
# =====================================================================

from __future__ import annotations

import re
import sys
import yaml
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

APPENDICES_DIR = BASE_DIR / "appendices"
FORMULA_INDEX = APPENDICES_DIR / "formula-index.md"
NOTATION_MASTER = APPENDICES_DIR / "notation-master.md"
UNIT_TABLES = APPENDICES_DIR / "unit-tables.md"

REFERENCES_DIR = BASE_DIR / "references"

CHAPTER_DIRS = [
    BASE_DIR / "layer-0-orientation",
    BASE_DIR / "layer-1-substrate",
    BASE_DIR / "layer-2-core",
    BASE_DIR / "layer-3-tracks",
]

REQUIRED_APPENDIX_FILES = [
    FORMULA_INDEX,
    NOTATION_MASTER,
    UNIT_TABLES,
]

NOTATION_REQUIRED_HEADINGS = [
    "Handbook alignment",
    "Collision table",
    "Structural conventions",
    "Subscript reservations",
    "Unit presentation",
    "Verified constants",
    "Chapter-local notation cross-reference",
]

UNIT_REQUIRED_HEADINGS = [
    "SI base units",
    "Common SI derived units",
    "Common USCS derived units",
    "Metric prefixes",
    "Landmark conversions",
    "Temperature values and differences",
    "Pound-mass / pound-force relations",
    "Universal gas constant forms",
    "Verified constants used by the notation contract",
]

REFERENCE_REQUIRED_FILES = [
    "References-and-Sources-Master-Index.md",
    "Core-Curriculum-References-and-Sources-complete.md",
    "Chemical-Track-References-and-Sources-complete.md",
    "Civil-Track-References-and-Sources-complete.md",
    "ECE-Track-References-and-Sources-complete.md",
    "Environmental-Track-References-and-Sources-complete.md",
    "Industrial-Systems-Track-References-and-Sources-complete.md",
    "Mechanical-Track-References-and-Sources-complete.md",
    "Other-Disciplines-Track-References-and-Sources-complete.md",
]

CHAPTER_ID_RE = re.compile(r"\b(0[0-3]-\d{2})\b")
TECHNICAL_CHAPTER_ID_RE = re.compile(r"\b(0[1-3]-\d{2})\b")
FORMULA_HEADING_RE = re.compile(r"^###\s+(0[1-3]-\d{2})\s+[—-]\s+.+$", re.MULTILINE)
FORMULA_ID_RE = re.compile(r"\*\*((0[1-3]-\d{2}):F(\d+))\*\*")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_front_matter_chapter(path: Path) -> str | None:
    text = load_text(path)
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        fm = yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return None
    ch = fm.get("chapter")
    return str(ch) if ch else None


def collect_existing_chapters() -> dict[str, Path]:
    chapters: dict[str, Path] = {}
    duplicates: dict[str, list[Path]] = {}

    for directory in CHAPTER_DIRS:
        if not directory.exists():
            continue
        for md in directory.rglob("*.md"):
            ch = parse_front_matter_chapter(md)
            if not ch:
                # Fall back to filename prefix for generated Layer 3 files whose
                # front matter may temporarily be unavailable during development.
                m = re.match(r"^(0[0-3]-\d{2})-", md.name)
                ch = m.group(1) if m else None
            if not ch:
                continue

            if ch in chapters and chapters[ch] != md:
                duplicates.setdefault(ch, [chapters[ch]]).append(md)
            else:
                chapters[ch] = md

    if duplicates:
        lines = ["Duplicate chapter IDs found on disk:"]
        for ch, paths in sorted(duplicates.items()):
            lines.append(f"  {ch}: " + ", ".join(str(p.relative_to(BASE_DIR)) for p in paths))
        raise RuntimeError("\n".join(lines))

    return chapters


def check_required_file(path: Path, violations: list[str]) -> None:
    rel = path.relative_to(BASE_DIR)
    if not path.exists():
        violations.append(f"Missing required file: {rel}")
        return
    if path.stat().st_size == 0:
        violations.append(f"Required file is empty: {rel}")


def check_formula_index(
    path: Path,
    existing: dict[str, Path],
    violations: list[str],
    reviews: list[str],
) -> tuple[int, int]:
    text = load_text(path)
    headings = [(m.group(1), m.start(), m.end()) for m in FORMULA_HEADING_RE.finditer(text)]
    formula_ids = [(m.group(1), m.group(2), int(m.group(3)), m.start()) for m in FORMULA_ID_RE.finditer(text)]

    heading_ids = [h[0] for h in headings]
    heading_set = set(heading_ids)
    technical_existing = {ch for ch in existing if ch.startswith(("01-","02-","03-"))}

    # Every current technical chapter should have an index heading, even if the
    # chapter explicitly states that no reusable formula was selected.
    missing_headings = sorted(technical_existing - heading_set)
    extra_headings = sorted(heading_set - technical_existing)

    for ch in missing_headings:
        violations.append(f"formula-index.md: missing chapter heading for {ch}")
    for ch in extra_headings:
        violations.append(f"formula-index.md: heading references missing chapter {ch}")

    if len(heading_ids) != len(heading_set):
        dupes = sorted(ch for ch in heading_set if heading_ids.count(ch) > 1)
        for ch in dupes:
            violations.append(f"formula-index.md: duplicate chapter heading {ch}")

    seen_formula_ids: set[str] = set()
    for full_id, ch, num, pos in formula_ids:
        if full_id in seen_formula_ids:
            violations.append(f"formula-index.md: duplicate formula ID {full_id}")
        seen_formula_ids.add(full_id)

        # Find the nearest preceding chapter heading.
        current_heading = None
        for hch, hstart, hend in headings:
            if hstart < pos:
                current_heading = hch
            else:
                break

        if current_heading is None:
            violations.append(f"formula-index.md: formula {full_id} appears before any chapter heading")
        elif current_heading != ch:
            violations.append(
                f"formula-index.md: formula {full_id} is under chapter {current_heading}"
            )

        if ch not in existing:
            violations.append(f"formula-index.md: formula {full_id} references missing chapter {ch}")

    # Formula-free chapter headings are allowed but worth reporting.
    formulas_by_chapter: dict[str, int] = {ch: 0 for ch in heading_set}
    for _, ch, _, _ in formula_ids:
        formulas_by_chapter[ch] = formulas_by_chapter.get(ch, 0) + 1
    for ch, count in sorted(formulas_by_chapter.items()):
        if count == 0:
            marker = re.search(
                rf"^###\s+{re.escape(ch)}\s+[—-].*?(?=^###\s+0[1-3]-\d{{2}}\s+[—-]|\Z)",
                text,
                re.MULTILINE | re.DOTALL,
            )
            block = marker.group(0) if marker else ""
            if "No reusable display formula selected" not in block:
                reviews.append(
                    f"formula-index.md: {ch} has no formula entries and no explicit formula-free note"
                )

    return len(headings), len(formula_ids)


def check_chapter_refs_in_table_file(
    path: Path,
    existing: dict[str, Path],
    violations: list[str],
) -> int:
    text = load_text(path)
    refs = set(TECHNICAL_CHAPTER_ID_RE.findall(text))
    for ch in sorted(refs):
        if ch not in existing:
            violations.append(f"{path.name}: references missing chapter {ch}")
    return len(refs)


def check_required_headings(
    path: Path,
    headings: list[str],
    violations: list[str],
) -> None:
    text = load_text(path)
    found = {m.group(1).strip() for m in re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE)}
    for heading in headings:
        if heading not in found:
            violations.append(f"{path.name}: missing required section '## {heading}'")


def check_bibliographic_references(violations: list[str], info: list[str]) -> int:
    if not REFERENCES_DIR.exists():
        info.append(
            "references/ directory not present; bibliographic source-register validation not run."
        )
        return 0

    checked = 0
    for name in REFERENCE_REQUIRED_FILES:
        path = REFERENCES_DIR / name
        checked += 1
        if not path.exists():
            violations.append(f"references/: missing required register {name}")
        elif path.stat().st_size == 0:
            violations.append(f"references/: required register is empty: {name}")

    return checked


def main() -> int:
    violations: list[str] = []
    reviews: list[str] = []
    info: list[str] = []

    try:
        existing = collect_existing_chapters()
    except Exception as exc:
        print(f"ERROR  Could not collect chapters: {exc}")
        return 2

    if not existing:
        print("ERROR  No chapter files found in the expected layer directories.")
        return 2

    for path in REQUIRED_APPENDIX_FILES:
        check_required_file(path, violations)

    formula_heading_count = 0
    formula_count = 0
    notation_ref_count = 0
    unit_ref_count = 0

    if FORMULA_INDEX.exists() and FORMULA_INDEX.stat().st_size:
        formula_heading_count, formula_count = check_formula_index(
            FORMULA_INDEX, existing, violations, reviews
        )

    if NOTATION_MASTER.exists() and NOTATION_MASTER.stat().st_size:
        check_required_headings(NOTATION_MASTER, NOTATION_REQUIRED_HEADINGS, violations)
        notation_ref_count = check_chapter_refs_in_table_file(
            NOTATION_MASTER, existing, violations
        )

    if UNIT_TABLES.exists() and UNIT_TABLES.stat().st_size:
        check_required_headings(UNIT_TABLES, UNIT_REQUIRED_HEADINGS, violations)
        unit_ref_count = check_chapter_refs_in_table_file(
            UNIT_TABLES, existing, violations
        )

    bibliographic_checked = check_bibliographic_references(violations, info)

    for msg in violations:
        print(f"FAIL  {msg}")
    for msg in reviews:
        print(f"REVIEW  {msg}")
    for msg in info:
        print(f"INFO  {msg}")

    technical_chapters = sum(
        1 for ch in existing if ch.startswith(("01-","02-","03-"))
    )

    print()
    print(
        f"{'PASS' if not violations else 'FAIL'}  "
        f"{technical_chapters} technical chapters on disk; "
        f"{formula_heading_count} formula-index chapter headings; "
        f"{formula_count} formula entries; "
        f"{notation_ref_count} notation chapter references; "
        f"{unit_ref_count} unit-table chapter references; "
        f"{bibliographic_checked} bibliographic registers checked; "
        f"{len(violations)} violations; {len(reviews)} reviews."
    )

    return 0 if not violations else 1


if __name__ == "__main__":
    raise SystemExit(main())
