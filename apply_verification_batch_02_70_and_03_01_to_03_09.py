#!/usr/bin/env python3
from __future__ import annotations
import argparse,re
from pathlib import Path

WORKED=re.compile(r'(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')
CORRECTIONS={}
TAGS={
('02-70','1'): ['<!-- VERIFY id="WE-02-70-001-uP" expr="4*2" expected="8" units="output units" atol="1e-9" rtol="1e-9" -->'],
('02-70','2'): ['<!-- VERIFY id="WE-02-70-002-uI" expr="0.5*3*4" expected="6" units="output units" atol="1e-9" rtol="1e-9" -->'],
('02-70','3'): ['<!-- VERIFY id="WE-02-70-003-uD" expr="2*(-0.5)" expected="-1" units="output units" atol="1e-9" rtol="1e-9" -->'],
('02-70','5'): ['<!-- VERIFY id="WE-02-70-005-Ts" expr="4/(0.4*5)" expected="2.0" units="s" atol="0.005" rtol="1e-9" -->'],

('03-01','1'): ['<!-- VERIFY id="WE-03-01-001-A" expr="100*0.30" expected="30" units="kmol/h" atol="1e-9" rtol="1e-9" -->','<!-- VERIFY id="WE-03-01-001-B" expr="100*0.70" expected="70" units="kmol/h" atol="1e-9" rtol="1e-9" -->'],
('03-01','2'): ['<!-- VERIFY id="WE-03-01-002-P2" expr="120-75" expected="45" units="kg/h" atol="1e-9" rtol="1e-9" -->'],
('03-01','4'): ['<!-- VERIFY id="WE-03-01-004-solute1" expr="100*0.40*0.20" expected="8" units="kg/h" atol="1e-9" rtol="1e-9" -->','<!-- VERIFY id="WE-03-01-004-solute2" expr="100*0.60*0.20" expected="12" units="kg/h" atol="1e-9" rtol="1e-9" -->'],
('03-01','6'): ['<!-- VERIFY id="WE-03-01-006-Q" expr="2*4*20" expected="160" units="kW" atol="1e-9" rtol="1e-9" -->'],
('03-01','9'): ['<!-- VERIFY id="WE-03-01-009-dT" expr="500/(10*2.5)" expected="20" units="K" atol="1e-9" rtol="1e-9" -->'],

('03-02','1'): ['<!-- VERIFY id="WE-03-02-001-R" expr="50/100" expected="0.50" units="dimensionless" atol="0.0005" rtol="1e-9" -->'],
('03-02','2'): ['<!-- VERIFY id="WE-03-02-002-X" expr="100*(100-10)/100" expected="90" units="percent" atol="0.05" rtol="1e-9" -->'],
('03-02','3'): ['<!-- VERIFY id="WE-03-02-003-bypass" expr="100*0.30" expected="30" units="kg/h" atol="1e-9" rtol="1e-9" -->','<!-- VERIFY id="WE-03-02-003-processed" expr="100*(1-0.30)" expected="70" units="kg/h" atol="1e-9" rtol="1e-9" -->'],
('03-02','4'): ['<!-- VERIFY id="WE-03-02-004-purge" expr="2/0.10" expected="20" units="kmol/h" atol="1e-9" rtol="1e-9" -->'],
('03-02','5'): ['<!-- VERIFY id="WE-03-02-005-accum" expr="5-3" expected="2" units="kg/min" atol="1e-9" rtol="1e-9" -->'],
('03-02','6'): ['<!-- VERIFY id="WE-03-02-006-tau" expr="100/10" expected="10" units="min" atol="1e-9" rtol="1e-9" -->'],
('03-02','9'): ['<!-- VERIFY id="WE-03-02-009-C" expr="2*(1-exp(-5/5))" expected="1.264" units="mol/L" atol="0.0005" rtol="1e-9" -->'],

('03-03','1'): ['<!-- VERIFY id="WE-03-03-001-A" expr="10-3" expected="7" units="mol" atol="1e-9" rtol="1e-9" -->','<!-- VERIFY id="WE-03-03-001-B" expr="2*3" expected="6" units="mol" atol="1e-9" rtol="1e-9" -->'],
('03-03','2'): ['<!-- VERIFY id="WE-03-03-002-X" expr="100*(100-25)/100" expected="75" units="percent" atol="0.05" rtol="1e-9" -->'],
('03-03','4'): ['<!-- VERIFY id="WE-03-03-004-O2" expr="2*(1+0.20)" expected="2.4" units="mol O2/mol CH4" atol="0.005" rtol="1e-9" -->','<!-- VERIFY id="WE-03-03-004-N2" expr="2.4*3.76" expected="9.024" units="mol N2/mol CH4" atol="0.0005" rtol="1e-9" -->'],
('03-03','5'): ['<!-- VERIFY id="WE-03-03-005-dHr" expr="-100" expected="-100" units="kJ/mol reaction" atol="1e-9" rtol="1e-9" -->'],
('03-03','6'): ['<!-- VERIFY id="WE-03-03-006-dHr398" expr="-100+0.020*(398-298)" expected="-98" units="kJ/mol" atol="0.005" rtol="1e-9" -->'],
('03-03','8'): ['<!-- VERIFY id="WE-03-03-008-selectivity" expr="80/20" expected="4" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('03-03','9'): ['<!-- VERIFY id="WE-03-03-009-excess" expr="100*(20.64-17.2)/17.2" expected="20" units="percent" atol="0.05" rtol="1e-9" -->'],

('03-04','2'): ['<!-- VERIFY id="WE-03-04-002-p" expr="500*0.002" expected="1.0" units="kPa" atol="0.005" rtol="1e-9" -->'],
('03-04','8'): ['<!-- VERIFY id="WE-03-04-008-K" expr="0.6/0.3" expected="2" units="dimensionless" atol="1e-9" rtol="1e-9" -->'],
('03-04','9'): ['<!-- VERIFY id="WE-03-04-009-sum" expr="0.5/2+0.5/0.5" expected="1.25" units="dimensionless" atol="0.005" rtol="1e-9" -->'],

('03-05','1'): ['<!-- VERIFY id="WE-03-05-001-J" expr="-1e-9*(-2e6)" expected="0.002" units="mol/(m2*s)" atol="0.0000005" rtol="1e-9" -->'],
('03-05','2'): ['<!-- VERIFY id="WE-03-05-002-L" expr="sqrt(1e-10*10000)" expected="0.001" units="m" atol="0.0000005" rtol="1e-9" -->'],
('03-05','4'): ['<!-- VERIFY id="WE-03-05-004-NA" expr="2e-5*10000/(8.314*300*0.01)" expected="0.00802" units="mol/(m2*s)" atol="0.000005" rtol="1e-9" -->'],
('03-05','5'): ['<!-- VERIFY id="WE-03-05-005-NA" expr="0.10*2" expected="0.20" units="mol/(m2*s)" atol="0.005" rtol="1e-9" -->'],
('03-05','7'): ['<!-- VERIFY id="WE-03-05-007-Sh" expr="0.02*0.05/1e-5" expected="100" units="dimensionless" atol="0.05" rtol="1e-9" -->'],

('03-06','1'): ['<!-- VERIFY id="WE-03-06-001-L" expr="100-40" expected="60" units="kmol/h" atol="1e-9" rtol="1e-9" -->'],
('03-06','2'): ['<!-- VERIFY id="WE-03-06-002-xA" expr="(100*0.5-40*0.8)/(100-40)" expected="0.30" units="mole fraction" atol="0.005" rtol="1e-9" -->'],
('03-06','3'): ['<!-- VERIFY id="WE-03-06-003-B" expr="100-40" expected="60" units="kmol/h" atol="1e-9" rtol="1e-9" -->'],
('03-06','7'): ['<!-- VERIFY id="WE-03-06-007-EMV" expr="(0.70-0.50)/(0.80-0.50)" expected="0.667" units="dimensionless" atol="0.0005" rtol="1e-9" -->'],
('03-06','8'): ['<!-- VERIFY id="WE-03-06-008-D" expr="100*(0.5-0.1)/(0.9-0.1)" expected="50" units="kmol/h" atol="0.05" rtol="1e-9" -->','<!-- VERIFY id="WE-03-06-008-B" expr="100-50" expected="50" units="kmol/h" atol="0.05" rtol="1e-9" -->'],

('03-07','1'): ['<!-- VERIFY id="WE-03-07-001-Z" expr="5*0.8" expected="4.0" units="m" atol="0.005" rtol="1e-9" -->'],
('03-07','3'): ['<!-- VERIFY id="WE-03-07-003-raffinate" expr="10-7" expected="3" units="mol" atol="1e-9" rtol="1e-9" -->'],
('03-07','4'): ['<!-- VERIFY id="WE-03-07-004-adsorbed" expr="1*(100-20)" expected="80" units="mg" atol="0.05" rtol="1e-9" -->'],
('03-07','5'): ['<!-- VERIFY id="WE-03-07-005-flux" expr="2e-6*50" expected="1e-4" units="mol/(m2*s)" atol="0.0000005" rtol="1e-9" -->'],

('03-08','1'): ['<!-- VERIFY id="WE-03-08-001-omega" expr="0.622*2/(100-2)" expected="0.01269" units="kg/kg dry air" atol="0.000005" rtol="1e-9" -->'],
('03-08','2'): ['<!-- VERIFY id="WE-03-08-002-water" expr="5*0.005" expected="0.025" units="kg/s" atol="0.0005" rtol="1e-9" -->'],
('03-08','3'): ['<!-- VERIFY id="WE-03-08-003-Xwb" expr="2/(2+8)" expected="0.20" units="dimensionless" atol="0.005" rtol="1e-9" -->','<!-- VERIFY id="WE-03-08-003-Xdb" expr="2/8" expected="0.25" units="dimensionless" atol="0.005" rtol="1e-9" -->'],
('03-08','4'): ['<!-- VERIFY id="WE-03-08-004-rate" expr="0.5*10" expected="5" units="kg/h" atol="0.05" rtol="1e-9" -->','<!-- VERIFY id="WE-03-08-004-time" expr="25/(0.5*10)" expected="5" units="h" atol="0.05" rtol="1e-9" -->'],
('03-08','6'): ['<!-- VERIFY id="WE-03-08-006-product" expr="1000*0.10/0.40" expected="250" units="kg/h" atol="0.5" rtol="1e-9" -->','<!-- VERIFY id="WE-03-08-006-vapor" expr="1000-250" expected="750" units="kg/h" atol="0.5" rtol="1e-9" -->'],
('03-08','8'): ['<!-- VERIFY id="WE-03-08-008-water" expr="2*(0.03-0.01)" expected="0.04" units="kg/s" atol="0.005" rtol="1e-9" -->'],
('03-08','9'): ['<!-- VERIFY id="WE-03-08-009-solids" expr="500*0.20" expected="100" units="kg/h" atol="0.5" rtol="1e-9" -->','<!-- VERIFY id="WE-03-08-009-product" expr="100/0.50" expected="200" units="kg/h" atol="0.5" rtol="1e-9" -->','<!-- VERIFY id="WE-03-08-009-evap" expr="500-200" expected="300" units="kg/h" atol="0.5" rtol="1e-9" -->'],

('03-09','3'): ['<!-- VERIFY id="WE-03-09-003-x" expr="30/200" expected="0.15" units="mass fraction" atol="0.005" rtol="1e-9" -->'],
('03-09','4'): ['<!-- VERIFY id="WE-03-09-004-RR" expr="20/2" expected="10" units="dimensionless" atol="0.05" rtol="1e-9" -->'],
('03-09','6'): ['<!-- VERIFY id="WE-03-09-006-theta" expr="degrees(atan(1.0/2.0))" expected="26.6" units="deg" atol="0.05" rtol="1e-9" -->'],
('03-09','7'): ['<!-- VERIFY id="WE-03-09-007-crystals" expr="100-30" expected="70" units="kg" atol="0.5" rtol="1e-9" -->'],
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
