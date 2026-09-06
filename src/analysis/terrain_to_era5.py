import xarray as xr
import rasterio
import numpy as np
import pandas as pd
from pathlib import Path


ERA5_FILE = Path(
    "data/raw/weather/era5/test_unpacked/"
    "data_stream-oper_stepType-instant.nc"
)

DEM_FILE = Path(
    "data/raw/terrain/copernicus_dem_study_area.tif"
)

OUTPUT = Path(
    "data/processed/terrain_era5_grid.csv"
)


# ---------------------------------------------------------
# 1. Load ERA5 grid
# ---------------------------------------------------------

ds = xr.open_dataset(ERA5_FILE, engine="netcdf4")

latitudes = ds.latitude.values
longitudes = ds.longitude.values

print("\n=== ERA5 GRID ===")
print("Latitude cells:", len(latitudes))
print("Longitude cells:", len(longitudes))
print("Total cells:", len(latitudes) * len(longitudes))


# ---------------------------------------------------------
# 2. Determine ERA5 cell boundaries
# ---------------------------------------------------------

lat_spacing = abs(float(latitudes[1] - latitudes[0]))
lon_spacing = abs(float(longitudes[1] - longitudes[0]))

half_lat = lat_spacing / 2
half_lon = lon_spacing / 2


# ---------------------------------------------------------
# 3. Open DEM
# ---------------------------------------------------------

with rasterio.open(DEM_FILE) as src:

    print("\n=== DEM ===")
    print("Resolution:", src.res)
    print("Bounds:", src.bounds)

    results = []

    # -----------------------------------------------------
    # 4. Process every ERA5 cell
    # -----------------------------------------------------

    for lat in latitudes:
        for lon in longitudes:

            # Cell footprint
            cell_min_lat = lat - half_lat
            cell_max_lat = lat + half_lat

            cell_min_lon = lon - half_lon
            cell_max_lon = lon + half_lon

            # Intersect with available DEM
            min_lon = max(cell_min_lon, src.bounds.left)
            max_lon = min(cell_max_lon, src.bounds.right)

            min_lat = max(cell_min_lat, src.bounds.bottom)
            max_lat = min(cell_max_lat, src.bounds.top)

            # Skip cells with no overlap
            if min_lon >= max_lon or min_lat >= max_lat:
                continue

            # Convert geographic bounds to raster window
            window = rasterio.windows.from_bounds(
                min_lon,
                min_lat,
                max_lon,
                max_lat,
                src.transform
            )

            # Read DEM pixels
            elevation = src.read(
                1,
                window=window,
                masked=True
            )

            # Remove invalid values
            values = elevation.compressed()

            if len(values) == 0:
                continue

            # Terrain statistics
            results.append(
                {
                    "latitude": float(lat),
                    "longitude": float(lon),
                    "elevation_mean_m": float(np.mean(values)),
                    "elevation_min_m": float(np.min(values)),
                    "elevation_max_m": float(np.max(values)),
                    "elevation_range_m": float(
                        np.max(values) - np.min(values)
                    ),
                    "elevation_std_m": float(np.std(values)),
                    "dem_pixel_count": int(len(values)),
                }
            )


# ---------------------------------------------------------
# 5. Save results
# ---------------------------------------------------------

output_df = pd.DataFrame(results)

OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True
)

output_df.to_csv(
    OUTPUT,
    index=False
)


print("\n=== TERRAIN AGGREGATION COMPLETE ===")
print("Cells produced:", len(output_df))
print("Expected ERA5 cells:", len(latitudes) * len(longitudes))
print("Output:", OUTPUT)

print("\nFirst five cells:")
print(output_df.head().to_string(index=False))

ds.close()
