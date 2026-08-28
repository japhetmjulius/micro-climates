import rasterio
from rasterio.merge import merge
from pathlib import Path


INPUT_DIR = Path("data/raw/terrain/copernicus_dem")
OUTPUT = Path("data/raw/terrain/copernicus_dem_mosaic.tif")


# Find all DEM tiles
tiles = sorted(INPUT_DIR.glob("*.tif"))

print(f"Found {len(tiles)} DEM tiles.")

if len(tiles) != 12:
    raise ValueError(
        f"Expected 12 DEM tiles, found {len(tiles)}"
    )


# Open all tiles
sources = [
    rasterio.open(tile)
    for tile in tiles
]

try:
    print("Mosaicking DEM tiles...")

    mosaic, transform = merge(sources)

    # Copy metadata from the first tile
    metadata = sources[0].meta.copy()

    # Update metadata for the mosaic
    metadata.update(
        {
            "height": mosaic.shape[1],
            "width": mosaic.shape[2],
            "transform": transform,
            "compress": "deflate",
        }
    )

    # Write mosaic
    with rasterio.open(
        OUTPUT,
        "w",
        **metadata
    ) as destination:

        destination.write(mosaic)

finally:
    # Close all input files
    for source in sources:
        source.close()


print(f"Mosaic saved to: {OUTPUT}")