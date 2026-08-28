import rasterio
from rasterio.windows import from_bounds
from pathlib import Path


INPUT = Path(
    "data/raw/terrain/copernicus_dem_mosaic.tif"
)

OUTPUT = Path(
    "data/raw/terrain/copernicus_dem_study_area.tif"
)


# Exact ERA5 study area
MIN_LON = 35.0
MAX_LON = 37.5
MIN_LAT = -1.5
MAX_LAT = 1.5


with rasterio.open(INPUT) as src:

    # Convert geographic bounds into raster pixel coordinates
    window = from_bounds(
        MIN_LON,
        MIN_LAT,
        MAX_LON,
        MAX_LAT,
        src.transform
    )

    # Read only the required portion
    data = src.read(window=window)

    # Calculate the transform for the clipped raster
    transform = src.window_transform(window)

    # Copy original metadata
    metadata = src.meta.copy()

    # Update metadata for clipped raster
    metadata.update(
        {
            "height": data.shape[1],
            "width": data.shape[2],
            "transform": transform,
            "compress": "deflate",
        }
    )

    # Write clipped DEM
    with rasterio.open(
        OUTPUT,
        "w",
        **metadata
    ) as dst:

        dst.write(data)


print("=== DEM CLIPPED ===")
print(f"Output: {OUTPUT}")
print(f"Width: {data.shape[2]}")
print(f"Height: {data.shape[1]}")
print(f"Bounds:")
print(f"  Longitude: {MIN_LON} to {MAX_LON}")
print(f"  Latitude:  {MIN_LAT} to {MAX_LAT}")