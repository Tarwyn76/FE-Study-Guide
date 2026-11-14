#!/usr/bin/env python3
from pathlib import Path
import re, collections

ROOT=Path(__file__).resolve().parents[1]
LAYERS=["layer-0-orientation","layer-1-substrate","layer-2-core","layer-3-tracks"]

def chapters():
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
    return out

CH=chapters()

def get_title(p,cid):
    txt=p.read_text(encoding="utf-8",errors="ignore")
    m=re.search(r"(?m)^#\s+(.+)$",txt)
    return m.group(1).strip() if m else cid

fp=ROOT/"appendices"/"formula-index.md"
f=fp.read_text(encoding="utf-8")
if "## Layer 0 — Orientation and Exam Strategy" not in f:
    layer0="""## Layer 0 — Orientation and Exam Strategy

### 00-02 — The Exam and the CBT Format

These relations are exam-management arithmetic rather than engineering formulas, but they are retained because the chapter uses them as reusable pacing/checking rules.

- **00-02:F1** — $\\displaystyle \\text{min per question}=\\frac{\\text{working minutes}}{110}$
- **00-02:F2** — $\\displaystyle \\frac{320\\ \\text{min}}{110\\ \\text{questions}}=2.91\\ \\frac{\\text{min}}{\\text{question}}$
- **00-02:F3** — $\\displaystyle \\frac{\\text{correct}}{110}\\times 100=\\text{percent correct}$

### 00-03 — Navigating the FE Reference Book

- **00-03:F1** — $\\displaystyle \\frac{2700\\ \\text{s}}{60}=45.0\\ \\text{min}$
- **00-03:F2** — $\\displaystyle \\text{Total correct}=\\text{initial correct}+\\text{recovered correct}$
- **00-03:F3** — $\\displaystyle \\frac{\\text{total correct}}{110}\\times100=\\text{percent correct}$

"""
    marker="## Layer 1 — Mathematical and Analytical Foundations"
    if marker not in f: raise RuntimeError("Layer 1 marker not found")
    f=f.replace(marker,layer0+marker,1)
    fp.write_text(f,encoding="utf-8")

np=ROOT/"appendices"/"notation-master.md"
n=np.read_text(encoding="utf-8")
section=["## Chapter coverage cross-reference","",
"This table establishes publication-level notation coverage for every canonical chapter. "
"Symbol definitions remain centralized above; a chapter marked local banner contains its own Notation Used Here section, while master only relies on the global contract unless a local ambiguity requires a banner.","",
"| Chapter | Title | Source | Coverage |",
"|---|---|---|---|"]
for cid in sorted(CH):
    p=CH[cid]; txt=p.read_text(encoding="utf-8",errors="ignore"); ttl=get_title(p,cid)
    rel=p.relative_to(ROOT).as_posix()
    local=bool(re.search(r"(?mi)^##\s+Notation Used Here\s*$",txt))
    section.append(f"| {cid} | {ttl.replace('|','/')} | [{rel}](../{rel}) | {'local banner' if local else 'master only'} |")
newsec="\n".join(section)+"\n"
m=re.search(r"(?ms)^## Chapter coverage cross-reference\s*$.*\Z",n)
if m: n=n[:m.start()]+newsec
else: n=n.rstrip()+"\n\n"+newsec
np.write_text(n,encoding="utf-8")

rp=ROOT/"references"/"References-and-Sources-Master-Index.md"
r=rp.read_text(encoding="utf-8")
def register_for(cid):
    if cid.startswith(("00-","01-","02-")):
        return "Core-Curriculum-References-and-Sources-complete.md"
    num=int(cid.split("-")[1])
    if 1<=num<=13: return "Chemical-Track-References-and-Sources-complete.md"
    if 14<=num<=30: return "Civil-Track-References-and-Sources-complete.md"
    if 31<=num<=47: return "ECE-Track-References-and-Sources-complete.md"
    if 48<=num<=61: return "Environmental-Track-References-and-Sources-complete.md"
    if 62<=num<=75: return "Industrial-Systems-Track-References-and-Sources-complete.md"
    if 76<=num<=90: return "Mechanical-Track-References-and-Sources-complete.md"
    if 91<=num<=95: return "Other-Disciplines-Track-References-and-Sources-complete.md"
    raise RuntimeError(f"unmapped chapter {cid}")

explicit=["## Explicit chapter-to-register map","",
"This publication-facing map expands the coverage ranges above so every canonical chapter has an explicit reference-register destination. "
"It is a navigation/index layer; detailed source provenance remains in the named register and meta/ledger.yaml.","",
"| Chapter | Title | Canonical reference register |",
"|---|---|---|"]
for cid in sorted(CH):
    p=CH[cid]; ttl=get_title(p,cid); reg=register_for(cid)
    explicit.append(f"| {cid} | {ttl.replace('|','/')} | [{reg}]({reg}) |")
ex="\n".join(explicit)+"\n"
m=re.search(r"(?ms)^## Explicit chapter-to-register map\s*$.*?(?=^##\s|\Z)",r)
if m: r=r[:m.start()]+ex+r[m.end():]
else:
    pos=r.find("## Source-history files")
    if pos<0: r=r.rstrip()+"\n\n"+ex
    else: r=r[:pos]+ex+"\n"+r[pos:]
r=r.replace("03-31 through 03-46","03-31 through 03-47")
r=r.replace("03-47 through 03-61","03-48 through 03-61")
r=r.replace("01-01 through 02-70","00-01 through 02-70")
rp.write_text(r,encoding="utf-8")

cp=ROOT/"references"/"Civil-Track-References-and-Sources-complete.md"
c=cp.read_text(encoding="utf-8")
c=c.replace("https://doi.org/10.3133/tm4B5","https://pubs.usgs.gov/publication/tm4B5")
cp.write_text(c,encoding="utf-8")

mp=ROOT/"references"/"Mechanical-Track-References-and-Sources-complete.md"
m=mp.read_text(encoding="utf-8")
m=m.replace(
"https://www.asme.org/codes-standards/bpvc-standards/section-viii-rules-construction-pressure-vessels",
"https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-rules-for-construction-of-pressure-vessels-division-1"
)
mp.write_text(m,encoding="utf-8")

print("appendix/reference publication repairs complete")
