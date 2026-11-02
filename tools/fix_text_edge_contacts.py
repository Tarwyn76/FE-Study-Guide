#!/usr/bin/env python3
from __future__ import annotations

import csv
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg

SVG_NS="http://www.w3.org/2000/svg"

def parse_vb(root):
    vals=[float(x) for x in root.get("viewBox").replace(","," ").split()]
    if len(vals)!=4:
        raise ValueError("bad viewBox")
    return vals

def main():
    repo=Path(__file__).resolve().parents[1]
    diag=repo/"meta"/"figure-current-standards-validation.csv"
    rows=list(csv.DictReader(diag.open(encoding="utf-8-sig")))
    targets=[r for r in rows if r["status"]=="REVIEW" and "text_edge_contact:" in (r.get("warnings") or "")]
    report=[]
    for r in targets:
        idx=int(r["index"])
        svg=next((repo/"figures"/"svg").glob(f"{idx:04d}_*.svg"))
        png=next((repo/"figures"/"png").glob(f"{idx:04d}_*.png"))
        root=ET.fromstring(svg.read_bytes())
        x,y,w,h=parse_vb(root)
        pad=w*0.04
        warning=(r.get("warnings") or "")
        sides=set(filter(None,warning.replace("text_edge_contact:","").split("+")))
        old=(x,y,w,h)
        if "left" in sides:
            x-=pad
            w+=pad
        if "right" in sides:
            w+=pad
        root.set("viewBox",f"{x:.6f} {y:.6f} {w:.6f} {h:.6f}")
        root.set("width",f"{w:.3f}pt")
        root.set("height",f"{h:.3f}pt")
        data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
        svg.write_bytes(data)
        cairosvg.svg2png(bytestring=data,write_to=str(png),output_width=3600,background_color="#ffffff")
        report.append({
            "index":idx,
            "figure":svg.stem,
            "sides":"+".join(sorted(sides)),
            "old_viewbox":" ".join(f"{v:.6f}" for v in old),
            "new_viewbox":f"{x:.6f} {y:.6f} {w:.6f} {h:.6f}",
            "horizontal_pad_pct_per_side":4.0,
        })
        print(f"padded {idx:04d} {sides}")
    out=repo/"meta"/"figure-text-edge-padding-fixes.csv"
    with out.open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(report[0].keys()))
        w.writeheader();w.writerows(report)
    print(f"fixed {len(report)} text-edge figures")

if __name__=="__main__":
    main()
