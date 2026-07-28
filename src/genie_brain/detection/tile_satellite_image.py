import os
from typing import Optional
import rasterio
from rasterio.windows import Window
import numpy as np


def tile_image(
    input_path: str,
    output_dir: str,
    tile_size: int = 640,
    overlap: float = 0.0,
    min_dimension: Optional[int] = None,
) -> dict[str, int]:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input image not found: {input_path}")
    if tile_size <= 0:
        raise ValueError(f"tile_size must be positive, got {tile_size}")
    os.makedirs(output_dir, exist_ok=True)
    stats = {"tiles_written": 0, "rows": 0, "cols": 0}
    with rasterio.open(input_path) as src:
        width = src.width
        height = src.height
        if min_dimension is not None:
            tile_size = min(tile_size, min(width, height))
        step = max(1, int(tile_size * (1.0 - overlap)))
        for i in range(0, height, step):
            row_h = min(tile_size, height - i)
            for j in range(0, width, step):
                col_w = min(tile_size, width - j)
                window = Window(j, i, col_w, row_h)
                transform = src.window_transform(window)
                profile = src.profile.copy()
                profile.update(
                    {
                        "height": row_h,
                        "width": col_w,
                        "transform": transform,
                    }
                )
                output_file = os.path.join(output_dir, f"tile_{i}_{j}.tif")
                with rasterio.open(output_file, "w", **profile) as dst:
                    dst.write(src.read(window=window))
                stats["tiles_written"] += 1
            stats["rows"] += 1
        stats["cols"] = width // step + (1 if width % step else 0)
    print(f"Tiling complete. {stats['tiles_written']} tiles saved to: {output_dir}")
    return stats


def tile_with_labels(
    input_path: str,
    output_dir: str,
    label_geojson: Optional[str] = None,
    tile_size: int = 640,
    overlap: float = 0.0,
) -> dict[str, int]:
    """Tile imagery and optionally extract label annotations per tile."""
    stats = tile_image(input_path, output_dir, tile_size=tile_size, overlap=overlap)
    if label_geojson is None:
        return stats
    import json
    with open(label_geojson, "r") as f:
        labels = json.load(f)
    tile_info = {"tiles_with_labels": 0, "total_labels": 0}
    tiles_dir = output_dir
    for tile_file in sorted(os.listdir(tiles_dir)):
        if not tile_file.endswith(".tif"):
            continue
        tile_path = os.path.join(tiles_dir, tile_file)
        with rasterio.open(tile_path) as src:
            tile_bounds = src.bounds
        matched = []
        for feature in labels.get("features", []):
            geom = feature.get("geometry", {})
            if geom.get("type") == "Polygon":
                coords = geom["coordinates"][0]
                poly_points = [(c[0], c[1]) for c in coords]
                from shapely.geometry import Polygon
                poly = Polygon(poly_points)
                if poly.intersects(
                    type(
                        "Bounds",
                        (),
                        {
                            "left": tile_bounds.left,
                            "bottom": tile_bounds.bottom,
                            "right": tile_bounds.right,
                            "top": tile_bounds.top,
                        },
                    )()
                ):
                    matched.append(feature)
        if matched:
            tile_info["tiles_with_labels"] += 1
            tile_info["total_labels"] += len(matched)
            label_out = os.path.splitext(tile_file)[0] + ".json"
            with open(os.path.join(tiles_dir, label_out), "w") as lf:
                json.dump({"tile": tile_file, "features": matched}, lf, indent=2)
    print(f"Label extraction complete. {tile_info['tiles_with_labels']} tiles with labels.")
    return {**stats, **tile_info}


if __name__ == "__main__":
    tile_image("path/to/large_image.tif", "path/to/output_tiles/", tile_size=640, overlap=0.1)
