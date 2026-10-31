#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import io
import math
import re
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
from PIL import Image
import numpy as np

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
PROD_RE = re.compile(r"^\s*\d{4}\s*[•·]\s*FIG-\d{2}-\d{2}-\d{3}\s*$", re.I)
SUB_RE = re.compile(r"(?<=\w)_(\([^)]+\)|[A-Za-z0-9]+(?:,[A-Za-z0-9]+)?)")

def q(tag: str) -> str:
    return f"{{{SVG_NS}}}{tag}"

def text_content(el: ET.Element) -> str:
    return "".join(el.itertext())

def parse_viewbox(root: ET.Element):
    vb = root.get("viewBox")
    if not vb:
        raise ValueError("SVG missing viewBox")
    vals = [float(x) for x in vb.replace(",", " ").split()]
    if len(vals) != 4:
        raise ValueError(f"Bad viewBox: {vb}")
    return vals

def render_svg_bytes(svg_bytes: bytes, width: int = 1200) -> Image.Image:
    png = cairosvg.svg2png(bytestring=svg_bytes, output_width=width, background_color="#ffffff")
    return Image.open(io.BytesIO(png)).convert("RGB")

def mask_from_image(im: Image.Image):
    a = np.asarray(im)
    return np.min(a, axis=2) < 245

def row_clusters(mask: np.ndarray):
    h, w = mask.shape
    minpix = max(5, w // 700)
    occ = mask.sum(axis=1)
    rows = np.where(occ >= minpix)[0]
    if len(rows) == 0:
        return []
    out = []
    s = p = int(rows[0])
    for rr in rows[1:]:
        rr = int(rr)
        if rr <= p + 2:
            p = rr
        else:
            out.append((s, p))
            s = p = rr
    out.append((s, p))
    return out

def bbox(mask: np.ndarray, y0: int = 0, y1: int | None = None):
    if y1 is None:
        y1 = mask.shape[0]
    sub = mask[y0:y1]
    ys, xs = np.where(sub)
    if len(xs) == 0:
        return None
    return (int(xs.min()), int(ys.min() + y0), int(xs.max() + 1), int(ys.max() + 1 + y0))

def append_translate(el: ET.Element, dx: float, dy: float):
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return
    old = el.get("transform", "").strip()
    t = f"translate({dx:.6f} {dy:.6f})"
    el.set("transform", (t + (" " + old if old else "")))

def remove_production_ids(root: ET.Element) -> int:
    removed = 0
    for parent in list(root.iter()):
        for child in list(parent):
            if child.tag == q("g") and PROD_RE.match(text_content(child).strip()):
                parent.remove(child)
                removed += 1
    return removed

def convert_simple_subscripts(root: ET.Element) -> int:
    changed = 0
    for text_el in root.iter(q("text")):
        if list(text_el):
            continue
        raw = text_el.text or ""
        if "_" not in raw:
            continue
        matches = list(SUB_RE.finditer(raw))
        if not matches:
            continue
        text_el.text = None
        pos = 0
        for m in matches:
            if m.start() > pos:
                t = ET.SubElement(text_el, q("tspan"))
                t.text = raw[pos:m.start()]
            base_underscore = m.start()
            # underscore itself is omitted; subscript contents are lowered/smaller
            sub = ET.SubElement(text_el, q("tspan"))
            sub.set("font-size", "75%")
            sub.set("dy", "0.28em")
            sub.text = m.group(1).strip("()")
            reset = ET.SubElement(text_el, q("tspan"))
            reset.set("dy", "-0.28em")
            reset.text = ""
            pos = m.end()
        if pos < len(raw):
            t = ET.SubElement(text_el, q("tspan"))
            t.text = raw[pos:]
        changed += len(matches)
    return changed

def find_top_level(root: ET.Element, id_value: str):
    for child in root:
        if child.get("id") == id_value:
            return child
    return None

def cleanup_one(svg_path: Path, png_path: Path):
    original_svg = svg_path.read_bytes()
    tree = ET.ElementTree(ET.fromstring(original_svg))
    root = tree.getroot()
    vb_x, vb_y, vb_w, vb_h = parse_viewbox(root)

    removed_ids = remove_production_ids(root)
    subs = convert_simple_subscripts(root)

    axes = find_top_level(root, "axes_1")
    if axes is None:
        axes = next((e for e in root.iter(q("g")) if e.get("id") == "axes_1"), None)

    # Render after footer/subscript cleanup to measure actual composition.
    svg0 = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    im0 = render_svg_bytes(svg0, 1200)
    mask0 = mask_from_image(im0)
    clusters = row_clusters(mask0)

    dx_u = dy_u = 0.0
    classification = "crop-only"

    if axes is not None and len(clusters) >= 2:
        h, w = mask0.shape
        # Find first substantial whitespace gap after the title band.
        split = None
        for i in range(min(4, len(clusters) - 1)):
            gap = clusters[i + 1][0] - clusters[i][1] - 1
            if gap > max(18, int(h * 0.03)):
                split = (clusters[i][1], clusters[i + 1][0], gap)
                break
        if split:
            title_end, body_start, gap = split
            body_bb = bbox(mask0, body_start, h)
            if body_bb:
                bx0, by0, bx1, by1 = body_bb
                body_center = (bx0 + bx1) / 2.0
                desired_center = w / 2.0
                dx_px = desired_center - body_center
                # Do not overcorrect intentionally asymmetric figures.
                dx_px = max(-0.12 * w, min(0.12 * w, dx_px))
                target_gap_px = max(16, int(h * 0.018))
                dy_px = -(max(0, gap - target_gap_px))
                sx = vb_w / w
                sy = vb_h / h
                dx_u = dx_px * sx
                dy_u = dy_px * sy
                if abs(dx_u) > 0.5 or abs(dy_u) > 0.5:
                    append_translate(axes, dx_u, dy_u)
                    classification = "reflow"

    # Render transformed SVG and crop viewBox around all visible content.
    svg1 = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    im1 = render_svg_bytes(svg1, 1400)
    mask1 = mask_from_image(im1)
    bb = bbox(mask1)
    if bb:
        x0, y0, x1, y1 = bb
        ih, iw = mask1.shape
        px = max(18, int((x1 - x0) * 0.03))
        py = max(16, int((y1 - y0) * 0.03))
        x0 = max(0, x0 - px); x1 = min(iw, x1 + px)
        y0 = max(0, y0 - py); y1 = min(ih, y1 + py)
        sx = vb_w / iw; sy = vb_h / ih
        new_x = vb_x + x0 * sx
        new_y = vb_y + y0 * sy
        new_w = (x1 - x0) * sx
        new_h = (y1 - y0) * sy
        root.set("viewBox", f"{new_x:.6f} {new_y:.6f} {new_w:.6f} {new_h:.6f}")
        root.set("width", f"{new_w:.3f}pt")
        root.set("height", f"{new_h:.3f}pt")
    else:
        new_w, new_h = vb_w, vb_h

    final_svg = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    svg_path.write_bytes(final_svg)

    # Regenerate synchronized PNG at 3600 px wide.
    cairosvg.svg2png(
        bytestring=final_svg,
        write_to=str(png_path),
        output_width=3600,
        background_color="#ffffff",
    )

    area_reduction = 1.0 - (new_w * new_h) / (vb_w * vb_h)
    return {
        "figure": svg_path.stem,
        "classification": classification,
        "production_ids_removed": removed_ids,
        "subscript_tokens_converted": subs,
        "dx_svg": round(dx_u, 4),
        "dy_svg": round(dy_u, 4),
        "old_viewbox_w": round(vb_w, 4),
        "old_viewbox_h": round(vb_h, 4),
        "new_viewbox_w": round(new_w, 4),
        "new_viewbox_h": round(new_h, 4),
        "area_reduction_pct": round(area_reduction * 100.0, 2),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    svg_dir = root / "figures" / "svg"
    png_dir = root / "figures" / "png"
    meta_dir = root / "meta"
    meta_dir.mkdir(exist_ok=True)

    report = []
    for idx in range(args.start, args.end + 1):
        prefix = f"{idx:04d}_"
        svgs = list(svg_dir.glob(prefix + "*.svg"))
        pngs = list(png_dir.glob(prefix + "*.png"))
        if len(svgs) != 1 or len(pngs) != 1:
            raise RuntimeError(f"{idx:04d}: expected exactly one SVG and PNG")
        report.append(cleanup_one(svgs[0], pngs[0]))
        print(f"processed {idx:04d}: {report[-1]['classification']}")

    report_path = meta_dir / f"figure-cleanup-strict-{args.start:04d}-{args.end:04d}.csv"
    with report_path.open("w", newline="", encoding="utf-8-sig") as f:
        fields = list(report[0].keys())
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(report)

    print(f"Wrote {report_path}")

if __name__ == "__main__":
    main()
