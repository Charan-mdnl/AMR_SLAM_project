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
# DWG 01: CHASSIS BASE FRAME FLOOR PLATE (SM-001)
# -------------------------------------------------------------
svg_dwg1 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="30" font-family="sans-serif" font-weight="bold">DWG 01: CHASSIS BASE FRAME FLOOR PLATE (SM-001)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">ENVELOPE: 1200.0 mm (L) x 1000.0 mm (W) x 6.0 mm (T) | MATERIAL: CRCA STEEL</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(200, 200)">
        <text x="600" y="-35" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">TOP PLAN VIEW (300mm Side Pod - 200mm Channel - 300mm Bridge - 200mm Channel Layout)</text>

        <!-- Outer Boundary -->
        <polygon points="40,0 1160,0 1200,40 1200,760 1160,800 40,800 0,760 0,40" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>

        <!-- Left Pod (300mm) -->
        <rect x="0" y="0" width="360" height="800" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="180" y="400" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle" transform="rotate(-90 180 400)">LEFT SIDE POD (300.0 mm W)</text>

        <!-- Channel 1 Cutout (200mm W x 1000mm L) -->
        <rect x="360" y="0" width="240" height="667" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
        <text x="480" y="333" fill="#ef4444" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">PALLET SLOT 1<br/>200.0 x 1000.0 mm</text>

        <!-- Center Bridge (300mm) -->
        <rect x="600" y="0" width="360" height="800" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="780" y="400" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle" transform="rotate(-90 780 400)">CENTER BRIDGE POD (300.0 mm W)</text>

        <!-- Channel 2 Cutout (200mm W x 1000mm L) -->
        <rect x="960" y="0" width="240" height="667" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
        <text x="1080" y="333" fill="#ef4444" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">PALLET SLOT 2<br/>200.0 x 1000.0 mm</text>

        <!-- 2 Center Drive Hub Motor Access Cutouts -->
        <rect x="100" y="350" width="160" height="100" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/>
        <text x="180" y="405" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">LEFT HUB MOTOR<br/>220x70 mm CUTOUT</text>

        <rect x="700" y="350" width="160" height="100" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/>
        <text x="780" y="405" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">RIGHT HUB MOTOR<br/>220x70 mm CUTOUT</text>

        <!-- 4 Corner Swivel Casters -->
        <circle cx="60" cy="60" r="14" fill="none" stroke="#4ade80" stroke-width="3"/>
        <circle cx="1140" cy="60" r="14" fill="none" stroke="#4ade80" stroke-width="3"/>
        <circle cx="60" cy="740" r="14" fill="none" stroke="#4ade80" stroke-width="3"/>
        <circle cx="1140" cy="740" r="14" fill="none" stroke="#4ade80" stroke-width="3"/>
        <text x="60" y="35" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">CASTER (FL)</text>
        <text x="1140" y="35" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">CASTER (FR)</text>
        <text x="60" y="780" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">CASTER (RL)</text>
        <text x="1140" y="780" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">CASTER (RR)</text>

        <!-- Width Callouts -->
        <line x1="0" y1="830" x2="360" y2="830" stroke="#38bdf8" stroke-width="2"/>
        <text x="180" y="855" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">300 mm</text>

        <line x1="360" y1="830" x2="600" y2="830" stroke="#ef4444" stroke-width="2"/>
        <text x="480" y="855" fill="#ef4444" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">200 mm</text>

        <line x1="600" y1="830" x2="960" y2="830" stroke="#38bdf8" stroke-width="2"/>
        <text x="780" y="855" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">300 mm</text>

        <line x1="960" y1="830" x2="1200" y2="830" stroke="#ef4444" stroke-width="2"/>
        <text x="1080" y="855" fill="#ef4444" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">200 mm</text>

        <line x1="0" y1="-15" x2="1200" y2="-15" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="-25" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">1000.0 mm (TOTAL OVERALL WIDTH)</text>

        <line x1="-30" y1="0" x2="-30" y2="800" stroke="#f8fafc" stroke-width="2"/>
        <text x="-45" y="400" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle" transform="rotate(-90 -45 400)">1200.0 mm (TOTAL OVERALL LENGTH)</text>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">USER CUSTOM AMR - DWG 01 FLOOR PLATE</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SM-001 | REV: 7.0 | TOL: ±0.5 mm</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">300-200-300-200 mm EXACT CHASSIS LAYOUT</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# DWG 04: STEPPED LINEAR GUIDE RAIL & UPPER ROLLERS (SG-001)
# -------------------------------------------------------------
svg_dwg4 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="30" font-family="sans-serif" font-weight="bold">DWG 04: STEPPED LINEAR GUIDE RAIL ("L GUIDE STEP") &amp; UPPER DRIVE ROLLERS</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: MACHINED C45 STEEL | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (PAIR)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(180, 240)">
        <text x="600" y="-40" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">ELEVATION PROFILE (STEPPED STAIRCASE GEOMETRY FOR UPPER DRIVE ROLLERS)</text>

        <polygon points="0,300 400,300 480,200 800,200 880,100 1200,100 1200,350 0,350" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>
        <path d="M 0,300 L 400,300 L 480,200 L 800,200 L 880,100 L 1200,100" fill="none" stroke="#4ade80" stroke-width="6"/>

        <!-- Upper Roller A (Closed State) -->
        <circle cx="180" cy="270" r="30" fill="none" stroke="#ef4444" stroke-width="4"/>
        <text x="180" y="225" fill="#ef4444" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">UPPER ROLLER (STEP 1 - CLOSED 170mm)</text>

        <!-- Upper Roller B (Extended State) -->
        <circle cx="1040" cy="70" r="30" fill="none" stroke="#38bdf8" stroke-width="4"/>
        <text x="1040" y="25" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">UPPER ROLLER (STEP 3 - EXTENDED 310mm)</text>

        <line x1="0" y1="400" x2="1200" y2="400" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="425" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">1000.0 mm (SLOT GUIDE RAIL LENGTH)</text>

        <line x1="-40" y1="350" x2="-40" y2="300" stroke="#4ade80" stroke-width="2"/>
        <text x="-55" y="330" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="end">20.0 mm (STEP 1)</text>

        <line x1="-40" y1="350" x2="-40" y2="200" stroke="#4ade80" stroke-width="2"/>
        <text x="-55" y="260" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="end">80.0 mm (STEP 2)</text>

        <line x1="-40" y1="350" x2="-40" y2="100" stroke="#4ade80" stroke-width="2"/>
        <text x="-55" y="150" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="end">140.0 mm (STEP 3)</text>

        <text x="440" y="240" fill="#f59e0b" font-size="16" font-family="sans-serif" font-weight="bold">30° RAMP</text>
        <text x="840" y="140" fill="#f59e0b" font-size="16" font-family="sans-serif" font-weight="bold">30° RAMP</text>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">USER CUSTOM AMR - STEPPED RAIL</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SG-001 / SG-002 | REV: 7.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">STEPPED GUIDE FOR PALLET UPPER ROLLERS</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# DWG 07: COMPLETE ASSEMBLY & WHEEL SCHEMATIC (MATCHING PAGE 12)
# -------------------------------------------------------------
svg_dwg7 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="30" font-family="sans-serif" font-weight="bold">DWG 07: COMPLETE ASSEMBLY &amp; 6-WHEEL DRIVE SCHEMATIC (AMR-000)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">6-WHEEL DIFFERENTIAL LAYOUT: 4x CORNER CASTERS + 2x CENTER SIDE HUB MOTORS</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <g transform="translate(250, 180)">
        <text x="500" y="-20" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">WHEEL SCHEMATIC (EXACT MATCH TO NOTEBOOK PAGE 12 BOTTOM)</text>

        <rect x="0" y="0" width="1000" height="600" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>

        <!-- 4 Casters -->
        <rect x="20" y="20" width="80" height="100" fill="#4ade80"/>
        <text x="60" y="75" fill="#0f172a" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

        <rect x="900" y="20" width="80" height="100" fill="#4ade80"/>
        <text x="940" y="75" fill="#0f172a" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

        <rect x="20" y="480" width="80" height="100" fill="#4ade80"/>
        <text x="60" y="535" fill="#0f172a" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

        <rect x="900" y="480" width="80" height="100" fill="#4ade80"/>
        <text x="940" y="535" fill="#0f172a" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">CW</text>

        <!-- 2 Center Hub Motors -->
        <rect x="20" y="250" width="100" height="100" fill="#ef4444"/>
        <text x="70" y="305" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hub M</text>

        <rect x="880" y="250" width="100" height="100" fill="#ef4444"/>
        <text x="930" y="305" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hub M</text>

        <!-- 2 Pallet Channels (P) -->
        <rect x="220" y="50" width="200" height="500" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="320" y="300" fill="#38bdf8" font-size="32" font-family="sans-serif" font-weight="bold" text-anchor="middle">P</text>

        <rect x="580" y="50" width="200" height="500" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="680" y="300" fill="#38bdf8" font-size="32" font-family="sans-serif" font-weight="bold" text-anchor="middle">P</text>
    </g>

    <g transform="translate(180, 840)">
        <g transform="translate(50, 0)">
            <text x="200" y="-15" fill="#ef4444" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">CLOSED STATE (170 mm H)</text>
            <rect x="0" y="0" width="400" height="140" fill="#0f172a" stroke="#f8fafc" stroke-width="2"/>
            <rect x="80" y="90" width="240" height="20" fill="#38bdf8"/>
            <text x="200" y="60" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">CARRIAGE FLUSH IN SLOT = 170 mm</text>
        </g>

        <g transform="translate(650, 0)">
            <text x="200" y="-15" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">EXTENDED STATE (310 mm H)</text>
            <rect x="0" y="0" width="400" height="140" fill="#0f172a" stroke="#f8fafc" stroke-width="2"/>
            <rect x="80" y="20" width="240" height="20" fill="#38bdf8"/>
            <line x1="100" y1="40" x2="300" y2="120" stroke="#4ade80" stroke-width="4"/>
            <line x1="300" y1="40" x2="100" y2="120" stroke="#4ade80" stroke-width="4"/>
            <text x="200" y="15" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">SCISSOR LIFTED = 310 mm</text>
        </g>
    </g>

    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">USER CUSTOM AMR - ASSEMBLY</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: AMR-000 | REV: 7.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">6-WHEEL DRIVE &amp; DUAL-HEIGHT LIFT</text>
    </g>
</svg>"""

all_blueprints = [
    ("DWG_01_FLOOR_BASE_PLATE", svg_dwg1),
    ("DWG_04_STEPPED_GUIDE_RAIL", svg_dwg4),
    ("DWG_07_COMPLETE_ASSEMBLY_CROSS_SECTIONS", svg_dwg7)
]

for name, svg_data in all_blueprints:
    svg_file = f"/tmp/{name}.svg"
    png_file = f"/tmp/{name}.png"
    jpg_file = f"/tmp/{name}.jpg"
    
    with open(svg_file, "w") as f:
        f.write(svg_data)
        
    cmd = f"rsvg-convert -w 1600 -h 1200 {svg_file} -o {png_file}"
    subprocess.run(cmd, shell=True)
    
    im = Image.open(png_file).convert("RGB")
    im.save(jpg_file, "JPEG", quality=95)
    
    for d in [scratch_dir, brain_dir, doc_dir, pict_dir]:
        subprocess.run(f"cp {png_file} {os.path.join(d, f'{name}.png')}", shell=True)
        subprocess.run(f"cp {jpg_file} {os.path.join(d, f'{name}.jpg')}", shell=True)
        
    print(f"Generated EXACT MATCHING JPG & PNG blueprint: {name} ({os.path.getsize(jpg_file)} bytes JPG)")

