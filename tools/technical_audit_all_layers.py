#!/usr/bin/env python3
"""
technical_audit_all_layers.py
=========================

Consolidated technical-content audit for FE Supplemental Guide Layers 1, 2, and 3 (v3).

Revision 6 adds generated-artwork discovery.  By default the audit now checks
figures/png/<Figure ID>.png and figures/svg/<Figure ID>.svg, reports generated
artwork counts, flags incomplete PNG/SVG pairs, and preserves manifest Status as
the engineering-QA gate.  It also retains the arithmetic and source-split fixes from
prior revisions.

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
    png/
      FIG-xx-xx-xxx.png
    svg/
      FIG-xx-xx-xxx.svg
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
tools/validation/technical-audit/

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
* Figure references, alt-text quality, descriptions, manifest status, and PNG/SVG file presence
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
    python .\tools\technical_audit_all_layers.py

From tools/:
    python .\technical_audit_all_layers.py

Show normalized paths only:
    python .\technical_audit_all_layers.py --show-paths

Treat REVIEW items as a failing exit status:
    python .\technical_audit_all_layers.py --strict
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import re
import ast
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
    "png_dir": Path("figures") / "png",
    "svg_dir": Path("figures") / "svg",
    "map": Path("layer-3-tracks") / "Layer-3-Chapter-Map.md",
    "output": Path("tools") / "validation" / "technical-audit",
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
)

SEVERITY_ORDER = {
    "CRITICAL": 0,
    "ERROR": 1,
    "WARNING": 2,
    "REVIEW": 3,
    "INFO": 4,
}

FIG_RE = re.compile(r"\bFIG-(?:01|02|03)-\d{2}-\d{3}\b")
CHAPTER_RE = re.compile(r"^(0[123])-(\d{2})$")
NUM_TOKEN_RE = re.compile(r"(?<![\w.-])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")
UNIT_TOKEN_RE = re.compile(
    r"\b(?:V|A|W|kW|MW|mW|Pa|kPa|MPa|psi|psf|ksi|pcf|N|kN|lbf|lbm|lb|kip|kg|g|"
    r"m|mm|cm|km|in|ft|yd|mi|s|min|h|hr|day|Hz|kHz|MHz|rad|deg|°C|°F|K|J|kJ|MJ|Btu|"
    r"mol|kmol|m/s|m/s\^2|ft/s|ft/s\^2|mi/hr|veh/hr|in/hr|cfs|gpm|cfm|rpm|"
    r"m\^2|m\^3|ft\^2|ft\^3|in\^2|in\^3|yd\^2|yd\^3|"
    r"m²|m³|ft²|ft³|in²|in³|yd²|yd³|"
    r"kip/ft|lb/ft|lbf/ft|lb/ft\^2|lb/ft²|lb/in\^2|lb/in²|acre|acres|"
    r"L|mL|gal|ohm|Ω|F|H|S|C|ppm|ppb|mg/L|g/L|kg/m\^3|kg/m³|Pa·s|cP|"
    r"W/m\^2|W/m²|W/m·K|W/m-K)\b"
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

# Simple standalone arithmetic statement, e.g. "24 × 2 = 48", "12 / 3 = 4".
#
# The earlier version could begin matching in the middle of a longer equation
# such as "100 + 0.020×100 = 102" and incorrectly audit only "0.020×100 = 102".
# This version requires a clean boundary around the full three-number
# expression. Ambiguous expressions are retained for REVIEW rather than ERROR.
SIMPLE_ARITH_RE = re.compile(
    r"(?<![\w\d\)\]\}%])"
    r"(?P<a>[-+]?\d+(?:\.\d+)?)\s*"
    r"(?P<op>[×xX*/+\-÷])\s*"
    r"(?P<b>[-+]?\d+(?:\.\d+)?)\s*=\s*"
    r"(?P<c>[-+]?\d+(?:\.\d+)?)"
    r"(?![\w\d\(\[\{%])"
)

# Operators/tokens that indicate the regex may still be looking at a fragment
# of a larger algebraic or LaTeX expression.
ARITH_FRAGMENT_LEFT_RE = re.compile(
    r"(?:[+\-*/×÷=^_(\[{]|\\(?:frac|sqrt|left|right|cdot|times|pm|Delta|sum))\s*$"
)
ARITH_FRAGMENT_RIGHT_RE = re.compile(
    r"^\s*(?:[+\-*/×÷=^_)\]}]|\\(?:frac|sqrt|left|right|cdot|times|pm|Delta|sum))"
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


def chapter_layer(ch: str) -> Optional[int]:
    m = CHAPTER_RE.match(str(ch).strip())
    return int(m.group(1)) if m else None


def chapter_local_num(ch: str) -> Optional[int]:
    m = CHAPTER_RE.match(str(ch).strip())
    return int(m.group(2)) if m else None


def chapter_num(ch: str) -> Optional[int]:
    """Sortable numeric key: layer 1 < layer 2 < layer 3."""
    layer = chapter_layer(ch)
    local = chapter_local_num(ch)
    return (layer * 1000 + local) if layer is not None and local is not None else None


def is_supported_chapter(ch: str) -> bool:
    layer = chapter_layer(ch)
    local = chapter_local_num(ch)
    return layer in {1, 2, 3} and local is not None and local >= 1


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
    if not is_supported_chapter(ch):
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


def discover_chapters(
    root: Path,
    issues: list[Issue],
    selected_layers: set[int],
    chapter_roots: Optional[list[Path]] = None,
) -> dict[str, ChapterDoc]:
    """
    Discover chapter Markdown files for Layers 1/2/3.

    Default behavior scans the repository recursively while excluding generated,
    metadata, tooling, archive, and dependency folders.  --chapter-root may be
    supplied one or more times to restrict discovery to known manuscript roots.
    """
    chapters: dict[str, ChapterDoc] = {}
    excluded_parts = {
        ".git", ".github", ".venv", "venv", "node_modules",
        "tools", "figures", "meta", "references",
        "archive", "archives", "backup", "backups",
        "__pycache__",
    }

    roots = chapter_roots or [root]
    candidate_paths: list[Path] = []
    for scan_root in roots:
        scan_root = scan_root.expanduser().resolve()
        if not scan_root.exists():
            add_issue(
                issues, "CRITICAL", "chapter_root_missing",
                file=str(scan_root),
                message="Configured chapter discovery root does not exist.",
                recommendation="Correct --chapter-root or restore the manuscript directory.",
            )
            continue
        try:
            iterable = scan_root.rglob("*.md")
            for path in iterable:
                try:
                    rel = path.resolve().relative_to(root)
                except Exception:
                    rel = path.resolve()
                parts_lower = {str(p).lower() for p in getattr(rel, "parts", ())}
                if parts_lower & excluded_parts:
                    continue
                if not re.match(r"^(?:01|02|03)-\d{2}-", path.name, re.I):
                    continue
                prefix_layer = int(path.name[:2])
                if prefix_layer not in selected_layers:
                    continue
                candidate_paths.append(path)
        except (PermissionError, OSError) as e:
            add_issue(
                issues, "CRITICAL", "chapter_root_unreadable",
                file=str(scan_root),
                message=f"Cannot scan chapter directory: {e}",
                recommendation="Make the directory locally available/readable and rerun.",
            )

    for path in sorted(set(candidate_paths)):
        doc = parse_frontmatter(path)
        if not doc:
            add_issue(
                issues, "ERROR", "chapter_unparseable",
                file=str(path),
                message="Could not parse chapter YAML frontmatter.",
                recommendation="Repair YAML frontmatter before technical review.",
            )
            continue
        layer = chapter_layer(doc.chapter)
        if layer not in selected_layers:
            continue
        if doc.chapter in chapters:
            add_issue(
                issues, "ERROR", "duplicate_chapter_document",
                chapter=doc.chapter, file=str(path),
                message="More than one technical-review candidate claims this chapter number.",
                recommendation="Keep one authoritative chapter file or restrict discovery with --chapter-root.",
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
    s = re.sub(r"\bfig-(?:01|02|03)-\d{2}-\d{3}\b", "<fig>", s)
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


def _safe_numeric_expression(expr: str) -> float | None:
    """
    Evaluate a numeric-only arithmetic expression safely.

    Supported:
      * decimal / integer literals
      * unary + and -
      * +, -, *, /
      * parentheses
      * ×, x, X, and ÷ as multiplication/division glyphs

    Any variable, function, LaTeX command, exponent operator, or other token
    causes the expression to be rejected rather than partially evaluated.
    """
    expr = expr.strip()
    if not expr:
        return None

    expr = (
        expr.replace("×", "*")
            .replace("÷", "/")
            .replace("−", "-")
    )

    expr = re.sub(r"(?<=[0-9\)])\s*[xX]\s*(?=[0-9\(])", "*", expr)

    if not re.fullmatch(r"[0-9eE.\s()+\-*/]+", expr):
        return None

    if not re.search(r"(?<=[0-9\)])\s*[+\-*/]\s*(?=[+\-]?(?:\d|\())", expr):
        return None

    try:
        node = ast.parse(expr, mode="eval")
    except SyntaxError:
        return None

    allowed_binops = (ast.Add, ast.Sub, ast.Mult, ast.Div)
    allowed_unary = (ast.UAdd, ast.USub)

    def eval_node(n):
        if isinstance(n, ast.Expression):
            return eval_node(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, allowed_unary):
            value = eval_node(n.operand)
            return value if isinstance(n.op, ast.UAdd) else -value
        if isinstance(n, ast.BinOp) and isinstance(n.op, allowed_binops):
            left = eval_node(n.left)
            right = eval_node(n.right)
            if isinstance(n.op, ast.Add):
                return left + right
            if isinstance(n.op, ast.Sub):
                return left - right
            if isinstance(n.op, ast.Mult):
                return left * right
            if isinstance(n.op, ast.Div):
                if right == 0:
                    raise ZeroDivisionError
                return left / right
        raise ValueError("unsupported expression")

    try:
        return float(eval_node(node))
    except (ValueError, TypeError, ZeroDivisionError, OverflowError):
        return None


def arithmetic_checks(text: str) -> list[dict[str, Any]]:
    """
    Check complete numeric arithmetic equalities while ignoring symbolic algebra.

    Earlier versions searched for a three-number substring such as a op b = c.
    That could audit only a fragment of a longer expression, for example:

        Q = 2×4×20 = 160
        ΔH = -100 + 0.020×100 = -98
        F = C + 2 - P = 2 + 2 - 2 = 2

    This version evaluates the entire numeric field immediately to the left of
    an equals sign. Algebraic fields containing variables are skipped. Thus
    compound numeric arithmetic is checked as a whole instead of producing
    false mismatches from internal fragments.
    """
    rows: list[dict[str, Any]] = []
    seen: set[tuple[int, str, str]] = set()

    result_re = re.compile(
        r"^\s*(?P<c>[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)"
        r"(?P<tail>.*)$"
    )

    for line_no, raw_line in enumerate(text.splitlines(), 1):
        if "=" not in raw_line:
            continue

        line = raw_line.replace(r"\[", " ").replace(r"\]", " ").replace("$$", " ")
        parts = line.split("=")
        if len(parts) < 2:
            continue

        for i in range(len(parts) - 1):
            lhs = parts[i].strip()
            rhs = parts[i + 1]

            expected = _safe_numeric_expression(lhs)
            if expected is None:
                continue

            rm = result_re.match(rhs)
            if not rm:
                continue

            stated = float(rm.group("c"))
            tail = rm.group("tail")

            if tail:
                if re.match(r"^[A-Za-z_\\(]", tail):
                    continue
                if re.match(r"^\s*[+\-*/×÷xX^]", tail):
                    continue
                if re.match(r"^[%]", tail):
                    pass
                elif re.match(r"^\s+[A-Za-zµμ°%]", tail):
                    pass
                elif re.match(r"^\s*[\.,;:\)\]\}]*\s*$", tail):
                    pass
                elif tail.strip():
                    continue

            tol = max(1e-9, abs(expected) * 0.015)
            math_ok = abs(expected - stated) <= tol
            if not math_ok:
                math_ok = arithmetic_display_equivalent(expected, stated, raw_line, tol)

            expression = f"{lhs}={rm.group('c')}"
            context = raw_line.strip()
            key = (line_no, expression, context)
            if key in seen:
                continue
            seen.add(key)

            op_count = len(re.findall(r"[+\-*/×÷xX]", lhs))
            rows.append({
                "expression": expression,
                "line_number": line_no,
                "context": context,
                "a": "",
                "operator": "compound" if op_count > 1 else "simple",
                "b": "",
                "stated": stated,
                "expected": expected,
                "difference": stated - expected,
                "math_status": "ok" if math_ok else "mismatch",
                "confidence": "high",
                "ambiguity_reason": "",
                "status": "ok" if math_ok else "mismatch_high_confidence",
            })

    return rows


def arithmetic_display_equivalent(expected: float, stated: float, raw_line: str, tol: float) -> bool:
    """Recognize equivalent percent or scaled-unit display values."""
    line = raw_line.replace("µ", "u").replace("μ", "u")

    if "%" in line:
        percent_tol = max(abs(stated) * 0.015, 1e-9)
        if abs(expected * 100.0 - stated) <= percent_tol:
            return True

    # Unit following the RHS number.
    m = re.search(
        r"=\s*[+\-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+\-]?\d+)?\s*"
        r"(ms|us|ns|mV|uV|kV|mA|uA|kA|mW|kW|MW|mm|cm|km|mg|ug|kg)\b",
        line,
    )
    if not m:
        return False

    unit = m.group(1)
    factors = {
        "ms": 1e-3, "us": 1e-6, "ns": 1e-9,
        "mV": 1e-3, "uV": 1e-6, "kV": 1e3,
        "mA": 1e-3, "uA": 1e-6, "kA": 1e3,
        "mW": 1e-3, "kW": 1e3, "MW": 1e6,
        "mm": 1e-3, "cm": 1e-2, "km": 1e3,
        "mg": 1e-3, "ug": 1e-6, "kg": 1e3,
    }
    factor = factors.get(unit)
    if factor is None:
        return False

    converted = stated * factor
    return abs(expected - converted) <= max(abs(expected) * 0.015, tol, 1e-12)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'’-]+\b", strip_markdown(text)))


# ---------------------------------------------------------------------------
# Worked-example extraction
# ---------------------------------------------------------------------------

def has_substantive_unlabeled_solution(block: str) -> bool:
    """Conservatively detect a worked solution when no explicit Solution label exists.

    Some Layer 1 chapters use Given/Find followed directly by equations, or use
    labels such as Hypotheses, Statistic, Critical value, Decision, and
    Conclusion.  This helper prevents those formats from being reported as
    missing-solution ERRORs while still leaving genuinely prompt-only examples
    eligible for that error.
    """
    if not block or word_count(block) < 18:
        return False

    # Strong structural indicators used by the Layer-1 manuscript.
    structural = re.search(
        r"(?mi)^\s*\*\*(?:Hypotheses?|Statistic|Test\s+statistic|Critical\s+value|"
        r"Decision|Conclusion|Interpretation|Sensitivity\s+coefficients?|"
        r"Nominal\s+(?:value|volume)|Relative\s+uncertainty|Degrees?\s+of\s+freedom|"
        r"p[- ]?value|Reject|Fail\s+to\s+reject)\.?\*\*",
        block,
    )
    if structural:
        return True

    # Quantitative reasoning indicators.  Require more than one so a prompt
    # containing a single formula is not mistaken for a completed solution.
    math_blocks = len(re.findall(r"\$\$(.*?)\$\$|\\\[(.*?)\\\]", block, re.S))
    equalities = len(re.findall(r"(?<![<>!])=(?!=)", block))
    result_markers = len(re.findall(
        r"(?i)\\boxed\{|\b(?:therefore|thus|hence|so|approximately|approx\.?|"
        r"reject\s+H_0|fail\s+to\s+reject|final|result)\b",
        block,
    ))

    return (math_blocks >= 2 and equalities >= 2) or (equalities >= 2 and result_markers >= 1)


def count_display_math_delimiters(text: str, bracket: str) -> int:
    """Count true LaTeX display delimiters while ignoring row-spacing commands.

    A real display opener/closer has an odd-length run of backslashes before
    ``[`` or ``]`` (normally one: ``\\[`` / ``\\]``).  Array/cases row spacing
    such as ``\\\\[4pt]`` has an even-length run and must not be counted as a
    display delimiter.
    """
    if bracket not in "[]":
        raise ValueError("bracket must be '[' or ']'")

    count = 0
    for i, ch in enumerate(text):
        if ch != bracket:
            continue
        j = i - 1
        nslashes = 0
        while j >= 0 and text[j] == "\\":
            nslashes += 1
            j -= 1
        if nslashes % 2 == 1:
            count += 1
    return count


def extract_worked_examples(doc: ChapterDoc) -> list[dict[str, Any]]:
    """
    Extract Worked Example blocks across Layers 1, 2, and 3.

    Supports Layer-1 style Given/Find/Approach/Solution blocks, Layer-2/3
    Problem/Solution blocks, and early Layer-2 solution-only "Model Check"
    examples without treating format differences as concrete parser errors.
    """
    matches = list(re.finditer(r"(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$", doc.raw))
    examples = []

    solution_marker_re = re.compile(
        r"(?mi)^\s*\*\*(?:"
        r"Solution(?:\s*[—:\-]\s*[^*]+)?|"
        r"Approach(?:\s*[—:\-]\s*[^*]+)?|"
        r"Fast\s+approach(?:\s*[—:\-]\s*[^*]+)?|"
        r"Calculation(?:\s*[—:\-]\s*[^*]+)?|"
        r"Work(?:\s*[—:\-]\s*[^*]+)?|"
        r"Analysis(?:\s*[—:\-]\s*[^*]+)?|"
        r"Answer(?:\s*[—:\-]\s*[^*]+)?|"
        r"Verification(?:\s*[—:\-]\s*[^*]+)?|"
        r"Check(?:\s*[—:\-]\s*[^*]+)?"
        r")\.?\*\*\s*"
    )
    prompt_marker_re = re.compile(
        r"(?mi)^\s*\*\*(?:Problem|Given|Find|Question|Scenario|Task|Asked)\.?\*\*\s*"
    )

    for i, m in enumerate(matches):
        start_block = m.end()
        end_block = matches[i + 1].start() if i + 1 < len(matches) else len(doc.raw)

        next_h2 = re.search(r"(?m)^##\s+", doc.raw[start_block:end_block])
        if next_h2:
            end_block = start_block + next_h2.start()

        block = doc.raw[start_block:end_block].strip()
        label = (m.group(1) or str(i + 1)).strip()

        sm = solution_marker_re.search(block)
        pre_solution = block[:sm.start()].strip() if sm else block
        post_solution = block[sm.end():].strip() if sm else ""
        prompt_markers = list(prompt_marker_re.finditer(pre_solution))

        if prompt_markers:
            problem = prompt_marker_re.sub("", pre_solution).strip()
        elif block:
            problem = label
        else:
            problem = ""

        if sm:
            solution = post_solution
        elif prompt_markers and has_substantive_unlabeled_solution(block):
            # Some Layer-1 worked examples use Given/Find and then proceed
            # directly into equations or headings such as Hypotheses/Statistic.
            # Treat the full block as the worked solution for audit purposes.
            solution = block
        elif prompt_markers:
            solution = ""
        else:
            solution = block

        examples.append({
            "label": label,
            "problem": problem,
            "solution": solution,
            "block": block,
            "implicit_prompt": bool(block and not prompt_markers),
        })
    return examples


# ---------------------------------------------------------------------------
# Formula audit
# ---------------------------------------------------------------------------

def audit_formulas(doc: ChapterDoc, issues: list[Issue]) -> list[dict[str, Any]]:
    rows = []
    blocks = extract_math_blocks(doc.raw)

    # Raw delimiter sanity. Ignore array/cases row-spacing commands such as
    # \\[4pt], \\[2mm], etc.; those contain an even number of backslashes and
    # are not display-math openers.
    open_display = count_display_math_delimiters(doc.raw, "[")
    close_display = count_display_math_delimiters(doc.raw, "]")
    if open_display != close_display:
        add_issue(
            issues, "ERROR", "math_delimiter_mismatch",
            chapter=doc.chapter, file=str(doc.path),
            message=(
                rf"Count of true \\[ and \\] display-math delimiters does not match "
                f"({open_display} open, {close_display} close)."
            ),
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


def build_artwork_index(primary_dir: Path, extension: str) -> dict[str, list[Path]]:
    """
    Recursively index artwork by Figure ID from both the configured format
    directory and its parent figures directory.

    Accepts exact filenames and descriptive filenames such as
    FIG-01-14-003-cofactor-expansion.png. Archive/archives/backup/backups\n    directories are excluded from live-artwork duplicate checks.\n    """
    roots: list[Path] = []
    for candidate in (primary_dir, primary_dir.parent):
        if candidate.exists():
            candidate = candidate.resolve()
            if candidate not in roots:
                roots.append(candidate)

    patt = re.compile(r"FIG-(?:01|02|03)-\d{2}-\d{3}", re.I)
    index: dict[str, list[Path]] = defaultdict(list)
    seen: set[Path] = set()

    excluded_artwork_dirs = {"archive", "archives", "backup", "backups"}

    for root_dir in roots:
        for path in root_dir.rglob(f"*{extension.lower()}"):
            if not path.is_file():
                continue

            # Archived/backup artwork is intentionally retained for history but
            # must not compete with the live file for duplicate-artwork checks.
            try:
                rel_parts = {p.lower() for p in path.relative_to(root_dir).parts[:-1]}
            except Exception:
                rel_parts = {p.lower() for p in path.parts[:-1]}
            if rel_parts & excluded_artwork_dirs:
                continue

            rp = path.resolve()
            if rp in seen:
                continue
            seen.add(rp)
            m = patt.search(path.stem)
            if m:
                index[m.group(0).upper()].append(path)
    return index


# ---------------------------------------------------------------------------
# Figure audit
# ---------------------------------------------------------------------------

def audit_figures(
    doc: ChapterDoc,
    manifest_by_id: dict[str, dict[str, str]],
    issues: list[Issue],
    png_dir: Path,
    svg_dir: Path,
    artwork_mode: str = "both",
    png_index: Optional[dict[str, list[Path]]] = None,
    svg_index: Optional[dict[str, list[Path]]] = None,
) -> list[dict[str, Any]]:
    """Audit figure metadata plus generated artwork file presence.

    Expected default layout:
        <root>/figures/png/FIG-xx-xx-xxx.png
        <root>/figures/svg/FIG-xx-xx-xxx.svg

    artwork_mode controls which formats constitute a complete artwork set:
      - both: require PNG and SVG (project default)
      - either: one of PNG/SVG is sufficient
      - png: require PNG only
      - svg: require SVG only

    File presence does not certify engineering accuracy.  The manifest Status field
    remains the QA gate.  Statuses such as verified/artwork_verified/qa_verified,
    approved, complete, or final are treated as artwork QA complete.
    """
    rows = []
    seen = set()
    verified_statuses = {
        "verified", "artwork_verified", "qa_verified", "approved", "complete", "final"
    }

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
        status_norm = status.lower().replace("-", "_").replace(" ", "_")
        qa_verified = status_norm in verified_statuses
        flags = []

        fid_key = fid.upper()
        png_candidates = (png_index or {}).get(fid_key, [])
        svg_candidates = (svg_index or {}).get(fid_key, [])

        png_path = png_candidates[0] if png_candidates else (png_dir / f"{fid}.png")
        svg_path = svg_candidates[0] if svg_candidates else (svg_dir / f"{fid}.svg")
        png_exists = png_path.is_file()
        svg_exists = svg_path.is_file()
        png_bytes = png_path.stat().st_size if png_exists else 0
        svg_bytes = svg_path.stat().st_size if svg_exists else 0

        if len(png_candidates) > 1:
            flags.append("duplicate_png_candidates")
            add_issue(
                issues, "WARNING", "figure_png_duplicate_candidates",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                message=f"Multiple PNG files map to {fid}: " + "; ".join(str(p) for p in png_candidates[:5]),
                recommendation="Keep one authoritative PNG artwork file for this Figure ID.",
            )
        if len(svg_candidates) > 1:
            flags.append("duplicate_svg_candidates")
            add_issue(
                issues, "WARNING", "figure_svg_duplicate_candidates",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                message=f"Multiple SVG files map to {fid}: " + "; ".join(str(p) for p in svg_candidates[:5]),
                recommendation="Keep one authoritative SVG artwork file for this Figure ID.",
            )

        if png_exists and png_bytes == 0:
            flags.append("png_zero_bytes")
            add_issue(
                issues, "ERROR", "figure_png_empty",
                chapter=doc.chapter, figure_id=fid, file=str(png_path),
                message="PNG artwork file exists but is zero bytes.",
                recommendation="Regenerate or replace the PNG artwork file.",
            )
        if svg_exists and svg_bytes == 0:
            flags.append("svg_zero_bytes")
            add_issue(
                issues, "ERROR", "figure_svg_empty",
                chapter=doc.chapter, figure_id=fid, file=str(svg_path),
                message="SVG artwork file exists but is zero bytes.",
                recommendation="Regenerate or replace the SVG artwork file.",
            )

        if png_exists and svg_exists:
            file_state = "both"
        elif png_exists:
            file_state = "png_only"
        elif svg_exists:
            file_state = "svg_only"
        else:
            file_state = "missing"

        if artwork_mode == "both":
            artwork_complete = png_exists and svg_exists and png_bytes > 0 and svg_bytes > 0
        elif artwork_mode == "either":
            artwork_complete = ((png_exists and png_bytes > 0) or (svg_exists and svg_bytes > 0))
        elif artwork_mode == "png":
            artwork_complete = png_exists and png_bytes > 0
        elif artwork_mode == "svg":
            artwork_complete = svg_exists and svg_bytes > 0
        else:  # defensive; argparse constrains this
            artwork_complete = False

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

        # Artwork-file audit.  Missing artwork remains INFO because generation is a
        # planned production backlog.  A partial PNG/SVG pair is a WARNING when both
        # formats are required.  A manifest that claims QA verification while required
        # files are absent is a concrete ERROR.
        if qa_verified and not artwork_complete:
            flags.append("verified_status_but_required_files_missing")
            add_issue(
                issues, "ERROR", "figure_verified_but_files_missing",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                message=(
                    f"Manifest status is '{status}', but required artwork files are incomplete "
                    f"for mode '{artwork_mode}' (PNG={png_exists}, SVG={svg_exists})."
                ),
                recommendation="Restore the required artwork files or change the manifest status until artwork QA is complete.",
            )
        elif not artwork_complete:
            if artwork_mode == "both" and file_state in {"png_only", "svg_only"}:
                flags.append("artwork_pair_incomplete")
                missing_fmt = "SVG" if file_state == "png_only" else "PNG"
                add_issue(
                    issues, "WARNING", "figure_artwork_pair_incomplete",
                    chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                    message=(
                        f"Only one artwork format exists ({file_state}); {missing_fmt} is missing. "
                        f"Expected {png_path.name} and {svg_path.name}."
                    ),
                    recommendation=f"Generate the missing {missing_fmt} counterpart in the configured artwork directory.",
                )
            else:
                flags.append("artwork_missing")
                add_issue(
                    issues, "INFO", "figure_artwork_missing",
                    chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                    message=(
                        f"Required artwork file set is not present for mode '{artwork_mode}' "
                        f"(PNG={png_exists}, SVG={svg_exists})."
                    ),
                    recommendation="Generate the artwork files in figures/png and figures/svg, then perform engineering QA.",
                )
        elif not qa_verified:
            flags.append("artwork_exists_unverified")
            add_issue(
                issues, "INFO", "figure_artwork_not_verified",
                chapter=doc.chapter, figure_id=fid, file=str(doc.path),
                message=(
                    f"Required artwork files exist (PNG={png_exists}, SVG={svg_exists}), but manifest status "
                    f"is '{status or 'blank'}'; technical artwork accuracy has not been verified."
                ),
                recommendation="Conduct visual engineering QA against the chapter and manifest, then mark the manifest status verified.",
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
            "png_path": str(png_path),
            "png_exists": png_exists,
            "png_bytes": png_bytes,
            "svg_path": str(svg_path),
            "svg_exists": svg_exists,
            "svg_bytes": svg_bytes,
            "file_state": file_state,
            "artwork_mode": artwork_mode,
            "artwork_complete": artwork_complete,
            "qa_verified": qa_verified,
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
            notes_text = str(atom.get("notes", ""))
            notes_has_external_source = bool(re.search(
                r"\b(?:external source support|additional external source support|externally supported)\b",
                notes_text,
                re.I,
            ))

            # A split is considered resolved only when the FE-Handbook side is
            # verified, an explicit external-source trail is present in the
            # ledger notes, and the chapter states the three-way source boundary.
            chapter_has_external_support = bool(re.search(
                r"\b(?:external source support|externally supported)\b",
                handbook_section or "",
                re.I,
            ))
            chapter_has_handbook_boundary = bool(re.search(
                r"\bFE[- ]Handbook[- ]supported\b|\bHandbook-supported\b",
                handbook_section or "",
                re.I,
            ))
            chapter_has_guide_synthesis = bool(re.search(
                r"\bguide synthesis\b",
                handbook_section or "",
                re.I,
            ))

            split_resolved = (
                hb_status == "in_handbook"
                and verified
                and bool(ref_section or ref_page)
                and notes_has_external_source
                and chapter_has_external_support
                and chapter_has_handbook_boundary
                and chapter_has_guide_synthesis
            )

            if split_resolved:
                # Do not emit an issue: the split remains a meaningful ledger
                # property, but its release-time source-boundary requirement has
                # been satisfied and should not count as REVIEW.
                status = "split_resolved"
            else:
                status = "split_unresolved"
                missing = []
                if hb_status != "in_handbook":
                    missing.append("handbook_status=in_handbook")
                if not verified:
                    missing.append("handbook_verified=true")
                if not (ref_section or ref_page):
                    missing.append("Handbook section/page")
                if not notes_has_external_source:
                    missing.append("external-source provenance in ledger notes")
                if not chapter_has_external_support:
                    missing.append("externally-supported label in chapter source boundary")
                if not chapter_has_handbook_boundary:
                    missing.append("FE-Handbook-supported label in chapter source boundary")
                if not chapter_has_guide_synthesis:
                    missing.append("guide-synthesis label in chapter source boundary")

                add_issue(
                    issues, "REVIEW", "source_split_unresolved",
                    chapter=doc.chapter, concept_id=cid, file=str(doc.path),
                    message=(
                        f"{cid} has split_required: true but its source boundary is not fully resolved. "
                        f"Missing: {', '.join(missing)}."
                    ),
                    recommendation=(
                        "Verify the FE-Handbook portion, record the external source in the ledger, "
                        "and clearly label FE-Handbook-supported, externally supported, and guide-synthesis material in the chapter."
                    ),
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
    png_dir: Path,
    svg_dir: Path,
    artwork_mode: str = "both",
    strict: bool = False,
    selected_layers: Optional[set[int]] = None,
    chapter_roots: Optional[list[Path]] = None,
) -> int:
    issues: list[Issue] = []

    ledger = load_yaml(ledger_path)
    concepts = ledger.get("concepts", [])
    if not isinstance(concepts, list):
        raise ValueError("Ledger field 'concepts' must be a list.")

    selected_layers = selected_layers or {1, 2, 3}

    by_id = {str(c.get("id", "")): c for c in concepts if c.get("id")}
    by_chapter: dict[str, list[dict[str, Any]]] = defaultdict(list)
    expected_chapters: set[str] = set()
    for c in concepts:
        ch = str(c.get("chapter", "")).strip()
        layer = chapter_layer(ch)
        if is_supported_chapter(ch) and layer in selected_layers:
            by_chapter[ch].append(c)
            expected_chapters.add(ch)

    _, manifest_rows = load_csv(manifest_path)
    manifest_by_id = {
        str(r.get("Figure ID", "")).strip(): r
        for r in manifest_rows if str(r.get("Figure ID", "")).strip()
    }

    chapters = discover_chapters(root, issues, selected_layers, chapter_roots)

    # Build once so nested batch/chapter artwork folders are recognized.
    png_index = build_artwork_index(png_dir, ".png")
    svg_index = build_artwork_index(svg_dir, ".svg")

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
        figure_rows.extend(audit_figures(doc, manifest_by_id, issues, png_dir, svg_dir, artwork_mode, png_index, svg_index))
        source_rows.extend(audit_sources(doc, atoms, issues))

        # Simple arithmetic consistency checks across the chapter.
        # Only high-confidence standalone mismatches are ERRORs. Possible
        # fragments of larger equations are REVIEW items with full context.
        for row in arithmetic_checks(doc.raw):
            row.update({
                "chapter": ch,
                "file": str(doc.path),
            })
            numerical_rows.append(row)

            if row["status"] == "mismatch_high_confidence":
                add_issue(
                    issues, "ERROR", "simple_arithmetic_mismatch",
                    chapter=ch, section=f"line {row['line_number']}", file=str(doc.path),
                    excerpt_text=row["context"],
                    message=(
                        f"Standalone arithmetic statement appears inconsistent: "
                        f"stated {row['stated']}, computed {row['expected']:.12g}."
                    ),
                    recommendation="Verify the arithmetic and any unit conversion surrounding this statement.",
                )
            elif row["status"] == "mismatch_needs_review":
                add_issue(
                    issues, "REVIEW", "simple_arithmetic_ambiguous",
                    chapter=ch, section=f"line {row['line_number']}", file=str(doc.path),
                    excerpt_text=row["context"],
                    message=(
                        f"Possible arithmetic mismatch found inside a larger/ambiguous expression: "
                        f"fragment '{row['expression']}'."
                    ),
                    recommendation=(
                        "Review the full equation context manually. Do not edit the chapter "
                        "based on the arithmetic fragment alone."
                    ),
                )

    duplicate_rows = audit_duplicate_text(duplicate_index, issues)

    # Coverage sanity: expected chapters come from the ledger for the selected layers.
    for ch in sorted(expected_chapters, key=lambda x: chapter_num(x) or 9999):
        if ch not in chapters:
            add_issue(
                issues, "CRITICAL", "chapter_missing",
                chapter=ch,
                message=f"Layer {chapter_layer(ch)} chapter is missing from technical audit scope.",
                recommendation="Restore the chapter, make it locally available, or correct --chapter-root.",
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
         "manifest_description", "manifest_alt", "manifest_status",
         "png_path", "png_exists", "png_bytes", "svg_path", "svg_exists", "svg_bytes",
         "file_state", "artwork_mode", "artwork_complete", "qa_verified", "flags"],
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
        ["chapter", "file", "line_number", "context", "expression", "a", "operator",
         "b", "stated", "expected", "difference", "math_status", "confidence",
         "ambiguity_reason", "status"],
    )

    counts = Counter(i.severity for i in issues)
    categories = Counter(i.category for i in issues)

    figure_file_states = Counter(str(r.get("file_state", "")) for r in figure_rows)
    figure_png_present = sum(bool(r.get("png_exists")) for r in figure_rows)
    figure_svg_present = sum(bool(r.get("svg_exists")) for r in figure_rows)
    figure_complete = sum(bool(r.get("artwork_complete")) for r in figure_rows)
    figure_qa_verified = sum(bool(r.get("qa_verified")) for r in figure_rows)

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
        "# Consolidated FE Technical Audit Summary",
        "",
        f"**Audit status:** {audit_status}  ",
        f"**Root:** `{root}`  ",
        f"**Ledger:** `{ledger_path}`  ",
        f"**Figure manifest:** `{manifest_path}`  ",
        f"**PNG artwork directory:** `{png_dir}`  ",
        f"**SVG artwork directory:** `{svg_dir}`  ",
        f"**Artwork requirement:** `{artwork_mode}`  ",
        "",
        "## Scope",
        "",
        f"- Selected layers: **{', '.join(str(x) for x in sorted(selected_layers))}**",
        f"- Chapters reviewed: **{len(chapters)} / {len(expected_chapters)} expected from ledger**",
        f"- Concept atoms in selected layers: **{sum(len(v) for v in by_chapter.values())}**",
        f"- Worked examples parsed: **{len(worked_rows)}**",
        f"- Display formulas parsed: **{len(formula_rows)}**",
        f"- Answer/practice-solution entries parsed: **{len(assessment_rows)}**",
        f"- Figure references reviewed: **{len(figure_rows)}**",
        f"- Source/Handbook atom records reviewed: **{len(source_rows)}**",
        f"- Simple arithmetic statements checked: **{len(numerical_rows)}**",
        "",
        "## Figure artwork inventory",
        "",
        f"- Referenced figures with PNG present: **{figure_png_present} / {len(figure_rows)}**",
        f"- Referenced figures with SVG present: **{figure_svg_present} / {len(figure_rows)}**",
        f"- Complete artwork sets for mode `{artwork_mode}`: **{figure_complete} / {len(figure_rows)}**",
        f"- Both PNG and SVG present: **{figure_file_states.get('both', 0)}**",
        f"- PNG only: **{figure_file_states.get('png_only', 0)}**",
        f"- SVG only: **{figure_file_states.get('svg_only', 0)}**",
        f"- Neither format present: **{figure_file_states.get('missing', 0)}**",
        f"- Manifest-marked artwork QA verified: **{figure_qa_verified} / {len(figure_rows)}**",
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
        "- **INFO** — status note, including artwork not yet generated or generated but not yet technically verified.",
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
        "6. Complete missing PNG/SVG artwork pairs, then perform figure engineering QA and update the manifest Status.",
        "7. Manually sample clean chapters for formula/model correctness because automated checks cannot prove engineering validity.",
        "",
        "## Important limitation",
        "",
        "A PASS from this script means the manuscript passed the implemented technical-content heuristics. It is **not** a certification that every equation, calculation, model assumption, source claim, or figure is technically correct. Final release still requires domain review of formulas, worked examples, practice solutions, and source support.",
        "",
    ]

    (outdir / "Technical-Audit-Summary.md").write_text("\n".join(summary), encoding="utf-8")

    print(f"Consolidated technical audit: {audit_status}")
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
        description="Perform a consolidated technical-content audit of FE Supplemental Guide Layers 1, 2, and 3."
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
        "--png-dir",
        type=Path,
        help="Optional PNG artwork directory. Default: <root>/figures/png",
    )
    ap.add_argument(
        "--svg-dir",
        type=Path,
        help="Optional SVG artwork directory. Default: <root>/figures/svg",
    )
    ap.add_argument(
        "--artwork-mode",
        choices=["both", "either", "png", "svg"],
        default="both",
        help="Required artwork format set. Default 'both' requires matching PNG and SVG files.",
    )
    ap.add_argument(
        "--out",
        type=Path,
        help="Optional output folder. Default: <root>/tools/validation/technical-audit",
    )
    ap.add_argument(
        "--layers",
        default="1,2,3",
        help="Comma-separated layers to audit, e.g. '1,2,3', '1,2', or '3'. Default: 1,2,3.",
    )
    ap.add_argument(
        "--chapter-root",
        action="append",
        type=Path,
        help="Optional manuscript root to scan. May be supplied multiple times. Default scans the repository recursively with exclusions.",
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

    try:
        selected_layers = {int(x.strip()) for x in str(args.layers).split(",") if x.strip()}
    except ValueError:
        print("ERROR: --layers must be a comma-separated list using 1, 2, and/or 3.", file=sys.stderr)
        return 2
    if not selected_layers or not selected_layers.issubset({1, 2, 3}):
        print("ERROR: --layers may contain only 1, 2, and/or 3.", file=sys.stderr)
        return 2

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
    png_dir = (
        args.png_dir.expanduser().resolve()
        if args.png_dir
        else canonical_path(root, "png_dir")
    )
    svg_dir = (
        args.svg_dir.expanduser().resolve()
        if args.svg_dir
        else canonical_path(root, "svg_dir")
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
    print(f"  png dir:  {png_dir}")
    print(f"  svg dir:  {svg_dir}")
    print(f"  artwork:  {args.artwork_mode}")
    print(f"  layers:   {','.join(str(x) for x in sorted(selected_layers))}")
    print(f"  output:   {outdir}")

    if args.show_paths:
        return 0

    if not looks_like_project_root(root):
        print(
            "ERROR: could not normalize to an FE-Study-Guide root containing "
            "meta/ledger.yaml and figures/figure-manifest.csv.",
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
            png_dir=png_dir,
            svg_dir=svg_dir,
            artwork_mode=args.artwork_mode,
            strict=args.strict,
            selected_layers=selected_layers,
            chapter_roots=args.chapter_root,
        )
    except PermissionError as e:
        print(f"ERROR: permission denied during technical audit: {e.filename or e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"ERROR: technical audit failed: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
