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
    * *Action:* I have been told that a good repo to begin with is via the fine-tuning via [AerialWaste dataset](https://github.com/nahitorres/AerialWaste).
* **Spectral Analysis:** Discriminate waste via NDWI and multi-band ratios using Sentinel-2 data.

#### 2. Recommended Data & Tooling
* **Frameworks:** `PyTorch` is required for training.
* **Geospatial Pipeline:** Utilize `GDAL` or `Rasterio` for image handling.
* **Orchestration:** `dask-geopandas` for parallel processing.

#### 3. First Step
Let us start with a research spike: **identify the best subset of the AerialWaste dataset for riverine contexts and propose a data ingestion pipeline using `rasterio`.**

Let me know if this technical direction aligns with your experience, or if you'd like to adjust the model/library choices!
