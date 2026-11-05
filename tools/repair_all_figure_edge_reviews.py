#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path
import cairosvg

repo = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("vf", repo/"tools"/"validate_figures_current.py")
vf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vf)

def parse_vb(root):
    return vf.parse_viewbox(root)

def repair_once(idx, sides, fraction):
    svg = next((repo/"figures"/"svg").glob(f"{idx:04d}_*.svg"))
    png = next((repo/"figures"/"png").glob(f"{idx:04d}_*.png"))
    root = ET.fromstring(svg.read_bytes())
    x,y,w,h = parse_vb(root)
    old=(x,y,w,h)
    px=w*fraction; py=h*fraction
    if "left" in sides: x-=px; w+=px
    if "right" in sides: w+=px
    if "top" in sides: y-=py; h+=py
    if "bottom" in sides: h+=py
    root.set("viewBox",f"{x:.6f} {y:.6f} {w:.6f} {h:.6f}")
    root.set("width",f"{w:.3f}pt"); root.set("height",f"{h:.3f}pt")
    data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
    svg.write_bytes(data)
    cairosvg.svg2png(bytestring=data,write_to=str(png),output_width=3600,background_color="#ffffff")
    return old,(x,y,w,h),svg,png

def main():
    report=[]
    fractions=(0.04,0.04,0.03)
    for round_no,fraction in enumerate(fractions,1):
        rows=[]
        for idx in range(1404):
            svg=next((repo/"figures"/"svg").glob(f"{idx:04d}_*.svg"))
            png=next((repo/"figures"/"png").glob(f"{idx:04d}_*.png"))
            rows.append(vf.validate_one(idx,svg,png))
        reviews=[r for r in rows if r["status"]=="REVIEW" and "text_edge_contact:" in (r.get("warnings") or "")]
        print(f"round {round_no}: edge reviews before={len(reviews)}")
        if not reviews: break
        for r in reviews:
            idx=int(r["index"])
            warning=r.get("warnings") or ""
            sides=set(warning.split("text_edge_contact:",1)[1].split(";",1)[0].split("+"))
            old,new,svg,png=repair_once(idx,sides,fraction)
            after=vf.validate_one(idx,svg,png)
            report.append({
                "round":round_no,"index":idx,"figure":r["figure"],
                "sides":"+".join(sorted(sides)),"padding_fraction":fraction,
                "status_before":r["status"],"status_after":after["status"],
                "issues_after":after.get("issues",""),"warnings_after":after.get("warnings",""),
                "old_viewbox":" ".join(f"{v:.6f}" for v in old),
                "new_viewbox":" ".join(f"{v:.6f}" for v in new),
            })
    out=repo/"meta"/"figure-edge-repair-current.csv"
    with out.open("w",newline="",encoding="utf-8-sig") as f:
        fields=["round","index","figure","sides","padding_fraction","status_before","status_after","issues_after","warnings_after","old_viewbox","new_viewbox"]
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(report)
    print(f"repair actions={len(report)}")
    print(out)

if __name__=="__main__":
    main()
