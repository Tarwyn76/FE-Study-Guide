"""Shared strict ledger reader and Markdown utilities for the FE guide.

Python 3.10+; PyYAML 6.x. Import load_ledger(path) from older tools to obtain
the same list-of-records interface, with strict input and graph checks.
No file is changed by any function in this module.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass, field
import glob
import heapq
import json
from pathlib import Path
import re
import unicodedata
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required. Install with: python -m pip install 'PyYAML>=6,<7'") from exc


class InputError(ValueError):
    """Input is absent, malformed, contradictory, or structurally unsafe."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys instead of silently retaining the last."""

    def construct_mapping(self, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in mapping
            except TypeError as exc:
                raise InputError(f"Unhashable YAML key at line {key_node.start_mark.line + 1}") from exc
            if duplicate:
                raise InputError(f"Duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}")
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


DOMAINS = "MATH ORIENT PROF PHYS MECH THRM ELEC CTRL CHE CIV ECE ENV IND MEC OTH BRDG".split()
ID_RE = re.compile(r"(" + "|".join(DOMAINS) + r")-([0-3])([A-F]?)-(\d{3})-(\d{2})\Z")
CHAPTER_RE = re.compile(r"\d{2}-\d{2}\Z")
FIGURE_RE = re.compile(r"FIG-\d{2}-\d{2}-\d{3}\Z")
FIGURE_FIND = re.compile(r"FIG-\d{2}-\d{2}-\d{3}")
STATUSES = {"planned", "drafted", "revised", "reviewed", "verified"}
ROUTES = {"chemical", "civil", "electrical-computer", "environmental", "industrial-systems", "mechanical", "other-disciplines"}
CHAPTER_DIRS = ("layer-0-orientation", "layer-1-substrate", "layer-2-core", "layer-3-tracks")
LIST_FIELDS = ("prerequisites", "introduces_terms", "introduces_symbols", "introduces_notation", "uses_symbols", "uses_terms", "figures")
REQUIRED = ("id", "title", "chapter", "layer", "tier", "track", *LIST_FIELDS,
            "handbook_ref", "handbook_verified", "handbook_status", "split_required",
            "spec_lines", "primer_source", "review_questions", "practice_problems", "status")


def text_bytes(path: Path) -> tuple[bytes, str]:
    try:
        data = path.read_bytes()
        return data, data.decode("utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise InputError(f"Cannot read UTF-8 input {path}: {exc}") from exc


def parse_yaml(text: str, source: str = "YAML") -> Any:
    try:
        return yaml.load(text, Loader=UniqueKeyLoader)
    except (yaml.YAMLError, InputError, RecursionError) as exc:
        raise InputError(f"{source}: {exc}") from exc


def string_list(value: Any, label: str) -> None:
    if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
        raise InputError(f"{label} must be a list of nonempty strings (use [] when empty)")


@dataclass
class Ledger:
    path: Path
    raw: dict
    original_bytes: bytes
    text: str
    concepts: list[dict]
    by_id: dict[str, dict]
    order: list[str]

    def ancestors(self) -> dict[str, set[str]]:
        result: dict[str, set[str]] = {}
        for cid in self.order:
            parents = self.by_id[cid]["prerequisites"]
            result[cid] = set(parents)
            for parent in parents:
                result[cid].update(result[parent])
        return result

    def chapter_records(self, chapter: str) -> list[dict]:
        return sorted((c for c in self.concepts if c["chapter"] == chapter), key=lambda c: c["id"])


def topological_order(records: list[dict]) -> list[str]:
    index = {c["id"]: c for c in records}
    children: dict[str, list[str]] = {cid: [] for cid in index}
    degree = {}
    for cid, concept in index.items():
        parents = concept["prerequisites"]
        if len(parents) != len(set(parents)):
            raise InputError(f"{cid}: duplicate prerequisite IDs")
        for parent in parents:
            if parent not in index:
                raise InputError(f"{cid}: unknown prerequisite {parent}")
            children[parent].append(cid)
        degree[cid] = len(parents)
    def priority(cid):
        c = index[cid]
        return c["layer"], c["chapter"], cid
    ready = [priority(cid) for cid, d in degree.items() if d == 0]
    heapq.heapify(ready)
    result = []
    while ready:
        _, _, cid = heapq.heappop(ready)
        result.append(cid)
        for child in children[cid]:
            degree[child] -= 1
            if degree[child] == 0:
                heapq.heappush(ready, priority(child))
    if len(result) != len(records):
        # Following one unresolved prerequisite repeatedly must reach a real
        # cycle. Do not label every blocked descendant as a cycle member.
        blocked = set(index) - set(result)
        current = min(blocked)
        walk, seen = [], {}
        while current not in seen:
            seen[current] = len(walk)
            walk.append(current)
            current = next(p for p in index[current]["prerequisites"] if p in blocked)
        cycle = walk[seen[current]:] + [current]
        raise InputError("Dependency cycle: " + " -> ".join(cycle))
    return result


def read_ledger(path: str | Path) -> Ledger:
    path = Path(path).resolve()
    original_bytes, text = text_bytes(path)
    raw = parse_yaml(text, str(path))
    if not isinstance(raw, dict):
        raise InputError(f"{path}: ledger root must be a mapping with a concepts list")
    if type(raw.get("schema_version")) is not int or raw["schema_version"] != 4:
        raise InputError(f"{path}: expected schema_version: 4; migrate or update the reader explicitly")
    if not isinstance(raw.get("handbook_edition"), str) or not raw["handbook_edition"].strip():
        raise InputError(f"{path}: handbook_edition must be a quoted, nonempty string")
    records = raw.get("concepts")
    if not isinstance(records, list) or not records:
        raise InputError(f"{path}: concepts must be a NONEMPTY list; zero concepts is not a successful build")
    index = {}
    for position, c in enumerate(records, 1):
        if not isinstance(c, dict):
            raise InputError(f"concepts[{position}]: expected a mapping")
        missing = [k for k in REQUIRED if k not in c]
        if missing:
            raise InputError(f"concepts[{position}] {c.get('id', '')}: missing fields: {', '.join(missing)}")
        cid = c["id"]
        match = ID_RE.fullmatch(cid) if isinstance(cid, str) else None
        if not match:
            raise InputError(f"concepts[{position}]: illegal concept ID {cid!r}")
        if cid in index:
            raise InputError(f"Duplicate concept ID: {cid}")
        index[cid] = c
        _, layer, tier, number, _ = match.groups()
        if type(c["layer"]) is not int or c["layer"] != int(layer):
            raise InputError(f"{cid}: layer does not match ID")
        expected_tier = tier if c["layer"] in (1, 2) else None
        if (c["layer"] in (1, 2) and not tier) or (c["layer"] in (0, 3) and tier) or c["tier"] != expected_tier:
            raise InputError(f"{cid}: tier does not match layer/ID")
        if not isinstance(c["chapter"], str) or not CHAPTER_RE.fullmatch(c["chapter"]) or c["chapter"] != f"{int(layer):02d}-{int(number):02d}":
            raise InputError(f"{cid}: chapter does not match ID/layer")
        if c["layer"] == 3:
            if not isinstance(c["track"], str) or c["track"] not in ROUTES:
                raise InputError(f"{cid}: layer 3 requires a recognized track")
        elif c["track"] is not None:
            raise InputError(f"{cid}: track must be null outside layer 3")
        for key in ("title", "notes"):
            if key == "notes" and key not in c:
                continue
            if not isinstance(c[key], str) or (key == "title" and not c[key].strip()):
                raise InputError(f"{cid}.{key}: expected a string")
        for key in LIST_FIELDS:
            string_list(c[key], f"{cid}.{key}")
        for key in ("uses_notation", "source_sections"):
            if key in c:
                string_list(c[key], f"{cid}.{key}")
        for key in ("review_questions", "practice_problems"):
            if type(c[key]) is not int or c[key] < 0:
                raise InputError(f"{cid}.{key}: expected a nonnegative integer, not a Boolean/string")
        for key in ("handbook_verified", "split_required"):
            if type(c[key]) is not bool:
                raise InputError(f"{cid}.{key}: expected true or false")
        if not isinstance(c["status"], str) or c["status"] not in STATUSES:
            raise InputError(f"{cid}: unrecognized status {c['status']!r}")
        if not isinstance(c["handbook_status"], str) or c["handbook_status"] not in {"in_handbook", "in_handbook_memorize_anyway", "not_in_handbook"}:
            raise InputError(f"{cid}: unrecognized handbook_status")
        ref = c["handbook_ref"]
        if ref is not None and (not isinstance(ref, dict) or not isinstance(ref.get("section"), str) or not ref["section"].strip() or "page" not in ref or (ref["page"] is not None and type(ref["page"]) not in (str, int))):
            raise InputError(f"{cid}: handbook_ref must be null or a section/page mapping")
        if c["primer_source"] is not None and (not isinstance(c["primer_source"], str) or not CHAPTER_RE.fullmatch(c["primer_source"])):
            raise InputError(f"{cid}: primer_source must be null or a chapter ID")
        if not isinstance(c["spec_lines"], list):
            raise InputError(f"{cid}: spec_lines must be a list")
        for item in c["spec_lines"]:
            if not isinstance(item, dict) or any(k not in item for k in ("discipline", "area", "item")):
                raise InputError(f"{cid}: malformed spec_lines entry")
            if any(type(item[k]) not in (str, int) or not str(item[k]).strip() for k in ("discipline", "area", "item")):
                raise InputError(f"{cid}: spec_lines values must be nonempty strings or integers")
        for fig in c["figures"]:
            if not FIGURE_RE.fullmatch(fig) or fig[4:9] != c["chapter"]:
                raise InputError(f"{cid}: malformed figure ID or wrong figure chapter: {fig}")
        aliases = c.get("term_aliases", {})
        if not isinstance(aliases, dict):
            raise InputError(f"{cid}: term_aliases must be a mapping")
        for term, values in aliases.items():
            if term not in c["introduces_terms"]:
                raise InputError(f"{cid}: alias target {term!r} is not introduced by this record")
            string_list(values, f"{cid}.term_aliases[{term!r}]")
        if "assessment_scope" in c and c["assessment_scope"] != "chapter_total":
            raise InputError(f"{cid}: unsupported assessment_scope (expected chapter_total)")
    sources = raw.get("_source_chapters", {})
    if not isinstance(sources, dict):
        raise InputError("_source_chapters must be a mapping when present")
    for chapter, entry in sources.items():
        if not isinstance(chapter, str) or not CHAPTER_RE.fullmatch(chapter) or not isinstance(entry, dict):
            raise InputError("_source_chapters entries must map chapter IDs to mappings")
        for key in ("completion_state", "source_sha256"):
            if key in entry and not isinstance(entry[key], str):
                raise InputError(f"_source_chapters[{chapter}].{key} must be a string")
        contexts = entry.get("contextual_key_terms", {})
        if not isinstance(contexts, dict) or any(not isinstance(k, str) or not isinstance(v, dict) or
                any(not isinstance(v.get(field), str) for field in ("owner", "canonical_term"))
                for k, v in contexts.items()):
            raise InputError(f"_source_chapters[{chapter}].contextual_key_terms needs term -> owner/canonical_term mappings")
    return Ledger(path, raw, original_bytes, text, records, index, topological_order(records))


def load_ledger(path: str | Path) -> list[dict]:
    """Compatibility interface for tools that previously returned list[dict]."""
    return read_ledger(path).concepts


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", value.strip()).casefold()


def heading_key(value: str) -> str:
    value = re.sub(r"^\d+(?:\.\d+)+\s+", "", value)
    return normalize(value.strip(" #"))


def visible_lines(text: str, front_end: int = 0) -> list[str]:
    """Mask front matter, fenced code, and HTML comments, preserving line numbers."""
    result, fence, comment = [], None, False
    for number, line in enumerate(text.splitlines(), 1):
        if number <= front_end:
            result.append("")
            continue
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            result.append("")
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]))
            result.append("")
            continue
        cleaned, tail = "", line
        while tail:
            if comment:
                end = tail.find("-->")
                if end < 0:
                    tail = ""
                else:
                    tail, comment = tail[end + 3:], False
            else:
                start = tail.find("<!--")
                if start < 0:
                    cleaned += tail
                    tail = ""
                else:
                    cleaned += tail[:start]
                    tail, comment = tail[start + 4:], True
        result.append(cleaned)
    return result


@dataclass
class Heading:
    level: int
    title: str
    line: int
    end: int


@dataclass
class Chapter:
    path: Path
    text: str
    meta: dict
    visible: list[str]
    headings: list[Heading]

    @property
    def id(self):
        return self.meta["chapter"]

    def body(self, heading: Heading) -> list[str]:
        return self.visible[heading.line:heading.end]

    def find(self, *keys: str) -> list[Heading]:
        wanted = {heading_key(k) for k in keys}
        return [h for h in self.headings if h.level == 2 and heading_key(h.title) in wanted]


def read_chapter(path: Path) -> Chapter:
    _, text = text_bytes(path)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise InputError(f"{path}: missing YAML front matter")
    end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
    if end is None:
        raise InputError(f"{path}: unterminated YAML front matter")
    meta = parse_yaml("\n".join(lines[1:end]), f"{path} front matter")
    if not isinstance(meta, dict) or not isinstance(meta.get("chapter"), str) or not CHAPTER_RE.fullmatch(meta["chapter"]):
        raise InputError(f"{path}: invalid/missing quoted chapter ID")
    string_list(meta.get("ledger_ids"), f"{path}: ledger_ids")
    if not meta["ledger_ids"] or len(meta["ledger_ids"]) != len(set(meta["ledger_ids"])):
        raise InputError(f"{path}: ledger_ids must be nonempty and unique")
    if 'layer' in meta and (type(meta['layer']) is not int or meta['layer'] not in range(4)):
        raise InputError(f"{path}: layer must be an integer from 0 through 3")
    if 'tier' in meta and meta['tier'] is not None and (not isinstance(meta['tier'], str) or meta['tier'] not in 'ABCDEF' or len(meta['tier']) != 1):
        raise InputError(f"{path}: tier must be null or A through F")
    if 'status' in meta and (not isinstance(meta['status'], str) or meta['status'] not in STATUSES):
        raise InputError(f"{path}: unrecognized chapter status")
    if 'title' in meta and (not isinstance(meta['title'], str) or not meta['title'].strip()):
        raise InputError(f"{path}: title must be a nonempty string")
    if 'routes' in meta:
        string_list(meta['routes'], f"{path}: routes")
        if any(route not in ROUTES for route in meta['routes']):
            raise InputError(f"{path}: routes contains an unrecognized discipline")
    vis = visible_lines(text, end + 1)
    heads = []
    for number, line in enumerate(vis, 1):
        m = re.match(r"^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+\s*)?$", line)
        if m:
            heads.append(Heading(len(m[1]), m[2].strip(), number, len(vis)))
    for i, h in enumerate(heads):
        following = next((n for n in heads[i + 1:] if n.level <= h.level), None)
        if following:
            h.end = following.line - 1
    return Chapter(path, text, meta, vis, heads)


def resolve_path(root: Path, value: str | Path) -> Path:
    path = Path(value).expanduser()
    return (path if path.is_absolute() else root / path).resolve()


def discover_chapters(root: Path, selections: list[str] | None) -> list[Chapter]:
    paths = set()
    if selections:
        for selection in selections:
            pattern = str(resolve_path(root, selection))
            matches = [Path(p) for p in glob.glob(pattern, recursive=True)]
            if not matches:
                raise InputError(f"Chapter selection matched no input: {selection}")
            for p in matches:
                paths.update(p.rglob("*.md") if p.is_dir() else [p])
    else:
        for name in CHAPTER_DIRS:
            base = root / name
            if base.is_dir():
                paths.update(base.rglob("*.md"))
    paths = {p.resolve() for p in paths if p.is_file() and p.suffix.lower() == ".md" and re.match(r"^\d{2}-\d{2}-", p.name)}
    if not paths:
        raise InputError("No chapter Markdown files found. Use the standard layer directories or --chapters with an explicit path/glob.")
    chapters = [read_chapter(p) for p in sorted(paths)]
    by_id = {}
    for chapter in chapters:
        if chapter.id in by_id:
            raise InputError(f"Duplicate chapter {chapter.id}: {by_id[chapter.id]} and {chapter.path}. Select one version explicitly.")
        by_id[chapter.id] = chapter.path
    return sorted(chapters, key=lambda c: c.id)


def table_rows(lines: list[str], first_line: int = 1) -> list[tuple[int, list[str]]]:
    result = []
    for n, line in enumerate(lines, first_line):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if cells and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            continue
        result.append((n, cells))
    return result


@dataclass
class Figure:
    id: str | None
    alt: str
    target: str
    line: int
    conflicting_ids: list[str] = field(default_factory=list)


def figures(chapter: Chapter) -> list[Figure]:
    text = "\n".join(chapter.visible)
    result = []
    for m in re.finditer(r"!\[(.*?)\]\(([^\n]+?)\)", text, re.S):
        ids = list(dict.fromkeys(FIGURE_FIND.findall(m[0])))
        target = m[2].strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = re.split(r'\s+[\"\']', target, 1)[0]
        result.append(Figure(ids[0] if ids else None, m[1], target, text.count("\n", 0, m.start()) + 1, ids if len(ids) > 1 else []))
    return result


@dataclass
class Diagnostic:
    severity: str
    code: str
    message: str
    path: str = ""
    line: int | None = None
    chapter: str | None = None


@dataclass
class Report:
    tool: str
    scope: str
    diagnostics: list[Diagnostic] = field(default_factory=list)
    statistics: dict = field(default_factory=dict)

    def add(self, severity, code, message, path="", line=None, chapter=None):
        self.diagnostics.append(Diagnostic(severity, code, message, str(path), line, chapter))

    def emit(self, args, input_error=False):
        counts = Counter(d.severity for d in self.diagnostics)
        exit_code = 2 if input_error else 1 if counts["ERROR"] or (args.strict and counts["WARNING"]) else 0
        status = "INPUT_ERROR" if input_error else "FAIL" if exit_code else "PASS_WITH_WARNINGS" if counts["WARNING"] else "PASS"
        if args.format == "json":
            print(json.dumps({"tool": self.tool, "scope": self.scope, "status": status, "exit_code": exit_code,
                              "counts": dict(counts), "statistics": self.statistics,
                              "diagnostics": [asdict(d) for d in self.diagnostics]}, indent=2, ensure_ascii=False))
        else:
            print(f"{self.tool}: {self.scope}")
            selected = self.diagnostics if args.max_findings == 0 else self.diagnostics[:args.max_findings]
            for d in selected:
                location = d.path + (f":{d.line}" if d.line else "")
                print(f"{d.severity} [{d.code}] {location}: {d.message}")
            omitted = len(self.diagnostics) - len(selected)
            if omitted:
                print(f"... {omitted} more findings; use --max-findings 0 or --format json.")
            print(f"{status}: {counts['ERROR']} errors, {counts['WARNING']} warnings; {json.dumps(self.statistics, ensure_ascii=False)}")
        return exit_code


def add_common_arguments(parser: argparse.ArgumentParser):
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Project root (default: parent of tools/)")
    parser.add_argument("--ledger", default="meta/ledger.yaml", help="Ledger path, relative to --root unless absolute")
    parser.add_argument("--chapters", action="append", metavar="PATH_OR_GLOB", help="Repeatable explicit chapter selection; quotes preserve globs/spaces")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--strict", action="store_true", help="Return exit 1 for warnings as well as errors")
    parser.add_argument("--max-findings", type=int, default=100, help="Text output limit; 0 prints all (JSON is always complete)")


def open_inputs(args):
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        raise InputError(f"Project root does not exist: {root}")
    if args.max_findings < 0:
        raise InputError("--max-findings must be nonnegative")
    return root, read_ledger(resolve_path(root, args.ledger))


def check_chapter_membership(ledger: Ledger, chapters: list[Chapter], report: Report, partial=False):
    available = {c.id for c in chapters}
    for chapter in chapters:
        expected = {c["id"] for c in ledger.chapter_records(chapter.id)}
        declared = set(chapter.meta["ledger_ids"])
        if not expected:
            report.add("ERROR", "UNREGISTERED_CHAPTER", "Chapter has no concept records in the ledger", chapter.path, 1, chapter.id)
        if expected != declared:
            report.add("ERROR", "FRONT_MATTER_IDS", f"Missing from ledger/chapter: {sorted(declared - expected)}; undeclared records: {sorted(expected - declared)}", chapter.path, 1, chapter.id)
        for key in ("layer", "tier", "status"):
            if key not in chapter.meta:
                report.add("ERROR", "FRONT_MATTER_FIELD", f"Missing {key}", chapter.path, 1, chapter.id)
        for cid in declared & expected:
            c = ledger.by_id[cid]
            for key in ("layer", "tier"):
                if chapter.meta.get(key) != c[key]:
                    report.add("ERROR", "FRONT_MATTER_METADATA", f"{key} differs from {cid}", chapter.path, 1, chapter.id)
        audit = ledger.raw.get("_source_chapters", {}).get(chapter.id, {})
        if isinstance(audit, dict) and audit.get("completion_state") in {"work_in_progress", "incomplete"}:
            report.add("INFO", "CHAPTER_INCOMPLETE", f"Recorded state: {audit['completion_state']}; findings are still reported, not suppressed", chapter.path, 1, chapter.id)
    missing = {c["chapter"] for c in ledger.concepts if c["status"] != "planned"} - available
    if missing and not partial:
        report.add("ERROR", "MISSING_CHAPTER_FILES", f"Non-planned ledger chapters have no source files: {sorted(missing)}", ledger.path)
    if partial:
        report.add("INFO", "PARTIAL_SCOPE", "Chapter checks apply only to the explicitly selected files", ledger.path)


def fail_input(report: Report, args, exc: Exception):
    report.add("ERROR", "INPUT", str(exc))
    return report.emit(args, input_error=True)
