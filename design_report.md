# Engineering Design, Mechanism & Model Report: Tusk-Style Pallet Moving AMR

This report provides a comprehensive, A-to-Z technical breakdown of a low-profile Autonomous Mobile Robot (AMR) designed for pallet handling, inspired by Tusk Robotics' Autonomous Pallet Robots (APR). It details all mechanisms, mechanical components (including telescopic guide rails and folding wheels), sizing calculations, and the complete family of product models.

---

## 1. Introduction: The APR Concept

Traditional automated guided vehicles (AGVs) for pallet handling are often modified versions of standard manual forklifts. These systems are heavy, rely on massive counterweights to balance cantilevered loads, have a high center of gravity, and require wide aisles to turn. 

In contrast, the **Autonomous Pallet Robot (APR)** concept pioneered by Tusk Robots utilizes a low-profile chassis. Rather than carrying the load on a cantilevered mast, the robot slides underneath or inserts its forks directly into the pallet openings. The load is lifted locally using a built-in vertical lift mechanism and carried directly over the robot's footprint. This results in:
* **Minimal Footprint:** The robot is barely larger than the pallet itself.
* **Narrow-Aisle Navigation:** Ability to operate in aisles as narrow as 1.4 meters for travel and 2.0 meters for pick-and-place.
* **High Stability:** Lower center of gravity during transit since the load sits close to the ground (raised by only ~50-100 mm).

---

## 2. Mechanical Architecture & Wheel Layout

The robot chassis consists of a rear compartment (housing electronics, power, and traction axles) and a front vertical lift carriage that carries two extending, adjustable forks.

```
       +---------------------------------------+
       |                 BATT                  |   <-- Rear Electronics Compartment
       |   +-------------------------------+   |
       |   |             IPC               |   |
       |   +-------------------------------+   |
       |  [Caster]      [Drive]      [Caster]  |   <-- Differential Drive Axis
       +----|--------------|--------------|----+
            |              |              |
            +-------[Lift Carriage]-------+        <-- Vertically guided on chassis rails
            |       |              |      |
            |       +----+----+    |      |        <-- Linear Slides for Fork Width
            |=======|=========|====|======|        <-- Adjust (Transverse Lead Screw)
            |       +----+----+    |      |
            |              |              |
            |   +----------+----------+   |        
            |   |   Telescopic Rails  |   |        <-- Multi-stage guide rails (Rollon DSS)
            |   |     Left Fork       |   |        
            |   |                     |   |
            |   |  [Folding Rollers]  |   |        <-- Foldable Tandem Wheels at Tips
            |   +---------------------+   |
            |                             |
            |   +---------------------+   |
            |   |   Telescopic Rails  |   |
            |   |     Right Fork      |   |
            |   |                     |   |
            |   |  [Folding Rollers]  |   |
            |   +---------------------+   |
            +-----------------------------+
```

### Wheel Configuration & Kinematics
As sketched on the right page of the notebook, the wheel layout utilizes:
1. **Two Differential Drive Wheels:** Mounted in the center-left and center-right of the rear chassis. This configuration allows for **in-place rotation** (zero turning radius), which is essential for maneuvering inside tight pallet lanes.
2. **Four Swivel Casters:** Located at the outer corners of the rear chassis. These casters are spring-loaded to ensure constant contact with the ground, absorbing floor irregularities and preventing the robot from tipping.
3. **Fork Tip Load Rollers:** Low-profile, tandem polyurethane rollers are placed at the front tip of each fork. When the forks slide into the bottom openings of a pallet, these rollers support the heavy payload.

---

## 3. A-to-Z Mechanism & Hardware Details

To keep the forks extremely thin ($65 \text{ mm}$ thickness) and prevent synchronization errors, the E10T uses a **unified carriage lift and fork extension architecture** rather than duplicate mechanisms in each fork.

### 3.1. Single-Motor Vertical Lift Carriage
Instead of duplicate motors and scissor lifts inside each fork, the entire fork carriage assembly is lifted vertically as a single unit on the front of the chassis base:
* **Vertical Guide Rails:** Two heavy-duty vertical linear profile rails (e.g., heavy-duty linear guide rails, L=500mm) are mounted on the front face of the chassis base. The carriage weldment slides along these rails using four flanged blocks.
* **Central Ball Screw Actuation:** A single high-capacity vertical ball screw (25mm diameter, 5mm pitch, L=400mm) is mounted centrally.
* **Actuation:** A single 1000W BLDC motor with a 1:15 planetary gearbox drives the ball screw. Rotating the screw raises or lowers the entire carriage, ensuring both forks lift in perfect synchronization with zero risk of tilt.

---

### 3.2. Telescopic Fork Extension Guide Rails
To pick up a pallet, the forks must extend forward out of the carriage by $1000\text{ to }1400 \text{ mm}$. Because the forks carry a cantilevered load of up to 1 ton ($1000 \text{ kg}$) before the front load rollers contact the floor, the guide rails must withstand immense bending moments.

#### Component Selection & Operation:
* **Telescopic Linear Guide Rails:** The robot uses heavy-duty, multi-stage industrial telescopic slides. These rails consist of an intermediate S-shaped steel profile and two sliding guide rails with ball cages, allowing for **over-extension** (the forks can extend more than 100% of their retracted length).
* **Single-Motor Synchronized Drive:** A single 24V 200W geared servo motor is mounted on the lift carriage. It drives a transverse splined shaft. The drive sprockets for both forks' extension chains slide along this splined shaft during width adjustment, but rotate with it. This extends both forks in perfect synchronization with only one motor.

---

### 3.3. Retractable & Folding Fork Wheel Mechanism
When handling closed-bottom pallets (such as EUR-2 pallets or "田" shaped pallets), the bottom of the pallet is blocked by transverse boards. A traditional pallet jack cannot slide in because its front rollers would crash into these boards. 

The E10T uses a **passive retractable load roller mechanism** at the front tip of each fork:

```
      A. ENTERING PALLET (Wheels Folded UP)
      +======================================+
      |  (Forks slide OVER bottom boards)    |
      |   (o)                                |
      |    \__ (Swingarm raised)             |
      |     (O) (Roller folded inside fork)  |
      +======================================+
         [=== Bottom Pallet Board ===]
      
      ---------------------------------------------------------
      
      B. LIFTING LOAD (Wheels Folded DOWN)
      +======================================+
      |                                      |
      |   (o)                                |
      |    | (Swingarm pushed down through gap)|
      |   (O) (Roller contacts floor)        |
      +====|=================================+
           v   [=== Bottom Pallet Board ===]
      =========== Floor Line ===========
```

#### Operational Sequence:
1. **Approach & Insertion (Forks Extend, Wheels UP):** As the telescopic forks extend and slide into the pallet, the front load rollers are **folded up** completely inside the $65\text{ mm}$ fork frame. This allows the forks to slide over the pallet's bottom boards without collision.
2. **Deployment & Lift (Wheels DOWN):** Once the forks are fully inserted, the central lift carriage begins to rise. A mechanical pull-rod linkage running inside the fork channel connects the front roller swingarm to the lifting carriage frame. As the carriage lifts relative to the chassis wheels, the linkage pushes the swingarm **downwards** through the gaps in the bottom boards to contact the floor.
3. **Synchronization:** This mechanical linkage ensures that the front wheels deploy at the exact same rate the rear carriage lifts, keeping the forks level and stable throughout the lifting sequence.

---

### 3.4. Transverse Fork Width Adjustment Mechanism
To handle different pallet widths (EUR-1: 800mm, EUR-2: 1000mm), the width span of the forks adjusts dynamically:
* **Transverse Linear Guides:** The base of each telescopic fork is mounted on linear guide carriages (e.g., Hiwin HGW20CC) on a transverse rail fixed to the front face of the carriage.
* **Differential Lead Screw:** A transverse lead screw runs through both fork bases. One half of the screw has left-handed threads, and the other has right-handed threads.
* **Width Adjust Motor:** A 24V DC geared motor with an encoder rotates the screw, sliding both forks symmetrically inward or outward between $550 \text{ mm}$ and $900 \text{ mm}$.

---

## 4. Sizing Calculations

### 4.1. Carriage Lift Actuation Force & Motor Torque
For a direct vertical lift carriage, the vertical load to lift is:

W_total = Payload + Lift Carriage Weight = 1080 kg

The vertical force required:

F_lift = 1080 kg × 9.81 m/s² ≈ 10,595 N

#### Ball Screw Torque:
The torque T_screw required to drive the vertical ball screw (with pitch p = 5 mm, lead L = 0.005 m, and screw efficiency η_screw = 0.90) is:

T_screw = (F_lift × L) / (2 × π × η_screw) = (10,595 × 0.005) / (2 × 3.1416 × 0.90) ≈ 9.37 Nm

#### Lift Motor sizing (with 1:15 Gearbox):
With a gearbox reduction of R = 15 and mechanical efficiency η_gearbox = 0.95, the required lift motor torque T_motor is:

T_motor = T_screw / (R × η_gearbox) = 9.37 / (15 × 0.95) ≈ 0.66 Nm

A standard **1000W BLDC motor** (rated torque ≈ 3.18 Nm at 3000 RPM) provides a safety factor of 4.8, easily handling starting acceleration and dynamic loading.

---

### 4.2. Drive Traction & Motor Torque
* **Total Gross Mass (M):** 1320 kg (Robot 320 kg + Payload 1000 kg).
* **Max Speed (v_max):** 1.5 m/s.
* **Acceleration Time (t_acc):** 2.0 s (Acceleration a = 0.75 m/s²).
* **Acceleration Force (F_acc):** M × a = 1320 × 0.75 = 990 N.
* **Rolling Resistance (F_roll):** M × g × f_r = 1320 × 9.81 × 0.02 ≈ 258.9 N (assuming polyurethane wheels on warehouse concrete, f_r = 0.02).
* **Total Tractive Effort (F_total):** F_acc + F_roll = 990 + 258.9 = 1248.9 N.
* **Force per Drive Wheel (2 active wheels):** F_wheel = F_total / 2 ≈ 624.5 N.
* **Wheel Torque (T_wheel):** F_wheel × R_wheel = 624.5 × 0.10 m ≈ 62.5 Nm (for 200 mm diameter wheels, R_wheel = 0.10 m).

#### Drive Motor Sizing (with 1:20 Gearbox):
Using a gearbox reduction of R = 20 (efficiency η_gearbox = 0.95):

T_drive_motor = T_wheel / (R × η_gearbox) = 62.5 / (20 × 0.95) ≈ 3.29 Nm

* **Motor Speed at Max Velocity:** 
  ω_motor = (v_max / R_wheel) × R = (1.5 / 0.10) × 20 = 300 rad/s ≈ 2865 RPM
* **Required Motor Power:** 
  P_motor = T_drive_motor × ω_motor = 3.29 Nm × 300 rad/s ≈ 987 W (Peak)

Therefore, **two 750W BLDC drive motors** with 1:20 planetary gearboxes provide excellent travel and acceleration.

---

## 5. Tusk Robotics Product Family & Models

Tusk Robotics offers several families of robots optimized for different pallet handling, stacking, and warehouse layouts. 

### 5.1. E-Series (Autonomous Pallet Robots - APRs)
This is the core E-series flat APR range designed for general intelligent pallet transport.
*   **E10 (Standard):** The flagship model. Features a 1000 kg capacity, 170mm lowered chassis height, and dual navigation (SLAM + QR code). The pallet is loaded directly over the vehicle body deck, offering high stability during travel.
*   **E10-SLAM:** Configured specifically with primary SLAM navigation (no floor markers/QR codes required) using safety LiDARs.
*   **E10T (Telescopic Fork):** Designed with the **telescopic extending fork** (1400mm reach) and **folding front wheels** to handle double-sided (closed-bottom) pallets directly from the floor.
*   **E15:** A heavy-duty version of the E10 with a load capacity of **1500 kg** (1.5 Tons).
*   **E08 & E12:** Sibling models designed to handle lighter (800 kg) and heavier (1200 kg) standard logistics lines.
*   **E10 (Thin/Slim):** Extra low-profile version with a lowered deck height to slide under low-clearance customized pallets or rack frames.

### 5.2. T-Series (Split Fork APRs)
*   **T10:** Designed specifically for narrow-aisle, closed-pallet handling. It features a unique **split-fork design** combined with a simultaneous support plate. When the forks slide into the pallet, the support plate lifts to distribute the load across the chassis, allowing the robot to remain balanced without a heavy rear counterweight. Enables travel in aisles as narrow as 1.35m.

### 5.3. F-Series (Autonomous Stacking/Forklift Robots)
*   **FL10 (High-Reach Stacker):** Unlike the flat E-series, the FL10 is a tall vertical stacker (approx. 2.0 meters tall) designed for high-density racking.
    *   **Lifting Height:** Lifts loads up to 2.5 meters.
    *   **Capacity:** Supports 800 kg at max height, or 1000 kg up to 1.6 meters.
    *   **Narrow-Aisle:** Operates in aisles of 1.8m to 1.85m, enabling double-layer stacking and automated conveyor line transfers.
*   **F10:** Standard autonomous stacking forklift version.

### 5.4. C-Series (Underride/Tugger AMRs)
*   **C10:** Designed to slide completely underneath custom racks, carts, or rolling cages (underride AMR). It utilizes a central pin elevator or a small flatbed lifting table to lock onto and lift the cart off the ground to transport it.

---

## 6. Software & Navigation System

### 6.1. High-Level Navigation Stack
* **PC Hardware:** Industrial PC running Ubuntu 22.04 LTS and ROS 2.
* **SLAM & Mapping:** Uses safety LiDAR data processed through the **SLAM Toolbox** or **Cartographer** to build a static grid map.
* **Path Planning & Navigation:** The **ROS 2 Nav2** stack utilizes the TEB Local Planner to compute smooth trajectories for differential drive kinematics.

### 6.2. Low-Level Control Node
* **MCU Hardware:** STM32F4 or Teensy 4.1 running micro-ROS.
* **Travel Synchronization:** Encoder feedback monitors the single extension motor shaft, ensuring that the splined shaft extends both forks symmetrically.
* **Passive Wheel Deployment:** The MCU monitors vertical lift encoders. Proximity switches at the top and bottom of the vertical lift carriage report carriage state, confirming the mechanical pull-rods have deployed or retracted the front wheels.
