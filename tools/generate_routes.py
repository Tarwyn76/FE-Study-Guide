#!/usr/bin/env python3
from pathlib import Path
import re,yaml
ROOT=Path(__file__).resolve().parents[1]
ROUTES=ROOT/"routes"; ROUTES.mkdir(exist_ok=True)
EXPECTED={
 "chemical":"route-chemical.md","civil":"route-civil.md","electrical-computer":"route-electrical-computer.md",
 "environmental":"route-environmental.md","industrial-systems":"route-industrial-systems.md",
 "mechanical":"route-mechanical.md","other-disciplines":"route-other-disciplines.md"}
ALIASES={
 "chemical":"chemical","civil":"civil",
 "electrical_and_computer":"electrical-computer","electrical-computer":"electrical-computer","electrical":"electrical-computer",
 "environmental":"environmental",
 "industrial_and_systems":"industrial-systems","industrial-systems":"industrial-systems","industrial":"industrial-systems",
 "mechanical":"mechanical",
 "other_disciplines":"other-disciplines","other-disciplines":"other-disciplines","other":"other-disciplines",
}
def fm(p):
    t=p.read_text(encoding="utf-8",errors="ignore")
    if not t.startswith("---"): return {}
    try:return yaml.safe_load(t.split("---",2)[1]) or {}
    except:return {}
chapters=[]
for p in ROOT.rglob("*.md"):
    if any(x in p.parts for x in ("routes","audit-results",".git")): continue
    m=re.match(r"^(\\d{2}-\\d{2})-",p.name)
    if not m: continue
    d=fm(p); ch=str(d.get("chapter") or m.group(1)); title=str(d.get("title") or p.stem)
    rs=d.get("routes") or []
    if isinstance(rs,str): rs=[rs]
    rs={ALIASES.get(str(x),str(x)) for x in rs}
    chapters.append((ch,title,rs,p))
for disc,name in EXPECTED.items():
    rows=sorted((ch,title,p) for ch,title,rs,p in chapters if disc in rs)
    lines=[f"# FE {disc.replace('-',' ').title()} Study Route","",
           "This route is generated from chapter front matter so it stays aligned with the canonical manuscript sequence.","",
           "## Checkpoints","",
           "- Complete each applicable **tier review** before advancing past its covered foundation block.",
           "- Complete **Practice Exam A** after the route content has been studied once.",
           "- Complete **Practice Exam B** as an independent second full-length practice set.","",
           "## Chapter sequence",""]
    last=None
    for ch,title,p in rows:
        layer=ch.split("-")[0]
        if layer!=last:
            label={"00":"Layer 0 — Orientation","01":"Layer 1 — Substrate","02":"Layer 2 — Core","03":"Layer 3 — Track"}.get(layer,f"Layer {layer}")
            lines+=["",f"### {label}",""];last=layer
        rel=p.relative_to(ROOT).as_posix()
        lines.append(f"- **{ch}** — {title} ({rel})")
    lines+=["","## Exam sequence","",
            "- Tier review checkpoints: use the tier-review exams at the end of their corresponding foundation blocks.",
            f"- Practice Exam A: appendices/practice-exams/{disc}-practice-a.yaml",
            f"- Practice Exam B: appendices/practice-exams/{disc}-practice-b.yaml",""]
    (ROUTES/name).write_text("\\n".join(lines),encoding="utf-8")
    print(disc,len(rows),name)
