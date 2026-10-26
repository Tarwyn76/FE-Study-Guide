#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

WORKED = re.compile(r'(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')

CORRECTIONS = {
    '02-50': [
        ('W=0.287*300*ln2=59.67 kJ.', 'W=0.287*300*ln2=59.68 kJ.'),
    ],
    '02-57': [
        ('Q=0.8σ(500^4-300^4)=2467 W.', 'Q=0.8σ(500^4-300^4)=2468 W.'),
    ],
}

TAGS = {
('02-50','1'): ['<!-- VERIFY id="WE-02-50-001-dU" expr="100-40" expected="60" units="kJ" atol="1e-9" rtol="1e-9" -->'],
('02-50','2'): ['<!-- VERIFY id="WE-02-50-002-dU" expr="80" expected="80" units="kJ" atol="1e-9" rtol="1e-9" -->'],
('02-50','3'): ['<!-- VERIFY id="WE-02-50-003-W" expr="200*0.5" expected="100" units="kJ" atol="1e-9" rtol="1e-9" -->'],
('02-50','4'): ['<!-- VERIFY id="WE-02-50-004-W" expr="0.287*300*ln(2)" expected="59.68" units="kJ" atol="0.005" rtol="1e-9" -->'],
('02-50','5'): ['<!-- VERIFY id="WE-02-50-005-W" expr="(150-200)/(1-1.3)" expected="166.7" units="kJ" atol="0.05" rtol="1e-9" -->'],

('02-51','1'): ['<!-- VERIFY id="WE-02-51-001-V2" expr="sqrt(2*(500-450)*1000)" expected="316.2" units="m/s" atol="0.05" rtol="1e-9" -->'],
('02-51','2'): ['<!-- VERIFY id="WE-02-51-002-work" expr="1200-900" expected="300" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],
('02-51','3'): ['<!-- VERIFY id="WE-02-51-003-work" expr="420-300" expected="120" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],
('02-51','4'): ['<!-- VERIFY id="WE-02-51-004-h2" expr="250" expected="250" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],
('02-51','5'): ['<!-- VERIFY id="WE-02-51-005-work" expr="0.001*5e6/1000" expected="5" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],
('02-51','8'): ['<!-- VERIFY id="WE-02-51-008-q" expr="1500-500" expected="1000" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],

('02-52','1'): ['<!-- VERIFY id="WE-02-52-001-dS" expr="100/500" expected="0.200" units="kJ/K" atol="0.0005" rtol="1e-9" -->'],
('02-52','2'): ['<!-- VERIFY id="WE-02-52-002-ds" expr="1.0*ln(600/300)" expected="0.693" units="kJ/kg*K" atol="0.0005" rtol="1e-9" -->'],
('02-52','3'): ['<!-- VERIFY id="WE-02-52-003-ds" expr="0.5*ln(600/300)" expected="0.347" units="kJ/kg*K" atol="0.0005" rtol="1e-9" -->'],

('02-53','1'): ['<!-- VERIFY id="WE-02-53-001-eff" expr="100*(1000-600)/1000" expected="40" units="percent" atol="0.05" rtol="1e-9" -->'],
('02-53','2'): ['<!-- VERIFY id="WE-02-53-002-eff" expr="100*(1-300/900)" expected="66.7" units="percent" atol="0.05" rtol="1e-9" -->'],
('02-53','3'): ['<!-- VERIFY id="WE-02-53-003-eff" expr="100*(1-1/(8**(1.4-1)))" expected="56.5" units="percent" atol="0.05" rtol="1e-9" -->'],
('02-53','4'): ['<!-- VERIFY id="WE-02-53-004-eff" expr="100*((3200-2300)-(210-200))/(3200-210)" expected="29.77" units="percent" atol="0.005" rtol="1e-9" -->'],
('02-53','5'): ['<!-- VERIFY id="WE-02-53-005-net-work" expr="500-300" expected="200" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],

('02-54','1'): ['<!-- VERIFY id="WE-02-54-001-COPR" expr="10/2" expected="5" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('02-54','2'): ['<!-- VERIFY id="WE-02-54-002-COPHP" expr="(10+2)/2" expected="6" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('02-54','3'): ['<!-- VERIFY id="WE-02-54-003-COPR" expr="270/(300-270)" expected="9" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('02-54','4'): ['<!-- VERIFY id="WE-02-54-004-COPR" expr="(400-250)/(450-400)" expected="3" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('02-54','5'): ['<!-- VERIFY id="WE-02-54-005-tons" expr="105.5/3.516" expected="30.0" units="ton refrigeration" atol="0.05" rtol="1e-9" -->'],
('02-54','6'): ['<!-- VERIFY id="WE-02-54-006-mdot" expr="30/(400-250)" expected="0.20" units="kg/s" atol="0.005" rtol="1e-9" -->'],

('02-55','1'): ['<!-- VERIFY id="WE-02-55-001-Q" expr="2*4*20/0.1" expected="1600" units="W" atol="1e-9" rtol="1e-9" -->'],
('02-55','2'): ['<!-- VERIFY id="WE-02-55-002-R" expr="0.05/(0.5*2)" expected="0.05" units="K/W" atol="1e-9" rtol="1e-9" -->'],
('02-55','3'): ['<!-- VERIFY id="WE-02-55-003-Rconv" expr="1/(25*4)" expected="0.010" units="K/W" atol="0.0005" rtol="1e-9" -->'],
('02-55','4'): ['<!-- VERIFY id="WE-02-55-004-Q" expr="70/(0.02+0.04+0.01)" expected="1000" units="W" atol="1e-9" rtol="1e-9" -->'],
('02-55','5'): ['<!-- VERIFY id="WE-02-55-005-R" expr="ln(0.04/0.02)/(2*pi*0.2*1)" expected="0.552" units="K/W" atol="0.0005" rtol="1e-9" -->'],
('02-55','8'): ['<!-- VERIFY id="WE-02-55-008-rcrit" expr="0.05/10" expected="0.005" units="m" atol="0.0000005" rtol="1e-9" -->'],

('02-56','1'): ['<!-- VERIFY id="WE-02-56-001-Bi" expr="20*0.001/(50*0.06)" expected="0.00667" units="dimensionless" atol="0.000005" rtol="1e-9" -->'],
('02-56','3'): ['<!-- VERIFY id="WE-02-56-003-tau" expr="7800*0.001*500/(20*0.06)" expected="3250" units="s" atol="1e-9" rtol="1e-9" -->'],
('02-56','4'): ['<!-- VERIFY id="WE-02-56-004-ratio" expr="exp(-1)" expected="0.3679" units="dimensionless" atol="0.00005" rtol="1e-9" -->'],
('02-56','5'): ['<!-- VERIFY id="WE-02-56-005-alpha" expr="15/(8000*500)" expected="3.75e-6" units="m^2/s" atol="1e-12" rtol="1e-9" -->'],
('02-56','6'): ['<!-- VERIFY id="WE-02-56-006-Fo" expr="(15/(8000*500))*100/(0.02**2)" expected="0.9375" units="dimensionless" atol="0.00005" rtol="1e-9" -->'],

('02-57','1'): ['<!-- VERIFY id="WE-02-57-001-Q" expr="50*2*(100-20)" expected="8000" units="W" atol="1e-9" rtol="1e-9" -->'],
('02-57','2'): ['<!-- VERIFY id="WE-02-57-002-Nu" expr="120*0.05/0.6" expected="10" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('02-57','3'): ['<!-- VERIFY id="WE-02-57-003-Re" expr="1000*2*0.05/0.001" expected="100000" units="dimensionless" atol="1e-6" rtol="1e-9" -->'],
('02-57','4'): ['<!-- VERIFY id="WE-02-57-004-Pr" expr="4180*0.001/0.6" expected="6.97" units="dimensionless" atol="0.005" rtol="1e-9" -->'],
('02-57','6'): ['<!-- VERIFY id="WE-02-57-006-Qemit" expr="0.8*5.67e-8*500**4" expected="2835" units="W" atol="0.5" rtol="1e-9" -->'],
('02-57','7'): ['<!-- VERIFY id="WE-02-57-007-Qnet" expr="0.8*5.67e-8*(500**4-300**4)" expected="2468" units="W" atol="0.5" rtol="1e-9" -->'],

('02-58','1'): ['<!-- VERIFY id="WE-02-58-001-Q" expr="4*(120-80)" expected="160" units="kW" atol="1e-9" rtol="1e-9" -->'],
('02-58','2'): ['<!-- VERIFY id="WE-02-58-002-Tco" expr="20+160/2" expected="100" units="degC" atol="1e-9" rtol="1e-9" -->'],
('02-58','3'): ['<!-- VERIFY id="WE-02-58-003-LMTD" expr="(40-20)/ln(40/20)" expected="28.85" units="K" atol="0.005" rtol="1e-9" -->'],
('02-58','4'): ['<!-- VERIFY id="WE-02-58-004-Q" expr="500*10*1*30/1000" expected="150" units="kW" atol="1e-9" rtol="1e-9" -->'],
('02-58','5'): [
'<!-- VERIFY id="WE-02-58-005-Cmin" expr="min(5,3)" expected="3" units="kW/K" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-58-005-Qmax" expr="min(5,3)*(120-20)" expected="300" units="kW" atol="1e-9" rtol="1e-9" -->'],
('02-58','6'): ['<!-- VERIFY id="WE-02-58-006-eff" expr="180/300" expected="0.60" units="dimensionless" atol="0.005" rtol="1e-9" -->'],
('02-58','7'): ['<!-- VERIFY id="WE-02-58-007-NTU" expr="6/3" expected="2" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('02-58','8'): ['<!-- VERIFY id="WE-02-58-008-Cr" expr="3/5" expected="0.60" units="dimensionless" atol="0.005" rtol="1e-9" -->'],

('02-59','1'): ['<!-- VERIFY id="WE-02-59-001-q" expr="2*15" expected="30" units="C" atol="1e-9" rtol="1e-9" -->'],
('02-59','3'): ['<!-- VERIFY id="WE-02-59-003-R" expr="1.72e-8*10/(1.0e-6)" expected="0.172" units="ohm" atol="0.0005" rtol="1e-9" -->'],
('02-59','4'): ['<!-- VERIFY id="WE-02-59-004-I" expr="12/6" expected="2" units="A" atol="1e-9" rtol="1e-9" -->'],
('02-59','5'): ['<!-- VERIFY id="WE-02-59-005-R" expr="10*(1+0.004*(70-20))" expected="12" units="ohm" atol="1e-9" rtol="1e-9" -->'],
('02-59','6'): ['<!-- VERIFY id="WE-02-59-006-P" expr="24*3" expected="72" units="W" atol="1e-9" rtol="1e-9" -->'],
('02-59','7'): [
'<!-- VERIFY id="WE-02-59-007-EkWh" expr="100/1000*5" expected="0.500" units="kWh" atol="0.0005" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-59-007-EMJ" expr="100*5*3600/1e6" expected="1.80" units="MJ" atol="0.005" rtol="1e-9" -->'],
('02-59','8'): ['<!-- VERIFY id="WE-02-59-008-P" expr="5**2*4" expected="100" units="W" atol="1e-9" rtol="1e-9" -->'],
('02-59','9'): ['<!-- VERIFY id="WE-02-59-009-P" expr="10**2/20" expected="5" units="W" atol="1e-9" rtol="1e-9" -->'],
}

def chapter_id(path: Path) -> str:
    m = re.match(r'^(\d{2}-\d{2})-', path.name)
    if not m: raise ValueError(f'Cannot determine chapter ID: {path}')
    return m.group(1)

def apply_file(path: Path) -> tuple[int,int]:
    cid = chapter_id(path)
    text = path.read_text(encoding='utf-8-sig')
    corrections = 0
    for old,new in CORRECTIONS.get(cid, []):
        if new in text:
            continue
        if old not in text:
            raise RuntimeError(f'Expected correction source text not found in {path.name}: {old}')
        text = text.replace(old,new,1)
        corrections += 1
    matches = list(WORKED.finditer(text))
    insertions = []
    for i,m in enumerate(matches):
        label = (m.group(1) or str(i+1)).strip()
        tags = TAGS.get((cid,label))
        if not tags: continue
        if all(t.split(' id="',1)[1].split('"',1)[0] in text for t in tags):
            continue
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        h2 = re.search(r'(?m)^##\s+', text[start:end])
        if h2: end = start+h2.start()
        missing = [t for t in tags if t.split(' id="',1)[1].split('"',1)[0] not in text]
        if missing:
            insertions.append((end, '\n\n'+'\n'.join(missing)+'\n'))
    for pos, payload in reversed(insertions):
        text = text[:pos].rstrip()+payload+'\n'+text[pos:].lstrip('\n')
    path.write_text(text,encoding='utf-8')
    return len(insertions), corrections

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('directory', nargs='?', default='layer-1-substrate')
    args=ap.parse_args()
    root=Path(args.directory)
    touched=corrected=0
    for p in sorted(root.glob('02-*.md')):
        n,c=apply_file(p)
        if n or c:
            print(f'updated {p.name}: {n} worked-example blocks; {c} corrections')
            touched += n; corrected += c
    print(f'updated blocks: {touched}; chapter corrections: {corrected}')

if __name__=='__main__': main()
