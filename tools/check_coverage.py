"""Validate NCEES specification coverage recorded in meta/ledger.yaml."""

from collections import Counter
from pathlib import Path
import sys
import yaml

LEDGER_PATH = Path(__file__).parent.parent / "meta" / "ledger.yaml"

def load_ledger(path: Path) -> tuple[list[dict], dict]:
    with path.open(encoding="utf-8") as source:
        raw = yaml.safe_load(source)
    if not isinstance(raw, dict) or not isinstance(raw.get("concepts"), list):
        raise ValueError("Ledger must contain a top-level 'concepts' list.")
    return raw["concepts"], raw

def main() -> None:
    concepts, ledger = load_ledger(LEDGER_PATH)
    lines = [
        (str(item.get("discipline", "")), str(item.get("area", "")), str(item.get("item", "")))
        for concept in concepts for item in (concept.get("spec_lines") or [])
    ]
    duplicates = [line for line, count in Counter(lines).items() if count > 1]
    unmapped = [c["id"] for c in concepts if c.get("layer") == 1 and not c.get("spec_lines")]
    print(f"Loaded {len(concepts)} concepts from ledger.")
    print(f"Mapped {len(set(lines))} unique specification lines.")
    if duplicates:
        print("WARNING  Specification lines claimed by multiple atoms:")
        for discipline, area, item in sorted(duplicates):
            print(f"  {discipline} / {area} / {item}")
    if unmapped and (ledger.get("_todo") or {}).get("spec_lines_layer_1"):
        print(f"INCOMPLETE  {len(unmapped)} Layer 1 atoms still have no spec_lines; tracked in ledger _todo.")
        sys.exit(2)
    if unmapped:
        print(f"FAIL  {len(unmapped)} Layer 1 atoms have no spec_lines and no _todo acknowledgement.")
        sys.exit(1)
    print("PASS  Every Layer 1 atom has at least one specification mapping.")

if __name__ == "__main__":
    main()
