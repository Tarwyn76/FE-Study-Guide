import sys,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
LEDGER=ROOT/"meta"/"ledger.yaml"
GLOB="appendices/review-exams/**/*.yaml"
def main():
    raw=yaml.safe_load(LEDGER.read_text(encoding="utf-8"))
    concepts=[x for x in raw["concepts"] if isinstance(x,dict) and "id" in x]
    seen=[]; ss=set()
    for c in concepts:
        ch=c.get("chapter","")
        if ch and ch not in ss: seen.append(ch); ss.add(ch)
    pos={ch:i for i,ch in enumerate(seen)}
    cid_ch={c["id"]:c.get("chapter","") for c in concepts}
    errors=[]; files=0; items=0
    for p in sorted(ROOT.glob(GLOB)):
        d=yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        files+=1
        through=d.get("covers_through_chapter","")
        tpos=pos.get(through,9999)
        for item in d.get("items",[]):
            items+=1
            for cid in item.get("requires_concepts",[]):
                ch=cid_ch.get(cid)
                if ch is None: errors.append(f"{p.name} {item.get('id')}: unknown concept {cid}"); continue
                if pos.get(ch,9999)>tpos:
                    errors.append(f"{p.name} {item.get('id')}: {cid} ({ch}) beyond {through}")
    for e in errors: print("  "+e)
    print(f"\n{'PASS' if not errors else 'FAIL'}  {files} tier exam files, {items} items, {len(errors)} prerequisite violations.")
    return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
