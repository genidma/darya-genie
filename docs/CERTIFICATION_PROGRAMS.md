# Darya Genie Certification Programs 🎓🏅

**Version:** 1.0 (Draft)
**Parent Epic:** [#12 — Education & Community Outreach](https://github.com/genidma/darya-genie/issues/12)
**Tracking Issue:** [#13 — Develop Certification Programs](https://github.com/genidma/darya-genie/issues/13)

This document defines the credentialing framework that turns Darya Genie's safety-first culture into a portable, community-owned career ladder. It is written against the three-part framework set out in epic [#12](https://github.com/genidma/darya-genie/issues/12).

---

## 1. The Problem

Grassroots river restoration fails for the same three reasons almost everywhere:

1. **Safety is assumed, not proven.** Volunteers and collectors are asked to work near toxic sludge, unstable banks, and monsoon flood zones without verifiable training. When an incident happens, the whole initiative loses its social licence.
2. **There is no ladder.** Cleanup work is treated as casual, unskilled labour. There is no recognised way to advance from "picking up waste" to "leading a restoration sector," so the most capable community members leave for better-paid work.
3. **Credentials don't travel.** Training delivered verbally or in a one-off workshop cannot be audited, reimbursed by funders, or transferred to a neighbouring basin or a future employer.

Institutional programmes try to solve this with expensive, centralised certification that never reaches the people actually near the water.

## 2. The Solution — and Who It's For

**Darya Genie Certification Programs** are a set of open-source, version-controlled credentialing tracks that gate participation on proven safety competence and then reward advancement with higher pay and greater responsibility.

The tracks are for:

| Audience | Entry Track | What certification unlocks |
|----------|-------------|----------------------------|
| **Community Collectors** — residents who collect fine-detail waste in narrow banks and alleys unreachable by the UGV | Certified Collector | Eligibility for micro-incentive payouts via `payment_gateway` |
| **Field Technicians** — UGV operators, decontamination and maintenance crew | Certified Collector → Field Technician | Shift assignment, equipment custody, hazard-pay tiers |
| **Drone Operators** — aerial reconnaissance and ground-truthing pilots | Aerial Operator | Solo flight authority under the CAA flight zone, scout-data custody |
| **Restorationists** — mangrove planters and site stewards | Restoration Lead | Per-sapling restoration credits, site ownership |
| **Leads** — those ready to train and coordinate others | Master Steward / Operational Lead | Trainer role, priority assignment, higher per-unit bonuses |

Every track maps onto the "Upward Mobility & Executive Training" budget line in the [README](/README.md) — certification *is* the fast-track leadership pipeline.

### The Certification Tracks

| Tier | Prerequisites | Assessment | Benefits |
|------|---------------|------------|----------|
| **Certified Collector** | None — open entry | [Darya Safety-First Certification Course](/docs/safety/) (45 min, 3 modules) + [Assessment Quiz](/docs/safety/assessment_quiz.md), 80% pass | Base micro-payouts, drop-hub access |
| **Field Technician** | Certified Collector + 10 verified shifts | Practical equipment-handling evaluation | Hazard-pay tier, UGV operation, equipment custody |
| **Aerial Operator** | Certified Collector + CAA Remote Pilot License (RPL) + Class 2 Medical | CAA licensing + internal pre-flight evaluation | Solo flight authority, scout-data custody (see [Drone Protocols](/docs/DRONE_UGV_COORDINATION_PROTOCOL.md)) |
| **Restoration Lead** | Certified Collector + [Mangrove Restoration module](/docs/safety/mangrove_propagation.md) + 25 successful plantings at 80%+ survival | Drone-verified growth audit | PKR 100/sapling bonus, priority assignment |
| **Master Steward** | Restoration Lead + 100 successful plantings at 90%+ survival | Peer review + trainer shadowing | Lead trainer role, PKR 150/sapling bonus |

> Advancement is never purely time-based. Every step requires **documented, system-verified evidence** — flight hours, shift logs, or drone-verified survival metrics.

## 3. The Secret Ingredient

The secret ingredient is that **the curriculum is version-controlled and auditable, and the credential is enforced by open-source code rather than by a certificate on a wall.**

This gives the programme a property that traditional NGO training lacks: *the claim "this person is certified" can be independently verified by anyone, at any time, from the repository itself.*

### How It Works

```
README.md → /docs/safety/ → docs/CERTIFICATION_PROGRAMS.md
                                   │
                                   ▼
              /scripts/certification_gatekeeper.py   (validates the quiz)
                                   │
                                   ▼
                     POST /api/certify → /src/api/auth.py
                                   │
                                   ▼
                          User.is_certified = True
                                   │
                                   ▼
                 payment_gateway releases micro-incentive payouts
```

1. **Version-controlled curriculum.** Each safety module and the assessment quiz live in Git alongside the code they govern. Changing a hazard threshold or an answer key produces a reviewable, dated commit — the training material and the audit trail are the *same artefact*.
2. **Code-enforced gatekeeping.** [`certification_gatekeeper.py`](/scripts/certification_gatekeeper.py) validates the quiz against the answer key and issues a SHA-256 certification token. There is no manual step where certification can be granted as a favour.
3. **Fail-closed payouts.** [`/src/api/auth.py`](/src/api/auth.py) refuses any micro-incentive payout unless `User.is_certified == True`. Safety is not a suggestion bolted onto the pipeline — it is a hard dependency of getting paid.
4. **Continuous re-assessment.** Higher tiers are not one-time passes. `certification_gatekeeper.py` re-assesses Restoration Lead status against drone-verified growth audits, so a credential can be *earned back* by outcomes, not tenure.

### Why This Matters for the Community

- **Forkable:** Any community that forks this repository inherits a working certification programme, not a blank page.
- **Fundable:** Funders and CAA regulators can audit the exact training a collector received — version, date, and pass score included.
- **Portable:** A collector's certification token is a verifiable record of competence that travels with them to another basin, sector, or employer.

---

## Related Documents

- [Safety & Certification Pipeline](/README.md#safety--certification-pipeline) — README overview
- [Safety-First Certification Course](/docs/safety/) — the 45-minute curriculum
- [Mangrove Restoration & Stewardship](/docs/safety/mangrove_propagation.md) — Restoration Lead track
- [Drone/UGV Coordination Protocol](/docs/DRONE_UGV_COORDINATION_PROTOCOL.md) — Aerial Operator prerequisites
- [Educational Curriculum](/docs/CURRICULUM.md) — broader education & outreach materials (epic #12)

---

## Contributing

Notable contributions to this programme become a permanent record in the [README's Notable Contributions](/README.md#-credits-and-notable-contributions) table. See [CONTRIBUTING.md](/CONTRIBUTING.md) to get started.
