from pathlib import Path
import re, shutil, sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'source'
DST = ROOT / 'layer-1-substrate'

TAGS = {
 '03-76-mechanism-kinematics-and-machine-motion.md': {
  '1': ['<!-- VERIFY id="WE-03-76-001-speed" expr="10*0.20" expected="2.0" units="m/s" atol="1e-12" rtol="1e-12" -->'],
  '2': ['<!-- VERIFY id="WE-03-76-002-speed" expr="4*0.30" expected="1.2" units="m/s" atol="1e-12" rtol="1e-12" -->'],
  '5': ['<!-- VERIFY id="WE-03-76-005-rpm" expr="-(20/60)*1200" expected="-400" units="rpm" atol="1e-9" rtol="1e-12" -->'],
  '6': ['<!-- VERIFY id="WE-03-76-006-reduction" expr="3*3" expected="9" units="dimensionless" atol="1e-12" rtol="1e-12" -->'],
 },
 '03-77-mechanical-vibrations-free-forced-damped-and-resonant-response.md': {
  '1': [
   '<!-- VERIFY id="WE-03-77-001-omega" expr="sqrt(400/4)" expected="10" units="rad/s" atol="1e-12" rtol="1e-12" -->',
   '<!-- VERIFY id="WE-03-77-001-freq" expr="sqrt(400/4)/(2*pi)" expected="1.59" units="Hz" atol="0.005" rtol="1e-12" -->',
  ],
  '2': ['<!-- VERIFY id="WE-03-77-002-damped-ratio" expr="sqrt(1-0.2**2)" expected="0.980" units="dimensionless" atol="0.0005" rtol="1e-12" -->'],
  '3': ['<!-- VERIFY id="WE-03-77-003-decrement" expr="ln(10/8)" expected="0.223" units="dimensionless" atol="0.0005" rtol="1e-12" -->'],
  '4': ['<!-- VERIFY id="WE-03-77-004-ratio" expr="10/10" expected="1.00" units="dimensionless" atol="1e-12" rtol="1e-12" -->'],
 },
 '03-78-failure-theories-stress-concentrations-fatigue-fracture-and-creep.md': {
  '1': ['<!-- VERIFY id="WE-03-78-001-local-stress" expr="2.0*80" expected="160" units="MPa" atol="1e-9" rtol="1e-12" -->'],
  '4': [
   '<!-- VERIFY id="WE-03-78-004-amplitude" expr="(100-20)/2" expected="40" units="MPa" atol="1e-9" rtol="1e-12" -->',
   '<!-- VERIFY id="WE-03-78-004-mean" expr="(100+20)/2" expected="60" units="MPa" atol="1e-9" rtol="1e-12" -->',
  ],
 },
 '03-81-compressible-flow-mach-number-nozzles-isentropic-flow-and-normal-shocks.md': {
  '1': ['<!-- VERIFY id="WE-03-81-001-mach" expr="340/340" expected="1.00" units="dimensionless" atol="1e-12" rtol="1e-12" -->'],
 },
 '03-84-mechanical-springs.md': {
  '2': ['<!-- VERIFY id="WE-03-84-002-rate-ratio" expr="1/2" expected="0.5" units="dimensionless" atol="1e-12" rtol="1e-12" -->'],
 },
 '03-88-shafts-keys-couplings-gears-belts-chains-and-power-transmission.md': {
  '4': ['<!-- VERIFY id="WE-03-88-004-pitch-diameter" expr="2*40" expected="80" units="mm" atol="1e-9" rtol="1e-12" -->'],
  '7': [
   '<!-- VERIFY id="WE-03-88-007-speed-ratio" expr="2/6" expected="0.3333333333333333" units="dimensionless" atol="1e-12" rtol="1e-12" -->',
   '<!-- VERIFY id="WE-03-88-007-reduction" expr="6/2" expected="3" units="dimensionless" atol="1e-12" rtol="1e-12" -->',
  ],
 },
 '03-90-fits-tolerances-gdandt-manufacturability-quality-and-reliability.md': {
  '1': ['<!-- VERIFY id="WE-03-90-001-size-tolerance" expr="20.021-20.000" expected="0.021" units="mm" atol="1e-12" rtol="1e-12" -->'],
  '6': ['<!-- VERIFY id="WE-03-90-006-stack" expr="0.10+0.10+0.10" expected="0.30" units="mm" atol="1e-12" rtol="1e-12" -->'],
 },
}

HEAD = re.compile(r'(?m)^###\s+Worked Example(?:\s+([^\n]+))?\s*$')

def insert_tags(text, mapping, filename):
    matches=list(HEAD.finditer(text))
    # Process from end so positions stay valid.
    for idx in range(len(matches)-1, -1, -1):
        m=matches[idx]
        label=(m.group(1) or str(idx+1)).strip()
        if label not in mapping:
            continue
        end=matches[idx+1].start() if idx+1<len(matches) else len(text)
        block=text[m.start():end]
        if '<!-- VERIFY' in block:
            continue
        # Put tags after the Solution paragraph and before the first thematic separator/next section.
        rel = block.find('\n---', block.find('**Solution.**'))
        if rel < 0:
            # fallback: before end of block
            rel=len(block)
        insert_pos=m.start()+rel
        tag_text='\n\n'+'\n'.join(mapping[label])+'\n'
        text=text[:insert_pos]+tag_text+text[insert_pos:]
    return text

def main():
    DST.mkdir(parents=True, exist_ok=True)
    # copy all source chapters, whether tagged or purely conceptual
    for p in sorted(SRC.glob('*.md')):
        txt=p.read_text(encoding='utf-8')
        txt=insert_tags(txt, TAGS.get(p.name, {}), p.name)
        (DST/p.name).write_text(txt, encoding='utf-8')
    print(f'Wrote {len(list(DST.glob("*.md")))} verified chapter copies to {DST}')

if __name__=='__main__': main()
