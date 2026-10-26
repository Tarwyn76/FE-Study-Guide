#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

WORKED = re.compile(r'(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')

TAGS = {
('02-40','1'): ['<!-- VERIFY id="WE-02-40-001-center" expr="(80+20)/2" expected="50" units="MPa" atol="1e-9" rtol="1e-9" -->'],
('02-40','2'): ['<!-- VERIFY id="WE-02-40-002-radius" expr="sqrt(((80-20)/2)**2+30**2)" expected="42.43" units="MPa" atol="0.005" rtol="1e-9" -->'],
('02-40','3'): [
'<!-- VERIFY id="WE-02-40-003-sigma1" expr="(80+20)/2+sqrt(((80-20)/2)**2+30**2)" expected="92.43" units="MPa" atol="0.005" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-40-003-sigma2" expr="(80+20)/2-sqrt(((80-20)/2)**2+30**2)" expected="7.57" units="MPa" atol="0.005" rtol="1e-9" -->'],
('02-40','4'): ['<!-- VERIFY id="WE-02-40-004-taumax-in" expr="sqrt(((80-20)/2)**2+30**2)" expected="42.43" units="MPa" atol="0.005" rtol="1e-9" -->'],
('02-40','6'): ['<!-- VERIFY id="WE-02-40-006-taumax-3d" expr="(92.43-0)/2" expected="46.22" units="MPa" atol="0.0051" rtol="1e-9" -->'],

('02-41','1'): ['<!-- VERIFY id="WE-02-41-001-gamma" expr="1000*9.81/1000" expected="9.81" units="kN/m^3" atol="1e-9" rtol="1e-9" -->'],
('02-41','2'): ['<!-- VERIFY id="WE-02-41-002-rho" expr="0.85*1000" expected="850" units="kg/m^3" atol="1e-9" rtol="1e-9" -->'],
('02-41','3'): ['<!-- VERIFY id="WE-02-41-003-pabs" expr="250+101" expected="351" units="kPa" atol="1e-9" rtol="1e-9" -->'],
('02-41','4'): ['<!-- VERIFY id="WE-02-41-004-nu" expr="0.002/800" expected="2.50e-6" units="m^2/s" atol="1e-12" rtol="1e-9" -->'],
('02-41','5'): ['<!-- VERIFY id="WE-02-41-005-tau" expr="0.5*4" expected="2.0" units="Pa" atol="1e-9" rtol="1e-9" -->'],
('02-41','6'): ['<!-- VERIFY id="WE-02-41-006-pressure" expr="1000*9.81*3/1000" expected="29.43" units="kPa" atol="0.005" rtol="1e-9" -->'],
('02-41','7'): ['<!-- VERIFY id="WE-02-41-007-rise" expr="4*0.072/(9810*0.001)" expected="0.0294" units="m" atol="0.00005" rtol="1e-9" -->'],

('02-42','1'): ['<!-- VERIFY id="WE-02-42-001-dp" expr="1000*9.81*0.40/1000" expected="3.924" units="kPa" atol="0.0005" rtol="1e-9" -->'],
('02-42','2'): ['<!-- VERIFY id="WE-02-42-002-patm" expr="13600*9.81*0.760/1000" expected="101.4" units="kPa" atol="0.005" rtol="1e-9" -->'],
('02-42','3'): ['<!-- VERIFY id="WE-02-42-003-fb" expr="1000*9.81*0.020" expected="196.2" units="N" atol="0.05" rtol="1e-9" -->'],
('02-42','4'): ['<!-- VERIFY id="WE-02-42-004-volume" expr="490.5/(1000*9.81)" expected="0.0500" units="m^3" atol="0.00005" rtol="1e-9" -->'],
('02-42','5'): ['<!-- VERIFY id="WE-02-42-005-force" expr="1000*9.81*3*2/1000" expected="58.86" units="kN" atol="0.005" rtol="1e-9" -->'],

('02-43','1'): ['<!-- VERIFY id="WE-02-43-001-Q" expr="0.020*3" expected="0.060" units="m^3/s" atol="0.0005" rtol="1e-9" -->'],
('02-43','2'): ['<!-- VERIFY id="WE-02-43-002-mdot" expr="1000*0.060" expected="60" units="kg/s" atol="1e-9" rtol="1e-9" -->'],
('02-43','3'): ['<!-- VERIFY id="WE-02-43-003-v2" expr="0.040*2/0.010" expected="8" units="m/s" atol="1e-9" rtol="1e-9" -->'],
('02-43','4'): ['<!-- VERIFY id="WE-02-43-004-v2" expr="1.2*0.10*5/(0.9*0.08)" expected="8.33" units="m/s" atol="0.005" rtol="1e-9" -->'],
('02-43','5'): ['<!-- VERIFY id="WE-02-43-005-outflow" expr="2+3" expected="5" units="kg/s" atol="1e-9" rtol="1e-9" -->'],

('02-44','1'): ['<!-- VERIFY id="WE-02-44-001-pressure" expr="9810*12/1000" expected="117.7" units="kPa" atol="0.05" rtol="1e-9" -->'],
('02-44','2'): ['<!-- VERIFY id="WE-02-44-002-vhead" expr="6**2/(2*9.81)" expected="1.835" units="m" atol="0.0005" rtol="1e-9" -->'],
('02-44','3'): ['<!-- VERIFY id="WE-02-44-003-speed" expr="sqrt(2*9.81*20)" expected="19.81" units="m/s" atol="0.005" rtol="1e-9" -->'],
('02-44','5'): ['<!-- VERIFY id="WE-02-44-005-dp" expr="1000*9.81*4/1000" expected="39.24" units="kPa" atol="0.005" rtol="1e-9" -->'],

('02-45','1'): ['<!-- VERIFY id="WE-02-45-001-Re" expr="2*0.05/1.0e-6" expected="100000" units="dimensionless" atol="1e-6" rtol="1e-9" -->'],
('02-45','2'): ['<!-- VERIFY id="WE-02-45-002-f" expr="64/1000" expected="0.064" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('02-45','3'): ['<!-- VERIFY id="WE-02-45-003-hf" expr="0.02*(50/0.10)*(2**2/(2*9.81))" expected="2.04" units="m" atol="0.005" rtol="1e-9" -->'],
('02-45','4'): ['<!-- VERIFY id="WE-02-45-004-hm" expr="1.5*(3**2/(2*9.81))" expected="0.688" units="m" atol="0.0005" rtol="1e-9" -->'],
('02-45','5'): ['<!-- VERIFY id="WE-02-45-005-Dh" expr="4*(0.2*0.1)/(2*(0.2+0.1))" expected="0.133" units="m" atol="0.0005" rtol="1e-9" -->'],

('02-46','1'): [
'<!-- VERIFY id="WE-02-46-001-mdot" expr="1000*0.05" expected="50" units="kg/s" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-46-001-dpx" expr="(1000*0.05)*(0-4)" expected="-200" units="N" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-46-001-dpy" expr="(1000*0.05)*(4-0)" expected="200" units="N" atol="1e-9" rtol="1e-9" -->'],
('02-46','2'): ['<!-- VERIFY id="WE-02-46-002-force" expr="1000*0.01*20" expected="200" units="N" atol="1e-9" rtol="1e-9" -->'],
('02-46','3'): ['<!-- VERIFY id="WE-02-46-003-speed" expr="sqrt(2*5000/1000)" expected="3.162" units="m/s" atol="0.0005" rtol="1e-9" -->'],
('02-46','4'): ['<!-- VERIFY id="WE-02-46-004-power" expr="1000*9.81*0.02*30/0.75/1000" expected="7.85" units="kW" atol="0.005" rtol="1e-9" -->'],
('02-46','5'): ['<!-- VERIFY id="WE-02-46-005-flow-ratio" expr="1.10" expected="1.10" units="ratio" atol="1e-9" rtol="1e-9" -->'],

('02-47','3'): ['<!-- VERIFY id="WE-02-47-003-u" expr="500/10" expected="50" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],
('02-47','4'): ['<!-- VERIFY id="WE-02-47-004-h" expr="200+300*0.5" expected="350" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],
('02-47','5'): ['<!-- VERIFY id="WE-02-47-005-wb" expr="500*0.2" expected="100" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],

('02-48','1'): ['<!-- VERIFY id="WE-02-48-001-h" expr="500+0.30*2200" expected="1160" units="kJ/kg" atol="1e-9" rtol="1e-9" -->'],
('02-48','2'): ['<!-- VERIFY id="WE-02-48-002-quality" expr="2/(2+6)" expected="0.25" units="fraction" atol="1e-9" rtol="1e-9" -->'],

('02-49','1'): ['<!-- VERIFY id="WE-02-49-001-pressure" expr="2*0.287*300/1" expected="172.2" units="kPa" atol="0.05" rtol="1e-9" -->'],
('02-49','2'): [
'<!-- VERIFY id="WE-02-49-002-R" expr="1.005-0.718" expected="0.287" units="kJ/kg*K" atol="0.0005" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-49-002-k" expr="1.005/0.718" expected="1.400" units="dimensionless" atol="0.0005" rtol="1e-9" -->'],
('02-49','3'): ['<!-- VERIFY id="WE-02-49-003-du" expr="0.718*50" expected="35.9" units="kJ/kg" atol="0.05" rtol="1e-9" -->'],
('02-49','4'): ['<!-- VERIFY id="WE-02-49-004-M" expr="0.3*28+0.7*44" expected="39.2" units="kg/kmol" atol="0.05" rtol="1e-9" -->'],
('02-49','5'): ['<!-- VERIFY id="WE-02-49-005-omega" expr="0.622*2/(100-2)" expected="0.01269" units="kg/kg dry air" atol="0.000005" rtol="1e-9" -->'],
('02-49','6'): [
'<!-- VERIFY id="WE-02-49-006-rh-frac" expr="2/4" expected="0.50" units="fraction" atol="1e-9" rtol="1e-9" -->',
'<!-- VERIFY id="WE-02-49-006-rh-pct" expr="100*2/4" expected="50" units="percent" atol="1e-9" rtol="1e-9" -->'],
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
