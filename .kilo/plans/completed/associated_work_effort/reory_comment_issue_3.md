Hi @reory, thanks for reaching out! We would love to have your help on this epic. 

To turn Issue #3 into actionable tasks, we have synthesized the research approach for satellite-based waste detection:

### Technical Roadmap for Satellite Pollution Detection

1. **Detection Methodologies:**
    * **Direct Object Detection:** Implement instance segmentation (e.g., Mask R-CNN) on high-resolution imagery to identify outlines/textures of waste piles.
    * **Spectral Analysis:** Utilize multispectral sensors to detect unique reflectance 'fingerprints' of plastics versus sand/organic matter.
    * **Indirect Tracing:** Analyze vegetation health indices and Land Surface Temperature (LST) fluctuations to pinpoint illegal dumping areas.

2. **Recommended Data & Tooling:**
    * **Sources:** Utilize Sentinel-2 (ESA) for high-frequency optical data or commercial VHR data (Planet/Maxar) where available.
    * **Datasets:** Explore the 'AerialWaste' dataset or 'Four-Band Solid Waste Dataset (FBSWD)' for model training.

### How to Contribute
* **Branching:** Please target all work to our 'main-dev' branch.
* **Security:** All code must pass our local security audit (pip-audit for dependencies, bandit for SAST). See our README.md for instructions.
* **First Step:** Let us start with a research spike—identify the best open-source dataset for training a model on riverine waste detection.

Let me know if this scope works for you!