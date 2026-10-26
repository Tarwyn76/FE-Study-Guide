#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

WORKED = re.compile(r'(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')

TAGS = {
    ('02-22','1'): [
        '<!-- VERIFY id="WE-02-22-001-weight" expr="20*9.81" expected="196.2" units="N" atol="0.01" rtol="1e-9" -->',
        '<!-- VERIFY id="WE-02-22-001-normal" expr="20*9.81" expected="196.2" units="N" atol="0.01" rtol="1e-9" -->',
    ],
    ('02-23','1'): [
        '<!-- VERIFY id="WE-02-23-001-fx" expr="500*cos(radians(30))" expected="433" units="N" atol="0.05" rtol="1e-9" -->',
        '<!-- VERIFY id="WE-02-23-001-fy" expr="500*sin(radians(30))" expected="250" units="N" atol="0.05" rtol="1e-9" -->',
    ],
    ('02-23','2'): [
        '<!-- VERIFY id="WE-02-23-002-resultant" expr="sqrt(300**2+400**2)" expected="500" units="N" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-25','1'): [
        '<!-- VERIFY id="WE-02-25-001-moment" expr="100*0.40" expected="40" units="N*m" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-25','2'): [
        '<!-- VERIFY id="WE-02-25-002-mz" expr="0.3*80-0.2*50" expected="14" units="N*m" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-25','3'): [
        '<!-- VERIFY id="WE-02-25-003-couple" expr="200*0.15" expected="30" units="N*m" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-26','1'): [
        '<!-- VERIFY id="WE-02-26-001-ay" expr="12/2" expected="6" units="kN" atol="1e-9" rtol="1e-9" -->',
        '<!-- VERIFY id="WE-02-26-001-by" expr="12/2" expected="6" units="kN" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-26','2'): [
        '<!-- VERIFY id="WE-02-26-002-by" expr="10*2/5" expected="4" units="kN" atol="1e-9" rtol="1e-9" -->',
        '<!-- VERIFY id="WE-02-26-002-ay" expr="10-(10*2/5)" expected="6" units="kN" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-26','3'): [
        '<!-- VERIFY id="WE-02-26-003-reactions" expr="1+1+1" expected="3" units="reactions" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-28','1'): [
        '<!-- VERIFY id="WE-02-28-001-resultant" expr="4*3" expected="12" units="kN" atol="1e-9" rtol="1e-9" -->',
        '<!-- VERIFY id="WE-02-28-001-location" expr="3/2" expected="1.5" units="m" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-28','2'): [
        '<!-- VERIFY id="WE-02-28-002-resultant" expr="0.5*6*4" expected="12" units="kN" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-28','4'): [
        '<!-- VERIFY id="WE-02-28-004-xbar" expr="(2*1+3*5)/(2+3)" expected="3.4" units="m" atol="1e-9" rtol="1e-9" -->',
    ],
    ('02-29','1'): [
        '<!-- VERIFY id="WE-02-29-001-ix" expr="0.20*0.30**3/12" expected="0.000450" units="m^4" atol="5e-10" rtol="1e-9" -->',
    ],
    ('02-29','2'): [
        '<!-- VERIFY id="WE-02-29-002-ix" expr="2.0e-6+0.001*0.05**2" expected="4.5e-6" units="m^4" atol="5e-12" rtol="1e-9" -->',
    ],
    ('02-29','5'): [
        '<!-- VERIFY id="WE-02-29-005-rx" expr="sqrt(8e-6/0.002)" expected="0.06325" units="m" atol="0.000005" rtol="1e-9" -->',
    ],
}

def chapter_id(path: Path) -> str:
    m = re.match(r'^(\d{2}-\d{2})-', path.name)
    if not m: raise ValueError(f'Cannot determine chapter ID: {path}')
    return m.group(1)

def apply_file(path: Path) -> int:
    cid = chapter_id(path)
    text = path.read_text(encoding='utf-8-sig')
    matches = list(WORKED.finditer(text))
    insertions = []
    for i,m in enumerate(matches):
        label = (m.group(1) or str(i+1)).strip()
        tags = TAGS.get((cid,label))
        if not tags: continue
        if any(t.split(' id="',1)[1].split('"',1)[0] in text for t in tags):
            continue
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        h2 = re.search(r'(?m)^##\s+', text[start:end])
        if h2: end = start+h2.start()
        insertions.append((end, '\n\n'+'\n'.join(tags)+'\n'))
    for pos, payload in reversed(insertions):
        text = text[:pos].rstrip()+payload+'\n'+text[pos:].lstrip('\n')
    path.write_text(text,encoding='utf-8')
    return len(insertions)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('directory', nargs='?', default='layer-1-substrate')
    args=ap.parse_args()
    root=Path(args.directory)
    touched=0
    for p in sorted(root.glob('02-*.md')):
        n=apply_file(p)
        if n:
            print(f'updated {p.name}: {n} worked-example blocks')
            touched += n
    print(f'updated blocks: {touched}')

if __name__=='__main__': main()
