#!/usr/bin/env python3
from __future__ import annotations

import csv
import io
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg
import numpy as np
from PIL import Image

SVG_NS = "http://www.w3.org/2000/svg"
Q = lambda tag: f"{{{SVG_NS}}}{tag}"

PROD_EXACT_RE = re.compile(r"^\s*\d{4}\s*[•·]\s*FIG-\d{2}-\d{2}-\d{3}\s*$", re.I)
PROD_TEXT_RE = re.compile(r"(?:\b\d{4}\s*[•·]\s*FIG-\d{2}-\d{2}-\d{3}\b|(?:^|\s)\d{4}_FIG-\d{2}-\d{2}-\d{3}|FIG-\d{2}-\d{2}-\d{3}\.(?:png|svg))", re.I)
SUB_RE = re.compile(r"(?<=\w)_(\([^)]+\)|[A-Za-z0-9]+(?:,[A-Za-z0-9]+)?)")
FONT_SIZE_RE = re.compile(r"font-size:\s*([0-9.]+)px")

def text_content(el: ET.Element) -> str:
    return "".join(el.itertext())

def parse_viewbox(root: ET.Element):
    vb = root.get("viewBox")
    if not vb:
        raise ValueError("SVG missing viewBox")
    vals = [float(x) for x in vb.replace(",", " ").split()]
    if len(vals) != 4 or vals[2] <= 0 or vals[3] <= 0:
        raise ValueError(f"bad viewBox: {vb}")
    return vals

def render_svg(svg_bytes: bytes, width: int = 1200) -> Image.Image:
    png = cairosvg.svg2png(bytestring=svg_bytes, output_width=width, background_color="#ffffff")
    return Image.open(io.BytesIO(png)).convert("RGB")

def mask_bbox(im: Image.Image):
    a = np.asarray(im)
    mask = np.min(a, axis=2) < 245
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return None
    return int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1)

def figure_group(root):
    return next((e for e in root.iter(Q("g")) if e.get("id") == "figure_1"), None)

def max_font_size(group):
    best = 0.0
    for text in group.iter(Q("text")):
        m = FONT_SIZE_RE.search(text.get("style", ""))
        if m:
            best = max(best, float(m.group(1)))
    return best

def select_axes_title(root):
    fig = figure_group(root)
    if fig is None:
        return [], None
    axes = [c for c in list(fig) if c.tag == Q("g") and (c.get("id") or "").startswith("axes_")]
    candidates = []
    for c in list(fig):
        if c.tag != Q("g"):
            continue
        cid = c.get("id") or ""
        if cid.startswith("axes_") or cid == "patch_1":
            continue
        s = max_font_size(c)
        if s > 0 and text_content(c).strip():
            candidates.append((s, c))
    return axes, max(candidates, key=lambda x: x[0])[1] if candidates else None

def render_selected(root, keep_ids, width=1200):
    import copy
    clone = copy.deepcopy(root)
    fig = figure_group(clone)
    if fig is None:
        return None, None
    for c in list(fig):
        if (c.get("id") or "") not in keep_ids:
            fig.remove(c)
    data = ET.tostring(clone, encoding="utf-8", xml_declaration=True)
    im = render_svg(data, width)
    return mask_bbox(im), im.size

def png_info(path: Path):
    with Image.open(path) as im:
        im.load()
        return im.size, im.mode

def validate_one(idx: int, svg_path: Path, png_path: Path):
    issues = []
    warnings = []
    raw = svg_path.read_bytes()
    try:
        root = ET.fromstring(raw)
        vb_x, vb_y, vb_w, vb_h = parse_viewbox(root)
    except Exception as e:
        return {"index": idx, "figure": svg_path.stem, "status": "FAIL", "issues": f"svg_parse:{e}"}

    desc = next(root.iter(Q("desc")), None)
    if desc is None or not text_content(desc).strip():
        issues.append("missing_desc")

    text_nodes = [text_content(t).strip() for t in root.iter(Q("text")) if text_content(t).strip()]
    prod_hits = [t for t in text_nodes if PROD_EXACT_RE.match(t) or PROD_TEXT_RE.search(t)]
    if prod_hits:
        issues.append(f"embedded_production_id:{len(prod_hits)}")

    raw_subs = [t for t in text_nodes if SUB_RE.search(t)]
    if raw_subs:
        issues.append(f"raw_subscript_tokens:{len(raw_subs)}")

    try:
        im = render_svg(raw, 1200)
        bb = mask_bbox(im)
    except Exception as e:
        issues.append(f"svg_render:{e}")
        bb = None
        im = None

    if bb and im:
        iw, ih = im.size
        x0, y0, x1, y1 = bb
        margins = {
            "left": x0 / iw,
            "right": (iw - x1) / iw,
            "top": y0 / ih,
            "bottom": (ih - y1) / ih,
        }
        # Current strict crop uses roughly 3% content padding left/right/top
        # and 4% bottom. Allow 10% per side for approved asymmetric/long-title
        # exceptions while still catching the excessive whitespace regressions.
        excessive = [k for k, v in margins.items() if v > 0.10]
        if excessive:
            issues.append("excess_outer_whitespace:" + "+".join(excessive))
        # Edge contact is review-worthy because some previously approved long
        # titles intentionally retain full horizontal extent.
        edge = [k for k, v in margins.items() if v < 0.001]
        if edge:
            warnings.append("edge_contact:" + "+".join(edge))
    else:
        issues.append("empty_or_unrenderable_svg")

    axes, title = select_axes_title(root)
    if axes and title is not None:
        aids = {a.get("id") for a in axes if a.get("id")}
        tid = title.get("id")
        if aids and tid:
            tbb, size = render_selected(root, {tid})
            bbb, _ = render_selected(root, aids)
            if tbb and bbb and size:
                gap = bbb[1] - tbb[3]
                offset = abs(((bbb[0] + bbb[2]) / 2.0) - size[0] / 2.0)
                if gap < 8:
                    issues.append(f"title_body_collision:{gap}px")
                elif gap > 45:
                    issues.append(f"title_body_gap_excess:{gap}px")
                if offset > size[0] * 0.105:
                    issues.append(f"body_off_center:{offset:.1f}px")

    try:
        (pw, ph), mode = png_info(png_path)
        if pw != 3600:
            issues.append(f"png_width:{pw}")
        svg_ratio = vb_w / vb_h
        png_ratio = pw / ph
        if abs(png_ratio / svg_ratio - 1.0) > 0.01:
            issues.append(f"png_svg_aspect_mismatch:{png_ratio:.4f}/{svg_ratio:.4f}")
    except Exception as e:
        issues.append(f"png_open:{e}")

    status = "FAIL" if issues else ("REVIEW" if warnings else "PASS")
    return {
        "index": idx,
        "figure": svg_path.stem,
        "status": status,
        "issues": ";".join(issues),
        "warnings": ";".join(warnings),
    }

def main():
    root = Path(__file__).resolve().parents[1]
    svg_dir = root / "figures" / "svg"
    png_dir = root / "figures" / "png"
    meta = root / "meta"
    meta.mkdir(exist_ok=True)

    indexed_svg = {}
    indexed_png = {}
    for p in svg_dir.glob("[0-9][0-9][0-9][0-9]_*.svg"):
        indexed_svg.setdefault(int(p.name[:4]), []).append(p)
    for p in png_dir.glob("[0-9][0-9][0-9][0-9]_*.png"):
        indexed_png.setdefault(int(p.name[:4]), []).append(p)

    all_idx = sorted(set(indexed_svg) | set(indexed_png))
    rows = []
    if not all_idx:
        print("No indexed figures found", file=sys.stderr)
        return 2

    for idx in range(all_idx[0], all_idx[-1] + 1):
        svgs = indexed_svg.get(idx, [])
        pngs = indexed_png.get(idx, [])
        if len(svgs) != 1 or len(pngs) != 1:
            rows.append({
                "index": idx,
                "figure": "",
                "status": "FAIL",
                "issues": f"pair_count:svg={len(svgs)},png={len(pngs)}",
                "warnings": "",
            })
            continue
        row = validate_one(idx, svgs[0], pngs[0])
        rows.append(row)
        print(f"{idx:04d} {row['status']} {row.get('issues','')} {row.get('warnings','')}")

    csv_path = meta / "figure-current-standards-validation.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["index", "figure", "status", "issues", "warnings"])
        w.writeheader()
        w.writerows(rows)

    passed = sum(r["status"] == "PASS" for r in rows)
    review = sum(r["status"] == "REVIEW" for r in rows)
    failed = sum(r["status"] == "FAIL" for r in rows)
    categories = {}
    for r in rows:
        for issue in filter(None, r.get("issues", "").split(";")):
            key = issue.split(":", 1)[0]
            categories[key] = categories.get(key, 0) + 1
    summary_path = meta / "figure-current-standards-validation.md"
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Current Figure Standards Validation\n\n")
        f.write(f"- Indexed range: {all_idx[0]:04d}–{all_idx[-1]:04d}\n")
        f.write(f"- Canonical figures checked: {len(rows)}\n")
        f.write(f"- PASS: {passed}\n- REVIEW: {review}\n- FAIL: {failed}\n\n")
        f.write("## Failure categories\n\n")
        if categories:
            for k, v in sorted(categories.items()):
                f.write(f"- {k}: {v}\n")
        else:
            f.write("- None\n")
        f.write("\nREVIEW is reserved for edge-contact conditions that may be intentional approved long-title/asymmetric exceptions. FAIL indicates a current standards violation.\n")

    print(f"Wrote {csv_path}")
    print(f"Wrote {summary_path}")
    print(f"SUMMARY PASS={passed} REVIEW={review} FAIL={failed}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
