#!/usr/bin/env python3
"""
Generate professional engineering part drawing sheets matching the Tusk reference format.
Sheet 1: Structural parts (base frame, fork plate, scissor arms)
Sheet 2: Hardware, wheels, motor, assemblies
"""
import os, subprocess, math
from PIL import Image

brain = "/home/charan/.gemini/antigravity-ide/brain/4ac556db-d1f1-449a-b470-f85aafe800fc"
doc = "/home/charan/Documents/tusk-amr-files"
os.makedirs(doc, exist_ok=True)

W, H = 2400, 1600  # A3 landscape ratio

def dim_line(x1, y1, x2, y2, label, offset=25, color="#e11d48", font_size=13, orient="h"):
    """Generate SVG for a dimension line with arrows and label."""
    lines = ""
    if orient == "h":
        yo = y1 + offset
        lines += f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="{yo+5}" stroke="{color}" stroke-width="0.8"/>'
        lines += f'<line x1="{x2}" y1="{y1}" x2="{x2}" y2="{yo+5}" stroke="{color}" stroke-width="0.8"/>'
        lines += f'<line x1="{x1}" y1="{yo}" x2="{x2}" y2="{yo}" stroke="{color}" stroke-width="1.2"/>'
        lines += f'<polygon points="{x1},{yo} {x1+6},{yo-3} {x1+6},{yo+3}" fill="{color}"/>'
        lines += f'<polygon points="{x2},{yo} {x2-6},{yo-3} {x2-6},{yo+3}" fill="{color}"/>'
        mx = (x1+x2)/2
        lines += f'<text x="{mx}" y="{yo-4}" fill="{color}" font-size="{font_size}" font-family="sans-serif" font-weight="bold" text-anchor="middle">{label}</text>'
    elif orient == "v":
        xo = x1 + offset
        lines += f'<line x1="{x1}" y1="{y1}" x2="{xo+5}" y2="{y1}" stroke="{color}" stroke-width="0.8"/>'
        lines += f'<line x1="{x1}" y1="{y2}" x2="{xo+5}" y2="{y2}" stroke="{color}" stroke-width="0.8"/>'
        lines += f'<line x1="{xo}" y1="{y1}" x2="{xo}" y2="{y2}" stroke="{color}" stroke-width="1.2"/>'
        lines += f'<polygon points="{xo},{y1} {xo-3},{y1+6} {xo+3},{y1+6}" fill="{color}"/>'
        lines += f'<polygon points="{xo},{y2} {xo-3},{y2-6} {xo+3},{y2-6}" fill="{color}"/>'
        my = (y1+y2)/2
        lines += f'<text x="{xo+5}" y="{my+4}" fill="{color}" font-size="{font_size}" font-family="sans-serif" font-weight="bold">{label}</text>'
    return lines

# ============================================================
# SHEET 1: STRUCTURAL PARTS
# ============================================================
sheet1 = f"""<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">
<rect width="{W}" height="{H}" fill="white"/>
<rect x="10" y="10" width="{W-20}" height="{H-20}" fill="none" stroke="#1e3a5f" stroke-width="4"/>
<rect x="15" y="15" width="{W-30}" height="{H-30}" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>

<!-- TITLE BLOCK -->
<text x="{W/2}" y="42" fill="#1e3a5f" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">LOW PROFILE PALLET AMR (SCISSOR LIFT TYPE) — 1000 kg PAYLOAD — USER CUSTOM DESIGN</text>
<text x="{W/2}" y="62" fill="#1e3a5f" font-size="16" font-family="sans-serif" text-anchor="middle">DETAILED PART DRAWINGS — SHEET 1 OF 2</text>
<line x1="20" y1="70" x2="{W-20}" y2="70" stroke="#1e3a5f" stroke-width="2"/>

<!-- ========== PART 1: BASE FRAME (WELDMENT) ========== -->
<text x="40" y="100" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">1. BASE FRAME (WELDMENT)</text>
<text x="40" y="118" fill="#555" font-size="11" font-family="sans-serif">Material: Q235 Steel    Tube: 80×60×4 mm    Plate Thick: 8 mm    All welds 6 mm fillet</text>

<!-- Front/Top View of base frame -->
<g transform="translate(60, 135)">
<text x="300" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>
<!-- Outer rectangle 1000 wide x 170 high (scaled: 600 x 102) -->
<rect x="0" y="0" width="600" height="102" fill="none" stroke="#1e3a5f" stroke-width="2.5"/>
<!-- Left pod (300mm = 180px) -->
<rect x="0" y="0" width="180" height="102" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Slot 1 (200mm = 120px) -->
<rect x="180" y="15" width="120" height="72" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Center bridge (300mm = 180px) -->
<rect x="300" y="0" width="180" height="102" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Slot 2 (200mm = 120px) -->
<rect x="480" y="15" width="120" height="72" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>

<!-- Dimension lines -->
{dim_line(0, 102, 180, 102, "300", 18)}
{dim_line(180, 102, 300, 102, "200", 18)}
{dim_line(300, 102, 480, 102, "300", 18)}
{dim_line(480, 102, 600, 102, "200", 18)}
{dim_line(0, 102, 600, 102, "1000", 38)}
{dim_line(600, 0, 600, 102, "170", 15, "#1e3a5f", 12, "v")}
</g>

<!-- Side View of base frame -->
<g transform="translate(720, 135)">
<text x="210" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>
<!-- Side rectangle 1200 long x 170 high (scaled: 420 x 102) -->
<rect x="0" y="0" width="420" height="102" fill="none" stroke="#1e3a5f" stroke-width="2.5"/>
<!-- Slot opening (1000mm = 350px from front) -->
<rect x="0" y="15" width="350" height="72" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Rear solid bridge (200mm = 70px) -->
<rect x="350" y="0" width="70" height="102" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>

{dim_line(0, 102, 350, 102, "1000", 18)}
{dim_line(350, 102, 420, 102, "200", 18)}
{dim_line(0, 102, 420, 102, "1200", 38)}
{dim_line(420, 0, 420, 102, "170", 15, "#1e3a5f", 12, "v")}
</g>

<!-- ========== PART 2: TOP PLATFORM (FORK PLATE) ========== -->
<line x1="20" y1="310" x2="{W-20}" y2="310" stroke="#ccc" stroke-width="1"/>
<text x="40" y="335" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">2. TOP PLATFORM (FORK PLATE)</text>
<text x="40" y="353" fill="#555" font-size="11" font-family="sans-serif">Material: Q235 Steel    Plate: 6 mm    QTY: 2 (Left &amp; Right fork channels)</text>

<g transform="translate(60, 370)">
<text x="250" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">TOP VIEW</text>
<!-- Fork plate: 1000mm long x 190mm wide (scaled: 500 x 57) -->
<rect x="0" y="0" width="500" height="57" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>
<!-- Mounting holes -->
<circle cx="30" cy="28" r="4" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="470" cy="28" r="4" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="510" y="20" fill="#555" font-size="10" font-family="sans-serif">Ø11 THRU (8x)</text>

{dim_line(0, 57, 500, 57, "1000 (Fork Length)", 18)}
{dim_line(500, 0, 500, 57, "190", 15, "#1e3a5f", 11, "v")}
</g>

<g transform="translate(620, 370)">
<text x="60" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>
<rect x="0" y="0" width="120" height="10" fill="#fef3c7" stroke="#1e3a5f" stroke-width="2"/>
<text x="60" y="25" fill="#555" font-size="10" font-family="sans-serif" text-anchor="middle">Fork Inner Width: 190</text>
{dim_line(120, 0, 120, 10, "6", 10, "#e11d48", 10, "v")}
</g>

<g transform="translate(830, 340)">
<text x="180" y="0" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">FORK SPACING (TOP VIEW REF.)</text>
<!-- Shows 2 fork plates spaced 560mm C-C -->
<rect x="0" y="20" width="360" height="80" fill="none" stroke="#aaa" stroke-width="1" stroke-dasharray="5,3"/>
<rect x="60" y="30" width="100" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="1.5"/>
<rect x="200" y="30" width="100" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="110" y="60" fill="#1e3a5f" font-size="10" font-family="sans-serif" text-anchor="middle">FORK 1</text>
<text x="250" y="60" fill="#1e3a5f" font-size="10" font-family="sans-serif" text-anchor="middle">FORK 2</text>
{dim_line(110, 42, 250, 42, "400 C-C", 30, "#e11d48", 11)}
</g>

<!-- ========== PART 3: SCISSOR ARM (1 PC) ========== -->
<line x1="20" y1="470" x2="{W-20}" y2="470" stroke="#ccc" stroke-width="1"/>
<text x="40" y="495" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">3. SCISSOR ARM (1 PC)</text>
<text x="40" y="513" fill="#555" font-size="11" font-family="sans-serif">Material: Rectangular Tube 60×40×6 mm (Q235 Steel)    QTY: 4 (2 per scissor set)</text>

<g transform="translate(60, 530)">
<text x="270" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>
<!-- Scissor arm: 760mm total, 720mm cut (scaled: 540 x 36) -->
<rect x="0" y="0" width="540" height="36" rx="18" fill="#dcfce7" stroke="#1e3a5f" stroke-width="2"/>
<!-- 3 pivot holes -->
<circle cx="30" cy="18" r="10" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="270" cy="18" r="10" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="510" cy="18" r="10" fill="white" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="30" y="55" fill="#555" font-size="9" font-family="sans-serif" text-anchor="middle">Ø20 H7</text>
<text x="270" y="55" fill="#555" font-size="9" font-family="sans-serif" text-anchor="middle">Ø20 H7 (CENTER)</text>
<text x="510" y="55" fill="#555" font-size="9" font-family="sans-serif" text-anchor="middle">Ø20 H7</text>

{dim_line(30, 36, 510, 36, "720 (Cut Length)", 25)}
{dim_line(0, 36, 540, 36, "760 (Overall)", 45)}
{dim_line(540, 0, 540, 36, "60", 12, "#1e3a5f", 10, "v")}
</g>

<g transform="translate(680, 530)">
<text x="30" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW (TUBE SECTION)</text>
<rect x="0" y="0" width="36" height="54" fill="#dcfce7" stroke="#1e3a5f" stroke-width="2"/>
<rect x="5" y="5" width="26" height="44" fill="white" stroke="#1e3a5f" stroke-width="1"/>
<text x="18" y="32" fill="#555" font-size="8" font-family="sans-serif" text-anchor="middle">THK 6</text>
{dim_line(0, 54, 36, 54, "40", 15, "#e11d48", 10)}
{dim_line(36, 0, 36, 54, "60", 12, "#1e3a5f", 10, "v")}
</g>

<!-- ========== PART 4: SCISSOR ARM (2nd PC - MIRROR) ========== -->
<g transform="translate(820, 490)">
<text x="40" y="5" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">4. SCISSOR ARM (2nd PC)</text>
<text x="40" y="23" fill="#555" font-size="11" font-family="sans-serif">Same as Part 3 (Mirror)</text>
<!-- Show X pattern -->
<line x1="60" y1="45" x2="360" y2="125" stroke="#16a34a" stroke-width="4"/>
<line x1="360" y1="45" x2="60" y2="125" stroke="#dc2626" stroke-width="4"/>
<text x="210" y="100" fill="#1e3a5f" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">SCISSOR X-PATTERN</text>
</g>

<!-- ========== PART 5-6: CROSS PIN + PIVOT BUSH ========== -->
<line x1="20" y1="660" x2="{W-20}" y2="660" stroke="#ccc" stroke-width="1"/>
<text x="40" y="685" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">5. CROSS PIN (PIVOT)</text>
<text x="40" y="703" fill="#555" font-size="11" font-family="sans-serif">Material: EN8 Steel    QTY: 12</text>

<g transform="translate(60, 715)">
<text x="100" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>
<rect x="0" y="5" width="200" height="16" fill="#fed7aa" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(0, 21, 200, 21, "140", 15)}
<text x="210" y="18" fill="#555" font-size="10" font-family="sans-serif">Ø20 h6</text>
</g>

<g transform="translate(300, 715)">
<text x="15" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE</text>
<circle cx="15" cy="13" r="12" fill="#fed7aa" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="35" y="18" fill="#555" font-size="10" font-family="sans-serif">Ø20 h6</text>
</g>

<text x="420" y="685" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">6. PIVOT BUSH</text>
<text x="420" y="703" fill="#555" font-size="11" font-family="sans-serif">Material: Bronze CuSn12    QTY: 12</text>

<g transform="translate(440, 715)">
<text x="40" y="-5" fill="#1e3a5f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>
<rect x="0" y="0" width="80" height="20" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(0, 20, 80, 20, "25", 12, "#e11d48", 10)}
<text x="90" y="15" fill="#555" font-size="10" font-family="sans-serif">Ø25 h6 / Ø20 H7</text>
</g>

<!-- ========== PART 7: BALL SCREW ========== -->
<text x="700" y="685" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">7. BALL SCREW</text>
<text x="700" y="703" fill="#555" font-size="11" font-family="sans-serif">Material: SCM415    Lead: 5 mm    Type: C7    QTY: 2</text>

<g transform="translate(720, 715)">
<rect x="0" y="5" width="360" height="12" fill="#d1d5db" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(0, 17, 360, 17, "600", 15)}
</g>

<!-- ========== PART 8-9: BALL NUT + MOTOR MOUNT ========== -->
<line x1="20" y1="780" x2="{W-20}" y2="780" stroke="#ccc" stroke-width="1"/>
<text x="40" y="805" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">8. BALL NUT + HOUSING</text>
<text x="40" y="823" fill="#555" font-size="11" font-family="sans-serif">4x M5 THRU    QTY: 2</text>

<g transform="translate(60, 835)">
<rect x="0" y="0" width="60" height="35" fill="#d1d5db" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="10" cy="10" r="3" fill="none" stroke="#1e3a5f" stroke-width="1"/>
<circle cx="50" cy="10" r="3" fill="none" stroke="#1e3a5f" stroke-width="1"/>
<circle cx="10" cy="25" r="3" fill="none" stroke="#1e3a5f" stroke-width="1"/>
<circle cx="50" cy="25" r="3" fill="none" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(0, 35, 60, 35, "55", 12, "#e11d48", 10)}
<text x="70" y="20" fill="#555" font-size="10" font-family="sans-serif">Ø40</text>
</g>

<text x="250" y="805" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">9. MOTOR MOUNT PLATE</text>
<text x="250" y="823" fill="#555" font-size="11" font-family="sans-serif">Material: Q235 Steel    Plate: 8 mm    QTY: 2</text>

<g transform="translate(270, 835)">
<rect x="0" y="0" width="120" height="96" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="15" cy="15" r="5" fill="none" stroke="#1e3a5f" stroke-width="1"/>
<circle cx="105" cy="15" r="5" fill="none" stroke="#1e3a5f" stroke-width="1"/>
<circle cx="15" cy="81" r="5" fill="none" stroke="#1e3a5f" stroke-width="1"/>
<circle cx="105" cy="81" r="5" fill="none" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(0, 96, 120, 96, "200", 15, "#e11d48", 10)}
{dim_line(120, 0, 120, 96, "160", 12, "#1e3a5f", 10, "v")}
<text x="60" y="55" fill="#555" font-size="9" font-family="sans-serif" text-anchor="middle">4x Ø11 THRU</text>
</g>

<text x="500" y="805" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">10. MOTOR (750W BLDC)</text>
<text x="500" y="823" fill="#555" font-size="11" font-family="sans-serif">Power: 750 W    Rated Speed: 3000 RPM    Rated Voltage: 24V DC</text>

<g transform="translate(520, 835)">
<text x="80" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE VIEW</text>
<rect x="0" y="0" width="160" height="70" rx="5" fill="#d1d5db" stroke="#1e3a5f" stroke-width="1.5"/>
<rect x="160" y="15" width="30" height="40" fill="#9ca3af" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(0, 70, 160, 70, "148", 15, "#e11d48", 10)}
<text x="80" y="92" fill="#555" font-size="10" font-family="sans-serif" text-anchor="middle">Ø115</text>
</g>

<g transform="translate(760, 835)">
<text x="35" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT</text>
<circle cx="35" cy="35" r="35" fill="#d1d5db" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="35" cy="35" r="8" fill="#9ca3af" stroke="#1e3a5f" stroke-width="1"/>
</g>

<!-- ========== PARTS 11-12: ROLLER BOGIE + PU ROLLER ========== -->
<line x1="20" y1="960" x2="{W-20}" y2="960" stroke="#ccc" stroke-width="1"/>
<text x="40" y="985" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">11. ROLLER BOGIE HOUSING (1 SET = 2 PCS)</text>
<text x="40" y="1003" fill="#555" font-size="11" font-family="sans-serif">Material: Q235 Steel    Plate: 8 mm    QTY: 4 sets</text>

<g transform="translate(60, 1015)">
<text x="80" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>
<path d="M 0,80 L 0,0 L 160,0 L 160,80 L 130,80 L 130,30 L 30,30 L 30,80 Z" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="50" cy="60" r="8" fill="none" stroke="#1e3a5f" stroke-width="1"/>
<circle cx="110" cy="60" r="8" fill="none" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(0, 80, 160, 80, "180", 15, "#e11d48", 10)}
{dim_line(160, 0, 160, 80, "140", 10, "#1e3a5f", 10, "v")}
<text x="80" y="72" fill="#555" font-size="9" font-family="sans-serif" text-anchor="middle">Ø14 (2x)</text>
</g>

<g transform="translate(300, 1015)">
<text x="30" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE</text>
<rect x="0" y="20" width="60" height="60" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(0, 80, 60, 80, "75", 12, "#e11d48", 10)}
</g>

<text x="440" y="985" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">12. POLYURETHANE ROLLER</text>
<text x="440" y="1003" fill="#555" font-size="11" font-family="sans-serif">Material: Polyurethane (PU)    Hardness: 95A    QTY: 8</text>

<g transform="translate(460, 1015)">
<text x="90" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>
<rect x="0" y="10" width="180" height="50" rx="25" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(0, 60, 180, 60, "180", 15, "#e11d48", 10)}
</g>

<g transform="translate(680, 1015)">
<text x="30" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE</text>
<circle cx="30" cy="35" r="30" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="30" cy="35" r="6" fill="white" stroke="#1e3a5f" stroke-width="1"/>
<text x="70" y="40" fill="#555" font-size="10" font-family="sans-serif">Ø60</text>
</g>

<!-- ========== BOTTOM TITLE BLOCK ========== -->
<line x1="20" y1="1130" x2="{W-20}" y2="1130" stroke="#1e3a5f" stroke-width="2"/>

<!-- KEY SPECS -->
<g transform="translate(30, 1145)">
<text x="0" y="15" fill="#1e3a5f" font-size="13" font-family="sans-serif" font-weight="bold">KEY OVERALL SPECIFICATIONS</text>
<text x="0" y="33" fill="#555" font-size="10" font-family="sans-serif">Payload Capacity: 1000 kg</text>
<text x="0" y="48" fill="#555" font-size="10" font-family="sans-serif">Overall Length: 1200 mm</text>
<text x="0" y="63" fill="#555" font-size="10" font-family="sans-serif">Overall Width: 1000 mm</text>
<text x="0" y="78" fill="#555" font-size="10" font-family="sans-serif">Lowered Height: 170 mm</text>
<text x="0" y="93" fill="#555" font-size="10" font-family="sans-serif">Max Lift Height (Top of Fork): 310 mm</text>
<text x="0" y="108" fill="#555" font-size="10" font-family="sans-serif">Fork Outer Width (Slot): 200 mm each</text>
<text x="0" y="123" fill="#555" font-size="10" font-family="sans-serif">Width Layout: 300+200+300+200 = 1000</text>
<text x="0" y="138" fill="#555" font-size="10" font-family="sans-serif">Drive: 2x Hub Motors (center sides)</text>
<text x="0" y="153" fill="#555" font-size="10" font-family="sans-serif">Support: 4x Corner Swivel Casters</text>
<text x="0" y="168" fill="#555" font-size="10" font-family="sans-serif">Navigation: SLAM + QR</text>
</g>

<g transform="translate(400, 1145)">
<text x="0" y="15" fill="#1e3a5f" font-size="13" font-family="sans-serif" font-weight="bold">GENERAL NOTES</text>
<text x="0" y="33" fill="#555" font-size="10" font-family="sans-serif">1. All dimensions are in millimeters (mm).</text>
<text x="0" y="48" fill="#555" font-size="10" font-family="sans-serif">2. Tolerances: ±0.5 mm unless otherwise stated.</text>
<text x="0" y="63" fill="#555" font-size="10" font-family="sans-serif">3. Weld all around 6 mm fillet weld for all frames.</text>
<text x="0" y="78" fill="#555" font-size="10" font-family="sans-serif">4. Deburr all edges and corners (R1 - R2).</text>
<text x="0" y="93" fill="#555" font-size="10" font-family="sans-serif">5. Use high-strength bolts (8.8 Grade).</text>
<text x="0" y="108" fill="#555" font-size="10" font-family="sans-serif">6. Surface Finish: Powder Coated.</text>
</g>

<g transform="translate(800, 1145)">
<text x="0" y="15" fill="#1e3a5f" font-size="13" font-family="sans-serif" font-weight="bold">MATERIAL SUMMARY</text>
<text x="0" y="33" fill="#555" font-size="10" font-family="sans-serif">Q235 Steel (Structural Parts)</text>
<text x="0" y="48" fill="#555" font-size="10" font-family="sans-serif">EN8 Steel (Pins &amp; Shafts)</text>
<text x="0" y="63" fill="#555" font-size="10" font-family="sans-serif">Bronze CuSn12 (Bushes)</text>
<text x="0" y="78" fill="#555" font-size="10" font-family="sans-serif">SCM415 (Ball Screw)</text>
<text x="0" y="93" fill="#555" font-size="10" font-family="sans-serif">Polyurethane 95A (Rollers &amp; Wheels)</text>
<text x="0" y="108" fill="#555" font-size="10" font-family="sans-serif">Cast Iron (Bearing Blocks)</text>
</g>

<!-- TITLE BLOCK BOTTOM RIGHT -->
<rect x="{W-450}" y="{H-80}" width="430" height="60" fill="none" stroke="#1e3a5f" stroke-width="2"/>
<text x="{W-440}" y="{H-55}" fill="#1e3a5f" font-size="14" font-family="sans-serif" font-weight="bold">USER CUSTOM AMR — SHEET 1 OF 2</text>
<text x="{W-440}" y="{H-35}" fill="#555" font-size="11" font-family="sans-serif">REV: 8.0 | SCALE: NTS | DATE: JULY 2026 | ALL DIMS IN mm</text>

</svg>"""

# ============================================================
# SHEET 2: HARDWARE, WHEELS, ASSEMBLIES
# ============================================================
sheet2 = f"""<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">
<rect width="{W}" height="{H}" fill="white"/>
<rect x="10" y="10" width="{W-20}" height="{H-20}" fill="none" stroke="#1e3a5f" stroke-width="4"/>
<rect x="15" y="15" width="{W-30}" height="{H-30}" fill="none" stroke="#1e3a5f" stroke-width="1.5"/>

<text x="{W/2}" y="42" fill="#1e3a5f" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">LOW PROFILE PALLET AMR (SCISSOR LIFT TYPE) — 1000 kg PAYLOAD — USER CUSTOM DESIGN</text>
<text x="{W/2}" y="62" fill="#1e3a5f" font-size="16" font-family="sans-serif" text-anchor="middle">DETAILED PART DRAWINGS — SHEET 2 OF 2</text>
<line x1="20" y1="70" x2="{W-20}" y2="70" stroke="#1e3a5f" stroke-width="2"/>

<!-- ========== PART 13: ROLLER SHAFT ========== -->
<text x="40" y="100" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">13. ROLLER SHAFT</text>
<text x="40" y="118" fill="#555" font-size="11" font-family="sans-serif">Material: EN8 Steel    QTY: 8</text>

<g transform="translate(60, 130)">
<text x="100" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT VIEW</text>
<rect x="0" y="5" width="200" height="14" fill="#fed7aa" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(0, 19, 200, 19, "180", 12)}
<text x="210" y="17" fill="#555" font-size="10" font-family="sans-serif">Ø20 h6</text>
</g>

<g transform="translate(320, 130)">
<text x="12" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE</text>
<circle cx="12" cy="12" r="10" fill="#fed7aa" stroke="#1e3a5f" stroke-width="1.5"/>
</g>

<!-- ========== PART 14: BEARING BLOCK ========== -->
<text x="440" y="100" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">14. BEARING BLOCK (BK15)</text>
<text x="440" y="118" fill="#555" font-size="11" font-family="sans-serif">Material: Cast Iron    QTY: 4</text>

<g transform="translate(460, 130)">
<text x="35" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT</text>
<rect x="0" y="0" width="70" height="50" rx="3" fill="#d1d5db" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="35" cy="25" r="10" fill="white" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(0, 50, 70, 50, "60", 12, "#e11d48", 10)}
{dim_line(70, 0, 70, 50, "89", 10, "#1e3a5f", 10, "v")}
<text x="35" y="70" fill="#555" font-size="9" font-family="sans-serif" text-anchor="middle">Ø15</text>
</g>

<g transform="translate(580, 130)">
<text x="15" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE</text>
<rect x="0" y="10" width="30" height="40" rx="3" fill="#d1d5db" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(30, 10, 30, 50, "34", 8, "#1e3a5f", 9, "v")}
</g>

<!-- ========== PART 15: LIMIT SWITCH BRACKET ========== -->
<text x="700" y="100" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">15. LIMIT SWITCH BRACKET</text>
<text x="700" y="118" fill="#555" font-size="11" font-family="sans-serif">Material: Q235 Steel    Plate: 6 mm    QTY: 4</text>

<g transform="translate(720, 130)">
<path d="M 0,50 L 0,0 L 50,0 L 50,30 L 20,30 L 20,50 Z" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="10" cy="10" r="4" fill="none" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(0, 50, 20, 50, "40", 12, "#e11d48", 9)}
{dim_line(50, 0, 50, 30, "48", 8, "#1e3a5f", 9, "v")}
<text x="60" y="15" fill="#555" font-size="9" font-family="sans-serif">Ø6.5 THRU</text>
</g>

<!-- ========== PART 16: SIDE COVER PLATE ========== -->
<text x="900" y="100" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">16. SIDE COVER PLATE</text>
<text x="900" y="118" fill="#555" font-size="11" font-family="sans-serif">Material: Q235 Steel    Plate: 2 mm    QTY: 2</text>

<g transform="translate(920, 130)">
<rect x="0" y="0" width="400" height="10" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
{dim_line(0, 10, 400, 10, "1200", 12)}
<text x="200" y="35" fill="#555" font-size="9" font-family="sans-serif" text-anchor="middle">6 mm height (folded lip)</text>
</g>

<!-- ========== PART 17: FORK EXTENSION (E10T CONFIG.) ========== -->
<line x1="20" y1="220" x2="{W-20}" y2="220" stroke="#ccc" stroke-width="1"/>
<text x="40" y="245" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">17. FORK EXTENSION (E10T CONFIG.)</text>
<text x="40" y="263" fill="#555" font-size="11" font-family="sans-serif">Material: Q235 Steel    Plate: 6 mm</text>

<g transform="translate(60, 278)">
<rect x="0" y="0" width="560" height="15" fill="#fef3c7" stroke="#1e3a5f" stroke-width="1.5"/>
<line x1="285" y1="0" x2="285" y2="15" stroke="#1e3a5f" stroke-width="1" stroke-dasharray="3,3"/>
{dim_line(0, 15, 285, 15, "Standard 713", 15)}
{dim_line(285, 15, 560, 15, "Extension 687", 15)}
{dim_line(0, 15, 560, 15, "TOTAL 1400", 35)}
</g>

<!-- ========== PART 18: DRIVE WHEEL (HUB MOTOR) ========== -->
<text x="700" y="245" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">18. DRIVE WHEEL (HUB MOTOR - MOTORIZED)</text>
<text x="700" y="263" fill="#555" font-size="11" font-family="sans-serif">Material: Polyurethane with Aluminum Hub    QTY: 2</text>

<g transform="translate(720, 278)">
<text x="40" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT</text>
<circle cx="40" cy="40" r="40" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2"/>
<circle cx="40" cy="40" r="10" fill="white" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(0, 80, 80, 80, "Ø200", 12)}
<text x="60" y="45" fill="#555" font-size="9" font-family="sans-serif">Ø25</text>
</g>

<g transform="translate(850, 278)">
<text x="15" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE</text>
<rect x="0" y="0" width="30" height="80" rx="5" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
</g>

<!-- ========== PART 19: IDLER/CASTER WHEEL ========== -->
<text x="960" y="245" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">19. CASTER WHEEL (SWIVEL)</text>
<text x="960" y="263" fill="#555" font-size="11" font-family="sans-serif">Material: PU + Steel Fork    QTY: 4</text>

<g transform="translate(980, 278)">
<text x="30" y="-5" fill="#1e3a5f" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT</text>
<circle cx="30" cy="35" r="25" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="30" cy="35" r="5" fill="white" stroke="#1e3a5f" stroke-width="1"/>
{dim_line(5, 60, 55, 60, "Ø100", 10, "#e11d48", 9)}
</g>

<!-- ========== PART 20: FASTENER KIT ========== -->
<line x1="20" y1="400" x2="{W-20}" y2="400" stroke="#ccc" stroke-width="1"/>
<text x="40" y="425" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">20. FASTENER KIT (MAIN)</text>

<g transform="translate(60, 445)">
<text x="0" y="0" fill="#555" font-size="11" font-family="sans-serif">Hex Bolt M10 x 30    16 Nos</text>
<text x="0" y="18" fill="#555" font-size="11" font-family="sans-serif">Hex Bolt M10 x 40     8 Nos</text>
<text x="0" y="36" fill="#555" font-size="11" font-family="sans-serif">Hex Bolt M12 x 35    16 Nos</text>
<text x="0" y="54" fill="#555" font-size="11" font-family="sans-serif">Lock Nut M10          24 Nos</text>
<text x="0" y="72" fill="#555" font-size="11" font-family="sans-serif">Lock Nut M12          16 Nos</text>
<text x="0" y="90" fill="#555" font-size="11" font-family="sans-serif">Flat Washer M10       24 Nos</text>
<text x="0" y="108" fill="#555" font-size="11" font-family="sans-serif">Flat Washer M12       16 Nos</text>
</g>

<!-- ========== PART 21: COMPLETE ASSEMBLY (LOWERED) ========== -->
<text x="400" y="425" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">21. COMPLETE ASSEMBLY (LOWERED)</text>
<text x="400" y="443" fill="#555" font-size="11" font-family="sans-serif">SIDE VIEW (LOWERED)</text>

<g transform="translate(420, 460)">
<!-- Base frame -->
<rect x="0" y="50" width="480" height="50" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="2"/>
<!-- Fork plate flush on top -->
<rect x="10" y="40" width="350" height="10" fill="#fef3c7" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Scissor collapsed inside -->
<line x1="30" y1="55" x2="340" y2="90" stroke="#16a34a" stroke-width="2"/>
<line x1="340" y1="55" x2="30" y2="90" stroke="#dc2626" stroke-width="2"/>
<!-- Wheels -->
<circle cx="50" cy="105" r="12" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="430" cy="105" r="12" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="240" cy="108" r="15" fill="#ef4444" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="240" y="113" fill="white" font-size="8" font-family="sans-serif" text-anchor="middle">HUB</text>

{dim_line(0, 100, 480, 100, "1200", 30)}
{dim_line(480, 40, 480, 120, "170", 15, "#1e3a5f", 11, "v")}
</g>

<!-- ========== PART 22: COMPLETE ASSEMBLY (RAISED MAX) ========== -->
<text x="400" y="600" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">22. COMPLETE ASSEMBLY (RAISED MAX)</text>
<text x="400" y="618" fill="#555" font-size="11" font-family="sans-serif">SIDE VIEW (RAISED MAX)</text>

<g transform="translate(420, 635)">
<!-- Base frame -->
<rect x="0" y="110" width="480" height="50" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="2"/>
<!-- Scissor expanded -->
<line x1="30" y1="20" x2="180" y2="155" stroke="#16a34a" stroke-width="3"/>
<line x1="180" y1="20" x2="30" y2="155" stroke="#dc2626" stroke-width="3"/>
<line x1="180" y1="20" x2="340" y2="155" stroke="#16a34a" stroke-width="3"/>
<line x1="340" y1="20" x2="180" y2="155" stroke="#dc2626" stroke-width="3"/>
<!-- Fork plate raised -->
<rect x="10" y="5" width="350" height="12" fill="#fef3c7" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Wheels -->
<circle cx="50" cy="165" r="12" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="430" cy="165" r="12" fill="#fbbf24" stroke="#1e3a5f" stroke-width="1.5"/>
<circle cx="240" cy="168" r="15" fill="#ef4444" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="240" y="173" fill="white" font-size="8" font-family="sans-serif" text-anchor="middle">HUB</text>

{dim_line(0, 160, 480, 160, "1200", 30)}
{dim_line(480, 5, 480, 180, "310", 15, "#1e3a5f", 11, "v")}
</g>

<!-- ========== PART 23: WHEEL SCHEMATIC (TOP VIEW) ========== -->
<line x1="20" y1="870" x2="{W-20}" y2="870" stroke="#ccc" stroke-width="1"/>
<text x="40" y="895" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">23. WHEEL LAYOUT &amp; LOAD DISTRIBUTION (TOP VIEW)</text>

<g transform="translate(60, 920)">
<!-- Chassis outline -->
<rect x="0" y="0" width="400" height="300" fill="none" stroke="#1e3a5f" stroke-width="2.5"/>

<!-- 4 Corner Casters -->
<rect x="10" y="10" width="35" height="45" fill="#4ade80" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="27" y="37" fill="#0f172a" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

<rect x="355" y="10" width="35" height="45" fill="#4ade80" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="372" y="37" fill="#0f172a" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

<rect x="10" y="245" width="35" height="45" fill="#4ade80" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="27" y="272" fill="#0f172a" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

<rect x="355" y="245" width="35" height="45" fill="#4ade80" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="372" y="272" fill="#0f172a" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

<!-- 2 Center Hub Motors -->
<rect x="10" y="120" width="45" height="60" fill="#ef4444" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="32" y="155" fill="white" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hub M</text>

<rect x="345" y="120" width="45" height="60" fill="#ef4444" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="367" y="155" fill="white" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hub M</text>

<!-- 2 Pallet Channels (P) -->
<rect x="100" y="20" width="80" height="260" fill="#dbeafe" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="140" y="155" fill="#1e3a5f" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">P</text>

<rect x="220" y="20" width="80" height="260" fill="#dbeafe" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="260" y="155" fill="#1e3a5f" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">P</text>

<!-- Dimension callouts -->
{dim_line(0, 300, 100, 300, "300", 15)}
{dim_line(100, 300, 180, 300, "200", 15)}
{dim_line(180, 300, 300, 300, "300", 15)}
{dim_line(300, 300, 400, 300, "200", 15, "#e11d48", 10)}
{dim_line(0, 300, 400, 300, "1000", 38)}

<text x="200" y="-8" fill="#555" font-size="11" font-family="sans-serif" text-anchor="middle">250 kg          500 kg          250 kg</text>
</g>

<!-- ========== MOTOR + TIMING BELT MECHANISM (USER'S CUSTOM) ========== -->
<text x="550" y="895" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">24. PALLET DRIVE MECHANISM (MOTOR + TIMING BELT + SHAFT)</text>
<text x="550" y="913" fill="#555" font-size="11" font-family="sans-serif">User's custom design: Motor drives timing belt → shaft → upper rollers push pallet along stepped guide</text>

<g transform="translate(570, 935)">
<!-- Motor body -->
<rect x="0" y="40" width="80" height="50" rx="5" fill="#d1d5db" stroke="#1e3a5f" stroke-width="2"/>
<text x="40" y="70" fill="#1e3a5f" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">MOTOR</text>
<!-- Motor pulley -->
<circle cx="90" cy="65" r="12" fill="#9ca3af" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Timing belt -->
<line x1="102" y1="60" x2="220" y2="60" stroke="#1e3a5f" stroke-width="2.5"/>
<line x1="102" y1="70" x2="220" y2="70" stroke="#1e3a5f" stroke-width="2.5"/>
<text x="160" y="55" fill="#e11d48" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">TIMING BELT</text>
<!-- Driven pulley -->
<circle cx="230" cy="65" r="15" fill="#9ca3af" stroke="#1e3a5f" stroke-width="1.5"/>
<!-- Shaft -->
<rect x="245" y="60" width="150" height="10" fill="#fed7aa" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="320" y="55" fill="#1e3a5f" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">SHAFT</text>
<!-- Upper roller on shaft end -->
<circle cx="405" cy="65" r="20" fill="#fbbf24" stroke="#1e3a5f" stroke-width="2"/>
<text x="405" y="70" fill="#1e3a5f" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">ROLLER</text>
<!-- Stepped guide rail below -->
<polygon points="350,90 370,90 380,80 420,80 430,70 470,70 470,95 350,95" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="1.5"/>
<text x="410" y="110" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">L GUIDE STEP</text>
</g>

<!-- ========== STEPPED GUIDE RAIL PROFILE ========== -->
<text x="550" y="1080" fill="#1e3a5f" font-size="16" font-family="sans-serif" font-weight="bold">25. STEPPED LINEAR GUIDE RAIL ("L GUIDE STEP")</text>
<text x="550" y="1098" fill="#555" font-size="11" font-family="sans-serif">Material: Machined C45 Steel    QTY: 2 (one per fork channel)    Length: 1000 mm</text>

<g transform="translate(570, 1115)">
<polygon points="0,100 200,100 230,70 400,70 430,35 550,35 550,110 0,110" fill="#e8f0fe" stroke="#1e3a5f" stroke-width="2"/>
<path d="M 0,100 L 200,100 L 230,70 L 400,70 L 430,35 L 550,35" fill="none" stroke="#4ade80" stroke-width="3"/>
{dim_line(0, 110, 550, 110, "1000", 15)}
<!-- Step heights -->
<text x="-15" y="107" fill="#e11d48" font-size="9" font-family="sans-serif" text-anchor="end">Step 1: 20mm</text>
<text x="-15" y="77" fill="#e11d48" font-size="9" font-family="sans-serif" text-anchor="end">Step 2: 80mm</text>
<text x="-15" y="42" fill="#e11d48" font-size="9" font-family="sans-serif" text-anchor="end">Step 3: 140mm</text>
</g>

<!-- TITLE BLOCK BOTTOM RIGHT -->
<rect x="{W-450}" y="{H-80}" width="430" height="60" fill="none" stroke="#1e3a5f" stroke-width="2"/>
<text x="{W-440}" y="{H-55}" fill="#1e3a5f" font-size="14" font-family="sans-serif" font-weight="bold">USER CUSTOM AMR — SHEET 2 OF 2</text>
<text x="{W-440}" y="{H-35}" fill="#555" font-size="11" font-family="sans-serif">REV: 8.0 | SCALE: NTS | DATE: JULY 2026 | ALL DIMS IN mm</text>

</svg>"""

# Render both sheets
for name, svg_data in [("sheet1_structural_parts", sheet1), ("sheet2_hardware_assemblies", sheet2)]:
    svg_file = f"/tmp/{name}.svg"
    png_file = f"/tmp/{name}.png"
    
    with open(svg_file, "w") as f:
        f.write(svg_data)
    
    subprocess.run(f"rsvg-convert -w {W} -h {H} {svg_file} -o {png_file}", shell=True)
    
    for d in [brain, doc]:
        subprocess.run(f"cp {png_file} {os.path.join(d, f'{name}.png')}", shell=True)
    
    sz = os.path.getsize(png_file)
    print(f"Generated: {name}.png ({sz} bytes)")

print("DONE - Both engineering drawing sheets generated.")
