import sys,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
BP=ROOT/"meta"/"tier-review-blueprints.yaml"
EXPECTED={"1A":20,"1B":32,"1C":34,"1D":38,"2A":30,"2B":32,"2C":45,"2D":45,"2E":28,"2F":20}
def main():
    d=yaml.safe_load(BP.read_text(encoding="utf-8")) or {}
    errors=[]
    rows=d.get("review_exams",[])
    if len(rows)!=10: errors.append(f"Expected 10 blueprints, found {len(rows)}")
    for r in rows:
        tier=r.get("tier"); total=r.get("question_count")
        if EXPECTED.get(tier)!=total: errors.append(f"{tier}: total {total}, expected {EXPECTED.get(tier)}")
        if sum(int(x.get("allocated",0)) for x in r.get("chapters",[]))!=total:
            errors.append(f"{tier}: chapter allocation sum mismatch")
    for e in errors: print("  "+e)
    print(f"\n{'PASS' if not errors else 'FAIL'}  {len(rows)} tier blueprints checked, {len(errors)} violations.")
    return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
