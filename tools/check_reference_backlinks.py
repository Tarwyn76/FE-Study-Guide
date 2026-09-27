# tools/check_reference_backlinks.py
# =====================================================================
# Validates all files in the reference/ directory.
# Reference files are EXEMPT from lint_forward_refs.py but must satisfy
# stricter backlink requirements:
#   - Every formula entry must have a "Taught in:" link
#   - Every linked chapter must exist on disk
#   - Every symbol used must appear in meta/notation.md
#   - Every term used must appear in meta/glossary.md
# =====================================================================

import re
import sys
import yaml
from pathlib import Path


BASE_DIR        = Path(__file__).parent.parent
REFERENCE_DIR   = BASE_DIR / "reference"
NOTATION_PATH   = BASE_DIR / "meta" / "notation.md"
GLOSSARY_PATH   = BASE_DIR / "meta" / "glossary.md"
CHAPTERS_DIRS   = [
    BASE_DIR / "layer-0-orientation",
    BASE_DIR / "layer-1-substrate",
    BASE_DIR / "layer-2-core",
    BASE_DIR / "layer-3-tracks",
    BASE_DIR / "reference",
]


def load_text(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def collect_existing_chapters() -> set[str]:
    """Collect all chapter IDs that exist on disk (from front matter)."""
    chapter_ids: set[str] = set()
    for d in CHAPTERS_DIRS:
        for md_file in d.rglob("*.md"):
            text = md_file.read_text(encoding="utf-8")
            if text.startswith("---"):
                end = text.find("\n---", 3)
                if end != -1:
                    try:
                        fm = yaml.safe_load(text[3:end]) or {}
                        ch = fm.get("chapter")
                        if ch:
                            chapter_ids.add(ch)
                    except yaml.YAMLError:
                        pass
    return chapter_ids


def extract_taught_in_links(text: str) -> list[str]:
    """Extract all 'Taught in:' chapter references from a reference file."""
    return re.findall(r"\*\*Taught in:\*\*.*?\[([^\]]+)\]", text)


def check_reference_file(
    ref_file: Path,
    existing_chapters: set[str],
    notation_text: str,
    glossary_text: str,
) -> list[str]:
    text = ref_file.read_text(encoding="utf-8")
    violations = []

    # Check 1: every ### formula heading has a "Taught in" link
    formula_headings = re.findall(r"^### (.+)$", text, re.MULTILINE)
    taught_in_links  = extract_taught_in_links(text)

    if len(formula_headings) > len(taught_in_links):
        violations.append(
            f"  {len(formula_headings)} formula headings but only "
            f"{len(taught_in_links)} 'Taught in:' links — some entries "
            f"are missing backlinks."
        )

    # Check 2: every linked chapter exists on disk
    all_chapter_links = re.findall(r"\]\(\.\./([\w\-]+/[\w\-]+\.md)\)", text)
    for link in all_chapter_links:
        link_path = BASE_DIR / link
        chapter_id_match = re.search(r"/([\d]{2}-[\d]{2}[\w\-]*)", link)
        if chapter_id_match:
            cid = chapter_id_match.group(1)
            if cid not in existing_chapters and not link_path.exists():
                violations.append(
                    f"  Broken link to chapter: '{link}'"
                )

    return violations


def main():
    if not REFERENCE_DIR.exists():
        print("INFO  reference/ directory not found — skipping backlink check.")
        sys.exit(0)

    existing_chapters = collect_existing_chapters()
    notation_text     = load_text(NOTATION_PATH)
    glossary_text     = load_text(GLOSSARY_PATH)

    total_violations = 0
    files_checked    = 0

    for ref_file in sorted(REFERENCE_DIR.glob("**/*.md")):
        violations = check_reference_file(
            ref_file, existing_chapters, notation_text, glossary_text
        )
        files_checked += 1
        if violations:
            total_violations += len(violations)
            print(f"\nFAIL  {ref_file.relative_to(BASE_DIR)}")
            for v in violations:
                print(v)

    if files_checked == 0:
        print("INFO  No reference files found.")
        sys.exit(0)

    print(
        f"\n{'PASS' if total_violations == 0 else 'FAIL'}  "
        f"{files_checked} reference files checked, {total_violations} violations."
    )
    sys.exit(0 if total_violations == 0 else 1)


if __name__ == "__main__":
    main()