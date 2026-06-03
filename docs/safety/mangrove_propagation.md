# Module: Mangrove Restoration & Stewardship 🌿

**Duration:** Part of "Restoration Lead" tier certification  
**Prerequisites:** Completion of Safety Modules 1-3 and passing certification assessment

---

## 1. Site Selection Intelligence (The "Suitability Map")

Before planting, all candidates must consult the Darya GIS Suitability Layer (accessible via the collector portal). This layer uses satellite imagery to identify sites based on:

### Tidal Elevation
Planting is strictly prohibited outside the "optimal intertidal window" to prevent drowning or dehydration.

| Elevation Zone | Planting Status | Rationale |
|----------------|-----------------|-----------|
| Above MHW* | PROHIBITED | Risk of dehydration, salinity stress |
| Optimal Intertidal (MHW to MLW) | APPROVED | Ideal for mangrove sapling establishment |
| Below MLW | PROHIBITED | Risk of submersion stress |

*Mean High Water to Mean Low Water

### Flow Velocity Filtering
Satellite data identifies "low-energy zones" where sediment is stable and sapling wash-out risk is below 5%.

- **High-Energy Zones** (>0.5 m/s): Prohibited - saplings will be washed away
- **Low-Energy Zones** (<0.3 m/s): Preferred - suitable for planting
- **Optimal Zones** (0.3-0.5 m/s): Conditional approval based on monsoon timing

### Ecological Exclusion Zones
The GIS layer automatically masks out:

- Active avian nesting sites (seasonal buffers applied)
- Protected micro-habitats (fish spawning areas, crab breeding grounds)
- Cultural heritage areas (marked by community custodians)

---

## 2. The Verification Workflow (Ground-Truthing)

Satellite data is a guide, not a guarantee. Every planting site must undergo the "Drone-Eye Verification" process:

### Survey Phase
1. Collector identifies candidate site via GIS portal
2. Darya drone performs low-altitude multispectral pass (10-15m AGL)
3. Camera captures: soil moisture, surface debris, tidal markers

### Validation Phase
- Drone logs GPS coordinates to `User_Registry.sites` collection
- System cross-references with suitability map
- Status updated to "Ready for Planting" if all criteria met

### Action Phase
Only sites marked "Ready" are cleared for sapling installation. Collector receives SMS confirmation with optimal planting window.

---

## 3. Propagation & Stewardship Protocols

### Installation Standards
- **Sapling Selection:** Only nursery-propagated seedlings with >80% survival rate used
- **Anchoring:** Biodegradable pins secured at 45° angle, 15cm depth
- **Spacing:** Minimum 2m between saplings for canopy development
- **Depth:** Planting depth maintained at 2cm above sediment line

### Reporting Requirements
After planting:
1. Collector scans geo-tag with mobile device
2. `payment_gateway` triggers "Restoration Credit" (PKR 100 per verified sapling)
3. Photo documentation uploaded showing installed sapling

### Maintenance Obligations
- **Growth Audits:** Bi-weekly drone surveys for site health
- **Failure Detection:** If mortality >20%, site flagged for re-evaluation
- **Status Review:** `certification_gatekeeper.py` re-assesses Restoration Lead status for underperforming sectors

---

## Integration with certification_gatekeeper.py

```python
def update_restoration_status(user_id, site_id, success_metric):
    """Update user status based on mangrove stewardship performance."""
    # Validates drone-survey data against site_id
    if drone_validation_service.verify_site(site_id):
        # Check growth audit results
        if success_metric > 0.8:  # 80% survival threshold
            db.users.update_one(
                {"user_id": user_id},
                {"$set": {"is_restoration_lead": True}}
            )
            return "Status Updated: Restoration Lead Authorized"
        else:
            # Schedule review session
            schedule_consultation(user_id)
            return "Status Update Pending: Growth Audit Required"
    return "Validation Failed: Site Not Approved"
```

---

## Restoration Lead Certification Pathway

| Level | Requirements | Benefits |
|-------|--------------|----------|
| Collector | Safety certification complete | Base micro-payouts |
| Restoration Lead | 25+ successful plantings, 80%+ survival rate | PKR 100/sapling bonus, priority assignment |
| Master Steward | 100+ successful plantings, 90%+ survival rate | Lead trainer role, PKR 150/sapling bonus |

---

## Worker Welfare Note

This module supports our **Alcoa Keystone Habit** by:
- Creating career advancement pathways within the cleanup ecosystem
- Ensuring fair compensation for skilled restoration work
- Maintaining community ownership of environmental outcomes