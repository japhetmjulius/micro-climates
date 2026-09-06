import pandas as pd
import xarray as xr

# IMPORTANT:
# Use the original combined dataset containing ALL 143 ERA5 cells.
FILE = "data/processed/microclimate_analysis.csv"

OUTPUT = "data/processed/microclimate_terrain_features.csv"

df = pd.read_csv(FILE)

# --------------------------------------------------
# 1. Build the complete 13 × 11 terrain grid
# --------------------------------------------------

terrain = (
    df.groupby(["latitude", "longitude"])[
        [
            "elevation_mean_m",
            "elevation_range_m",
            "elevation_std_m"
        ]
    ]
    .first()
    .reset_index()
)

grid = terrain.set_index(
    ["latitude", "longitude"]
).to_xarray()["elevation_mean_m"]

# --------------------------------------------------
# 2. Calculate 3 × 3 terrain neighborhood
# --------------------------------------------------

rolling = grid.rolling(
    latitude=3,
    longitude=3,
    center=True
)

window_sum = rolling.sum()
window_count = rolling.count()

# Remove the center cell
neighbor_sum = window_sum - grid

# Mean of the 8 surrounding cells
neighbor_mean = neighbor_sum / 8

# Require all 9 cells:
# 8 neighbors + center
terrain_position = (
    grid - neighbor_mean
).where(window_count == 9)

# --------------------------------------------------
# 3. Convert back to DataFrame
# --------------------------------------------------

position_df = (
    terrain_position
    .to_dataframe(name="terrain_position_m")
    .reset_index()
)

terrain = terrain.merge(
    position_df,
    on=["latitude", "longitude"],
    how="left"
)

# --------------------------------------------------
# 4. Join terrain position to all observations
# --------------------------------------------------

result = df.merge(
    terrain,
    on=["latitude", "longitude"],
    how="left",
    suffixes=("", "_terrain")
)

# Remove duplicate terrain columns
for col in [
    "elevation_mean_m_terrain",
    "elevation_range_m_terrain",
    "elevation_std_m_terrain"
]:
    if col in result.columns:
        result.drop(columns=col, inplace=True)

result.to_csv(OUTPUT, index=False)

# --------------------------------------------------
# 5. Verification
# --------------------------------------------------

print("\n=== TERRAIN POSITION ===")

for lat, lon, label in [
    (1.25, 36.00, "WARM"),
    (-0.50, 37.00, "COLD")
]:

    row = terrain[
        (terrain["latitude"] == lat) &
        (terrain["longitude"] == lon)
    ]

    print(f"\n{label} CANDIDATE ({lat}, {lon})")

    print(
        row[
            [
                "elevation_mean_m",
                "elevation_range_m",
                "elevation_std_m",
                "terrain_position_m"
            ]
        ].to_string(index=False)
    )

print("\n=== CHECK ===")
print("Terrain cells:", len(terrain))
print("Expected terrain cells: 143")
print("Rows:", len(result))

print(
    "Missing terrain positions:",
    result["terrain_position_m"].isna().sum()
)

print(
    "Expected missing positions:",
    12 * 44
)

print("\nSaved:", OUTPUT)
