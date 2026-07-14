/*
  =============================================================================
  Tusk-Style Autonomous Pallet Robot (APR) 3D Model
  =============================================================================
  Designed for EUR-2 Pallets (1200mm x 1000mm)
  
  All units in millimeters (mm).
  To view this model, open in OpenSCAD (https://www.openscad.org/)
  
  Features:
  - Low-profile differential-drive chassis (2 drive wheels + 4 corner casters)
  - Extending forks with internal scissor-lift linkage
  - Dual fork load rollers at front tips
  - Transverse slide rail for width adjustment
  - Semitransparent standard EUR-2 Pallet showing fork engagement
  =============================================================================
*/

// Design Parameters
robot_w = 1100;         // Chassis width
chassis_l = 400;        // Main body length
chassis_h = 170;        // Lowered chassis height
fork_l = 1000;          // Length of forks extending from main body
fork_w = 180;           // Width of each fork
fork_h = 65;            // Thickness of each fork when lowered
fork_spacing = 380;     // Space between forks (adjustable span)

drive_wheel_dia = 200;  // Center drive wheel diameter
drive_wheel_w = 75;     // Center drive wheel width
caster_dia = 100;       // Corner caster wheel diameter
fork_roller_dia = 60;   // Fork tip load roller diameter

lift_angle = 15;        // Lift linkage angle in degrees (0 to 25)
lift_height = 140 * sin(lift_angle); // Resulting vertical lift height (approx 0 to 60mm)

// Rendering control:
show_pallet = true;     // Set to false to hide the pallet
show_lift = true;       // Set to false to show robot in fully lowered state

$fn = 40;               // Cylindrical resolution

// Assembly Layout
union() {
    // Robot Base Assembly
    color("RoyalBlue") {
        chassis_body();
    }
    
    // Wheels & Actuation (Colored Yellow/Steel)
    drive_wheels();
    caster_wheels();
    
    // Forks Assembly (Left and Right)
    fork_offset_y = (fork_spacing + fork_w) / 2;
    
    // Left Fork
    translate([chassis_l, fork_offset_y - fork_w/2, 0])
        fork_assembly(show_lift ? lift_height : 0);
        
    // Right Fork
    translate([chassis_l, -fork_offset_y - fork_w/2, 0])
        fork_assembly(show_lift ? lift_height : 0);
        
    // Standard EUR-2 Pallet Overlay (Semi-transparent Wood)
    if (show_pallet) {
        translate([chassis_l - 100, -500, (show_lift ? lift_height : 0)]) {
            color([0.8, 0.6, 0.4, 0.45]) { // Semi-transparent brown
                eur2_pallet();
            }
        }
    }
}

// -----------------------------------------------------------------------------
// MODULES - DETAILED COMPONENTS
// -----------------------------------------------------------------------------

// Main low-profile chassis body
module chassis_body() {
    difference() {
        // Main block
        translate([0, -robot_w/2, 0])
            cube([chassis_l, robot_w, chassis_h]);
            
        // Cutout for front/rear LiDAR clearance (bevels)
        translate([-5, -robot_w/2 - 5, chassis_h - 40])
            rotate([0, 45, 0])
                cube([60, robot_w + 10, 60]);
                
        // Cutouts for drive wheels
        translate([chassis_l/2 - 10, -robot_w/2 - 5, -5])
            cube([60, drive_wheel_w + 10, drive_wheel_dia/2 + 20]);
        translate([chassis_l/2 - 10, robot_w/2 - drive_wheel_w - 5, -5])
            cube([60, drive_wheel_w + 10, drive_wheel_dia/2 + 20]);
            
        // Cutout for Battery Compartment access
        translate([50, -robot_w/4, chassis_h - 20])
            cube([150, robot_w/2, 25]);
    }
    
    // Front transverse slide rail for fork adjustment (simulated linear guide)
    color("DimGray") {
        translate([chassis_l - 15, -robot_w/2 + 80, 20])
            cube([15, robot_w - 160, 20]);
        translate([chassis_l - 15, -robot_w/2 + 80, 50])
            cube([15, robot_w - 160, 20]);
    }
}

// Drive Wheels (differential setup, mid-chassis)
module drive_wheels() {
    color("Orange") {
        // Left Drive Wheel
        translate([chassis_l/2, -robot_w/2 + drive_wheel_w/2, drive_wheel_dia/2 - 15]) {
            rotate([90, 0, 0]) {
                cylinder(d=drive_wheel_dia, h=drive_wheel_w, center=true);
                // Shaft
                color("LightGray")
                    cylinder(d=30, h=drive_wheel_w + 20, center=true);
            }
        }
        
        // Right Drive Wheel
        translate([chassis_l/2, robot_w/2 - drive_wheel_w/2, drive_wheel_dia/2 - 15]) {
            rotate([90, 0, 0]) {
                cylinder(d=drive_wheel_dia, h=drive_wheel_w, center=true);
                // Shaft
                color("LightGray")
                    cylinder(d=30, h=drive_wheel_w + 20, center=true);
            }
        }
    }
}

// Four corner caster assemblies
module caster_wheels() {
    color("DarkSlateGray") {
        // Caster positions
        cx = [40, chassis_l - 40];
        cy = [-robot_w/2 + 80, robot_w/2 - 80];
        
        for (x = cx) {
            for (y = cy) {
                translate([x, y, caster_dia/2 - 10]) {
                    // Wheel pivot mount
                    translate([0, 0, caster_dia/2 + 10])
                        cylinder(d=40, h=10, center=true);
                    // Caster Wheel
                    rotate([90, 0, 15]) {
                        cylinder(d=caster_dia, h=40, center=true);
                    }
                }
            }
        }
    }
}

// Fork assembly including bottom support fork, top lifting plate, and scissor mechanism
module fork_assembly(z_lift) {
    // 1. Lower Fork Base (stays near floor)
    color("SteelBlue") {
        difference() {
            // Fork body
            cube([fork_l, fork_w, fork_h]);
            // Inner channel for scissor lift & ball screw
            translate([20, 20, 15])
                cube([fork_l - 120, fork_w - 40, fork_h]);
            // Front roller axle slot
            translate([fork_l - 60, 10, -5])
                cube([40, fork_w - 20, 25]);
        }
    }
    
    // 2. Fork Tandem Load Rollers (low-profile wheel at front tip)
    color("Goldenrod") {
        // Twin rollers
        translate([fork_l - 45, fork_w/2, fork_roller_dia/2 - 5]) {
            rotate([90, 0, 0]) {
                cylinder(d=fork_roller_dia, h=fork_w - 30, center=true);
            }
        }
    }
    
    // 3. Scissor Lift Linkage Mechanism (Moving elements)
    // Pivot coordinate centers
    link_len = 240;
    px1 = 200;
    px2 = fork_l - 350;
    
    // Left link & Right link inside the fork
    color("Silver") {
        // Rear Scissor Leg Pair
        translate([px1, fork_w/2, 20])
            scissor_linkage(link_len, lift_angle);
            
        // Front Scissor Leg Pair
        translate([px2, fork_w/2, 20])
            scissor_linkage(link_len, lift_angle);
            
        // Actuator Screw (Ball screw) representation
        translate([50, fork_w/2, 25]) {
            rotate([0, 90, 0])
                cylinder(d=20, h=400);
        }
    }
    
    // 4. Upper Fork Deck (Lifts Vertically)
    color("DeepSkyBlue") {
        translate([10, 0, fork_h + z_lift]) {
            cube([fork_l - 20, fork_w, 15]); // Top plate
            // Skirts extending downwards to cover interior
            translate([0, 0, -20])
                cube([fork_l - 20, 5, 20]);
            translate([0, fork_w - 5, -20])
                cube([fork_l - 20, 5, 20]);
        }
    }
}

// Scissor Linkage definition
module scissor_linkage(length, angle) {
    // We draw two crossed bars
    rotate([0, angle, 0]) {
        translate([-length/2, -15, 0])
            cube([length, 10, 15]);
    }
    rotate([0, -angle, 0]) {
        translate([-length/2, 5, 0])
            cube([length, 10, 15]);
    }
    // Pivot pin in center
    cylinder(d=12, h=30, center=true);
}

// Standard EUR-2 Pallet (1200 x 1000 x 144 mm)
module eur2_pallet() {
    p_len = 1200;
    p_wid = 1000;
    p_h = 144;
    board_t = 22; // Board thickness
    block_h = 78; // Block height
    
    // 1. Top Deck Boards (horizontal, spaced out)
    for (y = [0, 200, 400, 600, 800, 980]) {
        translate([0, y, p_h - board_t])
            cube([p_len, 20, board_t]);
    }
    
    // 2. Stringer Boards (transverse, under deck boards)
    for (x = [0, p_len/2 - 10, p_len - 20]) {
        translate([x, 0, p_h - 2*board_t])
            cube([20, p_wid, board_t]);
    }
    
    // 3. Corner & Center Blocks (9 blocks total)
    bx = [0, p_len/2 - 60, p_len - 120];
    by = [0, p_wid/2 - 60, p_wid - 120];
    
    for (x = bx) {
        for (y = by) {
            translate([x, y, board_t])
                cube([120, 120, block_h]);
        }
    }
    
    // 4. Bottom Boards (three longitudinal boards running across bottom)
    for (y = [0, p_wid/2 - 60, p_wid - 120]) {
        translate([0, y, 0])
            cube([p_len, 120, board_t]);
    }
}
