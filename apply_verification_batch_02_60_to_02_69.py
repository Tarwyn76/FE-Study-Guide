#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

WORKED = re.compile(r'(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')

CORRECTIONS = {}

TAGS = {
('02-60', '1'): ['<!-- VERIFY id="WE-02-60-001-Req" expr="4+6+10" expected="20" units="ohm" atol="1e-09" rtol="1e-9" -->'],
('02-60', '2'): ['<!-- VERIFY id="WE-02-60-002-Req" expr="1/(1/6+1/3)" expected="2" units="ohm" atol="1e-09" rtol="1e-9" -->'],
('02-60', '3'): ['<!-- VERIFY id="WE-02-60-003-I" expr="5-2" expected="3" units="A" atol="1e-09" rtol="1e-9" -->'],
('02-60', '4'): ['<!-- VERIFY id="WE-02-60-004-I" expr="12/(2+4)" expected="2" units="A" atol="1e-09" rtol="1e-9" -->'],
('02-60', '5'): ['<!-- VERIFY id="WE-02-60-005-Vout" expr="12*4/(2+4)" expected="8" units="V" atol="1e-09" rtol="1e-9" -->'],
('02-60', '6'): ['<!-- VERIFY id="WE-02-60-006-V" expr="12*6/(3+6)" expected="8" units="V" atol="1e-09" rtol="1e-9" -->'],
('02-60', '7'): ['<!-- VERIFY id="WE-02-60-007-RL" expr="5" expected="5" units="ohm" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-60-007-Pmax" expr="10**2/(4*5)" expected="5" units="W" atol="1e-09" rtol="1e-9" -->'],
('02-60', '8'): ['<!-- VERIFY id="WE-02-60-008-Vth" expr="2*4" expected="8" units="V" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-60-008-Rth" expr="4" expected="4" units="ohm" atol="1e-09" rtol="1e-9" -->'],
('02-61', '1'): ['<!-- VERIFY id="WE-02-61-001-q" expr="10e-6*12*1e6" expected="120" units="uC" atol="1e-09" rtol="1e-9" -->'],
('02-61', '2'): ['<!-- VERIFY id="WE-02-61-002-W" expr="0.5*100e-6*20**2" expected="0.02" units="J" atol="5e-07" rtol="1e-9" -->'],
('02-61', '3'): ['<!-- VERIFY id="WE-02-61-003-Ceq" expr="6*3/(6+3)" expected="2" units="uF" atol="1e-09" rtol="1e-9" -->'],
('02-61', '4'): ['<!-- VERIFY id="WE-02-61-004-v" expr="0.50*4" expected="2" units="V" atol="1e-09" rtol="1e-9" -->'],
('02-61', '5'): ['<!-- VERIFY id="WE-02-61-005-W" expr="0.5*2*3**2" expected="9" units="J" atol="1e-09" rtol="1e-9" -->'],
('02-61', '6'): ['<!-- VERIFY id="WE-02-61-006-tau" expr="20e3*50e-6" expected="1" units="s" atol="0.0005" rtol="1e-9" -->'],
('02-61', '7'): ['<!-- VERIFY id="WE-02-61-007-tau" expr="2/10" expected="0.2" units="s" atol="0.0005" rtol="1e-9" -->'],
('02-61', '8'): ['<!-- VERIFY id="WE-02-61-008-v" expr="10*(1-exp(-2/2))" expected="6.32" units="V" atol="0.005" rtol="1e-9" -->'],
('02-61', '9'): ['<!-- VERIFY id="WE-02-61-009-i" expr="5*exp(-1/0.5)" expected="0.677" units="A" atol="0.0005" rtol="1e-9" -->'],
('02-62', '1'): ['<!-- VERIFY id="WE-02-62-001-T" expr="1000/60" expected="16.67" units="ms" atol="0.005" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-62-001-omega" expr="2*pi*60" expected="377" units="rad/s" atol="0.5" rtol="1e-9" -->'],
('02-62', '2'): ['<!-- VERIFY id="WE-02-62-002-Vrms" expr="170/sqrt(2)" expected="120.2" units="V" atol="0.05" rtol="1e-9" -->'],
('02-62', '3'): ['<!-- VERIFY id="WE-02-62-003-real" expr="10*cos(radians(30))" expected="8.66" units="" atol="0.005" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-62-003-imag" expr="10*sin(radians(30))" expected="5" units="" atol="0.005" rtol="1e-9" -->'],
('02-62', '4'): ['<!-- VERIFY id="WE-02-62-004-XL" expr="2*pi*60*0.10" expected="37.7" units="ohm" atol="0.05" rtol="1e-9" -->'],
('02-62', '5'): ['<!-- VERIFY id="WE-02-62-005-XC" expr="1/(2*pi*60*100e-6)" expected="26.5" units="ohm" atol="0.05" rtol="1e-9" -->'],
('02-62', '6'): ['<!-- VERIFY id="WE-02-62-006-f0" expr="1/(2*pi*sqrt(0.10*100e-6))" expected="50.3" units="Hz" atol="0.05" rtol="1e-9" -->'],
('02-62', '8'): ['<!-- VERIFY id="WE-02-62-008-Zmag" expr="sqrt(10**2+10**2)" expected="14.14" units="ohm" atol="0.005" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-62-008-theta" expr="degrees(atan(10/10))" expected="45" units="deg" atol="0.05" rtol="1e-9" -->'],
('02-62', '9'): ['<!-- VERIFY id="WE-02-62-009-Imag" expr="120/30" expected="4" units="A" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-62-009-Iangle" expr="0-(-20)" expected="20" units="deg" atol="0.05" rtol="1e-9" -->'],
('02-63', '1'): ['<!-- VERIFY id="WE-02-63-001-S" expr="120*10" expected="1200" units="VA" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-63-001-P" expr="120*10*0.8" expected="960" units="W" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-63-001-Q" expr="120*10*sqrt(1-0.8**2)" expected="720" units="var" atol="1e-09" rtol="1e-9" -->'],
('02-63', '2'): ['<!-- VERIFY id="WE-02-63-002-S" expr="5/0.60" expected="8.33" units="kVA" atol="0.005" rtol="1e-9" -->'],
('02-63', '3'): ['<!-- VERIFY id="WE-02-63-003-Qc" expr="10*(tan(acos(0.70))-tan(acos(0.95)))" expected="6.92" units="kVAR" atol="0.005" rtol="1e-9" -->'],
('02-63', '5'): ['<!-- VERIFY id="WE-02-63-005-VL" expr="sqrt(3)*277" expected="479.8" units="V" atol="0.05" rtol="1e-9" -->'],
('02-63', '6'): ['<!-- VERIFY id="WE-02-63-006-IL" expr="sqrt(3)*20" expected="34.64" units="A" atol="0.005" rtol="1e-9" -->'],
('02-63', '7'): ['<!-- VERIFY id="WE-02-63-007-P" expr="sqrt(3)*480*30*0.90/1000" expected="22.45" units="kW" atol="0.005" rtol="1e-9" -->'],
('02-63', '8'): ['<!-- VERIFY id="WE-02-63-008-S" expr="sqrt(3)*208*15/1000" expected="5.4" units="kVA" atol="0.005" rtol="1e-9" -->'],
('02-63', '9'): ['<!-- VERIFY id="WE-02-63-009-Zreal" expr="12/3" expected="4" units="ohm" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-63-009-Zimag" expr="6/3" expected="2" units="ohm" atol="1e-09" rtol="1e-9" -->'],
('02-64', '1'): ['<!-- VERIFY id="WE-02-64-001-B" expr="2.0e-3*500" expected="1" units="T" atol="0.0005" rtol="1e-9" -->'],
('02-64', '2'): ['<!-- VERIFY id="WE-02-64-002-F" expr="10*0.50*0.8" expected="4" units="N" atol="1e-09" rtol="1e-9" -->'],
('02-64', '3'): ['<!-- VERIFY id="WE-02-64-003-v" expr="200*abs((3e-3-1e-3)/0.01)" expected="40" units="V" atol="1e-09" rtol="1e-9" -->'],
('02-64', '4'): ['<!-- VERIFY id="WE-02-64-004-Rmag" expr="0.20/(1.0e-3*4e-4)" expected="500000" units="H^-1" atol="0.5" rtol="1e-9" -->'],
('02-64', '5'): ['<!-- VERIFY id="WE-02-64-005-a" expr="1000/250" expected="4" units="dimensionless" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-64-005-Vs" expr="480/(1000/250)" expected="120" units="V" atol="1e-09" rtol="1e-9" -->'],
('02-64', '6'): ['<!-- VERIFY id="WE-02-64-006-Zp" expr="(1000/250)**2*12" expected="192" units="ohm" atol="1e-09" rtol="1e-9" -->'],
('02-64', '8'): ['<!-- VERIFY id="WE-02-64-008-Ip" expr="10/5" expected="2" units="A" atol="1e-09" rtol="1e-9" -->'],
('02-65', '1'): ['<!-- VERIFY id="WE-02-65-001-eff" expr="100*8.5/10" expected="85" units="percent" atol="0.05" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-65-001-loss" expr="10-8.5" expected="1.5" units="kW" atol="0.005" rtol="1e-9" -->'],
('02-65', '2'): ['<!-- VERIFY id="WE-02-65-002-omega" expr="2*pi*1800/60" expected="188.5" units="rad/s" atol="0.05" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-65-002-P" expr="20*(2*pi*1800/60)/1000" expected="3.77" units="kW" atol="0.005" rtol="1e-9" -->'],
('02-65', '3'): ['<!-- VERIFY id="WE-02-65-003-ns" expr="120*60/4" expected="1800" units="rpm" atol="1e-09" rtol="1e-9" -->'],
('02-65', '4'): ['<!-- VERIFY id="WE-02-65-004-P" expr="3*(240*230/2)*sin(radians(20))/1000" expected="28.3" units="kW" atol="0.05" rtol="1e-9" -->'],
('02-65', '5'): ['<!-- VERIFY id="WE-02-65-005-slip" expr="100*(1800-1746)/1800" expected="3" units="percent" atol="0.05" rtol="1e-9" -->'],
('02-65', '6'): ['<!-- VERIFY id="WE-02-65-006-I" expr="(24-0.20*100)/1" expected="4" units="A" atol="1e-09" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-65-006-T" expr="0.20*((24-0.20*100)/1)" expected="0.8" units="N*m" atol="0.0005" rtol="1e-9" -->'],
('02-65', '7'): ['<!-- VERIFY id="WE-02-65-007-Pout" expr="5*0.90" expected="4.5" units="kW" atol="0.005" rtol="1e-9" -->'],
('02-65', '8'): ['<!-- VERIFY id="WE-02-65-008-ns" expr="120*50/6" expected="1000" units="rpm" atol="1e-09" rtol="1e-9" -->'],
('02-65', '9'): ['<!-- VERIFY id="WE-02-65-009-slip" expr="100*(1000-970)/1000" expected="3" units="percent" atol="0.05" rtol="1e-9" -->'],
('02-66', '1'): ['<!-- VERIFY id="WE-02-66-001-S" expr="(5-1)/(200-0)" expected="0.02" units="V/kPa" atol="0.0005" rtol="1e-9" -->'],
('02-66', '2'): ['<!-- VERIFY id="WE-02-66-002-error" expr="100.80-100.00" expected="0.8" units="degC" atol="0.005" rtol="1e-9" -->'],
('02-66', '4'): ['<!-- VERIFY id="WE-02-66-004-wR" expr="sqrt((5*0.2)**2+(10*0.1)**2)" expected="1.414" units="units" atol="0.0005" rtol="1e-9" -->'],
('02-66', '8'): ['<!-- VERIFY id="WE-02-66-008-resolution" expr="10/4096*1000" expected="2.441" units="mV" atol="0.0005" rtol="1e-9" -->'],
('02-66', '9'): ['<!-- VERIFY id="WE-02-66-009-u" expr="0.4/2" expected="0.2" units="kPa" atol="0.0005" rtol="1e-9" -->'],
('02-67', '1'): ['<!-- VERIFY id="WE-02-67-001-R" expr="100*(1+0.00385*100)" expected="138.5" units="ohm" atol="0.05" rtol="1e-9" -->'],
('02-67', '2'): ['<!-- VERIFY id="WE-02-67-002-R" expr="10000*exp(3950*(1/323.15-1/298.15))/1000" expected="3.59" units="kohm" atol="0.005" rtol="1e-9" -->'],
('02-67', '3'): ['<!-- VERIFY id="WE-02-67-003-V" expr="41e-6*100*1000" expected="4.1" units="mV" atol="0.005" rtol="1e-9" -->'],
('02-67', '4'): ['<!-- VERIFY id="WE-02-67-004-dR_R" expr="2.0*500e-6" expected="0.001" units="dimensionless" atol="5e-07" rtol="1e-9" -->'],
('02-67', '5'): ['<!-- VERIFY id="WE-02-67-005-Vo" expr="(0.001/4)*5*1000" expected="1.25" units="mV" atol="0.005" rtol="1e-9" -->'],
('02-67', '8'): ['<!-- VERIFY id="WE-02-67-008-Pg" expr="250-100" expected="150" units="kPa" atol="1e-09" rtol="1e-9" -->'],
('02-67', '9'): ['<!-- VERIFY id="WE-02-67-009-E" expr="0-59*(5-7)" expected="118" units="mV" atol="1e-09" rtol="1e-9" -->'],
('02-68', '1'): ['<!-- VERIFY id="WE-02-68-001-fs" expr="1/0.002" expected="500" units="Hz" atol="1e-09" rtol="1e-9" -->'],
('02-68', '3'): ['<!-- VERIFY id="WE-02-68-003-alias" expr="abs(900-1000)" expected="100" units="Hz" atol="1e-09" rtol="1e-9" -->'],
('02-68', '4'): ['<!-- VERIFY id="WE-02-68-004-resolution" expr="10/4096*1000" expected="2.441" units="mV/count" atol="0.0005" rtol="1e-9" -->'],
('02-68', '5'): ['<!-- VERIFY id="WE-02-68-005-V" expr="-5+3000*(10/4096)" expected="2.324" units="V" atol="0.0005" rtol="1e-9" -->'],
('02-68', '6'): ['<!-- VERIFY id="WE-02-68-006-y" expr="2*(1-exp(-3/3))" expected="1.264" units="dimensionless" atol="0.0005" rtol="1e-9" -->'],
('02-68', '7'): ['<!-- VERIFY id="WE-02-68-007-Ts" expr="4/(0.5*8)" expected="1" units="s" atol="0.0005" rtol="1e-9" -->'],
('02-69', '2'): ['<!-- VERIFY id="WE-02-69-002-Y" expr="4*3" expected="12" units="dimensionless" atol="1e-09" rtol="1e-9" -->'],
('02-69', '4'): ['<!-- VERIFY id="WE-02-69-004-YR" expr="(2*5)/(1+2*5*1)" expected="0.909" units="dimensionless" atol="0.0005" rtol="1e-9" -->', '<!-- VERIFY id="WE-02-69-004-YL" expr="5/(1+2*5*1)" expected="0.455" units="dimensionless" atol="0.0005" rtol="1e-9" -->'],
('02-69', '6'): ['<!-- VERIFY id="WE-02-69-006-G0" expr="5/(2*0+1)" expected="5" units="dimensionless" atol="1e-09" rtol="1e-9" -->'],
('02-69', '7'): ['<!-- VERIFY id="WE-02-69-007-GM" expr="-20*log10(0.25)" expected="12.04" units="dB" atol="0.005" rtol="1e-9" -->'],
('02-69', '8'): ['<!-- VERIFY id="WE-02-69-008-PM" expr="180-135" expected="45" units="deg" atol="0.05" rtol="1e-9" -->'],
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
