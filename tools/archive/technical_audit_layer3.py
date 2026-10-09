#!/usr/bin/env python3
"""
technical_audit_layer3.py
=========================

Technical-content audit for the FE Supplemental Guide Layer 3 project.

This script is intended to run AFTER the structural audit has passed. It does
not replace human engineering review; it identifies chapters, equations,
worked examples, answer keys, practice solutions, figures, and source claims
that deserve technical review.

Normalized repository layout
----------------------------
FE-Study-Guide/
  meta/
    ledger.yaml
  figures/
    figure-manifest.csv
  layer-3-tracks/
    Layer-3-Chapter-Map.md
    chemical/
    civil/
    electrical/
    environmental/
    industrial/
    mechanical/
    other/
  tools/
    validation/

Default output
--------------
tools/validation/layer3-technical-audit/

Generated reports
-----------------
Technical-Audit-Summary.md
Technical-Audit-Issues.csv
Technical-Audit-Chapters.csv
Technical-Audit-Worked-Examples.csv
Technical-Audit-Formulas.csv
Technical-Audit-Assessments.csv
Technical-Audit-Figures.csv
Technical-Audit-Sources.csv
Technical-Audit-Duplicate-Text.csv
Technical-Audit-Numerical-Checks.csv

What this script CAN check
--------------------------
* Missing or unusually weak worked-example solutions
* Generic/template solution language
* Numeric problems whose solutions contain no computed numeric result
* Repeated answer/solution text across a chapter or across chapters
* Very short answer explanations and practice solutions
* Formula delimiter/bracing problems and suspicious placeholder notation
* Simple arithmetic inconsistencies in explicit "a op b = c" statements
* Figure references, alt-text quality, descriptions, and manifest status
* Handbook/source-status consistency with ledger metadata
* Missing "As the Handbook States It" boundaries
* Source claims that still require manual/PDF verification
* Objective/section/assessment coverage heuristics
* TODO/TBD/placeholder/editorial language remaining in student-facing text

What this script CANNOT prove
-----------------------------
* That every engineering formula is physically correct
* That every model assumption is appropriate
* That every numerical worked example uses the correct governing equation
* That Handbook page content actually supports a claim unless a human or a
  dedicated source-verification workflow checks the cited source
* That a generated figure is technically accurate from its manifest text alone

Typical usage
-------------
From repository root:
    python .\tools\technical_audit_layer3.py

From tools/:
    python .\technical_audit_layer3.py

Show normalized paths only:
    python .\technical_audit_layer3.py --show-paths

Treat REVIEW items as a failing exit status:
    python .\technical_audit_layer3.py --strict
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import re
import sys
import hashlib
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
# Repository layout
# ---------------------------------------------------------------------------

NORMALIZED_LAYOUT = {
    "ledger": Path("meta") / "ledger.yaml",
    "manifest": Path("figures") / "figure-manifest.csv",
    "map": Path("layer-3-tracks") / "Layer-3-Chapter-Map.md",
    "layer3_root": Path("layer-3-tracks"),
    "output": Path("tools") / "validation" / "layer3-technical-audit",
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

TRACK_ALIASES = {
    "chemical": "chemical",
    "che": "chemical",
    "civil": "civil",
    "civ": "civil",
    "electrical": "electrical_and_computer",
    "ece": "electrical_and_computer",
    "electrical_and_computer": "electrical_and_computer",
    "environmental": "environmental",
    "env": "environmental",
    "industrial": "industrial_and_systems",
    "ind": "industrial_and_systems",
    "industrial_and_systems": "industrial_and_systems",
    "mechanical": "mechanical",
    "mec": "mechanical",
    "other": "other_disciplines",
    "oth": "other_disciplines",
    "other_disciplines": "other_disciplines",
}

PROJECT_ROOT_MARKERS = (
    NORMALIZED_LAYOUT["ledger"],
    NORMALIZED_LAYOUT["manifest"],
    NORMALIZED_LAYOUT["map"],
)

SEVERITY_ORDER = {
    "CRITICAL": 0,
    "ERROR": 1,
    "WARNING": 2,
    "REVIEW": 3,
    "INFO": 4,
}

FIG_RE = re.compile(r"\bFIG-03-\d{2}-\d{3}\b")
CHAPTER_RE = re.compile(r"^03-(\d{2})$")
NUM_TOKEN_RE = re.compile(r"(?<![\w.-])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")
UNIT_TOKEN_RE = re.compile(
    r"\b(?:V|A|W|kW|MW|mW|Pa|kPa|MPa|psi|psf|N|kN|lbf|lbm|kg|g|m|mm|cm|km|"
    r"s|min|h|Hz|kHz|MHz|rad|deg|°C|°F|K|J|kJ|MJ|Btu|mol|kmol|m/s|m/s\^2|"
    r"ft/s|ft/s\^2|m\^2|m\^3|ft\^2|ft\^3|L|mL|gal|gpm|cfm|rpm|ohm|Ω|F|H|"
    r"S|C|ppm|ppb|mg/L|g/L|kg/m\^3|Pa·s|cP|W/m\^2|W/m·K|W/m-K)\b"
)
HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.MULTILINE)
FIG_MD_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\bPLACEHOLDER\b",
    r"\bINSERT\b.+\bHERE\b",
    r"\bVERIFY\b.+\bLATER\b",
    r"\bcoming soon\b",
    r"\bto be completed\b",
]

GENERIC_SOLUTION_PATTERNS = [
    r"apply the (?:relation|equation|formula|method)",
    r"use the (?:relation|equation|formula|method)",
    r"identify the governing",
    r"verify (?:the )?(?:model|assumption|units|result)",
    r"substitute (?:the )?values",
    r"solve using the method",
    r"follow the steps above",
    r"refer to (?:§|section)",
    r"as described (?:above|earlier)",
    r"the result follows",
    r"calculate as appropriate",
    r"use the appropriate",
]

SUSPICIOUS_CLAIM_PATTERNS = [
    r"\balways\b",
    r"\bnever\b",
    r"\bexactly\b",
    r"\bmust\b",
    r"\bguarantees?\b",
    r"\b100%\b",
]

# Simple arithmetic statement, e.g. "24 × 2 = 48", "12 / 3 = 4".
# It intentionally ignores variables/units embedded between operands.
SIMPLE_ARITH_RE = re.compile(
    r"(?P<a>[-+]?\d+(?:\.\d+)?)\s*"
    r"(?P<op>[×xX*/+\-÷])\s*"
    r"(?P<b>[-+]?\d+(?:\.\d+)?)\s*=\s*"
    r"(?P<c>[-+]?\d+(?:\.\d+)?)"
)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    severity: str
    category: str
    chapter: str = ""
    section: str = ""
    concept_id: str = ""
    figure_id: str = ""
    file: str = ""
    excerpt: str = ""
    message: str = ""
    recommendation: str = ""

    def key(self):
        return (
            SEVERITY_ORDER.get(self.severity, 99),
            self.chapter,
            self.category,
            self.section,
            self.concept_id,
            self.figure_id,
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
# Generic helpers
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
    return n is not None and 1 <= n <= 95


def looks_like_project_root(path: Path) -> bool:
    try:
        return all((path / marker).exists() for marker in PROJECT_ROOT_MARKERS)
    except (PermissionError, OSError):
        return False


def normalize_project_root(start: Path) -> Path:
    start = start.expanduser().resolve()
    if start.is_file():
        start = start.parent
    for candidate in [start, *start.parents]:
        if looks_like_project_root(candidate):
            return candidate
    return start


def canonical_path(root: Path, key: str) -> Path:
    return (root / NORMALIZED_LAYOUT[key]).resolve()


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML mapping at top level: {path}")
    return data


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def excerpt(text: str, limit: int = 220) -> str:
    s = re.sub(r"\s+", " ", text).strip()
    return s if len(s) <= limit else s[: limit - 1] + "…"


def add_issue(
    issues: list[Issue],
    severity: str,
    category: str,
    *,
    chapter: str = "",
    section: str = "",
    concept_id: str = "",
    figure_id: str = "",
    file: str = "",
    excerpt_text: str = "",
    message: str,
    recommendation: str = "",
) -> None:
    issues.append(Issue(
        severity=severity,
        category=category,
        chapter=chapter,
        section=section,
        concept_id=concept_id,
        figure_id=figure_id,
        file=file,
        excerpt=excerpt(excerpt_text),
        message=message,
        recommendation=recommendation,
    ))


def parse_frontmatter(path: Path) -> Optional[ChapterDoc]:
    try:
        raw = path.read_text(encoding="utf-8")
    except (PermissionError, OSError, UnicodeError):
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
    ids = fm.get("ledger_ids", []) or []
    if isinstance(ids, str):
        ids = [ids]
    return ChapterDoc(
        path=path,
        chapter=ch,
        title=str(fm.get("title", "")).strip(),
        track=norm_track(fm.get("track")),
        ledger_ids=[str(x).strip() for x in ids],
        status=str(fm.get("status", "")).strip(),
        frontmatter=fm,
        body=parts[2],
        raw=raw,
    )


def discover_chapters(root: Path, issues: list[Issue]) -> dict[str, ChapterDoc]:
    chapters: dict[str, ChapterDoc] = {}
    for logical_track, rel in LAYER3_TRACK_DIRS.items():
        track_dir = (root / rel).resolve()
        try:
            files = list(track_dir.iterdir())
        except (PermissionError, OSError) as e:
            add_issue(
                issues, "CRITICAL", "track_folder_unreadable",
                file=str(track_dir),
                message=f"Cannot read Layer 3 track directory: {e}",
                recommendation="Make the directory locally available and readable.",
            )
            continue

        for path in files:
            try:
                if not path.is_file() or path.suffix.lower() != ".md":
                    continue
            except (PermissionError, OSError):
                continue
            if not re.match(r"^03-\d{2}-", path.name, re.I):
                continue
            doc = parse_frontmatter(path)
            if not doc:
                add_issue(
                    issues, "ERROR", "chapter_unparseable",
                    file=str(path),
                    message="Could not parse Layer 3 chapter frontmatter.",
                    recommendation="Repair YAML frontmatter before technical review.",
                )
                continue
            if doc.chapter in chapters:
                add_issue(
                    issues, "ERROR", "duplicate_chapter_document",
                    chapter=doc.chapter, file=str(path),
                    message="More than one technical-review candidate claims this chapter number.",
                    recommendation="Keep one authoritative chapter file.",
                )
                continue
            chapters[doc.chapter] = doc
    return chapters


def split_h2_sections(text: str) -> list[tuple[str, str]]:
    """Return [(heading, body)] for Markdown ## sections."""
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    out = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1).strip(), text[start:end]))
    return out


def numbered_blocks(text: str) -> list[tuple[int, str]]:
    """
    Split top-level numbered Markdown entries:
      1. ...
      body
      2. ...
    """
    matches = list(re.finditer(r"(?m)^\s*(\d+)\.\s+", text))
    out = []
    for i, m in enumerate(matches):
        n = int(m.group(1))
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((n, text[start:end].strip()))
    return out


def find_h2(text: str, heading_prefix: str) -> str:
    sections = split_h2_sections(text)
    for heading, body in sections:
        if heading.lower().startswith(heading_prefix.lower()):
            return body
    return ""


def strip_markdown(text: str) -> str:
    s = re.sub(r"```.*?```", " ", text, flags=re.S)
    s = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", s)
    s = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"[*_>#|]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def normalize_similarity_text(text: str) -> str:
    s = strip_markdown(text).lower()
    s = re.sub(r"\b\d+(?:\.\d+)?\b", "<num>", s)
    s = re.sub(r"\bfig-03-\d{2}-\d{3}\b", "<fig>", s)
    s = re.sub(r"\b§?\d+(?:\.\d+)+\b", "<sec>", s)
    s = re.sub(r"[^a-z<> ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def generic_solution_score(text: str) -> int:
    lower = strip_markdown(text).lower()
    return sum(bool(re.search(p, lower, re.I)) for p in GENERIC_SOLUTION_PATTERNS)


def has_placeholder(text: str) -> Optional[str]:
    for p in PLACEHOLDER_PATTERNS:
        m = re.search(p, text, re.I)
        if m:
            return m.group(0)
    return None


def has_numeric_token(text: str) -> bool:
    return bool(NUM_TOKEN_RE.search(text))


def numeric_tokens(text: str) -> list[str]:
    return NUM_TOKEN_RE.findall(text)


def has_unit_token(text: str) -> bool:
    return bool(UNIT_TOKEN_RE.search(text))


def balanced_braces(s: str) -> bool:
    depth = 0
    escaped = False
    for ch in s:
        if escaped:
            escaped = False
            continue
        if ch == "\\":
            escaped = True
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def extract_math_blocks(text: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    for m in re.finditer(r"\\\[(.*?)\\\]", text, re.S):
        blocks.append(("display_bracket", m.group(1).strip()))
    for m in re.finditer(r"\$\$(.*?)\$\$", text, re.S):
        blocks.append(("display_dollar", m.group(1).strip()))
    return blocks


def arithmetic_checks(text: str) -> list[dict[str, Any]]:
    rows = []
    for m in SIMPLE_ARITH_RE.finditer(text):
        a = float(m.group("a"))
        b = float(m.group("b"))
        c = float(m.group("c"))
        op = m.group("op")
        try:
            if op in {"×", "x", "X", "*"}:
                expected = a * b
            elif op in {"/", "÷"}:
                if b == 0:
                    continue
                expected = a / b
            elif op == "+":
                expected = a + b
            elif op == "-":
                expected = a - b
            else:
                continue
        except Exception:
            continue

        tol = max(1e-9, abs(expected) * 0.015)  # allow rounding
        ok = abs(expected - c) <= tol
        rows.append({
            "expression": m.group(0),
            "a": a,
            "operator": op,
            "b": b,
            "stated": c,
            "expected": expected,
            "difference": c - expected,
            "status": "ok" if ok else "mismatch",
        })
    return rows


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'’-]+\b", strip_markdown(text)))


# ---------------------------------------------------------------------------
# Worked-example extraction
# ---------------------------------------------------------------------------

def extract_worked_examples(doc: ChapterDoc) -> list[dict[str, Any]]:
    """
    Finds ### Worked Example ... blocks anywhere in the chapter.
    The generator used:
        ### Worked Example N
        **Problem.** ...
        **Solution.** ...
    This parser is intentionally tolerant.
    """
    matches = list(re.finditer(r"(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$", doc.raw))
    examples = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(doc.raw)

        # Do not swallow a later H2 section.
        next_h2 = re.search(r"(?m)^##\s+", doc.raw[start:end])
        if next_h2:
            end = start + next_h2.start()

        block = doc.raw[start:end].strip()
        problem_match = re.search(
            r"\*\*Problem\.?\*\*\s*(.*?)(?=\n\s*\*\*Solution\.?\*\*|\Z)",
            block, re.S | re.I
        )
        solution_match = re.search(
            r"\*\*Solution\.?\*\*\s*(.*)",
            block, re.S | re.I
        )
        label = (m.group(1) or str(i + 1)).strip()
        examples.append({
            "label": label,
            "problem": (problem_match.group(1).strip() if problem_match else ""),
            "solution": (solution_match.group(1).strip() if solution_match else ""),
            "block": block,
        })
    return examples


# ---------------------------------------------------------------------------
# Formula audit
# ---------------------------------------------------------------------------

def audit_formulas(doc: ChapterDoc, issues: list[Issue]) -> list[dict[str, Any]]:
    rows = []
    blocks = extract_math_blocks(doc.raw)

    # Raw delimiter sanity.
    if doc.raw.count(r"\[") != doc.raw.count(r"\]"):
        add_issue(
            issues, "ERROR", "math_delimiter_mismatch",
            chapter=doc.chapter, file=str(doc.path),
            message=r"Count of \[ and \] display-math delimiters does not match.",
            recommendation="Repair the malformed LaTeX display-math block.",
        )

    # Dollar display sanity.
    if doc.raw.count("$$") % 2:
        add_issue(
            issues, "ERROR", "math_dollar_delimiter_mismatch",
            chapter=doc.chapter, file=str(doc.path),
            message="Odd number of $$ display-math delimiters.",
            recommendation="Repair the malformed display-math block.",
        )

    for idx, (kind, expr) in enumerate(blocks, 1):
        status = "ok"
        flags = []

        if not balanced_braces(expr):
            status = "error"
            flags.append("unbalanced_braces")
            add_issue(
                issues, "ERROR", "formula_unbalanced_braces",
                chapter=doc.chapter, section=f"formula-{idx}", file=str(doc.path),
                excerpt_text=expr,
                message="Formula has unbalanced LaTeX braces.",
                recommendation="Repair the equation before technical verification.",
            )

        ph = has_placeholder(expr)
        if ph:
            status = "error"
            flags.append("placeholder")
            add_issue(
                issues, "ERROR", "formula_placeholder",
                chapter=doc.chapter, section=f"formula-{idx}", file=str(doc.path),
                excerpt_text=expr,
                message=f"Formula contains placeholder/editorial token '{ph}'.",
                recommendation="Replace placeholder notation with the intended equation.",
            )

        if re.search(r"\b(?:something|value|result|answer|TBD|XXX)\b", expr, re.I):
            flags.append("suspicious_symbol_text")
            add_issue(
                issues, "WARNING", "formula_suspicious_text",
                chapter=doc.chapter, section=f"formula-{idx}", file=str(doc.path),
                excerpt_text=expr,
                message="Formula contains prose-like placeholder text.",
                recommendation="Confirm all equation tokens are intentional variables/operators.",
            )

        rows.append({
            "chapter": doc.chapter,
            "file": str(doc.path),
            "formula_index": idx,
            "kind": kind,
            "formula": expr,
            "status": status,
            "flags": ";".join(flags),
        })

    return rows


# ---------------------------------------------------------------------------
# Worked examples / assessments
# ---------------------------------------------------------------------------

def audit_worked_examples(
    doc: ChapterDoc,
    issues: list[Issue],
    normalized_solution_index: dict[str, list[tuple[str, str, str]]],
) -> list[dict[str, Any]]:
    rows = []
    examples = extract_worked_examples(doc)

    if not examples:
        add_issue(
            issues, "WARNING", "worked_examples_missing",
            chapter=doc.chapter, file=str(doc.path),
            message="No 'Worked Example' blocks were found.",
            recommendation="Confirm the chapter intentionally contains no worked examples; otherwise add them.",
        )

    for ex in examples:
        label = ex["label"]
        problem = ex["problem"]
        solution = ex["solution"]
        p_wc = word_count(problem)
        s_wc = word_count(solution)
        p_num = has_numeric_token(problem)
        s_num = has_numeric_token(solution)
        p_unit = has_unit_token(problem)
        s_unit = has_unit_token(solution)
        generic = generic_solution_score(solution)
        flags = []

        if not problem:
            flags.append("missing_problem")
            add_issue(
                issues, "ERROR", "worked_example_missing_problem",
                chapter=doc.chapter, section=f"Worked Example {label}", file=str(doc.path),
                message="Worked example has no parsed Problem text.",
                recommendation="Add a concrete problem statement.",
            )

        if not solution:
            flags.append("missing_solution")
            add_issue(
                issues, "ERROR", "worked_example_missing_solution",
                chapter=doc.chapter, section=f"Worked Example {label}", file=str(doc.path),
                message="Worked example has no parsed Solution text.",
                recommendation="Provide a complete worked solution.",
            )
        else:
            if s_wc < 18:
                flags.append("very_short_solution")
                add_issue(
                    issues, "WARNING", "worked_example_short_solution",
                    chapter=doc.chapter, section=f"Worked Example {label}", file=str(doc.path),
                    excerpt_text=solution,
                    message=f"Worked solution is only {s_wc} words.",
                    recommendation="Expand the solution to show governing relation, substitution, units, and interpretation.",
                )

            if generic >= 2:
                flags.append("generic_solution")
                add_issue(
                    issues, "WARNING", "worked_example_generic_solution",
                    chapter=doc.chapter, section=f"Worked Example {label}", file=str(doc.path),
                    excerpt_text=solution,
                    message="Worked solution strongly resembles generic/template guidance rather than a demonstrated calculation.",
                    recommendation="Replace with a problem-specific derivation/calculation and final result.",
                )

            if p_num and not s_num:
                flags.append("numeric_problem_no_numeric_solution")
                add_issue(
                    issues, "WARNING", "numeric_example_without_numeric_result",
                    chapter=doc.chapter, section=f"Worked Example {label}", file=str(doc.path),
                    excerpt_text=solution,
                    message="Problem contains numeric data, but the parsed solution contains no numeric result.",
                    recommendation="Verify the example is fully solved and includes the computed answer.",
                )

            if p_unit and not s_unit and p_num:
                flags.append("solution_lacks_units")
                add_issue(
                    issues, "REVIEW", "worked_example_solution_units",
                    chapter=doc.chapter, section=f"Worked Example {label}", file=str(doc.path),
                    excerpt_text=solution,
                    message="Numeric problem includes engineering units, but no recognized unit was found in the solution.",
                    recommendation="Check dimensional consistency and include units on intermediate/final quantities where appropriate.",
                )

            ph = has_placeholder(solution)
            if ph:
                flags.append("placeholder")
                add_issue(
                    issues, "ERROR", "worked_example_placeholder",
                    chapter=doc.chapter, section=f"Worked Example {label}", file=str(doc.path),
                    excerpt_text=solution,
                    message=f"Worked solution contains placeholder/editorial token '{ph}'.",
                    recommendation="Replace the placeholder with completed technical content.",
                )

            norm = normalize_similarity_text(solution)
            if len(norm.split()) >= 10:
                normalized_solution_index[norm].append((doc.chapter, f"Worked Example {label}", str(doc.path)))

        rows.append({
            "chapter": doc.chapter,
            "track": doc.track,
            "file": str(doc.path),
            "example": label,
            "problem_words": p_wc,
            "solution_words": s_wc,
            "problem_has_number": p_num,
            "solution_has_number": s_num,
            "problem_has_unit": p_unit,
            "solution_has_unit": s_unit,
            "generic_score": generic,
            "flags": ";".join(flags),
            "problem_excerpt": excerpt(problem),
            "solution_excerpt": excerpt(solution),
        })
    return rows


def audit_assessments(
    doc: ChapterDoc,
    issues: list[Issue],
    normalized_solution_index: dict[str, list[tuple[str, str, str]]],
) -> list[dict[str, Any]]:
    rows = []

    sections = {
        "review_questions": find_h2(doc.raw, "Review Questions"),
        "answer_key": find_h2(doc.raw, "Answer Key"),
        "practice_problems": find_h2(doc.raw, "Practice Problems"),
        "practice_solutions": find_h2(doc.raw, "Practice Problem Solutions"),
    }

    parsed = {k: numbered_blocks(v) for k, v in sections.items()}

    for section_name in ("answer_key", "practice_solutions"):
        for n, body in parsed[section_name]:
            wc = word_count(body)
            generic = generic_solution_score(body)
            has_num = has_numeric_token(body)
            flags = []

            if wc < 7:
                flags.append("very_short")
                add_issue(
                    issues, "WARNING", "assessment_explanation_short",
                    chapter=doc.chapter, section=f"{section_name} {n}", file=str(doc.path),
                    excerpt_text=body,
                    message=f"{section_name.replace('_',' ')} entry {n} is only {wc} words.",
                    recommendation="Add enough explanation to show why the answer is correct or how the result is obtained.",
                )

            if generic >= 2:
                flags.append("generic")
                add_issue(
                    issues, "WARNING", "assessment_generic_solution",
                    chapter=doc.chapter, section=f"{section_name} {n}", file=str(doc.path),
                    excerpt_text=body,
                    message="Assessment solution/explanation appears templated or generic.",
                    recommendation="Replace with a question-specific explanation or calculation.",
                )

            ph = has_placeholder(body)
            if ph:
                flags.append("placeholder")
                add_issue(
                    issues, "ERROR", "assessment_placeholder",
                    chapter=doc.chapter, section=f"{section_name} {n}", file=str(doc.path),
                    excerpt_text=body,
                    message=f"Assessment solution contains placeholder/editorial token '{ph}'.",
                    recommendation="Complete the answer/solution.",
                )

            norm = normalize_similarity_text(body)
            if len(norm.split()) >= 8:
                normalized_solution_index[norm].append((doc.chapter, f"{section_name} {n}", str(doc.path)))

            rows.append({
                "chapter": doc.chapter,
                "track": doc.track,
                "file": str(doc.path),
                "section_type": section_name,
                "number": n,
                "word_count": wc,
                "has_number": has_num,
                "generic_score": generic,
                "flags": ";".join(flags),
                "excerpt": excerpt(body),
            })

    # Heuristic: numeric practice problem should usually yield numeric content
    # in the corresponding solution.
    probs = dict(parsed["practice_problems"])
    sols = dict(parsed["practice_solutions"])
    for n, problem in probs.items():
        if n not in sols:
            continue
        solution = sols[n]
        if has_numeric_token(problem) and not has_numeric_token(solution):
            add_issue(
                issues, "WARNING", "practice_numeric_without_numeric_solution",
                chapter=doc.chapter, section=f"Practice Problem {n}", file=str(doc.path),
                excerpt_text=solution,
                message="Practice problem contains numeric data but its solution contains no numeric result.",
                recommendation="Verify the practice solution is fully worked and not a procedural placeholder.",
            )

    return rows


# ---------------------------------------------------------------------------
# Figure audit
# ---------------------------------------------------------------------------

def audit_figures(
    doc: ChapterDoc,
    manifest_by_id: dict[str, dict[str, str]],
    issues: list[Issue],
) -> list[dict[str, Any]]:
    rows = []
    seen = set()

    for alt, target in FIG_MD_RE.findall(doc.raw):
        m = FIG_RE.search(alt + " " + target)
        if not m:
            continue
        fid = m.group(0)
        if fid in seen:
            continue
        seen.add(fid)

        mr = manifest_by_id.get(fid, {})
        alt_clean = strip_markdown(alt)
        desc = str(mr.get("Description", "")).strip()
        manifest_alt = str(mr.get("Alt Text", "")).strip()
        status = str(mr.get("Status", "")).strip()
        flags = []

        if len(alt_clean) < 20:
            flags.append("short_inline_alt")
            add_issue(
                issues, "REVIEW", "figure_alt_text_short",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                excerpt_text=alt_clean,
                message="Inline figure alt text is very short.",
                recommendation="Confirm the alt text explains the technical relationship, not merely the figure title.",
            )

        if not desc:
            flags.append("missing_manifest_description")
            add_issue(
                issues, "WARNING", "figure_description_missing",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                message="Figure manifest description is blank.",
                recommendation="Add a technical description sufficient for generation and QA.",
            )
        elif word_count(desc) < 8:
            flags.append("short_manifest_description")
            add_issue(
                issues, "REVIEW", "figure_description_short",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                excerpt_text=desc,
                message="Figure manifest description is unusually brief.",
                recommendation="Confirm it specifies geometry, labels, quantities, arrows, symbols, and relationships needed for technical accuracy.",
            )

        if not manifest_alt:
            flags.append("missing_manifest_alt")
            add_issue(
                issues, "WARNING", "figure_manifest_alt_missing",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                message="Manifest Alt Text is blank.",
                recommendation="Add accessible alt text describing the engineering information conveyed.",
            )

        if status.lower() in {"specified", "planned", ""}:
            flags.append("artwork_not_verified")
            add_issue(
                issues, "INFO", "figure_artwork_not_verified",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                message=f"Manifest status is '{status or 'blank'}'; technical artwork accuracy has not been verified.",
                recommendation="After artwork exists, conduct visual engineering QA against the chapter and manifest.",
            )

        rows.append({
            "chapter": doc.chapter,
            "track": doc.track,
            "file": str(doc.path),
            "figure_id": fid,
            "inline_alt": alt_clean,
            "manifest_type": mr.get("Type", ""),
            "manifest_description": desc,
            "manifest_alt": manifest_alt,
            "manifest_status": status,
            "flags": ";".join(flags),
        })

    return rows


# ---------------------------------------------------------------------------
# Source/Handbook audit
# ---------------------------------------------------------------------------

def audit_sources(
    doc: ChapterDoc,
    chapter_atoms: list[dict[str, Any]],
    issues: list[Issue],
) -> list[dict[str, Any]]:
    rows = []

    handbook_section = find_h2(doc.raw, "As the Handbook States It")
    if not handbook_section:
        add_issue(
            issues, "WARNING", "handbook_boundary_missing",
            chapter=doc.chapter, file=str(doc.path),
            message="Chapter has no 'As the Handbook States It' section.",
            recommendation="Add an explicit source boundary distinguishing Handbook content, spec-required knowledge, and guide-developed material.",
        )

    if handbook_section and not re.search(
        r"\b(?:source boundary|guide-developed|not in (?:the )?handbook|handbook)\b",
        handbook_section, re.I
    ):
        add_issue(
            issues, "REVIEW", "handbook_boundary_weak",
            chapter=doc.chapter, file=str(doc.path),
            excerpt_text=handbook_section,
            message="'As the Handbook States It' section may not clearly distinguish sourced vs. guide-developed material.",
            recommendation="State the source boundary explicitly.",
        )

    for atom in chapter_atoms:
        cid = str(atom.get("id", ""))
        hb_status = str(atom.get("handbook_status", "")).strip()
        verified = bool(atom.get("handbook_verified", False))
        hb_ref = atom.get("handbook_ref")
        split = bool(atom.get("split_required", False))

        ref_section = ""
        ref_page = ""
        if isinstance(hb_ref, dict):
            ref_section = str(hb_ref.get("section", "")).strip()
            ref_page = str(hb_ref.get("page", "")).strip()

        status = "ok"

        if hb_status == "in_handbook" and not verified:
            status = "manual_verification_required"
            add_issue(
                issues, "REVIEW", "handbook_claim_unverified",
                chapter=doc.chapter, concept_id=cid, file=str(doc.path),
                message=f"{cid} is marked in_handbook but handbook_verified is false.",
                recommendation="Verify the section/page directly against the designated FE Reference Handbook edition before release.",
            )

        if hb_status == "in_handbook_memorize_anyway" and not verified:
            status = "manual_verification_required"
            add_issue(
                issues, "REVIEW", "handbook_memorize_claim_unverified",
                chapter=doc.chapter, concept_id=cid, file=str(doc.path),
                message=f"{cid} claims Handbook availability plus memorize-anyway status, but the Handbook reference is not verified.",
                recommendation="Verify the cited Handbook location before keeping this classification.",
            )

        if split:
            status = "split_required"
            add_issue(
                issues, "REVIEW", "source_split_required",
                chapter=doc.chapter, concept_id=cid, file=str(doc.path),
                message=f"{cid} has split_required: true.",
                recommendation="Before release, separate or clearly label lookup material from memorize/guide-developed material.",
            )

        rows.append({
            "chapter": doc.chapter,
            "track": doc.track,
            "concept_id": cid,
            "handbook_status": hb_status,
            "handbook_verified": verified,
            "split_required": split,
            "handbook_section": ref_section,
            "handbook_page": ref_page,
            "audit_status": status,
            "notes": excerpt(str(atom.get("notes", "")), 300),
        })

    # Scan the chapter itself for absolute/high-confidence claims that may need
    # source confirmation. These are REVIEW flags, not presumed errors.
    body_plain = strip_markdown(doc.body)
    claim_hits = []
    for patt in SUSPICIOUS_CLAIM_PATTERNS:
        for m in re.finditer(patt, body_plain, re.I):
            claim_hits.append(m.group(0))
            if len(claim_hits) >= 10:
                break
        if len(claim_hits) >= 10:
            break

    if claim_hits and not handbook_section:
        add_issue(
            issues, "REVIEW", "strong_claim_without_source_boundary",
            chapter=doc.chapter, file=str(doc.path),
            message=f"Chapter contains strong/absolute wording ({', '.join(sorted(set(claim_hits))[:6])}) without a Handbook/source-boundary section.",
            recommendation="Review absolute statements for technical scope, exceptions, and sourcing.",
        )

    return rows


# ---------------------------------------------------------------------------
# Chapter-level audit
# ---------------------------------------------------------------------------

def audit_chapter_level(
    doc: ChapterDoc,
    chapter_atoms: list[dict[str, Any]],
    issues: list[Issue],
) -> dict[str, Any]:
    headings = split_h2_sections(doc.raw)
    heading_names = [h for h, _ in headings]
    objective_section = find_h2(doc.raw, "Learning Objectives")
    key_terms = find_h2(doc.raw, "Key Terms")
    where_wrong = find_h2(doc.raw, "Where This Goes Wrong")

    placeholder = has_placeholder(doc.body)
    if placeholder:
        add_issue(
            issues, "ERROR", "chapter_placeholder",
            chapter=doc.chapter, file=str(doc.path),
            excerpt_text=doc.body,
            message=f"Student-facing chapter text contains placeholder/editorial token '{placeholder}'.",
            recommendation="Complete or remove editorial placeholder text.",
        )

    if not objective_section:
        add_issue(
            issues, "WARNING", "learning_objectives_missing",
            chapter=doc.chapter, file=str(doc.path),
            message="Learning Objectives section is missing.",
            recommendation="Add measurable objectives before final technical review.",
        )

    if not where_wrong:
        add_issue(
            issues, "REVIEW", "failure_modes_section_missing",
            chapter=doc.chapter, file=str(doc.path),
            message="'Where This Goes Wrong' section is missing.",
            recommendation="Add common technical failure modes/misapplications if the chapter template requires them.",
        )

    if not key_terms:
        add_issue(
            issues, "REVIEW", "key_terms_missing",
            chapter=doc.chapter, file=str(doc.path),
            message="Key Terms section is missing.",
            recommendation="Confirm glossary/ledger terminology is represented in the chapter.",
        )

    # Compare introduced term count with terms actually appearing in chapter.
    introduced = []
    for atom in chapter_atoms:
        introduced.extend([str(t) for t in atom.get("introduces_terms", []) or []])

    missing_terms = []
    lower_body = doc.body.lower()
    for term in introduced:
        # Skip very short symbols disguised as terms.
        if len(term.strip()) < 3:
            continue
        if term.lower() not in lower_body:
            missing_terms.append(term)

    if missing_terms:
        add_issue(
            issues, "WARNING", "introduced_terms_not_found_in_chapter",
            chapter=doc.chapter, file=str(doc.path),
            message=f"{len(missing_terms)} ledger-introduced term(s) were not found verbatim in the chapter.",
            recommendation="Check for wording drift, aliases, or ledger/chapter mismatch: " + "; ".join(missing_terms[:12]),
        )

    # Objective count heuristic.
    objective_lines = re.findall(r"(?m)^\s*[*-]\s+\*\*[^*]+\*\*\s+(.+)$", objective_section)
    if objective_section and len(objective_lines) < 3:
        add_issue(
            issues, "REVIEW", "few_learning_objectives",
            chapter=doc.chapter, file=str(doc.path),
            message=f"Only {len(objective_lines)} formatted learning objectives were detected.",
            recommendation="Confirm the chapter has measurable objective coverage for its concept atoms.",
        )

    return {
        "chapter": doc.chapter,
        "track": doc.track,
        "title": doc.title,
        "file": str(doc.path),
        "status": doc.status,
        "concept_atoms": len(chapter_atoms),
        "h2_sections": len(headings),
        "learning_objectives_detected": len(objective_lines),
        "introduced_terms": len(introduced),
        "introduced_terms_missing_verbatim": len(missing_terms),
        "worked_examples": len(extract_worked_examples(doc)),
        "formulas": len(extract_math_blocks(doc.raw)),
        "figures_referenced": len(set(FIG_RE.findall(doc.raw))),
        "has_handbook_boundary": bool(find_h2(doc.raw, "As the Handbook States It")),
        "has_where_wrong": bool(where_wrong),
    }


# ---------------------------------------------------------------------------
# Duplicate-text audit
# ---------------------------------------------------------------------------

def audit_duplicate_text(
    normalized_index: dict[str, list[tuple[str, str, str]]],
    issues: list[Issue],
) -> list[dict[str, Any]]:
    rows = []
    for norm, occurrences in normalized_index.items():
        if len(occurrences) < 2:
            continue

        chapters = sorted(set(x[0] for x in occurrences))
        labels = [f"{c}:{s}" for c, s, _ in occurrences]

        # Exact normalized repetition across >=3 items is especially suspicious.
        sev = "WARNING" if len(occurrences) >= 3 else "REVIEW"
        category = "repeated_solution_text"
        add_issue(
            issues, sev, category,
            chapter=";".join(chapters[:6]),
            excerpt_text=norm,
            message=f"Same normalized solution/explanation text appears {len(occurrences)} times: {labels[:8]}",
            recommendation="Confirm repetition is pedagogically justified; replace template text with item-specific reasoning where appropriate.",
        )

        rows.append({
            "occurrence_count": len(occurrences),
            "chapters": ";".join(chapters),
            "locations": ";".join(labels),
            "normalized_text": norm,
        })
    return rows


# ---------------------------------------------------------------------------
# Main audit
# ---------------------------------------------------------------------------

def audit(
    root: Path,
    ledger_path: Path,
    manifest_path: Path,
    outdir: Path,
    strict: bool = False,
) -> int:
    issues: list[Issue] = []

    ledger = load_yaml(ledger_path)
    concepts = ledger.get("concepts", [])
    if not isinstance(concepts, list):
        raise ValueError("Ledger field 'concepts' must be a list.")

    by_id = {str(c.get("id", "")): c for c in concepts if c.get("id")}
    by_chapter: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for c in concepts:
        ch = str(c.get("chapter", "")).strip()
        if is_layer3_chapter(ch):
            by_chapter[ch].append(c)

    _, manifest_rows = load_csv(manifest_path)
    manifest_by_id = {
        str(r.get("Figure ID", "")).strip(): r
        for r in manifest_rows if str(r.get("Figure ID", "")).strip()
    }

    chapters = discover_chapters(root, issues)

    chapter_rows = []
    worked_rows = []
    formula_rows = []
    assessment_rows = []
    figure_rows = []
    source_rows = []
    numerical_rows = []
    duplicate_index: dict[str, list[tuple[str, str, str]]] = defaultdict(list)

    for ch in sorted(chapters, key=lambda x: chapter_num(x) or 999):
        doc = chapters[ch]
        atoms = by_chapter.get(ch, [])

        chapter_rows.append(audit_chapter_level(doc, atoms, issues))
        formula_rows.extend(audit_formulas(doc, issues))
        worked_rows.extend(audit_worked_examples(doc, issues, duplicate_index))
        assessment_rows.extend(audit_assessments(doc, issues, duplicate_index))
        figure_rows.extend(audit_figures(doc, manifest_by_id, issues))
        source_rows.extend(audit_sources(doc, atoms, issues))

        # Simple arithmetic consistency checks across the chapter.
        for row in arithmetic_checks(doc.raw):
            row.update({
                "chapter": ch,
                "file": str(doc.path),
            })
            numerical_rows.append(row)
            if row["status"] == "mismatch":
                add_issue(
                    issues, "ERROR", "simple_arithmetic_mismatch",
                    chapter=ch, file=str(doc.path),
                    excerpt_text=row["expression"],
                    message=f"Explicit arithmetic statement appears inconsistent: stated {row['stated']}, computed {row['expected']:.12g}.",
                    recommendation="Verify the arithmetic and any unit conversion surrounding this statement.",
                )

    duplicate_rows = audit_duplicate_text(duplicate_index, issues)

    # Coverage sanity.
    for n in range(1, 96):
        ch = f"03-{n:02d}"
        if ch not in chapters:
            add_issue(
                issues, "CRITICAL", "chapter_missing",
                chapter=ch,
                message="Layer 3 chapter is missing from technical audit scope.",
                recommendation="Restore the chapter before release review.",
            )

    # Output.
    outdir.mkdir(parents=True, exist_ok=True)

    issues.sort(key=Issue.key)
    write_csv(
        outdir / "Technical-Audit-Issues.csv",
        [asdict(i) for i in issues],
        ["severity", "category", "chapter", "section", "concept_id", "figure_id",
         "file", "excerpt", "message", "recommendation"],
    )

    write_csv(
        outdir / "Technical-Audit-Chapters.csv",
        chapter_rows,
        ["chapter", "track", "title", "file", "status", "concept_atoms",
         "h2_sections", "learning_objectives_detected", "introduced_terms",
         "introduced_terms_missing_verbatim", "worked_examples", "formulas",
         "figures_referenced", "has_handbook_boundary", "has_where_wrong"],
    )

    write_csv(
        outdir / "Technical-Audit-Worked-Examples.csv",
        worked_rows,
        ["chapter", "track", "file", "example", "problem_words", "solution_words",
         "problem_has_number", "solution_has_number", "problem_has_unit",
         "solution_has_unit", "generic_score", "flags", "problem_excerpt",
         "solution_excerpt"],
    )

    write_csv(
        outdir / "Technical-Audit-Formulas.csv",
        formula_rows,
        ["chapter", "file", "formula_index", "kind", "formula", "status", "flags"],
    )

    write_csv(
        outdir / "Technical-Audit-Assessments.csv",
        assessment_rows,
        ["chapter", "track", "file", "section_type", "number", "word_count",
         "has_number", "generic_score", "flags", "excerpt"],
    )

    write_csv(
        outdir / "Technical-Audit-Figures.csv",
        figure_rows,
        ["chapter", "track", "file", "figure_id", "inline_alt", "manifest_type",
         "manifest_description", "manifest_alt", "manifest_status", "flags"],
    )

    write_csv(
        outdir / "Technical-Audit-Sources.csv",
        source_rows,
        ["chapter", "track", "concept_id", "handbook_status", "handbook_verified",
         "split_required", "handbook_section", "handbook_page", "audit_status", "notes"],
    )

    write_csv(
        outdir / "Technical-Audit-Duplicate-Text.csv",
        duplicate_rows,
        ["occurrence_count", "chapters", "locations", "normalized_text"],
    )

    write_csv(
        outdir / "Technical-Audit-Numerical-Checks.csv",
        numerical_rows,
        ["chapter", "file", "expression", "a", "operator", "b", "stated",
         "expected", "difference", "status"],
    )

    counts = Counter(i.severity for i in issues)
    categories = Counter(i.category for i in issues)

    fail = counts["CRITICAL"] > 0 or counts["ERROR"] > 0
    strict_fail = strict and (counts["WARNING"] > 0 or counts["REVIEW"] > 0)

    if fail:
        audit_status = "FAIL"
    elif strict_fail:
        audit_status = "FAIL (STRICT REVIEW)"
    elif counts["WARNING"] or counts["REVIEW"]:
        audit_status = "PASS WITH TECHNICAL REVIEW REQUIRED"
    else:
        audit_status = "PASS"

    high = [i for i in issues if i.severity in {"CRITICAL", "ERROR", "WARNING", "REVIEW"}]

    summary = [
        "# Layer 3 Technical Audit Summary",
        "",
        f"**Audit status:** {audit_status}  ",
        f"**Root:** `{root}`  ",
        f"**Ledger:** `{ledger_path}`  ",
        f"**Figure manifest:** `{manifest_path}`  ",
        "",
        "## Scope",
        "",
        f"- Layer 3 chapters reviewed: **{len(chapters)} / 95**",
        f"- Layer 3 concept atoms in ledger: **{sum(len(v) for v in by_chapter.values())}**",
        f"- Worked examples parsed: **{len(worked_rows)}**",
        f"- Display formulas parsed: **{len(formula_rows)}**",
        f"- Answer/practice-solution entries parsed: **{len(assessment_rows)}**",
        f"- Figure references reviewed: **{len(figure_rows)}**",
        f"- Source/Handbook atom records reviewed: **{len(source_rows)}**",
        f"- Simple arithmetic statements checked: **{len(numerical_rows)}**",
        "",
        "## Issue counts",
        "",
        f"- CRITICAL: **{counts['CRITICAL']}**",
        f"- ERROR: **{counts['ERROR']}**",
        f"- WARNING: **{counts['WARNING']}**",
        f"- REVIEW: **{counts['REVIEW']}**",
        f"- INFO: **{counts['INFO']}**",
        "",
        "## Interpretation",
        "",
        "- **CRITICAL** — chapter/file is unavailable or audit scope is incomplete.",
        "- **ERROR** — concrete defect such as placeholder content, malformed equation, or arithmetic mismatch.",
        "- **WARNING** — likely technical-content weakness requiring correction or close review.",
        "- **REVIEW** — cannot be decided mechanically; requires engineering/editorial verification.",
        "- **INFO** — status note, usually figure artwork not yet technically verified.",
        "",
        "## Highest-priority findings",
        "",
    ]

    if not high:
        summary.append("No CRITICAL, ERROR, WARNING, or REVIEW findings were generated.")
    else:
        for i in high[:100]:
            loc = " / ".join(x for x in [i.chapter, i.section, i.concept_id, i.figure_id] if x)
            loc = f" ({loc})" if loc else ""
            summary.append(f"- **{i.severity} — {i.category}**{loc}: {i.message}")

    summary += [
        "",
        "## Category counts",
        "",
    ]
    for cat, n in sorted(categories.items(), key=lambda kv: (-kv[1], kv[0])):
        summary.append(f"- `{cat}`: {n}")

    summary += [
        "",
        "## Recommended review order",
        "",
        "1. Resolve CRITICAL and ERROR findings.",
        "2. Replace generic/template worked-example and practice-solution text.",
        "3. Verify every numeric example that lacks a numeric final result or units.",
        "4. Review repeated answer/solution text for copy/template artifacts.",
        "5. Verify Handbook/source claims marked unverified or split_required.",
        "6. Perform figure engineering QA after artwork is generated.",
        "7. Manually sample clean chapters for formula/model correctness because automated checks cannot prove engineering validity.",
        "",
        "## Important limitation",
        "",
        "A PASS from this script means the manuscript passed the implemented technical-content heuristics. It is **not** a certification that every equation, calculation, model assumption, source claim, or figure is technically correct. Final release still requires domain review of formulas, worked examples, practice solutions, and source support.",
        "",
    ]

    (outdir / "Technical-Audit-Summary.md").write_text("\n".join(summary), encoding="utf-8")

    print(f"Layer 3 technical audit: {audit_status}")
    print(
        f"  CRITICAL={counts['CRITICAL']}  ERROR={counts['ERROR']}  "
        f"WARNING={counts['WARNING']}  REVIEW={counts['REVIEW']}  INFO={counts['INFO']}"
    )
    print(f"  Output: {outdir}")

    return 1 if (fail or strict_fail) else 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Perform a technical-content audit of FE Supplemental Guide Layer 3."
    )
    ap.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Any directory inside the FE-Study-Guide repository.",
    )
    ap.add_argument(
        "--ledger",
        type=Path,
        help="Optional override. Default: <root>/meta/ledger.yaml",
    )
    ap.add_argument(
        "--manifest",
        type=Path,
        help="Optional override. Default: <root>/figures/figure-manifest.csv",
    )
    ap.add_argument(
        "--out",
        type=Path,
        help="Optional output folder. Default: <root>/tools/validation/layer3-technical-audit",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Return failing exit code when WARNING or REVIEW findings remain.",
    )
    ap.add_argument(
        "--show-paths",
        action="store_true",
        help="Print normalized paths and exit.",
    )
    args = ap.parse_args()

    root = normalize_project_root(args.root)

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
    outdir = (
        args.out.expanduser().resolve()
        if args.out
        else canonical_path(root, "output")
    )

    print("Normalized FE project paths:")
    print(f"  root:     {root}")
    print(f"  ledger:   {ledger}")
    print(f"  manifest: {manifest}")
    print(f"  layer3:   {canonical_path(root, 'layer3_root')}")
    print(f"  output:   {outdir}")

    if args.show_paths:
        return 0

    if not looks_like_project_root(root):
        print(
            "ERROR: could not normalize to an FE-Study-Guide root containing "
            "meta/ledger.yaml, figures/figure-manifest.csv, and "
            "layer-3-tracks/Layer-3-Chapter-Map.md.",
            file=sys.stderr,
        )
        return 2

    for label, path in [("ledger", ledger), ("manifest", manifest)]:
        try:
            if not path.is_file():
                print(f"ERROR: {label} file is missing: {path}", file=sys.stderr)
                return 2
        except PermissionError:
            print(f"ERROR: permission denied reading {label}: {path}", file=sys.stderr)
            print(
                "If this is OneDrive Files On-Demand, mark the file/folder "
                "'Always keep on this device' and rerun.",
                file=sys.stderr,
            )
            return 2

    try:
        return audit(
            root=root,
            ledger_path=ledger,
            manifest_path=manifest,
            outdir=outdir,
            strict=args.strict,
        )
    except PermissionError as e:
        print(f"ERROR: permission denied during technical audit: {e.filename or e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"ERROR: technical audit failed: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
