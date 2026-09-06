import pandas as pd
from scipy.stats import pearsonr

FILE = "data/processed/microclimate_terrain_features.csv"

df = pd.read_csv(FILE)

df = df.dropna(
    subset=[
        "terrain_position_m",
        "elevation_residual_c",
        "local_contrast_c"
    ]
).copy()

print("\n=== TERRAIN POSITION ANALYSIS ===")
print("Valid observations:", len(df))

tests = [
    (
        "Terrain position vs elevation residual",
        "terrain_position_m",
        "elevation_residual_c"
    ),
    (
        "Terrain position vs local temperature contrast",
        "terrain_position_m",
        "local_contrast_c"
    ),
    (
        "Terrain position vs temperature anomaly",
        "terrain_position_m",
        "temperature_anomaly_c"
    ),
]

for name, x, y in tests:

    r, p = pearsonr(df[x], df[y])

    print(f"\n{name}")
    print(f"Correlation: {r:.4f}")
    print(f"P-value:     {p:.6f}")

print("\n=== CANDIDATE COMPARISON ===")

for lat, lon, label in [
    (1.25, 36.00, "WARM"),
    (-0.50, 37.00, "COLD")
]:

    cell = df[
        (df["latitude"] == lat) &
        (df["longitude"] == lon)
    ]

    print(f"\n{label} ({lat}, {lon})")

    print(
        cell[
            [
                "terrain_position_m",
                "elevation_residual_c",
                "temperature_anomaly_c",
                "local_contrast_c"
            ]
        ].describe().to_string()
    )
