import xarray as xr
import pandas as pd
import numpy as np
from pathlib import Path

ERA5_FILE = Path(
    "data/raw/weather/era5/test_unpacked/"
    "data_stream-oper_stepType-instant.nc"
)

TERRAIN_FILE = Path(
    "data/processed/terrain_era5_grid.csv"
)

OUTPUT = Path(
    "data/processed/microclimate_analysis.csv"
)

# -----------------------------
# 1. Load ERA5
# -----------------------------
ds = xr.open_dataset(ERA5_FILE, engine="netcdf4")

temperature = ds["t2m"] - 273.15

# Spatial anomaly:
# each cell's temperature minus the
# study-area mean at that timestamp.
spatial_mean = temperature.mean(
    dim=["latitude", "longitude"]
)

anomaly = temperature - spatial_mean

# -----------------------------
# 2. Calculate local contrast
# -----------------------------
rolling_sum = anomaly.rolling(
    latitude=3,
    longitude=3,
    center=True
).sum()

center = anomaly

neighbor_mean = (
    rolling_sum - center
) / 8

local_contrast = center - neighbor_mean

# Only cells with a complete 3x3 neighborhood
local_contrast = local_contrast.where(
    anomaly.rolling(
        latitude=3,
        longitude=3,
        center=True
    ).count() == 9
)

# -----------------------------
# 3. Convert ERA5 to DataFrame
# -----------------------------
temperature_df = temperature.to_dataframe(
    name="temperature_c"
).reset_index()

anomaly_df = anomaly.to_dataframe(
    name="temperature_anomaly_c"
).reset_index()

contrast_df = local_contrast.to_dataframe(
    name="local_contrast_c"
).reset_index()

era5_df = temperature_df.merge(
    anomaly_df,
    on=["valid_time", "latitude", "longitude"]
)

era5_df = era5_df.merge(
    contrast_df,
    on=["valid_time", "latitude", "longitude"]
)

# -----------------------------
# 4. Load terrain
# -----------------------------
terrain_df = pd.read_csv(TERRAIN_FILE)

# -----------------------------
# 5. Join terrain to ERA5
# -----------------------------
combined = era5_df.merge(
    terrain_df,
    on=["latitude", "longitude"],
    how="left"
)

# -----------------------------
# 6. Save
# -----------------------------
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

combined.to_csv(
    OUTPUT,
    index=False
)

print("\n=== COMBINED DATASET ===")
print("Rows:", len(combined))
print("Columns:", len(combined.columns))
print("Output:", OUTPUT)

print("\nColumns:")
print(list(combined.columns))

print("\nMissing values:")
print(combined.isna().sum())

print("\nFirst five rows:")
print(combined.head().to_string(index=False))

ds.close()
