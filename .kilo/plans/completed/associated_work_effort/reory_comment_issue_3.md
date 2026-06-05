Hi @reory, thanks for reaching out! We would love to have your help on this epic. 

To get started, please take a moment to review our [README.md](https://github.com/genidma/darya-genie/) to understand our project standards.

### 🔄 Contributor Workflow
1. **Development:** Please target all new feature PRs to our `main-dev` branch.
2. **Security:** All code must pass our local security audit (`pip-audit` for dependencies, `bandit` for SAST) as documented in our README.

### 🛰️ Technical Roadmap (Issue #3)
We have developed a granular roadmap for satellite-based waste detection:

#### 1. Detection Methodologies & Implementation
* **Direct Object Detection:** Identify unauthorized landfills/blockages. 
    * *Architecture:* Utilize YOLOv8 or Mask R-CNN.
    * *Action:* Begin fine-tuning on the [AerialWaste dataset](https://github.com/nahitorres/AerialWaste).
* **Spectral Analysis:** Discriminate waste via NDWI and multi-band ratios using Sentinel-2 data.

#### 2. Recommended Data & Tooling
* **Frameworks:** `PyTorch` is required for training.
* **Geospatial Pipeline:** Utilize `GDAL` or `Rasterio` for image handling.
* **Orchestration:** `dask-geopandas` for parallel processing.

#### 3. First Step
Let us start with a research spike: **identify the best subset of the AerialWaste dataset for riverine contexts and propose a data ingestion pipeline using `rasterio`.**

Let me know if this technical direction aligns with your experience, or if you'd like to adjust the model/library choices!