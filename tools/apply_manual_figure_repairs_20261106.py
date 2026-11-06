#!/usr/bin/env python3
from __future__ import annotations

import csv, io, re
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
import numpy as np
from PIL import Image

SVG_NS="http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
Q=lambda t:f"{{{SVG_NS}}}{t}"

TARGETS = {
"0003":"spacing","0006":"center","0007":"center","0008":"align","0009":"crop","0010":"crop",
"0013":"recover","0014":"crop","0015":"flowchart","0017":"crop","0018":"gc-note","0019":"break-lines",
"0021":"crop","0022":"targets","0023":"crop","0024":"crop","0026":"crop","0028":"crop","0029":"crop","0030":"crop",
"0521":"overflow","0579":"overflow-text","0583":"overflow","0614":"overflow-text","0616":"overflow"
}

def text_content(el):
    return "".join(el.itertext())

def figure_group(root):
    return next((e for e in root.iter(Q("g")) if e.get("id")=="figure_1"),None)

def axes(root, aid="axes_1"):
    return next((e for e in root.iter(Q("g")) if e.get("id")==aid),None)

def full_canvas(root):
    fig=figure_group(root)
    if fig is not None:
        p1=next((g for g in list(fig) if g.get("id")=="patch_1"),None)
        if p1 is not None:
            p=next(p1.iter(Q("path")),None)
            if p is not None:
                nums=[float(x) for x in re.findall(r"-?\d+(?:\.\d+)?",p.get("d",""))]
                xs=nums[0::2]; ys=nums[1::2]
                if xs and ys:
                    return max(xs),max(ys)
    vb=[float(x) for x in root.get("viewBox","0 0 720 648").split()]
    return vb[2],vb[3]

def reset_full_view(root, extra=0.06):
    w,h=full_canvas(root); mx=w*extra; my=h*extra
    root.set("viewBox",f"{-mx:.6f} {-my:.6f} {w+2*mx:.6f} {h+2*my:.6f}")
    root.set("width",f"{w+2*mx:.3f}pt"); root.set("height",f"{h+2*my:.3f}pt")
    # Undo prior cleanup-only axes translations. Original Matplotlib axes groups were untransformed.
    for g in root.iter(Q("g")):
        if (g.get("id") or "").startswith("axes_"):
            tr=g.get("transform","")
            if tr.startswith("translate("):
                g.attrib.pop("transform",None)
    return w,h

def render(root,width=1600):
    b=ET.tostring(root,encoding="utf-8",xml_declaration=True)
    png=cairosvg.svg2png(bytestring=b,output_width=width,background_color="#ffffff")
    return Image.open(io.BytesIO(png)).convert("RGB")

def content_bbox(im):
    a=np.asarray(im)
    mask=np.min(a,axis=2)<245
    ys,xs=np.where(mask)
    if len(xs)==0:return None
    return int(xs.min()),int(ys.min()),int(xs.max()+1),int(ys.max()+1)

def tight_crop(root, margin_x=.035, margin_top=.035, margin_bottom=.055):
    vb=[float(x) for x in root.get("viewBox").split()]
    im=render(root,1800); bb=content_bbox(im)
    if not bb:return
    x0,y0,x1,y1=bb; iw,ih=im.size
    px=max(18,int((x1-x0)*margin_x)); pt=max(18,int((y1-y0)*margin_top)); pb=max(28,int((y1-y0)*margin_bottom))
    x0=max(0,x0-px); x1=min(iw,x1+px); y0=max(0,y0-pt); y1=min(ih,y1+pb)
    sx=vb[2]/iw; sy=vb[3]/ih
    nx=vb[0]+x0*sx; ny=vb[1]+y0*sy; nw=(x1-x0)*sx; nh=(y1-y0)*sy
    root.set("viewBox",f"{nx:.6f} {ny:.6f} {nw:.6f} {nh:.6f}")
    root.set("width",f"{nw:.3f}pt"); root.set("height",f"{nh:.3f}pt")

def add_transform(g,t):
    old=g.get("transform","").strip()
    g.set("transform",t+((" "+old) if old else ""))

def compress_0003(root,w,h):
    g=axes(root)
    if g is not None:
        cy=h/2
        add_transform(g,f"translate(0 {cy:.3f}) scale(1 0.84) translate(0 {-cy:.3f})")

def normalize_0015(root):
    # Normalize flowchart box outlines without altering arrows/text.
    for g in root.iter(Q("g")):
        gid=g.get("id") or ""
        if gid.startswith("patch_"):
            for p in g.iter(Q("path")):
                st=p.get("style","")
                if "stroke: #235a78" in st and "fill:" in st:
                    st=re.sub(r"stroke-width:\s*[0-9.]+","stroke-width: 1.2",st)
                    if "stroke-width:" not in st: st += "; stroke-width: 1.2"
                    p.set("style",st)

def explain_0018(root,w,h):
    g=axes(root)
    if g is None:return
    # Existing figure already states the meaning; keep that note visually close to the equations.
    for tg in g.iter(Q("g")):
        if (tg.get("id") or "").startswith("text_") and "bookkeeping factor" in text_content(tg):
            add_transform(tg,"translate(0 -18)")
            break

def break_0019(root):
    g=axes(root)
    if g is None:return
    rx=re.compile(r"M\s+([0-9.]+)\s+139\.5792\s+L\s+\1\s+546\.5556")
    for p in g.iter(Q("path")):
        st=p.get("style","")
        d=p.get("d","")
        m=rx.search(d)
        if m and "stroke: #235a78" in st and "stroke-width: 2" in st:
            x=float(m.group(1))
            p.set("d",f"M {x:.4f} 139.5792 L {x:.4f} 312 "
                      f"M {x-5:.4f} 320 L {x+5:.4f} 330 "
                      f"M {x-5:.4f} 334 L {x+5:.4f} 344 "
                      f"M {x:.4f} 352 L {x:.4f} 546.5556")

def shrink_0022(root):
    centers={"axes_2":(187.2,207.36),"axes_3":(511.2,207.36),"axes_4":(187.2,486.0),"axes_5":(511.2,486.0)}
    for aid,(cx,cy) in centers.items():
        g=axes(root,aid)
        if g is not None:
            add_transform(g,f"translate({cx} {cy}) scale(0.82) translate({-cx} {-cy})")

def condense_long_text(root,factor=.90):
    for t in root.iter(Q("text")):
        raw=text_content(t).strip()
        if len(raw)<55: continue
        st=t.get("style","")
        m=re.search(r"font-size:\s*([0-9.]+)px",st)
        if not m: continue
        old=float(m.group(1)); new=max(8.0,old*factor)
        t.set("style",st[:m.start(1)]+f"{new:.3f}"+st[m.end(1):])

def process(svg_path,png_path,idx,kind):
    root=ET.fromstring(svg_path.read_bytes())
    w,h=reset_full_view(root,0.08 if kind.startswith("overflow") else 0.055)

    if idx=="0003": compress_0003(root,w,h)
    if idx=="0015": normalize_0015(root)
    if idx=="0018": explain_0018(root,w,h)
    if idx=="0019": break_0019(root)
    if idx=="0022": shrink_0022(root)
    if kind.startswith("overflow"): condense_long_text(root,0.88 if kind=="overflow-text" else 0.92)

    tight_crop(root,0.045 if kind.startswith("overflow") else 0.032,
                    0.04,0.065 if kind.startswith("overflow") else 0.05)

    final=ET.tostring(root,encoding="utf-8",xml_declaration=True)
    svg_path.write_bytes(final)
    cairosvg.svg2png(bytestring=final,write_to=str(png_path),output_width=3600,background_color="#ffffff")

    im=Image.open(png_path).convert("RGB")
    bb=content_bbox(im)
    iw,ih=im.size
    if bb:
        left,top,right,bottom=bb
        safe=min(left,top,iw-right,ih-bottom)
        clipped = left<=2 or top<=2 or right>=iw-2 or bottom>=ih-2
    else:
        safe=0; clipped=True
    return {"figure_index":idx,"repair":kind,"clipped":str(clipped).lower(),"min_safe_margin_px":safe,
            "status":"PASS" if not clipped and safe>=12 else "REVIEW"}

def main():
    root=Path(__file__).resolve().parents[1]
    out=[]
    for idx,kind in TARGETS.items():
        svgs=list((root/"figures/svg").glob(f"{idx}_*.svg"))
        pngs=list((root/"figures/png").glob(f"{idx}_*.png"))
        if len(svgs)!=1 or len(pngs)!=1: raise RuntimeError(f"{idx}: expected one SVG and PNG")
        out.append(process(svgs[0],pngs[0],idx,kind))
        print(idx,out[-1])
    report=root/"meta/manual-figure-repair-validation-20261106.csv"
    with report.open("w",newline="",encoding="utf-8-sig") as f:
        wr=csv.DictWriter(f,fieldnames=list(out[0].keys())); wr.writeheader(); wr.writerows(out)
    print("Wrote",report)

if __name__=="__main__":
    main()
