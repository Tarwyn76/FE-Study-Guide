from pathlib import Path
import shutil, sys, yaml
if len(sys.argv)!=2:
    raise SystemExit(r'Usage: python apply_verification_batch_02_10_to_02_19.py "C:\path\to\FE-Study-Guide"')
root=Path(sys.argv[1]).resolve(); pkg=Path(__file__).resolve().parent
for source in sorted((pkg/'layer-1-substrate').glob('*.md')):
    matches=list(root.rglob(source.name))
    if len(matches)!=1:
        raise SystemExit(f'Expected exactly one local match for {source.name}; found {len(matches)}: {matches}')
    target=matches[0]; backup=target.with_suffix(target.suffix+'.bak-verify-20261025')
    if not backup.exists(): shutil.copy2(target,backup)
    shutil.copy2(source,target); print(f'Updated chapter: {target}')
tool_source=pkg/'tools'/'verify_examples.py'; tool_target=root/'tools'/'verify_examples.py'; tool_target.parent.mkdir(parents=True,exist_ok=True)
tool_backup=tool_target.with_suffix('.py.bak-verify-20261025')
if tool_target.exists() and not tool_backup.exists(): shutil.copy2(tool_target,tool_backup)
shutil.copy2(tool_source,tool_target); print(f'Updated verifier: {tool_target}')
incoming=yaml.safe_load((pkg/'meta'/'example-verification-exclusions.yaml').read_text(encoding='utf-8')) or {}
dest=root/'meta'/'example-verification-exclusions.yaml'
current=yaml.safe_load(dest.read_text(encoding='utf-8')) if dest.exists() else {'schema_version':1,'exclusions':[]}
current=current or {'schema_version':1,'exclusions':[]}; rows=current.setdefault('exclusions',[])
existing={(str(r.get('chapter')),str(r.get('example'))) for r in rows if isinstance(r,dict)}
for row in incoming.get('exclusions',[]):
    key=(str(row.get('chapter')),str(row.get('example')))
    if key not in existing: rows.append(row); existing.add(key)
dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(yaml.safe_dump(current,sort_keys=False,allow_unicode=True),encoding='utf-8')
print(f'Merged exclusions: {dest}')
