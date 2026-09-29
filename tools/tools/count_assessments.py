"""Inventory chapter assessments and optionally update generated ledger totals.

Default: read-only comparison. --write is an all-or-nothing operation for the
selected chapters, refuses ambiguous/incomplete assessment structures, and makes
a timestamped backup. Comments, key order, BOM, and line endings are preserved.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import os
from pathlib import Path
import re
import stat
import tempfile

import yaml

from ledger_io import (Chapter, InputError, Ledger, Report, add_common_arguments,
                       check_chapter_membership, discover_chapters, fail_input,
                       heading_key, open_inputs, read_ledger)

REVIEW_KEYS = ("Review Questions",)
PRACTICE_KEYS = ("Practice Problems",)
REVIEW_ANSWERS = ("Answer Key with Explanations", "Answers to Review Questions", "Review Answers", "Review Question Answers")
PRACTICE_ANSWERS = ("Practice Problem Solutions", "Solutions to Practice Problems", "Practice Answers", "Answers to Practice Problems")


def numbered_items(lines: list[str], first_line: int, answers=False) -> list[tuple[int, int]]:
    candidates = []
    for offset, line in enumerate(lines):
        bold = re.match(r"^( {0,3})(?:\*\*|__)(\d+)[.)](?:\*\*|__|\s)", line)
        plain = re.match(r"^( {0,3})(\d+)[.)]\s+", line)
        if bold:
            candidates.append((len(bold[1]), int(bold[2]), first_line + offset, True))
        elif plain:
            # For unbolded answer keys, a numeric sentence wrapped inside a
            # paragraph is not a new item. Indented list continuations may be
            # followed by the next item without an intervening blank line.
            previous = lines[offset - 1] if offset else ""
            previous_indent = len(previous) - len(previous.lstrip(' '))
            boundary = (not previous.strip() or previous.lstrip().startswith("#")
                        or bool(re.match(r"^ {0,3}\d+[.)]\s", previous))
                        or previous_indent > len(plain[1]))
            if not answers or boundary:
                candidates.append((len(plain[1]), int(plain[2]), first_line + offset, False))
    if not candidates:
        return []
    indent = min(c[0] for c in candidates)
    return [(n, line) for spaces, n, line, _ in candidates if spaces == indent]


def check_numbering(items, label, chapter, heading, report):
    numbers = [n for n, _ in items]
    if not numbers:
        report.add("ERROR", "EMPTY_ASSESSMENT_SECTION", f"{label} contains no recognized top-level numbered entries", chapter.path, heading.line, chapter.id)
        return
    repeated = [n for n, count in Counter(numbers).items() if count > 1]
    if repeated:
        report.add("ERROR", "DUPLICATE_ITEM_NUMBER", f"{label} repeats item numbers {repeated}", chapter.path, heading.line, chapter.id)
    if numbers != list(range(1, len(numbers) + 1)):
        report.add("ERROR", "NONSEQUENTIAL_NUMBERING", f"{label} must be numbered continuously from 1; found {numbers}", chapter.path, heading.line, chapter.id)


def assessment_inventory(chapter: Chapter, report: Report) -> dict:
    reviews = chapter.find(*REVIEW_KEYS)
    practices = chapter.find(*PRACTICE_KEYS)
    review_keys = chapter.find(*REVIEW_ANSWERS)
    practice_keys = chapter.find(*PRACTICE_ANSWERS)
    groups = {"review": reviews, "practice": practices, "review_answers": review_keys, "practice_answers": practice_keys}
    result = {key: [] for key in groups}
    if not reviews:
        report.add("ERROR", "MISSING_REVIEW_QUESTIONS", "No Review Questions section", chapter.path, chapter=chapter.id)
    for key, heads in groups.items():
        if len(heads) > 1:
            report.add("ERROR", "DUPLICATE_ASSESSMENT_SECTION", f"{len(heads)} {key} sections make the assessment ambiguous", chapter.path, heads[1].line, chapter.id)
        for h in heads:
            items = numbered_items(chapter.body(h), h.line + 1, answers=key.endswith("answers"))
            check_numbering(items, key, chapter, h, report)
            result[key].append(items)
    for kind in ("review", "practice"):
        question_groups = result[kind]
        answer_groups = result[kind + "_answers"]
        if question_groups and not answer_groups:
            count = sum(len(g) for g in question_groups)
            report.add("ERROR", "MISSING_ANSWER_KEY", f"{count} {kind} questions have no recognized answer-key section", chapter.path, groups[kind][0].line, chapter.id)
        elif answer_groups and not question_groups:
            report.add("ERROR", "ORPHAN_ANSWER_KEY", f"{kind} answer key has no corresponding questions", chapter.path, groups[kind + '_answers'][0].line, chapter.id)
        elif len(question_groups) == len(answer_groups) == 1:
            questions = {n for n, _ in question_groups[0]}
            answers = {n for n, _ in answer_groups[0]}
            if questions != answers:
                report.add("ERROR", "ANSWER_COVERAGE", f"{kind}: missing answers {sorted(questions - answers)}; answers without questions {sorted(answers - questions)}", chapter.path, groups[kind + '_answers'][0].line, chapter.id)
    totals = {key: sum(len(g) for g in value) for key, value in result.items()}
    return {"chapter": chapter.id, "file": str(chapter.path),
            "review_question_sets": [len(g) for g in result['review']],
            "practice_problem_sets": [len(g) for g in result['practice']],
            "review_questions": totals['review'], "practice_problems": totals['practice'],
            "review_answer_entries": totals['review_answers'], "practice_answer_entries": totals['practice_answers'],
            "counts_unambiguous": len(reviews) == 1 and len(practices) <= 1}


def planned_counts(ledger: Ledger, chapters: list[Chapter], report: Report) -> dict[str, dict[str, int]]:
    changes = {}
    inventories = []
    for chapter in chapters:
        inventory = assessment_inventory(chapter, report)
        inventories.append(inventory)
        records = ledger.chapter_records(chapter.id)
        if not records or not inventory['counts_unambiguous']:
            continue
        designated = [c for c in records if c.get("assessment_scope") == "chapter_total"]
        if len(designated) > 1:
            report.add("ERROR", "ASSESSMENT_ALLOCATION", "More than one record claims assessment_scope: chapter_total", ledger.path, chapter=chapter.id)
            continue
        owner = designated[0] if designated else records[0]
        if not designated and any(c['review_questions'] or c['practice_problems'] for c in records[1:]):
            report.add("ERROR", "ASSESSMENT_ALLOCATION", "Counts appear distributed across atoms but no chapter_total owner is declared; reconcile the allocation before updating", ledger.path, chapter=chapter.id)
            continue
        for c in records:
            values = {key: inventory[key] if c['id'] == owner['id'] else 0 for key in ('review_questions', 'practice_problems')}
            changed = {key: value for key, value in values.items() if c[key] != value}
            if changed:
                changes[c['id']] = changed
                report.add("ERROR", "COUNTS_STALE", f"{c['id']}: stored {[c['review_questions'], c['practice_problems']]} -> review/practice {[values['review_questions'], values['practice_problems']]}", ledger.path, chapter=chapter.id)
    report.statistics.update(chapters=len(chapters), inventories=inventories, records_requiring_update=len(changes))
    return changes


def updated_text(ledger: Ledger, changes: dict[str, dict[str, int]]) -> str:
    if any(getattr(event, 'anchor', None) is not None for event in yaml.parse(ledger.text)):
        raise InputError("--write does not modify YAML aliases/anchors. Expand aliases into explicit records first; read-only checks remain available.")
    tree = yaml.compose(ledger.text, Loader=yaml.SafeLoader)
    root_nodes = {key.value: value for key, value in tree.value}
    replacements = []
    seen = set()
    for concept_node in root_nodes['concepts'].value:
        nodes = {key.value: value for key, value in concept_node.value}
        cid = nodes['id'].value
        if cid not in changes:
            continue
        for key, value in changes[cid].items():
            if key not in ('review_questions', 'practice_problems'):
                raise InputError(f"Refusing to change non-generated field {key}")
            node = nodes[key]
            if not isinstance(node, yaml.ScalarNode) or node.tag != 'tag:yaml.org,2002:int':
                raise InputError(f"{cid}.{key}: cannot safely patch the integer scalar")
            replacements.append((node.start_mark.index, node.end_mark.index, str(value)))
            seen.add((cid, key))
    wanted = {(cid, key) for cid, values in changes.items() for key in values}
    if seen != wanted:
        raise InputError("Could not locate every generated count field; no file was changed")
    text = ledger.text
    for start, end, value in sorted(replacements, reverse=True):
        text = text[:start] + value + text[end:]
    # Compare parsed structures to ensure only the requested counts changed.
    after = yaml.safe_load(text)
    expected = yaml.safe_load(ledger.text)
    for c in expected['concepts']:
        c.update(changes.get(c['id'], {}))
    if after != expected:
        raise InputError("Generated update changed unexpected data; refusing to write")
    return text


def write_counts(ledger: Ledger, changes: dict[str, dict[str, int]]) -> Path | None:
    if not changes:
        return None
    text = updated_text(ledger, changes)
    payload = (b'\xef\xbb\xbf' if ledger.original_bytes.startswith(b'\xef\xbb\xbf') else b'') + text.encode('utf-8')
    path = ledger.path
    lock = path.with_name(path.name + '.counts.lock')
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise InputError(f"Update lock exists: {lock}; check whether another count update is running") from exc
    temporary = None
    try:
        with os.fdopen(fd, 'w') as handle:
            handle.write(str(os.getpid()))
        if path.read_bytes() != ledger.original_bytes:
            raise InputError("Ledger changed after it was read; rerun instead of overwriting newer content")
        backup = path.with_name(path.name + '.bak.' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ'))
        with backup.open('xb') as handle:
            handle.write(ledger.original_bytes)
        fd, name = tempfile.mkstemp(prefix=path.name + '.', suffix='.tmp', dir=path.parent)
        temporary = Path(name)
        with os.fdopen(fd, 'wb') as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, stat.S_IMODE(path.stat().st_mode))
        read_ledger(temporary)
        if path.read_bytes() != ledger.original_bytes:
            raise InputError("Ledger changed during the update; backup retained, original not overwritten")
        os.replace(temporary, path)
        return backup
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_arguments(parser)
    parser.add_argument('--write', action='store_true', help='Update generated count fields after all selected assessments pass structural checks; create a backup')
    args = parser.parse_args(argv)
    report = Report('count_assessments', 'assessment inventory and ledger count agreement; answer correctness is not evaluated')
    try:
        root, ledger = open_inputs(args)
        report.statistics['concepts_loaded'] = len(ledger.concepts)
        chapters = discover_chapters(root, args.chapters)
        check_chapter_membership(ledger, chapters, report, partial=bool(args.chapters))
        changes = planned_counts(ledger, chapters, report)
        blocking = [d for d in report.diagnostics if d.severity == 'ERROR' and d.code != 'COUNTS_STALE']
        if args.write and blocking:
            report.add('ERROR', 'WRITE_REFUSED', 'No counts written: fix blocking assessment/membership findings or explicitly select a valid chapter subset', ledger.path)
        elif args.write:
            backup = write_counts(ledger, changes)
            for d in report.diagnostics:
                if d.code == 'COUNTS_STALE':
                    d.severity, d.code = 'INFO', 'COUNTS_UPDATED'
            report.statistics['backup'] = str(backup) if backup else None
            report.statistics['written'] = bool(changes)
        else:
            report.statistics['written'] = False
        return report.emit(args)
    except (InputError, OSError) as exc:
        return fail_input(report, args, exc)


if __name__ == '__main__':
    raise SystemExit(main())
