#!/usr/bin/env python3
from pathlib import Path
import yaml, json

ROOT=Path(__file__).resolve().parents[1]
TARGETS={
"CHEM-A-Q016","CHEM-A-Q082","CHEM-B-Q020","CHEM-B-Q032","CHEM-B-Q043",
"CIV-A-Q021","CIV-A-Q023","CIV-A-Q027","CIV-A-Q079","CIV-B-Q022","CIV-B-Q024","CIV-B-Q028",
"ECE-A-Q061","ECE-B-Q061","ENV-A-Q029","ENV-A-Q035","ENV-A-Q104","ENV-B-Q005","ENV-B-Q009","ENV-B-Q031",
"IND-A-Q009","IND-A-Q055","IND-A-Q063","IND-B-Q011","IND-B-Q058",
"MEC-B-Q002","MEC-B-Q003","MEC-B-Q005","MEC-B-Q006","MEC-B-Q020",
"T1B-Q006","T1C-Q028","T1D-Q003","T1D-Q025",
"IND-A-Q017","IND-B-Q025","IND-A-Q029","IND-B-Q033","IND-A-Q046","IND-B-Q049",
"IND-A-Q065","IND-B-Q067","IND-A-Q090","IND-B-Q085","IND-A-Q091","IND-B-Q086","IND-A-Q105","IND-B-Q107",
"MEC-A-Q023","MEC-B-Q024","MEC-A-Q064","MEC-B-Q059","MEC-A-Q068","MEC-B-Q069","MEC-A-Q101","MEC-B-Q109",
"OTH-A-Q044","OTH-B-Q051","OTH-A-Q050","OTH-B-Q045","OTH-A-Q083","OTH-B-Q089","OTH-A-Q089","OTH-B-Q083",
"T2A-Q008","T2A-Q013"
}
found={}
for base in (ROOT/"appendices"/"practice-exams",ROOT/"appendices"/"review-exams"):
    for p in sorted(base.glob("*.yaml")):
        d=yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for item in d.get("items",[]) or []:
            iid=str(item.get("id",""))
            if iid in TARGETS:
                found[iid]={
                    "file":str(p.relative_to(ROOT)),
                    "exam_type":d.get("exam_type"),
                    "discipline":d.get("discipline"),
                    "tier":d.get("tier"),
                    "prompt":item.get("prompt"),
                    "choices":item.get("choices"),
                    "answer":item.get("answer"),
                    "solution":item.get("solution"),
                }
for iid in sorted(TARGETS):
    print(json.dumps({"id":iid,**found.get(iid,{"missing":True})},ensure_ascii=False))
print("FOUND",len(found),"TARGETS",len(TARGETS))
