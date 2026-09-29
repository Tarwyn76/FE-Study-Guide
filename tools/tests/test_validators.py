"""Regression tests use temporary projects; no manuscript inputs are required."""
from __future__ import annotations

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.insert(0, str(TOOLS))
from ledger_io import (InputError, Report, check_chapter_membership,
                       discover_chapters, figures, load_ledger, read_chapter,
                       read_ledger)
import count_assessments as count
import lint_ledger as ledger_lint
import lint_style as style


def concept(seq=1, **changes):
    c = dict(id=f'MATH-1A-001-{seq:02d}', title=f'Concept {seq}', chapter='01-01',
             layer=1, tier='A', track=None, prerequisites=[], introduces_terms=[],
             introduces_symbols=[], introduces_notation=[], uses_symbols=[],
             uses_terms=[], uses_notation=[], figures=[], handbook_ref=None,
             handbook_verified=False, handbook_status='not_in_handbook',
             split_required=False, spec_lines=[], primer_source=None,
             review_questions=0, practice_problems=0, status='drafted', notes='')
    c.update(changes)
    return c


ASSESSMENTS = '''
## Review Questions

### Conceptual

1. Explain the principle.
   1. An indented subpart is not another question.
2. Describe its limit.

### Calculation

3. Compute the result.

### Multiple Choice

4. Choose the correct result.

## Answer Key with Explanations

**1.** Explanation.

**2.** Explanation.

**3.** The largest result is
4. Choice D is a distractor, continuing the previous sentence.

**4. C.** Explanation.
'''


class ProjectTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'meta').mkdir()
        self.ledger_path = self.root / 'meta' / 'ledger.yaml'

    def ledger(self, records=None, **extra):
        raw = dict(schema_version=4, handbook_edition='10.6',
                   concepts=records if records is not None else [concept()])
        raw.update(extra)
        self.ledger_path.write_text(yaml.safe_dump(raw, sort_keys=False), encoding='utf-8')
        return read_ledger(self.ledger_path)

    def chapter(self, body=ASSESSMENTS, ids=None, chapter='01-01', **extra):
        meta = dict(chapter=chapter, title='Fixture', layer=int(chapter[:2]),
                    tier=None if chapter.startswith('00') else 'A',
                    ledger_ids=ids or [concept()['id']], routes=['mechanical'], status='drafted')
        meta.update(extra)
        folder = self.root / ('layer-0-orientation' if chapter.startswith('00') else 'layer-1-substrate')
        folder.mkdir(exist_ok=True)
        path = folder / f'{chapter}-fixture.md'
        path.write_text('---\n' + yaml.safe_dump(meta, sort_keys=False) + '---\n# Fixture\n' + body, encoding='utf-8')
        return read_chapter(path)

    def run_count(self, *options):
        out = io.StringIO()
        with redirect_stdout(out):
            code = count.main(['--root', str(self.root), '--format', 'json', *options])
        return code, json.loads(out.getvalue())


class LoaderTests(ProjectTest):
    def test_loads_concepts_mapping_and_optional_notes(self):
        record = concept()
        del record['notes']
        self.ledger([record])
        self.assertEqual(load_ledger(self.ledger_path), [record])

    def test_rejects_zero_concepts(self):
        with self.assertRaisesRegex(InputError, 'NONEMPTY'):
            self.ledger([])

    def test_rejects_duplicate_yaml_keys(self):
        self.ledger()
        self.ledger_path.write_text(self.ledger_path.read_text() + '\nschema_version: 4\n')
        with self.assertRaisesRegex(InputError, 'Duplicate YAML key'):
            read_ledger(self.ledger_path)

    def test_rejects_duplicate_concept_ids(self):
        with self.assertRaisesRegex(InputError, 'Duplicate concept ID'):
            self.ledger([concept(), concept()])

    def test_rejects_unknown_prerequisite(self):
        with self.assertRaisesRegex(InputError, 'unknown prerequisite'):
            self.ledger([concept(prerequisites=['MATH-1A-001-99'])])

    def test_rejects_cycle_with_descendants(self):
        a, b, c = concept(), concept(2), concept(3)
        a['prerequisites'] = [b['id']]
        b['prerequisites'] = [a['id']]
        c['prerequisites'] = [b['id']]
        with self.assertRaisesRegex(InputError, 'Dependency cycle') as caught:
            self.ledger([c, b, a])
        self.assertNotIn(c['id'], str(caught.exception))

    def test_transitive_order(self):
        a, b, c = concept(), concept(2), concept(3)
        b['prerequisites'] = [a['id']]
        c['prerequisites'] = [b['id']]
        ledger = self.ledger([c, b, a])
        self.assertEqual(ledger.order, [a['id'], b['id'], c['id']])
        self.assertEqual(ledger.ancestors()[c['id']], {a['id'], b['id']})

    def test_bad_types_fail_cleanly(self):
        for key, value in [('review_questions', True), ('status', []), ('handbook_status', {}),
                           ('layer', True), ('figures', 'FIG-01-01-001'), ('tier', 'B')]:
            with self.subTest(key=key), self.assertRaises(InputError):
                self.ledger([concept(**{key: value})])
        with self.assertRaises(InputError):
            self.ledger(_source_chapters=[])

    def test_rejects_unsafe_yaml(self):
        self.ledger_path.write_text('!!python/object/apply:os.system ["echo unsafe"]')
        with self.assertRaises(InputError):
            read_ledger(self.ledger_path)

    def test_duplicate_chapter_versions_are_not_silently_selected(self):
        c = self.chapter()
        c.path.with_name('01-01-fixture(1).md').write_text(c.text)
        with self.assertRaisesRegex(InputError, 'Duplicate chapter'):
            discover_chapters(self.root, None)

    def test_missing_drafted_sources_fail_but_planned_seeds_are_allowed(self):
        ledger = self.ledger([concept(), concept(2, status='planned', chapter='01-02', id='MATH-1A-002-01')])
        report = Report('test', '')
        check_chapter_membership(ledger, [self.chapter()], report)
        self.assertFalse(any(d.severity == 'ERROR' for d in report.diagnostics))
        report = Report('test', '')
        check_chapter_membership(ledger, [], report)
        self.assertIn('MISSING_CHAPTER_FILES', [d.code for d in report.diagnostics])


class AssessmentTests(ProjectTest):
    def test_numbering_nested_subparts_and_wrapped_answer(self):
        report = Report('test', '')
        inventory = count.assessment_inventory(self.chapter(), report)
        self.assertEqual(inventory['review_questions'], 4)
        self.assertEqual(inventory['review_answer_entries'], 4)
        self.assertFalse(report.diagnostics)

    def test_contiguous_multiline_plain_and_bold_answer_items(self):
        lines = ['1. First answer', '   continued explanation.', '2. Second answer',
                 '   continued explanation.', '3. Third answer', '', '**4.** Fourth answer']
        self.assertEqual([n for n, _ in count.numbered_items(lines, 1, answers=True)], [1, 2, 3, 4])

    def test_fenced_examples_and_comments_do_not_count(self):
        body = ASSESSMENTS.replace('### Conceptual', '```md\n## Review Questions\n99. Example\n```\n<!--\n100. Comment\n-->\n### Conceptual')
        report = Report('test', '')
        inventory = count.assessment_inventory(self.chapter(body), report)
        self.assertEqual(inventory['review_question_sets'], [4])
        self.assertFalse(report.diagnostics)

    def test_separate_practice_inventory(self):
        body = ASSESSMENTS + '\n## Practice Problems\n\n1. Solve.\n\n## Practice Problem Solutions\n\n1. Solution.\n'
        report = Report('test', '')
        inventory = count.assessment_inventory(self.chapter(body), report)
        self.assertEqual((inventory['review_questions'], inventory['practice_problems'], inventory['practice_answer_entries']), (4, 1, 1))
        self.assertFalse(report.diagnostics)

    def test_default_is_read_only(self):
        self.ledger()
        self.chapter()
        before = self.ledger_path.read_bytes()
        code, report = self.run_count()
        self.assertEqual(code, 1)
        self.assertIn('COUNTS_STALE', [d['code'] for d in report['diagnostics']])
        self.assertEqual(self.ledger_path.read_bytes(), before)
        self.assertFalse(list(self.ledger_path.parent.glob('*.bak.*')))

    def test_write_preserves_comments_bom_crlf_and_other_records(self):
        a, b = concept(assessment_scope='chapter_total'), concept(2)
        self.ledger([a, b], author_metadata={'preserve': ['verbatim', 17]})
        self.chapter(ids=[a['id'], b['id']])
        source = self.ledger_path.read_text().replace('review_questions: 0', 'review_questions: 0 # keep this comment', 1)
        before = b'\xef\xbb\xbf' + source.replace('\n', '\r\n').encode()
        self.ledger_path.write_bytes(before)
        code, report = self.run_count('--write')
        self.assertEqual(code, 0, report)
        self.assertEqual(self.ledger_path.read_bytes(), before.replace(b'review_questions: 0 #', b'review_questions: 4 #', 1))
        backup = Path(report['statistics']['backup'])
        self.assertEqual(backup.read_bytes(), before)
        self.assertFalse(self.ledger_path.with_name('ledger.yaml.counts.lock').exists())
        code, report = self.run_count('--write')
        self.assertEqual(code, 0)
        self.assertFalse(report['statistics']['written'])
        self.assertIsNone(report['statistics']['backup'])

    def test_missing_key_blocks_write(self):
        self.ledger()
        self.chapter(ASSESSMENTS.split('## Answer Key')[0])
        before = self.ledger_path.read_bytes()
        code, report = self.run_count('--write')
        self.assertEqual(code, 1)
        self.assertIn('WRITE_REFUSED', [d['code'] for d in report['diagnostics']])
        self.assertEqual(self.ledger_path.read_bytes(), before)

    def test_duplicate_question_sets_block_write(self):
        self.ledger()
        self.chapter(ASSESSMENTS + '\n## Review Questions\n\n1. Different question.\n')
        before = self.ledger_path.read_bytes()
        code, report = self.run_count('--write')
        self.assertEqual(code, 1)
        self.assertIn('DUPLICATE_ASSESSMENT_SECTION', [d['code'] for d in report['diagnostics']])
        self.assertEqual(self.ledger_path.read_bytes(), before)

    def test_missing_answer_and_repeated_number_are_errors(self):
        body = ASSESSMENTS.replace('**4. C.**', '**2. C.**')
        report = Report('test', '')
        count.assessment_inventory(self.chapter(body), report)
        self.assertTrue({'DUPLICATE_ITEM_NUMBER', 'ANSWER_COVERAGE'} <= {d.code for d in report.diagnostics})

    def test_distributed_legacy_counts_are_not_silently_reallocated(self):
        ledger = self.ledger([concept(review_questions=2), concept(2, review_questions=2)])
        chapter = self.chapter(ids=[c['id'] for c in ledger.concepts])
        report = Report('test', '')
        self.assertEqual(count.planned_counts(ledger, [chapter], report), {})
        self.assertIn('ASSESSMENT_ALLOCATION', [d.code for d in report.diagnostics])

    def test_write_refuses_stale_read_and_existing_lock(self):
        ledger = self.ledger()
        changes = {concept()['id']: {'review_questions': 4}}
        self.ledger_path.write_bytes(ledger.original_bytes + b'\n# concurrent edit\n')
        with self.assertRaisesRegex(InputError, 'changed after'):
            count.write_counts(ledger, changes)
        current = read_ledger(self.ledger_path)
        lock = self.ledger_path.with_name('ledger.yaml.counts.lock')
        lock.write_text('other process')
        with self.assertRaisesRegex(InputError, 'lock exists'):
            count.write_counts(current, changes)
        self.assertEqual(lock.read_text(), 'other process')
        self.assertFalse(list(self.ledger_path.parent.glob('*.bak.*')))

    def test_aliases_are_readable_but_not_rewritten(self):
        self.ledger()
        text = self.ledger_path.read_text().replace('prerequisites: []', 'prerequisites: &empty []').replace('uses_terms: []', 'uses_terms: *empty')
        self.ledger_path.write_text(text)
        ledger = read_ledger(self.ledger_path)
        with self.assertRaisesRegex(InputError, 'aliases'):
            count.write_counts(ledger, {concept()['id']: {'review_questions': 4}})
        self.assertEqual(self.ledger_path.read_text(), text)


class LedgerLintTests(ProjectTest):
    def test_ownership_terms_symbols_notation_and_transitive_uses(self):
        a = concept(introduces_terms=['Unit'], introduces_symbols=['distance'], introduces_notation=['sqrt'])
        b = concept(2, prerequisites=[a['id']])
        c = concept(3, prerequisites=[b['id']], uses_terms=['unit'], uses_symbols=['distance'], uses_notation=['sqrt'])
        ledger = self.ledger([a, b, c])
        report = Report('test', '')
        ledger_lint.ownership_checks(ledger, report)
        self.assertFalse(any(d.severity == 'ERROR' for d in report.diagnostics))
        c['prerequisites'] = []
        c['uses_notation'].append('undefined')
        ledger = self.ledger([a, b, c])
        report = Report('test', '')
        ledger_lint.ownership_checks(ledger, report)
        self.assertTrue({'UNDEFINED_USE', 'UNSATISFIED_DEPENDENCY'} <= {d.code for d in report.diagnostics})

    def test_duplicate_owner_and_verified_split(self):
        ledger = self.ledger([concept(introduces_terms=['Slope']), concept(2, introduces_terms=['slope'], status='verified', split_required=True)])
        report = Report('test', '')
        ledger_lint.ownership_checks(ledger, report)
        self.assertTrue({'DUPLICATE_OWNER', 'VERIFIED_NEEDS_SPLIT'} <= {d.code for d in report.diagnostics})

    def test_glossary_alias_and_introduction_contract(self):
        ledger = self.ledger([concept(introduces_terms=['unit vector'], term_aliases={'unit vector': ['unit direction vector']})])
        chapter = self.chapter('\n## Key Terms\n\n| Term | Definition |\n|---|---|\n| unit direction vector | Vector of length one. |\n')
        report = Report('test', '')
        ledger_lint.glossary_checks(ledger, [chapter], report)
        self.assertFalse(report.diagnostics)

    def test_notation_sample_is_not_an_actual_registry(self):
        ledger = self.ledger([concept(introduces_symbols=['distance'])])
        path = self.root / 'meta' / 'notation.md'
        table = '| Symbol | Meaning | SI | USCS |\n|---|---|---|---|\n| distance | Distance | m | ft |\n'
        path.write_text('```md\n' + table + '```\n')
        report = Report('test', '')
        owners = ledger_lint.ownership_checks(ledger, report)
        ledger_lint.notation_checks(ledger, path, owners, report)
        self.assertIn('NOTATION_REGISTRY_MISSING', [d.code for d in report.diagnostics])
        path.write_text(table)
        report = Report('test', '')
        ledger_lint.notation_checks(ledger, path, owners, report)
        self.assertFalse(report.diagnostics)

    def test_figure_manifest_and_missing_asset(self):
        fid = 'FIG-01-01-001'
        ledger = self.ledger([concept(figures=[fid])])
        chapter = self.chapter(f'\n![{fid}: A steel beam supporting a centered load.](../figures/{fid}.png)\n')
        manifest = self.root / 'manifest.csv'
        manifest.write_text('Figure ID,Chapter,Section\nFIG-01-01-002,01-01,1.2\n')
        report = Report('test', '')
        owners = ledger_lint.ownership_checks(ledger, report)
        ledger_lint.figure_checks(ledger, [chapter], owners, report, manifest, True)
        self.assertTrue({'IMAGE_FILE_MISSING', 'MANIFEST_FIGURE_MISSING', 'MANIFEST_NOT_INLINE'} <= {d.code for d in report.diagnostics})


class StyleTests(ProjectTest):
    def test_orientation_exemptions_and_heading_aliases(self):
        body = '\n'.join('## ' + h + '\n' for h in style.BASE_SECTIONS)
        body = body.replace('## Review Questions\n', '## Review Questions\n### Conceptual\n### Calculation\n### Multiple Choice\n')
        chapter = self.chapter(body, chapter='00-01', ids=['ORIENT-0-001-01'])
        report = Report('test', '')
        style.structural_checks(chapter, report)
        self.assertFalse(report.diagnostics)
        chapter = self.chapter(body.replace('Quick Reference', 'Summary Card'), chapter='00-01', ids=['ORIENT-0-001-01'])
        report = Report('test', '')
        style.structural_checks(chapter, report)
        self.assertEqual([d.code for d in report.diagnostics], ['NONSTANDARD_HEADING'])

    def test_examples_accept_explicit_check_variants(self):
        for check in ['Check', 'Check numerically', 'Units check', 'Dimensional check', 'Verify']:
            with self.subTest(check=check):
                body = '\n## 1.1 Lesson\n\n### Worked Example 1\n\n' + '\n\n'.join(f'**{label}.** Content.' for label in ['Given','Find','Approach','Solution',check])
                report = Report('test', '')
                self.assertEqual(style.example_checks(self.chapter(body), report), 1)
                self.assertFalse(report.diagnostics)

    def test_margin_box_and_cross_chapter_citations(self):
        body = "\n## 1.1 Lesson\n\n> ---\n> **Mentor's Margin**\n>\n> Body.\n>\n> ---\n\nSee §1.1 and 01-02 §2.1.\n"
        a = self.chapter(body)
        b = self.chapter('\n## 2.1 Lesson\n', chapter='01-02', ids=['MATH-1A-002-01'])
        report = Report('test', '')
        style.quote_checks(a, report)
        style.citation_checks(a, {a.id:a,b.id:b}, report)
        self.assertFalse(report.diagnostics)
        a = self.chapter(body + '\nBare §2.1 is wrong here.\n')
        style.citation_checks(a, {a.id:a,b.id:b}, report)
        self.assertIn('BARE_FOREIGN_SECTION', [d.code for d in report.diagnostics])


class CommandLineTests(ProjectTest):
    def test_all_entry_points_missing_ledger_return_json_exit_2(self):
        for script in ('lint_ledger.py', 'count_assessments.py', 'lint_style.py'):
            with self.subTest(script=script):
                p = subprocess.run([sys.executable, str(TOOLS/script), '--root', str(self.root), '--format', 'json'], text=True, capture_output=True)
                self.assertEqual(p.returncode, 2)
                self.assertEqual(json.loads(p.stdout)['status'], 'INPUT_ERROR')
                self.assertEqual(p.stderr, '')

    def test_ledger_only_and_strict_exit_status(self):
        self.ledger()
        args = [sys.executable, str(TOOLS/'lint_ledger.py'), '--root', str(self.root), '--ledger-only', '--format', 'json']
        p = subprocess.run(args, text=True, capture_output=True)
        self.assertEqual(p.returncode, 0)
        self.assertEqual(json.loads(p.stdout)['status'], 'PASS_WITH_WARNINGS')
        p = subprocess.run(args + ['--strict'], text=True, capture_output=True)
        self.assertEqual(p.returncode, 1)
        self.assertEqual(json.loads(p.stdout)['status'], 'FAIL')


if __name__ == '__main__':
    unittest.main()
