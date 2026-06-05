Hi @reory, thanks for reaching out! Would love to have your help on this epic. 

Secondly, there may be a fair bit of work involved and I am consulting primarily with an intelligence agnostic of a substrate (otherwise, generally referred to as an AI). I share this with you in terms of a. transparency b. part of that is that I don't know anything about GIS myself or not a lot. and c. most importantly, seeing that there is a fair bit of work involved, I don't want you or anyone helping out to get overwhelmed. specially considering that you are here to help and volunteer. and I really appreciate that!

So please don't feel obligate or overwhelmed. Feel free to carve out sections from below and completely go at your pace. I don't have a particular deadline for this project. Although it would be great to get our rivers and lakes cleaned up sooner than later and not have the pollution go in there in the first place (and within reason)

With these crucial notes and focusing our our well-being. 

I think a first good point to get started with is, via the [README.md](https://github.com/genidma/darya-genie/). Seeing that you are here, this is something that you have probably done. If not, it's a good idea to do so, in order to get familiar with the original proposition. 

Here are the details specific to this PR and associated PRs that may come out of issue #3 here:

### 1. Contributor Workflow
1.a. [ ] **Environment Setup:** Before installing dependencies, please create a virtual environment to isolate your workspace:
   * `python -m venv venv`
   * `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
   > [!IMPORTANT]
   > **Disk Space Management:** The dependencies for this project are significant. Anticipate needing 5-11GB total (Environment, Datasets, Tiled Images, Model Checkpoints).
   > * **Why use `--no-cache-dir`?** Normally, `pip` saves downloaded installer files in a local cache. Adding this flag tells `pip` to download, install, and immediately discard those files, saving crucial disk space.
   > * **Cloud Alternatives (Free Tier):** If you lack local space, use these cloud environments:
   >    * **Google Colab:** ~15GB ephemeral storage. *Tip:* Mount Google Drive to persist data and model checkpoints.
   >    * **Kaggle Kernels:** ~30GB scratch space. *Tip:* Use the "Datasets" feature to persist your training data between sessions.
   >    * **General Tip:** Always offload training and heavy data processing to these environments. Use your local machine only for code editing and lightweight tasks.

1.b. [ ] **Development:** Please create PRs from your feature branches. Our team will handle merging them into the appropriate development (`main-dev`) or production (`main`) pipelines.
   * To keep your branch up-to-date with our latest changes, please periodically pull from `main-dev`:
     * Fetch: `git fetch origin`
     * Merge: `git merge origin/main-dev`
1.c. [ ] **Security:** Pass local security audits:
   * Install: `pip install --no-cache-dir pip-audit bandit`
   * Dependency Audit: `pip-audit -r src/api/requirements.txt`
   * SAST Audit: `bandit -r src/api/`

### 2. Technical Roadmap (Issue #3)

2.a. [ ] **Detection Methodologies & Implementation**
   2.a.i. [ ] Direct Object Detection (YOLOv8 or Mask R-CNN)
      * Use tiling script: `src/genie_brain/detection/tile_satellite_image.py`
      * Dataset: [AerialWaste dataset](https://github.com/nahitorres/AerialWaste)
   2.a.ii. [ ] Spectral Analysis (NDWI/multi-band ratios using [Sentinel-2 data](https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2))

2.b. [ ] **Recommended Data & Tooling**
   2.b.i. [ ] Frameworks: `PyTorch` (compatible with CUDA environment: `pip install torch torchvision`)
   2.b.ii. [ ] Geospatial Pipeline: `GDAL` or `Rasterio`
   2.b.iii. [ ] Orchestration: `dask-geopandas` for parallel processing

2.c. [ ] **Model Implementation Workflow**
   2.c.i. [ ] Architecture Selection (YOLOv8 vs Mask R-CNN)
   2.c.ii. [ ] Data Preparation (Structure: `/data/images/train/`, `/data/labels/train/`, etc.)
   2.c.iii. [ ] Data Configuration: Create `riverine_waste.yaml` (format: `class_id x_center y_center width height`)
   2.c.iv. [ ] Training Script: Use YOLOv8 example
      ```python
      from ultralytics import YOLO
      model = YOLO('yolov8n.pt') 
      model.train(data='riverine_waste.yaml', epochs=50, imgsz=640)
      ```
      > [!IMPORTANT]
      > **GPU Highly Recommended:** Training on a CPU is impractical. If you lack a local NVIDIA GPU, use these free-tier cloud environments:
      > * **Google Colab:** Set `Runtime` -> `Change runtime type` to `T4 GPU`.
      > * **Kaggle Kernels:** Enable `GPU T4 x2` in the accelerator settings.

   2.c.v. [ ] Environment Setup:
      ```bash
      # For YOLOv8
      pip install --no-cache-dir ultralytics
      # For Mask R-CNN
      pip install --no-cache-dir detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
      ```
      > [!NOTE]
      > `fbaipublicfiles.com` is a domain owned by Meta. It is a legitimate and trusted source for hosting assets related to their open-source AI projects (like `detectron2`). https://www.whois.com/whois/fbaipublicfiles.com

2.d. [ ] **First Step:** Identify the best subset of the AerialWaste dataset for riverine contexts and propose a data ingestion pipeline using `rasterio`.
