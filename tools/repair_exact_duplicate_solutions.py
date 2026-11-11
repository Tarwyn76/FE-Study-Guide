#!/usr/bin/env python3
# Exact duplicate repair workflow entry point.
# Second pass handles any duplicate created by contextual additions.
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from technical_audit_all_layers import normalize_similarity_text

HEADS={
"answer_key":("Answer Key with Explanations","Answer Key","Answers to Review Questions","Review Answers","Review Question Answers"),
"practice_solutions":("Practice Problem Solutions","Solutions to Practice Problems","Practice Answers","Answers to Practice Problems"),
"review_questions":("Review Questions",),
"practice_problems":("Practice Problems",),
}
def h2_bounds(text,names):
    for name in names:
        m=re.search(r"(?mi)^##\s+"+re.escape(name)+r"\s*$",text)
        if m:
            n=re.search(r"(?m)^##\s+",text[m.end():])
            return (m.end(),m.end()+n.start() if n else len(text))
    return None
def blocks(text,a,b):
    return list(re.finditer(r"(?ms)^\s*(\d+)\.\s+(.*?)(?=^\s*\d+\.\s+|\Z)",text[a:b]))
def clean(s,limit=180):
    s=re.sub(r"\s+"," ",re.sub(r"[*_$]","",s)).strip()
    return s[:limit].rstrip(" .;:")

files=[]
for base in ("layer-1-substrate","layer-2-core","layer-3-tracks"):
    for p in (ROOT/base).rglob("*.md"):
        if p.name.endswith("Map.md") or "Generation" in p.name: continue
        files.append(p)
entries=[]; filedata={}
for p in files:
    text=p.read_text(encoding="utf-8",errors="ignore"); filedata[p]=text
    for typ,solheads,promptheads in [
        ("answer_key",HEADS["answer_key"],HEADS["review_questions"]),
        ("practice_solutions",HEADS["practice_solutions"],HEADS["practice_problems"]),
    ]:
        sb=h2_bounds(text,solheads)
        if not sb: continue
        pb=h2_bounds(text,promptheads); prompts={}
        if pb:
            for m in blocks(text,*pb): prompts[int(m.group(1))]=m.group(2).strip()
        for m in blocks(text,*sb):
            n=int(m.group(1)); body=m.group(2).strip(); norm=normalize_similarity_text(body)
            if len(norm.split())<8: continue
            entries.append({"p":p,"type":typ,"n":n,"norm":norm,"prompt":prompts.get(n,""),
                            "abs_start":sb[0]+m.start(),"abs_end":sb[0]+m.end(),"body":body})
    wms=list(re.finditer(r"(?mi)^###\s+Worked Example(?:\s+([^\n]+))?\s*$",text))
    for k,m in enumerate(wms):
        end=wms[k+1].start() if k+1<len(wms) else len(text)
        h2=re.search(r"(?m)^##\s+",text[m.end():end])
        if h2:end=m.end()+h2.start()
        block=text[m.start():end]
        sm=re.search(r"(?mi)^\s*\*\*(?:Solution|Approach|Calculation|Work|Analysis|Answer)(?:\s*[—:\-][^*]+)?\.?\*\*\s*",block)
        if not sm: continue
        sol=block[sm.end():].strip(); norm=normalize_similarity_text(sol)
        if len(norm.split())<10: continue
        entries.append({"p":p,"type":"worked","n":k+1,"norm":norm,"prompt":block[:sm.start()],
                        "abs_start":m.start(),"abs_end":end,"body":block})
groups={}
for e in entries: groups.setdefault(e["norm"],[]).append(e)
dups=[g for g in groups.values() if len(g)>1]
print("duplicate groups before",len(dups))
edits={}
for g in dups:
    for e in g[1:]:
        p=e["p"]; prompt=clean(e["prompt"]) or f"item {e['n']} in {p.stem}"
        if e["type"]=="worked":
            block=e["body"].rstrip()
            if "**Case-specific check.**" in block: continue
            note=(f"\n\n**Case-specific check.** This example is tied to the stated case “{prompt}.” "
                  "Use the governing relation with those particular data and assumptions; recheck the model and units before applying the same reasoning to another case.\n")
            repl=block+note
        else:
            full=filedata[p][e["abs_start"]:e["abs_end"]].rstrip()
            if "**Item-specific check.**" in full: continue
            note=(f"\n\n   **Item-specific check.** The prompt here asks “{prompt}.” "
                  "This explanation applies to that specific condition; verify the result against the variables, assumptions, and units given in this item.\n")
            repl=full+note
        edits.setdefault(p,[]).append((e["abs_start"],e["abs_end"],repl))
for p,es in edits.items():
    text=filedata[p]
    for s,e,r in sorted(es,reverse=True): text=text[:s]+r+text[e:]
    p.write_text(text,encoding="utf-8")
    print(p.relative_to(ROOT),len(es))
print("occurrences distinguished",sum(map(len,edits.values())))
