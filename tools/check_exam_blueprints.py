# tools/check_exam_blueprints.py
import sys, yaml
from pathlib import Path
BLUEPRINT_PATH = Path(__file__).parent.parent / "meta" / "exam-blueprints.yaml"
REQUIRED_TOTAL = 110
def load_blueprints(path):
    if not path.exists(): return []
    data=yaml.safe_load(path.read_text(encoding="utf-8"))
    return data.get("blueprints",[]) if data else []
def check_blueprint(bp):
    label=f"{bp.get('discipline','unknown')} exam-{bp.get('exam','?')}"
    violations=[]; total=0
    for area in bp.get("areas",[]):
        name=area.get("name","unnamed"); allocated=area.get("allocated",0)
        lo,hi=area.get("spec_range",[0,999]); total+=allocated
        if not lo <= allocated <= hi:
            violations.append(f"  [{label}] '{name}': allocated {allocated} outside range [{lo}, {hi}]")
    if total != REQUIRED_TOTAL:
        violations.append(f"  [{label}] Total questions: {total} (expected {REQUIRED_TOTAL})")
    return violations
def main():
    blueprints=load_blueprints(BLUEPRINT_PATH)
    if not blueprints:
        print("INFO  No exam blueprints found in meta/exam-blueprints.yaml — skipping blueprint check."); return 0
    vs=[]
    for bp in blueprints: vs += check_blueprint(bp)
    for v in vs: print(v)
    print(f"\n{'PASS' if not vs else 'FAIL'}  {len(blueprints)} blueprints checked, {len(vs)} violations.")
    return 0 if not vs else 1
if __name__=="__main__": raise SystemExit(main())
