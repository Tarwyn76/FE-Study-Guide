#!/usr/bin/env python3
from pathlib import Path
import re, yaml, csv, collections, hashlib, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"meta"/"release-readiness"
OUT.mkdir(parents=True,exist_ok=True)
LAYERS=["layer-0-orientation","layer-1-substrate","layer-2-core","layer-3-tracks"]

def canonical_chapters():
    by=collections.defaultdict(list)
    for base in LAYERS:
        d=ROOT/base
        if not d.exists(): continue
        for p in d.rglob("*.md"):
            m=re.match(r"^(\d{2}-\d{2})-",p.name)
            if m: by[m.group(1)].append(p)
    out={}
    for cid,ps in by.items():
        out[cid]=sorted(ps,key=lambda p:(("(inc)" in p.name.lower()),len(str(p)),str(p)))[0]
    return out,by

CH,CH_ALL=canonical_chapters()

def title(text,cid):
    m=re.search(r"(?m)^#\s+(.+)$",text)
    return m.group(1).strip() if m else cid

def anchor(s):
    s=re.sub(r"[^a-z0-9\s-]","",s.lower())
    return re.sub(r"\s+","-",s.strip())

def display_math(text):
    found=[]
    for pat in (r"\$\$(.+?)\$\$",r"\\\[(.+?)\\\]"):
        for m in re.finditer(pat,text,re.S):
            v=re.sub(r"\s+"," ",m.group(1)).strip()
            if v: found.append((m.start(),v))
    return sorted(found)

# Appendix completion: exhaustive formula register + crosswalk.
reg=["# Exhaustive Formula Register","",
"Machine-generated traceability register of every display-math block in the current chapter corpus. "
"The shorter Formula Index remains the learner-facing list of canonical/reusable relations.","",
f"Canonical chapters scanned: {len(CH)}",""]
cross=["# Chapter-to-Appendix Crosswalk","",
"Publication QA navigation map for the canonical chapter corpus.","",
"| Chapter | Title | Display formulas | Formula Index | Formula Register | Notation Master | Unit Tables |",
"|---|---|---:|---|---|---|---|"]
formula_counts={}
for cid in sorted(CH):
    p=CH[cid]; txt=p.read_text(encoding="utf-8",errors="ignore"); ttl=title(txt,cid)
    fm=display_math(txt); formula_counts[cid]=len(fm); rel=p.relative_to(ROOT).as_posix()
    reg += [f"## {cid} — {ttl}","",f"Chapter: [{rel}](../{rel})",""]
    if not fm:
        reg += ["_No display-math blocks detected._",""]
    else:
        for i,(_,formula) in enumerate(fm,1):
            reg.append(f"- **{cid}:D{i}** — " + "$$" + formula + "$$")
        reg.append("")
    cross.append(f"| [{cid}](../{rel}) | {ttl.replace('|','/')} | {len(fm)} | "
                 f"[index](formula-index.md#{anchor(cid+' '+ttl)}) | "
                 f"[register](formula-register.md#{anchor(cid+' '+ttl)}) | "
                 f"[notation](notation-master.md) | [units](unit-tables.md) |")
(ROOT/"appendices"/"formula-register.md").write_text("\n".join(reg)+"\n",encoding="utf-8")
(ROOT/"appendices"/"chapter-appendix-crosswalk.md").write_text("\n".join(cross)+"\n",encoding="utf-8")

fi=(ROOT/"appendices"/"formula-index.md").read_text(encoding="utf-8",errors="ignore")
fi_ids=set(re.findall(r"(?m)^###\s+(\d{2}-\d{2})\b",fi))
formula_index_missing=[cid for cid,n in formula_counts.items() if n and cid not in fi_ids]
nm=(ROOT/"appendices"/"notation-master.md").read_text(encoding="utf-8",errors="ignore")
notation_ids=set(re.findall(r"\b\d{2}-\d{2}\b",nm))
notation_missing=[cid for cid in CH if cid not in notation_ids]
ut=(ROOT/"appendices"/"unit-tables.md").read_text(encoding="utf-8",errors="ignore")
unit_required=["SI Base","Derived","USCS","Conversion","Temperature","Pressure","Energy","Power"]
unit_missing=[x for x in unit_required if x.lower() not in ut.lower()]

# Learner progression: ledger dependencies + route checkpoints.
ledger=yaml.safe_load((ROOT/"meta"/"ledger.yaml").read_text(encoding="utf-8")) or {}
concepts=[x for x in ledger.get("concepts",[]) if isinstance(x,dict) and x.get("id")]
byid={str(x["id"]):x for x in concepts}
rank={cid:i for i,cid in enumerate(sorted(CH))}
deps=[]
for atom in concepts:
    cid=str(atom.get("chapter",""))
    need=[]
    for key in ("requires_concepts","prerequisites","depends_on","requires"):
        v=atom.get(key)
        if isinstance(v,list): need.extend(str(x) for x in v)
        elif isinstance(v,str) and v.strip(): need.append(v.strip())
    for dep in need:
        src=byid.get(dep); dep_ch=str(src.get("chapter","")) if src else ""
        status="OK"
        if not src: status="MISSING_CONCEPT"
        elif cid in rank and dep_ch in rank and rank[dep_ch]>rank[cid]: status="USED_BEFORE_INTRODUCED"
        deps.append((atom["id"],cid,dep,dep_ch,status))
with open(OUT/"progression-dependencies.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh); w.writerow(["concept","chapter","requires","required_chapter","status"]); w.writerows(deps)

route_rows=[]
for disc in ["chemical","civil","electrical-computer","environmental","industrial-systems","mechanical","other-disciplines"]:
    p=ROOT/"routes"/f"route-{disc}.md"; txt=p.read_text(encoding="utf-8",errors="ignore") if p.exists() else ""
    route_rows.append({
      "discipline":disc,"exists":p.exists(),
      "tier_review":bool(re.search(r"tier.*review",txt,re.I)),
      "practice_a":bool(re.search(r"practice\s+(?:exam\s+)?a",txt,re.I)),
      "practice_b":bool(re.search(r"practice\s+(?:exam\s+)?b",txt,re.I)),
      "layer1":"Layer 1" in txt,"layer2":"Layer 2" in txt,"layer3":"Layer 3" in txt
    })
with open(OUT/"route-progression-check.csv","w",newline="",encoding="utf-8") as fh:
    cols=list(route_rows[0]); w=csv.DictWriter(fh,fieldnames=cols); w.writeheader(); w.writerows(route_rows)

# Exam quality: concept/calculation balance, distractors, template density.
def pattern(s):
    s=str(s).lower()
    s=re.sub(r"\$.*?\$"," <math> ",s)
    s=re.sub(r"[-+]?\d+(?:\.\d+)?","<n>",s)
    s=re.sub(r"\s+"," ",s).strip()
    return s
exam_rows=[]; exact=collections.defaultdict(list)
for base in (ROOT/"appendices"/"practice-exams",ROOT/"appendices"/"review-exams"):
    for p in sorted(base.glob("*.yaml")):
        data=yaml.safe_load(p.read_text(encoding="utf-8")) or {}; items=data.get("items",[]) or []
        if not items: continue
        calc=0; mc=0; dup_choices=0; solwords=[]; pats=collections.Counter()
        for it in items:
            pr=str(it.get("prompt","")).strip(); so=str(it.get("solution","")).strip()
            calc+=int(bool(re.search(r"\b(?:calculate|compute|determine|find|evaluate|solve|how many|how much)\b",pr,re.I)))
            choices=it.get("choices")
            if isinstance(choices,list):
                mc+=1; vals=[str(x).strip() for x in choices]
                dup_choices+=int(len(vals)!=len(set(vals)))
            solwords.append(len(re.findall(r"\b\w+\b",so)))
            pats[pattern(pr)]+=1; exact[pr].append((p.name,str(it.get("id",""))))
        repeated=sum(v for v in pats.values() if v>1)
        exam_rows.append({
          "file":p.relative_to(ROOT).as_posix(),"items":len(items),"calculation":calc,
          "conceptual":len(items)-calc,"mc":mc,"duplicate_choices":dup_choices,
          "avg_solution_words":round(sum(solwords)/len(solwords),1),
          "repeated_template_items":repeated,"max_same_template":max(pats.values()),
          "template_density":round(repeated/len(items),3)
        })
with open(OUT/"exam-quality-metrics.csv","w",newline="",encoding="utf-8") as fh:
    cols=list(exam_rows[0]); w=csv.DictWriter(fh,fieldnames=cols); w.writeheader(); w.writerows(exam_rows)
exact_dup={k:v for k,v in exact.items() if k and len(v)>1}

# References: chapter coverage, duplicate files, URL status.
ref_files=sorted((ROOT/"references").glob("*.md")); mapped=set(); urls=[]; hashes=collections.defaultdict(list)
for p in ref_files:
    txt=p.read_text(encoding="utf-8",errors="ignore")
    mapped.update(re.findall(r"\b(?:00|01|02|03)-\d{2}\b",txt))
    urls += [(p.name,u.rstrip(").,;")) for u in re.findall(r"https?://[^\s)>]+",txt)]
    hashes[hashlib.sha256(re.sub(r"\s+"," ",txt).strip().encode()).hexdigest()].append(p.name)
ref_dups=[x for x in hashes.values() if len(x)>1]
unmapped=[cid for cid in CH if cid not in mapped]
def check_url(row):
    fname,u=row
    try:
        req=urllib.request.Request(u,method="HEAD",headers={"User-Agent":"FE-Study-Guide-QA/1.0"})
        with urllib.request.urlopen(req,timeout=6) as resp:
            st="OK" if resp.status<400 else "BAD"; code=str(resp.status)
    except urllib.error.HTTPError as e:
        st="RESTRICTED" if e.code in (403,405,429) else "BAD"; code=str(e.code)
    except Exception as e:
        st="NETWORK_OR_TIMEOUT"; code=type(e).__name__
    return (fname,u,st,code)

with ThreadPoolExecutor(max_workers=24) as pool:
    urlrows=list(pool.map(check_url,urls))
with open(OUT/"reference-url-check.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh); w.writerow(["file","url","status","code"]); w.writerows(urlrows)

prog_bad=[x for x in deps if x[-1]!="OK"]
route_bad=[x for x in route_rows if not all(x[k] for k in ("exists","tier_review","practice_a","practice_b","layer1","layer2","layer3"))]
dense=[x for x in exam_rows if x["template_density"]>=0.30 or x["max_same_template"]>=4 or x["duplicate_choices"]]
hardurls=[x for x in urlrows if x[2]=="BAD"]; softurls=[x for x in urlrows if x[2] in ("RESTRICTED","NETWORK_OR_TIMEOUT")]

report=["# FE Guide — Content Release-Readiness Review","",
"Scope: appendix consolidation, learner progression, exam quality, and reference/publication QA. Image QA intentionally excluded.","",
"## Executive result","",
f"- Canonical chapters: **{len(CH)}**",
f"- Display formulas registered exhaustively: **{sum(formula_counts.values())}**",
f"- Formula-index chapter coverage gaps: **{len(formula_index_missing)}**",
f"- Notation cross-reference gaps: **{len(notation_missing)}**",
f"- Unit-table required-section gaps: **{len(unit_missing)}**",
f"- Concept prerequisite/order findings: **{len(prog_bad)}**",
f"- Route/checkpoint findings: **{len(route_bad)}**",
f"- Exam files quality-scanned: **{len(exam_rows)}**",
f"- Exam files needing template/distractor review: **{len(dense)}**",
f"- Exact duplicate prompts across exam corpus: **{len(exact_dup)}**",
f"- Chapters absent from reference registers: **{len(unmapped)}**",
f"- Broken reference URLs: **{len(hardurls)}**",
f"- Restricted/timeout reference URLs: **{len(softurls)}**","",
"## Appendix coverage","",
"Formula Index gaps: "+(", ".join(formula_index_missing) if formula_index_missing else "None")+".",
"Notation Master gaps: "+(", ".join(notation_missing) if notation_missing else "None")+".",
"Unit Tables section gaps: "+(", ".join(unit_missing) if unit_missing else "None")+".","",
"## Progression","",
f"Dependency issues: **{len(prog_bad)}**. Detailed rows: meta/release-readiness/progression-dependencies.csv.",
f"Route checkpoint issues: **{len(route_bad)}**. Detailed rows: meta/release-readiness/route-progression-check.csv.","",
"## Exam quality","",
"Metrics: meta/release-readiness/exam-quality-metrics.csv.",
f"Files above the template-density/repetition threshold: **{len(dense)}**."]
for r in dense[:40]:
    report.append(f"- {r['file']} — template density {r['template_density']:.1%}; max same template {r['max_same_template']}; duplicate choices {r['duplicate_choices']}.")
report += ["","## Reference/publication QA","",
f"Reference files: **{len(ref_files)}**.",
f"Chapters absent from registers: **{len(unmapped)}**.",
"Unmapped chapter IDs: "+(", ".join(unmapped) if unmapped else "None")+".",
f"Hard-broken URLs: **{len(hardurls)}**; restricted/timeout: **{len(softurls)}**.",
"Hard-broken URL rows: "+("; ".join(f"{x[0]} -> {x[1]} [{x[3]}]" for x in hardurls) if hardurls else "None")+".",
"URL details: meta/release-readiness/reference-url-check.csv.","",
"## Duplicate reference files",""]
report += ["- "+" / ".join(x) for x in ref_dups] if ref_dups else ["- None byte-equivalent after whitespace normalization."]
report += ["","## Publication decision","",
"Hard blockers: prerequisite/order defects, formula-bearing chapters missing from the Formula Index, duplicate answer choices, or hard-broken reference URLs. "
"Template-density findings require editorial judgment because deliberate A/B parallel forms are expected."]
(OUT/"content-release-readiness.md").write_text("\n".join(report)+"\n",encoding="utf-8")
print("\n".join(report[:120]))
