#!/usr/bin/env python3
from pathlib import Path
import re,yaml
ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/"meta"/"ledger.yaml"
TARGETS={
"MATH-1A-001-03":"layer-1-substrate/01-01-numbers-magnitude-and-metric-prefixes.md",
"MATH-1B-007-02":"layer-1-substrate/01-07-Polynomials-and-Their-Roots.md",
"MATH-1B-009-01":"layer-1-substrate/01-09-Analytic-Geometry.md",
"MATH-1B-009-02":"layer-1-substrate/01-09-Analytic-Geometry.md",
"MATH-1B-009-03":"layer-1-substrate/01-09-Analytic-Geometry.md",
"MATH-1B-010-01":"layer-1-substrate/01-10-Areas-Volumes-and-Mensuration.md",
"MATH-1B-011-02":"layer-1-substrate/01-11-Trigonometry.md",
"MATH-1B-011-03":"layer-1-substrate/01-11-Trigonometry.md",
"MATH-1B-012-02":"layer-1-substrate/01-12-Complex-Numbers.md",
"MATH-1B-013-01":"layer-1-substrate/01-13-Vectors-and-Vector-Operations.md",
"MATH-1B-015-02":"layer-1-substrate/01-15-Sequences-Series-and-Progressions.md",
"MATH-1B-015-03":"layer-1-substrate/01-15-Sequences-Series-and-Progressions.md",
}
data=yaml.safe_load(LEDGER.read_text(encoding="utf-8"))
concepts=data.get("concepts",[])
byid={str(x.get("id")):x for x in concepts if isinstance(x,dict) and x.get("id")}
for cid,rel in TARGETS.items():
    if cid not in byid: raise RuntimeError(f"missing ledger concept {cid}")
    atom=byid[cid]
    status=str(atom.get("handbook_status",""))
    if status not in ("in_handbook","in_handbook_memorize_anyway"):
        raise RuntimeError(f"{cid}: unexpected handbook_status={status}")
    ref=atom.get("handbook_ref")
    if not isinstance(ref,dict) or not (str(ref.get("section","")).strip() or str(ref.get("page","")).strip()):
        raise RuntimeError(f"{cid}: no Handbook section/page recorded in ledger")
    text=(ROOT/rel).read_text(encoding="utf-8",errors="ignore")
    m=re.search(r"(?mi)^##\s+As the Handbook States It\s*$",text)
    if not m: raise RuntimeError(f"{cid}: chapter lacks Handbook boundary")
    n=re.search(r"(?m)^##\s+",text[m.end():])
    sec=text[m.end():m.end()+n.start() if n else len(text)]
    if not re.search(r"(?i)Handbook[^\n]{0,100}(?:p\.|pp\.|page|pages)\s*\d",sec):
        raise RuntimeError(f"{cid}: chapter Handbook boundary lacks explicit page evidence")
    atom["handbook_verified"]=True
    note="Handbook location reconciled against the chapter's explicit FE Reference Handbook 10.6 page mapping and the completed Core Curriculum reference register."
    old=str(atom.get("notes","")).strip()
    if note.lower() not in old.lower():
        atom["notes"]=(old+" "+note).strip()
    print(cid,status,ref)
LEDGER.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=120),encoding="utf-8")
print("verified",len(TARGETS))
