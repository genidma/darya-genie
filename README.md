# Darya Genie (दरिया जिनी / دریا جنی) 🌊🤖

> **Proposed: Grassroots, community-funded robotic river restoration for the Lyari Basin, Karachi and another river that is to be determined in India.**

Darya Genie is an open-source, decentralized civic-tech initiative designed to bypass institutional gridlock and clean up urban waterways. By combining low-cost autonomous waste-harvesting hardware with a culturally resonant, interactive mascot and a micro-equity donation loop, we shift the environmental narrative from "the state's problem" to a community-owned triumph.

### Founder's Vision

Darya (meaning river in Hindi or Urdu) Genie was born from almost two decades of lived experience near polluted rivers—specifically 5 years living 1 km away—a personal journey sparked by watching modern travel vlogs revisit these same waterways. The vision is a humble one: What if you could fork a repository here on GitHub and immediately access the material needed to help clean up a local river or stream safely, sustainably, and without creating further environmental or safety issues?

## Concept Visuals

![Darya Genie Concept](img/darya_genie_concept_06-03-2026.png)
*Darya Genie UGV concept illustration.*

![Swarm Coordination Hope & Healing](img/darya_genie_concept_swarm_co-ord_hope_healing_06-03-2026.png)
*Illustration of drone swarm coordinating with UGV for hopeful healing of the river.*

## Repository Structure

This repository is organized as follows:

```
├── hardware/              # UGV chassis CAD files, wiring schematics, and BOM
├── firmware/              # Microcontroller code for motor drivers and LED matrix
│   └── motor_controller/  # PlatformIO project for ESP32 with micro-ROS
├── src/
│   ├── genie_brain/       # ROS 2 package for navigation and vision
│   ├── payment_gateway/   # FastAPI server for mobile wallet webhooks
│   └── api/               # Authentication and certification middleware
├── docs/                  
│   ├── safety/            # Darya Safety-First Certification Course (45-min curriculum)
│   ├── restoration/
│   │   └── gis_protocols.md         # Satellite-to-site suitability logic
│   ├── CURRICULUM.md      # Educational outreach materials
│   ├── DRONE_PROTOCOLS.md # Drone-to-UGV coordination protocols
│   └── SECURITY_AND_ASSET_PROTECTION.md # Asset protection and security policy
├── scripts/
│   └── certification_gatekeeper.py  # Validates quiz and updates User_Registry
└── tests/                 # Hardware-in-the-loop (HIL) simulation scripts
```

## 💰 Financial Transparency & Worker Welfare (Year 01 Only)

Traditional top-down river restoration initiatives for the Lyari Basin carry massive, gridlocked budgets (such as the S-III plan's **~$150M CAD / PKR 43B** allocation), which frequently suffer from bureaucratic friction and low deployment execution. 

Darya Genie completely flips this paradigm. We treat **Worker Welfare as our Alcoa Keystone Habit**—inspired by Charles Duhigg's *The Power of Habit*. We believe that by fiercely protecting, properly feeding, and aggressively investing in our frontline team, we automatically secure operational safety, technical discipline, and unshakeable community trust. 

Our expanded **Year 01 Pilot Target is $320,000 CAD**, built explicitly to eliminate hand-to-mouth precarity, establish multi-domain aerial scouting operations, and design a high-mobility leadership pipeline:

| Phase / Budget Category | Year 01 Allocation (CAD) | Cornerstone Utility & Worker Welfare Impact |
| :--- | :--- | :--- |
| **Core Salaries & Management** | $145,000 | Guarantees living wages for ground technicians, drone operators, a part-time deployment driver, a Technical Trainer, and a full-time project General Manager. |
| **Drone Hardware & Logistics** | $45,000 | Procuring a multi-drone aerial reconnaissance fleet, custom climate-controlled storage cases, and a secure mobile logistics truck to transport the UGV and drones safely. |
| **Aviation Safety & Certifications** | $20,000 | Earmarked for official Civil Aviation Authority (CAA) commercial drone licensing, rigorous field safety training courses, and operational insurance. |
| **Upward Mobility & Executive Training** | $40,000 | Structured 2-to-3 year fast-track program. Earmarked funds for leadership workshops, advanced robotics upskilling, and business management training to transition field workers into future Directors. |
| **Holistic Support, Meals & Office Care** | $35,000 | Daily high-nutrition catered meals for all ground and aerial crew, field health checks, high-grade personal protective equipment (PPE), and air-conditioned office workspaces, with showers and a place to take naps |
| **Core Ground Autonomy (UGV)** | $25,000 | Rugged tracked UGV chassis fabrication, Jetson/Raspberry Pi compute blocks, conveyor mechanics, sealed sensor suites, and local W-11 truck art styling. |
| **Community Seeding** | $10,000 | Initial liquidity to back local community collection drop-hubs for immediate wallet payouts. This complements robot operations by incentivizing fine-detail collection in narrow banks/alleys unreachable by UGV, creating a "Micro-Equity Loop" where citizens become restoration partners. |

*Every 5-rupee (or 20 rupee) micro-donation processed by the gateway flows directly into sustaining local incentive liquidity, protecting team welfare, and supporting hardware maintenance.*

### 📈 The Micro-Equity Scalability Model (The 20/20 Projection)

To understand the mathematical velocity of decentralized civic tech, consider this hyper-conservative baseline projection for Karachi's urban density:

* **Target Activation:** 20% of Karachi's projected population (~4.62 Million active community participants).
* **Micro-Equity Quantum:** A single, one-time donation of **20 PKR (~$0.07 CAD)** per person.

$$	ext{Total Capital} = 4,620,000 	imes 20	ext{ PKR} = 92,400,000	ext{ PKR}$$

This single, low-friction activation wave yields approximately **$322,300 CAD**. 

#### ⚡ The Operational Reality Shift
1. **Instant Self-Sovereignty:** This single loop completely clears our expanded **Year 01 Pilot Budget ($320,000 CAD)**, securing premium living wages, drone safety certifications, mobile logistics, and hardware fabrication with an immediate cash reserve to seed Year 02.
2. **Infinite Compound Runway:** If this same 20% cohort triggers a 20 PKR transaction just once per quarter, the platform generates over **$1.2 Million CAD annually**—fully funding a multi-robot fleet, localized aerial monitoring, and a permanent local leadership pipeline without a single cent of institutional debt or state intervention.

## Safety & Certification Pipeline

Darya Genie operates on the fundamental principle that **safety certification is a prerequisite for participation**. All community collectors, drone operators, and field personnel must complete the **Darya Safety-First Certification Course** before engaging in river cleanup activities. This 45-minute curriculum is version-controlled and auditable.

```
README.md → /docs/safety/ → /scripts/certification_gatekeeper.py → /src/api/auth.py → User.is_certified = True
```

### Path to Certified Collector

1. **Curriculum Access:** Participants complete the 3-module safety course (`/docs/safety/module_01-03_*.md`) covering hazards, equipment handling, and toxin awareness.
2. **Assessment Validation:** `certification_gatekeeper.py` validates the final quiz and updates the User_Registry via `POST /api/certify` upon passing.
3. **Payment Gateway Enforcement:** `/src/api/auth.py` middleware checks `User.is_certified == True` before processing any micro-incentive payout.

For full curriculum details and certification requirements, see the [`/docs/safety/`](/docs/safety/) directory.

### Restoration Pipeline Integration
The GIS protocols feed directly into the mangrove propagation workflow. Data is available via ESA (European Space Agency's) [Sentinel-2 Mission](https://browser.dataspace.copernicus.eu/?zoom=16&lat=24.879&lng=67.01395&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX1%2FEtIi0s5wgJf9hrUj6eo955RFHfzkjRinuZQfXnaEd77%2F097XT4GX2lCW3DsLLtBi05SG5P%2FZwlSRsTEKkKN48iTv5JvAf0bqrvGCpz0ysBMZmm9fUuXXK&datasetId=S2_L2A_CDAS). And private data is available via other satellite providers (not factored into the budget as of yet)

![Sentinel-2 dashboard](img/darya_genie_sentinel2_snapshot_06-03-2026.PNG)
*Sentinel-2 dashboard snapshot*

```
Sentinel-2 → GIS Filtering → Drone Verification → Mangrove Planting → Growth Audits
```

![Hiring University Students in order to inform decision making](img/darya_genie_concept_GIS_supported_mangrove_reforesting_06-03-2026.png)
*University students hired in order to identify ideal flood-proof zones via GIS (Geographic Information Systems)*

See [GIS & Satellite Suitability Protocol](/docs/restoration/gis_protocols.md) for technical details on converting satellite intel into planting coordinates.

![Mangrove Restoration](img/darya_genie_concept_mangrove_reforesting_06-03-2026.png)
*Drone-verified mangrove saplings being planted in GIS-validated zones.*

---

## 🔒 Security & Asset Protection

For a detailed breakdown of our multi-domain physical and social security protocols, please review the [Security & Asset Protection Protocol](/docs/SECURITY_AND_ASSET_PROTECTION.md).

## 🛠️ Security Audit Workflow

We maintain high code integrity by performing regular security audits. To audit new API contributions:

```bash
# 1. Run dependency audit to identify vulnerabilities
~/.local/bin/pip-audit -r src/api/requirements.txt

# 2. Run static analysis (SAST) to detect common Python security flaws
~/.local/bin/bandit -r src/api/
```

## 🔄 Development Workflow

We follow a structured branching strategy to ensure all contributions pass through rigorous testing and security verification before hitting production:

1. **Gemini Features:** `feature/gemini-updates` (Initial feature development)
2. **Integration/Testing:** `main-dev` (Consolidated features, security audits, and automated testing)
3. **Production:** `main` (Stable release candidate)

All PRs must be merged into `main-dev` first for testing. Only after passing all audits and tests can changes be promoted to `main`.

## 🤝 Credits and Notable Contributions

### Notable Contributions

| Handle | PR Link | Synopsis |
| :--- | :--- | :--- |
| [@HMS091](https://github.com/HMS091) | [PR #5](https://github.com/genidma/darya-genie/pull/5) | Implementation of FastAPI service for restoration and waste submission. |

### Credits

- [Gemini by Google](https://gemini.google.com/) as the original brainstorming partner and lead architect
- [@genidma](https://github.com/genidma) for the origination of the idea
- [Kilo - Nvidia Nemotron 3 Super(free)](https://github.com/Kilo-Org/kilocode) for helping update the README and helping develop the very first iteration of the codebase
- [Kilo - Laguna M1](https://github.com/Kilo-Org/kilocode) for advanced systems architecture and safety protocol development
- [Qoder](https://qoder.com/) (formerly Lingma) for helping link the image to the README.

## 🛰️ Riverine Ecosystem Monitoring

- [ ] Investigate satellite imagery for monitoring riverine health and restoration suitability — [Google AI Mode link](https://share.google/aimode/UbOT272aCmDSQSeHh)
