feat: implement satellite imagery detection pipeline for riverine waste (issue #3)

Add a complete ML/CV detection pipeline for identifying pollution and waste
in waterways using satellite imagery, aligning with the technical roadmap
outlined in issue #3.

## Contributor Workflow (1.a-c)

- Add venv setup instructions, disk space management (5-11GB estimate),
  and cloud alternatives (Google Colab ~15GB, Kaggle Kernels ~30GB)
  to CONTRIBUTING.md with --no-cache-dir pip guidance.
- Document PR workflow from feature branches with main-dev integration
  and promotion path to main (Gemini Features -> main-dev -> main).
- Add security audit commands (pip-audit, bandit) and pre-PR checklist.

## Detection Methodologies (2.a.i - Direct Object Detection)

- Enhance tile_satellite_image.py with overlap support, variable tile
  sizing (min_dimension guard), label extraction via GeoJSON intersection,
  and comprehensive stats tracking.
- Add train_yolo.py with configurable YOLOv8 training pipeline supporting
  both pretrained and from-scratch modes, plus evaluation post-training.
- Implement mask_rcnn_pipeline.py for instance segmentation with
  Mask R-CNN (ResNet50 FPN V2 backbone), SGD optimizer, StepLR scheduler,
  and checkpoint persistence.
- Add detectron2_setup.py with automatic CUDA/torch version detection
  and pip-based detectron2 wheel installation from Meta's fbaipublicfiles CDN.

## Spectral Analysis (2.a.ii)

- Create spectral_analysis.py with NDVI, NDWI, AWI, and NDBI computation
  from multispectral/Sentinel-2 imagery.
- Add river_health_assessment() for integrated river condition scoring
  based on vegetation and water indices.
- Support S2L1C and S2L2A sensor types with configurable band indices.
- Optional output to GeoTIFF per index.

## Data & Tooling (2.b)

- Update pyproject.toml with detection optional dependency group:
  torch, torchvision, ultralytics, dask-geopandas, geopandas, shapely,
  rasterio, numpy.
- Update src/api/requirements.txt with all detect dependencies.

## Model Implementation Workflow (2.c)

- Create riverine_waste.yaml with 8 riverine waste classes:
  plastic_bottles, plastic_bags, floating_debris, accumulated_waste,
  tires, construction_waste, metal_scrap, organic_waste.
- Create data directory structure:
  data/images/train/, data/images/val/, data/images/test/
  data/labels/train/, data/labels/val/, data/labels/test/
- Create detection module __init__.py exposing tile_image, spectral
  analysis functions, and RiverineAerialWasteIngestor.

## First Step - AerialWaste Riverine Pipeline (2.d)

- Create data_ingestion/riverine_ingest.py implementing RiverineAerialWasteIngestor
  class with:
  - fetch_metadata() supporting local JSON or remote Zenodo download
  - load_riverine_boundaries() for GeoJSON river boundary overlays
  - is_riverine_location() with buffer-based spatial filtering
  - compute_riverine_score() combining water proximity, waste type
    relevance, and area type classification
  - filter_riverine_subset() sorting by score with source preference
  - tile_and_convert_annotations() for rasterio-based tiling with
    YOLO-format label generation
  - ingest() orchestrating full pipeline with train/val/test splits
    (70/15/15)

## Note

The Google share link (https://share.google/aimode/UbOT272aCmDSQSeH) in
the original issue body is no longer reachable and could not be recovered.

Co-authored-by: opencode zen <ling-3.0-flash-free>