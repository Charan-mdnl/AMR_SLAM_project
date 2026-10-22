import os
import subprocess

out_dir = "/home/charan/.gemini/antigravity-ide/scratch/tusk-amr-analysis"
brain_dir = "/home/charan/.gemini/antigravity-ide/brain/4ac556db-d1f1-449a-b470-f85aafe800fc"
doc_dir = "/home/charan/Documents/tusk-amr-files"

def generate_part_html(part_id, part_name, svg_content):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #0f172a;
            color: #f8fafc;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 1200px;
            height: 900px;
        }}
        .blueprint-container {{
            width: 1160px;
            height: 860px;
            border: 3px solid #38bdf8;
            background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
            box-sizing: border-box;
            position: relative;
            padding: 20px;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
        }}
        svg {{
            width: 100%;
            height: 100%;
        }}
    </style>
</head>
<body>
    <div class="blueprint-container">
        {svg_content}
    </div>
</body>
</html>"""
    return html

# --- SVG 1: FLOOR BASE PLATE (SM-001) ---
svg_sm001 = """
<svg viewBox="0 0 1120 820" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="0.5"/>
        </pattern>
    </defs>
    <rect width="1120" height="820" fill="url(#grid)"/>

    <text x="30" y="40" fill="#38bdf8" font-size="22" font-weight="bold">DETAILED PART DRAWING: PART 01 - CHASSIS FLOOR BASE PLATE (SM-001)</text>
    <text x="30" y="65" fill="#94a3b8" font-size="14">MATERIAL: CRCA STEEL (6.0 mm) | ALL DIMENSIONS IN MILLIMETERS (mm) | SCALE 1:10</text>

    <g transform="translate(160, 120)">
        <text x="400" y="-20" fill="#38bdf8" font-size="16" text-anchor="middle" font-weight="bold">TOP PLAN VIEW (1200 mm x 1000 mm)</text>
        
        <polygon points="40,0 760,0 800,40 800,620 760,660 40,660 0,620 0,40" fill="none" stroke="#f8fafc" stroke-width="3"/>
        
        <text x="770" y="25" fill="#f59e0b" font-size="11">40x45°</text>
        
        <rect x="250" y="230" width="300" height="200" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,4"/>
        <text x="400" y="335" fill="#94a3b8" font-size="13" text-anchor="middle">CENTER CLEARANCE CUTOUT (300 x 200 mm)</text>

        <rect x="60" y="260" width="140" height="140" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
        <text x="130" y="335" fill="#ef4444" font-size="11" text-anchor="middle">DRIVE WHEEL (L)<br/>220x70 mm</text>

        <rect x="600" y="260" width="140" height="140" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
        <text x="670" y="335" fill="#ef4444" font-size="11" text-anchor="middle">DRIVE WHEEL (R)<br/>220x70 mm</text>

        <circle cx="50" cy="50" r="12" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="750" cy="50" r="12" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="50" cy="610" r="12" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="750" cy="610" r="12" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <text x="50" y="30" fill="#38bdf8" font-size="10" text-anchor="middle">4x Ø9 THRU</text>

        <line x1="150" y1="40" x2="150" y2="620" stroke="#4ade80" stroke-width="2" stroke-dasharray="8,4"/>
        <line x1="650" y1="40" x2="650" y2="620" stroke="#4ade80" stroke-width="2" stroke-dasharray="8,4"/>
        <text x="150" y="20" fill="#4ade80" font-size="11" text-anchor="middle">STEPPED RAIL MOUNT LINE (L)</text>
        <text x="650" y="20" fill="#4ade80" font-size="11" text-anchor="middle">STEPPED RAIL MOUNT LINE (R)</text>

        <line x1="0" y1="-35" x2="800" y2="-35" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="400" y="-42" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">1200.0 mm (LENGTH)</text>

        <line x1="-35" y1="0" x2="-35" y2="660" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="-45" y="330" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle" transform="rotate(-90 -45 330)">1000.0 mm (WIDTH)</text>

        <line x1="150" y1="685" x2="650" y2="685" stroke="#4ade80" stroke-width="1.5"/>
        <text x="400" y="700" fill="#4ade80" font-size="12" text-anchor="middle">800.0 mm (RAIL SPACING C-C)</text>
    </g>

    <g transform="translate(750, 680)">
        <rect width="340" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="35" x2="340" y2="35" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="70" x2="340" y2="70" stroke="#38bdf8" stroke-width="1"/>
        <text x="10" y="25" fill="#f8fafc" font-size="14" font-weight="bold">TUSK E10 TITAN AMR - PART 01</text>
        <text x="10" y="58" fill="#94a3b8" font-size="12">DWG NO: SM-001 | REV: 3.0</text>
        <text x="10" y="93" fill="#94a3b8" font-size="12">SHEET METAL: 6.0 mm CRCA STEEL</text>
    </g>
</svg>
"""

# --- SVG 2: SIDEWALLS (SM-002 & SM-003) ---
svg_sm002 = """
<svg viewBox="0 0 1120 820" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="0.5"/>
        </pattern>
    </defs>
    <rect width="1120" height="820" fill="url(#grid)"/>

    <text x="30" y="40" fill="#38bdf8" font-size="22" font-weight="bold">DETAILED PART DRAWING: PART 02 - OUTER SIDEWALLS (SM-002 / SM-003)</text>
    <text x="30" y="65" fill="#94a3b8" font-size="14">MATERIAL: CRCA STEEL (3.0 mm) | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (LEFT &amp; RIGHT)</text>

    <!-- FLAT PATTERN (UNFOLDED) -->
    <g transform="translate(100, 150)">
        <text x="450" y="-30" fill="#38bdf8" font-size="16" text-anchor="middle" font-weight="bold">FLAT PATTERN - UNFOLDED SHEET (1200 mm x 230 mm)</text>
        <rect x="0" y="0" width="900" height="180" fill="#1e293b" stroke="#f8fafc" stroke-width="3"/>

        <!-- Bend Lines (30mm from top and bottom) -->
        <line x1="0" y1="25" x2="900" y2="25" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6,4"/>
        <line x1="0" y1="155" x2="900" y2="155" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6,4"/>
        <text x="450" y="18" fill="#f59e0b" font-size="11" text-anchor="middle">BEND LINE 90° INWARD (R3)</text>
        <text x="450" y="172" fill="#f59e0b" font-size="11" text-anchor="middle">BEND LINE 90° INWARD (R3)</text>

        <!-- Drive Wheel Slot Cutout -->
        <rect x="360" y="25" width="180" height="130" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
        <text x="450" y="95" fill="#ef4444" font-size="12" text-anchor="middle">DRIVE WHEEL SLOT<br/>240 x 100 mm</text>

        <!-- Dimensions -->
        <line x1="0" y1="-10" x2="900" y2="-10" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="-18" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">1200.0 mm (FLAT LENGTH)</text>

        <line x1="-20" y1="0" x2="-20" y2="180" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-30" y="90" fill="#4ade80" font-size="12" text-anchor="end">230.0 mm (FLAT HEIGHT)</text>
    </g>

    <!-- FORMED PROFILE (SIDE VIEW) -->
    <g transform="translate(100, 440)">
        <text x="450" y="-20" fill="#38bdf8" font-size="16" text-anchor="middle" font-weight="bold">FORMED SIDE ELEVATION (170 mm FORMED HEIGHT)</text>
        <rect x="0" y="0" width="900" height="130" fill="#1e293b" stroke="#f8fafc" stroke-width="3"/>
        <rect x="360" y="0" width="180" height="130" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
        <text x="450" y="70" fill="#ef4444" font-size="12" text-anchor="middle">DRIVE WHEEL CLEARANCE SLOT</text>

        <line x1="-20" y1="0" x2="-20" y2="130" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-30" y="65" fill="#4ade80" font-size="12" text-anchor="end">170.0 mm (FORMED H)</text>
    </g>

    <!-- TITLE BLOCK -->
    <g transform="translate(750, 680)">
        <rect width="340" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="35" x2="340" y2="35" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="70" x2="340" y2="70" stroke="#38bdf8" stroke-width="1"/>
        <text x="10" y="25" fill="#f8fafc" font-size="14" font-weight="bold">TUSK E10 TITAN AMR - PART 02</text>
        <text x="10" y="58" fill="#94a3b8" font-size="12">DWG NO: SM-002 / SM-003 | REV: 3.0</text>
        <text x="10" y="93" fill="#94a3b8" font-size="12">CRCA STEEL (3.0 mm) | BEND R3</text>
    </g>
</svg>
"""

# --- SVG 3: STEPPED LINEAR GUIDE RAIL (SG-001) ---
svg_sg001 = """
<svg viewBox="0 0 1120 820" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="0.5"/>
        </pattern>
    </defs>
    <rect width="1120" height="820" fill="url(#grid)"/>

    <text x="30" y="40" fill="#38bdf8" font-size="22" font-weight="bold">DETAILED PART DRAWING: PART 04 - STEPPED LINEAR GUIDE RAIL (SG-001 / SG-002)</text>
    <text x="30" y="65" fill="#94a3b8" font-size="14">MATERIAL: MACHINED C45 STEEL | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (PAIR)</text>

    <g transform="translate(100, 180)">
        <text x="450" y="-40" fill="#38bdf8" font-size="16" text-anchor="middle" font-weight="bold">ELEVATION PROFILE (STEPPED STAIRCASE GEOMETRY)</text>

        <polygon points="0,220 380,220 440,160 680,160 740,100 960,100 960,260 0,260" fill="#1e293b" stroke="#f8fafc" stroke-width="3"/>
        <path d="M 0,220 L 380,220 L 440,160 L 680,160 L 740,100 L 960,100" fill="none" stroke="#4ade80" stroke-width="4"/>

        <rect x="120" y="180" width="80" height="40" rx="4" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
        <text x="160" y="170" fill="#ef4444" font-size="11" text-anchor="middle">CARRIAGE (POS A - 90mm Entry)</text>

        <rect x="800" y="60" width="80" height="40" rx="4" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <text x="840" y="45" fill="#38bdf8" font-size="11" text-anchor="middle">CARRIAGE (POS C - 170mm Lifted)</text>

        <circle cx="50" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="200" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="350" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="500" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="650" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="800" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="910" cy="245" r="4" fill="#f8fafc"/>
        <text x="480" y="285" fill="#94a3b8" font-size="11" text-anchor="middle">M8 COUNTERSUNK MOUNTING HOLES (100mm PITCH)</text>

        <line x1="0" y1="310" x2="960" y2="310" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="480" y="330" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">1100.0 mm (TOTAL RAIL LENGTH)</text>

        <line x1="-30" y1="260" x2="-30" y2="220" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-40" y="243" fill="#4ade80" font-size="12" text-anchor="end">20 mm (STEP 1)</text>

        <line x1="-30" y1="260" x2="-30" y2="160" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-40" y="195" fill="#4ade80" font-size="12" text-anchor="end">60 mm (STEP 2)</text>

        <line x1="-30" y1="260" x2="-30" y2="100" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-40" y="135" fill="#4ade80" font-size="12" text-anchor="end">100 mm (STEP 3)</text>

        <text x="410" y="200" fill="#f59e0b" font-size="12">30° RAMP</text>
        <text x="710" y="140" fill="#f59e0b" font-size="12">30° RAMP</text>
    </g>

    <g transform="translate(150, 560)">
        <text x="100" y="-20" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">CROSS-SECTION A-A (RAIL + BLOCK)</text>
        <rect x="60" y="30" width="80" height="120" fill="#1e293b" stroke="#f8fafc" stroke-width="2"/>
        <path d="M 80,30 L 100,10 L 120,30" fill="none" stroke="#4ade80" stroke-width="3"/>
        <rect x="70" y="-20" width="60" height="50" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="85" cy="5" r="5" fill="#f59e0b"/>
        <circle cx="115" cy="5" r="5" fill="#f59e0b"/>
        <text x="100" y="175" fill="#94a3b8" font-size="12" text-anchor="middle">RAIL WIDTH: 25 mm | BLOCK: 80x50 mm</text>
    </g>

    <g transform="translate(750, 680)">
        <rect width="340" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="35" x2="340" y2="35" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="70" x2="340" y2="70" stroke="#38bdf8" stroke-width="1"/>
        <text x="10" y="25" fill="#f8fafc" font-size="14" font-weight="bold">TUSK E10 TITAN AMR - PART 04</text>
        <text x="10" y="58" fill="#94a3b8" font-size="12">DWG NO: SG-001 / SG-002 | REV: 3.0</text>
        <text x="10" y="93" fill="#94a3b8" font-size="12">MACHINED C45 STEEL (STEPPED PROFILE)</text>
    </g>
</svg>
"""

# --- SVG 4: FORK TINES & CARRIAGE (FC-001 & FC-003) ---
svg_fc001 = """
<svg viewBox="0 0 1120 820" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="0.5"/>
        </pattern>
    </defs>
    <rect width="1120" height="820" fill="url(#grid)"/>

    <text x="30" y="40" fill="#38bdf8" font-size="22" font-weight="bold">DETAILED PART DRAWING: PART 05 &amp; 06 - FORK CARRIAGE &amp; TINES (FC-001 &amp; FC-003)</text>
    <text x="30" y="65" fill="#94a3b8" font-size="14">MATERIAL: CRCA 6mm BASE &amp; 100x40x3mm BOX TINES | ALL DIMENSIONS IN MILLIMETERS (mm)</text>

    <g transform="translate(100, 150)">
        <text x="450" y="-30" fill="#38bdf8" font-size="16" text-anchor="middle" font-weight="bold">SIDE ELEVATION - FORK TINE (1100 mm TOTAL LENGTH)</text>
        
        <polygon points="0,40 750,40 900,100 0,100" fill="#1e293b" stroke="#f8fafc" stroke-width="3"/>
        <rect x="-30" y="10" width="30" height="110" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>
        <circle cx="-15" cy="30" r="5" fill="#0f172a"/>
        <circle cx="-15" cy="100" r="5" fill="#0f172a"/>

        <line x1="0" y1="130" x2="900" y2="130" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="150" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">1100.0 mm (TOTAL FORK LENGTH)</text>

        <line x1="-50" y1="40" x2="-50" y2="100" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-60" y="75" fill="#4ade80" font-size="13" text-anchor="end">100.0 mm (HEIGHT)</text>

        <line x1="920" y1="100" x2="920" y2="90" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="930" y="98" fill="#f59e0b" font-size="12">20.0 mm TIP</text>

        <text x="820" y="60" fill="#f59e0b" font-size="12">150mm TAPER</text>
    </g>

    <g transform="translate(150, 420)">
        <text x="400" y="-20" fill="#38bdf8" font-size="16" text-anchor="middle" font-weight="bold">CARRIAGE PLATFORM TOP PLAN (940 mm x 400 mm)</text>
        <rect x="0" y="0" width="800" height="200" fill="#1e293b" stroke="#f8fafc" stroke-width="3"/>

        <rect x="160" y="0" width="40" height="200" fill="#38bdf8" opacity="0.3"/>
        <rect x="600" y="0" width="40" height="200" fill="#38bdf8" opacity="0.3"/>
        <text x="180" y="105" fill="#4ade80" font-size="12" text-anchor="middle" transform="rotate(-90 180 105)">FORK TINE 1</text>
        <text x="620" y="105" fill="#4ade80" font-size="12" text-anchor="middle" transform="rotate(-90 620 105)">FORK TINE 2</text>

        <line x1="180" y1="230" x2="620" y2="230" stroke="#4ade80" stroke-width="1.5"/>
        <text x="400" y="248" fill="#4ade80" font-size="14" font-weight="bold" text-anchor="middle">560.0 mm (FORK SPACING C-C)</text>

        <line x1="0" y1="-10" x2="800" y2="-10" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="400" y="-18" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">940.0 mm (CARRIAGE WIDTH)</text>
    </g>

    <g transform="translate(750, 680)">
        <rect width="340" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="35" x2="340" y2="35" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="70" x2="340" y2="70" stroke="#38bdf8" stroke-width="1"/>
        <text x="10" y="25" fill="#f8fafc" font-size="14" font-weight="bold">TUSK E10 TITAN AMR - PART 05 &amp; 06</text>
        <text x="10" y="58" fill="#94a3b8" font-size="12">DWG NO: FC-001 / FC-003 | REV: 3.0</text>
        <text x="10" y="93" fill="#94a3b8" font-size="12">CRCA STEEL &amp; STRUCTURAL BOX SECTION</text>
    </g>
</svg>
"""

# --- SVG 5: SCISSOR LINKAGE ARMS (SA-001 & SA-002) ---
svg_sa001 = """
<svg viewBox="0 0 1120 820" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="0.5"/>
        </pattern>
    </defs>
    <rect width="1120" height="820" fill="url(#grid)"/>

    <text x="30" y="40" fill="#38bdf8" font-size="22" font-weight="bold">DETAILED PART DRAWING: PART 07 - SCISSOR LINKAGE ARMS (SA-001 / SA-002)</text>
    <text x="30" y="65" fill="#94a3b8" font-size="14">MATERIAL: 60x40x6mm RHS TUBE (Q235 STEEL) | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (PAIR)</text>

    <!-- FRONT ELEVATION OF LINKAGE ARM -->
    <g transform="translate(100, 200)">
        <text x="450" y="-40" fill="#38bdf8" font-size="16" text-anchor="middle" font-weight="bold">FRONT ELEVATION - SCISSOR ARM (760 mm OVERALL LENGTH)</text>
        
        <!-- Arm Main Tube with Rounded Ends -->
        <rect x="0" y="0" width="900" height="100" rx="50" ry="50" fill="#1e293b" stroke="#f8fafc" stroke-width="3"/>

        <!-- 3 Reamed Pivot Bores with Bronze Bushings -->
        <circle cx="50" cy="50" r="24" fill="#0f172a" stroke="#4ade80" stroke-width="3"/>
        <circle cx="50" cy="50" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="50" y="95" fill="#4ade80" font-size="11" text-anchor="middle">Ø20 H7 (End 1)</text>

        <circle cx="450" cy="50" r="24" fill="#0f172a" stroke="#4ade80" stroke-width="3"/>
        <circle cx="450" cy="50" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="450" y="95" fill="#4ade80" font-size="11" text-anchor="middle">Ø20 H7 (Center Pivot)</text>

        <circle cx="850" cy="50" r="24" fill="#0f172a" stroke="#4ade80" stroke-width="3"/>
        <circle cx="850" cy="50" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="850" y="95" fill="#4ade80" font-size="11" text-anchor="middle">Ø20 H7 (End 2)</text>

        <!-- Dimension Lines -->
        <line x1="50" y1="130" x2="850" y2="130" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="150" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">720.0 mm (HOLE-TO-HOLE CENTER DISTANCE)</text>

        <line x1="0" y1="-15" x2="900" y2="-15" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="-25" fill="#f8fafc" font-size="13" text-anchor="middle">760.0 mm (OVERALL CUT LENGTH)</text>

        <line x1="-20" y1="0" x2="-20" y2="100" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-30" y="55" fill="#4ade80" font-size="13" text-anchor="end">60.0 mm (HEIGHT)</text>
    </g>

    <!-- TUBE CROSS-SECTION -->
    <g transform="translate(200, 520)">
        <text x="100" y="-20" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">TUBE CROSS-SECTION (60x40x6 mm)</text>
        <rect x="50" y="10" width="100" height="140" fill="#1e293b" stroke="#f8fafc" stroke-width="3"/>
        <rect x="65" y="25" width="70" height="110" fill="#0f172a" stroke="#94a3b8" stroke-width="1.5"/>
        <text x="100" y="175" fill="#94a3b8" font-size="12" text-anchor="middle">6.0 mm WALL THICKNESS</text>
    </g>

    <!-- TITLE BLOCK -->
    <g transform="translate(750, 680)">
        <rect width="340" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="35" x2="340" y2="35" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="70" x2="340" y2="70" stroke="#38bdf8" stroke-width="1"/>
        <text x="10" y="25" fill="#f8fafc" font-size="14" font-weight="bold">TUSK E10 TITAN AMR - PART 07</text>
        <text x="10" y="58" fill="#94a3b8" font-size="12">DWG NO: SA-001 / SA-002 | REV: 3.0</text>
        <text x="10" y="93" fill="#94a3b8" font-size="12">60x40x6 mm RHS TUBE | BRONZE BUSHED</text>
    </g>
</svg>
"""

# Save HTML files to /tmp/ and convert via Brave screenshot
parts = [
    ("part_01_floor_plate", svg_sm001),
    ("part_02_sidewalls", svg_sm002),
    ("part_04_stepped_rail", svg_sg001),
    ("part_05_fork_carriage", svg_fc001),
    ("part_07_scissor_arms", svg_sa001)
]

for name, svg in parts:
    html_str = generate_part_html(name, name, svg)
    tmp_html = f"/tmp/{name}.html"
    tmp_png = f"/tmp/{name}.png"
    
    out_png = os.path.join(out_dir, f"{name}.png")
    brain_png = os.path.join(brain_dir, f"{name}.png")
    doc_png = os.path.join(doc_dir, f"{name}.png")
    
    with open(tmp_html, "w") as f:
        f.write(html_str)
        
    cmd = f"brave --headless --disable-gpu --screenshot={tmp_png} --window-size=1200,900 file://{tmp_html}"
    subprocess.run(cmd, shell=True)
    
    subprocess.run(f"cp {tmp_png} {out_png}", shell=True)
    subprocess.run(f"cp {tmp_png} {brain_png}", shell=True)
    subprocess.run(f"cp {tmp_png} {doc_png}", shell=True)
    print(f"Successfully rendered and copied {name}.png")

