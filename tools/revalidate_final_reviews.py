#!/usr/bin/env python3
from __future__ import annotations
import csv
import importlib.util
from pathlib import Path

repo=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("vf", repo/"tools"/"validate_figures_current.py")
vf=importlib.util.module_from_spec(spec)
spec.loader.exec_module(vf)

rows=list(csv.DictReader((repo/"meta"/"figure-current-standards-validation.csv").open(encoding="utf-8-sig")))
targets=[516]
results=[]
for idx in targets:
    svg=next((repo/"figures"/"svg").glob(f"{idx:04d}_*.svg"))
    png=next((repo/"figures"/"png").glob(f"{idx:04d}_*.png"))
    row=vf.validate_one(idx,svg,png)
    results.append(row)
    print(idx,row["status"],row.get("issues",""),row.get("warnings",""))
fail=[r for r in results if r["status"]!="PASS"]
out=repo/"meta"/"figure-final-targeted-revalidation.csv"
with out.open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=["index","figure","status","issues","warnings"])
    w.writeheader(); w.writerows(results)
print(f"TARGETS={len(results)} PASS={len(results)-len(fail)} NONPASS={len(fail)}")
raise SystemExit(1 if fail else 0)

# rerun after final six-figure edge clearance

# verify balanced 0516 repair
