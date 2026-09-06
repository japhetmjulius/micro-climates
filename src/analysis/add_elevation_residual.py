import pandas as pd
from scipy.stats import linregress

INPUT = "data/processed/microclimate_terrain_features.csv"
OUTPUT = "data/processed/microclimate_terrain_features.csv"

df = pd.read_csv(INPUT)

# Use rows where elevation and temperature anomaly exist
valid = df.dropna(
    subset=[
        "elevation_mean_m",
        "temperature_anomaly_c"
    ]
).copy()

# Fit:
# temperature anomaly = slope * elevation + intercept
result = linregress(
    valid["elevation_mean_m"],
    valid["temperature_anomaly_c"]
)

slope = result.slope
intercept = result.intercept

print("=== ELEVATION REGRESSION ===")
print(f"Slope:     {slope:.8f} °C/m")
print(f"Intercept: {intercept:.6f} °C")
print(f"R²:        {result.rvalue ** 2:.4f}")

# Predicted anomaly from elevation
df["elevation_predicted_anomaly_c"] = (
    slope * df["elevation_mean_m"] + intercept
)

# Actual anomaly minus elevation-only prediction
df["elevation_residual_c"] = (
    df["temperature_anomaly_c"]
    - df["elevation_predicted_anomaly_c"]
)

df.to_csv(OUTPUT, index=False)

print("\nAdded column:")
print("elevation_residual_c")

print(f"\nSaved: {OUTPUT}")
