import pandas as pd

FILE = "data/processed/microclimate_residuals.csv"

df = pd.read_csv(FILE)

candidates = [
    (1.25, 36.00, "WARM"),
    (-0.50, 37.00, "COLD"),
]

for lat, lon, label in candidates:

    print("\n" + "=" * 70)
    print(f"{label} CANDIDATE")
    print(f"Location: {lat}, {lon}")
    print("=" * 70)

    cell = df[
        (df["latitude"] == lat) &
        (df["longitude"] == lon)
    ]

    print("\nCandidate statistics:")
    print(
        cell[
            [
                "temperature_anomaly_c",
                "local_contrast_c",
                "elevation_mean_m",
                "elevation_min_m",
                "elevation_max_m",
                "elevation_range_m",
                "elevation_std_m",
                "elevation_residual_c"
            ]
        ].describe().to_string()
    )

    # Spatial neighbors within one ERA5 grid cell
    neighbors = df[
        (df["latitude"].between(lat - 0.25, lat + 0.25)) &
        (df["longitude"].between(lon - 0.25, lon + 0.25))
    ]

    spatial = (
        neighbors.groupby(
            ["latitude", "longitude"]
        )[
            [
                "temperature_anomaly_c",
                "elevation_mean_m",
                "elevation_range_m",
                "elevation_std_m",
                "elevation_residual_c"
            ]
        ]
        .mean()
        .reset_index()
    )

    print("\n9-cell neighborhood:")
    print(
        spatial.to_string(index=False)
    )
