from pathlib import Path
import shutil
import sys
import yaml

if len(sys.argv) != 2:
    raise SystemExit(
        r'Usage: python apply_verification_batch_01_01_to_01_05.py '
        r'"C:\Users\knigh\OneDrive\Documents\GitHub\FE-Study-Guide"'
    )

root = Path(sys.argv[1]).resolve()
pkg = Path(__file__).resolve().parent

chapter_dir = pkg / "layer-1-substrate"
for source in sorted(chapter_dir.glob("*.md")):
    matches = list(root.rglob(source.name))
    if len(matches) != 1:
        raise SystemExit(
            f"Expected exactly one local match for {source.name}; found {len(matches)}: {matches}"
        )
    target = matches[0]
    backup = target.with_suffix(target.suffix + ".bak-verify-20261023")
    if not backup.exists():
        shutil.copy2(target, backup)
    shutil.copy2(source, target)
    print(f"Updated chapter: {target}")
    print(f"Backup:          {backup}")

# Replace verifier, preserving a backup.
tool_source = pkg / "tools" / "verify_examples.py"
tool_target = root / "tools" / "verify_examples.py"
tool_backup = tool_target.with_suffix(".py.bak-verify-20261023")
if tool_target.exists() and not tool_backup.exists():
    shutil.copy2(tool_target, tool_backup)
shutil.copy2(tool_source, tool_target)
print(f"Updated verifier: {tool_target}")

# Merge curated exclusions rather than overwriting an existing file.
incoming_path = pkg / "meta" / "example-verification-exclusions.yaml"
incoming = yaml.safe_load(incoming_path.read_text(encoding="utf-8")) or {}
incoming_rows = incoming.get("exclusions", [])

dest = root / "meta" / "example-verification-exclusions.yaml"
if dest.exists():
    current = yaml.safe_load(dest.read_text(encoding="utf-8")) or {}
else:
    current = {"schema_version": 1, "exclusions": []}

rows = current.setdefault("exclusions", [])
existing = {(str(r.get("chapter")), str(r.get("example"))) for r in rows if isinstance(r, dict)}

for row in incoming_rows:
    key = (str(row.get("chapter")), str(row.get("example")))
    if key not in existing:
        rows.append(row)
        existing.add(key)

dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(
    yaml.safe_dump(current, sort_keys=False, allow_unicode=True),
    encoding="utf-8"
)
print(f"Merged exclusions: {dest}")
