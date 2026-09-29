"""Check the FE guide's mechanically enforceable chapter conventions.

Checks structure, headings, notation banners, example labels, Mentor's Margin
boxes, section citations, and descriptive image alt text. It does not certify
technical correctness, voice, accessibility of rendered artwork, or NCEES facts.
"""
from __future__ import annotations

import argparse
from collections import Counter
import re

from ledger_io import (InputError, Report, add_common_arguments,
                       check_chapter_membership, discover_chapters, fail_input,
                       figures, heading_key, normalize, open_inputs, resolve_path,
                       table_rows, text_bytes, visible_lines)


ALIASES = {
    "answer key with explanations": {"answers to review questions", "review answers", "review question answers"},
    "quick reference": {"summary card"},
    "what's next": {"looking ahead", "where we go from here", "going further"},
}
BASE_SECTIONS = ["Before You Start", "On the Board Today", "Learning Objectives", "Where This Goes Wrong", "Key Terms", "Review Questions", "Answer Key with Explanations", "Quick Reference", "What's Next"]


def section_map(chapter, report):
    mapping = {}
    for h in chapter.headings:
        if h.level != 2:
            continue
        key = heading_key(h.title)
        canonical = next((k for k, variants in ALIASES.items() if key in variants), key)
        if canonical != key:
            report.add('ERROR', 'NONSTANDARD_HEADING', f'{h.title!r} supplies content but should use the standard heading {canonical!r}', chapter.path, h.line, chapter.id)
        if canonical in mapping:
            report.add('ERROR', 'DUPLICATE_HEADING', f'Duplicate section {h.title!r}', chapter.path, h.line, chapter.id)
        else:
            mapping[canonical] = h
    return mapping


def structural_checks(chapter, report):
    mapping = section_map(chapter, report)
    orientation = chapter.meta.get('template') == 'orientation' or chapter.meta.get('layer') == 0
    required = BASE_SECTIONS + ([] if orientation else ['Notation Used Here', 'As the Handbook States It'])
    for name in required:
        if heading_key(name) not in mapping:
            report.add('ERROR', 'MISSING_SECTION', f'Missing required section {name!r}', chapter.path, chapter=chapter.id)
    for first, second in [('before you start','on the board today'), ('on the board today','learning objectives'),
                          ('key terms','review questions'), ('review questions','answer key with explanations'),
                          ('answer key with explanations','quick reference'), ('quick reference',"what's next")]:
        if first in mapping and second in mapping and mapping[first].line > mapping[second].line:
            report.add('ERROR', 'SECTION_ORDER', f'{first!r} must precede {second!r}', chapter.path, mapping[first].line, chapter.id)
    previous = 0
    for h in chapter.headings:
        if previous and h.level > previous + 1:
            report.add('ERROR', 'HEADING_LEVEL_SKIP', f'Heading jumps from level {previous} to {h.level}', chapter.path, h.line, chapter.id)
        previous = h.level
    numbered = [(h, re.match(r'^(\d+)\.(\d+)(?:\.(\d+))?\b', h.title)) for h in chapter.headings]
    numbered = [(h,m) for h,m in numbered if m]
    prefix = 0 if orientation else int(chapter.id[3:])
    numbers = [m[0] for _,m in numbered]
    for number,count in Counter(numbers).items():
        if count > 1:
            report.add('ERROR', 'DUPLICATE_SECTION_NUMBER', f'Section {number} occurs {count} times', chapter.path, chapter=chapter.id)
    for h,m in numbered:
        if int(m[1]) != prefix:
            report.add('ERROR', 'SECTION_PREFIX', f'Section prefix should be {prefix} for chapter {chapter.id}', chapter.path, h.line, chapter.id)
    if numbered and 'learning objectives' in mapping and mapping['learning objectives'].line > numbered[0][0].line:
        report.add('ERROR', 'OBJECTIVES_AFTER_TEACHING', 'Learning Objectives follows the first teaching section', chapter.path, mapping['learning objectives'].line, chapter.id)
    for key in ('title', 'routes', 'status'):
        if key not in chapter.meta:
            report.add('ERROR', 'FRONT_MATTER_FIELD', f'Missing front-matter {key}', chapter.path, 1, chapter.id)
    if not re.fullmatch(r'\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md', chapter.path.name):
        report.add('WARNING', 'FILENAME_STYLE', 'Filename differs from the chapter-number-kebab-case.md convention; upload suffixes such as (1) can cause this', chapter.path, chapter=chapter.id)
    review = mapping.get('review questions')
    if review:
        categories = {heading_key(h.title) for h in chapter.headings if h.level == 3 and review.line < h.line <= review.end}
        missing = {'conceptual', 'calculation', 'multiple choice'} - categories
        if missing:
            report.add('ERROR', 'REVIEW_PARTS_MISSING', f'Combined review format lacks subsections: {sorted(missing)}', chapter.path, review.line, chapter.id)
    return mapping, orientation


def example_checks(chapter, report):
    examples = [h for h in chapter.headings if re.match(r'^(?:Worked\s+)?Example\s+\d+\b', h.title, re.I)]
    for h in examples:
        body = '\n'.join(chapter.body(h))
        labels = set()
        for m in re.finditer(r'^\s*(?:\*\*|__|#{3,6}\s+)(Given|Find|Approach|Solution|Check|Verify|Units check|Dimensional check|Numerical check)\b', body, re.M | re.I):
            label = m[1].casefold()
            labels.add('check' if label == 'verify' or label.endswith(' check') else label)
        missing = {'given','find','approach','solution','check'} - labels
        if missing:
            report.add('ERROR', 'EXAMPLE_PARTS_MISSING', f'{h.title}: missing labeled parts {sorted(missing)}. Check numerically / Units check / Verify variants are recognized where labeled.', chapter.path, h.line, chapter.id)
    return len(examples)


def quote_checks(chapter, report):
    lines = chapter.visible
    i = 0
    while i < len(lines):
        if not re.match(r'^ {0,3}>', lines[i]):
            i += 1
            continue
        start = i
        block = []
        while i < len(lines) and re.match(r'^ {0,3}>', lines[i]):
            block.append(re.sub(r'^ {0,3}> ?', '', lines[i]))
            i += 1
        for offset, line in enumerate(block):
            if re.search(r"Mentor['’]s Margin", line, re.I):
                exact = bool(re.fullmatch(r"\*\*Mentor['’]s Margin\*\*", line.strip(), re.I))
                nonblank = [x.strip() for x in block if x.strip()]
                boxed = len(nonblank) >= 3 and nonblank[0] == '---' and nonblank[-1] == '---'
                spacing = offset + 1 < len(block) and not block[offset + 1].strip()
                if not (exact and boxed and spacing):
                    report.add('ERROR', 'MENTOR_MARGIN_FORMAT', 'Use a boxed blockquote with opening/closing > ---, a standalone **Mentor\'s Margin** label, and a blank quoted line before its body', chapter.path, start + offset + 1, chapter.id)
            if re.match(r'^\*\*Preview note', line, re.I) and not re.match(r'^\*\*Preview note\.\*\*\s', line, re.I):
                report.add('ERROR', 'PREVIEW_NOTE_FORMAT', 'Use > **Preview note.** followed by the preview text', chapter.path, start + offset + 1, chapter.id)


def citation_checks(chapter, chapter_index, report):
    local = {m[1] for h in chapter.headings if (m := re.match(r'^(\d+(?:\.\d+)+)\b', h.title))}
    for line_number,line in enumerate(chapter.visible,1):
        line = re.sub(r'`+[^`]*`+', '', line)
        for match in re.finditer(r'§(\d+(?:\.\d+)+)', line):
            prefix = line[:match.start()]
            qualifier = re.search(r'(?<!\d)(\d{2}-\d{2})(?:\s*[,:(]\s*|\s*)$', prefix)
            if qualifier:
                target_id = qualifier[1]
                target = chapter_index.get(target_id)
                if target is None:
                    report.add('WARNING', 'CITATION_TARGET_UNAVAILABLE', f'Cannot check {target_id} §{match[1]} because the target chapter is outside this input set', chapter.path, line_number, chapter.id)
                else:
                    target_sections = {m[1] for h in target.headings if (m := re.match(r'^(\d+(?:\.\d+)+)\b', h.title))}
                    if match[1] not in target_sections:
                        report.add('ERROR', 'CITATION_SECTION_MISSING', f'{target_id} has no section {match[1]}', chapter.path, line_number, chapter.id)
            elif match[1] not in local:
                report.add('ERROR', 'BARE_FOREIGN_SECTION', f'Bare §{match[1]} does not exist in this chapter; qualify a cross-chapter citation with its chapter ID', chapter.path, line_number, chapter.id)


TEX_GREEK = {'rho':'ρ','sigma':'σ','tau':'τ','mu':'μ','nu':'ν','alpha':'α','beta':'β','eta':'η','lambda':'λ','omega':'ω','theta':'θ','phi':'φ'}


def collision_symbols(notation_text):
    text = '\n'.join(visible_lines(notation_text))
    section = re.search(r'^## Rule 2\b(.*?)(?=^## |\Z)', text, re.M | re.S)
    if not section:
        return set()
    rows = table_rows(section[1].splitlines())
    return {cells[0].strip('`$* ') for _,cells in rows[1:] if cells}


def printed_symbols(cell):
    symbols = set()
    for expression in re.findall(r'\$([^$]+)\$', cell):
        for part in expression.split(','):
            part = part.strip()
            if re.fullmatch(r'[A-Za-zΑ-ω]', part):
                symbols.add(part)
            elif re.fullmatch(r'\\[a-z]+', part):
                symbols.add(TEX_GREEK.get(part[1:], part))
    return symbols


def notation_banner_checks(chapter, mapping, orientation, reserved, report):
    if orientation:
        return
    head = mapping.get('notation used here')
    if not head:
        return
    rows = table_rows(chapter.body(head), head.line + 1)
    if not rows:
        report.add('ERROR', 'NOTATION_BANNER_TABLE', 'Notation Used Here contains no table', chapter.path, head.line, chapter.id)
        return
    keys = [normalize(v) for v in rows[0][1]]
    if not {'symbol','si','uscs'}.issubset(keys) or not any(k in keys for k in ('meaning','meaning in this chapter')):
        report.add('ERROR', 'NOTATION_BANNER_COLUMNS', 'The notation contract requires Symbol / Meaning in this chapter / SI / USCS; Notes alone is not a units column', chapter.path, rows[0][0], chapter.id)
    seen = set()
    for line,cells in rows[1:]:
        if len(cells) != len(keys):
            report.add('ERROR', 'NOTATION_BANNER_WIDTH', 'Notation row width does not match the header', chapter.path, line, chapter.id)
            continue
        if 'symbol' in keys:
            seen.update(printed_symbols(cells[keys.index('symbol')]))
        for key in ('si','uscs'):
            if key in keys and not cells[keys.index(key)].strip():
                report.add('ERROR', 'NOTATION_BANNER_EMPTY_UNIT', f'Empty {key.upper()} cell; state units, dimensionless, or not applicable explicitly', chapter.path, line, chapter.id)
    collisions = seen & reserved
    banner = '\n'.join(chapter.body(head))
    if collisions and not re.search(r'collision\s+notes?', banner, re.I):
        report.add('ERROR', 'COLLISION_NOTE_MISSING', f'Reserved printed symbols {sorted(collisions)} occur in the banner without its required Collision note label', chapter.path, head.line, chapter.id)


def image_checks(chapter, report):
    for image in figures(chapter):
        alt = re.sub(r'FIG-\d{2}-\d{2}-\d{3}', '', image.alt).strip(' :—-')
        if not alt or re.fullmatch(r'(?:Figure|Fig\.?)\s*[\d.]+', alt, re.I):
            report.add('ERROR', 'ALT_TEXT_MISSING', 'Image alt text must describe the physical situation, not just give a figure label', chapter.path, image.line, chapter.id)
        elif len(re.findall(r'\w+', alt)) < 5:
            report.add('WARNING', 'ALT_TEXT_SHORT', 'Very short image description; review whether it conveys the physical situation', chapter.path, image.line, chapter.id)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_arguments(parser)
    parser.add_argument('--style-guide', default='meta/style-guide.md')
    parser.add_argument('--notation', default='meta/notation.md')
    args = parser.parse_args(argv)
    report = Report('lint_style', 'mechanical conventions from the supplied FE style guide and schema-4 ledger')
    try:
        root,ledger = open_inputs(args)
        report.statistics['concepts_loaded'] = len(ledger.concepts)
        style_path = resolve_path(root,args.style_guide)
        _,style = text_bytes(style_path)
        _,notation = text_bytes(resolve_path(root,args.notation))
        if not style.strip() or not notation.strip():
            raise InputError('Style guide and notation contract must be nonempty files')
        if 'Review questions vs practice problems' in style and 'Review Questions**, in three parts' in style:
            report.add('WARNING','STYLE_POLICY_CONFLICT','Style guide specifies both combined three-part review questions and separate conceptual/practice counts. This tool uses the current ledger’s combined-review convention and does not enforce either conflicting numerical quota.',style_path)
        if 'memorize: true' in style:
            report.add('WARNING','STYLE_SCHEMA_LEGACY','Style guide still describes memorize: true/false; schema 4 uses handbook_status and split_required. The current schema governs metadata checks.',style_path)
        chapters = discover_chapters(root,args.chapters)
        check_chapter_membership(ledger,chapters,report,partial=bool(args.chapters))
        index = {c.id:c for c in chapters}
        reserved = collision_symbols(notation)
        example_count = 0
        for chapter in chapters:
            mapping,orientation = structural_checks(chapter,report)
            example_count += example_checks(chapter,report)
            quote_checks(chapter,report)
            citation_checks(chapter,index,report)
            notation_banner_checks(chapter,mapping,orientation,reserved,report)
            image_checks(chapter,report)
        report.statistics.update(chapters=len(chapters),worked_examples_checked=example_count)
        return report.emit(args)
    except (InputError,OSError) as exc:
        return fail_input(report,args,exc)


if __name__ == '__main__':
    raise SystemExit(main())
