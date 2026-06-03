# Darya Genie (دريا جني) 🌊🤖

> **Grassroots, community-funded robotic river restoration for the Lyari Basin, Karachi.**

Darya Genie is an open-source, decentralized civic-tech initiative designed to bypass institutional gridlock and clean up urban waterways. By combining low-cost autonomous waste-harvesting hardware with a culturally resonant, interactive mascot and a micro-equity donation loop, we shift the environmental narrative from "the state's problem" to a community-owned triumph.

---

## 🚀 The Core Ecosystem

Darya Genie operates via three integrated layers:

1. **The Mascot UGV (Darya Genie):** A rugged, expressive, tracked Unmanned Ground Vehicle that manages shallow-bank skimming, interacts with local neighborhoods, and serves as an educational ambassador.

![Darya Genie Concept](img/darya_genie_concept_06-03-2026.png)

2. **The Micro-Equity Network:** An API-driven loop integrating local mobile wallets (EasyPaisa/JazzCash). A 5-rupee micro-donation activates the Genie's physical interactive "dance" and immediate trash collection sequence.
3. **Upstream Interceptors:** Low-cost physical trash booms and autonomous surface vessels (ASVs) managing deep-water conveyor harvesting where toxicity levels are too hostile for human workers.

---

## 🛠️ Repository Architecture

This repository hosts the core logic, firmware, and telemetry pipelines for the Darya Genie ecosystem.

```text
├── hardware/               # UGV chassis CAD files, wiring schematics, and BOM
├── firmware/               # Microcontroller code for motor drivers and LED matrix faces
├── src/
│   ├── genie_brain/        # ROS 2 nodes for navigation, obstacle avoidance, and computer vision
│   ├── voice_engine/       # Audio playback triggers for Urdu and Sindhi localization
│   └── payment_gateway/    # Webhook listeners for mobile wallet micro-transaction processing
├── docs/                   # Educational curriculum and community deployment handbooks
└── tests/                  # Hardware-in-the-loop (HIL) simulation scripts