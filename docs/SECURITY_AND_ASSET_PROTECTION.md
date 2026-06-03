# Security & Asset Protection Protocol

**Document Version:** 1.0  
**Effective Date:** 2026-06-03  
**Classification:** Internal Operational Policy  

---

## 1. Physical Hardening: Rolling Vault Truck Protocols

The mobile command truck serves as our primary rolling vault, ensuring secure transport and storage of all robotic assets in the challenging urban environment of Lyari Basin.

### 1.1 Truck Security Standards
- **Reinforced Storage Vault:** The truck bed is fitted with a modular, weather-sealed, steel-reinforced compartment rated IP67 against dust and water ingress.
- **Locking Mechanisms:** Primary lock: Abloy PL362 (pick-resistant, hardened steel). Secondary: GPS-enabled electromechanical lock integrated with the vehicle alarm.
- **Alarm System:** Viper 5706V 2-way security system with shock sensors, door sensors, and tilt sensors. Alerts dispatched to GM and lead technician via SMS/onboard comms.
- **Surveillance:** 360° dashcam coverage with night vision capability. Footage retained locally for 30 days and automatically uploaded to secure cloud storage when in WiFi range.

### 1.2 Transit Security Procedures
- **Pre-Movement Check:** All equipment locked, latches secured, and GPS tracker activated. Verification logged in transit sheet.
- **Escort Protocol:** On high-risk routes, a community guardian or hired security rides along during transit.
- **Route Planning:** GM reviews daily travel plans using the day's risk assessment and chooses primary/alternate routes accordingly.

---

## 2. Modular Decoupling: End-of-Shift Component Removal Ritual

At the close of each operational day, critical components undergo a deliberate removal ritual to reduce theft risk and enable overnight maintenance.

### 2.1 Component Inventory Protocol
| Component | Storage Location | Security Action |
|-----------|------------------|---------------|
| UGV Compute Block (Jetson/RPI) | Mobile Vault | Removed nightly |
| Drone Battery Packs | Fire-Safe LiPo Bags | Removed nightly |
| Motor Controller ESP32 Units | Anti-Static Cases | Removed nightly |
| Sensor Arrays (Lidar, Camera) | Shock-Proof Cases | Removed nightly |

### 2.2 Removal Checklist
1. Power down all systems and disconnect batteries.
2. Photograph each component's serial number and condition for digital log.
3. Place components in designated cases with RFID tags.
4. Verify case count against daily manifest (must match).
5. Secure cases in truck vault; lock and activate alarm.

---

## 3. Silent Telemetry: Independent GPS/LoRaWAN Tracking

Each major asset carries independent tracking to enable silent recovery in event of theft or loss.

### 3.1 Tracking Hardware Specification
- **GPS Module:** Quectel L86-M33 (99% sensitivity, AGPS-ready) integrated into each asset's control board.
- **Radio Backup:** RFM95W LoRa module (433 MHz) transmitting heartbeat every 30 seconds to community gateway nodes.
- **Power Source:** Dedicated LiPo cell providing >72 hours of independent tracking.
- **Activation:** GPS/LoRa units remain active as long as asset battery retains >20% capacity; fallback to dedicated cell.

### 3.2 Recovery Network
- **Community Gateways:** Volunteers host LoRaWAN gateways on rooftops; their registration and monthly stipend covered under "Micro-Incentive Seeding" budget.
- **Law Enforcement:** Encrypted geofence breach alerts sent to GM and local community liaison; recovery actions coordinated through established local networks.

---

## 4. Social Shield: Community Custodianship & Guardian Incentives

Our security model extends into the social domain, leveraging local knowledge and stake in the project as a deterrent against sabotage or theft.

### 4.1 Guardian Incentive Program
- **Monthly Stipend:** Rs 5,000 provided to registered community guardians who assist in overnight site watches and transit escort duties.
- **Micro-Wallet Integration:** Guardians receive a QR code sticker; any citizen scanning it to report suspicious activity earns a Rs 50 micro-reward.
- **Recognition Tiers:** Based on cumulative contributions, guardians progress through Bronze/Silver/Gold tiers with increasing monthly stipends and priority employment consideration.

### 4.2 Cultural Integration Strategy
- **Local Artisan Collaboration:** UGV styling incorporates traditional Karachi truck art; community sees the robot as "theirs."
- **School Partnership:** Local schools invited to name individual drones; children become invested stakeholders.
- **Transparency Boards:** Daily operational summary posted at neighborhood mosque/community center; open-source logs available via QR code.

---

## Worker Welfare Note

All security protocols are designed around the **Alcoa Keystone Habit**: by ensuring our workers feel protected and valued, we create operational discipline that naturally extends to asset protection. Every security procedure considers the physical and psychological safety of personnel first, recognizing that secure workers equal secure hardware.