# Darya Genie (دريا جني) 🌊🤖

> **Grassroots, community-funded robotic river restoration for the Lyari Basin, Karachi.**

Darya Genie is an open-source, decentralized civic-tech initiative designed to bypass institutional gridlock and clean up urban waterways. By combining low-cost autonomous waste-harvesting hardware with a culturally resonant, interactive mascot and a micro-equity donation loop, we shift the environmental narrative from "the state's problem" to a community-owned triumph.

## Repository Structure

This repository is organized as follows:

```
├── hardware/               # UGV chassis CAD files, wiring schematics, and BOM
├── firmware/               # Microcontroller code for motor drivers and LED matrix faces
│   └── motor_controller/   # PlatformIO project for ESP32 with micro-ROS
├── src/
│   ├── genie_brain/        # ROS 2 package for the robot's brain (navigation, vision, etc.)
│   └── payment_gateway/    # FastAPI server for processing mobile wallet webhooks
├── docs/                   # Educational curriculum and community deployment handbooks
└── tests/                  # Hardware-in-the-loop (HIL) simulation scripts
```

## 💰 Financial Transparency & Worker Welfare (Year 01 Only)

Traditional top-down river restoration initiatives for the Lyari Basin carry massive, gridlocked budgets (such as the S-III plan's **~$150M CAD / PKR 43B** allocation), which frequently suffer from bureaucratic friction and low deployment execution. 

Darya Genie completely flips this paradigm. We treat **Worker Welfare as our Alcoa Keystone Habit**—inspired by Charles Duhigg’s *The Power of Habit*. We believe that by fiercely protecting, properly feeding, and aggressively investing in our frontline team, we automatically secure operational safety, technical discipline, and unshakeable community trust. 

Our expanded **Year 01 Pilot Target is $250,000 CAD**, built explicitly to eliminate hand-to-mouth precarity and design a high-mobility leadership pipeline:

| Phase / Budget Category | Year 01 Allocation (CAD) | Cornerstone Utility & Worker Welfare Impact |
| :--- | :--- | :--- |
| **Premium Living Wages** | $110,000 | Defeats hand-to-mouth financial precarity. Provides highly competitive, dignified salaries for field operators and technicians, anchoring long-term retention. |
| **Upward Mobility & Executive Training** | $40,000 | Structured 2-to-3 year fast-track program. Earmarked funds for leadership workshops, technical robotics upskilling, and management training to transition field workers into Directors. |
| **Holistic Support, Meals & Office Care** | $35,000 | Daily high-nutrition catered meals, comprehensive field health checks, high-grade personal protective equipment (PPE), and modern, air-conditioned office workspaces. |
| **Core Hardware & Autonomy** | $50,000 | Rugged tracked UGV chassis, Jetson/Raspberry Pi compute blocks, conveyor mechanics, sealed sensor suites, and local W-11 truck art styling. |
| **Micro-Incentive Seeding** | $15,000 | Initial liquidity to back local community collection drop-hubs for immediate wallet payouts. |

*Every 5-rupee micro-donation processed by the gateway flows directly into sustaining local incentive liquidity, protecting team welfare, and supporting hardware maintenance.*

## Credits

- [Kilo](https://github.com/Kilo-Org/kilocode) for helping update the README.
- [Gemini by Google](https://gemini.google.com/) as the original brainstorming partner.
- [@genidma](https://github.com/genidma) for the origination of the idea.
- [Qoder](https://qoder.com/) (formerly Lingma) for helping link the image to the README.