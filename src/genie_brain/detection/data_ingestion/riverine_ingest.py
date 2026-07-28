"""
Data ingestion pipeline for the AerialWaste dataset, filtered for riverine contexts.
Proposes a rasterio-based pipeline to prepare satellite imagery for waste detection training.

Reference: AerialWaste dataset (Torres & Fraternali, 2023)
https://github.com/nahitorres/AerialWaste
https://zenodo.org/records/12162383
"""

import os
import json
import requests
from pathlib import Path
from typing import Optional

import rasterio
from rasterio.windows import Window
from rasterio.transform import from_bounds
import geopandas as gpd
from shapely.geometry import box


AERIALWASTE_META_URL = (
    "https://zenodo.org/records/12162383/files/aerialwaste_metadata.json"
)
AERIALWASTE_ZENODO_URL = "https://zenodo.org/records/12162383"

RIVERINE_WASTE_CLASSES = [
    "plastic_bottles",
    "plastic_bags",
    "floating_debris",
    "accumulated_waste",
    "tires",
    "construction_waste",
    "metal_scrap",
    "organic_waste",
]

AGEA_ORDER = "agea_ortophotos"
WV3_ORDER = "worldview3"
GE_ORDER = "google_earth"


class RiverineAerialWasteIngestor:
    """
    Ingest and filter the AerialWaste dataset for riverine waste detection.
    """

    def __init__(
        self,
        root_dir: str,
        output_dir: str,
        tile_size: int = 640,
        overlap: float = 0.1,
    ):
        self.root_dir = Path(root_dir)
        self.output_dir = Path(output_dir)
        self.tile_size = tile_size
        self.overlap = overlap
        self.riverine_masks: Optional[gpd.GeoDataFrame] = None

        (self.output_dir / "images" / "train").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "images" / "val").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "images" / "test").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "labels" / "train").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "labels" / "val").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "labels" / "test").mkdir(parents=True, exist_ok=True)

    def fetch_metadata(self, local_path: Optional[str] = None) -> dict:
        if local_path and os.path.exists(local_path):
            with open(local_path, "r") as f:
                return json.load(f)

        resp = requests.get(AERIALWASTE_META_URL, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def load_riverine_boundaries(self, geojson_path: str) -> gpd.GeoDataFrame:
        self.riverine_masks = gpd.read_file(geojson_path)
        if self.riverine_masks.crs is None:
            self.riverine_masks = self.riverine_masks.set_crs("EPSG:4326")
        return self.riverine_masks

    def is_riverine_location(
        self, lat: float, lon: float, buffer_meters: float = 500.0
    ) -> bool:
        if self.riverine_masks is None:
            return True
        point = gpd.points_from_xy([lon], [lat], crs="EPSG:4326").iloc[0]
        buffered = point.buffer(buffer_meters / 111000.0)
        return any(self.riverine_masks.contains(buffered) | self.riverine_masks.intersects(buffered))

    def load_geotiff(self, image_path: str) -> rasterio.DatasetReader:
        return rasterio.open(image_path)

    def compute_riverine_score(
        self, image_path: str, metadata: dict
    ) -> float:
        with self.load_geotiff(image_path) as src:
            if src.crs is None:
                return 0.0
            bounds = src.bounds
            center_lat = (bounds.top + bounds.bottom) / 2.0
            center_lon = (bounds.left + bounds.right) / 2.0

        in_riverine = self.is_riverine_location(center_lat, center_lon)

        meta = metadata.get("metadata", {})
        waste_types = meta.get("type_of_visible_objects", "")
        area_type = meta.get("area_type", "unknown")

        score = 0.0
        if in_riverine:
            score += 0.4
        if any(wt in waste_types.lower() for wt in RIVERINE_WASTE_CLASSES):
            score += 0.3
        if area_type.lower() in ("riparian", "riverbank", "floodplain", "wetland"):
            score += 0.3
        return min(score, 1.0)

    def filter_riverine_subset(
        self,
        metadata: dict,
        min_score: float = 0.3,
        source_preference: str = AGEA_ORDER,
    ) -> list[dict]:
        candidates = []
        for entry in metadata.get("data", []):
            img_path = entry.get("image_path", "")
            if not img_path or not os.path.exists(img_path):
                continue
            score = self.compute_riverine_score(img_path, entry)
            if score >= min_score:
                candidates.append({**entry, "riverine_score": score})

        candidates.sort(key=lambda x: x.get("riverine_score", 0.0), reverse=True)

        if source_preference:
            source_key = f"source"
            candidates.sort(
                key=lambda x: (
                    0 if x.get(source_key) == source_preference else 1,
                    -x.get("riverine_score", 0.0),
                )
            )
        return candidates

    def tile_and_convert_annotations(
        self, image_path: str, annotations: dict, split: str
    ) -> list[dict]:
        with self.load_geotiff(image_path) as src:
            width = src.width
            height = src.height
            tiles = []
            for i in range(0, height, self.tile_size):
                for j in range(0, width, self.tile_size):
                    window = Window(j, i, self.tile_size, self.tile_size)
                    if window.width > width or window.height > height:
                        continue
                    tile_name = os.path.basename(image_path).replace(".tif", f"_tile_{i}_{j}.tif")
                    tile_path = self.output_dir / "images" / split / tile_name
                    profile = src.profile.copy()
                    profile.update({"height": self.tile_size, "width": self.tile_size, "transform": src.window_transform(window)})
                    with rasterio.open(tile_path, "w", **profile) as dst:
                        dst.write(src.read(window=window))
                    tiles.append({"tile_path": str(tile_path), "annotations": annotations, "split": split})
        return tiles

    def ingest(
        self,
        metadata_path: str,
        geojson_path: Optional[str] = None,
        min_score: float = 0.3,
        train_ratio: float = 0.7,
        val_ratio: float = 0.15,
    ) -> dict:
        metadata = self.fetch_metadata(local_path=metadata_path)
        if geojson_path:
            self.load_riverine_boundaries(geojson_path)
        riverine_entries = self.filter_riverine_subset(metadata, min_score=min_score)

        n_total = len(riverine_entries)
        n_train = int(n_total * train_ratio)
        n_val = int(n_total * val_ratio)

        splits = {
            "train": riverine_entries[:n_train],
            "val": riverine_entries[n_train : n_train + n_val],
            "test": riverine_entries[n_train + n_val :],
        }

        summary = {"total": n_total, "train": n_train, "val": n_val, "test": n_total - n_train - n_val}
        for split_name, entries in splits.items():
            for entry in entries:
                self.tile_and_convert_annotations(
                    entry.get("image_path", ""),
                    entry.get("annotations", {}),
                    split_name,
                )
        return summary


if __name__ == "__main__":
    ingestor = RiverineAerialWasteIngestor(
        root_dir="/data/aerialwaste",
        output_dir="/data/riverine_waste",
        tile_size=640,
    )
    result = ingestor.ingest(
        metadata_path="/data/aerialwaste/metadata.json",
        geojson_path="/data/aerialwaste/river_boundaries.geojson",
        min_score=0.3,
    )
    print(f"Ingestion complete: {result}")