#!/usr/bin/env python3
"""
Conservative textbook-layout normalization for FE Guide SVG figures.

This pass only trims exterior whitespace/canvas size. It does not move semantic
diagram groups or rewrite labels. Figures with large internal blank bands are
reported for manual review.
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import re
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
from PIL import Image

NUM_UNIT = re.compile(r"^\s*([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)\s*([A-Za-z%]*)\s*$")
INDEX_RE = re.compile(r"^(\d{4})_")

def parse_number_unit(value: str | None):
    if not value:
        return None
    m = NUM_UNIT.match(value)
    if not m:
        return None
    return float(m.group(1)), m.group(2)

def fmt(v: float) -> str:
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return s if s else "0"

def is_background(elem: ET.Element) -> bool:
    eid = elem.attrib.get("id", "")
    if eid == "patch_1":
        return True
    style = elem.attrib.get("style", "").replace(" ", "").lower()
    fill = elem.attrib.get("fill", "").replace(" ", "").lower()
    stroke = elem.attrib.get("stroke", "").replace(" ", "").lower()
    white = ("fill:#ffffff" in style or "fill:white" in style or fill in {"#fff", "#ffffff", "white"})
    nostroke = ("stroke:none" in style or stroke in {"", "none"})
    return white and nostroke and elem.tag.rsplit("}", 1)[-1] == "rect"

def remove_backgrounds(root: ET.Element) -> None:
    for parent in root.iter():
        for child in list(parent):
            if is_background(child):
                parent.remove(child)

def render_bbox(svg_text: str, max_px: int = 1800):
    root = ET.fromstring(svg_text)
    vb = root.attrib.get("viewBox")
    if not vb:
        return None
    vals = [float(x) for x in vb.replace(",", " ").split()]
    if len(vals) != 4:
        return None
    vx, vy, vw, vh = vals
    if vw <= 0 or vh <= 0:
        return None

    remove_backgrounds(root)
    clean = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    scale = min(max_px / max(vw, vh), 4.0)
    scale = max(scale, 1.0)
    out_w = max(1, int(math.ceil(vw * scale)))
    out_h = max(1, int(math.ceil(vh * scale)))
    png = cairosvg.svg2png(bytestring=clean, output_width=out_w, output_height=out_h)
    im = Image.open(io.BytesIO(png)).convert("RGBA")

    px = im.load()
    minx, miny = im.width, im.height
    maxx = maxy = -1
    occupied_rows = [False] * im.height
    occupied_cols = [False] * im.width

    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a <= 8:
                continue
            if r >= 249 and g >= 249 and b >= 249:
                continue
            minx = min(minx, x); maxx = max(maxx, x)
            miny = min(miny, y); maxy = max(maxy, y)
            occupied_rows[y] = True
            occupied_cols[x] = True

    if maxx < minx or maxy < miny:
        return None

    x0 = vx + (minx / im.width) * vw
    x1 = vx + ((maxx + 1) / im.width) * vw
    y0 = vy + (miny / im.height) * vh
    y1 = vy + ((maxy + 1) / im.height) * vh

    def largest_blank(flags, start, end):
        best = cur = 0
        for i in range(start, end + 1):
            if not flags[i]:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return best

    inner_h = maxy - miny + 1
    inner_w = maxx - minx + 1
    blank_row = largest_blank(occupied_rows, miny, maxy) / max(1, inner_h)
    blank_col = largest_blank(occupied_cols, minx, maxx) / max(1, inner_w)

    return (vx, vy, vw, vh), (x0, y0, x1, y1), blank_row, blank_col

def update_svg(svg_text: str, margin_fraction: float, min_margin: float):
    info = render_bbox(svg_text)
    if not info:
        return svg_text, None
    (vx, vy, vw, vh), (x0, y0, x1, y1), blank_row, blank_col = info
    cw, ch = x1 - x0, y1 - y0
    margin = max(min_margin, margin_fraction * max(cw, ch))

    nx0 = max(vx, x0 - margin)
    ny0 = max(vy, y0 - margin)
    nx1 = min(vx + vw, x1 + margin)
    ny1 = min(vy + vh, y1 + margin)
    nw, nh = nx1 - nx0, ny1 - ny0

    old_area = vw * vh
    new_area = nw * nh
    reduction = 1.0 - (new_area / old_area)

    # Avoid tiny, churn-only edits.
    if reduction < 0.035:
        return svg_text, {
            "changed": False, "reduction": reduction,
            "blank_row": blank_row, "blank_col": blank_col,
            "old_w": vw, "old_h": vh, "new_w": vw, "new_h": vh,
        }

    root = ET.fromstring(svg_text)
    root.set("viewBox", f"{fmt(nx0)} {fmt(ny0)} {fmt(nw)} {fmt(nh)}")

    for attr, old_dim, new_dim in (("width", vw, nw), ("height", vh, nh)):
        parsed = parse_number_unit(root.attrib.get(attr))
        if parsed:
            val, unit = parsed
            root.set(attr, f"{fmt(val * new_dim / old_dim)}{unit}")

    new_text = ET.tostring(root, encoding="unicode")
    if svg_text.lstrip().startswith("<?xml"):
        new_text = "<?xml version='1.0' encoding='UTF-8'?>\n" + new_text

    return new_text, {
        "changed": True, "reduction": reduction,
        "blank_row": blank_row, "blank_col": blank_col,
        "old_w": vw, "old_h": vh, "new_w": nw, "new_h": nh,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="figures/svg")
    ap.add_argument("--start-index", type=int, default=13,
                    help="Skip indexed figures below this number; 0000-0012 are manually reviewed.")
    ap.add_argument("--margin-fraction", type=float, default=0.025)
    ap.add_argument("--min-margin", type=float, default=8.0)
    ap.add_argument("--report", default="meta/figure-layout-cleanup-report.csv")
    args = ap.parse_args()

    root = Path(args.root)
    report = Path(args.report)
    report.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    changed = 0
    scanned = 0

    for path in sorted(root.glob("*.svg")):
        m = INDEX_RE.match(path.name)
        if m and int(m.group(1)) < args.start_index:
            continue

        scanned += 1
        original = path.read_text(encoding="utf-8")
        try:
            updated, stats = update_svg(original, args.margin_fraction, args.min_margin)
        except Exception as exc:
            rows.append({
                "figure": path.name, "status": "ERROR", "area_reduction_pct": "",
                "largest_internal_blank_row_pct": "", "largest_internal_blank_col_pct": "",
                "manual_review": "YES", "reason": str(exc),
            })
            continue

        if not stats:
            rows.append({
                "figure": path.name, "status": "SKIP", "area_reduction_pct": "",
                "largest_internal_blank_row_pct": "", "largest_internal_blank_col_pct": "",
                "manual_review": "YES", "reason": "No renderable content/viewBox",
            })
            continue

        if stats["changed"] and updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            status = "TRIMMED"
        else:
            status = "UNCHANGED"

        blank_r = stats["blank_row"] * 100
        blank_c = stats["blank_col"] * 100
        manual = blank_r >= 18 or blank_c >= 22
        reason = []
        if blank_r >= 18:
            reason.append("large internal vertical gap")
        if blank_c >= 22:
            reason.append("large internal horizontal gap")

        rows.append({
            "figure": path.name,
            "status": status,
            "area_reduction_pct": f"{stats['reduction']*100:.1f}",
            "largest_internal_blank_row_pct": f"{blank_r:.1f}",
            "largest_internal_blank_col_pct": f"{blank_c:.1f}",
            "manual_review": "YES" if manual else "NO",
            "reason": "; ".join(reason),
        })

    with report.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "figure", "status", "area_reduction_pct",
            "largest_internal_blank_row_pct", "largest_internal_blank_col_pct",
            "manual_review", "reason"
        ])
        w.writeheader()
        w.writerows(rows)

    print(f"Scanned {scanned} SVGs; trimmed {changed}; report: {report}")
    flagged = sum(r["manual_review"] == "YES" for r in rows)
    print(f"Manual semantic/layout review flags: {flagged}")

if __name__ == "__main__":
    main()
