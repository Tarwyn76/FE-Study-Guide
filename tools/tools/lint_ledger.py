"""Validate ledger ownership, dependencies, and manuscript/notation agreement.

The default requires chapters and the notation contract. --ledger-only is an
explicitly narrower structural/ownership check. A figure manifest and physical
image assets are checked only when --manifest / --check-assets are requested.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import csv
import hashlib
import io
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from ledger_io import (FIGURE_RE, InputError, Report, add_common_arguments,
                       check_chapter_membership, discover_chapters, fail_input,
                       figures, normalize, open_inputs, resolve_path, table_rows,
                       text_bytes, visible_lines)


def ownership_checks(ledger, report):
    ancestors = ledger.ancestors()
    owners = {}
    for field in ('introduces_terms', 'introduces_symbols', 'introduces_notation', 'figures'):
        owner_map = {}
        for c in ledger.concepts:
            for value in c.get(field, []):
                key = normalize(value) if field == 'introduces_terms' else value
                if key in owner_map:
                    report.add('ERROR', 'DUPLICATE_OWNER', f'{field} {value!r} owned by {owner_map[key]} and {c["id"]}', ledger.path)
                else:
                    owner_map[key] = c['id']
        owners[field] = owner_map
    for token in owners['introduces_symbols'].keys() & owners['introduces_notation'].keys():
        report.add('ERROR', 'SYMBOL_NOTATION_COLLISION', f'{token} is registered as both a quantity and an operator/delimiter', ledger.path)
    for c in ledger.concepts:
        for used, introduced in (('uses_terms', 'introduces_terms'), ('uses_symbols', 'introduces_symbols'), ('uses_notation', 'introduces_notation')):
            for value in c.get(used, []):
                key = normalize(value) if used == 'uses_terms' else value
                owner = owners[introduced].get(key)
                if owner is None:
                    report.add('ERROR', 'UNDEFINED_USE', f'{c["id"]}: {used} {value!r} has no defining owner', ledger.path)
                elif owner not in ancestors[c['id']]:
                    report.add('ERROR', 'UNSATISFIED_DEPENDENCY', f'{c["id"]} uses {value!r}, but owner {owner} is not a transitive prerequisite', ledger.path)
        if c['status'] == 'verified' and c['split_required']:
            report.add('ERROR', 'VERIFIED_NEEDS_SPLIT', f'{c["id"]} is verified but still requires decomposition', ledger.path)
        if c['handbook_verified'] and (not c['handbook_ref'] or c['handbook_ref'].get('page') is None):
            report.add('ERROR', 'VERIFIED_WITHOUT_PAGE', f'{c["id"]} claims Handbook verification without a page reference', ledger.path)
        if c['handbook_verified'] and 'approxim' in str(c.get('handbook_ref', {})).casefold():
            report.add('ERROR', 'APPROXIMATE_PAGE_VERIFIED', f'{c["id"]} marks an approximate page as verified', ledger.path)
        if not c['prerequisites'] and c['layer'] != 0:
            report.add('WARNING', 'AXIOM_REVIEW', f'{c["id"]} has no prerequisites; confirm it is a true axiom', ledger.path)
    split = [c['id'] for c in ledger.concepts if c['split_required']]
    unmapped = [c['id'] for c in ledger.concepts if c['layer'] == 1 and not c['spec_lines']]
    unverified = [c['id'] for c in ledger.concepts if c['handbook_ref'] and not c['handbook_verified']]
    if split:
        report.add('WARNING', 'DECOMPOSITION_PENDING', f'{len(split)} concepts retain split_required: true; this blocks release, not dependency sorting', ledger.path)
    if unmapped:
        report.add('WARNING', 'SPEC_COVERAGE_PENDING', f'{len(unmapped)} Layer 1 concepts have no official specification mapping; no official specification inventory is validated by this tool', ledger.path)
    if unverified:
        report.add('WARNING', 'HANDBOOK_AUDIT_PENDING', f'{len(unverified)} page/location claims remain unverified against the PDF', ledger.path)
    catalog = ledger.raw.get('_symbol_catalog', {})
    if not isinstance(catalog, dict):
        raise InputError('_symbol_catalog must be a mapping when present')
    for token, entry in catalog.items():
        if token not in owners['introduces_symbols']:
            report.add('ERROR', 'CATALOG_OWNER', f'Symbol catalog contains unowned quantity {token!r}', ledger.path)
        if not isinstance(entry, dict) or any(not isinstance(entry.get(k), str) or not entry[k].strip() for k in ('display', 'meaning', 'SI', 'USCS')):
            report.add('ERROR', 'CATALOG_FIELDS', f'{token}: catalog entries need display, meaning, SI, and USCS strings', ledger.path)
    report.statistics.update(concepts=len(ledger.concepts), chapter_ids=len({c['chapter'] for c in ledger.concepts}),
                             dependency_edges=sum(len(c['prerequisites']) for c in ledger.concepts),
                             quantities=len(owners['introduces_symbols']), notation_tokens=len(owners['introduces_notation']),
                             unique_terms=len(owners['introduces_terms']), figure_ids=len(owners['figures']),
                             split_required=len(split), unmapped_layer_1=len(unmapped))
    return owners


def glossary_key(value):
    value = value.replace('$', '').replace('`', '').replace('*', '')
    return re.sub(r'[^\w]+', ' ', normalize(value)).strip()


def glossary_variants(value):
    variants = {glossary_key(value), glossary_key(re.sub(r'\$[^$]*\$', '', value))}
    # Explicit slash labels can cover multiple terms: "level curve / contour"
    # and "vertical stretch/compression". Match actual registered names only.
    plain = re.sub(r'\$[^$]*\$', '', value)
    if '/' in plain:
        parts = [x.strip() for x in plain.split('/')]
        variants.update(glossary_key(x) for x in parts)
        prefix = parts[0].rsplit(' ', 1)[0] if ' ' in parts[0] else ''
        if prefix:
            variants.update(glossary_key(prefix + ' ' + x) for x in parts[1:])
    return variants - {''}


def glossary_checks(ledger, chapters, report):
    lookup = defaultdict(set)
    for c in ledger.concepts:
        for term in c['introduces_terms']:
            lookup[glossary_key(term)].add((c['id'], term))
        for term, aliases in c.get('term_aliases', {}).items():
            for alias in aliases:
                lookup[glossary_key(alias)].add((c['id'], term))
    for chapter in chapters:
        heads = chapter.find('Key Terms')
        if len(heads) != 1:
            report.add('ERROR', 'KEY_TERMS_SECTION_COUNT', f'Expected one Key Terms section; found {len(heads)}', chapter.path, heads[0].line if heads else None, chapter.id)
        expected = {(c['id'], t) for c in ledger.chapter_records(chapter.id) for t in c['introduces_terms']}
        found = set()
        contextual = ledger.raw.get('_source_chapters', {}).get(chapter.id, {}).get('contextual_key_terms', {})
        if not isinstance(contextual, dict):
            raise InputError(f'_source_chapters[{chapter.id}].contextual_key_terms must be a mapping')
        for head in heads:
            rows = table_rows(chapter.body(head), head.line + 1)
            if not rows or [normalize(x) for x in rows[0][1]] != ['term', 'definition']:
                report.add('ERROR', 'KEY_TERMS_TABLE', 'Key Terms requires a Term / Definition table', chapter.path, head.line, chapter.id)
                continue
            for line, cells in rows[1:]:
                if len(cells) != 2 or not cells[0] or not cells[1]:
                    report.add('ERROR', 'KEY_TERMS_ROW', 'Expected a nonempty term and definition', chapter.path, line, chapter.id)
                    continue
                label = cells[0]
                context = next((v for k, v in contextual.items() if normalize(k) == normalize(label)), None)
                if context:
                    if not isinstance(context, dict) or context.get('owner') not in ledger.by_id or context.get('canonical_term') not in ledger.by_id[context['owner']]['introduces_terms']:
                        report.add('ERROR', 'CONTEXTUAL_TERM_INVALID', f'Invalid explicit ownership mapping for {label!r}', ledger.path, chapter=chapter.id)
                        continue
                    matches = {(context['owner'], context['canonical_term'])}
                else:
                    matches = set().union(*(lookup.get(key, set()) for key in glossary_variants(label)))
                if not matches:
                    report.add('ERROR', 'KEY_TERM_UNREGISTERED', f'{label!r} does not resolve to an introduced term or explicit alias; symbol-only rows are not glossary terms', chapter.path, line, chapter.id)
                    continue
                own = {(owner, term) for owner, term in matches if ledger.by_id[owner]['chapter'] == chapter.id}
                foreign = matches - own
                if not own:
                    report.add('ERROR', 'KEY_TERM_PREREQUISITE_REPEATED', f'{label!r} is owned by {sorted(owner for owner, _ in foreign)}; the current invariant requires this table to contain this chapter’s introductions', chapter.path, line, chapter.id)
                found.update(own)
        missing = sorted(term for _, term in expected - found)
        if missing:
            report.add('ERROR', 'INTRODUCED_TERM_NOT_LISTED', f'Introduced terms missing from the Key Terms table: {missing}', chapter.path, heads[0].line if heads else None, chapter.id)


def notation_checks(ledger, path, owners, report):
    _, text = text_bytes(path)
    rows = table_rows(visible_lines(text))
    registry, headers = {}, None
    for line, cells in rows:
        keys = [normalize(x) for x in cells]
        if 'symbol' in keys and 'si' in keys and 'uscs' in keys:
            headers = keys
            continue
        if any(k in keys for k in ('symbol', 'convention', 'subscript')):
            headers = None
            continue
        if headers and len(cells) == len(headers):
            row = dict(zip(headers, cells))
            token = row.get('ledger token', row.get('token', row['symbol'])).strip('`$* ')
            if token in registry:
                report.add('ERROR', 'DUPLICATE_NOTATION_ROW', f'{token!r} appears more than once in the units registry', path, line)
            registry[token] = row
    if not registry:
        report.add('ERROR', 'NOTATION_REGISTRY_MISSING', 'No actual Symbol / Meaning / SI / USCS registry found outside fenced examples. A sample banner is not a populated registry.', path)
        return
    catalog = ledger.raw.get('_symbol_catalog', {})
    missing = []
    for token in owners['introduces_symbols']:
        row = registry.get(token)
        if row is None:
            entry = catalog.get(token, {})
            display = entry.get('display') if isinstance(entry, dict) else None
            row = registry.get(display) if isinstance(display, str) else None
        if row is None:
            missing.append(token)
        elif not row.get('si') or not row.get('uscs') or not any(row.get(k) for k in ('meaning', 'meaning in this chapter', 'quantity')):
            report.add('ERROR', 'NOTATION_UNITS_MISSING', f'{token} lacks a meaning or one of the SI/USCS fields', path)
    if missing:
        report.add('ERROR', 'NOTATION_SYMBOLS_MISSING', f'No unambiguous units-registry entry for: {missing}. An optional Ledger token column can map canonical IDs to printed symbols.', path)


def figure_checks(ledger, chapters, owners, report, manifest=None, check_assets=False):
    inline = {}
    for chapter in chapters:
        for image in figures(chapter):
            if not image.id:
                report.add('ERROR', 'FIGURE_ID_MISSING', 'Image has no FIG-xx-xx-xxx ID in its alt text or target', chapter.path, image.line, chapter.id)
                continue
            if image.conflicting_ids:
                report.add('ERROR', 'FIGURE_ID_CONFLICT', f'Image carries conflicting IDs {image.conflicting_ids}', chapter.path, image.line, chapter.id)
            if image.id in inline:
                report.add('ERROR', 'FIGURE_INLINE_DUPLICATE', f'{image.id} is referenced more than once', chapter.path, image.line, chapter.id)
            inline[image.id] = (chapter, image)
            owner = owners['figures'].get(image.id)
            if owner is None:
                report.add('ERROR', 'FIGURE_UNOWNED', f'{image.id} has no concept owner', chapter.path, image.line, chapter.id)
            elif ledger.by_id[owner]['chapter'] != chapter.id:
                report.add('ERROR', 'FIGURE_WRONG_CHAPTER', f'{image.id} is owned by {owner}', chapter.path, image.line, chapter.id)
            if check_assets:
                parts = urlsplit(image.target)
                if parts.scheme or parts.netloc:
                    report.add('WARNING', 'REMOTE_ASSET_NOT_CHECKED', f'{image.id}: remote asset existence is outside this offline check', chapter.path, image.line, chapter.id)
                elif not (chapter.path.parent / unquote(parts.path)).is_file():
                    report.add('ERROR', 'IMAGE_FILE_MISSING', f'{image.id}: image file not found at {image.target}', chapter.path, image.line, chapter.id)
    selected = {c.id for c in chapters}
    for fid, owner in owners['figures'].items():
        if ledger.by_id[owner]['chapter'] in selected and fid not in inline:
            report.add('ERROR', 'FIGURE_NOT_INLINE', f'{fid}, owned by {owner}, has no inline image reference in its chapter', ledger.path)
    report.statistics['inline_figures'] = len(inline)
    report.statistics['image_assets_checked'] = check_assets
    if manifest:
        _, text = text_bytes(manifest)
        reader = csv.DictReader(io.StringIO(text))
        if not reader.fieldnames or any(key not in reader.fieldnames for key in ('Figure ID', 'Chapter', 'Section')):
            raise InputError(f'{manifest}: expected CSV columns Figure ID, Chapter, and Section')
        rows = {}
        for row in reader:
            number = reader.line_num
            if None in row or any(v is None for v in row.values()):
                report.add('ERROR', 'MANIFEST_WIDTH', 'CSV row width does not match its header', manifest, number)
                continue
            fid = row['Figure ID'].strip()
            if not FIGURE_RE.fullmatch(fid):
                report.add('ERROR', 'MANIFEST_ID', f'Invalid figure ID {fid!r}', manifest, number)
            if fid in rows:
                report.add('ERROR', 'MANIFEST_DUPLICATE', f'Duplicate {fid}', manifest, number)
            rows[fid] = row
            if row['Chapter'].strip() in selected and not row['Section'].strip():
                report.add('WARNING', 'MANIFEST_SECTION_MISSING', f'{fid} has no placement section', manifest, number)
        for fid, (chapter, image) in inline.items():
            if fid not in rows:
                report.add('ERROR', 'MANIFEST_FIGURE_MISSING', f'{fid} is inline but missing from the manifest', chapter.path, image.line, chapter.id)
            elif rows[fid]['Chapter'].strip() != chapter.id:
                report.add('ERROR', 'MANIFEST_CHAPTER', f'{fid} has the wrong manifest chapter', manifest, chapter=chapter.id)
        for fid, row in rows.items():
            if row['Chapter'].strip() in selected and fid not in inline:
                report.add('ERROR', 'MANIFEST_NOT_INLINE', f'{fid} is declared for a supplied chapter but not referenced inline', manifest)
        report.statistics['manifest_records'] = len(rows)
    else:
        report.add('INFO', 'MANIFEST_NOT_REQUESTED', 'Manifest comparison was not requested; use --manifest PATH')


def source_checks(ledger, chapters, report):
    for chapter in chapters:
        local = {m[1] for h in chapter.headings if (m := re.match(r'^(\d+(?:\.\d+)+)\b', h.title))}
        for c in ledger.chapter_records(chapter.id):
            for section in c.get('source_sections', []):
                if section not in local:
                    report.add('ERROR', 'SOURCE_SECTION_MISSING', f'{c["id"]} points to absent section {section}', chapter.path, chapter=chapter.id)
        snapshot = ledger.raw.get('_source_chapters', {}).get(chapter.id, {})
        expected_hash = snapshot.get('source_sha256') if isinstance(snapshot, dict) else None
        if expected_hash and hashlib.sha256(chapter.path.read_bytes()).hexdigest() != expected_hash:
            report.add('WARNING', 'SOURCE_CHANGED_SINCE_AUDIT', 'Chapter differs from the snapshot used to map its concepts; review ledger ownership against the edits', chapter.path, chapter=chapter.id)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_arguments(parser)
    parser.add_argument('--ledger-only', action='store_true', help='Explicitly omit all manuscript, manifest, and notation-file checks')
    parser.add_argument('--notation', default='meta/notation.md')
    parser.add_argument('--manifest', help='Optional figure manifest CSV; if requested, missing/malformed input is an error')
    parser.add_argument('--check-assets', action='store_true', help='Also require local image targets to exist')
    args = parser.parse_args(argv)
    report = Report('lint_ledger', 'ledger structure and ownership only' if args.ledger_only else 'ledger, supplied chapters, glossary, and notation contract')
    try:
        root, ledger = open_inputs(args)
        if args.ledger_only and (args.chapters or args.manifest or args.check_assets):
            raise InputError('--ledger-only cannot be combined with chapter/manifest/asset selections')
        owners = ownership_checks(ledger, report)
        if not args.ledger_only:
            chapters = discover_chapters(root, args.chapters)
            check_chapter_membership(ledger, chapters, report, partial=bool(args.chapters))
            source_checks(ledger, chapters, report)
            glossary_checks(ledger, chapters, report)
            notation_checks(ledger, resolve_path(root, args.notation), owners, report)
            figure_checks(ledger, chapters, owners, report,
                          resolve_path(root, args.manifest) if args.manifest else None, args.check_assets)
            report.statistics['chapters_checked'] = len(chapters)
        return report.emit(args)
    except (InputError, OSError, csv.Error) as exc:
        return fail_input(report, args, exc)


if __name__ == '__main__':
    raise SystemExit(main())
