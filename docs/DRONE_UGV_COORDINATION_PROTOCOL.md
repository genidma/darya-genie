# Drone-UGV Coordination Protocol for Darya Genie

**Version:** 1.0  
**Effective Date:** 2026-06-03  
**Applicable To:** All field operations personnel, drone operators, UGV technicians, and General Managers operating in the Lyari Basin, Karachi.

---

## 1. Logistics, Transit, and Secure Storage

### 1.1 Mobile Command Truck Operations
- **Loading Protocol:**
  - UGV: Secured using four (4) ratchet straps rated for 5,000 lbs each, attached to chassis tie-down points. Straps inspected pre- and post-transit.
  - Drone Fleet: Each drone stored in custom-cut foam inserts within IP67-rated hard cases. Batteries removed and stored separately in fire-retardant LiPo bags.
  - Base Station: Tripod-mounted radios and laptops secured in shock-mounted racks. Cables coiled and Velcro-strapped to prevent snagging.
- **Transit:**
  - Maximum speed: 60 km/h on highways, 40 km/h on urban roads.
  - Driver must perform a 360° visual check of the truck's surroundings before moving.
  - General Manager (GM) or designated Part-Time Driver (PTD) maintains a transit log (paper and digital) noting departure/arrival times, route taken, and any incidents.
- **Unloading:**
  - Conducted on level ground with wheel chocks placed on the UGV.
  - Drones and equipment unloaded only after the truck engine is off and parking brake engaged.
  - UGV powered on only after clear of truck ramps and personnel are at least 5 meters away.

### 1.2 Climate-Controlled Storage
- **Storage Facility Requirements:**
  - Temperature: Maintained between 15°C and 25°C.
  - Humidity: Maintained between 40% and 60% RH.
  - Ventilation: Minimum 6 air changes per hour; LiPo storage area must have explosion-proof ventilation.
- **Battery Management:**
  - LiPo Batteries (Drones): Stored at 3.8V per cell (storage voltage) in fire-retardant bags. Voltage checked weekly.
  - UGV Batteries (Lead-Acid/LiFePO4): Kept on trickle charge when not in use. Electrolyte levels (if applicable) checked monthly.
  - Charging Logs: Each battery cycle logged in the digital asset management system (DAMS) including: date, operator, charger used, start/end voltage, temperature, and any anomalies.
- **End-of-Shift Security Audit:**
  - Conducted by the PTD and witnessed by the GM.
  - Checklist includes: all equipment accounted for, batteries stored correctly, vehicles locked, facility alarm set, and security camera footage reviewed.
  - Any discrepancies trigger an immediate incident report and notification to the Regional Director.

---

## 2. Aerial Scouting and UGV Pathfinding Coordination

### 2.1 Drone Fleet Mission Execution
- **Pre-Flight Planning:**
  - Mission area defined in QGroundControl using the latest riverbank survey (updated weekly).
  - Flight altitude: 30-50m AGL for optimal GSD (Ground Sampling Distance) of 2cm/pixel.
  - Overlap: Frontal 80%, side 70% to ensure photogrammetric quality.
  - Weather limits: Max wind speed 15 km/h, no precipitation, visibility >5km.
- **Data Collection:**
  - Primary Sensor: RGB camera (Sony RX1R II equivalent) for plastic detection.
  - Secondary Sensor: Thermal camera (FLIR Vue Pro R) for identifying organic blockages and hazardous hotspots.
  - Telemetry: GPS, IMU, and battery voltage streamed at 5Hz to the Ground Control Station (GCS).
- **In-Flight Adaptation:**
  - Drone pilot can adjust waypoints in real-time based on live video feed to investigate suspected hazards.
  - All deviations from the planned path are logged and geotagged.

### 2.2 Data Processing and UGV Integration
- **Edge Processing (On GCS Laptop):**
  - Raw imagery processed via OpenDroneMap (ODM) to generate:
    - Orthomosaic (GeoTIFF)
    - Digital Surface Model (DSM)
    - Plastic density heatmap (using trained TensorFlow model)
  - Processing must complete within 15 minutes of landing to be tactically useful.
- **ROS 2 Interface:**
  - Processed geotiff and heatmap are converted to ROS 2 `nav_msgs/OccupancyGrid` and published to the topic `/drone/scout_map`.
  - Plastic density thresholds (configurable via ROS 2 parameters) are used to generate waypoints for high-density zones.
  - The `genie_brain` navigation node subscribes to `/drone/scout_map` and uses it as a layered costmap in conjunction with its own lidar scans.
  - Waypoints are published to `/genie/navigation/target` as `geometry_msgs/PoseStamped` arrays.
- **Fallback Mechanism:**
  - If drone data is stale (>30 minutes old) or unavailable, the UGV reverts to its internal SLAM and frontier-based exploration.

---

## 3. Civil Aviation Authority (CAA) Regulatory Compliance & Operator Certification

### 3.1 Operator Prerequisites
- **Mandatory Licensing:**
  - All drone operators must hold a valid CAA Remote Pilot License (RPL) for multicopter operations.
  - License must be current (renewed every 24 months) and accompanied by a Class 2 Medical Certificate.
- **Pre-Flight Safety Checklist (Conducted Before Every Flight):**
  - [ ] Airspace check via CAA's DroneAlert app (verified no temporary flight restrictions).
  - [ ] Aircraft inspection: propellers, motors, frame, GPS lock (>8 satellites).
  - [ ] Battery health: voltage balance, physical swelling, temperature <40°C.
  - [ ] Control link: RC and telemetry signal strength > -85 dBm.
  - [ ] Emergency systems: RTH, geofence, and failsafe functions tested.
  - [ ] Weather re-check: wind, precipitation, visibility.
  - [ ] Ground crew briefed: spotters assigned, emergency procedures reviewed.
- **Airspace Geofencing:**
  - All drones programmed with CAA-defined Lyari Basin UAS Flight Zone (latitude/longitude boundaries).
  - Geofence altitude ceiling: 120m AGL (CAA maximum for uncontrolled airspace).
  - Near-restricted zones (e.g., airports, military bases) trigger automatic RTH if breached.

### 3.2 Operator Upskilling Matrix
| **Experience Level** | **Timeframe** | **Key Competencies**                                                                 | **Responsibilities**                                                                 |
|----------------------|---------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Junior Operator      | 0-12 months   | CAA RPL, basic flight maneuvers, pre-flight checks, data offload                   | Flies supervised missions, assists in equipment maintenance, logs flight data.     |
| Field Operator       | 1-3 years     | Advanced mission planning, photogrammetry processing, emergency maneuvers, minor repairs | Leads solo flights, trains juniors, processes scout data, maintains flight logs.   |
| Operational Lead     | 3+ years      | Fleet coordination, risk assessment, regulatory liaison, incident command          | Schedules drone/UGV ops, interfaces with CAA/local authorities, mentors Field Ops. |
| Regional Director    | 5+ years      | Strategic planning, budget management, multi-site oversight, policy development    | Oversees all basin operations, ensures compliance, reports to NGO Board, seeks funding. |

*Note: Advancement requires documented flight hours, successful evaluations, and completion of internal safety courses.*

---

## 4. Field Safety, Emergency Fail-safes, and "Alcoa Keystone Habit" Integration

### 4.1 Core Safety Rules (Keystone Habit: Worker Welfare)
- **Minimum Standoff Distances:**
  - Drones must maintain **15 meters** horizontally from any unauthorised person, vehicle, or structure.
  - UGV must maintain **5 meters** from pedestrians during autonomous operation; switches to teleoperation if closer approach is needed.
- **Toxic Sludge Exposure Mitigation:**
  - All personnel must wear: nitrile gloves, rubber boots, face shields, and respirators (P100 filters) when within 10m of the water edge.
  - Post-shift decontamination: equipment washed with 10% bleach solution, personnel showered on-site.
- **Communication Loops:**
  - Ground crew uses Motorola DP4400e radios on Channel 1 (Primary) and Channel 2 (Emergency).
  - GM monitors all channels and conducts hourly check-ins via radio and WhatsApp group.
  - Any safety concern ("Stop Work Authority") can be issued by any crew member and must be acted upon immediately.

### 4.2 Automated Software Fail-safes
- **Drone Returns-to-Home (RTH) Triggers:**
  - **Low Battery:** RTH initiated at 30% remaining capacity (configurable).
  - **RC Signal Loss:** RTH after 3 seconds of no signal from transmitter.
  - **Geofence Breach:** Immediate RTH if drone exits CAA-approved flight zone.
  - **Critical System Failure:** IMU or GPS failure triggers landing in place (if safe) or RTH.
- **UGV Emergency Stop (E-Stop) Hooks:**
  - **Hardware:** Two (2) physical E-Stop buttons on the UGV chassis (IP67 rated) that cut motor power via redundant relays.
  - **Software via FastAPI Gateway:**
    - Endpoint: `POST /emergency/stop` (authenticated via API key).
    - Action: Publishes a `std_msgs/Bool` message (True) to the ROS 2 topic `/genie/e_stop`.
    - The `genie_brain` node subscribes to this topic and immediately sends zero-velocity commands to all motor controllers.
  - **Trigger Sources:** Can be activated by the GM via radio command (relayed to base station operator) or by any crew member using the authenticated mobile app.

### 4.3 Incident Reporting and Investigation
- **Immediate Response:**
  - For any injury: administer first aid, evacuate if necessary, notify GM and Regional Director.
  - For equipment damage: secure the scene, preserve evidence, notify GM.
- **Reporting:**
  - All incidents (near-misses, property damage, injury) must be logged in the Digital Incident Reporting System (DIRS) within 24 hours.
  - Reports include: timestamp, location, personnel involved, sequence of events, root cause analysis, and corrective actions.
- **Investigation:**
  - Regional Director leads investigation for Level 2+ incidents (potential for serious harm).
  - Findings reviewed quarterly by the Safety Committee to update protocols and training.

---

**Approval:**  
This protocol has been reviewed and approved by the Darya Genie Safety Committee and Regional Director for the Lyari Basin.

*End of Document*