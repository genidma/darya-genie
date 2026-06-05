Hi @reory, thanks for reaching out! Would love to have your help on this epic. 

Secondly, there may be a fair bit of work involved and I am consulting primarily with an intelligence agnostic of a substrate (otherwise, generally referred to as an AI). I share this with you in terms of a. transparency b. part of that is that I don't know anything about GIS myself or not a lot. and c. most importantly, seeing that there is a fair bit of work involved, I don't want you or anyone helping out to get overwhelmed. specially considering that you are here to help and volunteer. and I really appreciate that!

So please don't feel obligate or overwhelmed. Feel free to carve out sections from below and completely go at your pace. I don't have a particular deadline for this project. Although it would be great to get our rivers and lakes cleaned up sooner than later and not have the pollution go in there in the first place (and within reason)

With these crucial notes and focusing our our well-being. 

I think a first good point to get started with is, via the [README.md](https://github.com/genidma/darya-genie/). Seeing that you are here, this is something that you have probably done. If not, it's a good idea to do so, in order to get familiar with the original proposition. 

Here are the details specific to this PR and associated PRs that may come out of issue #3 here:

### 🔄 Contributor Workflow
1. **Development:** Feel free to target all new feature PRs to the `main-dev` branch as a redirection. 
   * To synchronize a feature branch (PR) with `main-dev`, please follow these steps:
     * **Fetch:** Update local repository with latest remote changes (`git fetch origin`).
     * **Checkout:** Switch to the feature branch (`git checkout <branch-name>`).
     * **Merge/Rebase:** Integrate `main-dev` into the feature branch (`git merge origin/main-dev` or `git rebase origin/main-dev`).
     * **Resolve:** Fix any merge conflicts, if they occur.
     * **Push:** Update the remote PR branch (`git push origin <branch-name>`).
2. **Security:** It would be great if you can install and run the following security audits. All code must pass these checks as documented in our README:
   * To install the tools, run: `pip install pip-audit bandit`
   * To audit dependencies, run: `pip-audit -r src/api/requirements.txt`
   * To perform static analysis (SAST), run: `bandit -r src/api/`

### 🛰️ Technical Roadmap (Issue #3)
A proposed granular roadmap for satellite-based waste detection:

#### 1. Detection Methodologies & Implementation
* **Direct Object Detection:** Identify unauthorized landfills/blockages. 
    * *Architecture:* Utilize YOLOv8 or Mask R-CNN.
    * *Script:* A tiling script is available at `src/genie_brain/detection/tile_satellite_image.py` to prepare high-resolution images for detection.
    * *Action:* I have been told that a good repo to begin with is via the fine-tuning via [AerialWaste dataset](https://github.com/nahitorres/AerialWaste).
* **Spectral Analysis:** Discriminate waste via NDWI and multi-band ratios using Sentinel-2 data.

#### 2. Recommended Data & Tooling
* **Frameworks:** `PyTorch` is required for training.
* **Geospatial Pipeline:** Utilize `GDAL` or `Rasterio` for image handling.
* **Orchestration:** `dask-geopandas` for parallel processing.


#### 4. Model Implementation Workflow
1. **Architecture Selection:**
   * **YOLOv8 (`ultralytics`):** Best for real-time inference and rapid iteration.
   * **Mask R-CNN (`detectron2`):** Best if pixel-perfect instance segmentation is required.

2. **Data Preparation (Required Directory Structure):**
   Before training, your data *must* follow this structure:
   ```
   /data/
     /images/train/ (raw .jpg or .png images)
     /images/val/
     /labels/train/ (YOLO .txt files)
     /labels/val/
   ```

3. **Data Configuration (YOLO):**
   Create a `riverine_waste.yaml` file in your root project directory:
   ```yaml
   # Path to your dataset root
   path: /path/to/data/
   train: images/train
   val: images/val
   
   # Class names
   names:
     0: riverine_waste
   ```
   * **Label Formatting:** Each `.txt` file in `labels/` must contain lines matching the format: `class_id x_center y_center width height`.
     * *Example:* `0 0.5 0.5 0.2 0.2` (Class 0 at the center with 20% width/height).

4. **Training Script (YOLOv8 Example):**
   Ensure `riverine_waste.yaml` is in the same directory as this script.
   ```python
   from ultralytics import YOLO

   # 1. Load a pre-trained YOLOv8 model (n=nano, s=small, m=medium, l=large)
   model = YOLO('yolov8n.pt') 

   # 2. Train using your configuration file
   model.train(data='riverine_waste.yaml', epochs=50, imgsz=640)
   ```

5. **Environment Setup:**
   ```bash
   # For YOLOv8
   pip install ultralytics
   # For Mask R-CNN
   pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
   ```
   > [!NOTE]
   > `fbaipublicfiles.com` is a domain owned by Meta. It is a legitimate and trusted source for hosting assets related to their open-source AI projects (like `detectron2`). https://www.whois.com/whois/fbaipublicfiles.com
