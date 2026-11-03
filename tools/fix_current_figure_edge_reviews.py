#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg

SVG_NS = "http://www.w3.org/2000/svg"
EDGE_RE = re.compile(r"(?:^|;)text_edge_contact:([^;]+)")

def parse_viewbox(root):
    raw = root.get("viewBox")
    if not raw:
        raise ValueError("SVG missing viewBox")
    vals = [float(x) for x in raw.replace(",", " ").split()]
    if len(vals) != 4 or vals[2] <= 0 or vals[3] <= 0:
        raise ValueError(f"bad viewBox: {raw}")
    return vals

def main():
    repo = Path(__file__).resolve().parents[1]
    report_path = repo / "meta" / "figure-current-standards-validation.csv"
    if not report_path.exists():
        raise SystemExit("Run tools/validate_figures_current.py first")

    rows = list(csv.DictReader(report_path.open(encoding="utf-8-sig")))
    targets = []
    for row in rows:
        if row.get("status") != "REVIEW":
            continue
        m = EDGE_RE.search(row.get("warnings") or "")
        if not m:
            continue
        sides = {s for s in m.group(1).split("+") if s in {"left","right","top","bottom"}}
        if sides:
            targets.append((int(row["index"]), row["figure"], sides))

    out_rows = []
    for idx, figure, sides in targets:
        svg = next((repo / "figures" / "svg").glob(f"{idx:04d}_*.svg"))
        png = next((repo / "figures" / "png").glob(f"{idx:04d}_*.png"))
        root = ET.fromstring(svg.read_bytes())
        x, y, w, h = parse_viewbox(root)
        old = (x, y, w, h)

        # Minimal recovery margin: enough to expose text geometry that is
        # currently clipped at the viewBox edge while remaining well inside
        # the validator's 10% outer-whitespace limit.
        px = w * 0.04
        py = h * 0.04
        if "left" in sides:
            x -= px
            w += px
        if "right" in sides:
            w += px
        if "top" in sides:
            y -= py
            h += py
        if "bottom" in sides:
            h += py

        root.set("viewBox", f"{x:.6f} {y:.6f} {w:.6f} {h:.6f}")
        root.set("width", f"{w:.3f}pt")
        root.set("height", f"{h:.3f}pt")
        data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        svg.write_bytes(data)
        cairosvg.svg2png(
            bytestring=data,
            write_to=str(png),
            output_width=3600,
            background_color="#ffffff",
        )
        out_rows.append({
            "index": idx,
            "figure": figure,
            "sides": "+".join(sorted(sides)),
            "old_viewbox": " ".join(f"{v:.6f}" for v in old),
            "new_viewbox": f"{x:.6f} {y:.6f} {w:.6f} {h:.6f}",
            "padding_fraction": "0.04",
        })
        print(f"padded {idx:04d} {figure}: {'+'.join(sorted(sides))}")

    out = repo / "meta" / "figure-current-edge-padding-fixes.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        fields = ["index","figure","sides","old_viewbox","new_viewbox","padding_fraction"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"EDGE_REVIEW_TARGETS={len(targets)}")
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
