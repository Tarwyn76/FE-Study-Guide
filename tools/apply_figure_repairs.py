#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil

HERE = Path(__file__).resolve().parents[1]

def find_one(root: Path, name: str):
    hits=list(root.rglob(name))
    if not hits: return None
    # Prefer non-backup, shortest path.
    hits.sort(key=lambda p:(len(p.parts),str(p)))
    return hits[0]

def main():
    ap=argparse.ArgumentParser(description='Apply FE figure QA Phase-1 repairs.')
    ap.add_argument('--root',required=True,help='FE Supplemental Guide repository root')
    ap.add_argument('--manifest',help='Optional path to the canonical figure manifest CSV to replace with the repaired manifest')
    args=ap.parse_args(); root=Path(args.root).resolve()
    changes=[]; missing=[]
    # Replace corrected chapter files when matching names exist.
    for src in (HERE/'chapters').glob('*.md'):
        dst=find_one(root,src.name)
        if dst is None:
            missing.append(src.name); continue
        if dst.read_bytes()!=src.read_bytes():
            shutil.copy2(src,dst); changes.append(str(dst))
    # Copy figure aliases/replacements to a figures directory.
    figdirs=[p for p in root.rglob('figures') if p.is_dir()]
    figdir=sorted(figdirs,key=lambda p:(len(p.parts),str(p)))[0] if figdirs else root/'figures'
    figdir.mkdir(parents=True,exist_ok=True)
    for src in (HERE/'figures').iterdir():
        dst=figdir/src.name
        if not dst.exists() or dst.read_bytes()!=src.read_bytes():
            shutil.copy2(src,dst); changes.append(str(dst))
    if args.manifest:
        mdst=Path(args.manifest).resolve()
        msrc=HERE/'manifests'/'figure-manifest-fixed.csv'
        if not mdst.exists() or mdst.read_bytes()!=msrc.read_bytes():
            mdst.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(msrc,mdst); changes.append(str(mdst))
    print(f'updated files: {len(changes)}')
    for p in changes: print('  '+p)
    if missing:
        print('chapter names not found (left unchanged):')
        for n in missing: print('  '+n)

if __name__=='__main__': main()
