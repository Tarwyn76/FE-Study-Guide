#!/usr/bin/env python3
from pathlib import Path
import argparse, collections, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "publication"

ROUTES = {
    "chemical": ("Chemical Engineering", "chemical", range(1, 14), "Chemical-Track-References-and-Sources-complete.md"),
    "civil": ("Civil Engineering", "civil", range(14, 31), "Civil-Track-References-and-Sources-complete.md"),
    "electrical-computer": ("Electrical and Computer Engineering", "electrical-computer", range(31, 47), "ECE-Track-References-and-Sources-complete.md"),
    "environmental": ("Environmental Engineering", "environmental", range(47, 62), "Environmental-Track-References-and-Sources-complete.md"),
    "industrial-systems": ("Industrial and Systems Engineering", "industrial-systems", range(62, 76), "Industrial-Systems-Track-References-and-Sources-complete.md"),
    "mechanical": ("Mechanical Engineering", "mechanical", range(76, 91), "Mechanical-Track-References-and-Sources-complete.md"),
    "other-disciplines": ("Other Disciplines", "other-disciplines", range(91, 96), "Other-Disciplines-Track-References-and-Sources-complete.md"),
}

LAYER_ROOTS = [
    ROOT / "layer-0-orientation",
    ROOT / "layer-1-substrate",
    ROOT / "layer-2-core",
    ROOT / "layer-3-tracks",
]

def chapter_map():
    by = collections.defaultdict(list)
    for base in LAYER_ROOTS:
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            m = re.match(r"^(\d{2}-\d{2})-", p.name)
            if m:
                by[m.group(1)].append(p)
    out = {}
    dup = {}
    for cid, ps in by.items():
        ordered = sorted(ps, key=lambda p: (("(inc)" in p.name.lower()), len(str(p)), str(p)))
        out[cid] = ordered[0]
        if len(ordered) > 1:
            dup[cid] = [str(x.relative_to(ROOT)) for x in ordered]
    return out, dup

CHAPTERS, DUPLICATES = chapter_map()

def strip_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            return text[end+5:]
    return text

def first_h1(text):
    m = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return m.group(1).strip() if m else None

def anchor_for(path):
    stem = path.stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "-", stem).strip("-")
    return "pub-" + stem

def explicit_first_h1(text, anchor):
    m = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    if not m:
        return "# Untitled {#" + anchor + "}\n\n" + text
    heading = m.group(1).strip()
    replacement = f"# {heading} {{#{anchor}}}"
    return text[:m.start()] + replacement + text[m.end():]

def normalize_target(source, raw):
    target = raw.strip().strip("<>")
    if re.match(r"^[a-z]+://", target, re.I) or target.startswith(("mailto:", "#")):
        return None, target
    frag = ""
    if "#" in target:
        target, frag = target.split("#", 1)
    if not target:
        return source, "#" + frag
    p = (source.parent / target).resolve()
    return p, frag

IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")

def process_markdown(path, included, anchor_map, stats):
    text = strip_front_matter(path.read_text(encoding="utf-8", errors="ignore"))
    text = explicit_first_h1(text, anchor_map[path.resolve()])

    def image_sub(m):
        alt, raw = m.group(1), m.group(2)
        if re.match(r"^[a-z]+://", raw, re.I):
            stats["remote_images"] += 1
            return m.group(0)
        base = Path(raw.split("#",1)[0]).name
        png = ROOT / "figures" / "png" / base
        if png.suffix.lower() != ".png":
            png = png.with_suffix(".png")
        if not png.exists():
            stats["missing_images"].append({
                "source": str(path.relative_to(ROOT)),
                "link": raw,
                "expected": str(png.relative_to(ROOT)),
            })
            return m.group(0)
        stats["images"] += 1
        return f"![{alt}](figures/png/{png.name})"

    text = IMAGE_RE.sub(image_sub, text)

    def link_sub(m):
        label, raw = m.group(1), m.group(2).strip()
        if re.match(r"^[a-z]+://", raw, re.I) or raw.startswith(("mailto:", "#")):
            if raw.startswith("#"):
                stats["same_doc_fragments"] += 1
            else:
                stats["external_links"] += 1
            return m.group(0)
        target_path, frag = normalize_target(path.resolve(), raw)
        if target_path and target_path.suffix.lower() == ".md":
            if target_path in included and target_path in anchor_map:
                stats["rewritten_local_links"] += 1
                if frag:
                    stats["crossfile_fragment_links_to_top"] += 1
                return f"[{label}](#{anchor_map[target_path]})"
            stats["links_to_unincluded_md"] += 1
            return label
        # Preserve non-Markdown local links; preflight will report if needed.
        stats["other_local_links"] += 1
        return m.group(0)

    text = LINK_RE.sub(link_sub, text)
    return text.strip() + "\n"

def route_sources(route):
    display, exam_slug, nums, track_ref = ROUTES[route]
    common_ids = [f"00-{i:02d}" for i in range(1,4)]
    common_ids += [f"01-{i:02d}" for i in range(1,41)]
    common_ids += [f"02-{i:02d}" for i in range(1,71)]
    track_ids = [f"03-{i:02d}" for i in nums]
    missing_ids = [cid for cid in common_ids + track_ids if cid not in CHAPTERS]
    if missing_ids:
        raise RuntimeError("Missing canonical chapter IDs: " + ", ".join(missing_ids))

    route_file = ROOT / "routes" / f"route-{route}.md"
    tier = [ROOT / "appendices" / "review-exams" / f"tier-{x}-review.md"
            for x in ("1a","1b","1c","1d","2a","2b","2c","2d","2e","2f")]
    practice = [
        ROOT / "appendices" / "practice-exams" / f"{exam_slug}-practice-a.md",
        ROOT / "appendices" / "practice-exams" / f"{exam_slug}-practice-b.md",
    ]
    appendices = [
        ROOT / "appendices" / "unit-tables.md",
        ROOT / "appendices" / "formula-index.md",
        ROOT / "appendices" / "notation-master.md",
    ]
    references = [
        ROOT / "references" / "References-and-Sources-Master-Index.md",
        ROOT / "references" / "Core-Curriculum-References-and-Sources-complete.md",
        ROOT / "references" / track_ref,
    ]

    order = [route_file]
    order += [CHAPTERS[cid] for cid in common_ids]
    order += [CHAPTERS[cid] for cid in track_ids]
    order += tier + practice + appendices + references
    missing = [str(p.relative_to(ROOT)) for p in order if not p.exists()]
    if missing:
        raise RuntimeError("Missing publication source files: " + ", ".join(missing))
    return display, order

def metadata(display):
    return f"""---
title: "FE Supplemental Study Guide — {display} Route"
subtitle: "Release Candidate Publication"
date: "2026-11-14"
lang: en-US
documentclass: report
classoption:
  - oneside
papersize: letter
geometry:
  - margin=0.75in
fontsize: 10pt
toc: true
toc-depth: 2
numbersections: false
colorlinks: true
linkcolor: blue
urlcolor: blue
mainfont: "DejaVu Serif"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
header-includes:
  - |
    \\usepackage{{graphicx}}
    \\usepackage{{float}}
    \\usepackage{{longtable}}
    \\usepackage{{booktabs}}
    \\usepackage{{microtype}}
    \\setkeys{{Gin}}{{width=\\linewidth,height=0.82\\textheight,keepaspectratio}}
---

"""

def assemble(route):
    display, sources = route_sources(route)
    included = {p.resolve() for p in sources}
    anchor_map = {p.resolve(): anchor_for(p) for p in sources}
    stats = collections.defaultdict(int)
    stats["missing_images"] = []

    parts = [metadata(display)]
    for i, p in enumerate(sources):
        rel = p.relative_to(ROOT)
        parts += [
            "\n\n<!-- PUBLICATION SOURCE: " + str(rel) + " -->\n\n",
            process_markdown(p.resolve(), included, anchor_map, stats),
        ]
    BUILD.mkdir(parents=True, exist_ok=True)
    out = BUILD / f"fe-study-guide-{route}.md"
    out.write_text("".join(parts), encoding="utf-8")

    info = {
        "route": route,
        "display_name": display,
        "source_files": len(sources),
        "canonical_chapters": sum(1 for p in sources if re.match(r"^\d{2}-\d{2}-", p.name)),
        "images": stats["images"],
        "missing_images": stats["missing_images"],
        "external_links": stats["external_links"],
        "rewritten_local_links": stats["rewritten_local_links"],
        "crossfile_fragment_links_to_top": stats["crossfile_fragment_links_to_top"],
        "links_to_unincluded_md": stats["links_to_unincluded_md"],
        "other_local_links": stats["other_local_links"],
        "same_doc_fragments": stats["same_doc_fragments"],
        "remote_images": stats["remote_images"],
        "markdown_bytes": out.stat().st_size,
        "output_markdown": str(out.relative_to(ROOT)),
    }
    report = BUILD / f"fe-study-guide-{route}-preflight.json"
    report.write_text(json.dumps(info, indent=2), encoding="utf-8")
    if info["missing_images"]:
        print(json.dumps(info, indent=2))
        raise RuntimeError(f"{route}: {len(info['missing_images'])} missing image asset(s)")
    return info

def all_preflight():
    results = []
    for route in ROUTES:
        results.append(assemble(route))
    summary = {
        "routes": len(results),
        "results": results,
        "duplicate_chapter_ids": DUPLICATES,
    }
    (BUILD / "publication-preflight-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if DUPLICATES:
        print("NOTE: duplicate chapter IDs exist; canonical selection recorded above.", file=sys.stderr)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--route", choices=list(ROUTES))
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    if args.all or not args.route:
        all_preflight()
    else:
        print(json.dumps(assemble(args.route), indent=2))

if __name__ == "__main__":
    main()
