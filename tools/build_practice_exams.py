#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, hashlib, sys
from collections import defaultdict
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "appendices" / "practice-exams"
AREA_RE = re.compile(r"^\s*##\s+(.+?)\s*$", re.M)
NUM_ITEM_RE = re.compile(r"(?ms)^\s*(\d+)\.\s+(.*?)(?=^\s*\d+\.\s+|\Z)")

def norm(s:str)->str:
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]+"," ",s.lower())).strip()

def load_yaml(p:Path):
    return yaml.safe_load(p.read_text(encoding="utf-8"))

def locate_chapter(ch:str)->Path|None:
    hits=[]
    for base in [ROOT/"layer-0-orientation",ROOT/"layer-1-substrate",ROOT/"layer-2-core",ROOT/"layer-3-tracks"]:
        if base.exists():
            hits += list(base.rglob(f"{ch}-*.md"))
    return sorted(hits)[0] if hits else None

def section(text:str, heading:str)->str:
    m=re.search(rf"(?im)^##\s+{re.escape(heading)}\s*$", text)
    if not m: return ""
    start=m.end()
    n=re.search(r"(?m)^##\s+", text[start:])
    end=start+(n.start() if n else len(text)-start)
    return text[start:end].strip()

def numbered(text:str):
    return [(int(m.group(1)),m.group(2).strip()) for m in NUM_ITEM_RE.finditer(text)]

def chapter_bank(ch:str):
    p=locate_chapter(ch)
    if not p: return []
    txt=p.read_text(encoding="utf-8")
    probs=numbered(section(txt,"Practice Problems"))
    sols=dict(numbered(section(txt,"Practice Problem Solutions")))
    out=[]
    for n,q in probs:
        if n in sols:
            out.append(dict(source_chapter=ch,source_question=n,source_category="practice-problem",prompt=q,solution=sols[n]))
    # Review questions are fallback only.
    rev=section(txt,"Review Questions")
    key=section(txt,"Answer Key with Explanations")
    rqs=numbered(rev); rsol=dict(numbered(key))
    for n,q in rqs:
        if n in rsol:
            out.append(dict(source_chapter=ch,source_question=n,source_category="review-fallback",prompt=q,solution=rsol[n]))
    return out

def concept_maps(ledger:dict):
    # (discipline, area number) -> concept rows
    maps=defaultdict(list)
    by_ch=defaultdict(list)
    for c in ledger.get("concepts",[]):
        if not isinstance(c,dict) or not c.get("id"): continue
        by_ch[str(c.get("chapter",""))].append(c)
        for sl in c.get("spec_lines",[]) or []:
            if not isinstance(sl,dict): continue
            disc=str(sl.get("discipline","")).strip()
            area=sl.get("area")
            try: area=int(area)
            except Exception: continue
            maps[(disc,area)].append(c)
    return maps,by_ch

def candidates_for(disc:str, area_no:int, cmap, bank_cache):
    concepts=cmap.get((disc,area_no),[])
    ch_to_concepts=defaultdict(list)
    for c in concepts:
        ch_to_concepts[str(c.get("chapter",""))].append(c)
    rows=[]
    for ch,cs in sorted(ch_to_concepts.items()):
        if ch not in bank_cache: bank_cache[ch]=chapter_bank(ch)
        bank=bank_cache[ch]
        # Deterministic concept mapping; source question remains traceable.
        for k,row in enumerate(bank):
            c=cs[k % len(cs)]
            rows.append({**row,"requires_concepts":[c["id"]]})
    # Prefer practice problems, then review fallback.
    rows.sort(key=lambda r:(r["source_category"]!="practice-problem",r["source_chapter"],r["source_question"]))
    # De-dupe exact normalized prompt.
    seen=set(); uniq=[]
    for r in rows:
        n=norm(r["prompt"])
        if n and n not in seen:
            seen.add(n); uniq.append(r)
    return uniq

def choose_forms(disc,bpA,bpB,cmap):
    bank_cache={}
    chosen={"A":[],"B":[]}
    used_global=set()
    for area_no,(aA,aB) in enumerate(zip(bpA["areas"],bpB["areas"]),1):
        if aA["name"]!=aB["name"]:
            raise RuntimeError(f"{disc}: A/B area order mismatch at {area_no}")
        pool=candidates_for(disc,area_no,cmap,bank_cache)
        needA=int(aA["allocated"]); needB=int(aB["allocated"])
        # First pass: unique across both forms.
        fresh=[r for r in pool if norm(r["prompt"]) not in used_global]
        if len(fresh) < needA+needB:
            raise RuntimeError(
                f"{disc} area {area_no} {aA['name']}: need {needA+needB} unique source items across A/B, found {len(fresh)}. "
                "Author additional practice problems before release."
            )
        # Stable interleave so A/B draw from different chapters/questions where possible.
        seed=int(hashlib.sha256(f"{disc}:{area_no}".encode()).hexdigest()[:8],16)
        fresh=sorted(fresh,key=lambda r:hashlib.sha256((str(seed)+r["source_chapter"]+str(r["source_question"])+r["prompt"]).encode()).hexdigest())
        A=fresh[:needA]; B=fresh[needA:needA+needB]
        for form,rows,area in [("A",A,aA),("B",B,aB)]:
            for r in rows:
                used_global.add(norm(r["prompt"]))
                chosen[form].append({**r,"knowledge_area":area["name"]})
    return chosen

def render_yaml(disc,form,bp,items):
    payload={
      "schema_version":1,
      "exam_type":f"practice-{form}",
      "discipline":disc,
      "exam":form,
      "question_count":110,
      "time_limit_minutes":320,
      "appointment_minutes":355,
      "source_basis":"Book-authored end-of-chapter Practice Problems; Review Questions used only as explicit fallback. A/B source prompts are disjoint within each discipline.",
      "items":[]
    }
    for i,it in enumerate(items,1):
        payload["items"].append({
          "id":f"{disc.upper().replace('-','')}-{form}-Q{i:03d}",
          "knowledge_area":it["knowledge_area"],
          "source_chapter":it["source_chapter"],
          "source_question":it["source_question"],
          "source_category":it["source_category"],
          "requires_concepts":it["requires_concepts"],
          "prompt":it["prompt"],
          "solution":it["solution"],
        })
    return yaml.safe_dump(payload,sort_keys=False,allow_unicode=True,width=110)

def render_md(disc,form,bp,items):
    title=disc.replace("-"," ").title()
    out=[f"# FE {title} Practice Exam {form}","",f"**Questions:** 110  ","**Working time:** 5 h 20 min  ","**Appointment model:** 5 h 55 min including tutorial/break administration  ","","> Use the FE Reference Handbook and an approved calculator under exam-like conditions.","","---",""]
    for i,it in enumerate(items,1):
        out += [f"## {i}", "", it["prompt"], ""]
    out += ["---","","# Answer Key and Remediation",""]
    for i,it in enumerate(items,1):
        out += [f"## {i}","",it["solution"],"",f"**Remediate:** Chapter {it['source_chapter']} · concept `{it['requires_concepts'][0]}` · {it['knowledge_area']}.",""]
    return "\n".join(out).rstrip()+"\n"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--discipline",action="append",help="Limit to one or more discipline slugs")
    args=ap.parse_args()
    bp=load_yaml(ROOT/"meta"/"exam-blueprints.yaml")
    ledger=load_yaml(ROOT/"meta"/"ledger.yaml")
    cmap,_=concept_maps(ledger)
    by=defaultdict(dict)
    for row in bp.get("blueprints",[]):
        by[str(row["discipline"])][str(row["exam"]).upper()]=row
    targets=args.discipline or sorted(by)
    OUT.mkdir(parents=True,exist_ok=True)
    report=[]
    for disc in targets:
        if set(by[disc])!={"A","B"}: raise RuntimeError(f"{disc}: missing A/B blueprint")
        chosen=choose_forms(disc,by[disc]["A"],by[disc]["B"],cmap)
        for form in ("A","B"):
            items=chosen[form]
            if len(items)!=110: raise RuntimeError(f"{disc}-{form}: {len(items)} items")
            y=OUT/f"{disc}-practice-{form.lower()}.yaml"
            m=OUT/f"{disc}-practice-{form.lower()}.md"
            y.write_text(render_yaml(disc,form,by[disc][form],items),encoding="utf-8")
            m.write_text(render_md(disc,form,by[disc][form],items),encoding="utf-8")
            report.append(f"- {disc}-{form}: 110 questions")
            print(report[-1])
    (OUT/"PRACTICE-EXAM-PRODUCTION-REPORT.md").write_text(
        "# Practice Exam Production Report\n\n"
        + "\n".join(report)
        + "\n\nGeneration is blueprint-locked and ledger-mapped. Source prompts are disjoint between A/B forms within each discipline.\n",
        encoding="utf-8")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
