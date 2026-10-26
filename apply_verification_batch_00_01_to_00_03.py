from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'source'
DST = ROOT / 'layer-0-orientation'

TAGS = {
    '00-02-the-exam-and-the-cbt-format.md': {
        '1 — Building a Time Budget': [
            '<!-- VERIFY id="WE-00-02-001-working-minutes" expr="5*60+20" expected="320" units="min" atol="1e-12" rtol="1e-12" -->',
            '<!-- VERIFY id="WE-00-02-001-average-minutes" expr="320/110" expected="2.91" units="min/question" atol="0.005" rtol="1e-12" -->',
            '<!-- VERIFY id="WE-00-02-001-rounded-seconds" expr="(320/110)*60" expected="175" units="s/question" atol="0.5" rtol="1e-12" -->',
            '<!-- VERIFY id="WE-00-02-001-quarter-checkpoint" expr="320/4" expected="80" units="min" atol="1e-12" rtol="1e-12" -->',
        ],
    },
}

HEAD = re.compile(r'(?m)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')

def insert_tags(text, mapping):
    matches = list(HEAD.finditer(text))
    for idx in range(len(matches)-1, -1, -1):
        m = matches[idx]
        label = (m.group(1) or str(idx+1)).strip()
        tags = mapping.get(label)
        if not tags:
            continue
        end = matches[idx+1].start() if idx+1 < len(matches) else len(text)
        block = text[m.start():end]
        if '<!-- VERIFY' in block:
            continue
        # Insert after the Check paragraph when present; otherwise before next thematic separator.
        check = re.search(r'(?ms)^\*\*Check\.\*\*.*?(?=\n\n(?:\*\*Interpretation|\|-----------\||---|##\s)|\Z)', block)
        if check:
            insert_pos = m.start() + check.end()
        else:
            rel = block.find('\n---')
            insert_pos = m.start() + (rel if rel >= 0 else len(block))
        tag_text = '\n\n' + '\n'.join(tags)
        text = text[:insert_pos] + tag_text + text[insert_pos:]
    return text

def main():
    DST.mkdir(parents=True, exist_ok=True)
    for p in sorted(SRC.glob('*.md')):
        txt = p.read_text(encoding='utf-8')
        txt = insert_tags(txt, TAGS.get(p.name, {}))
        (DST / p.name).write_text(txt, encoding='utf-8')
    print(f'Wrote {len(list(DST.glob("*.md")))} verified front-matter chapter copies to {DST}')

if __name__ == '__main__':
    main()
