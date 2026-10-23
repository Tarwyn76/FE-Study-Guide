#!/usr/bin/env python3
"""Technical audit for FE Supplemental Guide exam assets.

Audits:
  * meta/exam-blueprints.yaml
  * meta/tier-review-blueprints.yaml
  * appendices/review-exams/**/*.yaml
  * appendices/practice-exams/**/*.yaml
  * appendices/test-out-quizzes/**/*.yaml (if present)

This intentionally complements, rather than replaces,
technical_audit_all_layers_fixed_v7.py.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, math, re, sys, yaml
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

EXPECTED_TIERS = {
    "1A": [f"01-{i:02d}" for i in range(1,4)],
    "1B": [f"01-{i:02d}" for i in range(4,16)],
    "1C": [f"01-{i:02d}" for i in range(16,28)],
    "1D": [f"01-{i:02d}" for i in range(28,42)],
    "2A": [f"02-{i:02d}" for i in range(1,11)],
    "2B": [f"02-{i:02d}" for i in range(11,22)],
    "2C": [f"02-{i:02d}" for i in range(22,41)],
    "2D": [f"02-{i:02d}" for i in range(41,59)],
    "2E": [f"02-{i:02d}" for i in range(59,66)],
    "2F": [f"02-{i:02d}" for i in range(66,71)],
}
EXPECTED_DISCIPLINES = [
    "chemical", "civil", "electrical-computer", "environmental",
    "industrial-systems", "mechanical", "other-disciplines",
]
TRACK_ALIASES = {
    "chemical": {"chemical"},
    "civil": {"civil"},
    "electrical-computer": {"electrical_and_computer", "electrical-computer", "electrical"},
    "environmental": {"environmental"},
    "industrial-systems": {"industrial_and_systems", "industrial-systems", "industrial"},
    "mechanical": {"mechanical"},
    "other-disciplines": {"other_disciplines", "other-disciplines", "other"},
}
SEVERITY_ORDER={"CRITICAL":0,"ERROR":1,"WARNING":2,"REVIEW":3,"INFO":4}
PLACEHOLDER_RE=re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER|INSERT HERE|VERIFY ME)\b",re.I)
NUM_RE=re.compile(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")
UNIT_RE=re.compile(r"\b(?:m|mm|cm|km|ft|in|s|min|hr|kg|g|lbm|slug|N|lbf|Pa|kPa|MPa|psi|J|kJ|W|kW|MW|A|V|ohm|Ω|F|H|Hz|rad|mol|kmol|K|degC|degF|°C|°F|C|L|mL|m\^2|m\^3|ft\^2|ft\^3)\b")

@dataclass
class Issue:
    severity:str; category:str; file:str=""; exam:str=""; item:str=""; message:str=""; recommendation:str=""; excerpt:str=""


def add(issues,*args,**kwargs): issues.append(Issue(*args,**kwargs))

def norm(s:str)->str:
    s=re.sub(r"```.*?```"," ",str(s),flags=re.S)
    s=re.sub(r"\$+"," ",s)
    s=re.sub(r"\\[A-Za-z]+"," ",s)
    s=re.sub(r"[^a-z0-9]+"," ",s.lower())
    return " ".join(s.split())

def tokens(s:str)->set[str]:
    stop={"the","and","for","with","from","that","this","what","which","when","where","why","how","into","then","than","are","is","was","were","be","to","of","in","on","a","an"}
    return {x for x in norm(s).split() if len(x)>2 and x not in stop}

def jaccard(a:str,b:str)->float:
    A,B=tokens(a),tokens(b)
    return len(A&B)/len(A|B) if A and B else 0.0

def read_yaml(path:Path)->Any:
    try: return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e: return {"__parse_error__":str(e)}

def load_ledger(path:Path):
    data=read_yaml(path)
    if not isinstance(data,dict) or not isinstance(data.get("concepts"),list):
        raise ValueError(f"Invalid ledger: {path}")
    concepts=[c for c in data["concepts"] if isinstance(c,dict) and c.get("id")]
    by_id={c["id"]:c for c in concepts}
    by_ch=defaultdict(list)
    chapter_order=[]; seen=set()
    for c in concepts:
        by_ch[c.get("chapter","")].append(c)
        ch=c.get("chapter","")
        if ch and ch not in seen: chapter_order.append(ch); seen.add(ch)
    pos={ch:i for i,ch in enumerate(chapter_order)}
    return concepts,by_id,by_ch,pos

def exam_label(d:dict,path:Path)->str:
    if d.get("exam_type")=="tier-review": return f"tier-{d.get('tier','?')}"
    if str(d.get("exam_type","")).startswith("practice"):
        form=d.get("exam") or str(d.get("exam_type","")).split("-")[-1].upper()
        return f"{d.get('discipline','?')}-{form}"
    return path.stem

def extract_choices(item:dict)->list[str]:
    c=item.get("choices")
    if isinstance(c,list):
        return [str(x.get("text",x)) if isinstance(x,dict) else str(x) for x in c]
    p=str(item.get("prompt",''))
    # Support both one-choice-per-line and compact forms such as
    # "A) foo  B) bar  C) baz  D) qux" used by some chapter banks.
    matches=list(re.finditer(r"(?:^|\s)([A-D])[\)\.]\s*",p,re.M))
    out=[]
    for i,m in enumerate(matches):
        start=m.end(); end=matches[i+1].start() if i+1<len(matches) else len(p)
        val=p[start:end].strip()
        if val: out.append(val)
    return out

def keyed_answer(item:dict)->str:
    for k in ("answer","correct_answer","keyed_answer"):
        if item.get(k) not in (None,""): return str(item[k]).strip()
    s=str(item.get("solution",''))
    m=re.match(r"\s*\*{0,2}([A-D])\b",s,re.I)
    return m.group(1).upper() if m else ""

def expects_numeric(prompt:str)->bool:
    return bool(re.search(r"\b(?:calculate|compute|determine|find|evaluate|how many|how much|value|magnitude|rate|percent|percentage|probability|distance|time|force|stress|pressure|temperature|power|energy|current|voltage|resistance|flow|velocity|acceleration)\b",prompt,re.I)) and bool(NUM_RE.search(prompt))

def is_dimensionless_prompt(prompt:str)->bool:
    return bool(re.search(r"\b(?:ratio|coefficient|factor|probability|fraction|percent|percentage|efficiency|power factor|reynolds|mach|dimensionless|index)\b",prompt,re.I))

def audit_blueprints(root:Path,issues:list[Issue]):
    pb=root/'meta'/'exam-blueprints.yaml'; tb=root/'meta'/'tier-review-blueprints.yaml'
    practice={}; tiers={}
    if not pb.exists(): add(issues,"CRITICAL","practice_blueprint_missing",str(pb),message="meta/exam-blueprints.yaml is missing.")
    else:
        d=read_yaml(pb)
        if "__parse_error__" in d: add(issues,"CRITICAL","practice_blueprint_parse",str(pb),message=d["__parse_error__"])
        else:
            rows=d.get("blueprints",[]) or []
            if len(rows)!=14: add(issues,"ERROR","practice_blueprint_inventory",str(pb),message=f"Found {len(rows)} practice blueprints; expected 14.")
            for bp in rows:
                disc=str(bp.get("discipline","")); form=str(bp.get("exam","")).upper(); key=(disc,form); practice[key]=bp
                total=sum(int(a.get("allocated",0)) for a in bp.get("areas",[]) or [])
                if total!=110: add(issues,"ERROR","practice_blueprint_total",str(pb),exam=f"{disc}-{form}",message=f"Area allocations total {total}; expected 110.")
                seen=[]
                for area in bp.get("areas",[]) or []:
                    name=area.get("name",""); seen.append(name); lo,hi=area.get("spec_range",[0,999]); val=int(area.get("allocated",0))
                    if not lo<=val<=hi: add(issues,"ERROR","practice_blueprint_range",str(pb),exam=f"{disc}-{form}",message=f"{name}: {val} outside [{lo}, {hi}].")
                if len(seen)!=len(set(seen)): add(issues,"ERROR","practice_blueprint_duplicate_area",str(pb),exam=f"{disc}-{form}",message="Duplicate knowledge-area names in blueprint.")
            expected={(d,f) for d in EXPECTED_DISCIPLINES for f in ('A','B')}
            missing=expected-set(practice)
            for k in sorted(missing): add(issues,"ERROR","practice_blueprint_missing_form",str(pb),exam=f"{k[0]}-{k[1]}",message="Expected practice blueprint is missing.")
    if not tb.exists(): add(issues,"CRITICAL","tier_blueprint_missing",str(tb),message="meta/tier-review-blueprints.yaml is missing.")
    else:
        d=read_yaml(tb)
        if "__parse_error__" in d: add(issues,"CRITICAL","tier_blueprint_parse",str(tb),message=d["__parse_error__"])
        else:
            rows=d.get("review_exams",[]) or []
            if len(rows)!=10: add(issues,"ERROR","tier_blueprint_inventory",str(tb),message=f"Found {len(rows)} tier blueprints; expected 10.")
            for bp in rows:
                tier=str(bp.get("tier","")); tiers[tier]=bp; total=int(bp.get("question_count",0)); alloc=sum(int(x.get("allocated",0)) for x in bp.get("chapters",[]) or [])
                if not 20<=total<=45: add(issues,"ERROR","tier_blueprint_total_range",str(tb),exam=f"tier-{tier}",message=f"question_count {total} outside guide range 20–45.")
                if alloc!=total: add(issues,"ERROR","tier_blueprint_allocation",str(tb),exam=f"tier-{tier}",message=f"Chapter allocations total {alloc}; blueprint total is {total}.")
                got=[x.get("chapter") for x in bp.get("chapters",[]) or []]
                if tier in EXPECTED_TIERS and got!=EXPECTED_TIERS[tier]: add(issues,"ERROR","tier_blueprint_scope",str(tb),exam=f"tier-{tier}",message=f"Chapter scope {got} does not match expected {EXPECTED_TIERS[tier]}.")
            for tier in EXPECTED_TIERS:
                if tier not in tiers: add(issues,"ERROR","tier_blueprint_missing_tier",str(tb),exam=f"tier-{tier}",message="Expected tier blueprint is missing.")
    return practice,tiers

def discover_exams(root:Path):
    pats=[root/'appendices'/'review-exams',root/'appendices'/'practice-exams',root/'appendices'/'test-out-quizzes']
    out=[]
    for p in pats:
        if p.exists(): out += sorted(p.rglob('*.yaml'))
    return out

def audit_exam_file(path:Path,d:dict,by_id:dict,pos:dict,practice_bp:dict,tier_bp:dict,issues:list[Issue]):
    if "__parse_error__" in d:
        add(issues,"CRITICAL","exam_yaml_parse",str(path),message=d["__parse_error__"]); return None
    label=exam_label(d,path); et=str(d.get("exam_type",'')); items=d.get("items",[])
    if not isinstance(items,list): add(issues,"CRITICAL","exam_items_schema",str(path),exam=label,message="items must be a list."); return None
    ids=[]
    for req in ("schema_version","exam_type","items"):
        if req not in d: add(issues,"ERROR","exam_required_field",str(path),exam=label,message=f"Missing required field '{req}'.")
    declared=d.get("question_count")
    if declared is not None and int(declared)!=len(items): add(issues,"ERROR","exam_question_count",str(path),exam=label,message=f"Declared {declared}; found {len(items)} items.")
    if et=='tier-review':
        tier=str(d.get('tier','')); bp=tier_bp.get(tier)
        if not bp: add(issues,"ERROR","tier_exam_no_blueprint",str(path),exam=label,message=f"No blueprint for tier {tier}.")
        elif len(items)!=int(bp.get('question_count',0)): add(issues,"ERROR","tier_exam_blueprint_count",str(path),exam=label,message=f"Found {len(items)} items; blueprint requires {bp.get('question_count')}.")
        counts=Counter(str(i.get('source_chapter','')) for i in items)
        if bp:
            for row in bp.get('chapters',[]) or []:
                ch=str(row.get('chapter')); need=int(row.get('allocated',0)); got=counts[ch]
                if got!=need: add(issues,"ERROR","tier_exam_chapter_allocation",str(path),exam=label,message=f"{ch}: found {got}, blueprint requires {need}.")
    elif et.startswith('practice'):
        disc=str(d.get('discipline','')); form=str(d.get('exam') or et.split('-')[-1]).upper(); bp=practice_bp.get((disc,form))
        if len(items)!=110: add(issues,"ERROR","practice_exam_total",str(path),exam=label,message=f"Found {len(items)} questions; expected 110.")
        if not bp: add(issues,"ERROR","practice_exam_no_blueprint",str(path),exam=label,message=f"No practice blueprint for {disc}-{form}.")
        area_counts=Counter(str(i.get('knowledge_area','')) for i in items)
        if bp:
            expected={str(a.get('name')):int(a.get('allocated',0)) for a in bp.get('areas',[]) or []}
            for name,need in expected.items():
                if area_counts[name]!=need: add(issues,"ERROR","practice_exam_area_allocation",str(path),exam=label,message=f"{name}: found {area_counts[name]}, blueprint requires {need}.")
            extras={k:v for k,v in area_counts.items() if k and k not in expected}
            for k,v in extras.items(): add(issues,"ERROR","practice_exam_unknown_area",str(path),exam=label,message=f"Unknown knowledge area '{k}' on {v} item(s).")
    else:
        if et not in ('test-out',''): add(issues,"WARNING","exam_type_unknown",str(path),exam=label,message=f"Unknown exam_type '{et}'.")

    through=str(d.get('covers_through_chapter','')); tpos=pos.get(through,10**9)
    if through and through not in pos: add(issues,"WARNING","covers_through_unknown",str(path),exam=label,message=f"covers_through_chapter '{through}' not found in ledger chapter order.")
    for idx,item in enumerate(items,1):
        if not isinstance(item,dict): add(issues,"ERROR","item_schema",str(path),exam=label,item=str(idx),message="Item is not a mapping."); continue
        iid=str(item.get('id',''))
        if not iid: add(issues,"ERROR","item_id_missing",str(path),exam=label,item=str(idx),message="Item id missing.")
        elif iid in ids: add(issues,"ERROR","item_id_duplicate",str(path),exam=label,item=iid,message="Duplicate item id within exam.")
        ids.append(iid)
        prompt=str(item.get('prompt','')).strip(); solution=str(item.get('solution','')).strip()
        if not prompt: add(issues,"ERROR","item_prompt_missing",str(path),exam=label,item=iid,message="Prompt is blank.")
        if not solution: add(issues,"ERROR","item_solution_missing",str(path),exam=label,item=iid,message="Solution/explanation is blank.")
        if PLACEHOLDER_RE.search(prompt+' '+solution): add(issues,"ERROR","item_placeholder",str(path),exam=label,item=iid,message="Placeholder/editorial token remains.",excerpt=(prompt+' '+solution)[:240])
        req=item.get('requires_concepts',[]) or []
        if not isinstance(req,list) or not req: add(issues,"ERROR","item_concept_mapping_missing",str(path),exam=label,item=iid,message="requires_concepts must contain at least one ledger concept id.")
        for cid in req if isinstance(req,list) else []:
            c=by_id.get(cid)
            if not c: add(issues,"ERROR","item_unknown_concept",str(path),exam=label,item=iid,message=f"Concept '{cid}' not found in ledger."); continue
            ch=str(c.get('chapter',''))
            if through and ch in pos and pos[ch]>tpos: add(issues,"ERROR","item_beyond_scope",str(path),exam=label,item=iid,message=f"{cid} ({ch}) is beyond covers_through_chapter {through}.")
            if et.startswith('practice'):
                disc=str(d.get('discipline','')); track=c.get('track')
                if track and str(track) not in TRACK_ALIASES.get(disc,{disc}): add(issues,"ERROR","item_wrong_discipline_track",str(path),exam=label,item=iid,message=f"{cid} belongs to track '{track}', not discipline '{disc}'.")
        choices=extract_choices(item)
        ans=keyed_answer(item)
        qtype=str(item.get('question_type') or item.get('source_category') or '').lower()
        looks_mc=len(choices)>=2 or 'multiple' in qtype
        if looks_mc:
            if len(choices)<2: add(issues,"ERROR","mc_choices_missing",str(path),exam=label,item=iid,message="Multiple-choice item has fewer than two parsed choices.")
            if not ans: add(issues,"WARNING","mc_key_missing",str(path),exam=label,item=iid,message="Multiple-choice item has no machine-readable/parseable keyed answer.")
            elif ans.upper() in ('A','B','C','D') and len(choices) < ord(ans.upper())-64: add(issues,"ERROR","mc_key_out_of_range",str(path),exam=label,item=iid,message=f"Key {ans} exceeds available choices.")
        if expects_numeric(prompt) and solution and not NUM_RE.search(solution): add(issues,"WARNING","numeric_solution_no_number",str(path),exam=label,item=iid,message="Prompt appears to request a numeric result but solution contains no numeric token.")
        if expects_numeric(prompt) and UNIT_RE.search(prompt) and solution and not is_dimensionless_prompt(prompt) and not UNIT_RE.search(solution): add(issues,"REVIEW","numeric_solution_units",str(path),exam=label,item=iid,message="Dimensional numeric prompt has no recognized unit in solution.")
        # lightweight delimiter checks
        if prompt.count('$$')%2 or solution.count('$$')%2: add(issues,"ERROR","math_delimiter_unbalanced",str(path),exam=label,item=iid,message="Unbalanced $$ math delimiter.")
    return {"path":path,"data":d,"label":label,"type":et,"items":items}

def duplicate_audit(exams:list[dict],issues:list[Issue]):
    prompt_index=defaultdict(list); solution_index=defaultdict(list)
    tier_prompts=[]; practice_by_disc=defaultdict(lambda:defaultdict(list))
    for ex in exams:
        if not ex: continue
        for it in ex['items']:
            p=norm(it.get('prompt','')); s=norm(it.get('solution','')); key=(ex['label'],str(it.get('id','')),str(ex['path']))
            if len(p.split())>=6: prompt_index[p].append(key)
            if len(s.split())>=10: solution_index[s].append(key)
            if ex['type']=='tier-review': tier_prompts.append((p,key))
            if ex['type'].startswith('practice'):
                disc=str(ex['data'].get('discipline','')); form=str(ex['data'].get('exam') or ex['type'].split('-')[-1]).upper()
                practice_by_disc[disc][form].append((p,key))
    for p,locs in prompt_index.items():
        if len(locs)>1:
            add(issues,"WARNING","duplicate_prompt_exact",exam='; '.join(x[0] for x in locs),item='; '.join(x[1] for x in locs),message=f"Exact normalized prompt occurs {len(locs)} times.",excerpt=p[:240])
    for s,locs in solution_index.items():
        if len(locs)>1:
            add(issues,"REVIEW","duplicate_solution_exact",exam='; '.join(x[0] for x in locs),item='; '.join(x[1] for x in locs),message=f"Exact normalized solution occurs {len(locs)} times.",excerpt=s[:240])
    # Practice A/B near-duplicate gate.
    for disc,forms in practice_by_disc.items():
        A=forms.get('A',[]); B=forms.get('B',[])
        for pa,ka in A:
            if len(pa.split())<8: continue
            best=(0,None)
            for pb,kb in B:
                if len(pb.split())<8: continue
                score=jaccard(pa,pb)
                if score>best[0]: best=(score,kb)
            if best[0]>=0.80:
                add(issues,"WARNING","practice_ab_near_duplicate",exam=f"{disc}-A/B",item=f"{ka[1]} ↔ {best[1][1]}",message=f"A/B prompt similarity Jaccard={best[0]:.2f}; parallel forms should not reuse near-identical questions.")
    # Practice-vs-tier reuse.
    tier_map={p:k for p,k in tier_prompts if p}
    for disc,forms in practice_by_disc.items():
        for form,rows in forms.items():
            for p,k in rows:
                if p in tier_map:
                    tk=tier_map[p]; add(issues,"WARNING","practice_reuses_tier_prompt",exam=f"{disc}-{form}",item=k[1],message=f"Practice prompt exactly reuses tier item {tk[0]} {tk[1]}.")

def write_reports(outdir:Path,issues:list[Issue],exam_rows:list[dict],allow_incomplete:bool):
    outdir.mkdir(parents=True,exist_ok=True)
    stamp=dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    issues_sorted=sorted(issues,key=lambda x:(SEVERITY_ORDER.get(x.severity,9),x.category,x.exam,x.item))
    csvp=outdir/f"Exam-Audit-Issues({stamp}).csv"
    with csvp.open('w',newline='',encoding='utf-8') as f:
        fields=list(asdict(Issue('','','')).keys()); w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); [w.writerow(asdict(i)) for i in issues_sorted]
    inv=outdir/f"Exam-Audit-Inventory({stamp}).csv"
    with inv.open('w',newline='',encoding='utf-8') as f:
        fields=['exam','exam_type','file','items','discipline','tier','covers_through_chapter']; w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); [w.writerow(r) for r in exam_rows]
    counts=Counter(i.severity for i in issues); cats=Counter(i.category for i in issues)
    strict_block=sum(counts[x] for x in ('CRITICAL','ERROR','WARNING'))
    status='PASS' if strict_block==0 else ('PASS WITH INCOMPLETE INVENTORY' if allow_incomplete and all(i.category.startswith('missing_expected_') for i in issues if i.severity in ('CRITICAL','ERROR','WARNING')) else 'FAIL')
    md=outdir/f"Exam-Audit-Summary({stamp}).md"
    lines=["# FE Exam Technical Audit Summary","",f"**Status:** {status}","",f"**Exam files audited:** {len(exam_rows)}",f"**Items audited:** {sum(r['items'] for r in exam_rows)}","", "## Severity counts","", "| Severity | Count |","|---|---:|"]
    for s in ('CRITICAL','ERROR','WARNING','REVIEW','INFO'): lines.append(f"| {s} | {counts[s]} |")
    lines += ["","## Category counts","","| Category | Count |","|---|---:|"]
    for c,n in cats.most_common(): lines.append(f"| {c} | {n} |")
    lines += ["","## Scope","","This audit covers exam blueprints, tier/practice/test-out YAML structure, ledger concept mappings, discipline-track legality, answer/solution completeness, simple numeric/unit heuristics, and duplicate/parallel-form checks. It does not prove that every engineering answer is technically correct; numerical/engineering QA still requires independent review or recomputation."]
    md.write_text('\n'.join(lines),encoding='utf-8')
    return status,md,csvp,inv

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.'); ap.add_argument('--outdir',default='audit-results/exams'); ap.add_argument('--allow-incomplete',action='store_true',help='Do not fail solely because the 14 practice exam files are not authored yet.')
    args=ap.parse_args(); root=Path(args.root).resolve(); issues=[]
    ledger=root/'meta'/'ledger.yaml'
    if not ledger.exists(): print(f"CRITICAL missing {ledger}"); return 2
    concepts,by_id,by_ch,pos=load_ledger(ledger)
    practice_bp,tier_bp=audit_blueprints(root,issues)
    files=discover_exams(root); audited=[]; rows=[]
    seen_tiers=set(); seen_practice=set()
    for p in files:
        d=read_yaml(p); ex=audit_exam_file(p,d,by_id,pos,practice_bp,tier_bp,issues); audited.append(ex)
        if ex:
            if ex['type']=='tier-review': seen_tiers.add(str(ex['data'].get('tier','')))
            if ex['type'].startswith('practice'): seen_practice.add((str(ex['data'].get('discipline','')),str(ex['data'].get('exam') or ex['type'].split('-')[-1]).upper()))
            rows.append({'exam':ex['label'],'exam_type':ex['type'],'file':str(p),'items':len(ex['items']),'discipline':ex['data'].get('discipline',''),'tier':ex['data'].get('tier',''),'covers_through_chapter':ex['data'].get('covers_through_chapter','')})
    for tier in EXPECTED_TIERS:
        if tier not in seen_tiers: add(issues,'ERROR','missing_expected_tier_exam',exam=f'tier-{tier}',message='Expected tier review exam file is missing.')
    expected_practice={(d,f) for d in EXPECTED_DISCIPLINES for f in ('A','B')}
    for d,f in sorted(expected_practice-seen_practice):
        sev='INFO' if args.allow_incomplete else 'ERROR'; add(issues,sev,'missing_expected_practice_exam',exam=f'{d}-{f}',message='Expected full practice exam file is not authored/present.')
    duplicate_audit([x for x in audited if x],issues)
    status,md,csv,inv=write_reports(root/args.outdir,issues,rows,args.allow_incomplete)
    print(f"{status}  {len(rows)} exam files, {sum(r['items'] for r in rows)} items")
    counts=Counter(i.severity for i in issues); print('  '+', '.join(f"{s}={counts[s]}" for s in ('CRITICAL','ERROR','WARNING','REVIEW','INFO')))
    print(md); print(csv); print(inv)
    blockers=counts['CRITICAL']+counts['ERROR']+counts['WARNING']
    return 0 if blockers==0 else 1
if __name__=='__main__': raise SystemExit(main())
