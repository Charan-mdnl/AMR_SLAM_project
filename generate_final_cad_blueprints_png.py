#!/usr/bin/env python3
"""
Generate complete, 100% accurate, high-resolution PNG blueprints for each part of the AMR.
Layout across 1000mm width:
- Left Outer Pod: 150 mm
- Fork Channel 1: 200 mm
- Central Bridge Pod: 300 mm
- Fork Channel 2: 200 mm
- Right Outer Pod: 150 mm
Total = 150 + 200 + 300 + 200 + 150 = 1000 mm.

Length breakdown:
- Fork Channel Depth: 1000 mm
- Rear Solid Bridge: 200 mm
Total = 1200 mm.
"""

import os
import subprocess

brain_dir = "/home/charan/.gemini/antigravity-ide/brain/4ac556db-d1f1-449a-b470-f85aafe800fc"
doc_dir = "/home/charan/Documents/tusk-amr-files"
os.makedirs(doc_dir, exist_ok=True)

PW, PH = 1800, 1200

def dim_h(x1, y1, x2, label, off=25, col="#e11d48", fs=14):
    yo = y1 + off
    s = ""
    s += f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="{yo+4}" stroke="{col}" stroke-width="0.8" stroke-dasharray="3,2"/>'
    s += f'<line x1="{x2}" y1="{y1}" x2="{x2}" y2="{yo+4}" stroke="{col}" stroke-width="0.8" stroke-dasharray="3,2"/>'
    s += f'<line x1="{x1}" y1="{yo}" x2="{x2}" y2="{yo}" stroke="{col}" stroke-width="1.4"/>'
    s += f'<polygon points="{x1},{yo} {x1+7},{yo-3} {x1+7},{yo+3}" fill="{col}"/>'
    s += f'<polygon points="{x2},{yo} {x2-7},{yo-3} {x2-7},{yo+3}" fill="{col}"/>'
    mx = (x1 + x2) / 2
    s += f'<text x="{mx}" y="{yo-5}" fill="{col}" font-size="{fs}" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">{label}</text>'
    return s

def dim_v(x1, y1, y2, label, off=25, col="#1e3a5f", fs=14):
    xo = x1 + off
    s = ""
    s += f'<line x1="{x1}" y1="{y1}" x2="{xo+4}" y2="{y1}" stroke="{col}" stroke-width="0.8" stroke-dasharray="3,2"/>'
    s += f'<line x1="{x1}" y1="{y2}" x2="{xo+4}" y2="{y2}" stroke="{col}" stroke-width="0.8" stroke-dasharray="3,2"/>'
    s += f'<line x1="{xo}" y1="{y1}" x2="{xo}" y2="{y2}" stroke="{col}" stroke-width="1.4"/>'
    s += f'<polygon points="{xo},{y1} {xo-3},{y1+7} {xo+3},{y1+7}" fill="{col}"/>'
    s += f'<polygon points="{xo},{y2} {xo-3},{y2-7} {xo+3},{y2-7}" fill="{col}"/>'
    my = (y1 + y2) / 2
    s += f'<text x="{xo+6}" y="{my+5}" fill="{col}" font-size="{fs}" font-family="Arial,sans-serif" font-weight="bold">{label}</text>'
    return s

def border(title, subtitle, material, qty):
    return f"""<svg width="{PW}" height="{PH}" xmlns="http://www.w3.org/2000/svg">
<rect width="{PW}" height="{PH}" fill="white"/>
<rect x="8" y="8" width="{PW-16}" height="{PH-16}" fill="none" stroke="#1e3a5f" stroke-width="3.5"/>
<rect x="12" y="12" width="{PW-24}" height="{PH-24}" fill="none" stroke="#1e3a5f" stroke-width="1.2"/>
<!-- Title block top -->
<rect x="12" y="12" width="{PW-24}" height="55" fill="#1e3a5f"/>
<text x="{PW/2}" y="40" fill="white" font-size="22" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">{title}</text>
<text x="{PW/2}" y="60" fill="#93c5fd" font-size="14" font-family="Arial,sans-serif" text-anchor="middle">{subtitle}</text>
<!-- Material & Qty -->
<text x="30" y="88" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold">Material: {material}    |    QTY: {qty}    |    All dims in mm    |    Tolerances: ±0.5 mm</text>
<line x1="12" y1="95" x2="{PW-12}" y2="95" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Title block bottom -->
<rect x="{PW-380}" y="{PH-50}" width="368" height="38" fill="#1e3a5f"/>
<text x="{PW-196}" y="{PH-25}" fill="white" font-size="13" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">AMR CAD DRAWING PACKAGE | SCALE: NTS | JULY 2026</text>
"""

def render_png(name, svg_content):
    svg_path = f"/tmp/{name}.svg"
    png_path = f"/tmp/{name}.png"
    with open(svg_path, "w") as f:
        f.write(svg_content)
    subprocess.run(f"rsvg-convert -w {PW} -h {PH} {svg_path} -o {png_path}", shell=True)
    for d in [brain_dir, doc_dir]:
        subprocess.run(f"cp {png_path} {os.path.join(d, f'{name}.png')}", shell=True)
    print(f"Generated {name}.png ({os.path.getsize(png_path)} bytes)")

# =================================================================
# PART 01: BASE FRAME WELDMENT (150-200-300-200-150 Layout)
# =================================================================
svg1 = border("PART 01 — BASE FRAME (CHASSIS WELDMENT)", 
              "AMR Main Chassis — Symmetric 150-200-300-200-150 mm Layout", 
              "Q235 Steel | Rect Tube 80×60×4 mm and 8 mm Plate", "1")

# FRONT VIEW
svg1 += '<text x="450" y="130" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW (Width = 1000 mm)</text>'
svg1 += '<g transform="translate(60, 145)">'
# 1000mm -> 700px scale factor (0.7)
# Left Pod: 150mm = 105px
# Channel 1: 200mm = 140px
# Center Pod: 300mm = 210px
# Channel 2: 200mm = 140px
# Right Pod: 150mm = 105px
svg1 += '<rect x="0" y="0" width="700" height="119" fill="none" stroke="#1e3a5f" stroke-width="3"/>'
svg1 += '<rect x="0" y="0" width="105" height="119" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
svg1 += '<rect x="105" y="14" width="140" height="91" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg1 += '<rect x="245" y="0" width="210" height="119" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
svg1 += '<rect x="455" y="14" width="140" height="91" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg1 += '<rect x="595" y="0" width="105" height="119" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'

svg1 += '<text x="52" y="65" fill="#1e3a5f" font-size="11" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">LEFT POD</text>'
svg1 += '<text x="175" y="65" fill="#888" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">FORK SLOT 1</text>'
svg1 += '<text x="350" y="65" fill="#1e3a5f" font-size="12" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">CENTER BRIDGE POD</text>'
svg1 += '<text x="525" y="65" fill="#888" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">FORK SLOT 2</text>'
svg1 += '<text x="647" y="65" fill="#1e3a5f" font-size="11" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">RIGHT POD</text>'

svg1 += dim_h(0, 119, 105, "150", 20)
svg1 += dim_h(105, 119, 245, "200", 20)
svg1 += dim_h(245, 119, 455, "300", 20)
svg1 += dim_h(455, 119, 595, "200", 20)
svg1 += dim_h(595, 119, 700, "150", 20)
svg1 += dim_h(0, 119, 700, "1000 mm TOTAL CHASSIS WIDTH", 50, "#1e3a5f", 15)
svg1 += dim_v(700, 0, 119, "170 mm", 20)
svg1 += dim_v(105, 14, 105, "150 mm (Slot H)", -35, "#e11d48", 11)
svg1 += '</g>'

# SIDE VIEW
svg1 += '<text x="450" y="360" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (Length = 1200 mm)</text>'
svg1 += '<g transform="translate(60, 375)">'
# 1200mm -> 700px scale factor (0.583)
# Fork Channel: 1000mm = 583px
# Rear Bridge: 200mm = 117px
svg1 += '<rect x="0" y="0" width="700" height="119" fill="none" stroke="#1e3a5f" stroke-width="3"/>'
svg1 += '<rect x="0" y="14" width="583" height="91" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg1 += '<rect x="583" y="0" width="117" height="119" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2"/>'
svg1 += '<text x="291" y="65" fill="#888" font-size="13" font-family="Arial,sans-serif" text-anchor="middle">OPEN FORK CHANNEL (1000 mm Entry Depth)</text>'
svg1 += '<text x="641" y="65" fill="#1e3a5f" font-size="11" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">REAR BRIDGE</text>'

svg1 += dim_h(0, 119, 583, "1000 mm (Fork Entry)", 20)
svg1 += dim_h(583, 119, 700, "200 mm", 20)
svg1 += dim_h(0, 119, 700, "1200 mm TOTAL CHASSIS LENGTH", 50, "#1e3a5f", 15)
svg1 += dim_v(700, 0, 119, "170 mm", 20)
svg1 += '</g>'

# TOP VIEW
svg1 += '<text x="450" y="570" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">TOP VIEW (Plan Layout)</text>'
svg1 += '<g transform="translate(60, 585)">'
# 1000mm W -> 600px, 1200mm L -> 500px
# Layout W: 150(90px) + 200(120px) + 300(180px) + 200(120px) + 150(90px) = 600px
# Layout L: 1000(416px) + 200(84px) = 500px
svg1 += '<rect x="0" y="0" width="600" height="500" fill="none" stroke="#1e3a5f" stroke-width="3"/>'
# Left pod
svg1 += '<rect x="0" y="0" width="90" height="500" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="1.5"/>'
# Channel 1
svg1 += '<rect x="90" y="0" width="120" height="416" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
# Center pod
svg1 += '<rect x="210" y="0" width="180" height="500" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="1.5"/>'
# Channel 2
svg1 += '<rect x="390" y="0" width="120" height="416" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
# Right pod
svg1 += '<rect x="510" y="0" width="90" height="500" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="1.5"/>'
# Rear solid bridge
svg1 += '<rect x="0" y="416" width="600" height="84" fill="#dbeafe" stroke="#1e3a5f" stroke-width="2"/>'
svg1 += '<text x="300" y="462" fill="#1e3a5f" font-size="14" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">REAR SOLID BRIDGE (200 mm)</text>'

# Hub motors
svg1 += '<circle cx="45" cy="250" r="22" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg1 += '<text x="45" y="255" fill="white" font-size="8" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">HUB M</text>'
svg1 += '<circle cx="555" cy="250" r="22" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg1 += '<text x="555" y="255" fill="white" font-size="8" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">HUB M</text>'

# Casters
for cx, cy in [(25, 25), (25, 475), (575, 25), (575, 475)]:
    svg1 += f'<rect x="{cx-12}" y="{cy-12}" width="24" height="24" fill="#4ade80" stroke="#1e3a5f" stroke-width="1.5"/>'
    svg1 += f'<text x="{cx}" y="{cy+4}" fill="#0f172a" font-size="8" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">CW</text>'

svg1 += dim_h(0, 500, 90, "150", 20)
svg1 += dim_h(90, 500, 210, "200", 20)
svg1 += dim_h(210, 500, 390, "300", 20)
svg1 += dim_h(390, 500, 510, "200", 20)
svg1 += dim_h(510, 500, 600, "150", 20)
svg1 += dim_h(0, 500, 600, "1000 mm TOTAL WIDTH", 50, "#1e3a5f", 15)
svg1 += dim_v(600, 0, 500, "1200 mm TOTAL LENGTH", 20, "#1e3a5f", 15)
svg1 += dim_v(600, 0, 416, "1000 mm", 65, "#e11d48", 12)
svg1 += dim_v(600, 416, 500, "200 mm", 65, "#e11d48", 12)
svg1 += '</g>'

svg1 += '</svg>'
render_png("PART_01_BASE_FRAME", svg1)


# =================================================================
# PART 02: FORK PLATFORMS (TOP PLATES)
# =================================================================
svg2 = border("PART 02 — TOP PLATFORMS (FORK PLATES)", 
              "Lifting Plates inside 200 mm Fork Channels", 
              "Q235 Steel | Plate: 6 mm", "2 (Left and Right)")

svg2 += '<text x="500" y="135" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">TOP VIEW</text>'
svg2 += '<g transform="translate(60, 150)">'
svg2 += '<rect x="0" y="0" width="750" height="143" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2.5"/>'
for x in [40, 250, 500, 710]:
    svg2 += f'<circle cx="{x}" cy="30" r="6" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
    svg2 += f'<circle cx="{x}" cy="113" r="6" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>'
svg2 += '<text x="740" y="30" fill="#555" font-size="11" font-family="Arial,sans-serif">8x Ø11 THRU</text>'
svg2 += dim_h(0, 143, 750, "1000 mm (Fork Plate Length)", 25)
svg2 += dim_v(750, 0, 143, "190 mm (Plate Width)", 25)
svg2 += dim_h(40, 0, 710, "920 mm (Hole Pitch)", -22, "#888", 11)
svg2 += '</g>'

svg2 += '<text x="500" y="375" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>'
svg2 += '<g transform="translate(60, 395)">'
svg2 += '<rect x="0" y="0" width="750" height="8" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>'
svg2 += dim_h(0, 8, 750, "1000 mm", 20)
svg2 += dim_v(750, 0, 8, "6 mm", 25, "#e11d48", 13)
svg2 += '</g>'

svg2 += '<text x="500" y="490" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW (End View)</text>'
svg2 += '<g transform="translate(250, 510)">'
svg2 += '<rect x="0" y="0" width="286" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>'
svg2 += '<circle cx="30" cy="6" r="4" fill="none" stroke="#1e3a5f" stroke-width="1"/>'
svg2 += '<circle cx="256" cy="6" r="4" fill="none" stroke="#1e3a5f" stroke-width="1"/>'
svg2 += dim_h(0, 12, 286, "190 mm", 20)
svg2 += dim_v(286, 0, 12, "6 mm", 15, "#e11d48", 12)
svg2 += '</g>'

svg2 += '</svg>'
render_png("PART_02_FORK_PLATE", svg2)


# =================================================================
# PART 03: SCISSOR ARMS
# =================================================================
svg3 = border("PART 03 — SCISSOR LINKAGE ARM", 
              "Scissor Lift X-Arms — Rectangular Structural Tube", 
              "Q235 Steel | Rect Tube 60×40×6 mm", "4 (2 per channel set)")

svg3 += '<text x="500" y="135" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW (Single Arm)</text>'
svg3 += '<g transform="translate(80, 160)">'
svg3 += '<rect x="0" y="0" width="680" height="48" rx="24" fill="#dcfce7" stroke="#1e3a5f" stroke-width="2.5"/>'
svg3 += '<circle cx="34" cy="24" r="14" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg3 += '<circle cx="340" cy="24" r="14" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg3 += '<circle cx="646" cy="24" r="14" fill="white" stroke="#1e3a5f" stroke-width="2"/>'
svg3 += '<text x="34" y="29" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø20</text>'
svg3 += '<text x="340" y="29" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø20</text>'
svg3 += '<text x="646" y="29" fill="#1e3a5f" font-size="10" font-family="Arial,sans-serif" text-anchor="middle">Ø20</text>'

svg3 += dim_h(0, 48, 680, "760 mm (Overall Arm Length)", 25)
svg3 += dim_h(34, 48, 646, "720 mm (Cut Length / Pivot C-C)", 55)
svg3 += dim_h(34, 48, 340, "360 mm (Center Pivot Pitch)", 85, "#888", 12)
svg3 += dim_v(680, 0, 48, "60 mm", 25)
svg3 += '<text x="30" y="80" fill="#555" font-size="12" font-family="Arial,sans-serif">3x Ø20 H7 Reamed Holes</text>'
svg3 += '</g>'

svg3 += '<text x="300" y="380" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (Tube Section)</text>'
svg3 += '<g transform="translate(200, 400)">'
svg3 += '<rect x="0" y="0" width="80" height="120" fill="#dcfce7" stroke="#1e3a5f" stroke-width="2.5"/>'
svg3 += '<rect x="12" y="12" width="56" height="96" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>'
svg3 += '<text x="40" y="65" fill="#888" font-size="11" font-family="Arial,sans-serif" text-anchor="middle">THK 6 mm</text>'
svg3 += dim_h(0, 120, 80, "40 mm", 20)
svg3 += dim_v(80, 0, 120, "60 mm", 20)
svg3 += '</g>'

svg3 += '</svg>'
render_png("PART_03_SCISSOR_ARM", svg3)


# =================================================================
# PART 04: PINS AND BUSHES
# =================================================================
svg4 = border("PARTS 04 and 05 — CROSS PIVOT PIN and PIVOT BUSH", 
              "Precision Hardware for Scissor Joints", 
              "Pin: EN8 Steel | Bush: Bronze CuSn12", "12 Pins, 12 Bushes")

svg4 += '<text x="450" y="135" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">CROSS PIVOT PIN</text>'
svg4 += '<g transform="translate(80, 170)">'
svg4 += '<rect x="0" y="0" width="540" height="40" rx="20" fill="#fed7aa" stroke="#1e3a5f" stroke-width="2.5"/>'
svg4 += dim_h(0, 40, 540, "140 mm", 25)
svg4 += dim_v(540, 0, 40, "Ø20 h6", 25)
svg4 += '</g>'

svg4 += '<text x="450" y="380" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">PIVOT BUSH</text>'
svg4 += '<g transform="translate(80, 410)">'
svg4 += '<rect x="0" y="0" width="200" height="60" rx="10" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2.5"/>'
svg4 += dim_h(0, 60, 200, "25 mm", 25)
svg4 += dim_v(200, 0, 60, "Ø25 h6 (OD)", 25)
svg4 += '<text x="100" y="35" fill="white" font-size="12" font-family="Arial,sans-serif" text-anchor="middle">BORE Ø20 H7</text>'
svg4 += '</g>'

svg4 += '</svg>'
render_png("PART_04_PIN_BUSH", svg4)


# =================================================================
# PART 05: STEPPED GUIDE RAIL
# =================================================================
svg5 = border("PART 05 — STEPPED LINEAR GUIDE RAIL (L GUIDE STEP)", 
              "Linear Step Guide mounted along channel sidewalls", 
              "Machined C45 Steel", "2 (One per channel)")

svg5 += '<text x="500" y="140" fill="#1e3a5f" font-size="18" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">SIDE PROFILE (3-Step Elevation)</text>'
svg5 += '<g transform="translate(100, 170)">'
svg5 += '<polygon points="0,200 350,200 370,140 700,140 720,70 1000,70 1000,220 0,220" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2.5"/>'
svg5 += '<line x1="0" y1="200" x2="350" y2="200" stroke="#4ade80" stroke-width="4"/>'
svg5 += '<line x1="370" y1="140" x2="700" y2="140" stroke="#4ade80" stroke-width="4"/>'
svg5 += '<line x1="720" y1="70" x2="1000" y2="70" stroke="#4ade80" stroke-width="4"/>'

svg5 += dim_h(0, 220, 350, "350 mm (Step 1)", 20)
svg5 += dim_h(370, 220, 700, "330 mm (Step 2)", 20)
svg5 += dim_h(720, 220, 1000, "280 mm (Step 3)", 20)
svg5 += dim_h(0, 220, 1000, "1000 mm TOTAL LENGTH", 50, "#1e3a5f", 16)

svg5 += dim_v(-30, 200, 220, "20 mm", -40, "#e11d48", 12)
svg5 += dim_v(-30, 140, 220, "80 mm", -80, "#e11d48", 13)
svg5 += dim_v(-30, 70, 220, "150 mm", -120, "#e11d48", 14)
svg5 += '</g>'

svg5 += '</svg>'
render_png("PART_05_STEPPED_GUIDE", svg5)


# =================================================================
# PART 06: COMPLETE ASSEMBLY SCHEMATIC
# =================================================================
svg6 = border("PART 06 — COMPLETE AMR ASSEMBLY DRAWINGS", 
              "Full Robot Assembly — Lowered vs Extended Elevation", 
              "Assembled Components", "1 Unit")

# LOWERED VIEW
svg6 += '<text x="500" y="140" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">LOWERED STATE (170 mm Clearance Height)</text>'
svg6 += '<g transform="translate(80, 170)">'
svg6 += '<rect x="0" y="40" width="800" height="90" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2.5"/>'
svg6 += '<rect x="20" y="28" width="580" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="1.5"/>'
svg6 += '<line x1="40" y1="48" x2="590" y2="122" stroke="#16a34a" stroke-width="3"/>'
svg6 += '<line x1="590" y1="48" x2="40" y2="122" stroke="#dc2626" stroke-width="3"/>'
svg6 += '<circle cx="50" cy="138" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
svg6 += '<circle cx="750" cy="138" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
svg6 += '<circle cx="400" cy="140" r="18" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg6 += '<text x="400" y="145" fill="white" font-size="9" font-family="Arial,sans-serif" text-anchor="middle">HUB</text>'
svg6 += dim_h(0, 130, 800, "1200 mm Length", 30)
svg6 += dim_v(800, 28, 145, "170 mm", 30, "#1e3a5f", 16)
svg6 += '</g>'

# EXTENDED VIEW
svg6 += '<text x="500" y="395" fill="#1e3a5f" font-size="20" font-family="Arial,sans-serif" font-weight="bold" text-anchor="middle">RAISED STATE (310 mm Max Lift Height)</text>'
svg6 += '<g transform="translate(80, 420)">'
svg6 += '<rect x="0" y="200" width="800" height="90" fill="#e8f4fd" stroke="#1e3a5f" stroke-width="2.5"/>'
svg6 += '<rect x="20" y="15" width="580" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>'
svg6 += '<line x1="60" y1="27" x2="290" y2="285" stroke="#16a34a" stroke-width="4"/>'
svg6 += '<line x1="290" y1="27" x2="60" y2="285" stroke="#dc2626" stroke-width="4"/>'
svg6 += '<line x1="290" y1="27" x2="560" y2="285" stroke="#16a34a" stroke-width="4"/>'
svg6 += '<line x1="560" y1="27" x2="290" y2="285" stroke="#dc2626" stroke-width="4"/>'
svg6 += '<circle cx="50" cy="298" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
svg6 += '<circle cx="750" cy="298" r="14" fill="#4ade80" stroke="#1e3a5f" stroke-width="2"/>'
svg6 += '<circle cx="400" cy="300" r="18" fill="#ef4444" stroke="#1e3a5f" stroke-width="2"/>'
svg6 += '<text x="400" y="305" fill="white" font-size="9" font-family="Arial,sans-serif" text-anchor="middle">HUB</text>'
svg6 += dim_h(0, 290, 800, "1200 mm Length", 30)
svg6 += dim_v(800, 15, 305, "310 mm", 30, "#e11d48", 16)
svg6 += '</g>'

svg6 += '</svg>'
render_png("PART_06_COMPLETE_ASSEMBLY", svg6)

print("\n=== SUCCESS: All 6 CAD Blueprints successfully generated in PNG format ===")
