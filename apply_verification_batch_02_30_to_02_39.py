#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

WORKED = re.compile(r'(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')

TAGS = {
('02-30','1'): ['<!-- VERIFY id="WE-02-30-001-fmax" expr="0.40*100" expected="40" units="N" atol="1e-9" rtol="1e-9" -->'],
('02-30','2'): ['<!-- VERIFY id="WE-02-30-002-friction" expr="min(25,0.40*100)" expected="25" units="N" atol="1e-9" rtol="1e-9" -->'],
('02-30','3'): ['<!-- VERIFY id="WE-02-30-003-fk" expr="0.30*100" expected="30" units="N" atol="1e-9" rtol="1e-9" -->'],
('02-30','4'): ['<!-- VERIFY id="WE-02-30-004-normal" expr="500*cos(radians(20))" expected="469.8" units="N" atol="0.05" rtol="1e-9" -->'],
('02-30','8'): ['<!-- VERIFY id="WE-02-30-008-tight" expr="100*exp(0.2*pi)" expected="187.4" units="N" atol="0.05" rtol="1e-9" -->'],

('02-31','1'): ['<!-- VERIFY id="WE-02-31-001-v" expr="5+2*4" expected="13" units="m/s" atol="1e-9" rtol="1e-9" -->'],
('02-31','2'): ['<!-- VERIFY id="WE-02-31-002-ds" expr="5*4+0.5*2*4**2" expected="36" units="m" atol="1e-9" rtol="1e-9" -->'],
('02-31','3'): ['<!-- VERIFY id="WE-02-31-003-speed" expr="9.81*2" expected="19.62" units="m/s" atol="0.005" rtol="1e-9" -->'],
('02-31','4'): ['<!-- VERIFY id="WE-02-31-004-a" expr="2*3" expected="6" units="m/s^2" atol="1e-9" rtol="1e-9" -->'],
('02-31','9'): ['<!-- VERIFY id="WE-02-31-009-vrel" expr="20-15" expected="5" units="m/s" atol="1e-9" rtol="1e-9" -->'],

('02-32','1'): [
'<!-- VERIFY id="WE-02-32-001-vx" expr="20*cos(radians(30))" expected="17.32" units="m/s" atol="0.005" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-32-001-vy" expr="20*sin(radians(30))" expected="10.0" units="m/s" atol="0.005" rtol="1e-9" -->'],
('02-32','2'): ['<!-- VERIFY id="WE-02-32-002-time" expr="2*(20*sin(radians(30)))/9.81" expected="2.039" units="s" atol="0.0005" rtol="1e-9" -->'],
('02-32','3'): ['<!-- VERIFY id="WE-02-32-003-an" expr="12**2/8" expected="18" units="m/s^2" atol="1e-9" rtol="1e-9" -->'],
('02-32','4'): ['<!-- VERIFY id="WE-02-32-004-v" expr="0.4*10" expected="4" units="m/s" atol="1e-9" rtol="1e-9" -->'],
('02-32','5'): ['<!-- VERIFY id="WE-02-32-005-an" expr="0.4*10**2" expected="40" units="m/s^2" atol="1e-9" rtol="1e-9" -->'],
('02-32','9'): [
'<!-- VERIFY id="WE-02-32-009-vrel-x" expr="5-1" expected="4" units="m/s" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-32-009-vrel-y" expr="2-(-1)" expected="3" units="m/s" atol="1e-9" rtol="1e-9" -->'],

('02-33','1'): ['<!-- VERIFY id="WE-02-33-001-a" expr="50/10" expected="5" units="m/s^2" atol="1e-9" rtol="1e-9" -->'],
('02-33','2'): ['<!-- VERIFY id="WE-02-33-002-weight" expr="5*9.81" expected="49.05" units="N" atol="0.005" rtol="1e-9" -->'],
('02-33','3'): ['<!-- VERIFY id="WE-02-33-003-fn" expr="2*6**2/3" expected="24" units="N" atol="1e-9" rtol="1e-9" -->'],
('02-33','4'): ['<!-- VERIFY id="WE-02-33-004-a" expr="(100-30)/20" expected="3.5" units="m/s^2" atol="1e-9" rtol="1e-9" -->'],

('02-34','1'): ['<!-- VERIFY id="WE-02-34-001-work" expr="50*4" expected="200" units="J" atol="1e-9" rtol="1e-9" -->'],
('02-34','2'): ['<!-- VERIFY id="WE-02-34-002-ke" expr="0.5*2*5**2" expected="25" units="J" atol="1e-9" rtol="1e-9" -->'],
('02-34','3'): ['<!-- VERIFY id="WE-02-34-003-dv" expr="3*9.81*2" expected="58.86" units="J" atol="0.005" rtol="1e-9" -->'],
('02-34','4'): ['<!-- VERIFY id="WE-02-34-004-spring" expr="0.5*400*0.10**2" expected="2" units="J" atol="1e-9" rtol="1e-9" -->'],
('02-34','5'): ['<!-- VERIFY id="WE-02-34-005-power" expr="100*3" expected="300" units="W" atol="1e-9" rtol="1e-9" -->'],
('02-34','6'): ['<!-- VERIFY id="WE-02-34-006-power" expr="20*100" expected="2000" units="W" atol="1e-9" rtol="1e-9" -->'],
('02-34','7'): [
'<!-- VERIFY id="WE-02-34-007-eff-frac" expr="4/5" expected="0.80" units="fraction" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-34-007-eff-pct" expr="100*4/5" expected="80" units="percent" atol="1e-9" rtol="1e-9" -->'],

('02-35','1'): ['<!-- VERIFY id="WE-02-35-001-p" expr="2*5" expected="10" units="kg*m/s" atol="1e-9" rtol="1e-9" -->'],
('02-35','2'): ['<!-- VERIFY id="WE-02-35-002-impulse" expr="20*0.5" expected="10" units="N*s" atol="1e-9" rtol="1e-9" -->'],
('02-35','3'): [
'<!-- VERIFY id="WE-02-35-003-p2" expr="2*5-4" expected="6" units="kg*m/s" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-35-003-v2" expr="(2*5-4)/2" expected="3" units="m/s" atol="1e-9" rtol="1e-9" -->'],
('02-35','4'): ['<!-- VERIFY id="WE-02-35-004-v" expr="(2*4+3*0)/(2+3)" expected="1.6" units="m/s" atol="1e-9" rtol="1e-9" -->'],

('02-36','1'): ['<!-- VERIFY id="WE-02-36-001-v" expr="0.5*8" expected="4" units="m/s" atol="1e-9" rtol="1e-9" -->'],
('02-36','2'): ['<!-- VERIFY id="WE-02-36-002-at" expr="0.5*3" expected="1.5" units="m/s^2" atol="1e-9" rtol="1e-9" -->'],
('02-36','3'): ['<!-- VERIFY id="WE-02-36-003-an" expr="0.5*8**2" expected="32" units="m/s^2" atol="1e-9" rtol="1e-9" -->'],
('02-36','4'): ['<!-- VERIFY id="WE-02-36-004-I" expr="0.5*10*0.4**2" expected="0.8" units="kg*m^2" atol="1e-9" rtol="1e-9" -->'],
('02-36','6'): ['<!-- VERIFY id="WE-02-36-006-ke" expr="0.5*5*2**2+0.5*0.4*3**2" expected="11.8" units="J" atol="1e-9" rtol="1e-9" -->'],

('02-37','1'): ['<!-- VERIFY id="WE-02-37-001-stress" expr="20000/400" expected="50" units="MPa" atol="1e-9" rtol="1e-9" -->'],
('02-37','2'): ['<!-- VERIFY id="WE-02-37-002-strain" expr="0.001/2" expected="0.0005" units="strain" atol="1e-12" rtol="1e-9" -->'],
('02-37','3'): ['<!-- VERIFY id="WE-02-37-003-stress" expr="200000*0.0005" expected="100" units="MPa" atol="1e-9" rtol="1e-9" -->'],
('02-37','4'): [
'<!-- VERIFY id="WE-02-37-004-delta-m" expr="30000*2/(300e-6*200e9)" expected="0.001" units="m" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-37-004-delta-mm" expr="1000*30000*2/(300e-6*200e9)" expected="1.0" units="mm" atol="1e-9" rtol="1e-9" -->'],
('02-37','5'): [
'<!-- VERIFY id="WE-02-37-005-delta-m" expr="12e-6*3*50" expected="0.0018" units="m" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-37-005-delta-mm" expr="1000*12e-6*3*50" expected="1.8" units="mm" atol="1e-9" rtol="1e-9" -->'],
('02-37','6'): ['<!-- VERIFY id="WE-02-37-006-stress" expr="200e9*12e-6*50/1e6" expected="120" units="MPa" atol="1e-9" rtol="1e-9" -->'],
('02-37','7'): ['<!-- VERIFY id="WE-02-37-007-G" expr="200/(2*(1+0.30))" expected="76.9" units="GPa" atol="0.05" rtol="1e-9" -->'],
('02-37','8'): ['<!-- VERIFY id="WE-02-37-008-hoop" expr="2e6*0.25/0.005/1e6" expected="100" units="MPa" atol="1e-9" rtol="1e-9" -->'],
('02-37','9'): ['<!-- VERIFY id="WE-02-37-009-axial" expr="2e6*0.25/(2*0.005)/1e6" expected="50" units="MPa" atol="1e-9" rtol="1e-9" -->'],

('02-38','1'): ['<!-- VERIFY id="WE-02-38-001-J" expr="pi*0.04**4/32" expected="2.513e-7" units="m^4" atol="5e-11" rtol="1e-9" -->'],
('02-38','2'): ['<!-- VERIFY id="WE-02-38-002-tau" expr="500*0.02/(pi*0.04**4/32)/1e6" expected="39.8" units="MPa" atol="0.05" rtol="1e-9" -->'],
('02-38','3'): [
'<!-- VERIFY id="WE-02-38-003-phi-rad" expr="500*1/(80e9*(pi*0.04**4/32))" expected="0.02487" units="rad" atol="0.000005" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-38-003-phi-deg" expr="degrees(500*1/(80e9*(pi*0.04**4/32)))" expected="1.425" units="deg" atol="0.0005" rtol="1e-9" -->'],
('02-38','6'): ['<!-- VERIFY id="WE-02-38-006-torque" expr="10000/100" expected="100" units="N*m" atol="1e-9" rtol="1e-9" -->'],

('02-39','1'): [
'<!-- VERIFY id="WE-02-39-001-RA" expr="10/2" expected="5" units="kN" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-39-001-RB" expr="10/2" expected="5" units="kN" atol="1e-9" rtol="1e-9" -->'],
('02-39','2'): ['<!-- VERIFY id="WE-02-39-002-Mmax" expr="10*4/4" expected="10" units="kN*m" atol="1e-9" rtol="1e-9" -->'],
('02-39','3'): ['<!-- VERIFY id="WE-02-39-003-dVdx" expr="-3" expected="-3" units="kN/m" atol="1e-9" rtol="1e-9" -->'],
('02-39','5'): ['<!-- VERIFY id="WE-02-39-005-stress" expr="5000*0.05/8e-6/1e6" expected="31.25" units="MPa" atol="1e-9" rtol="1e-9" -->'],
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
