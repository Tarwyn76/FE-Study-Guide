#!/usr/bin/env python3
# Chemical source-boundary repair workflow entry point.
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
FILES=[
"03-01-Material-and-Energy-Balances-Single-Units-and-Process-Flowsheets.md",
"03-07-Absorption-Extraction-Adsorption-and-Membrane-Separations.md",
"03-08-Humidification-Drying-and-Evaporation.md",
"03-12-Process-Flow-Diagrams-P-IDs-Equipment-Sizing-Scale-Up-and-Cost-Estimation.md",
"03-13-Process-Optimization-Advanced-Control-and-Process-Safety.md",
]
BOUNDARY="""### Source Boundary

- **FE-Handbook-supported** — Equations, definitions, tables, and relations explicitly identified in this Handbook section are supported by the cited FE Reference Handbook location recorded for the chapter/concept.
- **Externally supported** — Material extending beyond the Handbook is supported by the external-source provenance recorded in the concept ledger and the Chemical Track References and Sources register.
- **Guide synthesis** — Explanatory sequencing, worked-example framing, exam-navigation advice, and connections among separately sourced concepts are guide-developed synthesis unless separately attributed.

"""
for fn in FILES:
    p=ROOT/"layer-3-tracks"/"chemical"/fn
    text=p.read_text(encoding="utf-8")
    m=re.search(r"(?mi)^##\s+As the Handbook States It\s*$",text)
    if not m: raise RuntimeError(f"missing Handbook section: {fn}")
    nxt=re.search(r"(?m)^##\s+",text[m.end():])
    end=m.end()+nxt.start() if nxt else len(text)
    section=text[m.end():end]
    if "FE-Handbook-supported" in section and "Externally supported" in section and "Guide synthesis" in section:
        print("already",fn); continue
    insert=end
    text=text[:insert]+("\n\n"+BOUNDARY)+text[insert:]
    p.write_text(text,encoding="utf-8")
    print("updated",fn)
