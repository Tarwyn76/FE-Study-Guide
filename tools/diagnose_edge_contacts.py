#!/usr/bin/env python3
from __future__ import annotations

import copy
import csv
import io
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg
import numpy as np
from PIL import Image

SVG_NS = "http://www.w3.org/2000/svg"
Q = lambda tag: f"{{{SVG_NS}}}{tag}"
KEEP = {Q("svg"), Q("g"), Q("text"), Q("tspan"), Q("defs"), Q("style")}

def render(data: bytes, width=1200):
    png = cairosvg.svg2png(bytestring=data, output_width=width, background_color="#ffffff")
    return Image.open(io.BytesIO(png)).convert("RGB")

def bbox(im):
    a=np.asarray(im)
    m=np.min(a,axis=2)<245
    ys,xs=np.where(m)
    if len(xs)==0:
        return None
    return int(xs.min()),int(ys.min()),int(xs.max()+1),int(ys.max()+1)

def strip_to_text(el):
    for child in list(el):
        if child.tag not in KEEP:
            el.remove(child)
        else:
            strip_to_text(child)

def main():
    root=Path(__file__).resolve().parents[1]
    csv_path=root/"meta"/"figure-current-standards-validation.csv"
    rows=list(csv.DictReader(csv_path.open(encoding="utf-8-sig")))
    review=[r for r in rows if r["status"]=="REVIEW"]
    out=[]
    for r in review:
        idx=int(r["index"])
        svg=next((root/"figures"/"svg").glob(f"{idx:04d}_*.svg"))
        tree=ET.fromstring(svg.read_bytes())
        clone=copy.deepcopy(tree)
        strip_to_text(clone)
        data=ET.tostring(clone,encoding="utf-8",xml_declaration=True)
        im=render(data)
        bb=bbox(im)
        sides=(r.get("warnings") or "").replace("edge_contact:","").split("+")
        text_sides=[]
        margins={}
        if bb:
            x0,y0,x1,y1=bb
            iw,ih=im.size
            margins={"left":x0/iw,"right":(iw-x1)/iw,"top":y0/ih,"bottom":(ih-y1)/ih}
            text_sides=[s for s in sides if s in margins and margins[s] < 0.002]
        classification="TEXT_EDGE" if text_sides else "GEOMETRY_EDGE"
        out.append({
            "index":idx,
            "figure":r["figure"],
            "reported_edge":"+".join(sides),
            "classification":classification,
            "text_edge_sides":"+".join(text_sides),
            "text_left_pct":round(margins.get("left",1)*100,3),
            "text_right_pct":round(margins.get("right",1)*100,3),
            "text_top_pct":round(margins.get("top",1)*100,3),
            "text_bottom_pct":round(margins.get("bottom",1)*100,3),
        })
        print(idx,classification,text_sides,margins)
    outp=root/"meta"/"figure-edge-contact-diagnostic.csv"
    with outp.open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0].keys()))
        w.writeheader();w.writerows(out)
    text_count=sum(x["classification"]=="TEXT_EDGE" for x in out)
    md=root/"meta"/"figure-edge-contact-diagnostic.md"
    md.write_text(
        "# Figure Edge-Contact Diagnostic\n\n"
        f"- Review cases checked: {len(out)}\n"
        f"- Geometry-only edge contacts: {len(out)-text_count}\n"
        f"- Text edge contacts requiring inspection: {text_count}\n",
        encoding="utf-8"
    )
    return 1 if text_count else 0

if __name__=="__main__":
    raise SystemExit(main())
