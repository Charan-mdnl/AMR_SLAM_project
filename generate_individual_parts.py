#!/usr/bin/env python3
"""
Generate individual PNG part drawings for each component.
Each PNG has: FRONT VIEW, SIDE VIEW, TOP VIEW (where applicable),
with proper dimension lines, material callouts, tolerances.
Dimensions scaled from Tusk E10 reference for 1200x1000mm chassis.
"""
import os, subprocess

brain = "/home/charan/.gemini/antigravity-ide/brain/4ac556db-d1f1-449a-b470-f85aafe800fc"
doc = "/home/charan/Documents/tusk-amr-files"
os.makedirs(doc, exist_ok=True)

PW, PH = 1800, 1200  # Per-part image size


def dim_h(x1, y1, x2, label, off=25, col="#e11d48", fs=14):
    """Horizontal dimension line with arrows."""
    yo = y1 + off
    s = ""
    s += f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="{yo+4}" stroke="{col}" stroke-width="0.7" stroke-dasharray="3,2"/>'
    s += f'<line x1="{x2}" y1="{y1}" x2="{x2}" y2="{yo+4}" stroke="{col}" stroke-width="0.7" stroke-dasharray="3,2"/>'
    s += f'<line x1="{x1}" y1="{yo}" x2="{x2}" y2="{yo}" stroke="{col}" stroke-width="1.3"/>'
    s += f'<polygon points="{x1},{yo} {x1+7},{yo-3} {x1+7},{yo+3}" fill="{col}"/>'
    s += f'<polygon points="{x2},{yo} {x2-7},{yo-3} {x2-7},{yo+3}" fill="{col}"/>'
    mx = (x1 + x2) / 2
    s += f'<text x="{mx}" y="{yo-5}" fill="{col}" font-size="{fs}" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">{label}</text>'
    return s


def dim_v(x1, y1, y2, label, off=25, col="#1e3a5f", fs=14):
    """Vertical dimension line with arrows."""
    xo = x1 + off
    s = ""
    s += f'<line x1="{x1}" y1="{y1}" x2="{xo+4}" y2="{y1}" stroke="{col}" stroke-width="0.7" stroke-dasharray="3,2"/>'
    s += f'<line x1="{x1}" y1="{y2}" x2="{xo+4}" y2="{y2}" stroke="{col}" stroke-width="0.7" stroke-dasharray="3,2"/>'
    s += f'<line x1="{xo}" y1="{y1}" x2="{xo}" y2="{y2}" stroke="{col}" stroke-width="1.3"/>'
    s += f'<polygon points="{xo},{y1} {xo-3},{y1+7} {xo+3},{y1+7}" fill="{col}"/>'
    s += f'<polygon points="{xo},{y2} {xo-3},{y2-7} {xo+3},{y2-7}" fill="{col}"/>'
    my = (y1 + y2) / 2
    s += f'<text x="{xo+6}" y="{my+5}" fill="{col}" font-size="{fs}" font-family="Arial,sans-serif" font-weight="bold">{label}</text>'
    return s


def border(title, subtitle, material, qty):
    """Standard drawing border with title block."""
    return f"""<svg width="{PW}" height="{PH}" xmlns="http://www.w3.org/2000/svg">
<rect width="{PW}" height="{PH}" fill="white"/>
<rect x="8" y="8" width="{PW-16}" height="{PH-16}" fill="none" stroke="#1e3a5f" stroke-width="3.5"/>
<rect x="12" y="12" width="{PW-24}" height="{PH-24}" fill="none" stroke="#1e3a5f" stroke-width="1.2"/>
<!-- Title block top -->
<rect x="12" y="12" width="{PW-24}" height="55" fill="#1e3a5f"/>
<text x="{PW/2}" y="40" fill="white" font-size="22" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">{title}</text>
<text x="{PW/2}" y="60" fill="#93c5fd" font-size="14" font-family="Arial,sans-serif" text-anchor="middle">{subtitle}</text>
<!-- Material & Qty -->
<text x="30" y="88" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold">Material: {material}    |    QTY: {qty}    |    All dims in mm    |    Tolerances: ±0.5 mm unless noted</text>
<line x1="12" y1="95" x2="{PW-12}" y2="95" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Title block bottom -->
<rect x="{PW-350}" y="{PH-50}" width="338" height="38" fill="#1e3a5f"/>
<text x="{PW-180}" y="{PH-25}" fill="white" font-size="13" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">USER CUSTOM AMR | SCALE: NTS | JULY 2026</text>
"""


def save_svg_as_png(name, svg_content):
    svg_path = f"/tmp/{name}.svg"
    png_path = f"/tmp/{name}.png"
    with open(svg_path, "w") as f:
        f.write(svg_content)
    subprocess.run(f"rsvg-convert -w {PW} -h {PH} {svg_path} -o {png_path}", shell=True)
    for d in [brain, doc]:
        subprocess.run(f"cp {png_path} {os.path.join(d, f'{name}.png')}", shell=True)
    sz = os.path.getsize(png_path)
    print(f"  -> {name}.png ({sz} bytes)")


# =================================================================
# PART 01: BASE FRAME (WELDMENT)
# =================================================================
print("Part 01: Base Frame...")
svg = border("PART 01 — BASE FRAME (WELDMENT)", "Low Profile Pallet AMR — 1000 kg Payload", "Q235 Steel | Tube: 80×60×4 mm | Plate: 8 mm | All welds 6 mm fillet", "1")

# FRONT VIEW (looking at the 1000mm width face)
svg += '<text x="400" y="135" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW (Width = 1000 mm)</text>'
svg += '<g transform="translate(60, 150)">'
# Scale: 1000mm -> 680px (0.68 factor)
# Overall outer frame
svg += '<rect x="0" y="0" width="680" height="116" fill="none" stroke="#1e3a5f" stroke-width="3"/>'
# Left pod (300mm = 204px)
svg += '<rect x="0" y="0" width="204" height="116" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
# Fork channel 1 (200mm = 136px) - open slot
svg += '<rect x="204" y="12" width="136" height="92" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="272" y="65" fill="#888" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">FORK</text>'
svg += '<text x="272" y="80" fill="#888" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">CHANNEL 1</text>'
# Center bridge pod (300mm = 204px)
svg += '<rect x="340" y="0" width="204" height="116" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
# Fork channel 2 (200mm = 136px)
svg += '<rect x="544" y="12" width="136" height="92" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="612" y="65" fill="#888" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">FORK</text>'
svg += '<text x="612" y="80" fill="#888" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">CHANNEL 2</text>'
# Tube cross-sections on frame edges
svg += '<rect x="0" y="0" width="10" height="116" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<rect x="194" y="0" width="10" height="116" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<rect x="340" y="0" width="10" height="116" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<rect x="534" y="0" width="10" height="116" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<rect x="670" y="0" width="10" height="116" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1"/>'
# Dimensions
svg += dim_h(0, 116, 204, "300", 20)
svg += dim_h(204, 116, 340, "200", 20)
svg += dim_h(340, 116, 544, "300", 20)
svg += dim_h(544, 116, 680, "200", 20)
svg += dim_h(0, 116, 680, "1000 (Total Width)", 48)
svg += dim_v(680, 0, 116, "170", 20)
svg += dim_v(204, 12, 104, "146 (Channel H)", 20, "#e11d48")
svg += dim_h(204, 12, 340, "200 (Channel W)", -20, "#e11d48")
svg += '</g>'

# SIDE VIEW (looking at the 1200mm length face)
svg += '<text x="400" y="360" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (Length = 1200 mm)</text>'
svg += '<g transform="translate(60, 375)">'
# Scale: 1200mm -> 680px (0.567 factor)
svg += '<rect x="0" y="0" width="680" height="116" fill="none" stroke="#1e3a5f" stroke-width="3"/>'
# Fork channel opening from front (1000mm = 567px)
svg += '<rect x="0" y="12" width="567" height="92" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="283" y="65" fill="#888" font-size="13" font-family="Arial,sans-serif" text-anchor="middle">FORK CHANNEL (Open Front)</text>'
# Rear solid bridge (200mm = 113px)
svg += '<rect x="567" y="0" width="113" height="116" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="623" y="65" fill="#888" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">REAR</text>'
svg += '<text x="623" y="80" fill="#888" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">BRIDGE</text>'
# Tube edges
svg += '<rect x="0" y="0" width="680" height="8" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<rect x="0" y="108" width="680" height="8" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1"/>'
# Dims
svg += dim_h(0, 116, 567, "1000 (Fork Depth)", 20)
svg += dim_h(567, 116, 680, "200", 20)
svg += dim_h(0, 116, 680, "1200 (Total Length)", 48)
svg += dim_v(680, 0, 116, "170", 20)
svg += dim_v(0, 0, 8, "8 (Plate)", -50, "#e11d48", 11)
svg += '</g>'

# TOP VIEW
svg += '<text x="400" y="570" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">TOP VIEW</text>'
svg += '<g transform="translate(60, 585)">'
# Scale: 1200mm -> 600px, 1000mm -> 500px
svg += '<rect x="0" y="0" width="600" height="500" fill="none" stroke="#1e3a5f" stroke-width="3"/>'
# Left pod
svg += '<rect x="0" y="0" width="150" height="500" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="1.5"/>'
# Channel 1
svg += '<rect x="150" y="0" width="100" height="416" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="200" y="220" fill="#aaa" font-size="14" font-family="Arial,sans-serif" text-anchor="middle" transform="rotate(-90,200,220)">FORK CHANNEL 1 (Open Front)</text>'
# Center bridge
svg += '<rect x="250" y="0" width="150" height="500" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="1.5"/>'
# Channel 2
svg += '<rect x="400" y="0" width="100" height="416" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="450" y="220" fill="#aaa" font-size="14" font-family="Arial,sans-serif" text-anchor="middle" transform="rotate(-90,450,220)">FORK CHANNEL 2 (Open Front)</text>'
# Right extension (last 100px of width = 200mm... wait that's already accounted for)
# Rear bridge
svg += '<rect x="0" y="416" width="600" height="84" fill="#dbeafe" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="300" y="465" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" text-anchor="middle">REAR SOLID BRIDGE (200 mm)</text>'

# Hub motor positions (center of each side pod, Y=250 = midway)
svg += '<circle cx="75" cy="250" r="20" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="75" y="255" fill="white" font-size="9" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">HUB M</text>'
svg += '<circle cx="525" cy="250" r="20" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="525" y="255" fill="white" font-size="9" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">HUB M</text>'

# Corner casters
for cx, cy in [(30, 25), (30, 475), (570, 25), (570, 475)]:
    svg += f'<rect x="{cx-12}" y="{cy-12}" width="24" height="24" fill="#4ade80" stroke="#1e3a5f" stroke-width="1.5"/>'
    svg += f'<text x="{cx}" y="{cy+4}" fill="#0f172a" font-size="8" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">CW</text>'

# Dims
svg += dim_h(0, 500, 150, "300", 20, "#e11d48", 13)
svg += dim_h(150, 500, 250, "200", 20, "#e11d48", 13)
svg += dim_h(250, 500, 400, "300", 20, "#e11d48", 13)
svg += dim_h(400, 500, 500, "200", 20, "#e11d48", 13)
svg += dim_h(0, 500, 600, "1000 (Width)", 48, "#1e3a5f", 15)
svg += dim_v(600, 0, 500, "1200 (Length)", 20, "#1e3a5f", 15)
svg += dim_v(600, 416, 500, "200", 60, "#e11d48", 13)
svg += dim_v(600, 0, 416, "1000 (Fork Depth)", 100, "#e11d48", 13)
svg += '</g>'

svg += '</svg>'
save_svg_as_png("PART_01_BASE_FRAME", svg)


# =================================================================
# PART 02: TOP PLATFORM (FORK PLATE)
# =================================================================
print("Part 02: Fork Plate...")
svg = border("PART 02 — TOP PLATFORM (FORK PLATE)", "Fits inside 200 mm fork channel — lifts pallet", "Q235 Steel | Plate: 6 mm", "2 (Left and Right Channels)")

# TOP VIEW
svg += '<text x="500" y="135" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">TOP VIEW</text>'
svg += '<g transform="translate(60, 150)">'
svg += '<rect x="0" y="0" width="750" height="143" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2.5"/>'
# Mounting holes (4 pairs along length)
for x in [40, 250, 500, 710]:
    svg += f'<circle cx="{x}" cy="30" r="6" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
    svg += f'<circle cx="{x}" cy="113" r="6" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="740" y="30" fill="#555" font-size="11" font-family="Arial,sans-serif">Ø11 THRU (8x)</text>'
svg += dim_h(0, 143, 750, "1000 (Fork Length)", 25)
svg += dim_v(750, 0, 143, "190 (Fork Width)", 25)
# Hole spacing dims
svg += dim_h(40, 0, 710, "920 (Hole Pitch L)", -22, "#888", 11)
svg += dim_h(0, 0, 40, "40", -22, "#888", 10)
svg += dim_v(0, 0, 30, "30", -40, "#888", 10)
svg += '</g>'

# SIDE VIEW
svg += '<text x="500" y="375" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>'
svg += '<g transform="translate(60, 395)">'
svg += '<rect x="0" y="0" width="750" height="8" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>'
svg += dim_h(0, 8, 750, "1000", 20)
svg += dim_v(750, 0, 8, "6 (Plate Thick)", 25, "#e11d48", 13)
svg += '</g>'

# FRONT VIEW (end view)
svg += '<text x="500" y="490" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW (End View)</text>'
svg += '<g transform="translate(250, 510)">'
svg += '<rect x="0" y="0" width="286" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="30" cy="6" r="5" fill="none" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<circle cx="256" cy="6" r="5" fill="none" stroke="#1e3a5f" stroke-width="1"/>'
svg += dim_h(0, 12, 286, "190", 20)
svg += dim_v(286, 0, 12, "6", 15, "#e11d48", 12)
svg += '</g>'

# ASSEMBLY CONTEXT
svg += '<text x="500" y="620" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">ASSEMBLY FIT REFERENCE</text>'
svg += '<g transform="translate(200, 640)">'
svg += '<rect x="0" y="0" width="600" height="100" fill="none" stroke="#aaa" stroke-width="1.5" stroke-dasharray="8,4"/>'
svg += '<text x="300" y="20" fill="#aaa" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">Base Frame Channel Cross-Section</text>'
# Channel walls
svg += '<rect x="0" y="0" width="8" height="100" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<rect x="242" y="0" width="8" height="100" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="1"/>'
svg += dim_h(0, 100, 250, "200 (Channel)", 15, "#888", 12)
# Fork plate inside channel
svg += '<rect x="5" y="70" width="240" height="8" fill="#fef3c7" stroke="#e11d48" stroke-width="2"/>'
svg += '<text x="125" y="65" fill="#e11d48" font-size="12" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">Fork Plate (190 mm) → 5 mm clearance each side</text>'
svg += dim_h(5, 78, 245, "190", 15, "#e11d48", 12)
svg += '</g>'

# NOTES
svg += '<text x="60" y="830" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold">NOTES:</text>'
svg += '<text x="60" y="850" fill="#555" font-size="12" font-family="Arial,sans-serif">1. Fork plate slides up/down inside 200 mm channel, lifted by scissor mechanism.</text>'
svg += '<text x="60" y="870" fill="#555" font-size="12" font-family="Arial,sans-serif">2. 8x Ø11 mounting holes match scissor arm pivot pin locations.</text>'
svg += '<text x="60" y="890" fill="#555" font-size="12" font-family="Arial,sans-serif">3. Bottom surface must be flat — contact face with scissor arm top ends.</text>'

svg += '</svg>'
save_svg_as_png("PART_02_FORK_PLATE", svg)


# =================================================================
# PART 03: SCISSOR ARM
# =================================================================
print("Part 03: Scissor Arm...")
svg = border("PART 03 — SCISSOR ARM", "Rectangular tube X-linkage arm — forms scissor lift mechanism", "Q235 Steel | Rectangular Tube 60×40×6 mm", "4 pcs (2 per scissor set × 2 sets)")

# TOP VIEW (plan view of single arm)
svg += '<text x="500" y="135" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW (Single Arm)</text>'
svg += '<g transform="translate(80, 160)">'
svg += '<rect x="0" y="0" width="680" height="48" rx="24" fill="#dcfce7" stroke="#1e3a5f" stroke-width="2.5"/>'
# 3 pivot holes
svg += '<circle cx="34" cy="24" r="14" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="340" cy="24" r="14" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="646" cy="24" r="14" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="34" y="29" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø20</text>'
svg += '<text x="340" y="29" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø20</text>'
svg += '<text x="646" y="29" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø20</text>'
# Dims
svg += dim_h(0, 48, 680, "760 (Overall Length)", 25)
svg += dim_h(34, 48, 646, "720 (Cut Length / Hole C-C)", 55)
svg += dim_h(34, 48, 340, "360 (Half Pitch)", 85, "#888", 12)
svg += dim_v(680, 0, 48, "60 (Tube Height)", 25)
svg += '<text x="30" y="80" fill="#555" font-size="12" font-family="Arial,sans-serif">Ø20 H7 (3 holes)</text>'
svg += '</g>'

# SIDE VIEW (tube cross-section)
svg += '<text x="300" y="380" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (Tube Section)</text>'
svg += '<g transform="translate(200, 400)">'
svg += '<rect x="0" y="0" width="80" height="120" fill="#dcfce7" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<rect x="12" y="12" width="56" height="96" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="40" y="65" fill="#888" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">THK 6</text>'
svg += dim_h(0, 120, 80, "40", 20)
svg += dim_v(80, 0, 120, "60", 20)
svg += '</g>'

# TOP VIEW (plan of tube)
svg += '<text x="700" y="380" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">TOP VIEW</text>'
svg += '<g transform="translate(400, 400)">'
svg += '<rect x="0" y="0" width="540" height="64" fill="#dcfce7" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="30" cy="32" r="12" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<circle cx="270" cy="32" r="12" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<circle cx="510" cy="32" r="12" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += dim_h(0, 64, 540, "760", 20, "#888", 12)
svg += dim_v(540, 0, 64, "40", 15, "#888", 12)
svg += '</g>'

# SCISSOR X-PATTERN (assembly context)
svg += '<text x="900" y="580" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SCISSOR X-PATTERN (Assembly Ref.)</text>'
svg += '<g transform="translate(600, 600)">'
svg += '<line x1="0" y1="0" x2="600" y2="200" stroke="#16a34a" stroke-width="4"/>'
svg += '<line x1="600" y1="0" x2="0" y2="200" stroke="#dc2626" stroke-width="4"/>'
svg += '<circle cx="300" cy="100" r="10" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="0" cy="0" r="8" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="600" cy="0" r="8" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="0" cy="200" r="8" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="600" cy="200" r="8" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="300" y="135" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" text-anchor="middle">Center Pivot Pin</text>'
svg += '<text x="0" y="-15" fill="#16a34a" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">Fixed End</text>'
svg += '<text x="600" y="-15" fill="#dc2626" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">Sliding End</text>'
svg += '</g>'

# NOTES
svg += '<text x="60" y="680" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold">NOTES:</text>'
svg += '<text x="60" y="700" fill="#555" font-size="12" font-family="Arial,sans-serif">1. Two arms form one X-linkage. One arm is mirror (Part 4).</text>'
svg += '<text x="60" y="720" fill="#555" font-size="12" font-family="Arial,sans-serif">2. Center hole = pivot point. End holes connect to base frame (fixed) and fork plate (sliding).</text>'
svg += '<text x="60" y="740" fill="#555" font-size="12" font-family="Arial,sans-serif">3. All 3 holes: Ø20 H7 reamed. Insert bronze bushes (Part 6) and cross pins (Part 5).</text>'
svg += '<text x="60" y="760" fill="#555" font-size="12" font-family="Arial,sans-serif">4. Sliding end rides in horizontal slot machined in base frame rail. Slot width: 22 mm.</text>'

svg += '</svg>'
save_svg_as_png("PART_03_SCISSOR_ARM", svg)


# =================================================================
# PART 05: CROSS PIN + PART 06: PIVOT BUSH
# =================================================================
print("Part 05-06: Cross Pin + Pivot Bush...")
svg = border("PARTS 05 & 06 — CROSS PIN (PIVOT) + PIVOT BUSH", "Pivot hardware for scissor linkage joints", "Part 5: EN8 Steel | Part 6: Bronze CuSn12", "Part 5: 12 pcs | Part 6: 12 pcs")

# CROSS PIN
svg += '<text x="450" y="135" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 05: CROSS PIN (PIVOT)</text>'

svg += '<text x="350" y="180" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>'
svg += '<g transform="translate(80, 200)">'
svg += '<rect x="0" y="0" width="540" height="40" rx="20" fill="#fed7aa" stroke="#1e3a5f" stroke-width="2.5"/>'
# Shoulder detail
svg += '<rect x="20" y="5" width="500" height="30" fill="#f59e0b" stroke="#1e3a5f" stroke-width="1"/>'
svg += dim_h(0, 40, 540, "140", 25)
svg += dim_h(20, 40, 520, "120 (Shoulder Length)", 55, "#888", 12)
svg += dim_v(540, 0, 40, "Ø20 h6", 25)
svg += '</g>'

svg += '<text x="900" y="180" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (End)</text>'
svg += '<g transform="translate(840, 200)">'
svg += '<circle cx="40" cy="20" r="20" fill="#fed7aa" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<circle cx="40" cy="20" r="3" fill="#1e3a5f"/>'
svg += '<text x="75" y="25" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif">Ø20 h6</text>'
svg += '</g>'

# PIVOT BUSH
svg += '<line x1="30" y1="350" x2="{0}" y2="350" stroke="#ccc" stroke-width="1.5"/>'.format(PW-30)
svg += '<text x="450" y="390" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 06: PIVOT BUSH</text>'

svg += '<text x="250" y="435" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>'
svg += '<g transform="translate(80, 455)">'
svg += '<rect x="0" y="0" width="200" height="60" rx="10" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<rect x="10" y="10" width="180" height="40" fill="#f59e0b" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<text x="100" y="35" fill="white" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">BORE Ø20 H7</text>'
svg += dim_h(0, 60, 200, "25 (Length)", 25)
svg += dim_v(200, 0, 60, "Ø25 h6 (OD)", 25)
svg += '</g>'

svg += '<text x="600" y="435" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (End)</text>'
svg += '<g transform="translate(530, 455)">'
svg += '<circle cx="45" cy="30" r="30" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<circle cx="45" cy="30" r="14" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="90" y="20" fill="#1e3a5f" font-size="13" font-family="Arial,sans-serif">OD: Ø25 h6</text>'
svg += '<text x="90" y="40" fill="#e11d48" font-size="13" font-family="Arial,sans-serif">ID: Ø20 H7</text>'
svg += '</g>'

# FIT DIAGRAM
svg += '<text x="450" y="600" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">ASSEMBLY FIT: Pin → Bush → Scissor Arm Bore</text>'
svg += '<g transform="translate(200, 620)">'
svg += '<rect x="0" y="0" width="500" height="80" fill="none" stroke="#aaa" stroke-width="1.5" stroke-dasharray="5,3"/>'
# Arm bore
svg += '<rect x="180" y="0" width="140" height="80" fill="#dcfce7" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="250" y="20" fill="#1e3a5f" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">Scissor Arm Bore</text>'
# Bush inside bore
svg += '<rect x="195" y="10" width="110" height="60" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="250" y="40" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Bush Ø25/Ø20</text>'
# Pin inside bush
svg += '<rect x="210" y="20" width="80" height="40" rx="20" fill="#fed7aa" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="250" y="45" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Pin Ø20</text>'
svg += '</g>'

svg += '</svg>'
save_svg_as_png("PART_05_06_PIN_BUSH", svg)


# =================================================================
# PART 07: BALL SCREW + PART 08: BALL NUT
# =================================================================
print("Part 07-08: Ball Screw + Nut...")
svg = border("PARTS 07 & 08 — BALL SCREW + BALL NUT HOUSING", "Drives scissor mechanism horizontal actuation", "Part 7: SCM415 | Part 8: Steel Housing", "Part 7: 2 pcs | Part 8: 2 pcs")

svg += '<text x="500" y="140" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 07: BALL SCREW — FRONT VIEW</text>'
svg += '<g transform="translate(80, 170)">'
# Screw shaft
svg += '<rect x="0" y="20" width="900" height="20" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2"/>'
# Thread pattern lines
for i in range(0, 900, 20):
    svg += f'<line x1="{i}" y1="20" x2="{i+10}" y2="40" stroke="#999" stroke-width="0.8"/>'
# End journals
svg += '<rect x="-10" y="15" width="30" height="30" rx="3" fill="#9ca3af" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<rect x="880" y="15" width="30" height="30" rx="3" fill="#9ca3af" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += dim_h(0, 40, 900, "600 (Screw Length)", 25)
svg += dim_v(900, 20, 40, "Ø16", 20)
svg += '<text x="450" y="15" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" text-anchor="middle">Lead: 5 mm | Type: C7 | Material: SCM415</text>'
svg += '</g>'

svg += '<text x="200" y="310" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (End)</text>'
svg += '<g transform="translate(120, 330)">'
svg += '<circle cx="40" cy="40" r="12" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="40" cy="40" r="3" fill="#1e3a5f"/>'
svg += '<text x="65" y="45" fill="#1e3a5f" font-size="13" font-family="Arial,sans-serif">Ø16</text>'
svg += '</g>'

# BALL NUT
svg += '<line x1="30" y1="440" x2="{0}" y2="440" stroke="#ccc" stroke-width="1.5"/>'.format(PW-30)
svg += '<text x="500" y="480" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 08: BALL NUT + HOUSING</text>'

svg += '<text x="250" y="520" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>'
svg += '<g transform="translate(100, 540)">'
svg += '<rect x="0" y="0" width="140" height="100" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<circle cx="70" cy="50" r="25" fill="#9ca3af" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<circle cx="70" cy="50" r="10" fill="white" stroke="#1e3a5f" stroke-width="1"/>'
# Mounting holes
svg += '<circle cx="20" cy="20" r="5" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<circle cx="120" cy="20" r="5" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<circle cx="20" cy="80" r="5" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<circle cx="120" cy="80" r="5" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += dim_h(0, 100, 140, "55", 20)
svg += dim_v(140, 0, 100, "55", 20)
svg += '<text x="70" y="120" fill="#555" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">4x M5 THRU | Ø40 Bore</text>'
svg += '</g>'

svg += '<text x="600" y="520" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>'
svg += '<g transform="translate(500, 540)">'
svg += '<rect x="0" y="20" width="40" height="60" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2"/>'
svg += dim_h(0, 80, 40, "10", 20, "#e11d48", 12)
svg += '</g>'

svg += '</svg>'
save_svg_as_png("PART_07_08_BALL_SCREW_NUT", svg)


# =================================================================
# PART 09-10: MOTOR MOUNT + MOTOR
# =================================================================
print("Part 09-10: Motor Mount + Motor...")
svg = border("PARTS 09 & 10 — MOTOR MOUNT PLATE + 750W BLDC MOTOR", "Drives ball screw for scissor actuation", "Part 9: Q235 Steel 8 mm | Part 10: 750W BLDC 24V DC", "Part 9: 2 | Part 10: 2")

svg += '<text x="400" y="140" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 09: MOTOR MOUNT PLATE — FRONT VIEW</text>'
svg += '<g transform="translate(80, 160)">'
svg += '<rect x="0" y="0" width="360" height="288" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2.5"/>'
# Motor center hole
svg += '<circle cx="180" cy="144" r="45" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="180" y="148" fill="#888" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">Motor Spigot Ø90</text>'
# 4 mounting holes
for x, y in [(30, 30), (330, 30), (30, 258), (330, 258)]:
    svg += f'<circle cx="{x}" cy="{y}" r="8" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="365" y="35" fill="#555" font-size="11" font-family="Arial,sans-serif">Ø11 THRU (4x)</text>'
svg += dim_h(0, 288, 360, "200", 25)
svg += dim_v(360, 0, 288, "160", 25)
svg += dim_h(30, 0, 330, "170 (Hole Pitch W)", -22, "#888", 11)
svg += dim_v(0, 30, 258, "128 (Hole Pitch H)", -50, "#888", 11)
svg += '</g>'

svg += '<text x="700" y="140" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>'
svg += '<g transform="translate(600, 160)">'
svg += '<rect x="0" y="100" width="14" height="88" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
svg += dim_h(0, 188, 14, "8", 20, "#e11d48", 13)
svg += '</g>'

# MOTOR
svg += '<line x1="30" y1="530" x2="{0}" y2="530" stroke="#ccc" stroke-width="1.5"/>'.format(PW-30)
svg += '<text x="400" y="570" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 10: MOTOR (750W BLDC) — SIDE VIEW</text>'
svg += '<g transform="translate(80, 590)">'
svg += '<rect x="0" y="0" width="400" height="220" rx="10" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2.5"/>'
# Output shaft
svg += '<rect x="400" y="80" width="80" height="60" fill="#9ca3af" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="440" y="115" fill="white" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">Shaft</text>'
svg += dim_h(0, 220, 400, "148 (Motor Body)", 25)
svg += dim_h(400, 220, 480, "40 (Shaft)", 25, "#888", 11)
svg += dim_v(0, 0, 220, "Ø115", -50)
svg += '<text x="200" y="115" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" text-anchor="middle">750W BLDC</text>'
svg += '<text x="200" y="140" fill="#555" font-size="13" font-family="Arial,sans-serif" text-anchor="middle">24V DC | 3000 RPM</text>'
svg += '</g>'

svg += '<text x="800" y="570" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW (End)</text>'
svg += '<g transform="translate(680, 590)">'
svg += '<circle cx="110" cy="110" r="110" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<circle cx="110" cy="110" r="15" fill="#9ca3af" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="110" y="115" fill="white" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø14</text>'
svg += dim_h(0, 220, 220, "Ø115", 15, "#1e3a5f", 14)
svg += '</g>'

svg += '</svg>'
save_svg_as_png("PART_09_10_MOTOR_MOUNT", svg)


# =================================================================
# PART 18: DRIVE WHEEL (HUB MOTOR) + PART 19: CASTER WHEEL
# =================================================================
print("Part 18-19: Hub Motor + Caster...")
svg = border("PARTS 18 & 19 — HUB MOTOR DRIVE WHEEL + CASTER WHEEL", "Hub motors on side pods (center), Casters at 4 corners", "Part 18: PU + Alu Hub + BLDC | Part 19: PU + Steel Fork (Swivel)", "Part 18: 2 | Part 19: 4")

svg += '<text x="450" y="140" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 18: DRIVE WHEEL (HUB MOTOR — MOTORIZED)</text>'

svg += '<text x="250" y="180" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>'
svg += '<g transform="translate(100, 200)">'
svg += '<circle cx="150" cy="150" r="150" fill="#fbbf24" stroke="#1e3a5f" stroke-width="3"/>'
svg += '<circle cx="150" cy="150" r="80" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="150" cy="150" r="20" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="150" y="155" fill="#1e3a5f" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">Ø25</text>'
svg += '<text x="150" y="100" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">BLDC HUB MOTOR</text>'
svg += dim_h(0, 300, 300, "Ø200", 25, "#e11d48", 16)
svg += '</g>'

svg += '<text x="650" y="180" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>'
svg += '<g transform="translate(580, 200)">'
svg += '<rect x="0" y="50" width="60" height="200" rx="10" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2.5"/>'
# Hub motor body inside
svg += '<rect x="10" y="80" width="40" height="140" fill="#d1d5db" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += dim_h(0, 250, 60, "50 (Width)", 25)
svg += dim_v(60, 50, 250, "Ø200", 25)
svg += '</g>'

# CASTER
svg += '<line x1="30" y1="600" x2="{0}" y2="600" stroke="#ccc" stroke-width="1.5"/>'.format(PW-30)
svg += '<text x="450" y="640" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 19: CASTER WHEEL (SWIVEL TYPE)</text>'

svg += '<text x="250" y="680" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>'
svg += '<g transform="translate(100, 700)">'
# Fork
svg += '<path d="M 50,0 L 150,0 L 160,30 L 160,120 L 40,120 L 40,30 Z" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
# Wheel
svg += '<circle cx="100" cy="120" r="50" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<circle cx="100" cy="120" r="10" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
# Mounting plate
svg += '<rect x="30" y="-10" width="140" height="15" fill="#b0c4de" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += dim_h(50, 170, 150, "Ø100", 20)
svg += dim_v(160, -10, 170, "135 (Total H)", 25)
svg += '<text x="100" y="195" fill="#555" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">Swivel Top Plate: 115×95 mm | 4× Ø11 Bolt</text>'
svg += '</g>'

svg += '<text x="650" y="680" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>'
svg += '<g transform="translate(550, 700)">'
svg += '<rect x="0" y="10" width="40" height="100" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="20" cy="110" r="40" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="20" cy="110" r="8" fill="white" stroke="#1e3a5f" stroke-width="1"/>'
svg += dim_h(0, 150, 40, "45", 20, "#888", 12)
svg += '</g>'

# Wheel schematic
svg += '<text x="1100" y="680" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">WHEEL LAYOUT (TOP VIEW)</text>'
svg += '<g transform="translate(900, 700)">'
svg += '<rect x="0" y="0" width="350" height="280" fill="none" stroke="#1e3a5f" stroke-width="2"/>'
# CW corners
for x, y in [(15, 15), (315, 15), (15, 245), (315, 245)]:
    svg += f'<rect x="{x}" y="{y}" width="20" height="20" fill="#4ade80" stroke="#1e3a5f" stroke-width="1"/>'
    svg += f'<text x="{x+10}" y="{y+14}" fill="#0f172a" font-size="7" font-family="Arial,sans-serif" text-anchor="middle">CW</text>'
# Hub motors
svg += '<rect x="10" y="120" width="30" height="40" fill="#ef4444" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<text x="25" y="143" fill="white" font-size="7" font-family="Arial,sans-serif" text-anchor="middle">HM</text>'
svg += '<rect x="310" y="120" width="30" height="40" fill="#ef4444" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<text x="325" y="143" fill="white" font-size="7" font-family="Arial,sans-serif" text-anchor="middle">HM</text>'
# Pallet channels
svg += '<rect x="105" y="10" width="60" height="260" fill="#dbeafe" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<text x="135" y="140" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">P</text>'
svg += '<rect x="185" y="10" width="60" height="260" fill="#dbeafe" stroke="#1e3a5f" stroke-width="1"/>'
svg += '<text x="215" y="140" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">P</text>'
svg += '</g>'

svg += '</svg>'
save_svg_as_png("PART_18_19_WHEELS", svg)


# =================================================================
# PART 21-22: COMPLETE ASSEMBLY (LOWERED + RAISED)
# =================================================================
print("Part 21-22: Assembly Views...")
svg = border("PARTS 21 & 22 — COMPLETE ASSEMBLY VIEWS", "Side View: Lowered (170 mm) & Raised Max (310 mm)", "All parts assembled", "—")

# LOWERED
svg += '<text x="500" y="140" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">21. COMPLETE ASSEMBLY — LOWERED (SIDE VIEW)</text>'
svg += '<g transform="translate(80, 170)">'
# Base frame
svg += '<rect x="0" y="40" width="800" height="90" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2.5"/>'
# Fork plate (flush on top in lowered state)
svg += '<rect x="20" y="28" width="580" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="1.5"/>'
# Scissor collapsed inside
svg += '<line x1="40" y1="48" x2="590" y2="122" stroke="#16a34a" stroke-width="3"/>'
svg += '<line x1="590" y1="48" x2="40" y2="122" stroke="#dc2626" stroke-width="3"/>'
svg += '<circle cx="315" cy="85" r="6" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
# Ground line
svg += '<line x1="-20" y1="145" x2="830" y2="145" stroke="#888" stroke-width="1" stroke-dasharray="5,3"/>'
# Caster wheels
svg += '<circle cx="50" cy="138" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="750" cy="138" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
# Hub motor (center, slightly larger)
svg += '<circle cx="400" cy="140" r="18" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="400" y="145" fill="white" font-size="9" font-family="Arial,sans-serif" text-anchor="middle">HUB</text>'
# Dims
svg += dim_h(0, 130, 800, "1200", 30)
svg += dim_v(800, 28, 145, "170", 30, "#1e3a5f", 16)
svg += '<text x="660" y="80" fill="#888" font-size="12" font-family="Arial,sans-serif">Rear Bridge</text>'
svg += '</g>'

# RAISED
svg += '<text x="500" y="395" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">22. COMPLETE ASSEMBLY — RAISED MAX (SIDE VIEW)</text>'
svg += '<g transform="translate(80, 420)">'
# Base frame
svg += '<rect x="0" y="200" width="800" height="90" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2.5"/>'
# Fork plate raised up
svg += '<rect x="20" y="15" width="580" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="310" y="12" fill="#e11d48" font-size="14" font-family="Arial,sans-serif" text-anchor="middle">PALLET LIFTS HERE</text>'
# Scissor X expanded
svg += '<line x1="60" y1="27" x2="290" y2="285" stroke="#16a34a" stroke-width="4"/>'
svg += '<line x1="290" y1="27" x2="60" y2="285" stroke="#dc2626" stroke-width="4"/>'
svg += '<line x1="290" y1="27" x2="560" y2="285" stroke="#16a34a" stroke-width="4"/>'
svg += '<line x1="560" y1="27" x2="290" y2="285" stroke="#dc2626" stroke-width="4"/>'
svg += '<circle cx="175" cy="156" r="7" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="425" cy="156" r="7" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
# Ground line
svg += '<line x1="-20" y1="305" x2="830" y2="305" stroke="#888" stroke-width="1" stroke-dasharray="5,3"/>'
# Wheels
svg += '<circle cx="50" cy="298" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="750" cy="298" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<circle cx="400" cy="300" r="18" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="400" y="305" fill="white" font-size="9" font-family="Arial,sans-serif" text-anchor="middle">HUB</text>'
# Dims
svg += dim_h(0, 290, 800, "1200", 30)
svg += dim_v(800, 15, 305, "310 (Raised)", 30, "#e11d48", 16)
svg += dim_v(800, 200, 305, "90+15", 70, "#888", 12)
svg += '<text x="400" y="340" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" text-anchor="middle">Lift Stroke = 310 - 170 = 140 mm</text>'
svg += '</g>'

svg += '</svg>'
save_svg_as_png("PART_21_22_ASSEMBLY", svg)


# =================================================================
# PART 24-25: PALLET DRIVE + STEPPED GUIDE
# =================================================================
print("Part 24-25: Motor+Belt Drive + Stepped Guide...")
svg = border("PARTS 24 & 25 — PALLET DRIVE MECHANISM + STEPPED GUIDE RAIL", "User custom: Motor → Timing Belt → Shaft → Rollers push pallet along stepped guide", "Part 24: Motor+Belt Assembly | Part 25: Machined C45 Steel", "Part 24: 2 sets | Part 25: 2 pcs")

svg += '<text x="500" y="140" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 24: PALLET DRIVE MECHANISM (MOTOR + TIMING BELT + SHAFT)</text>'
svg += '<g transform="translate(80, 170)">'
# Motor
svg += '<rect x="0" y="60" width="140" height="100" rx="8" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<text x="70" y="115" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">MOTOR</text>'
svg += '<text x="70" y="135" fill="#555" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">750W BLDC</text>'
# Motor pulley
svg += '<circle cx="160" cy="110" r="20" fill="#9ca3af" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="160" y="115" fill="white" font-size="9" font-family="Arial,sans-serif" text-anchor="middle">Ø40</text>'
# Timing belt
svg += '<line x1="180" y1="100" x2="400" y2="100" stroke="#1e3a5f" stroke-width="4"/>'
svg += '<line x1="180" y1="120" x2="400" y2="120" stroke="#1e3a5f" stroke-width="4"/>'
# Belt teeth marks
for x in range(185, 400, 15):
    svg += f'<line x1="{x}" y1="100" x2="{x+5}" y2="120" stroke="#888" stroke-width="1"/>'
svg += '<text x="290" y="90" fill="#e11d48" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">TIMING BELT</text>'
# Driven pulley
svg += '<circle cx="420" cy="110" r="25" fill="#9ca3af" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="420" y="115" fill="white" font-size="9" font-family="Arial,sans-serif" text-anchor="middle">Ø50</text>'
# Shaft
svg += '<rect x="445" y="100" width="280" height="20" fill="#fed7aa" stroke="#1e3a5f" stroke-width="2"/>'
svg += '<text x="585" y="95" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SHAFT (Ø20 h6)</text>'
# Roller/wheel on shaft end
svg += '<circle cx="745" cy="110" r="35" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2.5"/>'
svg += '<circle cx="745" cy="110" r="8" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg += '<text x="745" y="115" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø70</text>'
svg += '<text x="745" y="160" fill="#1e3a5f" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">DRIVE ROLLER</text>'
# Dims
svg += dim_h(0, 160, 140, "148", 20, "#888", 12)
svg += dim_h(160, 160, 420, "260 (Belt C-C)", 20)
svg += dim_h(445, 120, 725, "280 (Shaft L)", 25)
svg += '</g>'

# STEPPED GUIDE
svg += '<line x1="30" y1="460" x2="{0}" y2="460" stroke="#ccc" stroke-width="1.5"/>'.format(PW-30)
svg += '<text x="500" y="500" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PART 25: STEPPED LINEAR GUIDE RAIL ("L GUIDE STEP")</text>'
svg += '<text x="500" y="520" fill="#555" font-size="13" font-family="Arial,sans-serif" text-anchor="middle">Mounted along each fork channel sidewall — pallet rollers ride on stepped surface</text>'

svg += '<text x="500" y="555" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (Profile)</text>'
svg += '<g transform="translate(100, 580)">'
# Stepped profile - 3 steps along 1000mm
svg += '<polygon points="0,200 350,200 370,140 700,140 720,70 1000,70 1000,220 0,220" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2.5"/>'
# Step surface lines (green highlight)
svg += '<line x1="0" y1="200" x2="350" y2="200" stroke="#4ade80" stroke-width="4"/>'
svg += '<line x1="370" y1="140" x2="700" y2="140" stroke="#4ade80" stroke-width="4"/>'
svg += '<line x1="720" y1="70" x2="1000" y2="70" stroke="#4ade80" stroke-width="4"/>'
# Riser lines
svg += '<line x1="350" y1="200" x2="370" y2="140" stroke="#4ade80" stroke-width="3"/>'
svg += '<line x1="700" y1="140" x2="720" y2="70" stroke="#4ade80" stroke-width="3"/>'
# Step dim annotations
svg += dim_h(0, 220, 350, "350 (Step 1)", 20)
svg += dim_h(370, 220, 700, "330 (Step 2)", 20)
svg += dim_h(720, 220, 1000, "280 (Step 3)", 20)
svg += dim_h(0, 220, 1000, "1000 (Total Length)", 50, "#1e3a5f", 16)
# Step heights
svg += dim_v(-30, 200, 220, "20", -50, "#e11d48", 12)
svg += dim_v(-30, 140, 220, "80", -90, "#e11d48", 13)
svg += dim_v(-30, 70, 220, "150", -130, "#e11d48", 14)
svg += '<text x="-135" y="215" fill="#e11d48" font-size="11" font-family="Arial,sans-serif">Step 1 Height</text>'
svg += '<text x="-180" y="175" fill="#e11d48" font-size="11" font-family="Arial,sans-serif">Step 2 Height</text>'
svg += '<text x="-220" y="140" fill="#e11d48" font-size="11" font-family="Arial,sans-serif">Step 3 Height (Max Lift)</text>'
# Arrow showing pallet entry direction
svg += '<line x1="-50" y1="130" x2="50" y2="130" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arrow)"/>'
svg += '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#1e3a5f"/></marker></defs>'
svg += '<text x="-70" y="135" fill="#1e3a5f" font-size="12" font-family="Arial,sans-serif" text-anchor="end">PALLET ENTRY</text>'
svg += '</g>'

# CROSS SECTION
svg += '<text x="1350" y="555" fill="#1e3a5f" font-size="16" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">CROSS SECTION</text>'
svg += '<g transform="translate(1250, 580)">'
svg += '<rect x="0" y="0" width="30" height="200" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
svg += dim_h(0, 200, 30, "30", 15, "#e11d48", 12)
svg += dim_v(30, 0, 200, "200 (Fits in channel wall)", 15, "#888", 11)
svg += '</g>'

svg += '</svg>'
save_svg_as_png("PART_24_25_DRIVE_GUIDE", svg)


print("\n=== ALL INDIVIDUAL PART PNGs GENERATED ===")
print(f"Files saved to:\n  {brain}/\n  {doc}/")
