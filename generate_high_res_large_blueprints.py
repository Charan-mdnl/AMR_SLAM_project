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
# SVG PART 01: FLOOR BASE PLATE (SM-001) - 1600x1200
# -------------------------------------------------------------
svg_p1 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <!-- HEADER -->
    <text x="60" y="70" fill="#38bdf8" font-size="30" font-family="sans-serif" font-weight="bold">PART 01 DRAWING: CHASSIS FLOOR BASE PLATE (SM-001)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: CRCA STEEL (6.0 mm THICK) | ALL DIMENSIONS IN MILLIMETERS (mm)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <!-- TOP PLAN VIEW -->
    <g transform="translate(250, 200)">
        <text x="500" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">TOP PLAN VIEW (1200.0 mm x 1000.0 mm)</text>
        
        <!-- Main Plate Contour -->
        <polygon points="50,0 950,0 1000,50 1000,750 950,800 50,800 0,750 0,50" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>
        <text x="940" y="35" fill="#f59e0b" font-size="16" font-family="sans-serif" font-weight="bold">40x45° CHAMFER (4x)</text>
        
        <!-- Center Cutout -->
        <rect x="350" y="260" width="300" height="280" fill="#1e293b" stroke="#94a3b8" stroke-width="3" stroke-dasharray="8,6"/>
        <text x="500" y="405" fill="#94a3b8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">CENTER CUTOUT (300 x 200 mm)</text>

        <!-- Drive Wheel Cutouts -->
        <rect x="70" y="300" width="180" height="200" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
        <text x="160" y="405" fill="#ef4444" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">LEFT DRIVE WHEEL<br/>CUTOUT 220x70 mm</text>

        <rect x="750" y="300" width="180" height="200" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
        <text x="840" y="405" fill="#ef4444" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">RIGHT DRIVE WHEEL<br/>CUTOUT 220x70 mm</text>

        <!-- Caster Mount Holes (4 sets) -->
        <circle cx="60" cy="60" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="940" cy="60" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="60" cy="740" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="940" cy="740" r="14" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <text x="60" y="35" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">4x Ø9 THRU (80x80 PITCH)</text>

        <!-- Stepped Rail Lines -->
        <line x1="180" y1="40" x2="180" y2="760" stroke="#4ade80" stroke-width="3" stroke-dasharray="10,5"/>
        <line x1="820" y1="40" x2="820" y2="760" stroke="#4ade80" stroke-width="3" stroke-dasharray="10,5"/>
        <text x="180" y="20" fill="#4ade80" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">STEPPED RAIL MOUNT (LEFT)</text>
        <text x="820" y="20" fill="#4ade80" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">STEPPED RAIL MOUNT (RIGHT)</text>

        <!-- Dimensions -->
        <!-- Length 1200mm -->
        <line x1="0" y1="-50" x2="1000" y2="-50" stroke="#f8fafc" stroke-width="2"/>
        <line x1="0" y1="-65" x2="0" y2="-35" stroke="#f8fafc" stroke-width="2"/>
        <line x1="1000" y1="-65" x2="1000" y2="-35" stroke="#f8fafc" stroke-width="2"/>
        <text x="500" y="-60" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">1200.0 mm (OVERALL LENGTH)</text>

        <!-- Width 1000mm -->
        <line x1="-50" y1="0" x2="-50" y2="800" stroke="#f8fafc" stroke-width="2"/>
        <line x1="-65" y1="0" x2="-35" y2="0" stroke="#f8fafc" stroke-width="2"/>
        <line x1="-65" y1="800" x2="-35" y2="800" stroke="#f8fafc" stroke-width="2"/>
        <text x="-60" y="400" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle" transform="rotate(-90 -60 400)">1000.0 mm (OVERALL WIDTH)</text>

        <!-- Rail Spacing 800mm -->
        <line x1="180" y1="830" x2="820" y2="830" stroke="#4ade80" stroke-width="2"/>
        <text x="500" y="855" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">800.0 mm (RAIL SPACING CENTER-TO-CENTER)</text>
    </g>

    <!-- TITLE BLOCK -->
    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 01</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SM-001 | REV: 4.0 | TOL: ±0.5 mm</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">SHEET METAL: 6.0 mm CRCA STEEL</text>
    </g>
</svg>"""

# -------------------------------------------------------------
# SVG PART 04: STEPPED LINEAR GUIDE RAIL (SG-001 / SG-002)
# -------------------------------------------------------------
svg_p4 = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <text x="60" y="70" fill="#38bdf8" font-size="30" font-family="sans-serif" font-weight="bold">PART 04 DRAWING: STEPPED LINEAR GUIDE RAIL (SG-001 / SG-002)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">MATERIAL: MACHINED C45 STEEL | ALL DIMENSIONS IN MILLIMETERS (mm) | QTY: 2 (PAIR)</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <!-- ELEVATION PROFILE -->
    <g transform="translate(180, 240)">
        <text x="600" y="-50" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">ELEVATION PROFILE (STEPPED STAIRCASE GEOMETRY)</text>

        <!-- Stepped Profile Polygon -->
        <polygon points="0,300 450,300 530,220 830,220 910,140 1200,140 1200,350 0,350" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>
        <path d="M 0,300 L 450,300 L 530,220 L 830,220 L 910,140 L 1200,140" fill="none" stroke="#4ade80" stroke-width="6"/>

        <!-- Carriage Block Position A (Low) -->
        <rect x="150" y="240" width="120" height="60" rx="6" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,6"/>
        <text x="210" y="225" fill="#ef4444" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">CARRIAGE (POS A - 90mm Entry)</text>

        <!-- Carriage Block Position C (High) -->
        <rect x="1000" y="80" width="120" height="60" rx="6" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <text x="1060" y="60" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">CARRIAGE (POS C - 170mm Lifted)</text>

        <!-- Mounting Holes -->
        <circle cx="80" cy="325" r="6" fill="#f8fafc"/>
        <circle cx="280" cy="325" r="6" fill="#f8fafc"/>
        <circle cx="480" cy="325" r="6" fill="#f8fafc"/>
        <circle cx="680" cy="325" r="6" fill="#f8fafc"/>
        <circle cx="880" cy="325" r="6" fill="#f8fafc"/>
        <circle cx="1100" cy="325" r="6" fill="#f8fafc"/>
        <text x="600" y="385" fill="#94a3b8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">11x M8 COUNTERSUNK MOUNTING HOLES (100.0 mm PITCH)</text>

        <!-- Length 1100mm -->
        <line x1="0" y1="420" x2="1200" y2="420" stroke="#f8fafc" stroke-width="2"/>
        <text x="600" y="445" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">1100.0 mm (TOTAL RAIL LENGTH)</text>

        <!-- Step Heights -->
        <line x1="-40" y1="350" x2="-40" y2="300" stroke="#4ade80" stroke-width="2"/>
        <text x="-55" y="330" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="end">20.0 mm (STEP 1)</text>

        <line x1="-40" y1="350" x2="-40" y2="220" stroke="#4ade80" stroke-width="2"/>
        <text x="-55" y="270" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="end">60.0 mm (STEP 2)</text>

        <line x1="-40" y1="350" x2="-40" y2="140" stroke="#4ade80" stroke-width="2"/>
        <text x="-55" y="190" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="end">100.0 mm (STEP 3)</text>

        <text x="490" y="270" fill="#f59e0b" font-size="16" font-family="sans-serif" font-weight="bold">30° RAMP</text>
        <text x="870" y="190" fill="#f59e0b" font-size="16" font-family="sans-serif" font-weight="bold">30° RAMP</text>
    </g>

    <!-- CROSS-SECTION A-A -->
    <g transform="translate(250, 750)">
        <text x="150" y="-25" fill="#38bdf8" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">CROSS-SECTION A-A (RAIL + CARRIAGE BLOCK)</text>
        <rect x="90" y="40" width="120" height="160" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
        <path d="M 120,40 L 150,10 L 180,40" fill="none" stroke="#4ade80" stroke-width="4"/>
        <rect x="105" y="-30" width="90" height="70" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="125" cy="5" r="7" fill="#f59e0b"/>
        <circle cx="175" cy="5" r="7" fill="#f59e0b"/>
        <text x="150" y="235" fill="#94a3b8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">RAIL WIDTH: 25.0 mm | CARRIAGE BLOCK: 80x50x30 mm</text>
    </g>

    <!-- TITLE BLOCK -->
    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN AMR - PART 04</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: SG-001 / SG-002 | REV: 4.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">MACHINED C45 STEEL (STEPPED PROFILE)</text>
    </g>
</svg>"""

all_svgs = [
    ("part_01_floor_base_plate", svg_p1),
    ("part_04_stepped_guide_rail", svg_p4)
]

for name, svg_data in all_svgs:
    svg_file = f"/tmp/{name}.svg"
    png_file = f"/tmp/{name}.png"
    
    with open(svg_file, "w") as f:
        f.write(svg_data)
        
    cmd = f"rsvg-convert -w 1600 -h 1200 {svg_file} -o {png_file}"
    subprocess.run(cmd, shell=True)
    
    out_png = os.path.join(scratch_dir, f"{name}.png")
    brain_png = os.path.join(brain_dir, f"{name}.png")
    doc_png = os.path.join(doc_dir, f"{name}.png")
    pict_png = os.path.join(pict_dir, f"{name}.png")
    
    subprocess.run(f"cp {png_file} {out_png}", shell=True)
    subprocess.run(f"cp {png_file} {brain_png}", shell=True)
    subprocess.run(f"cp {png_file} {doc_png}", shell=True)
    subprocess.run(f"cp {png_file} {pict_png}", shell=True)
    print(f"Generated 1600x1200 PNG image: {name}.png ({os.path.getsize(png_file)} bytes)")

