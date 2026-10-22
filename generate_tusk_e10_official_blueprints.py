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
# SVG PART 01: TUSK E10 TITAN DUAL SCISSOR ASSEMBLY (AMR-001)
# -------------------------------------------------------------
svg_assembly = """<svg width="1600" height="1200" xmlns="http://www.w3.org/2000/svg">
    <rect width="1600" height="1200" fill="#0f172a"/>
    <rect x="25" y="25" width="1550" height="1150" fill="#1e293b" stroke="#38bdf8" stroke-width="5"/>

    <!-- HEADER -->
    <text x="60" y="70" fill="#38bdf8" font-size="30" font-family="sans-serif" font-weight="bold">TUSK E10 TITAN — OFFICIAL DUAL SCISSOR LIFT CAD ASSEMBLY (AMR-001)</text>
    <text x="60" y="105" fill="#94a3b8" font-size="18" font-family="sans-serif">ENVELOPE: 1000 mm (W) x 1200 mm (L) x 170 mm (H) | TWIN PARALLEL SCISSOR LIFT PLATFORMS | PAYLOAD: 1000 kg</text>
    <line x1="60" y1="125" x2="1540" y2="125" stroke="#334155" stroke-width="3"/>

    <!-- DUAL HEIGHT FRONT ELEVATION (FLUSH vs LIFTED) -->
    <g transform="translate(100, 180)">
        <!-- LOWERED STOWED POSITION -->
        <g transform="translate(0, 0)">
            <text x="320" y="-20" fill="#ef4444" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">STOWED / FLUSH POSITION (170 mm Height)</text>
            <rect x="0" y="0" width="640" height="220" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
            
            <!-- Outer Chassis Pods -->
            <rect x="0" y="0" width="160" height="220" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <rect x="480" y="0" width="160" height="220" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

            <!-- Twin Flush Fork Plates -->
            <rect x="180" y="20" width="120" height="30" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>
            <rect x="340" y="20" width="120" height="30" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>

            <!-- Folded Scissor Links -->
            <line x1="190" y1="50" x2="290" y2="190" stroke="#4ade80" stroke-width="4"/>
            <line x1="290" y1="50" x2="190" y2="190" stroke="#4ade80" stroke-width="4"/>
            <line x1="350" y1="50" x2="450" y2="190" stroke="#4ade80" stroke-width="4"/>
            <line x1="450" y1="50" x2="350" y2="190" stroke="#4ade80" stroke-width="4"/>

            <text x="320" y="255" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">CHASSIS HEIGHT = 170.0 mm (FLUSH WITH TOP COVER)</text>
        </g>

        <!-- RAISED LIFTED POSITION -->
        <g transform="translate(720, 0)">
            <text x="320" y="-20" fill="#38bdf8" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">RAISED / LIFTED POSITION (310 mm Height)</text>
            <rect x="0" y="90" width="640" height="130" fill="#0f172a" stroke="#f8fafc" stroke-width="3"/>
            
            <!-- Outer Chassis Pods -->
            <rect x="0" y="90" width="160" height="130" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <rect x="480" y="90" width="160" height="130" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

            <!-- Raised Twin Scissor Fork Plates -->
            <rect x="180" y="-30" width="120" height="30" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>
            <rect x="340" y="-30" width="120" height="30" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>

            <!-- Expanded Scissor X-Arms -->
            <line x1="190" y1="0" x2="290" y2="190" stroke="#4ade80" stroke-width="5"/>
            <line x1="290" y1="0" x2="190" y2="190" stroke="#4ade80" stroke-width="5"/>
            <circle cx="240" cy="95" r="7" fill="#f59e0b"/>

            <line x1="350" y1="0" x2="450" y2="190" stroke="#4ade80" stroke-width="5"/>
            <line x1="450" y1="0" x2="350" y2="190" stroke="#4ade80" stroke-width="5"/>
            <circle cx="400" cy="95" r="7" fill="#f59e0b"/>

            <text x="320" y="255" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">TOTAL LIFT STROKE = 140.0 mm (PALLET RAISED TO 310 mm)</text>
        </g>
    </g>

    <!-- SIDE CUTAWAY ELEVATION -->
    <g transform="translate(100, 520)">
        <text x="670" y="-30" fill="#38bdf8" font-size="22" font-family="sans-serif" font-weight="bold" text-anchor="middle">SIDE CUTAWAY ELEVATION (BALL SCREW &amp; SCISSOR DRIVE MECHANISM)</text>
        
        <rect x="0" y="0" width="1340" height="260" rx="10" fill="#0f172a" stroke="#f8fafc" stroke-width="4"/>

        <!-- Drive Wheels -->
        <circle cx="150" cy="260" r="60" fill="#1e293b" stroke="#ef4444" stroke-width="4"/>
        <circle cx="1190" cy="260" r="60" fill="#1e293b" stroke="#ef4444" stroke-width="4"/>

        <!-- Linear Guide Rail along bottom -->
        <rect x="100" y="220" width="1140" height="20" fill="#334155" stroke="#4ade80" stroke-width="2"/>

        <!-- Central Ball Screw Shaft -->
        <line x1="150" y1="180" x2="1100" y2="180" stroke="#f59e0b" stroke-width="6" stroke-dasharray="12,4"/>
        <circle cx="150" cy="180" r="14" fill="#38bdf8"/>
        <text x="150" y="150" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">SERVO MOTOR</text>
        
        <!-- Sliding Nut & Scissor Base Pins -->
        <rect x="400" y="160" width="80" height="40" fill="#ef4444"/>
        <text x="440" y="150" fill="#ef4444" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">BALL NUT</text>

        <!-- Scissor X-Arms Side View -->
        <line x1="250" y1="50" x2="440" y2="220" stroke="#4ade80" stroke-width="6"/>
        <line x1="440" y1="50" x2="250" y2="220" stroke="#4ade80" stroke-width="6"/>
        <circle cx="345" cy="135" r="8" fill="#f59e0b"/>

        <line x1="750" y1="50" x2="940" y2="220" stroke="#4ade80" stroke-width="6"/>
        <line x1="940" y1="50" x2="750" y2="220" stroke="#4ade80" stroke-width="6"/>
        <circle cx="845" cy="135" r="8" fill="#f59e0b"/>

        <!-- Fork Top Platform -->
        <rect x="200" y="30" width="850" height="20" fill="#38bdf8" stroke="#f8fafc" stroke-width="3"/>

        <!-- Dimensions -->
        <line x1="0" y1="340" x2="1340" y2="340" stroke="#f8fafc" stroke-width="2"/>
        <text x="670" y="365" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">1200.0 mm (TOTAL AMR CHASSIS LENGTH)</text>
    </g>

    <!-- TITLE BLOCK -->
    <g transform="translate(1050, 1000)">
        <rect width="500" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
        <line x1="0" y1="50" x2="500" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="100" x2="500" y2="100" stroke="#38bdf8" stroke-width="2"/>
        <text x="20" y="35" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold">OFFICIAL TUSK E10 TITAN BLUEPRINT</text>
        <text x="20" y="85" fill="#94a3b8" font-size="16" font-family="sans-serif">DWG NO: AMR-E10-TITAN | REV: 5.0</text>
        <text x="20" y="135" fill="#94a3b8" font-size="16" font-family="sans-serif">TWIN PARALLEL BALL SCREW SCISSOR LIFT</text>
    </g>
</svg>"""

svg_file = "/tmp/tusk_e10_official_dual_scissor.svg"
png_file = "/tmp/tusk_e10_official_dual_scissor.png"

with open(svg_file, "w") as f:
    f.write(svg_assembly)
    
cmd = f"rsvg-convert -w 1600 -h 1200 {svg_file} -o {png_file}"
subprocess.run(cmd, shell=True)

out_png = os.path.join(scratch_dir, "tusk_e10_official_dual_scissor.png")
brain_png = os.path.join(brain_dir, "tusk_e10_official_dual_scissor.png")
doc_png = os.path.join(doc_dir, "tusk_e10_official_dual_scissor.png")
pict_png = os.path.join(pict_dir, "tusk_e10_official_dual_scissor.png")

subprocess.run(f"cp {png_file} {out_png}", shell=True)
subprocess.run(f"cp {png_file} {brain_png}", shell=True)
subprocess.run(f"cp {png_file} {doc_png}", shell=True)
subprocess.run(f"cp {png_file} {pict_png}", shell=True)
print(f"Generated Official Tusk E10 Dual Scissor PNG: {os.path.getsize(png_file)} bytes")

