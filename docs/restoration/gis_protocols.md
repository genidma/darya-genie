# GIS & Satellite Suitability Protocol

**Version:** 1.0  
**Effective Date:** 2026-06-03  
**Classification:** Technical Infrastructure Protocol  

---

## 1. Data Acquisition

### 1.1 Satellite Source
- **Primary:** Sentinel-2 MSI (MultiSpectral Instrument) L2A products via Copernicus Open Access Hub
- **Resolution:** 10m multispectral bands (B2, B3, B4, B8) for vegetation/water indices
- **Reprocessing:** Cloud-optimized GeoTIFFs with atmospheric correction applied

### 1.2 Acquisition Frequency
- **Baseline:** Bi-weekly imagery snapshots to monitor riverbed shifts and sediment accumulation
- **Trigger-based:** Additional passes during monsoon season or major weather events
- **Archive:** Minimum 12 months of historical imagery retained for trend analysis

---

## 2. The "Suitability Filtering" Logic

Three automated masks applied to all satellite imagery to identify viable planting zones:

### 2.1 Velocity Mask
- **Data Source:** HEC-RAS hydraulic modeling integrated with Sentinel-2 water index
- **Threshold:** Flow velocity < 0.3 m/s for primary zones, 0.3-0.5 m/s for conditional zones
- **Exclusion:** Areas exceeding 0.5 m/s marked as "HIGH_RISK" and removed from candidate pool

### 2.2 Elevation Mask
- **Method:** SRTM-30m DEM fused with tidal gauge data from nearby Karachi port
- **Optimal Zone:** Areas between Mean High Water (MHW) and Mean Low Water (MLW)
- **Elevation Range:** 0.5m to 2.0m above chart datum (verified via drone altimeter)
- **Filter:** Automatic exclusion of permanently submerged (>2.0m) or exposed (>2.0m above MHW) areas

### 2.3 Buffer Mask
- **Avian Nesting:** 50m exclusion buffer around identified nesting sites (updated monthly from ornithology surveys)
- **UGV Transit:** 10m buffer around planned UGV routes from `/genie/navigation/target`
- **Drone Corridors:** 20m vertical buffer around active drone survey paths
- **Cultural Sites:** Community-identified zones excluded based on guardian feedback

---

## 3. Feedback Loop

### 3.1 Ground Verification
```
GIS_Suitable_Site → Drone_Swarm_Survey → Site_Status = "VERIFIED"
```
- Every site identified as suitable via GIS must undergo drone verification
- Multispectral drone pass confirms soil moisture and absence of surface debris
- Coordinates logged to `User_Registry.sites.ready_for_planting`

### 3.2 Failure Analysis
- **Failure Trigger:** Drone survey reports sapling mortality >20% within 90 days
- **Flagging:** Coordinates marked with `site_failure: true` in database
- **Model Retraining:** Failed sites added to negative training set for next suitability cycle
- **Root Cause:** Investigation determines if masking parameters need adjustment

### 3.3 Continuous Improvement
- Weekly accuracy reports generated comparing predicted vs actual survival rates
- Masking thresholds adjusted quarterly based on field performance
- Community guardian input incorporated for exclusion zone updates

---

## Worker Welfare Integration

This protocol supports our **Alcoa Keystone Habit** by:
- Reducing wasted effort on unsuitable sites through predictive intelligence
- Creating technical roles in GIS analysis and drone survey operations
- Ensuring Restoration Leads have highest probability of successful outcomes