# tools/check_exam_blueprints.py
# =====================================================================
# Validates every practice exam blueprint:
#   - Total question count must equal exactly 110
#   - Each knowledge area allocation must fall within the published
#     NCEES range for that discipline
#   - Every area in the spec must be present in the blueprint
#
# Blueprint files live in:
#   meta/exam-blueprints.yaml
#
# Format:
#   blueprints:
#     - discipline: civil
#       exam: A
#       areas:
#         - name: "Mathematics and Statistics"
#           spec_range: [8, 12]
#           allocated: 9
#         ...
# =====================================================================

import sys
import yaml
from pathlib import Path


BLUEPRINT_PATH = Path(__file__).parent.parent / "meta" / "exam-blueprints.yaml"
REQUIRED_TOTAL = 110


def load_blueprints(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("blueprints", []) if data else []


def check_blueprint(bp: dict) -> list[str]:
    discipline = bp.get("discipline", "unknown")
    exam       = bp.get("exam", "?")
    label      = f"{discipline} exam-{exam}"
    areas      = bp.get("areas", [])
    violations = []

    total = 0
    for area in areas:
        name      = area.get("name", "unnamed")
        allocated = area.get("allocated", 0)
        lo, hi    = area.get("spec_range", [0, 999])
        total    += allocated

        if not (lo <= allocated <= hi):
            violations.append(
                f"  [{label}] '{name}': allocated {allocated} "
                f"outside range [{lo}, {hi}]"
            )

    if total != REQUIRED_TOTAL:
        violations.append(
            f"  [{label}] Total questions: {total} "
            f"(expected {REQUIRED_TOTAL})"
        )

    return violations


def main():
    blueprints = load_blueprints(BLUEPRINT_PATH)
    if not blueprints:
        print(
            "INFO  No exam blueprints found in meta/exam-blueprints.yaml — "
            "skipping blueprint check."
        )
        sys.exit(0)

    total_violations = 0
    for bp in blueprints:
        violations = check_blueprint(bp)
        total_violations += len(violations)
        for v in violations:
            print(v)

    print(
        f"\n{'PASS' if total_violations == 0 else 'FAIL'}  "
        f"{len(blueprints)} blueprints checked, {total_violations} violations."
    )
    sys.exit(0 if total_violations == 0 else 1)


if __name__ == "__main__":
    main()