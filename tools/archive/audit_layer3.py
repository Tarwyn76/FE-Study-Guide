#!/usr/bin/env python3
"""
audi_layer3.py
==============

Automated audit utility for the FE Supplemental Guide Layer 3 project.

Primary checks
--------------
1. Chapter/map/frontmatter consistency
2. Ledger integrity and concept ownership
3. Prerequisite existence, chronology, and cycle detection
4. Term/symbol/notation ownership and dependency resolution
5. Figure references vs. figure manifest
6. Review/answer/practice numbering and ledger assessment totals
7. Handbook/source-status consistency
8. FE specification mapping structure and optional exact spec-catalog coverage
9. Reserved chapter protection (03-96 through 03-99)
10. Duplicate chapter/file detection
11. Permission-tolerant scanning for Windows/OneDrive project trees

Outputs
-------
Layer3-Audit-Summary.md
Layer3-Audit-Issues.csv
Layer3-Spec-Coverage.csv
Layer3-Prerequisite-Audit.csv
Layer3-Figure-Audit.csv
Layer3-Handbook-Audit.csv
Layer3-Duplicate-Ownership.csv

Typical usage
-------------
python audit_layer3.py --root C:\\Users\\knigh\\OneDrive\\Documents\\GitHub\\FE-Study-Guide

Explicit files may be supplied when auto-discovery is undesirable:

python audit_layer3.py \
    --root ./FE_Layer3_Master \
    --ledger ./ledger-updated-through-03-95.yaml \
    --manifest ./figure-manifest-updated-through-03-95.csv \
    --map ./Layer-3-Chapter-Map-updated-through-OTH.md \
    --out ./audit-output

Optional exact FE-spec coverage catalog:

python audit_layer3.py --root C:\\Users\\knigh\\OneDrive\\Documents\\GitHub\\FE-Study-Guide --spec-catalog ./layer3-spec-catalog.csv

Supported spec-catalog columns:
discipline,area,item,title,required

`item` may be a letter such as A, B, C or another stable identifier.
`required` defaults to true when omitted.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable, Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


# ---------------------------------------------------------------------------
# Project constants
# ---------------------------------------------------------------------------

LAYER3_MIN = 1
LAYER3_MAX = 95
RESERVED_CHAPTERS = {"03-96", "03-97", "03-98", "03-99"}

# Canonical repository layout from locations.txt.
# All automatic path resolution is anchored to the project root instead of
# recursively searching the entire OneDrive/Git working tree.
NORMALIZED_LAYOUT = {
    "ledger": Path("meta") / "ledger.yaml",
    "manifest": Path("figures") / "figure-manifest.csv",
    "map": Path("layer-3-tracks") / "Layer-3-Chapter-Map.md",
    "layer3_root": Path("layer-3-tracks"),
    "output": Path("tools") / "validation" / "layer3-audit",
}

LAYER3_TRACK_DIRS = {
    "chemical": Path("layer-3-tracks") / "chemical",
    "civil": Path("layer-3-tracks") / "civil",
    "electrical_and_computer": Path("layer-3-tracks") / "electrical",
    "environmental": Path("layer-3-tracks") / "environmental",
    "industrial_and_systems": Path("layer-3-tracks") / "industrial",
    "mechanical": Path("layer-3-tracks") / "mechanical",
    "other_disciplines": Path("layer-3-tracks") / "other",
}

PROJECT_ROOT_MARKERS = (
    Path("meta") / "ledger.yaml",
    Path("figures") / "figure-manifest.csv",
    Path("layer-3-tracks") / "Layer-3-Chapter-Map.md",
)

TRACK_RANGES = {
    "chemical": ("03-01", "03-13"),
    "civil": ("03-14", "03-30"),
    "electrical_and_computer": ("03-31", "03-47"),
    "environmental": ("03-48", "03-61"),
    "industrial_and_systems": ("03-62", "03-75"),
    "mechanical": ("03-76", "03-90"),
    "other_disciplines": ("03-91", "03-95"),
}

TRACK_ALIASES = {
    "che": "chemical",
    "chemical": "chemical",
    "civ": "civil",
    "civil": "civil",
    "ece": "electrical_and_computer",
    "electrical": "electrical_and_computer",
    "electrical_and_computer": "electrical_and_computer",
    "env": "environmental",
    "environmental": "environmental",
    "ind": "industrial_and_systems",
    "industrial": "industrial_and_systems",
    "industrial_and_systems": "industrial_and_systems",
    "mec": "mechanical",
    "mechanical": "mechanical",
    "oth": "other_disciplines",
    "other": "other_disciplines",
    "other_disciplines": "other_disciplines",
}

# Known official FE specification area counts for the tracks whose exact
# specification numbering was established during the Layer 3 build.
# These are used only as a coarse sanity check when no exact spec catalog is
# supplied. They do NOT claim item-level completeness.
EXPECTED_AREA_COUNTS = {
    "electrical_and_computer": 17,
    "environmental": 15,
    "industrial_and_systems": 13,
    "mechanical": 14,
    "other_disciplines": 14,
}

SEVERITY_ORDER = {
    "BLOCKER": 0,
    "ERROR": 1,
    "WARNING": 2,
    "INFO": 3,
}

FIG_RE = re.compile(r"\bFIG-03-\d{2}-\d{3}\b")
CHAPTER_RE = re.compile(r"^03-(\d{2})$")
NUMBERED_LINE_RE = re.compile(r"^\s*(\d+)\.\s+", re.MULTILINE)


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    severity: str
    category: str
    chapter: str = ""
    concept_id: str = ""
    figure_id: str = ""
    file: str = ""
    message: str = ""
    recommendation: str = ""

    def key(self):
        return (
            SEVERITY_ORDER.get(self.severity, 99),
            self.chapter,
            self.category,
            self.concept_id,
            self.figure_id,
            self.file,
            self.message,
        )


@dataclass
class ChapterDoc:
    path: Path
    chapter: str
    title: str
    track: str
    ledger_ids: list[str]
    status: str
    frontmatter: dict[str, Any]
    body: str
    raw: str


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def norm_track(value: Any) -> str:
    if value is None:
        return ""
    s = str(value).strip().lower().replace(" ", "_").replace("&", "and")
    return TRACK_ALIASES.get(s, s)


def chapter_num(ch: str) -> Optional[int]:
    m = CHAPTER_RE.match(str(ch).strip())
    return int(m.group(1)) if m else None


def is_layer3_chapter(ch: str) -> bool:
    n = chapter_num(ch)
    return n is not None and LAYER3_MIN <= n <= LAYER3_MAX


def expected_track_for_chapter(ch: str) -> Optional[str]:
    n = chapter_num(ch)
    if n is None:
        return None
    for track, (lo, hi) in TRACK_RANGES.items():
        if chapter_num(lo) <= n <= chapter_num(hi):
            return track
    return None



def looks_like_project_root(path: Path) -> bool:
    """Return True when the canonical FE project layout is present."""
    try:
        return all((path / marker).exists() for marker in PROJECT_ROOT_MARKERS)
    except (PermissionError, OSError):
        return False


def normalize_project_root(start: Path) -> Path:
    """
    Normalize any path inside the repository to the FE-Study-Guide project root.

    This allows the script to be launched from:
      - the repository root,
      - tools/,
      - layer-3-tracks/,
      - an individual track folder,
      - or another descendant directory.

    No recursive search is performed.
    """
    start = start.expanduser().resolve()

    if start.is_file():
        start = start.parent

    candidates = [start, *start.parents]
    for candidate in candidates:
        if looks_like_project_root(candidate):
            return candidate

    # If the caller explicitly supplied the root but one marker is temporarily
    # unavailable (for example OneDrive hydration), preserve the supplied path
    # so the later canonical-path diagnostics can identify the exact problem.
    return start


def canonical_path(root: Path, key: str) -> Path:
    """Resolve one canonical project material path."""
    return (root / NORMALIZED_LAYOUT[key]).resolve()


def validate_canonical_layout(root: Path) -> list[str]:
    """Return human-readable problems with the canonical repository layout."""
    problems: list[str] = []
    checks = {
        "ledger": canonical_path(root, "ledger"),
        "manifest": canonical_path(root, "manifest"),
        "map": canonical_path(root, "map"),
        "Layer 3 root": canonical_path(root, "layer3_root"),
    }
    for label, path in checks.items():
        try:
            if not path.exists():
                problems.append(f"{label} not found at expected path: {path}")
        except (PermissionError, OSError) as e:
            problems.append(f"{label} is inaccessible at expected path: {path} ({e})")

    for track, rel in LAYER3_TRACK_DIRS.items():
        path = (root / rel).resolve()
        try:
            if not path.is_dir():
                problems.append(f"Layer 3 track folder '{track}' not found at expected path: {path}")
        except (PermissionError, OSError) as e:
            problems.append(f"Layer 3 track folder '{track}' is inaccessible: {path} ({e})")

    return problems


def natural_version_score(path: Path) -> tuple[int, str]:
    """
    Prefer files explicitly updated through the highest chapter number.
    Falls back to lexical path ordering.
    """
    m = re.search(r"through[-_ ](?:03-)?(\d{2})", path.name, re.I)
    if m:
        return int(m.group(1)), str(path)
    m = re.search(r"03-(\d{2})", path.name)
    return (int(m.group(1)) if m else -1), str(path)


def safe_walk_files(root: Path, suffix: Optional[str] = None) -> Iterable[Path]:
    """
    Walk a project tree without aborting on unreadable OneDrive/Git/junction folders.

    os.walk() calls onerror for directories it cannot enter. We intentionally
    continue past those directories so one protected folder does not terminate
    the entire audit.
    """
    def _onerror(err: OSError) -> None:
        print(f"WARNING: skipping inaccessible path during scan: {err.filename} ({err})",
              file=sys.stderr)

    for dirpath, dirnames, filenames in os.walk(
        root,
        topdown=True,
        onerror=_onerror,
        followlinks=False,
    ):
        # Avoid directories that cannot contain authoritative project source
        # but commonly create access/performance problems.
        dirnames[:] = [
            d for d in dirnames
            if d not in {".git", ".github", "__pycache__", ".venv", "venv",
                         "node_modules", ".idea", ".vs"}
        ]
        base = Path(dirpath)
        for name in filenames:
            if suffix is None or name.lower().endswith(suffix.lower()):
                yield base / name


def discover_latest(root: Path, patterns: Iterable[str]) -> Optional[Path]:
    """
    Safely discover the newest matching file without Path.rglob(), which can
    terminate on Windows/OneDrive PermissionError entries.
    """
    import fnmatch

    candidates: list[Path] = []
    pats = list(patterns)
    for path in safe_walk_files(root):
        try:
            if any(fnmatch.fnmatch(path.name, pat) for pat in pats) and path.is_file():
                candidates.append(path)
        except (PermissionError, OSError):
            continue

    if not candidates:
        return None
    return max(candidates, key=natural_version_score)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML mapping at top level: {path}")
    return data


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def parse_frontmatter(path: Path) -> Optional[ChapterDoc]:
    try:
        raw = path.read_text(encoding="utf-8")
    except (PermissionError, OSError, UnicodeError) as e:
        print(f"WARNING: unable to read chapter candidate {path}: {e}", file=sys.stderr)
        return None
    if not raw.startswith("---"):
        return None
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        return None
    if not isinstance(fm, dict):
        return None

    ch = str(fm.get("chapter", "")).strip()
    if not is_layer3_chapter(ch):
        return None

    ledger_ids = fm.get("ledger_ids", [])
    if isinstance(ledger_ids, str):
        ledger_ids = [ledger_ids]
    ledger_ids = [str(x).strip() for x in (ledger_ids or [])]

    return ChapterDoc(
        path=path,
        chapter=ch,
        title=str(fm.get("title", "")).strip(),
        track=norm_track(fm.get("track")),
        ledger_ids=ledger_ids,
        status=str(fm.get("status", "")).strip(),
        frontmatter=fm,
        body=parts[2],
        raw=raw,
    )


def section_between(text: str, start_heading: str, next_headings: list[str]) -> str:
    idx = text.find(start_heading)
    if idx < 0:
        return ""
    start = idx + len(start_heading)
    end = len(text)
    for h in next_headings:
        j = text.find(h, start)
        if j >= 0:
            end = min(end, j)
    return text[start:end]


def numbered_entries(section: str) -> list[int]:
    return [int(x) for x in NUMBERED_LINE_RE.findall(section)]


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def add_issue(
    issues: list[Issue],
    severity: str,
    category: str,
    *,
    chapter: str = "",
    concept_id: str = "",
    figure_id: str = "",
    file: str = "",
    message: str,
    recommendation: str = "",
) -> None:
    issues.append(Issue(
        severity=severity,
        category=category,
        chapter=chapter,
        concept_id=concept_id,
        figure_id=figure_id,
        file=file,
        message=message,
        recommendation=recommendation,
    ))


# ---------------------------------------------------------------------------
# Map parsing
# ---------------------------------------------------------------------------

def parse_map(path: Path) -> dict[str, dict[str, str]]:
    """
    Parse Markdown table rows of the form:
    | 03-31 | Title | Drafted |
    """
    rows: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        ch = cells[0]
        if is_layer3_chapter(ch) or ch in RESERVED_CHAPTERS:
            rows[ch] = {"title": cells[1], "status": cells[2]}
    return rows


# ---------------------------------------------------------------------------
# Chapter discovery
# ---------------------------------------------------------------------------

def discover_chapters(root: Path, issues: list[Issue]) -> tuple[dict[str, ChapterDoc], dict[str, list[Path]]]:
    """
    Discover Layer 3 chapters only inside the seven canonical track folders.

    This deliberately avoids recursive repository-wide scanning. The layout is:
      layer-3-tracks/chemical
      layer-3-tracks/civil
      layer-3-tracks/electrical
      layer-3-tracks/environmental
      layer-3-tracks/industrial
      layer-3-tracks/mechanical
      layer-3-tracks/other
    """
    grouped: dict[str, list[ChapterDoc]] = defaultdict(list)

    for logical_track, rel_dir in LAYER3_TRACK_DIRS.items():
        track_dir = (root / rel_dir).resolve()

        try:
            entries = list(track_dir.iterdir())
        except PermissionError as e:
            add_issue(
                issues, "BLOCKER", "track_directory_permission",
                file=str(track_dir),
                message=f"Cannot read normalized Layer 3 track directory: {e}",
                recommendation="Make the directory locally available in OneDrive and grant the current Windows account read access.",
            )
            continue
        except OSError as e:
            add_issue(
                issues, "BLOCKER", "track_directory_unreadable",
                file=str(track_dir),
                message=f"Cannot read normalized Layer 3 track directory: {e}",
                recommendation="Verify the repository layout and filesystem state.",
            )
            continue

        for path in entries:
            try:
                if not path.is_file() or path.suffix.lower() != ".md":
                    continue
            except (PermissionError, OSError):
                continue

            name = path.name.lower()
            if "generation-report" in name or "chapter-map" in name or "audit" in name:
                continue
            if not re.match(r"^03-\d{2}-", path.name, re.I):
                continue

            doc = parse_frontmatter(path)
            if not doc:
                add_issue(
                    issues, "WARNING", "chapter_frontmatter_unreadable",
                    file=str(path),
                    message="Layer 3 chapter candidate could not be parsed as a chapter with YAML frontmatter.",
                    recommendation="Verify the file begins with valid YAML frontmatter including chapter, title, track, ledger_ids, and status.",
                )
                continue

            expected_track = expected_track_for_chapter(doc.chapter)
            if expected_track and expected_track != logical_track:
                add_issue(
                    issues, "ERROR", "chapter_in_wrong_track_folder",
                    chapter=doc.chapter, file=str(path),
                    message=f"Chapter is physically stored in '{logical_track}' but its chapter number belongs to '{expected_track}'.",
                    recommendation="Move the file to the normalized track folder or correct the chapter number.",
                )

            grouped[doc.chapter].append(doc)

    chosen: dict[str, ChapterDoc] = {}
    duplicates: dict[str, list[Path]] = {}

    for ch, docs in grouped.items():
        docs_sorted = sorted(docs, key=lambda d: natural_version_score(d.path), reverse=True)
        chosen[ch] = docs_sorted[0]
        if len(docs_sorted) > 1:
            duplicates[ch] = [d.path for d in docs_sorted]
            add_issue(
                issues, "WARNING", "chapter_duplicate",
                chapter=ch,
                file=str(docs_sorted[0].path),
                message=f"{len(docs_sorted)} chapter files claim {ch}; audit selected {docs_sorted[0].path.name}.",
                recommendation="Keep exactly one authoritative Markdown file for each Layer 3 chapter in its normalized track folder.",
            )

    return chosen, duplicates


# ---------------------------------------------------------------------------
# Prerequisite graph
# ---------------------------------------------------------------------------

def detect_cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    WHITE, GRAY, BLACK = 0, 1, 2
    state = {n: WHITE for n in graph}
    stack: list[str] = []
    cycles: list[list[str]] = []

    def dfs(node: str):
        state[node] = GRAY
        stack.append(node)
        for nxt in graph.get(node, []):
            if nxt not in graph:
                continue
            if state[nxt] == WHITE:
                dfs(nxt)
            elif state[nxt] == GRAY:
                try:
                    i = stack.index(nxt)
                    cyc = stack[i:] + [nxt]
                    if cyc not in cycles:
                        cycles.append(cyc)
                except ValueError:
                    pass
        stack.pop()
        state[node] = BLACK

    for n in graph:
        if state[n] == WHITE:
            dfs(n)
    return cycles


# ---------------------------------------------------------------------------
# Spec catalog
# ---------------------------------------------------------------------------

def load_spec_catalog(path: Optional[Path]) -> list[dict[str, str]]:
    if not path:
        return []
    suffix = path.suffix.lower()
    if suffix in {".yaml", ".yml"}:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("spec_items", data.get("items", []))
        if not isinstance(data, list):
            raise ValueError("Spec catalog YAML must contain a list or spec_items/items list.")
        out = []
        for row in data:
            if isinstance(row, dict):
                out.append({k: str(v) for k, v in row.items()})
        return out
    _, rows = load_csv(path)
    return rows


def truthy(value: Any) -> bool:
    if value is None or value == "":
        return True
    return str(value).strip().lower() not in {"0", "false", "no", "n"}


# ---------------------------------------------------------------------------
# Audit engine
# ---------------------------------------------------------------------------

def audit(
    root: Path,
    ledger_path: Path,
    manifest_path: Path,
    map_path: Path,
    outdir: Path,
    spec_catalog_path: Optional[Path] = None,
) -> int:
    issues: list[Issue] = []

    ledger = load_yaml(ledger_path)
    concepts = ledger.get("concepts", [])
    if not isinstance(concepts, list):
        raise ValueError("Ledger field 'concepts' must be a list.")

    _, manifest_rows = load_csv(manifest_path)
    map_rows = parse_map(map_path)
    chapters, duplicate_chapter_files = discover_chapters(root, issues)

    # ----- expected chapter coverage
    for n in range(LAYER3_MIN, LAYER3_MAX + 1):
        ch = f"03-{n:02d}"
        if ch not in map_rows:
            add_issue(
                issues, "ERROR", "map_missing_chapter",
                chapter=ch, file=str(map_path),
                message="Layer 3 chapter is missing from the chapter map.",
                recommendation="Restore the chapter row in the Layer 3 map.",
            )
        if ch not in chapters:
            add_issue(
                issues, "BLOCKER", "chapter_missing",
                chapter=ch,
                message="No authoritative Markdown chapter was found.",
                recommendation="Add the missing chapter Markdown file to the master Layer 3 folder.",
            )

    # Reserved slots should not have drafted chapter documents or registered Layer 3 concepts.
    for ch in RESERVED_CHAPTERS:
        if ch in chapters:
            add_issue(
                issues, "WARNING", "reserved_chapter_used",
                chapter=ch, file=str(chapters[ch].path),
                message="Reserved Layer 3 chapter slot has a chapter document.",
                recommendation="Keep 03-96 through 03-99 unused unless a verified gap or approved capstone has been assigned.",
            )

    # ----- ledger indexing
    by_id: dict[str, dict[str, Any]] = {}
    duplicate_ids: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for c in concepts:
        cid = str(c.get("id", "")).strip()
        if not cid:
            add_issue(
                issues, "ERROR", "ledger_missing_id",
                message="A ledger concept has no id.",
                recommendation="Assign a unique concept ID.",
            )
            continue
        if cid in by_id:
            duplicate_ids[cid].append(c)
        else:
            by_id[cid] = c

    for cid, dups in duplicate_ids.items():
        c = by_id[cid]
        add_issue(
            issues, "BLOCKER", "duplicate_concept_id",
            chapter=str(c.get("chapter", "")), concept_id=cid,
            message=f"Concept ID {cid} appears more than once in the ledger.",
            recommendation="Merge or rename duplicate concept registrations so every concept ID is globally unique.",
        )

    # ----- chapter vs map/frontmatter/ledger
    ledger_by_chapter: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for c in concepts:
        ch = str(c.get("chapter", "")).strip()
        if ch:
            ledger_by_chapter[ch].append(c)

    for ch, doc in sorted(chapters.items()):
        if not is_layer3_chapter(ch):
            continue

        expected_track = expected_track_for_chapter(ch)
        map_row = map_rows.get(ch)

        if expected_track and doc.track != expected_track:
            add_issue(
                issues, "ERROR", "track_mismatch",
                chapter=ch, file=str(doc.path),
                message=f"Frontmatter track is '{doc.track}', expected '{expected_track}' from the Layer 3 numbering range.",
                recommendation="Correct the frontmatter track or chapter number.",
            )

        if map_row:
            if doc.title and map_row["title"] and doc.title.strip() != map_row["title"].strip():
                add_issue(
                    issues, "ERROR", "title_mismatch",
                    chapter=ch, file=str(doc.path),
                    message=f"Chapter title differs from map: '{doc.title}' vs '{map_row['title']}'.",
                    recommendation="Choose one canonical title and update the map/frontmatter consistently.",
                )
            if map_row["status"].strip().lower() in {"planned", "reserved"} and doc.status.strip().lower() == "drafted":
                add_issue(
                    issues, "WARNING", "map_status_stale",
                    chapter=ch, file=str(map_path),
                    message=f"Map status is '{map_row['status']}' but chapter frontmatter is drafted.",
                    recommendation="Update the chapter map status.",
                )

        ledger_ids_actual = [str(c.get("id", "")) for c in ledger_by_chapter.get(ch, []) if str(c.get("id", ""))]
        if set(doc.ledger_ids) != set(ledger_ids_actual):
            missing = sorted(set(ledger_ids_actual) - set(doc.ledger_ids))
            extra = sorted(set(doc.ledger_ids) - set(ledger_ids_actual))
            add_issue(
                issues, "ERROR", "ledger_id_mismatch",
                chapter=ch, file=str(doc.path),
                message=f"Frontmatter ledger_ids differ from ledger ownership. Missing in frontmatter={missing}; extra in frontmatter={extra}.",
                recommendation="Synchronize chapter frontmatter ledger_ids with the authoritative ledger.",
            )

        for cid in doc.ledger_ids:
            c = by_id.get(cid)
            if not c:
                add_issue(
                    issues, "BLOCKER", "frontmatter_unknown_concept",
                    chapter=ch, concept_id=cid, file=str(doc.path),
                    message="Frontmatter references a concept ID that does not exist in the ledger.",
                    recommendation="Register the concept or remove/correct the stale ledger_id.",
                )
            elif str(c.get("chapter", "")).strip() != ch:
                add_issue(
                    issues, "ERROR", "concept_wrong_chapter",
                    chapter=ch, concept_id=cid, file=str(doc.path),
                    message=f"Ledger says concept belongs to chapter {c.get('chapter')}.",
                    recommendation="Correct concept ownership or chapter frontmatter.",
                )

        # Assessment numbering
        review = section_between(doc.raw, "## Review Questions", ["## Answer Key", "## Practice Problems"])
        answers = section_between(doc.raw, "## Answer Key with Explanations", ["## Practice Problems"])
        practice = section_between(doc.raw, "## Practice Problems", ["## Practice Problem Solutions"])
        solutions = section_between(doc.raw, "## Practice Problem Solutions", ["## Quick Reference", "## What's Next"])

        review_nums = numbered_entries(review)
        answer_nums = numbered_entries(answers)
        practice_nums = numbered_entries(practice)
        solution_nums = numbered_entries(solutions)

        def check_sequence(label: str, nums: list[int], expected: Optional[int] = None):
            if not nums:
                add_issue(
                    issues, "ERROR", f"{label}_missing",
                    chapter=ch, file=str(doc.path),
                    message=f"No numbered {label.replace('_', ' ')} entries found.",
                    recommendation=f"Restore the {label.replace('_', ' ')} section and numbering.",
                )
                return
            target = list(range(1, max(nums) + 1))
            if nums != target:
                add_issue(
                    issues, "ERROR", f"{label}_numbering",
                    chapter=ch, file=str(doc.path),
                    message=f"{label.replace('_',' ').title()} numbering is not contiguous 1..N: {nums}.",
                    recommendation="Renumber entries contiguously and remove duplicated numbering.",
                )
            if expected is not None and len(nums) != expected:
                add_issue(
                    issues, "ERROR", f"{label}_count",
                    chapter=ch, file=str(doc.path),
                    message=f"Found {len(nums)} {label.replace('_',' ')} entries; ledger expects {expected}.",
                    recommendation="Synchronize chapter assessment count and ledger chapter_total values.",
                )

        chapter_atoms = ledger_by_chapter.get(ch, [])
        review_expected = max([int(c.get("review_questions") or 0) for c in chapter_atoms] or [0]) or None
        practice_expected = max([int(c.get("practice_problems") or 0) for c in chapter_atoms] or [0]) or None

        check_sequence("review_questions", review_nums, review_expected)
        check_sequence("answer_key", answer_nums, review_expected)
        check_sequence("practice_problems", practice_nums, practice_expected)
        check_sequence("practice_solutions", solution_nums, practice_expected)

        if review_nums and answer_nums and len(review_nums) != len(answer_nums):
            add_issue(
                issues, "ERROR", "review_answer_count_mismatch",
                chapter=ch, file=str(doc.path),
                message=f"{len(review_nums)} review questions but {len(answer_nums)} answer entries.",
                recommendation="Provide exactly one numbered answer for every review question.",
            )
        if practice_nums and solution_nums and len(practice_nums) != len(solution_nums):
            add_issue(
                issues, "ERROR", "practice_solution_count_mismatch",
                chapter=ch, file=str(doc.path),
                message=f"{len(practice_nums)} practice problems but {len(solution_nums)} numbered solutions.",
                recommendation="Provide exactly one numbered solution for every practice problem.",
            )

    # ----- prerequisites
    graph: dict[str, list[str]] = {}
    prereq_rows: list[dict[str, Any]] = []
    for cid, c in by_id.items():
        prereqs = [str(x).strip() for x in (c.get("prerequisites") or [])]
        graph[cid] = prereqs
        c_ch = str(c.get("chapter", "")).strip()
        c_num = chapter_num(c_ch)
        for p in prereqs:
            status = "ok"
            detail = ""
            if p not in by_id:
                status = "missing"
                detail = "Prerequisite ID is absent from ledger."
                add_issue(
                    issues, "BLOCKER", "missing_prerequisite",
                    chapter=c_ch, concept_id=cid,
                    message=f"Prerequisite {p} does not exist.",
                    recommendation="Correct the prerequisite ID or register the missing canonical concept.",
                )
            else:
                p_ch = str(by_id[p].get("chapter", "")).strip()
                p_num = chapter_num(p_ch)
                # Within Layer 3, a prerequisite should not come from a later chapter.
                if c_num is not None and p_num is not None and p_num > c_num:
                    status = "forward_reference"
                    detail = f"Prerequisite belongs to later chapter {p_ch}."
                    add_issue(
                        issues, "ERROR", "forward_prerequisite",
                        chapter=c_ch, concept_id=cid,
                        message=f"Prerequisite {p} comes from later chapter {p_ch}.",
                        recommendation="Reverse the dependency, move the concept, or reuse an earlier canonical owner.",
                    )
            prereq_rows.append({
                "concept_id": cid,
                "chapter": c_ch,
                "prerequisite_id": p,
                "status": status,
                "detail": detail,
            })

    cycles = detect_cycles(graph)
    for cyc in cycles:
        add_issue(
            issues, "BLOCKER", "prerequisite_cycle",
            concept_id=cyc[0] if cyc else "",
            message="Prerequisite cycle detected: " + " -> ".join(cyc),
            recommendation="Break the cycle by assigning one canonical owner earlier in the dependency chain.",
        )

    # ----- ownership: terms, symbols, notation
    dup_rows: list[dict[str, Any]] = []
    for field in ("introduces_terms", "introduces_symbols", "introduces_notation"):
        owners: dict[str, list[str]] = defaultdict(list)
        for cid, c in by_id.items():
            for item in c.get(field, []) or []:
                s = str(item).strip()
                if s:
                    owners[s].append(cid)
        for item, ids in owners.items():
            if len(ids) > 1:
                sev = "ERROR" if field == "introduces_terms" else "WARNING"
                add_issue(
                    issues, sev, "duplicate_ownership",
                    concept_id=";".join(ids),
                    message=f"{field} item '{item}' has multiple owners: {ids}.",
                    recommendation="Keep one canonical owner and convert later occurrences to uses_* dependencies or aliases.",
                )
                dup_rows.append({
                    "ownership_type": field,
                    "item": item,
                    "owner_count": len(ids),
                    "owners": ";".join(ids),
                })

    # Dependency resolution for uses_* fields.
    introduction_index = {
        "uses_terms": defaultdict(list),
        "uses_symbols": defaultdict(list),
        "uses_notation": defaultdict(list),
    }
    source_field = {
        "uses_terms": "introduces_terms",
        "uses_symbols": "introduces_symbols",
        "uses_notation": "introduces_notation",
    }
    for uses_field, intro_field in source_field.items():
        for cid, c in by_id.items():
            for item in c.get(intro_field, []) or []:
                introduction_index[uses_field][str(item).strip()].append(cid)

    for cid, c in by_id.items():
        c_num = chapter_num(str(c.get("chapter", "")))
        for uses_field in ("uses_terms", "uses_symbols", "uses_notation"):
            for item in c.get(uses_field, []) or []:
                item = str(item).strip()
                owners = introduction_index[uses_field].get(item, [])
                if not owners:
                    add_issue(
                        issues, "WARNING", "unresolved_dependency",
                        chapter=str(c.get("chapter", "")), concept_id=cid,
                        message=f"{uses_field} '{item}' has no registered owner.",
                        recommendation="Register the canonical owner or correct the spelling/alias.",
                    )
                else:
                    earlier = False
                    for owner in owners:
                        o_num = chapter_num(str(by_id[owner].get("chapter", "")))
                        if o_num is None or c_num is None or o_num <= c_num:
                            earlier = True
                    if not earlier:
                        add_issue(
                            issues, "ERROR", "dependency_owned_later",
                            chapter=str(c.get("chapter", "")), concept_id=cid,
                            message=f"{uses_field} '{item}' is only introduced by a later Layer 3 concept: {owners}.",
                            recommendation="Move canonical ownership earlier or change the prerequisite/ownership design.",
                        )

    # ----- figure audit
    manifest_by_fig: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in manifest_rows:
        fid = str(r.get("Figure ID", "")).strip()
        if fid:
            manifest_by_fig[fid].append(r)

    figure_rows: list[dict[str, Any]] = []
    referenced_by: dict[str, list[str]] = defaultdict(list)

    for ch, doc in chapters.items():
        for fid in sorted(set(FIG_RE.findall(doc.raw))):
            referenced_by[fid].append(ch)
            if fid not in manifest_by_fig:
                add_issue(
                    issues, "ERROR", "figure_not_in_manifest",
                    chapter=ch, figure_id=fid, file=str(doc.path),
                    message="Chapter references a figure that is absent from the figure manifest.",
                    recommendation="Register the figure in the manifest or correct the figure ID.",
                )
            figure_rows.append({
                "figure_id": fid,
                "chapter": ch,
                "reference_status": "registered" if fid in manifest_by_fig else "missing_manifest",
                "manifest_chapter": (manifest_by_fig.get(fid) or [{}])[0].get("Chapter", ""),
                "manifest_status": (manifest_by_fig.get(fid) or [{}])[0].get("Status", ""),
                "owner_count": "",
                "detail": "",
            })

    for fid, rows in manifest_by_fig.items():
        if len(rows) > 1:
            add_issue(
                issues, "ERROR", "duplicate_figure_manifest_id",
                figure_id=fid,
                message=f"Figure ID appears {len(rows)} times in the manifest.",
                recommendation="Keep one manifest row per figure owner.",
            )
        refs = referenced_by.get(fid, [])
        owner_count = len(set(refs))
        if owner_count == 0:
            ch = rows[0].get("Chapter", "") if rows else ""
            if is_layer3_chapter(ch):
                add_issue(
                    issues, "WARNING", "orphan_manifest_figure",
                    chapter=ch, figure_id=fid,
                    message="Layer 3 figure is registered in the manifest but not referenced by any audited chapter.",
                    recommendation="Add the figure reference to its owner chapter or remove stale manifest registration.",
                )
        elif owner_count > 1:
            add_issue(
                issues, "ERROR", "multiple_figure_owners",
                figure_id=fid,
                message=f"Figure is referenced by multiple chapters: {sorted(set(refs))}.",
                recommendation="Assign one canonical figure owner and reference/reuse it explicitly if cross-chapter reuse is intended.",
            )

        for r in rows:
            m_ch = str(r.get("Chapter", "")).strip()
            if refs and m_ch and m_ch not in refs:
                add_issue(
                    issues, "ERROR", "figure_chapter_mismatch",
                    chapter=m_ch, figure_id=fid,
                    message=f"Manifest owner chapter {m_ch} does not match chapter reference(s) {sorted(set(refs))}.",
                    recommendation="Correct the manifest Chapter field or the chapter figure reference.",
                )

    # Add manifest-only rows to figure report.
    already = {(r["figure_id"], r["chapter"]) for r in figure_rows}
    for fid, rows in manifest_by_fig.items():
        for r in rows:
            ch = str(r.get("Chapter", "")).strip()
            if (fid, ch) not in already and is_layer3_chapter(ch):
                figure_rows.append({
                    "figure_id": fid,
                    "chapter": ch,
                    "reference_status": "orphan" if not referenced_by.get(fid) else "referenced_elsewhere",
                    "manifest_chapter": ch,
                    "manifest_status": r.get("Status", ""),
                    "owner_count": len(set(referenced_by.get(fid, []))),
                    "detail": "",
                })

    # ----- handbook/source audit
    handbook_rows: list[dict[str, Any]] = []
    for cid, c in by_id.items():
        ch = str(c.get("chapter", "")).strip()
        if not is_layer3_chapter(ch):
            continue
        hb_status = str(c.get("handbook_status", "")).strip()
        verified = bool(c.get("handbook_verified", False))
        hb_ref = c.get("handbook_ref")
        split = bool(c.get("split_required", False))

        ref_section = ""
        ref_page = ""
        if isinstance(hb_ref, dict):
            ref_section = str(hb_ref.get("section", "")).strip()
            ref_page = str(hb_ref.get("page", "")).strip()
        elif hb_ref:
            ref_section = str(hb_ref)

        row_status = "ok"
        if verified and not hb_ref:
            row_status = "verified_without_ref"
            add_issue(
                issues, "ERROR", "handbook_verified_without_ref",
                chapter=ch, concept_id=cid,
                message="handbook_verified is true but handbook_ref is empty.",
                recommendation="Add the verified Handbook section/page or set handbook_verified false.",
            )
        if hb_status == "not_in_handbook" and hb_ref:
            row_status = "not_in_handbook_with_ref"
            add_issue(
                issues, "ERROR", "not_in_handbook_with_ref",
                chapter=ch, concept_id=cid,
                message="Concept is marked not_in_handbook but also claims a handbook_ref.",
                recommendation="Remove the Handbook reference or correct the handbook_status.",
            )
        if hb_status == "not_in_handbook" and verified:
            row_status = "not_in_handbook_verified"
            add_issue(
                issues, "ERROR", "not_in_handbook_verified",
                chapter=ch, concept_id=cid,
                message="Concept is marked not_in_handbook but handbook_verified is true.",
                recommendation="Make handbook_status and handbook_verified consistent.",
            )
        if hb_status == "in_handbook" and not verified:
            add_issue(
                issues, "WARNING", "in_handbook_unverified",
                chapter=ch, concept_id=cid,
                message="Concept is marked in_handbook but handbook_verified is false.",
                recommendation="Verify the page/section or change the source status.",
            )
        if split and not c.get("notes"):
            add_issue(
                issues, "WARNING", "split_without_notes",
                chapter=ch, concept_id=cid,
                message="split_required is true but the ledger has no explanatory notes.",
                recommendation="Document which portion is Handbook-supported and which portion is guide-developed.",
            )

        # Basic page sanity: every page number token should be within Handbook printed range.
        page_nums = [int(x) for x in re.findall(r"\d{1,3}", ref_page)]
        if any(p < 1 or p > 500 for p in page_nums):
            row_status = "page_out_of_range"
            add_issue(
                issues, "ERROR", "handbook_page_out_of_range",
                chapter=ch, concept_id=cid,
                message=f"Handbook page reference appears out of printed range 1–500: '{ref_page}'.",
                recommendation="Verify the printed Handbook page, not the PDF viewer page.",
            )

        handbook_rows.append({
            "concept_id": cid,
            "chapter": ch,
            "handbook_status": hb_status,
            "handbook_verified": verified,
            "split_required": split,
            "handbook_section": ref_section,
            "handbook_page": ref_page,
            "audit_status": row_status,
        })

    # ----- spec coverage
    spec_rows: list[dict[str, Any]] = []
    mapped: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    areas_by_disc: dict[str, set[str]] = defaultdict(set)

    for cid, c in by_id.items():
        ch = str(c.get("chapter", "")).strip()
        if not is_layer3_chapter(ch):
            continue
        for sl in c.get("spec_lines", []) or []:
            if not isinstance(sl, dict):
                continue
            disc = norm_track(sl.get("discipline"))
            area = str(sl.get("area", "")).strip()
            item = str(sl.get("item", "")).strip()
            mapped[(disc, area, item)].append(cid)
            if area:
                # Area may be "8–10" for integration; only count simple integer areas.
                if re.fullmatch(r"\d+", area):
                    areas_by_disc[disc].add(area)
            spec_rows.append({
                "discipline": disc,
                "area": area,
                "item": item,
                "title": "",
                "required": "",
                "owner_count": len(mapped[(disc, area, item)]),
                "owners": ";".join(mapped[(disc, area, item)]),
                "status": "mapped",
            })

    # Coarse area sanity where exact area counts are known.
    for disc, expected_count in EXPECTED_AREA_COUNTS.items():
        if disc == "other_disciplines":
            # OTH integration atoms intentionally use combined area strings;
            # exact route coverage comes from prerequisites, not atom count.
            continue
        area_nums = {int(a) for a in areas_by_disc.get(disc, set()) if a.isdigit()}
        missing_areas = sorted(set(range(1, expected_count + 1)) - area_nums)
        if missing_areas:
            add_issue(
                issues, "INFO", "spec_area_not_directly_mapped",
                message=f"{disc}: no direct Layer 3 atom mapping found for official spec area(s) {missing_areas}. This may be intentional if covered by Layers 1–2.",
                recommendation="Confirm each missing area is intentionally owned in Layers 1–2 or add an explicit route mapping; do not duplicate ownership.",
            )

    catalog = load_spec_catalog(spec_catalog_path)
    if catalog:
        # Rebuild an exact coverage report from the external catalog.
        exact_rows: list[dict[str, Any]] = []
        for row in catalog:
            disc = norm_track(row.get("discipline"))
            area = str(row.get("area", "")).strip()
            item = str(row.get("item", "")).strip()
            title = str(row.get("title", "")).strip()
            required = truthy(row.get("required"))
            # Exact match first; area-only fallback only when catalog item blank.
            owners = mapped.get((disc, area, item), [])
            if not owners and not item:
                owners = sorted({
                    cid for (d, a, _i), ids in mapped.items()
                    if d == disc and a == area
                    for cid in ids
                })
            status = "covered" if owners else ("missing_required" if required else "unmapped_optional")
            exact_rows.append({
                "discipline": disc,
                "area": area,
                "item": item,
                "title": title,
                "required": required,
                "owner_count": len(owners),
                "owners": ";".join(owners),
                "status": status,
            })
            if required and not owners:
                add_issue(
                    issues, "ERROR", "spec_item_uncovered",
                    message=f"Required spec item is not mapped: {disc} area {area} item {item} {title}".strip(),
                    recommendation="Map the item to an existing canonical concept or create a new concept only if there is a verified coverage gap.",
                )
        spec_rows = exact_rows
    else:
        add_issue(
            issues, "INFO", "exact_spec_catalog_not_supplied",
            message="No external exact specification catalog was supplied; item-level official specification completeness was not mechanically proven.",
            recommendation="Provide --spec-catalog with discipline/area/item rows for exact item-level coverage verification.",
        )

    # Duplicate exact spec mapping is not necessarily an error; report it for review.
    for key, owners in mapped.items():
        if len(set(owners)) > 1:
            disc, area, item = key
            add_issue(
                issues, "INFO", "multiple_concepts_map_same_spec_item",
                concept_id=";".join(sorted(set(owners))),
                message=f"{disc} area {area} item {item} maps to multiple concepts.",
                recommendation="Confirm this is intentional decomposition, not duplicate concept ownership.",
            )

    # ----- reserved concepts
    for cid, c in by_id.items():
        ch = str(c.get("chapter", "")).strip()
        if ch in RESERVED_CHAPTERS:
            add_issue(
                issues, "WARNING", "reserved_chapter_concept_registered",
                chapter=ch, concept_id=cid,
                message="A concept is registered to a reserved Layer 3 slot.",
                recommendation="Remove it unless 03-96–03-99 have been explicitly approved for a verified gap/capstone.",
            )

    # ----- issue output
    issues.sort(key=Issue.key)
    outdir.mkdir(parents=True, exist_ok=True)

    issue_fields = [
        "severity", "category", "chapter", "concept_id", "figure_id",
        "file", "message", "recommendation",
    ]
    write_csv(outdir/"Layer3-Audit-Issues.csv", [asdict(i) for i in issues], issue_fields)

    write_csv(
        outdir/"Layer3-Prerequisite-Audit.csv",
        prereq_rows,
        ["concept_id", "chapter", "prerequisite_id", "status", "detail"],
    )

    write_csv(
        outdir/"Layer3-Figure-Audit.csv",
        figure_rows,
        ["figure_id", "chapter", "reference_status", "manifest_chapter", "manifest_status", "owner_count", "detail"],
    )

    write_csv(
        outdir/"Layer3-Handbook-Audit.csv",
        handbook_rows,
        ["concept_id", "chapter", "handbook_status", "handbook_verified", "split_required", "handbook_section", "handbook_page", "audit_status"],
    )

    write_csv(
        outdir/"Layer3-Duplicate-Ownership.csv",
        dup_rows,
        ["ownership_type", "item", "owner_count", "owners"],
    )

    write_csv(
        outdir/"Layer3-Spec-Coverage.csv",
        spec_rows,
        ["discipline", "area", "item", "title", "required", "owner_count", "owners", "status"],
    )

    # ----- summary
    counts = Counter(i.severity for i in issues)
    cat_counts = Counter(i.category for i in issues)

    chapter_count = len([ch for ch in chapters if is_layer3_chapter(ch)])
    concept_count = len([c for c in concepts if is_layer3_chapter(str(c.get("chapter", "")).strip())])
    manifest_count = len([r for r in manifest_rows if is_layer3_chapter(str(r.get("Chapter", "")).strip())])

    status = "PASS" if counts["BLOCKER"] == 0 and counts["ERROR"] == 0 else "FAIL"
    if status == "PASS" and counts["WARNING"]:
        status = "PASS WITH WARNINGS"

    lines = [
        "# Layer 3 Audit Summary",
        "",
        f"**Audit status:** {status}  ",
        f"**Root:** `{root}`  ",
        f"**Ledger:** `{ledger_path}`  ",
        f"**Figure manifest:** `{manifest_path}`  ",
        f"**Chapter map:** `{map_path}`  ",
        "",
        "## Scope",
        "",
        f"- Layer 3 chapter files found: **{chapter_count} / 95**",
        f"- Layer 3 ledger concepts audited: **{concept_count}**",
        f"- Layer 3 manifest figures audited: **{manifest_count}**",
        f"- Duplicate chapter-number groups found: **{len(duplicate_chapter_files)}**",
        f"- Prerequisite cycles found: **{len(cycles)}**",
        "",
        "## Issue counts",
        "",
        f"- BLOCKER: **{counts['BLOCKER']}**",
        f"- ERROR: **{counts['ERROR']}**",
        f"- WARNING: **{counts['WARNING']}**",
        f"- INFO: **{counts['INFO']}**",
        "",
        "## Interpretation",
        "",
        "- **BLOCKER** — release cannot proceed until corrected.",
        "- **ERROR** — concrete structural/source/coverage inconsistency requiring correction.",
        "- **WARNING** — likely problem or manual-review requirement.",
        "- **INFO** — audit note, intentional decomposition to verify, or check not fully provable without an external catalog.",
        "",
        "## Highest-priority issues",
        "",
    ]

    top = [i for i in issues if i.severity in {"BLOCKER", "ERROR", "WARNING"}][:50]
    if not top:
        lines.append("No blocker, error, or warning issues were found by the automated checks.")
    else:
        for i in top:
            where = " / ".join(x for x in [i.chapter, i.concept_id, i.figure_id] if x)
            where = f" ({where})" if where else ""
            lines.append(f"- **{i.severity} — {i.category}**{where}: {i.message}")

    lines += [
        "",
        "## Category counts",
        "",
    ]
    for cat, n in sorted(cat_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"- `{cat}`: {n}")

    lines += [
        "",
        "## Generated reports",
        "",
        "- `Layer3-Audit-Issues.csv` — sortable master punch list.",
        "- `Layer3-Spec-Coverage.csv` — specification mappings and optional exact coverage.",
        "- `Layer3-Prerequisite-Audit.csv` — every prerequisite edge and its status.",
        "- `Layer3-Figure-Audit.csv` — chapter references versus manifest ownership.",
        "- `Layer3-Handbook-Audit.csv` — source-status consistency and page-reference checks.",
        "- `Layer3-Duplicate-Ownership.csv` — duplicate term/symbol/notation ownership.",
        "",
        "## Important limitation",
        "",
        "This script performs structural and consistency auditing. It does **not** prove that every formula, worked example, answer explanation, or engineering statement is technically correct. After BLOCKER/ERROR issues are resolved, manually review flagged chapters and a representative sample of clean chapters for pedagogy, calculation accuracy, and figure quality.",
        "",
    ]
    (outdir/"Layer3-Audit-Summary.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Layer 3 audit: {status}")
    print(f"  BLOCKER={counts['BLOCKER']}  ERROR={counts['ERROR']}  WARNING={counts['WARNING']}  INFO={counts['INFO']}")
    print(f"  Output: {outdir}")

    return 0 if counts["BLOCKER"] == 0 and counts["ERROR"] == 0 else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Audit the FE Supplemental Guide Layer 3 project (03-01 through 03-95) using the normalized repository layout."
    )
    ap.add_argument(
        "--root", type=Path, default=Path.cwd(),
        help=(
            "Any directory inside the FE-Study-Guide repository. "
            "The script walks upward to normalize it to the project root."
        ),
    )
    ap.add_argument(
        "--ledger", type=Path,
        help="Optional override. Default normalized path: <root>/meta/ledger.yaml",
    )
    ap.add_argument(
        "--manifest", type=Path,
        help="Optional override. Default normalized path: <root>/figures/figure-manifest.csv",
    )
    ap.add_argument(
        "--map", dest="map_path", type=Path,
        help="Optional override. Default normalized path: <root>/layer-3-tracks/Layer-3-Chapter-Map.md",
    )
    ap.add_argument(
        "--out", type=Path,
        help="Optional output folder. Default: <root>/tools/validation/layer3-audit",
    )
    ap.add_argument(
        "--spec-catalog", type=Path,
        help="Optional CSV/YAML exact FE specification catalog for item-level coverage verification.",
    )
    ap.add_argument(
        "--show-paths", action="store_true",
        help="Print the normalized project paths and exit without running the audit.",
    )
    args = ap.parse_args()

    requested = args.root.expanduser().resolve()
    root = normalize_project_root(requested)

    if not root.exists():
        print(f"ERROR: normalized project root does not exist: {root}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"ERROR: normalized project root is not a directory: {root}", file=sys.stderr)
        return 2

    # Canonical locations derived directly from the repository inventory.
    ledger = (
        args.ledger.expanduser().resolve()
        if args.ledger
        else canonical_path(root, "ledger")
    )
    manifest = (
        args.manifest.expanduser().resolve()
        if args.manifest
        else canonical_path(root, "manifest")
    )
    map_path = (
        args.map_path.expanduser().resolve()
        if args.map_path
        else canonical_path(root, "map")
    )
    outdir = (
        args.out.expanduser().resolve()
        if args.out
        else canonical_path(root, "output")
    )
    spec_catalog = args.spec_catalog.expanduser().resolve() if args.spec_catalog else None

    print("Normalized FE project paths:")
    print(f"  root:     {root}")
    print(f"  ledger:   {ledger}")
    print(f"  manifest: {manifest}")
    print(f"  map:      {map_path}")
    print(f"  layer3:   {canonical_path(root, 'layer3_root')}")
    print(f"  output:   {outdir}")

    if args.show_paths:
        return 0

    # Validate the standard project structure first. This gives exact path
    # diagnostics rather than a generic recursive-scan PermissionError.
    layout_problems = validate_canonical_layout(root)
    if layout_problems:
        print("\nERROR: normalized project layout is incomplete or inaccessible:", file=sys.stderr)
        for problem in layout_problems:
            print(f"  - {problem}", file=sys.stderr)
        return 2

    # Explicit override files are still permitted, but they must be files.
    for label, p in [("ledger", ledger), ("manifest", manifest), ("map", map_path)]:
        try:
            if not p.exists():
                print(f"ERROR: {label} file does not exist: {p}", file=sys.stderr)
                return 2
            if not p.is_file():
                print(f"ERROR: {label} path is not a file: {p}", file=sys.stderr)
                return 2
        except PermissionError:
            print(f"ERROR: permission denied accessing {label}: {p}", file=sys.stderr)
            print(
                "If this is a OneDrive Files On-Demand location, mark the file/folder "
                "'Always keep on this device' and rerun the audit.",
                file=sys.stderr,
            )
            return 2

    if spec_catalog:
        try:
            if not spec_catalog.is_file():
                print(f"ERROR: spec catalog does not exist or is not a file: {spec_catalog}", file=sys.stderr)
                return 2
        except PermissionError:
            print(f"ERROR: permission denied accessing spec catalog: {spec_catalog}", file=sys.stderr)
            return 2

    try:
        return audit(
            root=root,
            ledger_path=ledger,
            manifest_path=manifest,
            map_path=map_path,
            outdir=outdir,
            spec_catalog_path=spec_catalog,
        )
    except PermissionError as e:
        print(f"ERROR: permission denied while auditing: {e.filename or e}", file=sys.stderr)
        print(
            "The audit now uses normalized direct paths rather than recursive discovery. "
            "Make the reported OneDrive file/folder locally available and readable, then rerun.",
            file=sys.stderr,
        )
        return 2
    except Exception as e:
        print(f"ERROR: audit failed: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
