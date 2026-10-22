import os
import subprocess
from PIL import Image

scratch_dir = "/home/charan/.gemini/antigravity-ide/scratch/tusk-amr-analysis"
brain_dir = "/home/charan/.gemini/antigravity-ide/brain/4ac556db-d1f1-449a-b470-f85aafe800fc"
doc_dir = "/home/charan/Documents/tusk-amr-files"
pict_dir = "/home/charan/Pictures/blueprints"

os.makedirs(scratch_dir, exist_ok=True)
os.makedirs(doc_dir, exist_ok=True)
os.makedirs(pict_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. PART 01: FLOOR BASE PLATE (SM-001)
# -------------------------------------------------------------
svg_p1 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="32" font-family="sans-serif" font-weight="bold">PART 01 DRAWING: CHASSIS FLOOR BASE PLATE (SM-001)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: CRCA STEEL (6.0 mm THICK) | ALL DIMENSIONS IN MILLIMETERS (mm)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(250, 200)">
        <text x="500" y="-30" fill="#38bdf8" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">TOP PLAN VIEW (1200.0 mm x 1000.0 mm)</text>
        
        <polygon points="50,0 950,0 1000,50 1000,750 950,800 50,800 0,750 0,50" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>
        <text x="940" y="35" fill="#f59e0b" font-size="16" font-family="sans-serif" font-weight="bold">40x45° CHAMFER (4x)</text>
        
        <rect x="350" y="260" width="300" height="280" fill="#1e293b" stroke="#94a3b8" stroke-width="3" stroke-dasharray="8,6"/>
        <text x="500" y="405" fill="#94a3b8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">CENTER CUTOUT (300 x 200 mm)</text>

        <rect x="70" y="300" width="180" height="200" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
        <text x="160" y="405" fill="#ef4444" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">LEFT DRIVE WHEEL<br/>CUTOUT 220x70 mm</text>

        <rect x="750" y="300" width="180" height="200" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
        <text x="840" y="405" fill="#ef4444" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">RIGHT DRIVE WHEEL<br/>CUTOUT 220x70 mm</text>

        <circle cx="60" cy="60" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="940" cy="60" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="60" cy="740" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="940" cy="740" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <text x="60" y="35" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">4x Ø9 THRU (80x80 PITCH)</text>

        <line x1="180" y1="40" x2="180" y2="760" stroke="#4ade80" stroke-width="3" stroke-dasharray="10,5"/>
        <line x1="820" y1="40" x2="820" y2="760" stroke="#4ade80" stroke-width="3" stroke-dasharray="10,5"/>
        <text x="180" y="20" fill="#4ade80" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">RAIL MOUNT LINE (LEFT)</text>
        <text x="820" y="20" fill="#4ade80" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">RAIL MOUNT LINE (RIGHT)</text>

        <line x1="0" y1="-50" x2="1000" y2="-50" stroke="#f8fafc" stroke-width="2"/>
        <text x="500" y="-60" fill="#f8fafc" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">1200.0 mm (OVERALL LENGTH)</text>

        <line x1="-50" y1="0" x2="-50" y2="800" stroke="#f8fafc" stroke-width="2"/>
        <text x="-60" y="400" fill="#f8fafc" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle" transform="rotate(-90 -60 400)">1000.0 mm (OVERALL WIDTH)</text>

        <line x1="180" y1="830" x2="820" y2="830" stroke="#4ade80" stroke-width="2"/>
        <text x="500" y="855" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">800.0 mm (RAIL SPACING CENTER-TO-CENTER)</text>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 01</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SM-001 | REV: 5.0 | TOL: ±0.5 mm</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">SHEET METAL: 6.0 mm CRCA STEEL</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# 2. PART 02: OUTER SIDEWALLS (SM-002 / SM-003)
# -------------------------------------------------------------
svg_p2 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="32" font-family="sans-serif" font-weight="bold">PART 02 DRAWING: OUTER SIDEWALLS (SM-002 / SM-003)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: CRCA STEEL (3.0 mm THICK) | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (LEFT &amp; RIGHT)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(180, 200)">
        <text x="600" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">FLAT PATTERN - UNFOLDED SHEET (1200 mm x 230 mm)</text>
        <rect x="0" y="0" width="1200" height="230" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>

        <line x1="0" y1="30" x2="1200" y2="30" stroke="#f59e0b" stroke-width="2" stroke-dasharray="8,6"/>
        <line x1="0" y1="200" x2="1200" y2="200" stroke="#f59e0b" stroke-width="2" stroke-dasharray="8,6"/>
        <text x="600" y="22" fill="#f59e0b" font-size="14" font-family="sans-serif" text-anchor="middle">BEND LINE 90° INWARD (R3.0 mm)</text>
        <text x="600" y="220" fill="#f59e0b" font-size="14" font-family="sans-serif" text-anchor="middle">BEND LINE 90° INWARD (R3.0 mm)</text>

        <rect x="480" y="30" width="240" height="170" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
        <text x="600" y="120" fill="#ef4444" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">DRIVE WHEEL SLOT<br/>240.0 x 100.0 mm</text>

        <line x1="0" y1="-15" x2="1200" y2="-15" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="-25" fill="#f8fafc" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">1200.0 mm (FLAT SHEET LENGTH)</text>

        <line x1="-30" y1="0" x2="-30" y2="230" stroke="#4ade80" stroke-width="2"/>
        <text x="-40" y="115" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="end">230.0 mm (FLAT HEIGHT)</text>
    </g>

    <g transform="translate(180, 580)">
        <text x="600" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">FORMED SIDE ELEVATION (170 mm FORMED HEIGHT)</text>
        <rect x="0" y="0" width="1200" height="170" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>
        <rect x="480" y="0" width="240" height="170" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
        <text x="600" y="90" fill="#ef4444" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">DRIVE WHEEL CLEARANCE SLOT</text>

        <line x1="-30" y1="0" x2="-30" y2="170" stroke="#4ade80" stroke-width="2"/>
        <text x="-40" y="85" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="end">170.0 mm (FORMED H)</text>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 02</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SM-002 / SM-003 | REV: 5.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">CRCA STEEL (3.0 mm) | BEND R3.0 mm</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# 3. PART 03: FRONT & REAR END WALLS (SM-004 / SM-005)
# -------------------------------------------------------------
svg_p3 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="32" font-family="sans-serif" font-weight="bold">PART 03 DRAWING: FRONT &amp; REAR END WALLS (SM-004 / SM-005)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: CRCA STEEL (3.0 mm THICK) | ALL DIMENSIONS IN MILLIMETERS (mm)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(180, 200)">
        <text x="600" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT END WALL (SM-004) - FORMED VIEW WITH DUAL FORK SLOTS</text>
        <rect x="0" y="0" width="1200" height="170" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>

        <rect x="240" y="60" width="130" height="110" fill="#1e293b" stroke="#4ade80" stroke-width="3"/>
        <text x="305" y="120" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">FORK SLOT 1<br/>110x50 mm</text>

        <rect x="830" y="60" width="130" height="110" fill="#1e293b" stroke="#4ade80" stroke-width="3"/>
        <text x="895" y="120" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">FORK SLOT 2<br/>110x50 mm</text>

        <line x1="305" y1="200" x2="895" y2="200" stroke="#4ade80" stroke-width="2"/>
        <text x="600" y="225" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">560.0 mm (FORK SLOT CENTER SPACING)</text>

        <line x1="0" y1="-15" x2="1200" y2="-15" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="-25" fill="#f8fafc" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">994.0 mm (FORMED END WALL WIDTH)</text>
    </g>

    <g transform="translate(180, 580)">
        <text x="600" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">REAR END WALL (SM-005) - CLOSED PROFILE WITH LiDAR CUTOUTS</text>
        <rect x="0" y="0" width="1200" height="170" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>
        <circle cx="80" cy="85" r="25" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
        <circle cx="1120" cy="85" r="25" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
        <text x="600" y="95" fill="#94a3b8" font-size="16" font-family="sans-serif" text-anchor="middle">SOLID REAR WALL WITH DUAL LiDAR SAFETY SENSOR CUTOUTS (Ø30 mm)</text>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 03</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SM-004 / SM-005 | REV: 5.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">CRCA STEEL (3.0 mm) | DUAL SLOTS</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# 4. PART 04: TWIN SCISSOR TOP PLATFORMS (FP-001 & FP-002)
# -------------------------------------------------------------
svg_p4 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="32" font-family="sans-serif" font-weight="bold">PART 04 DRAWING: TWIN SCISSOR LIFT TOP PLATFORMS (FP-001 / FP-002)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: CRCA STEEL (6.0 mm THICK) | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (PAIR)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(180, 200)">
        <text x="600" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">TOP PLAN VIEW - FORK LIFT PLATFORM PLATE (1100.0 mm x 180.0 mm)</text>
        <rect x="0" y="0" width="1200" height="200" rx="10" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>

        <!-- Upper Fixed & Sliding Pivot Brackets -->
        <rect x="100" y="20" width="80" height="160" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="140" y="105" fill="#38bdf8" font-size="13" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 140 105)">FIXED PIVOT</text>

        <rect x="1020" y="20" width="80" height="160" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
        <text x="1060" y="105" fill="#4ade80" font-size="13" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 1060 105)">SLIDING TRACK</text>

        <!-- Dimensions -->
        <line x1="0" y1="-15" x2="1200" y2="-15" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="-25" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">1100.0 mm (TOTAL PLATFORM LENGTH)</text>

        <line x1="-30" y1="0" x2="-30" y2="200" stroke="#4ade80" stroke-width="2"/>
        <text x="-40" y="100" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="end">180.0 mm (PLATFORM W)</text>
    </g>

    <g transform="translate(180, 560)">
        <text x="600" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">TWIN PARALLEL FORK PLATFORM SPACING (560 mm CENTER-TO-CENTER)</text>
        
        <rect x="100" y="0" width="1000" height="160" fill="#0f172a" stroke="#94a3b8" stroke-width="2" stroke-dasharray="8,6"/>
        <rect x="250" y="20" width="180" height="120" fill="#38bdf8" opacity="0.4"/>
        <rect x="770" y="20" width="180" height="120" fill="#38bdf8" opacity="0.4"/>
        
        <text x="340" y="85" fill="#f8fafc" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">PLATFORM 1 (180mm)</text>
        <text x="860" y="85" fill="#f8fafc" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">PLATFORM 2 (180mm)</text>

        <line x1="340" y1="190" x2="860" y2="190" stroke="#4ade80" stroke-width="2"/>
        <text x="600" y="215" fill="#4ade80" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">560.0 mm (EUR PALLET FORK SPACING C-C)</text>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 04</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: FP-001 / FP-002 | REV: 5.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">CRCA STEEL (6.0 mm) | TWIN PLATFORMS</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# 5. PART 05: SCISSOR LINKAGE ARMS (SA-001 & SA-002)
# -------------------------------------------------------------
svg_p5 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="32" font-family="sans-serif" font-weight="bold">PART 05 DRAWING: SCISSOR LINKAGE ARMS (SA-001 / SA-002)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: 40x20x4.0mm RHS TUBE (Q235 STEEL) | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 8 (4 PAIRS)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(180, 240)">
        <text x="600" y="-40" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">FRONT ELEVATION - SCISSOR ARM (550 mm OVERALL CUT LENGTH)</text>
        
        <rect x="0" y="0" width="1200" height="140" rx="70" ry="70" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>

        <circle cx="70" cy="70" r="30" fill="#1e293b" stroke="#4ade80" stroke-width="4"/>
        <circle cx="70" cy="70" r="18" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <text x="70" y="130" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Ø25 H7 / Ø20 ID (End 1)</text>

        <circle cx="600" cy="70" r="30" fill="#1e293b" stroke="#4ade80" stroke-width="4"/>
        <circle cx="600" cy="70" r="18" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <text x="600" y="130" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Ø25 H7 / Ø20 ID (Center Pivot)</text>

        <circle cx="1130" cy="70" r="30" fill="#1e293b" stroke="#4ade80" stroke-width="4"/>
        <circle cx="1130" cy="70" r="18" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <text x="1130" y="130" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Ø25 H7 / Ø20 ID (End 2)</text>

        <line x1="70" y1="180" x2="1130" y2="180" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="205" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">510.0 mm (HOLE-TO-HOLE CENTER DISTANCE)</text>

        <line x1="0" y1="-20" x2="1200" y2="-20" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="-30" fill="#f8fafc" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">550.0 mm (OVERALL CUT LENGTH)</text>

        <line x1="-30" y1="0" x2="-30" y2="140" stroke="#4ade80" stroke-width="2"/>
        <text x="-40" y="75" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="end">40.0 mm (HEIGHT)</text>
    </g>

    <g transform="translate(300, 680)">
        <text x="150" y="-20" fill="#38bdf8" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">TUBE CROSS-SECTION (40x20x4.0 mm)</text>
        <rect x="70" y="10" width="160" height="120" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>
        <rect x="90" y="30" width="120" height="80" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
        <text x="150" y="160" fill="#94a3b8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">4.0 mm WALL THICKNESS</text>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 05</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SA-001 / SA-002 | REV: 5.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">40x20x4.0 mm RHS TUBE | BRONZE BUSHED</text>
    </g>
</svg>"""

# Save and render all SVGs to JPG and PNG
all_parts = [
    ("part_01_floor_base_plate", svg_p1),
    ("part_02_outer_sidewalls", svg_p2),
    ("part_03_front_rear_end_walls", svg_p3),
    ("part_04_twin_scissor_top_platforms", svg_p4),
    ("part_05_scissor_x_linkage_arms", svg_p5)
]

for name, svg_data in all_parts:
    svg_file = f"/tmp/{name}.svg"
    png_file = f"/tmp/{name}.png"
    jpg_file = f"/tmp/{name}.jpg"
    
    with open(svg_file, "w") as f:
        f.write(svg_data)
        
    cmd = f"rsvg-convert -w 1600 -h 1200 {svg_file} -o {png_file}"
    subprocess.run(cmd, shell=True)
    
    # Convert PNG to high quality JPG
    im = Image.open(png_file).convert("RGB")
    im.save(jpg_file, "JPEG", quality=95)
    
    # Copy to all target directories
    for d in [scratch_dir, brain_dir, doc_dir, pict_dir]:
        subprocess.run(f"cp {png_file} {os.path.join(d, f'{name}.png')}", shell=True)
        subprocess.run(f"cp {jpg_file} {os.path.join(d, f'{name}.jpg')}", shell=True)
        
    print(f"Generated JPG & PNG blueprint: {name} ({os.path.getsize(jpg_file)} bytes JPG)")

