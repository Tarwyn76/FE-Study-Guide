#!/usr/bin/env python3
"""Audit the seven reader-facing route markdown files against chapter front matter."""
from __future__ import annotations
import argparse,re,sys,yaml,csv,datetime as dt
from collections import Counter
from pathlib import Path
EXPECTED={
 "chemical":"route-chemical.md","civil":"route-civil.md","electrical-computer":"route-electrical-computer.md",
 "environmental":"route-environmental.md","industrial-systems":"route-industrial-systems.md",
 "mechanical":"route-mechanical.md","other-disciplines":"route-other-disciplines.md"}
CH_RE=re.compile(r"\b(?:00|01|02|03)-\d{2}\b")

def fm(path):
    t=path.read_text(encoding='utf-8',errors='ignore')
    if not t.startswith('---'): return {},t
    parts=t.split('---',2)
    try: return yaml.safe_load(parts[1]) or {},parts[2]
    except Exception: return {},t

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.'); ap.add_argument('--allow-incomplete',action='store_true'); ap.add_argument('--outdir',default='audit-results/routes'); a=ap.parse_args(); root=Path(a.root).resolve()
    issues=[]; routes=root/'routes'; route_docs={}
    for disc,name in EXPECTED.items():
        p=routes/name
        if not p.exists(): issues.append(('INFO' if a.allow_incomplete else 'ERROR','route_missing',disc,name,'Expected route file is missing.')); continue
        txt=p.read_text(encoding='utf-8',errors='ignore'); route_docs[disc]=(p,txt,set(CH_RE.findall(txt)))
        for token in ('Practice Exam A','Practice Exam B','tier review'):
            if token.lower() not in txt.lower(): issues.append(('WARNING','route_checkpoint_missing',disc,name,f"Route does not mention {token}."))
    # Discover chapter markdown anywhere except generated/audit dirs.
    chapter_routes={}
    for p in root.rglob('*.md'):
        if any(x in p.parts for x in ('routes','audit-results','.git')): continue
        m=re.match(r'^(\d{2}-\d{2})-',p.name)
        if not m: continue
        meta,_=fm(p); ch=str(meta.get('chapter') or m.group(1)); rs=meta.get('routes') or []
        if isinstance(rs,str): rs=[rs]
        chapter_routes[ch]=set(map(str,rs))
    for disc,(p,txt,listed) in route_docs.items():
        expected={ch for ch,rs in chapter_routes.items() if disc in rs}
        missing=sorted(expected-listed); extras=sorted(ch for ch in listed if ch in chapter_routes and disc not in chapter_routes[ch])
        for ch in missing: issues.append(('ERROR','route_required_chapter_missing',disc,p.name,f"{ch} front matter includes this route but route file does not list it."))
        for ch in extras: issues.append(('REVIEW','route_offroute_chapter_listed',disc,p.name,f"{ch} is listed but its front matter does not include this route; confirm it is intentionally optional."))
    out=root/a.outdir; out.mkdir(parents=True,exist_ok=True); stamp=dt.datetime.now().strftime('%Y%m%d-%H%M%S'); cp=out/f'Route-Audit-Issues({stamp}).csv'; mp=out/f'Route-Audit-Summary({stamp}).md'
    with cp.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['severity','category','discipline','file','message']); w.writerows(issues)
    c=Counter(x[0] for x in issues); cats=Counter(x[1] for x in issues); blockers=c['ERROR']+c['WARNING']
    lines=['# FE Route Audit Summary','',f"**Route files present:** {len(route_docs)}/7",'', '## Severity counts','', '| Severity | Count |','|---|---:|']+[f'| {s} | {c[s]} |' for s in ('ERROR','WARNING','REVIEW','INFO')]+['','## Category counts','', '| Category | Count |','|---|---:|']+[f'| {k} | {v} |' for k,v in cats.most_common()]
    mp.write_text('\n'.join(lines),encoding='utf-8'); print(f"{'PASS' if blockers==0 else 'FAIL'}  {len(route_docs)}/7 route files present; ERROR={c['ERROR']} WARNING={c['WARNING']} REVIEW={c['REVIEW']} INFO={c['INFO']}"); print(mp); print(cp); return 0 if blockers==0 else 1
if __name__=='__main__': raise SystemExit(main())
