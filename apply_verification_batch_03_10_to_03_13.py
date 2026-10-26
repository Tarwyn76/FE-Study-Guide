#!/usr/bin/env python3
from __future__ import annotations
import argparse,re
from pathlib import Path

WORKED=re.compile(r'(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')
CORRECTIONS={}
TAGS={
('03-10','1'): ['<!-- VERIFY id="WE-03-10-001-rate" expr="10/(2*5)" expected="1" units="mol/(L*min)" atol="1e-9" rtol="1e-9" -->'],
('03-10','2'): ['<!-- VERIFY id="WE-03-10-002-order" expr="2+1" expected="3" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('03-10','3'): ['<!-- VERIFY id="WE-03-10-003-fraction" expr="exp(-0.2*5)" expected="0.3679" units="dimensionless" atol="0.00005" rtol="1e-9" -->'],
('03-10','6'): ['<!-- VERIFY id="WE-03-10-006-vmaxfrac" expr="1/(1+1)" expected="0.5" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('03-10','7'): ['<!-- VERIFY id="WE-03-10-007-D" expr="5*10" expected="50" units="mol" atol="1e-9" rtol="1e-9" -->'],
('03-10','8'): ['<!-- VERIFY id="WE-03-10-008-time" expr="10/2" expected="5" units="min" atol="1e-9" rtol="1e-9" -->'],
('03-10','9'): ['<!-- VERIFY id="WE-03-10-009-CA" expr="1/(1/2+0.1*5)" expected="1" units="mol/L" atol="1e-9" rtol="1e-9" -->'],

('03-11','1'): ['<!-- VERIFY id="WE-03-11-001-time" expr="-ln(0.1)/0.1" expected="23.03" units="min" atol="0.005" rtol="1e-9" -->'],
('03-11','2'): ['<!-- VERIFY id="WE-03-11-002-Vratio" expr="1+0.5*0.8" expected="1.4" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('03-11','3'): ['<!-- VERIFY id="WE-03-11-003-V" expr="10*0.6/2" expected="3" units="m3" atol="1e-9" rtol="1e-9" -->'],
('03-11','4'): ['<!-- VERIFY id="WE-03-11-004-V" expr="10*0.6/2" expected="3" units="m3" atol="1e-9" rtol="1e-9" -->'],
('03-11','5'): ['<!-- VERIFY id="WE-03-11-005-ratio" expr="(1/(1+1))**2" expected="0.25" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('03-11','8'): ['<!-- VERIFY id="WE-03-11-008-ratio" expr="1/(1+1)" expected="0.5" units="dimensionless" atol="1e-9" rtol="1e-9" -->','<!-- VERIFY id="WE-03-11-008-X" expr="1-1/(1+1)" expected="0.5" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('03-11','9'): ['<!-- VERIFY id="WE-03-11-009-X" expr="1-exp(-1)" expected="0.632" units="dimensionless" atol="0.0002" rtol="1e-9" -->'],

('03-12','3'): ['<!-- VERIFY id="WE-03-12-003-area" expr="500/(1*25)" expected="20" units="m2" atol="1e-9" rtol="1e-9" -->'],
('03-12','5'): ['<!-- VERIFY id="WE-03-12-005-cost" expr="200000*650/500" expected="260000" units="USD" atol="0.5" rtol="1e-9" -->'],
('03-12','6'): ['<!-- VERIFY id="WE-03-12-006-ratio" expr="2**0.6" expected="1.516" units="dimensionless" atol="0.0005" rtol="1e-9" -->'],
('03-12','8'): ['<!-- VERIFY id="WE-03-12-008-capital" expr="1000000*5" expected="5000000" units="USD" atol="0.5" rtol="1e-9" -->'],

('03-13','3'): ['<!-- VERIFY id="WE-03-13-003-B" expr="2.5*4" expected="10" units="kg/s" atol="1e-9" rtol="1e-9" -->'],
}

def chapter_id(path:Path)->str:
    m=re.match(r'^(\d{2}-\d{2})-',path.name)
    if not m: raise ValueError(path)
    return m.group(1)

def apply_file(path:Path):
    cid=chapter_id(path); text=path.read_text(encoding='utf-8-sig'); corrections=0
    for old,new in CORRECTIONS.get(cid,[]):
        if new in text: continue
        if old not in text: raise RuntimeError(f'Correction source missing in {path.name}: {old}')
        text=text.replace(old,new,1); corrections+=1
    ms=list(WORKED.finditer(text)); ins=[]
    for i,m in enumerate(ms):
        label=(m.group(1) or str(i+1)).strip(); tags=TAGS.get((cid,label))
        if not tags: continue
        start=m.end(); end=ms[i+1].start() if i+1<len(ms) else len(text)
        h2=re.search(r'(?m)^##\s+',text[start:end])
        if h2: end=start+h2.start()
        missing=[t for t in tags if t.split(' id="',1)[1].split('"',1)[0] not in text]
        if missing: ins.append((end,'\n\n'+'\n'.join(missing)+'\n'))
    for pos,payload in reversed(ins):
        text=text[:pos].rstrip()+payload+'\n'+text[pos:].lstrip('\n')
    path.write_text(text,encoding='utf-8')
    return len(ins),corrections

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('directory',nargs='?',default='layer-1-substrate'); a=ap.parse_args(); root=Path(a.directory)
    touched=corrected=0
    for p in sorted(root.glob('*.md')):
        n,c=apply_file(p)
        if n or c: print(f'updated {p.name}: {n} worked-example blocks; {c} corrections')
        touched+=n; corrected+=c
    print(f'updated blocks: {touched}; chapter corrections: {corrected}')
if __name__=='__main__': main()
