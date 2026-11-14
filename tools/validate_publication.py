#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, subprocess, sys, zipfile, tempfile
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parents[1]

class H(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.hrefs=[]; self.imgs=[]; self.headings=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        if tag=="a" and "href" in a: self.hrefs.append(a["href"])
        if tag=="img" and "src" in a: self.imgs.append(a["src"])
        if tag in ("h1","h2","h3"): self.headings.append(tag)

def cmd(args):
    return subprocess.run(args,capture_output=True,text=True,check=False)

def bbox_margins(pdf):
    p=cmd(["pdftotext","-bbox",str(pdf),"-"])
    if p.returncode != 0:
        return None, "pdftotext -bbox failed"
    page_re=re.compile(r'<page width="([0-9.]+)" height="([0-9.]+)">([\s\S]*?)</page>')
    word_re=re.compile(r'<word xMin="([0-9.]+)" yMin="([0-9.]+)" xMax="([0-9.]+)" yMax="([0-9.]+)"')
    per=[]
    for pm in page_re.finditer(p.stdout):
        w=float(pm.group(1)); h=float(pm.group(2)); words=word_re.findall(pm.group(3))
        if not words: continue
        vals=[tuple(map(float,x)) for x in words]
        per.append({
            "width":w,"height":h,
            "left":min(x[0] for x in vals),
            "top":min(x[1] for x in vals),
            "right":min(w-x[2] for x in vals),
            "bottom":min(h-x[3] for x in vals),
        })
    if not per: return None, "no PDF text boxes found"
    return {
        "pages_measured":len(per),
        "min_left_pt":round(min(x["left"] for x in per),2),
        "min_top_pt":round(min(x["top"] for x in per),2),
        "min_right_pt":round(min(x["right"] for x in per),2),
        "min_bottom_pt":round(min(x["bottom"] for x in per),2),
    }, None

def font_embedding(pdf):
    p=cmd(["pdffonts",str(pdf)])
    if p.returncode != 0: return [], ["pdffonts failed"]
    rows=[]
    bad=[]
    lines=p.stdout.splitlines()[2:]
    for line in lines:
        if not line.strip(): continue
        cols=line.split()
        # pdffonts columns end with emb sub uni object ID
        if len(cols) >= 7:
            emb=cols[-5] if len(cols)>=8 else ""
            rows.append(line.strip())
            if emb.lower()!="yes": bad.append(line.strip())
    return rows,bad

def grayscale_samples(pdf,pages):
    out=[]
    with tempfile.TemporaryDirectory() as td:
        for pg in sorted(set(pages)):
            prefix=Path(td)/f"page-{pg}"
            p=cmd(["pdftoppm","-f",str(pg),"-l",str(pg),"-singlefile","-gray","-png","-r","90",str(pdf),str(prefix)])
            img=prefix.with_suffix(".png")
            out.append({"page":pg,"ok":p.returncode==0 and img.exists() and img.stat().st_size>2000,
                        "bytes":img.stat().st_size if img.exists() else 0})
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--route",required=True)
    ap.add_argument("--pdf",required=True)
    ap.add_argument("--epub",required=True)
    ap.add_argument("--html",required=True)
    args=ap.parse_args()
    pdf=ROOT/args.pdf; epub=ROOT/args.epub; html=ROOT/args.html
    failures=[]; warnings=[]; result={"route":args.route}

    if not pdf.exists() or pdf.stat().st_size<10000:
        failures.append("PDF missing or implausibly small")
    else:
        p=cmd(["pdfinfo",str(pdf)])
        result["pdfinfo"]=p.stdout
        m=re.search(r"(?m)^Pages:\s+(\d+)",p.stdout)
        pages=int(m.group(1)) if m else None
        result["pdf_pages"]=pages
        sm=re.search(r"(?m)^Page size:\s+([0-9.]+) x ([0-9.]+) pts",p.stdout)
        if sm:
            pw,ph=map(float,sm.groups()); result["page_size_pt"]=[pw,ph]
            if abs(pw-612)>5 or abs(ph-792)>5:
                failures.append(f"PDF page size is not US Letter: {pw} x {ph} pt")
        else:
            warnings.append("Could not parse PDF page size")

        t=cmd(["pdftotext",str(pdf),"-"])
        text=t.stdout
        result["pdf_text_chars"]=len(text)
        required=("FE Supplemental Study Guide","Table of Contents","Practice Exam","Formula Index","Notation Master","References")
        missing=[token for token in required if token.lower() not in text.lower()]
        result["missing_expected_tokens"]=missing
        if missing: failures.append("PDF text missing expected sections: "+", ".join(missing))

        raw_tex=re.findall(r"\\(?:frac|dfrac|tfrac|boxed|begin|end|left|right|text|sqrt|sum|int)\b|\$\$",text)
        result["raw_tex_leak_count"]=len(raw_tex)
        if raw_tex: failures.append(f"PDF contains {len(raw_tex)} raw TeX/math tokens")

        margins,err=bbox_margins(pdf)
        result["text_margins"]=margins
        if err: warnings.append(err)
        elif min(margins["min_left_pt"],margins["min_right_pt"],margins["min_top_pt"],margins["min_bottom_pt"]) < 8:
            failures.append("PDF text approaches/clips a page edge (<8 pt clearance)")

        fonts,badfonts=font_embedding(pdf)
        result["pdf_font_rows"]=len(fonts); result["unembedded_fonts"]=badfonts
        if badfonts: failures.append(f"PDF has {len(badfonts)} unembedded font(s)")

        if pages:
            sample_pages=[1,max(1,pages//4),max(1,pages//2),max(1,(3*pages)//4),pages]
            gs=grayscale_samples(pdf,sample_pages)
            result["grayscale_samples"]=gs
            if not all(x["ok"] for x in gs): failures.append("One or more representative pages failed grayscale rasterization")

    if not epub.exists() or epub.stat().st_size<10000:
        failures.append("EPUB missing or implausibly small")
    else:
        try:
            with zipfile.ZipFile(epub) as z:
                names=z.namelist()
                result["epub_entries"]=len(names)
                if "mimetype" not in names: failures.append("EPUB missing mimetype")
                if not any(n.lower().endswith((".xhtml",".html")) for n in names): failures.append("EPUB has no XHTML/HTML content")
                bad_images=[n for n in names if n.lower().endswith((".png",".jpg",".jpeg",".svg")) and z.getinfo(n).file_size==0]
                result["epub_zero_byte_images"]=bad_images
                if bad_images: failures.append(f"EPUB has {len(bad_images)} zero-byte image assets")
        except Exception as e:
            failures.append("EPUB unreadable: "+repr(e))

    if not html.exists() or html.stat().st_size<10000:
        failures.append("HTML missing or implausibly small")
    else:
        h=H(); h.feed(html.read_text(encoding="utf-8",errors="ignore"))
        broken=[x for x in h.hrefs if x.startswith("#") and x[1:] and x[1:] not in h.ids]
        result["html_ids"]=len(h.ids); result["html_links"]=len(h.hrefs)
        result["html_images"]=len(h.imgs); result["broken_internal_links"]=broken[:100]
        result["html_heading_count"]=len(h.headings)
        if broken: failures.append(f"HTML contains {len(broken)} broken internal anchors")
        if len(h.imgs)==0: failures.append("HTML contains no images")

    result["warnings"]=warnings
    result["failures"]=failures
    out=pdf.parent/f"fe-study-guide-{args.route}-publication-validation.json"
    out.write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
    if failures: sys.exit(1)

if __name__=="__main__":
    main()
