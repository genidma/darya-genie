"""
Spectral Analysis Module for Darya Genie.
Computes vegetation/water indices (NDVI, NDWI) from multispectral and Sentinel-2 imagery
to support pollution detection and river health assessment.
"""

import numpy as np
import rasterio
from rasterio.plot import show
from typing import Optional, Literal


def compute_ndvi(red_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    """Compute Normalized Difference Vegetation Index."""
    denom = red_band.astype(np.float32) + nir_band.astype(np.float32)
    denom = np.where(denom == 0, 1e-10, denom)
    return (nir_band.astype(np.float32) - red_band.astype(np.float32)) / denom


def compute_ndwi(
    green_band: np.ndarray, nir_band: np.ndarray
) -> np.ndarray:
    """Compute Normalized Difference Water Index."""
    denom = green_band.astype(np.float32) + nir_band.astype(np.float32)
    denom = np.where(denom == 0, 1e-10, denom)
    return (green_band.astype(np.float32) - nir_band.astype(np.float32)) / denom


def compute_awi(
    green_band: np.ndarray, swir_band: np.ndarray
) -> np.ndarray:
    """Compute Automated Water Index (MNDWI variant)."""
    denom = green_band.astype(np.float32) + swir_band.astype(np.float32)
    denom = np.where(denom == 0, 1e-10, denom)
    return (green_band.astype(np.float32) - swir_band.astype(np.float32)) / denom


def compute_ndbi(
    swir1_band: np.ndarray, swir2_band: np.ndarray
) -> np.ndarray:
    """Compute Normalized Difference Built-up Index."""
    denom = swir1_band.astype(np.float32) + swir2_band.astype(np.float32)
    denom = np.where(denom == 0, 1e-10, denom)
    return (swir1_band.astype(np.float32) - swir2_band.astype(np.float32)) / denom


def get_sentinel2_band_indices(sensor: Literal["S2L1C", "S2L2A"]) -> dict[str, int]:
    if sensor == "S2L1C":
        return {
            "B2": 0,
            "B3": 1,
            "B4": 2,
            "B5": 3,
            "B6": 4,
            "B7": 5,
            "B8": 6,
            "B8A": 7,
            "B11": 8,
            "B12": 9,
        }
    return {
        "B2": 0,
        "B3": 1,
        "B4": 2,
        "B5": 3,
        "B6": 4,
        "B7": 5,
        "B8": 6,
        "B8A": 7,
        "B11": 8,
        "B12": 9,
    }


def analyze_multispectral(
    image_path: str,
    indices: list[str] | None = None,
    sensor: Literal["S2L1C", "S2L2A"] = "S2L1C",
    output_dir: Optional[str] = None,
) -> dict[str, np.ndarray]:
    if indices is None:
        indices = ["ndvi", "ndwi", "awi", "ndbi"]

    band_map = get_sentinel2_band_indices(sensor)
    results: dict[str, np.ndarray] = {}

    with rasterio.open(image_path) as src:
        bands = src.read()
        profile = src.profile.copy()

    b2 = bands[band_map["B2"]].astype(np.float32)
    b3 = bands[band_map["B3"]].astype(np.float32)
    b4 = bands[band_map["B4"]].astype(np.float32)
    b5 = bands[band_map["B5"]].astype(np.float32) if len(bands) > band_map["B5"] else None
    b7 = bands[band_map["B7"]].astype(np.float32) if len(bands) > band_map["B7"] else None
    b8 = bands[band_map["B8"]].astype(np.float32)
    b8a = bands[band_map["B8A"]].astype(np.float32) if band_map.get("B8A") is not None and len(bands) > band_map["B8A"] else None
    b11 = bands[band_map["B11"]].astype(np.float32) if len(bands) > band_map["B11"] else None
    b12 = bands[band_map["B12"]].astype(np.float32) if len(bands) > band_map["B12"] else None

    if "ndvi" in indices and b8 is not None and b4 is not None:
        results["ndvi"] = compute_ndvi(b4, b8)

    if "ndwi" in indices and b3 is not None and b8 is not None:
        results["ndwi"] = compute_ndwi(b3, b8)

    if "awi" in indices and b3 is not None and b11 is not None:
        results["awi"] = compute_awi(b3, b11)

    if "ndbi" in indices and b11 is not None and b12 is not None:
        results["ndbi"] = compute_ndbi(b11, b12)

    if output_dir:
        import os
        os.makedirs(output_dir, exist_ok=True)
        for name, arr in results.items():
            out_profile = profile.copy()
            out_profile.update({"count": 1, "dtype": "float32"})
            out_path = os.path.join(output_dir, f"{name}.tif")
            with rasterio.open(out_path, "w", **out_profile) as dst:
                dst.write(arr, 1)

    return results


def river_health_assessment(
    image_path: str, sensor: Literal["S2L1C", "S2L2A"] = "S2L1C"
) -> dict[str, float]:
    results = analyze_multispectral(image_path, indices=["ndvi", "ndwi", "awi"], sensor=sensor)
    assessment: dict[str, float] = {}
    for name, arr in results.items():
        arr_clean = arr[np.isfinite(arr)]
        if arr_clean.size == 0:
            assessment[name] = float("nan")
            continue
        mean_val = float(np.mean(arr_clean))
        std_val = float(np.std(arr_clean))
        assessment[name] = {"mean": mean_val, "std": std_val, "trend": "healthy" if mean_val > 0.2 else "degraded"}
    return assessment


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python spectral_analysis.py <image_path>")
        sys.exit(1)
    result = analyze_multispectral(sys.argv[1], output_dir="./spectral_output")
    print(f"Computed indices: {list(result.keys())}")