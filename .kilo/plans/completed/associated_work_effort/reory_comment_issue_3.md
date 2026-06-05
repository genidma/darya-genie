Hi @reory, thanks for reaching out! We would love to have your help on this epic. 

To turn Issue #3 into actionable tasks, we have developed a more granular technical roadmap for satellite-based waste detection:

### 🛰️ Technical Roadmap for Satellite Pollution Detection

#### 1. Detection Methodologies & Implementation
* **Direct Object Detection (Primary Focus):**
    * **Objective:** Identify unauthorized landfills and large waste blockages in riverbanks.
    * **Architecture:** Utilize **YOLOv8** or **Mask R-CNN** via the `ultralytics` or `detectron2` libraries. These are better suited for fast, high-resolution processing than legacy models.
    * **Action:** Begin by fine-tuning on the [AerialWaste dataset](https://github.com/nahitorres/AerialWaste) or similar overhead datasets to establish a baseline model.
    * **Preprocessing:** Implement tiling of high-res satellite imagery to manage memory constraints for model inference.

* **Spectral Analysis (Advanced):**
    * **Objective:** Discriminate between waste materials (plastics/tires) and environmental debris.
    * **Action:** If using Sentinel-2 (multispectral), calculate **NDWI** (Normalized Difference Water Index) to isolate water bodies, then analyze multi-band ratios for non-organic spectral signatures in adjacent bank zones.

#### 2. Recommended Data & Tooling
* **Frameworks:** `PyTorch` is required for model training. 
* **Geospatial Pipeline:** Utilize `GDAL` or `Rasterio` for handling satellite imagery formats (GeoTIFF, JP2) and geospatial transformations.
* **Orchestration:** Use `dask-geopandas` to handle parallel processing of large satellite tiles.

#### 3. How to Contribute
* **Branching:** Please target all work to our `main-dev` branch.
* **Security:** All code must pass our local security audit (`pip-audit` for dependencies, `bandit` for SAST). See our README.md for instructions.
* **First Step:** Conduct a research spike to identify the best subset of the AerialWaste dataset for riverine contexts, and propose a data ingestion pipeline using `rasterio`.

Let me know if this technical direction aligns with your experience, or if you'd like to adjust the model/library choices!