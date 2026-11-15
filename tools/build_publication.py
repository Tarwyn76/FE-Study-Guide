#!/usr/bin/env python3
from pathlib import Path
import argparse, collections, json, re, sys, subprocess, shutil

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "publication"

ROUTES = {
    "chemical": ("Chemical Engineering", "chemical", range(1, 14), "Chemical-Track-References-and-Sources-complete.md"),
    "civil": ("Civil Engineering", "civil", range(14, 31), "Civil-Track-References-and-Sources-complete.md"),
    "electrical-computer": ("Electrical and Computer Engineering", "electrical-computer", range(31, 48), "ECE-Track-References-and-Sources-complete.md"),
    "environmental": ("Environmental Engineering", "environmental", range(48, 62), "Environmental-Track-References-and-Sources-complete.md"),
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
    """Remove one leading YAML metadata block, tolerating BOM, CRLF, and blank space."""
    text=text.lstrip("\ufeff")
    m=re.match(r"\A[ \t\r\n]*---[ \t]*\r?\n.*?\r?\n---[ \t]*\r?\n", text, re.S)
    if m:
        return text[m.end():]
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

IMAGE_RE = re.compile(r"!\[(.*?)\]\(([^)\n]+)\)", re.S)
FIGURE_ID_RE = re.compile(r"(FIG-\d{2}-\d{2}-\d{3})", re.I)

def resolve_figure(raw):
    base = Path(raw.split("#",1)[0]).name
    if Path(base).suffix.lower() != ".png":
        base = str(Path(base).with_suffix(".png"))
    exact = ROOT / "figures" / "png" / base
    if exact.exists():
        return exact, "exact"
    m = FIGURE_ID_RE.search(base)
    if not m:
        return None, "no-id"
    fid = m.group(1).upper()
    candidates = sorted((ROOT/"figures"/"png").glob(f"*{fid}*.png"))
    if len(candidates) == 1:
        return candidates[0], "figure-id"
    # Prefer an exact FIG-ID asset over descriptive or alternate aliases.
    exact_id = [p for p in candidates if re.fullmatch(rf"(?:\d{{4}}_)?{re.escape(fid)}\.png", p.name, re.I)]
    if len(exact_id) == 1:
        return exact_id[0], "figure-id-exact"
    return None, "ambiguous"
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")

def normalize_nested_math_delimiters(text, path, stats):
    """Remove TeX math open/close delimiters that appear inside $...$ or $...$."""
    def clean_content(content, offset):
        original=content
        content=content.replace(r"\(", "").replace(r"\)", "")
        # Markdown escaping can leave an invalid TeX escaped star in math
        # (for example x^\*). Normalize it to an explicit math superscript/
        # subscript star so XeLaTeX receives valid syntax.
        content=re.sub(r"([_^])\\\*", r"\1{*}", content)
        if content == original:
            return content
        line = text.count("\n", 0, offset) + 1
        stats["nested_math_repairs"].append({
            "source": str(path.relative_to(ROOT)),
            "line": line,
            "snippet": re.sub(r"\s+", " ", original).strip()[:240],
        })
        return content

    # Display math first so the inline pass cannot consume its dollar pairs.
    out=[]; pos=0
    for m in re.finditer(r"\$\$(.*?)\$\$", text, re.S):
        out.append(text[pos:m.start()])
        body=clean_content(m.group(1),m.start(1))
        out.append("$$"+body+"$$")
        pos=m.end()
    out.append(text[pos:])
    text2="".join(out)

    out=[]; pos=0
    for m in re.finditer(r"(?<![\\$])\$([^$\n]+?)(?<!\\)\$(?!\$)", text2):
        out.append(text2[pos:m.start()])
        body=m.group(1)
        if any(tok in body for tok in (r"\(", r"\)")):
            line=text2.count("\n",0,m.start(1))+1
            stats["nested_math_repairs"].append({
                "source": str(path.relative_to(ROOT)),
                "line": line,
                "snippet": re.sub(r"\s+", " ", body).strip()[:240],
            })
            body=body.replace(r"\(","").replace(r"\)","")
        body=re.sub(r"([_^])\\\*", r"\1{*}", body)
        out.append("$"+body+"$")
        pos=m.end()
    out.append(text2[pos:])
    return "".join(out)

def process_markdown(path, included, anchor_map, stats):
    text = strip_front_matter(path.read_text(encoding="utf-8", errors="ignore"))
    text = normalize_nested_math_delimiters(text, path, stats)
    # Pandoc can lower some display blocks to inline math in large concatenated
    # documents; amsmath then rejects \\tag. Preserve the visible number without
    # using the restricted command.
    text = re.sub(r"\\tag\{([^{}]+)\}", r"\\qquad\\text{(\1)}", text)
    text = explicit_first_h1(text, anchor_map[path.resolve()])

    def image_sub(m):
        alt, dest = m.group(1), m.group(2).strip()
        # Markdown image destinations may include an optional title after the path.
        if dest.startswith("<") and ">" in dest:
            raw = dest[1:dest.index(">")]
        else:
            raw = dest.split(None, 1)[0]
        raw = raw.strip().strip("<>")
        if re.match(r"^[a-z]+://", raw, re.I):
            stats["remote_images"] += 1
            return m.group(0)
        png, mode = resolve_figure(raw)
        if png is None:
            stats["missing_images"].append({
                "source": str(path.relative_to(ROOT)),
                "link": raw,
                "resolution": mode,
            })
            return m.group(0)
        stats["images"] += 1
        if mode != "exact":
            stats["figure_id_resolutions"] += 1
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
    common_ids += [f"01-{i:02d}" for i in range(1,42)]
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

def metadata_text(display):
    return f"""title: "FE Supplemental Study Guide — {display} Route"
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
    \\usepackage{{cancel}}
    \\usepackage{{xurl}}
    \\Urlmuskip=0mu plus 1mu\\relax
    \\setlength{{\\emergencystretch}}{{3em}}
    \\setkeys{{Gin}}{{width=\\linewidth,height=0.82\\textheight,keepaspectratio}}
"""

def assemble(route):
    display, sources = route_sources(route)
    included = {p.resolve() for p in sources}
    anchor_map = {p.resolve(): anchor_for(p) for p in sources}
    stats = collections.defaultdict(int)
    stats["missing_images"] = []
    stats["nested_math_repairs"] = []

    meta = BUILD / f"fe-study-guide-{route}.yaml"
    BUILD.mkdir(parents=True, exist_ok=True)
    meta.write_text(metadata_text(display), encoding="utf-8")
    parts = []
    for i, p in enumerate(sources):
        rel = p.relative_to(ROOT)
        parts += [
            "\n\n<!-- PUBLICATION SOURCE: " + str(rel) + " -->\n\n",
            process_markdown(p.resolve(), included, anchor_map, stats),
        ]
    out = BUILD / f"fe-study-guide-{route}.md"
    out.write_text("".join(parts), encoding="utf-8")

    info = {
        "route": route,
        "display_name": display,
        "source_files": len(sources),
        "canonical_chapters": sum(1 for p in sources if re.match(r"^\d{2}-\d{2}-", p.name)),
        "images": stats["images"],
        "figure_id_resolutions": stats["figure_id_resolutions"],
        "missing_images": stats["missing_images"],
        "nested_math_repairs": stats["nested_math_repairs"],
        "external_links": stats["external_links"],
        "rewritten_local_links": stats["rewritten_local_links"],
        "crossfile_fragment_links_to_top": stats["crossfile_fragment_links_to_top"],
        "links_to_unincluded_md": stats["links_to_unincluded_md"],
        "other_local_links": stats["other_local_links"],
        "same_doc_fragments": stats["same_doc_fragments"],
        "remote_images": stats["remote_images"],
        "markdown_bytes": out.stat().st_size,
        "output_markdown": str(out.relative_to(ROOT)),
        "metadata_file": str(meta.relative_to(ROOT)),
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
    return results

def run_checked(cmd, **kwargs):
    print("+", " ".join(str(x) for x in cmd), flush=True)
    return subprocess.run(cmd, check=True, text=True, **kwargs)

def render_and_validate(info):
    route=info["route"]
    md=ROOT/info["output_markdown"]
    meta=ROOT/info["metadata_file"]
    pdf=BUILD/f"fe-study-guide-{route}.pdf"
    log=BUILD/f"fe-study-guide-{route}.latex.log"

    cmd=[
        "pandoc", str(md.relative_to(ROOT)),
        "--metadata-file", str(meta.relative_to(ROOT)),
        "--from", "markdown-yaml_metadata_block+raw_tex+tex_math_dollars",
        "--pdf-engine=xelatex",
        "--resource-path", ".",
        "--standalone",
        "--toc", "--toc-depth=2",
        "-o", str(pdf.relative_to(ROOT)),
    ]
    proc=subprocess.run(cmd,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log.write_text(proc.stdout,encoding="utf-8")
    if proc.returncode != 0:
        print(proc.stdout[-16000:])
        raise RuntimeError(f"{route}: Pandoc/XeLaTeX build failed")

    q=subprocess.run(["qpdf","--check",str(pdf)],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if q.returncode != 0:
        raise RuntimeError(f"{route}: qpdf validation failed: {q.stdout}")

    pinfo=run_checked(["pdfinfo",str(pdf)],capture_output=True).stdout
    pages=int(re.search(r"(?m)^Pages:\s+(\d+)",pinfo).group(1))
    page_size=re.search(r"(?m)^Page size:\s+(.+)$",pinfo).group(1).strip()

    txt=BUILD/f"fe-study-guide-{route}.txt"
    run_checked(["pdftotext","-layout",str(pdf),str(txt)])
    extracted=txt.read_text(encoding="utf-8",errors="ignore")

    missing_titles=[]
    display, sources=route_sources(route)
    for p in sources:
        if not re.match(r"^\d{2}-\d{2}-",p.name):
            continue
        t=first_h1(strip_front_matter(p.read_text(encoding="utf-8",errors="ignore")))
        if t and re.sub(r"\s+"," ",t).strip() not in re.sub(r"\s+"," ",extracted):
            missing_titles.append(t)

    page_texts=extracted.split("\f")
    empty=[i+1 for i,x in enumerate(page_texts) if len(re.sub(r"\s+","",x))<12]
    consecutive=[(n,n+1) for n in empty if n+1 in empty]

    render_dir=BUILD/f"fe-study-guide-{route}-renders"
    render_dir.mkdir(exist_ok=True)
    sample_pages=sorted({1,max(1,pages//4),max(1,pages//2),max(1,3*pages//4),pages})
    samples=[]
    try:
        from PIL import Image, ImageStat
        for pg in sample_pages:
            prefix=render_dir/f"page-{pg}"
            run_checked(["pdftoppm","-f",str(pg),"-singlefile","-r","90","-gray","-png",str(pdf),str(prefix)],
                        stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            im=Image.open(str(prefix)+".png").convert("L")
            st=ImageStat.Stat(im)
            samples.append({"page":pg,"mean_gray":round(st.mean[0],1),"std_gray":round(st.stddev[0],1)})
            if st.stddev[0] < 2.0:
                raise RuntimeError(f"{route}: rendered sample page {pg} appears blank")
    except ImportError:
        samples=[]

    ltxt=log.read_text(encoding="utf-8",errors="ignore")
    return {
        **info,
        "pdf":str(pdf.relative_to(ROOT)),
        "pdf_bytes":pdf.stat().st_size,
        "pages":pages,
        "page_size":page_size,
        "missing_chapter_titles":missing_titles,
        "consecutive_blank_pages":consecutive,
        "overfull_hbox_warnings":len(re.findall(r"Overfull \\\\hbox",ltxt)),
        "missing_glyph_warnings":len(re.findall(r"Missing character:",ltxt)),
        "undefined_reference_warnings":len(re.findall(r"(?:undefined reference|Reference .* undefined)",ltxt,re.I)),
        "render_samples":samples,
    }

def render_all(preflight_results):
    results=[]
    for info in preflight_results:
        results.append(render_and_validate(info))

    hard=[]
    for r in results:
        if r["missing_chapter_titles"]:
            hard.append((r["route"],"missing chapter titles",r["missing_chapter_titles"][:5]))
        if r["consecutive_blank_pages"]:
            hard.append((r["route"],"consecutive blank pages",r["consecutive_blank_pages"][:5]))
        if r["missing_glyph_warnings"]:
            hard.append((r["route"],"missing glyph warnings",r["missing_glyph_warnings"]))
        if r["undefined_reference_warnings"]:
            hard.append((r["route"],"undefined reference warnings",r["undefined_reference_warnings"]))

    outdir=ROOT/"reports"/"publishing"
    outdir.mkdir(parents=True,exist_ok=True)
    summary={"routes":results,"hard_findings":hard}
    (outdir/"publishing-validation.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    lines=["# FE Guide Publishing Validation","",
           "Image-artwork aesthetic QA remains deferred; this report covers publication rendering and structure.","",
           "| Route | Chapters | Pages | PDF size | Overfull boxes | Missing glyphs | Missing titles |",
           "|---|---:|---:|---:|---:|---:|---:|"]
    for r in results:
        lines.append(f"| {r['route']} | {r['canonical_chapters']} | {r['pages']} | {r['pdf_bytes']/1048576:.1f} MiB | {r['overfull_hbox_warnings']} | {r['missing_glyph_warnings']} | {len(r['missing_chapter_titles'])} |")
    lines += ["",
              f"- Unresolved image assets: **{sum(len(r['missing_images']) for r in results)}**",
              f"- Hard publication findings: **{len(hard)}**",
              "",
              "## Render sample checks",""]
    for r in results:
        lines.append(f"- **{r['route']}:** "+", ".join(f"p{x['page']} mean/std {x['mean_gray']}/{x['std_gray']}" for x in r['render_samples']))
    if hard:
        lines += ["","## Hard findings",""]
        lines += [f"- {x}" for x in hard]
    else:
        lines += ["","## Result","","**PASS** - no hard structural/rendering publication defects detected."]
    (outdir/"publishing-validation.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("\n".join(lines))
    if hard:
        raise RuntimeError("Hard publication findings remain")
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--route", choices=list(ROUTES))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--render", action="store_true", help="Build and validate route PDFs after preflight")
    args = ap.parse_args()
    if args.all or not args.route:
        results=all_preflight()
        if args.render:
            render_all(results)
    else:
        info=assemble(args.route)
        print(json.dumps(info, indent=2))
        if args.render:
            render_and_validate(info)

if __name__ == "__main__":
    main()
