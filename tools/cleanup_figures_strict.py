#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import csv
import io
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
FONT_SIZE_RE = re.compile(r"font-size:\s*([0-9.]+)px")

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
    png = cairosvg.svg2png(
        bytestring=svg_bytes,
        output_width=width,
        background_color="#ffffff",
    )
    return Image.open(io.BytesIO(png)).convert("RGB")

def mask_from_image(im: Image.Image):
    a = np.asarray(im)
    return np.min(a, axis=2) < 245

def bbox(mask: np.ndarray):
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return None
    return (int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1))

def figure_group(root: ET.Element):
    return next((e for e in root.iter(q("g")) if e.get("id") == "figure_1"), None)

def append_translate(el: ET.Element, dx: float, dy: float):
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return
    old = el.get("transform", "").strip()
    t = f"translate({dx:.6f} {dy:.6f})"
    el.set("transform", t + ((" " + old) if old else ""))

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
        # Do not rewrite text that is already composed from tspans.
        if list(text_el):
            continue

        raw = text_el.text or ""
        if "_" not in raw:
            continue

        matches = list(SUB_RE.finditer(raw))
        if not matches:
            continue

        style = text_el.get("style", "")
        msize = FONT_SIZE_RE.search(style)
        base_size = float(msize.group(1)) if msize else 11.0
        sub_size = max(6.0, base_size * 0.72)
        shift = max(1.5, base_size * 0.24)

        text_el.text = None
        pos = 0

        for m in matches:
            if m.start() > pos:
                lead = ET.SubElement(text_el, q("tspan"))
                lead.set("style", f"font-size: {base_size:.3f}px")
                lead.text = raw[pos:m.start()]

            sub = ET.SubElement(text_el, q("tspan"))
            sub.set("style", f"font-size: {sub_size:.3f}px")
            sub.set("dy", f"{shift:.3f}px")
            sub.text = m.group(1).strip("()")

            # Restore the original baseline and font size before continuing.
            reset = ET.SubElement(text_el, q("tspan"))
            reset.set("style", f"font-size: {base_size:.3f}px")
            reset.set("dy", f"-{shift:.3f}px")
            reset.text = "\u200b"
            pos = m.end()

        if pos < len(raw):
            tail = ET.SubElement(text_el, q("tspan"))
            tail.set("style", f"font-size: {base_size:.3f}px")
            tail.text = raw[pos:]

        changed += len(matches)

    return changed

def max_font_size(group: ET.Element) -> float:
    best = 0.0
    for text in group.iter(q("text")):
        style = text.get("style", "")
        m = FONT_SIZE_RE.search(style)
        if m:
            best = max(best, float(m.group(1)))
    return best

def select_groups(root: ET.Element):
    fig = figure_group(root)
    if fig is None:
        return [], None

    axes = [
        child for child in list(fig)
        if child.tag == q("g") and (child.get("id") or "").startswith("axes_")
    ]

    title_candidates = []
    for child in list(fig):
        if child.tag != q("g"):
            continue
        cid = child.get("id") or ""
        if cid.startswith("axes_") or cid == "patch_1":
            continue
        size = max_font_size(child)
        if size > 0 and text_content(child).strip():
            title_candidates.append((size, child))

    title = max(title_candidates, key=lambda x: x[0])[1] if title_candidates else None
    return axes, title

def render_selected_bbox(root: ET.Element, keep_ids: set[str], width: int = 1200):
    clone = copy.deepcopy(root)
    fig = figure_group(clone)
    if fig is None:
        return None, None

    for child in list(fig):
        cid = child.get("id") or ""
        if cid not in keep_ids:
            fig.remove(child)

    svg = ET.tostring(clone, encoding="utf-8", xml_declaration=True)
    im = render_svg_bytes(svg, width)
    return bbox(mask_from_image(im)), im.size

def find_by_id(root: ET.Element, id_value: str):
    return next((e for e in root.iter(q("g")) if e.get("id") == id_value), None)

def remove_group_ids(root: ET.Element, ids: set[str]):
    if not ids:
        return
    for parent in list(root.iter()):
        for child in list(parent):
            if child.tag == q("g") and (child.get("id") or "") in ids:
                parent.remove(child)

def render_nested_group_bbox(root: ET.Element, axes_id: str, target_id: str, width: int = 1200):
    clone = copy.deepcopy(root)
    fig = figure_group(clone)
    if fig is None:
        return None, None

    axes = next((g for g in list(fig) if g.get("id") == axes_id), None)
    if axes is None:
        return None, None

    for child in list(fig):
        if child is not axes:
            fig.remove(child)

    target = next((g for g in list(axes) if g.get("id") == target_id), None)
    if target is None:
        return None, None

    for child in list(axes):
        if child is not target:
            axes.remove(child)

    svg = ET.tostring(clone, encoding="utf-8", xml_declaration=True)
    im = render_svg_bytes(svg, width)
    return bbox(mask_from_image(im)), im.size

def find_bottom_caption_groups(root: ET.Element, axes_groups: list[ET.Element], title_group: ET.Element | None, width: int = 1200):
    candidates = []
    title_id = title_group.get("id") if title_group is not None else None

    # Figure-level explanatory captions (common Matplotlib figtext pattern).
    fig = figure_group(root)
    if fig is not None:
        for child in list(fig):
            cid = child.get("id") or ""
            if not cid.startswith("text_") or cid == title_id:
                continue
            txt = text_content(child).strip()
            if len(txt) < 35 or txt.count(" ") < 5:
                continue
            size = max_font_size(child)
            if size <= 0 or size > 11.5:
                continue
            bb, canvas = render_selected_bbox(root, {cid}, width)
            if not bb or not canvas:
                continue
            iw, ih = canvas
            if bb[1] >= int(ih * 0.62):
                candidates.append((None, cid, bb, canvas))

    # Axes-level explanatory captions for figures authored with ax.text().
    for axes in axes_groups:
        axes_id = axes.get("id") or ""
        if not axes_id:
            continue
        for child in list(axes):
            cid = child.get("id") or ""
            if not cid.startswith("text_"):
                continue
            txt = text_content(child).strip()
            if len(txt) < 35 or txt.count(" ") < 5:
                continue
            size = max_font_size(child)
            if size <= 0 or size > 11.5:
                continue
            bb, canvas = render_nested_group_bbox(root, axes_id, cid, width)
            if not bb or not canvas:
                continue
            iw, ih = canvas
            if bb[1] >= int(ih * 0.62):
                candidates.append((axes_id, cid, bb, canvas))

    return candidates

def cleanup_one(svg_path: Path, png_path: Path):
    original_svg = svg_path.read_bytes()
    root = ET.fromstring(original_svg)
    vb_x, vb_y, vb_w, vb_h = parse_viewbox(root)

    removed_ids = remove_production_ids(root)
    subs = convert_simple_subscripts(root)

    axes_groups, title_group = select_groups(root)
    axes_ids = {g.get("id") for g in axes_groups if g.get("id")}
    title_id = title_group.get("id") if title_group is not None else None

    dx_u = 0.0
    dy_u = 0.0
    gap_before = None
    gap_after = None
    center_offset_before = None
    center_offset_after = None
    classification = "crop-only"

    if axes_ids and title_id:
        title_bb, size = render_selected_bbox(root, {title_id}, 1200)
        body_bb, _ = render_selected_bbox(root, axes_ids, 1200)

        if title_bb and body_bb and size:
            iw, ih = size
            tx0, ty0, tx1, ty1 = title_bb
            bx0, by0, bx1, by1 = body_bb

            gap_before = by0 - ty1
            center_offset_before = ((bx0 + bx1) / 2.0) - (iw / 2.0)

            title_h = max(1, ty1 - ty0)
            target_gap = max(14, int(title_h * 0.75))

            dx_px = -center_offset_before
            # Keep centering correction bounded so intentionally asymmetric
            # diagrams are not radically rearranged.
            dx_px = max(-0.10 * iw, min(0.10 * iw, dx_px))
            dy_px = -max(0, gap_before - target_gap)

            sx = vb_w / iw
            sy = vb_h / ih
            dx_u = dx_px * sx
            dy_u = dy_px * sy

            if abs(dx_u) > 0.25 or abs(dy_u) > 0.25:
                for group in axes_groups:
                    append_translate(group, dx_u, dy_u)
                classification = "reflow"

                # Re-measure to verify the transformation stayed safe.
                title_bb2, size2 = render_selected_bbox(root, {title_id}, 1200)
                body_bb2, _ = render_selected_bbox(root, axes_ids, 1200)
                if title_bb2 and body_bb2 and size2:
                    iw2, ih2 = size2
                    gap_after = body_bb2[1] - title_bb2[3]
                    center_offset_after = ((body_bb2[0] + body_bb2[2]) / 2.0) - (iw2 / 2.0)

                    # Collision guard: back the body down if rounding/rendering
                    # made the measured gap smaller than half the target.
                    min_safe_gap = max(8, target_gap // 2)
                    if gap_after < min_safe_gap:
                        correction_px = min_safe_gap - gap_after
                        correction_u = correction_px * (vb_h / ih2)
                        for group in axes_groups:
                            append_translate(group, 0.0, correction_u)
                        dy_u += correction_u
                        body_bb3, _ = render_selected_bbox(root, axes_ids, 1200)
                        if body_bb3:
                            gap_after = body_bb3[1] - title_bb2[3]

    # Tighten large internal gaps above long bottom explanatory captions.
    # Only sentence-like small text groups near the bottom of axes are moved;
    # diagrams, plots, equations, arrows, and other geometry remain fixed.
    caption_groups_moved = 0
    caption_shift_u = 0.0
    body_caption_gap_before = None
    body_caption_gap_after = None

    caption_candidates = find_bottom_caption_groups(root, axes_groups, title_group, 1200)
    if caption_candidates:
        caption_ids = {item[1] for item in caption_candidates}

        clone_no_captions = copy.deepcopy(root)
        remove_group_ids(clone_no_captions, caption_ids)
        body_bb, canvas = render_selected_bbox(clone_no_captions, axes_ids, 1200)

        if body_bb and canvas:
            iw, ih = canvas
            caption_top = min(item[2][1] for item in caption_candidates)
            body_bottom = body_bb[3]
            body_caption_gap_before = caption_top - body_bottom

            # Keep approximately one text-line of whitespace.
            cap_heights = [item[2][3] - item[2][1] for item in caption_candidates]
            target_gap = max(14, int(max(cap_heights) * 0.9))
            shift_px = max(0, body_caption_gap_before - target_gap)

            if shift_px > 2:
                sy = vb_h / ih
                caption_shift_u = -(shift_px * sy)
                for _, cid, _, _ in caption_candidates:
                    grp = find_by_id(root, cid)
                    if grp is not None:
                        append_translate(grp, 0.0, caption_shift_u)
                        caption_groups_moved += 1

                # Verify the moved caption union stays separated from body.
                moved_boxes = []
                for axes_id, cid, _, _ in caption_candidates:
                    if axes_id is None:
                        bb2, _ = render_selected_bbox(root, {cid}, 1200)
                    else:
                        bb2, _ = render_nested_group_bbox(root, axes_id, cid, 1200)
                    if bb2:
                        moved_boxes.append(bb2)
                if moved_boxes:
                    body_caption_gap_after = min(bb[1] for bb in moved_boxes) - body_bottom

    # Crop the canvas around the final full composition. This removes the
    # deleted production footer and excessive outer whitespace without
    # changing internal geometry further.
    svg1 = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    im1 = render_svg_bytes(svg1, 1400)
    mask1 = mask_from_image(im1)
    bb = bbox(mask1)

    if bb:
        x0, y0, x1, y1 = bb
        iw, ih = im1.size
        px = max(18, int((x1 - x0) * 0.03))
        py_top = max(16, int((y1 - y0) * 0.03))
        py_bottom = max(28, int((y1 - y0) * 0.04))
        x0 = max(0, x0 - px)
        x1 = min(iw, x1 + px)
        y0 = max(0, y0 - py_top)
        y1 = min(ih, y1 + py_bottom)

        sx = vb_w / iw
        sy = vb_h / ih
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
        "title_body_gap_before_px": gap_before if gap_before is not None else "",
        "title_body_gap_after_px": gap_after if gap_after is not None else "",
        "body_center_offset_before_px": round(center_offset_before, 2) if center_offset_before is not None else "",
        "body_center_offset_after_px": round(center_offset_after, 2) if center_offset_after is not None else "",
        "caption_groups_moved": caption_groups_moved,
        "caption_shift_svg": round(caption_shift_u, 4),
        "body_caption_gap_before_px": body_caption_gap_before if body_caption_gap_before is not None else "",
        "body_caption_gap_after_px": body_caption_gap_after if body_caption_gap_after is not None else "",
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
        item = cleanup_one(svgs[0], pngs[0])
        report.append(item)
        print(
            f"processed {idx:04d}: {item['classification']} "
            f"gap {item['title_body_gap_before_px']} -> {item['title_body_gap_after_px']}"
        )

    report_path = meta_dir / f"figure-cleanup-strict-{args.start:04d}-{args.end:04d}.csv"
    with report_path.open("w", newline="", encoding="utf-8-sig") as f:
        fields = list(report[0].keys())
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(report)

    print(f"Wrote {report_path}")

if __name__ == "__main__":
    main()
