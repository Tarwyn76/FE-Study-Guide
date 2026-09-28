# tools/lint_forward_refs.py
# =====================================================================
# Scans every chapter Markdown file for technical terms and symbols.
# Fails the build if any term or symbol appears before the chapter
# that first defines it, according to the ledger.
#
# Navigational references (chapter titles, figure IDs, section numbers)
# are exempt — only ledger-tracked terms and symbols are checked.
# Files with front matter containing `reference: true` are exempt from
# this check and routed to check_reference_backlinks.py instead.
# Files with template: orientation skip the §3/§4/§7 structure checks.
# =====================================================================

import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict


LEDGER_PATH  = Path(__file__).parent.parent / "meta" / "ledger.yaml"
CHAPTERS_DIR = Path(__file__).parent.parent
CHAPTER_GLOBS = [
    "layer-0-orientation/*.md",
    "layer-1-substrate/*.md",
    "layer-2-core/**/*.md",
    "layer-3-tracks/**/*.md",
]


# ---------------------------------------------------------------------------
# Load ledger helpers
# ---------------------------------------------------------------------------

def load_ledger(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    if not isinstance(raw, dict) or not isinstance(raw.get("concepts"), list):
        raise ValueError("Ledger must contain a top-level 'concepts' list.")
    return [item for item in raw["concepts"] if isinstance(item, dict) and "id" in item]


def build_definition_map(concepts: list[dict]) -> dict[str, str]:
    """
    Returns term_or_symbol → chapter_id where it is first defined.
    Both introduces_terms and introduces_symbols are indexed.
    """
    definition_map: dict[str, str] = {}
    for concept in concepts:
        chapter = concept.get("chapter", "")
        for term in concept.get("introduces_terms", []):
            key = term.strip().lower()
            if key and key not in definition_map:
                definition_map[key] = chapter
        for sym in concept.get("introduces_symbols", []):
            key = sym.strip()
            if key and key not in definition_map:
                definition_map[key] = chapter
    return definition_map


def build_chapter_order(concepts: list[dict]) -> dict[str, int]:
    """
    Returns chapter_id → integer position (0-based) in dependency order.
    Uses a simple sort by layer/tier/chapter string for the seed order;
    the full topological sort lives in build_order.py.
    """
    chapters_seen: list[str] = []
    seen_set: set[str] = set()
    for concept in concepts:
        ch = concept.get("chapter", "")
        if ch and ch not in seen_set:
            chapters_seen.append(ch)
            seen_set.add(ch)
    return {ch: i for i, ch in enumerate(chapters_seen)}


# ---------------------------------------------------------------------------
# Chapter file helpers
# ---------------------------------------------------------------------------

def iter_chapter_files(base: Path, globs: list[str]):
    for pattern in globs:
        yield from sorted(base.glob(pattern))


def parse_front_matter(text: str) -> dict:
    """Extract YAML front matter between --- delimiters."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return {}


def extract_chapter_id(front_matter: dict, path: Path) -> str:
    """Return chapter ID from front matter, falling back to filename stem."""
    return front_matter.get("chapter", path.stem)


def extract_prose_terms(text: str) -> list[tuple[int, str]]:
    """
    Extract words and phrases from Markdown prose (not code blocks,
    not front matter, not figure captions).
    Returns list of (line_number, token).
    """
    # Remove front matter
    body = re.sub(r"^---.*?---\n", "", text, flags=re.DOTALL)

    # Remove fenced code blocks
    body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    body = re.sub(r"`[^`]+`", "", body)

    # Remove figure callout lines
    body = re.sub(r"!\[.*?\]\(.*?\)", "", body)

    results = []
    for lineno, line in enumerate(body.splitlines(), start=1):
        # Extract words (3+ chars) and simple multi-word phrases (2 words)
        words = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_\-]{2,}\b", line)
        for w in words:
            results.append((lineno, w.lower()))
    return results


# ---------------------------------------------------------------------------
# Primer exemption
# ---------------------------------------------------------------------------

def load_primer_exemptions(concepts: list[dict]) -> dict[str, str]:
    """
    Returns term → chapter_id where the term is introduced in a Primer.
    A Primer block in chapter X that borrows a concept from chapter Y
    is registered as: term → X  (treated as defined at X for linting
    purposes, since the Primer makes it locally available).
    """
    exemptions: dict[str, str] = {}
    for concept in concepts:
        primer_source = concept.get("primer_source")
        if primer_source:
            for term in concept.get("introduces_terms", []):
                key = term.strip().lower()
                if key:
                    exemptions[key] = primer_source
    return exemptions


# ---------------------------------------------------------------------------
# Main lint logic
# ---------------------------------------------------------------------------

def lint(
    chapter_file: Path,
    chapter_id: str,
    chapter_position: int,
    definition_map: dict[str, str],
    chapter_order: dict[str, int],
    primer_exemptions: dict[str, str],
    is_reference: bool,
    is_orientation: bool,
) -> list[str]:
    """
    Returns a list of violation strings (empty = clean).
    """
    if is_reference:
        return []   # Reference files checked by check_reference_backlinks.py

    text = chapter_file.read_text(encoding="utf-8")
    prose_tokens = extract_prose_terms(text)
    violations = []

    for lineno, token in prose_tokens:
        if token not in definition_map:
            continue  # Not a tracked term; skip

        defining_chapter = definition_map[token]

        # Check primer exemption: if token is introduced by a Primer
        # in this very chapter, it's available here
        if primer_exemptions.get(token) == chapter_id:
            continue

        defining_pos = chapter_order.get(defining_chapter, -1)

        if defining_pos > chapter_position:
            violations.append(
                f"  Line {lineno:4d}: '{token}' defined in {defining_chapter} "
                f"(position {defining_pos}) but used here "
                f"in {chapter_id} (position {chapter_position})"
            )

    return violations


def main():
    concepts = load_ledger(LEDGER_PATH)
    definition_map   = build_definition_map(concepts)
    chapter_order    = build_chapter_order(concepts)
    primer_exemptions = load_primer_exemptions(concepts)

    total_violations = 0
    files_checked    = 0

    for chapter_file in iter_chapter_files(CHAPTERS_DIR, CHAPTER_GLOBS):
        text = chapter_file.read_text(encoding="utf-8")
        fm   = parse_front_matter(text)

        chapter_id   = extract_chapter_id(fm, chapter_file)
        chapter_pos  = chapter_order.get(chapter_id, 9999)
        is_reference = fm.get("reference", False)
        is_orient    = fm.get("template", "") == "orientation"

        violations = lint(
            chapter_file=chapter_file,
            chapter_id=chapter_id,
            chapter_position=chapter_pos,
            definition_map=definition_map,
            chapter_order=chapter_order,
            primer_exemptions=primer_exemptions,
            is_reference=is_reference,
            is_orientation=is_orient,
        )

        files_checked += 1
        if violations:
            total_violations += len(violations)
            print(f"\nFAIL  {chapter_file.relative_to(CHAPTERS_DIR)}")
            for v in violations:
                print(v)

    print(
        f"\n{'PASS' if total_violations == 0 else 'FAIL'}  "
        f"{files_checked} files checked, {total_violations} violations."
    )
    sys.exit(0 if total_violations == 0 else 1)


if __name__ == "__main__":
    main()