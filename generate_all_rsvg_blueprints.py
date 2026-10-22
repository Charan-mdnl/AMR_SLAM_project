import os
import subprocess

scratch_dir = "/home/charan/.gemini/antigravity-ide/scratch/tusk-amr-analysis"
brain_dir = "/home/charan/.gemini/antigravity-ide/brain/4ac556db-d1f1-449a-b470-f85aafe800fc"
doc_dir = "/home/charan/Documents/tusk-amr-files"
pict_dir = "/home/charan/Pictures/blueprints"

os.makedirs(scratch_dir, exist_ok=True)
os.makedirs(doc_dir, exist_ok=True)
os.makedirs(pict_dir, exist_ok=True)

# -------------------------------------------------------------
# SVG PART 01: FLOOR BASE PLATE (SM-001)
# -------------------------------------------------------------
svg_p1 = """<svg width="1200" height="900" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="900" fill="#0f172a"/>
    <rect x="20" y="20" width="1160" height="860" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>

    <!-- HEADER -->
    <text x="50" y="60" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold">DETAILED PART DRAWING: PART 01 - CHASSIS FLOOR BASE PLATE (SM-001)</text>
    <text x="50" y="85" fill="#94a3b8" font-size="14" font-family="sans-serif">MATERIAL: CRCA STEEL (6.0 mm) | ALL DIMENSIONS IN MILLIMETERS (mm) | SCALE 1:10</text>
    <line x1="50" y1="100" x2="1110" y2="100" stroke="#334155" stroke-width="2"/>

    <!-- TOP PLAN VIEW -->
    <g transform="translate(180, 150)">
        <text x="400" y="-15" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">TOP PLAN VIEW (1200 mm x 1000 mm)</text>
        
        <!-- Main Plate Contour with Chamfers -->
        <polygon points="40,0 760,0 800,40 800,560 760,600 40,600 0,560 0,40" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        <text x="765" y="25" fill="#f59e0b" font-size="11" font-family="sans-serif">40x45°</text>
        
        <!-- Center Clearance Cutout -->
        <rect x="250" y="200" width="300" height="200" fill="#1e293b" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,4"/>
        <text x="400" y="305" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">CENTER CLEARANCE CUTOUT (300 x 200 mm)</text>

        <!-- Drive Wheel Cutouts -->
        <rect x="60" y="230" width="140" height="140" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
        <text x="130" y="305" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle">DRIVE WHEEL (L)<br/>220x70 mm</text>

        <rect x="600" y="230" width="140" height="140" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
        <text x="670" y="305" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle">DRIVE WHEEL (R)<br/>220x70 mm</text>

        <!-- Caster Mount Holes -->
        <circle cx="50" cy="50" r="10" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="750" cy="50" r="10" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="50" cy="550" r="10" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="750" cy="550" r="10" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <text x="50" y="30" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">4x Ø9 THRU</text>

        <!-- Stepped Rail Lines -->
        <line x1="150" y1="30" x2="150" y2="570" stroke="#4ade80" stroke-width="2" stroke-dasharray="8,4"/>
        <line x1="650" y1="30" x2="650" y2="570" stroke="#4ade80" stroke-width="2" stroke-dasharray="8,4"/>
        <text x="150" y="15" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle">STEPPED RAIL MOUNT (L)</text>
        <text x="650" y="15" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle">STEPPED RAIL MOUNT (R)</text>

        <!-- Dimensions -->
        <line x1="0" y1="-30" x2="800" y2="-30" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="400" y="-35" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">1200.0 mm (LENGTH)</text>

        <line x1="-30" y1="0" x2="-30" y2="600" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="-40" y="300" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle" transform="rotate(-90 -40 300)">1000.0 mm (WIDTH)</text>

        <line x1="150" y1="625" x2="650" y2="625" stroke="#4ade80" stroke-width="1.5"/>
        <text x="400" y="642" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle">800.0 mm (RAIL SPACING C-C)</text>
    </g>

    <!-- TITLE BLOCK -->
    <g transform="translate(800, 740)">
        <rect width="360" height="120" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="80" x2="360" y2="80" stroke="#38bdf8" stroke-width="1"/>
        <text x="15" y="28" fill="#f8fafc" font-size="15" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 01</text>
        <text x="15" y="65" fill="#94a3b8" font-size="13" font-family="sans-serif">DWG NO: SM-001 | REV: 3.0</text>
        <text x="15" y="105" fill="#94a3b8" font-size="13" font-family="sans-serif">SHEET METAL: 6.0 mm CRCA STEEL</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# SVG PART 02: OUTER SIDEWALLS (SM-002 / SM-003)
# -------------------------------------------------------------
svg_p2 = """<svg width="1200" height="900" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="900" fill="#0f172a"/>
    <rect x="20" y="20" width="1160" height="860" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>

    <text x="50" y="60" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold">DETAILED PART DRAWING: PART 02 - OUTER SIDEWALLS (SM-002 / SM-003)</text>
    <text x="50" y="85" fill="#94a3b8" font-size="14" font-family="sans-serif">MATERIAL: CRCA STEEL (3.0 mm) | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (LEFT &amp; RIGHT)</text>
    <line x1="50" y1="100" x2="1110" y2="100" stroke="#334155" stroke-width="2"/>

    <!-- FLAT PATTERN (UNFOLDED) -->
    <g transform="translate(140, 160)">
        <text x="450" y="-25" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">FLAT PATTERN - UNFOLDED SHEET (1200 mm x 230 mm)</text>
        <rect x="0" y="0" width="900" height="180" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>

        <!-- Bend Lines -->
        <line x1="0" y1="25" x2="900" y2="25" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6,4"/>
        <line x1="0" y1="155" x2="900" y2="155" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6,4"/>
        <text x="450" y="18" fill="#f59e0b" font-size="11" font-family="sans-serif" text-anchor="middle">BEND LINE 90° INWARD (R3)</text>
        <text x="450" y="172" fill="#f59e0b" font-size="11" font-family="sans-serif" text-anchor="middle">BEND LINE 90° INWARD (R3)</text>

        <!-- Drive Wheel Slot Cutout -->
        <rect x="360" y="25" width="180" height="130" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
        <text x="450" y="95" fill="#ef4444" font-size="12" font-family="sans-serif" text-anchor="middle">DRIVE WHEEL SLOT<br/>240 x 100 mm</text>

        <!-- Dimensions -->
        <line x1="0" y1="-10" x2="900" y2="-10" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="-18" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">1200.0 mm (FLAT LENGTH)</text>

        <line x1="-20" y1="0" x2="-20" y2="180" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-30" y="90" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="end">230.0 mm (FLAT H)</text>
    </g>

    <!-- FORMED PROFILE -->
    <g transform="translate(140, 460)">
        <text x="450" y="-20" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">FORMED SIDE ELEVATION (170 mm FORMED HEIGHT)</text>
        <rect x="0" y="0" width="900" height="130" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        <rect x="360" y="0" width="180" height="130" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
        <text x="450" y="70" fill="#ef4444" font-size="12" font-family="sans-serif" text-anchor="middle">DRIVE WHEEL CLEARANCE SLOT</text>

        <line x1="-20" y1="0" x2="-20" y2="130" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-30" y="65" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="end">170.0 mm (FORMED H)</text>
    </g>

    <g transform="translate(800, 740)">
        <rect width="360" height="120" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="80" x2="360" y2="80" stroke="#38bdf8" stroke-width="1"/>
        <text x="15" y="28" fill="#f8fafc" font-size="15" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 02</text>
        <text x="15" y="65" fill="#94a3b8" font-size="13" font-family="sans-serif">DWG NO: SM-002 / SM-003 | REV: 3.0</text>
        <text x="15" y="105" fill="#94a3b8" font-size="13" font-family="sans-serif">CRCA STEEL (3.0 mm) | BEND R3</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# SVG PART 03: FRONT & REAR END WALLS (SM-004 / SM-005)
# -------------------------------------------------------------
svg_p3 = """<svg width="1200" height="900" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="900" fill="#0f172a"/>
    <rect x="20" y="20" width="1160" height="860" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>

    <text x="50" y="60" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold">DETAILED PART DRAWING: PART 03 - FRONT &amp; REAR END WALLS (SM-004 / SM-005)</text>
    <text x="50" y="85" fill="#94a3b8" font-size="14" font-family="sans-serif">MATERIAL: CRCA STEEL (3.0 mm) | ALL DIMENSIONS IN MILLIMETERS (mm)</text>
    <line x1="50" y1="100" x2="1110" y2="100" stroke="#334155" stroke-width="2"/>

    <g transform="translate(140, 170)">
        <text x="450" y="-25" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT END WALL (SM-004) - FORMED VIEW WITH DUAL FORK SLOTS</text>
        <rect x="0" y="0" width="900" height="150" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>

        <rect x="180" y="60" width="100" height="90" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
        <text x="230" y="110" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle">FORK SLOT 1<br/>110x50 mm</text>

        <rect x="620" y="60" width="100" height="90" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
        <text x="670" y="110" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle">FORK SLOT 2<br/>110x50 mm</text>

        <line x1="230" y1="180" x2="670" y2="180" stroke="#4ade80" stroke-width="1.5"/>
        <text x="450" y="195" fill="#4ade80" font-size="13" font-family="sans-serif" text-anchor="middle">560.0 mm (FORK SLOT CENTER SPACING)</text>

        <line x1="0" y1="-10" x2="900" y2="-10" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="-18" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">994.0 mm (FORMED WIDTH)</text>
    </g>

    <g transform="translate(140, 470)">
        <text x="450" y="-20" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">REAR END WALL (SM-005) - CLOSED PROFILE</text>
        <rect x="0" y="0" width="900" height="150" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        <text x="450" y="80" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">SOLID REAR WALL WITH SENSOR MOUNT HOLES</text>
    </g>

    <g transform="translate(800, 740)">
        <rect width="360" height="120" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="80" x2="360" y2="80" stroke="#38bdf8" stroke-width="1"/>
        <text x="15" y="28" fill="#f8fafc" font-size="15" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 03</text>
        <text x="15" y="65" fill="#94a3b8" font-size="13" font-family="sans-serif">DWG NO: SM-004 / SM-005 | REV: 3.0</text>
        <text x="15" y="105" fill="#94a3b8" font-size="13" font-family="sans-serif">CRCA STEEL (3.0 mm) | DUAL SLOTS</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# SVG PART 04: STEPPED LINEAR GUIDE RAIL (SG-001 / SG-002)
# -------------------------------------------------------------
svg_p4 = """<svg width="1200" height="900" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="900" fill="#0f172a"/>
    <rect x="20" y="20" width="1160" height="860" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>

    <text x="50" y="60" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold">DETAILED PART DRAWING: PART 04 - STEPPED LINEAR GUIDE RAIL (SG-001 / SG-002)</text>
    <text x="50" y="85" fill="#94a3b8" font-size="14" font-family="sans-serif">MATERIAL: MACHINED C45 STEEL | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (PAIR)</text>
    <line x1="50" y1="100" x2="1110" y2="100" stroke="#334155" stroke-width="2"/>

    <g transform="translate(140, 180)">
        <text x="450" y="-35" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ELEVATION PROFILE (STEPPED STAIRCASE GEOMETRY)</text>

        <polygon points="0,220 380,220 440,160 680,160 740,100 900,100 900,260 0,260" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        <path d="M 0,220 L 380,220 L 440,160 L 680,160 L 740,100 L 900,100" fill="none" stroke="#4ade80" stroke-width="4"/>

        <rect x="120" y="180" width="80" height="40" rx="4" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
        <text x="160" y="170" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle">CARRIAGE (POS A - 90mm Entry)</text>

        <rect x="780" y="60" width="80" height="40" rx="4" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <text x="820" y="45" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle">CARRIAGE (POS C - 170mm Lifted)</text>

        <circle cx="50" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="200" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="350" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="500" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="650" cy="245" r="4" fill="#f8fafc"/>
        <circle cx="800" cy="245" r="4" fill="#f8fafc"/>
        <text x="450" y="285" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">M8 COUNTERSUNK MOUNTING HOLES (100mm PITCH)</text>

        <line x1="0" y1="310" x2="900" y2="310" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="330" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">1100.0 mm (TOTAL RAIL LENGTH)</text>

        <line x1="-30" y1="260" x2="-30" y2="220" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-40" y="243" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="end">20 mm (STEP 1)</text>

        <line x1="-30" y1="260" x2="-30" y2="160" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-40" y="195" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="end">60 mm (STEP 2)</text>

        <line x1="-30" y1="260" x2="-30" y2="100" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-40" y="135" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="end">100 mm (STEP 3)</text>

        <text x="410" y="200" fill="#f59e0b" font-size="12" font-family="sans-serif">30° RAMP</text>
        <text x="710" y="140" fill="#f59e0b" font-size="12" font-family="sans-serif">30° RAMP</text>
    </g>

    <g transform="translate(180, 560)">
        <text x="100" y="-20" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">CROSS-SECTION A-A (RAIL + BLOCK)</text>
        <rect x="60" y="30" width="80" height="120" fill="#0f172a" stroke="#f8fafc" stroke-width="2"/>
        <path d="M 80,30 L 100,10 L 120,30" fill="none" stroke="#4ade80" stroke-width="3"/>
        <rect x="70" y="-20" width="60" height="50" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="85" cy="5" r="5" fill="#f59e0b"/>
        <circle cx="115" cy="5" r="5" fill="#f59e0b"/>
        <text x="100" y="175" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">RAIL WIDTH: 25 mm | BLOCK: 80x50 mm</text>
    </g>

    <g transform="translate(800, 740)">
        <rect width="360" height="120" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="80" x2="360" y2="80" stroke="#38bdf8" stroke-width="1"/>
        <text x="15" y="28" fill="#f8fafc" font-size="15" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 04</text>
        <text x="15" y="65" fill="#94a3b8" font-size="13" font-family="sans-serif">DWG NO: SG-001 / SG-002 | REV: 3.0</text>
        <text x="15" y="105" fill="#94a3b8" font-size="13" font-family="sans-serif">MACHINED C45 STEEL (STEPPED PROFILE)</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# SVG PART 05 & 06: FORK CARRIAGE & TINES (FC-001 & FC-003)
# -------------------------------------------------------------
svg_p5 = """<svg width="1200" height="900" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="900" fill="#0f172a"/>
    <rect x="20" y="20" width="1160" height="860" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>

    <text x="50" y="60" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold">DETAILED PART DRAWING: PART 05 &amp; 06 - FORK CARRIAGE &amp; TINES (FC-001 &amp; FC-003)</text>
    <text x="50" y="85" fill="#94a3b8" font-size="14" font-family="sans-serif">MATERIAL: CRCA 6mm BASE &amp; 100x40x3mm BOX TINES | ALL DIMENSIONS IN MILLIMETERS (mm)</text>
    <line x1="50" y1="100" x2="1110" y2="100" stroke="#334155" stroke-width="2"/>

    <g transform="translate(140, 160)">
        <text x="450" y="-25" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE ELEVATION - FORK TINE (1100 mm TOTAL LENGTH)</text>
        
        <polygon points="0,40 750,40 900,100 0,100" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        <rect x="-30" y="10" width="30" height="110" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>
        <circle cx="-15" cy="30" r="5" fill="#0f172a"/>
        <circle cx="-15" cy="100" r="5" fill="#0f172a"/>

        <line x1="0" y1="130" x2="900" y2="130" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="150" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">1100.0 mm (TOTAL FORK LENGTH)</text>

        <line x1="-50" y1="40" x2="-50" y2="100" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-60" y="75" fill="#4ade80" font-size="13" font-family="sans-serif" text-anchor="end">100.0 mm (H)</text>

        <text x="830" y="60" fill="#f59e0b" font-size="12" font-family="sans-serif">150mm TAPER (20mm TIP)</text>
    </g>

    <g transform="translate(190, 440)">
        <text x="400" y="-20" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">CARRIAGE PLATFORM TOP PLAN (940 mm x 400 mm)</text>
        <rect x="0" y="0" width="800" height="200" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>

        <rect x="160" y="0" width="40" height="200" fill="#38bdf8" opacity="0.4"/>
        <rect x="600" y="0" width="40" height="200" fill="#38bdf8" opacity="0.4"/>
        <text x="180" y="105" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 180 105)">FORK TINE 1</text>
        <text x="620" y="105" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 620 105)">FORK TINE 2</text>

        <line x1="180" y1="225" x2="620" y2="225" stroke="#4ade80" stroke-width="1.5"/>
        <text x="400" y="242" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">560.0 mm (FORK SPACING C-C)</text>

        <line x1="0" y1="-10" x2="800" y2="-10" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="400" y="-18" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">940.0 mm (CARRIAGE WIDTH)</text>
    </g>

    <g transform="translate(800, 740)">
        <rect width="360" height="120" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="80" x2="360" y2="80" stroke="#38bdf8" stroke-width="1"/>
        <text x="15" y="28" fill="#f8fafc" font-size="15" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 05 &amp; 06</text>
        <text x="15" y="65" fill="#94a3b8" font-size="13" font-family="sans-serif">DWG NO: FC-001 / FC-003 | REV: 3.0</text>
        <text x="15" y="105" fill="#94a3b8" font-size="13" font-family="sans-serif">CRCA STEEL &amp; STRUCTURAL BOX SECTION</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# SVG PART 07: SCISSOR LINKAGE ARMS (SA-001 / SA-002)
# -------------------------------------------------------------
svg_p7 = """<svg width="1200" height="900" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="900" fill="#0f172a"/>
    <rect x="20" y="20" width="1160" height="860" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>

    <text x="50" y="60" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold">DETAILED PART DRAWING: PART 07 - SCISSOR LINKAGE ARMS (SA-001 / SA-002)</text>
    <text x="50" y="85" fill="#94a3b8" font-size="14" font-family="sans-serif">MATERIAL: 60x40x6mm RHS TUBE (Q235 STEEL) | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (PAIR)</text>
    <line x1="50" y1="100" x2="1110" y2="100" stroke="#334155" stroke-width="2"/>

    <g transform="translate(140, 200)">
        <text x="450" y="-35" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT ELEVATION - SCISSOR ARM (760 mm OVERALL LENGTH)</text>
        
        <rect x="0" y="0" width="900" height="100" rx="50" ry="50" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>

        <circle cx="50" cy="50" r="24" fill="#1e293b" stroke="#4ade80" stroke-width="3"/>
        <circle cx="50" cy="50" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="50" y="95" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle">Ø20 H7 (End 1)</text>

        <circle cx="450" cy="50" r="24" fill="#1e293b" stroke="#4ade80" stroke-width="3"/>
        <circle cx="450" cy="50" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="450" y="95" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle">Ø20 H7 (Center Pivot)</text>

        <circle cx="850" cy="50" r="24" fill="#1e293b" stroke="#4ade80" stroke-width="3"/>
        <circle cx="850" cy="50" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="850" y="95" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle">Ø20 H7 (End 2)</text>

        <line x1="50" y1="130" x2="850" y2="130" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="150" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">720.0 mm (HOLE-TO-HOLE CENTER DISTANCE)</text>

        <line x1="0" y1="-15" x2="900" y2="-15" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="450" y="-25" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">760.0 mm (OVERALL CUT LENGTH)</text>

        <line x1="-20" y1="0" x2="-20" y2="100" stroke="#4ade80" stroke-width="1.5"/>
        <text x="-30" y="55" fill="#4ade80" font-size="13" font-family="sans-serif" text-anchor="end">60.0 mm (HEIGHT)</text>
    </g>

    <g transform="translate(240, 520)">
        <text x="100" y="-20" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">TUBE CROSS-SECTION (60x40x6 mm)</text>
        <rect x="50" y="10" width="100" height="140" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        <rect x="65" y="25" width="70" height="110" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
        <text x="100" y="175" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">6.0 mm WALL THICKNESS</text>
    </g>

    <g transform="translate(800, 740)">
        <rect width="360" height="120" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="80" x2="360" y2="80" stroke="#38bdf8" stroke-width="1"/>
        <text x="15" y="28" fill="#f8fafc" font-size="15" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 07</text>
        <text x="15" y="65" fill="#94a3b8" font-size="13" font-family="sans-serif">DWG NO: SA-001 / SA-002 | REV: 3.0</text>
        <text x="15" y="105" fill="#94a3b8" font-size="13" font-family="sans-serif">60x40x6 mm RHS TUBE | BRONZE BUSHED</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# SVG PART 08: COMPLETE ASSEMBLY & DUAL-HEIGHT SECTIONS
# -------------------------------------------------------------
svg_p8 = """<svg width="1200" height="900" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="900" fill="#0f172a"/>
    <rect x="20" y="20" width="1160" height="860" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>

    <text x="50" y="60" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold">DETAILED PART DRAWING: PART 08 - COMPLETE ASSEMBLY &amp; DUAL-HEIGHT CROSS SECTIONS</text>
    <text x="50" y="85" fill="#94a3b8" font-size="14" font-family="sans-serif">COMPLETE AMR CHASSIS ASSEMBLY | 1200 x 1000 x 170 mm | STEPPED GUIDE LIFT</text>
    <line x1="50" y1="100" x2="1110" y2="100" stroke="#334155" stroke-width="2"/>

    <g transform="translate(140, 160)">
        <text x="450" y="-20" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">CHASSIS SIDE ELEVATION CUTAWAY (1200 mm LENGTH)</text>
        <rect x="0" y="0" width="900" height="150" rx="10" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        
        <circle cx="100" cy="150" r="45" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
        <circle cx="800" cy="150" r="45" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>

        <path d="M 50,130 L 350,130 L 400,80 L 600,80 L 650,40 L 850,40" fill="none" stroke="#4ade80" stroke-width="4"/>

        <rect x="620" y="10" width="120" height="30" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>
        <line x1="740" y1="15" x2="950" y2="15" stroke="#38bdf8" stroke-width="6"/>

        <text x="450" y="180" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">1200.0 mm (OVERALL CHASSIS LENGTH)</text>
    </g>

    <g transform="translate(140, 450)">
        <g transform="translate(30, 0)">
            <text x="160" y="-15" fill="#ef4444" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">POS A: LOW (90 mm Fork Entry)</text>
            <rect x="0" y="0" width="320" height="160" fill="#0f172a" stroke="#f8fafc" stroke-width="2"/>
            <rect x="60" y="100" width="200" height="20" fill="#38bdf8"/>
            <rect x="80" y="120" width="30" height="40" fill="#94a3b8"/>
            <rect x="210" y="120" width="30" height="40" fill="#94a3b8"/>
            <text x="160" y="80" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle">FORK ENTRY HEIGHT = 90 mm</text>
        </g>

        <g transform="translate(490, 0)">
            <text x="160" y="-15" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">POS C: HIGH (170 mm Lifted Height)</text>
            <rect x="0" y="0" width="320" height="160" fill="#0f172a" stroke="#f8fafc" stroke-width="2"/>
            <rect x="60" y="30" width="200" height="20" fill="#38bdf8"/>
            <rect x="80" y="50" width="30" height="110" fill="#94a3b8"/>
            <rect x="210" y="50" width="30" height="110" fill="#94a3b8"/>
            <text x="160" y="20" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle">PALLET WHEEL CLEARANCE = 30 mm</text>
        </g>
    </g>

    <g transform="translate(800, 740)">
        <rect width="360" height="120" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="80" x2="360" y2="80" stroke="#38bdf8" stroke-width="1"/>
        <text x="15" y="28" fill="#f8fafc" font-size="15" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 08</text>
        <text x="15" y="65" fill="#94a3b8" font-size="13" font-family="sans-serif">DWG NO: AMR-000 | REV: 3.0</text>
        <text x="15" y="105" fill="#94a3b8" font-size="13" font-family="sans-serif">COMPLETE ASSEMBLY &amp; DUAL HEIGHTS</text>
    </g>
</svg>"""

all_parts = [
    ("part_01_floor_base_plate", svg_p1),
    ("part_02_outer_sidewalls", svg_p2),
    ("part_03_front_rear_walls", svg_p3),
    ("part_04_stepped_guide_rail", svg_p4),
    ("part_05_fork_carriage_tines", svg_p5),
    ("part_07_scissor_linkage_arms", svg_p7),
    ("part_08_complete_assembly_sections", svg_p8)
]

for name, svg_data in all_parts:
    svg_file = f"/tmp/{name}.svg"
    png_file = f"/tmp/{name}.png"
    
    with open(svg_file, "w") as f:
        f.write(svg_data)
        
    cmd = f"rsvg-convert -w 1200 -h 900 {svg_file} -o {png_file}"
    subprocess.run(cmd, shell=True)
    
    out_png = os.path.join(scratch_dir, f"{name}.png")
    brain_png = os.path.join(brain_dir, f"{name}.png")
    doc_png = os.path.join(doc_dir, f"{name}.png")
    pict_png = os.path.join(pict_dir, f"{name}.png")
    
    subprocess.run(f"cp {png_file} {out_png}", shell=True)
    subprocess.run(f"cp {png_file} {brain_png}", shell=True)
    subprocess.run(f"cp {png_file} {doc_png}", shell=True)
    subprocess.run(f"cp {png_file} {pict_png}", shell=True)
    print(f"Generated RSVG PNG image: {name}.png ({os.path.getsize(png_file)} bytes)")

