#!/usr/bin/env python3
"""Master FE release-audit runner.

Default mode is strict release gating. Use --development while practice exams
and route files are still being authored.
"""
from __future__ import annotations
import argparse,subprocess,sys,time
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.'); ap.add_argument('--development',action='store_true'); a=ap.parse_args(); root=Path(a.root).resolve(); tools=root/'tools'
    commands=[
      ('manuscript technical audit',[sys.executable,str(tools/'technical_audit_all_layers_fixed_v7.py'),'--root',str(root)]),
      ('practice blueprint check',[sys.executable,str(tools/'check_exam_blueprints.py')]),
      ('tier blueprint check',[sys.executable,str(tools/'check_tier_review_blueprints.py')]),
      ('item prerequisite check',[sys.executable,str(tools/'check_item_prereqs.py')]),
      ('exam technical audit',[sys.executable,str(tools/'technical_audit_exams.py'),str(root)]+(['--allow-incomplete'] if a.development else [])),
      ('route audit',[sys.executable,str(tools/'audit_routes.py'),str(root)]+(['--allow-incomplete'] if a.development else [])),
    ]
    failures=0
    print(f"FE release audit — {'DEVELOPMENT' if a.development else 'STRICT RELEASE'} mode\n")
    for label,cmd in commands:
        if not Path(cmd[1]).exists():
            print(f"SKIP  {label}: missing {cmd[1]}")
            if not a.development: failures+=1
            continue
        print(f"\n=== {label} ===")
        p=subprocess.run(cmd,cwd=root)
        if p.returncode!=0: failures+=1
    print(f"\n{'PASS' if failures==0 else 'FAIL'}  master release audit: {failures} failing/missing check(s).")
    return 0 if failures==0 else 1
if __name__=='__main__': raise SystemExit(main())
