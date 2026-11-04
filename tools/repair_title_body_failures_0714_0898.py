#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg

repo = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("vf", repo / "tools" / "validate_figures_current.py")
vf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vf)

SVG_NS = "http://www.w3.org/2000/svg"
Q = lambda tag: f"{{{SVG_NS}}}{{tag}}"

TARGETS = [714, 898]
TARGET_GAP_PX = 18

def append_translate(el, dx, dy):
    old = (el.get("transform") or "").strip()
    t = f"translate({dx:.6f} {dy:.6f})"
    el.set("transform", t + ((" " + old) if old else ""))

def main():
    out_rows = []
    for idx in TARGETS:
        svg = next((repo / "figures" / "svg").glob(f"{idx:04d}_*.svg"))
        png = next((repo / "figures" / "png").glob(f"{idx:04d}_*.png"))
        root = ET.fromstring(svg.read_bytes())
        vb_x, vb_y, vb_w, vb_h = vf.parse_viewbox(root)
        axes, title = vf.select_axes_title(root)
        if not axes or title is None:
            raise SystemExit(f"{idx:04d}: could not identify axes/title")

        aids = {a.get("id") for a in axes if a.get("id")}
        tid = title.get("id")
        tbb, size = vf.render_selected(root, {tid})
        bbb, _ = vf.render_selected(root, aids)
        if not tbb or not bbb or not size:
            raise SystemExit(f"{idx:04d}: could not measure title/body")

        gap_before = bbb[1] - tbb[3]
        needed_px = max(0, TARGET_GAP_PX - gap_before)
        if needed_px:
            dy_svg = needed_px * (vb_h / size[1])
            for group in axes:
                append_translate(group, 0.0, dy_svg)
        else:
            dy_svg = 0.0

        data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        svg.write_bytes(data)
        cairosvg.svg2png(
            bytestring=data,
            write_to=str(png),
            output_width=3600,
            background_color="#ffffff",
        )

        # Verify immediately using the same current-standards validator.
        row = vf.validate_one(idx, svg, png)
        axes2, title2 = vf.select_axes_title(ET.fromstring(data))
        aids2 = {a.get("id") for a in axes2 if a.get("id")}
        tid2 = title2.get("id") if title2 is not None else None
        tbb2, size2 = vf.render_selected(ET.fromstring(data), {tid2}) if tid2 else (None, None)
        bbb2, _ = vf.render_selected(ET.fromstring(data), aids2) if aids2 else (None, None)
        gap_after = (bbb2[1] - tbb2[3]) if tbb2 and bbb2 else ""

        out_rows.append({
            "index": idx,
            "figure": svg.stem,
            "gap_before_px": gap_before,
            "target_gap_px": TARGET_GAP_PX,
            "dy_svg": round(dy_svg, 6),
            "gap_after_px": gap_after,
            "status_after": row["status"],
            "issues_after": row.get("issues", ""),
            "warnings_after": row.get("warnings", ""),
        })
        print(f"{idx:04d}: gap {gap_before}px -> {gap_after}px; {row['status']} {row.get('issues','')} {row.get('warnings','')}")

    out = repo / "meta" / "figure-targeted-title-body-repairs.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
