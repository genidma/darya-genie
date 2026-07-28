import os
from pathlib import Path
from typing import Optional

import numpy as np
import rasterio
from rasterio.crs import CRS


def ensure_directory(path: str) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def validate_geotiff(image_path: str) -> dict:
    with rasterio.open(image_path) as src:
        info = {
            "path": image_path,
            "width": src.width,
            "height": src.height,
            "count": src.count,
            "crs": str(src.crs) if src.crs else None,
            "bounds": src.bounds,
            "driver": src.driver,
            "dtype": src.dtypes[0] if src.dtypes else None,
        }
    return info


def split_train_val_test(
    image_paths: list[str],
    train_ratio: float = 0.7,
    val_ratio: float = 0.15,
    seed: int = 42,
) -> dict[str, list[str]]:
    import random
    rng = random.Random(seed)
    shuffled = image_paths.copy()
    rng.shuffle(shuffled)
    n = len(shuffled)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    return {
        "train": shuffled[:n_train],
        "val": shuffled[n_train : n_train + n_val],
        "test": shuffled[n_train + n_val :],
    }


def generate_yolo_label(
    tile_path: str,
    annotations: list[dict],
    output_dir: str,
    class_id_map: dict[str, int],
) -> Optional[str]:
    if not annotations:
        return None
    with rasterio.open(tile_path) as src:
        tile_bounds = src.bounds
    label_lines = []
    for ann in annotations:
        geom = ann.get("geometry", {})
        if geom.get("type") != "Polygon":
            continue
        coords = geom["coordinates"][0]
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        cx = (minx + maxx) / 2.0
        cy = (miny + maxy) / 2.0
        w = maxx - minx
        h = maxy - miny
        class_name = ann.get("properties", {}).get("class", "unknown")
        class_id = class_id_map.get(class_name, 0)
        x_norm = cx / tile_bounds.right
        y_norm = cy / tile_bounds.top
        w_norm = w / (tile_bounds.right - tile_bounds.left)
        h_norm = h / (tile_bounds.top - tile_bounds.bottom)
        x_norm = max(0.0, min(1.0, x_norm))
        y_norm = max(0.0, min(1.0, y_norm))
        w_norm = max(0.0, min(1.0, w_norm))
        h_norm = max(0.0, min(1.0, h_norm))
        label_lines.append(f"{class_id} {x_norm:.6f} {y_norm:.6f} {w_norm:.6f} {h_norm:.6f}")
    if not label_lines:
        return None
    label_path = os.path.join(output_dir, Path(tile_path).stem + ".txt")
    with open(label_path, "w") as f:
        f.write("\n".join(label_lines))
    return label_path


def compute_raster_stats(image_path: str) -> dict:
    with rasterio.open(image_path) as src:
        arr = src.read()
        stats = {
            "shape": arr.shape,
            "dtype": str(arr.dtype),
            "min": float(np.nanmin(arr)),
            "max": float(np.nanmax(arr)),
            "mean": float(np.nanmean(arr)),
            "std": float(np.nanstd(arr)),
        }
    return stats
