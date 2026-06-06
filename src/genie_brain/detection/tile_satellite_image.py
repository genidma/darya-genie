import rasterio
from rasterio.windows import Window
import os

def tile_image(input_path, output_dir, tile_size=640):
    """
    Tiles a high-resolution GeoTIFF into smaller patches (e.g., 640x640).
    """
    os.makedirs(output_dir, exist_ok=True)
    with rasterio.open(input_path) as src:
        width = src.width
        height = src.height
        for i in range(0, height, tile_size):
            for j in range(0, width, tile_size):
                window = Window(j, i, tile_size, tile_size)
                transform = src.window_transform(window)
                profile = src.profile.copy()
                profile.update({
                    'height': tile_size,
                    'width': tile_size,
                    'transform': transform
                })
                output_file = os.path.join(output_dir, f"tile_{i}_{j}.tif")
                with rasterio.open(output_file, 'w', **profile) as dst:
                    dst.write(src.read(window=window))
    print(f"Tiling complete. Tiles saved to: {output_dir}")

if __name__ == "__main__":
    # Example usage:
    # tile_image("path/to/large_image.tif", "path/to/output_tiles/")
    pass
