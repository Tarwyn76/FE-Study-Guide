#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, subprocess, sys, zipfile
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parents[1]

class H(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.hrefs=[]; self.imgs=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        if tag=="a" and "href" in a: self.hrefs.append(a["href"])
        if tag=="img" and "src" in a: self.imgs.append(a["src"])

def cmd(args):
    return subprocess.run(args,capture_output=True,text=True,check=False)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--route",required=True)
    ap.add_argument("--pdf",required=True)
    ap.add_argument("--epub",required=True)
    ap.add_argument("--html",required=True)
    args=ap.parse_args()
    pdf=ROOT/args.pdf; epub=ROOT/args.epub; html=ROOT/args.html
    failures=[]; result={"route":args.route}

    if not pdf.exists() or pdf.stat().st_size<10000: failures.append("PDF missing or implausibly small")
    else:
        p=cmd(["pdfinfo",str(pdf)])
        result["pdfinfo"]=p.stdout
        m=re.search(r"(?m)^Pages:\s+(\d+)",p.stdout)
        result["pdf_pages"]=int(m.group(1)) if m else None
        t=cmd(["pdftotext",str(pdf),"-"])
        result["pdf_text_chars"]=len(t.stdout)
        for token in ("FE Supplemental Study Guide","Table of Contents","Practice Exam"):
            if token.lower() not in t.stdout.lower(): failures.append(f"PDF text missing expected token: {token}")

    if not epub.exists() or epub.stat().st_size<10000: failures.append("EPUB missing or implausibly small")
    else:
        try:
            with zipfile.ZipFile(epub) as z:
                names=z.namelist()
                result["epub_entries"]=len(names)
                if "mimetype" not in names: failures.append("EPUB missing mimetype")
                if not any(n.lower().endswith((".xhtml",".html")) for n in names): failures.append("EPUB has no XHTML/HTML content")
        except Exception as e: failures.append("EPUB unreadable: "+repr(e))

    if not html.exists() or html.stat().st_size<10000: failures.append("HTML missing or implausibly small")
    else:
        h=H(); h.feed(html.read_text(encoding="utf-8",errors="ignore"))
        broken=[x for x in h.hrefs if x.startswith("#") and x[1:] and x[1:] not in h.ids]
        result["html_ids"]=len(h.ids); result["html_links"]=len(h.hrefs)
        result["html_images"]=len(h.imgs); result["broken_internal_links"]=broken[:100]
        if broken: failures.append(f"HTML contains {len(broken)} broken internal anchors")

    result["failures"]=failures
    out=pdf.parent/f"fe-study-guide-{args.route}-publication-validation.json"
    out.write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
    if failures: sys.exit(1)

if __name__=="__main__": main()
