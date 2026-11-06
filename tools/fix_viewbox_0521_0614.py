#!/usr/bin/env python3
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ("0521", "FIG-02-39-007"),
    ("0614", "FIG-02-53-002"),
]
PAD = 24.0  # pt on every side

for idx, stem in FILES:
    svg_path = ROOT / "figures" / "svg" / f"{idx}_{stem}.svg"
    png_path = ROOT / "figures" / "png" / f"{idx}_{stem}.png"

    tree = ET.parse(svg_path)
    root = tree.getroot()

    vb = [float(x) for x in root.attrib["viewBox"].replace(",", " ").split()]
    x, y, w, h = vb
    nx, ny = x - PAD, y - PAD
    nw, nh = w + 2 * PAD, h + 2 * PAD

    root.set("viewBox", f"{nx:.6f} {ny:.6f} {nw:.6f} {nh:.6f}")
    root.set("width", f"{nw:.6f}pt")
    root.set("height", f"{nh:.6f}pt")

    tree.write(svg_path, encoding="utf-8", xml_declaration=True)

    svg_bytes = svg_path.read_bytes()
    cairosvg.svg2png(
        bytestring=svg_bytes,
        write_to=str(png_path),
        output_width=3600,
        background_color="#ffffff",
    )

    print(f"{idx}: {x:g} {y:g} {w:g} {h:g} -> {nx:g} {ny:g} {nw:g} {nh:g}")
