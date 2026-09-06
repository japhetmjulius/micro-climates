import pandas as pd
import numpy as np
from scipy.stats import linregress

FILE = "data/processed/microclimate_analysis.csv"
OUTPUT = "data/processed/microclimate_residuals.csv"

df = pd.read_csv(FILE)

df = df.dropna(
    subset=[
        "elevation_mean_m",
        "temperature_anomaly_c",
        "local_contrast_c"
    ]
).copy()

# Fit a simple linear relationship:
# temperature anomaly = a + b * elevation
result = linregress(
    df["elevation_mean_m"],
    df["temperature_anomaly_c"]
)

df["predicted_anomaly_c"] = (
    result.intercept
    + result.slope * df["elevation_mean_m"]
)

# Actual - predicted
df["elevation_residual_c"] = (
    df["temperature_anomaly_c"]
    - df["predicted_anomaly_c"]
)

print("\n=== ELEVATION REGRESSION ===")
print(f"Slope:      {result.slope:.6f} °C/m")
print(f"Intercept:  {result.intercept:.4f} °C")
print(f"R²:         {result.rvalue ** 2:.4f}")

print("\n=== RESIDUAL STATISTICS ===")
print(
    df["elevation_residual_c"].describe()
)

print("\n=== WARMEST UNEXPLAINED CELLS ===")

warm = df.nlargest(
    10,
    "elevation_residual_c"
)

print(
    warm[
        [
            "valid_time",
            "latitude",
            "longitude",
            "temperature_anomaly_c",
            "elevation_mean_m",
            "predicted_anomaly_c",
            "elevation_residual_c",
            "local_contrast_c"
        ]
    ].to_string(index=False)
)

print("\n=== COLDEST UNEXPLAINED CELLS ===")

cold = df.nsmallest(
    10,
    "elevation_residual_c"
)

print(
    cold[
        [
            "valid_time",
            "latitude",
            "longitude",
            "temperature_anomaly_c",
            "elevation_mean_m",
            "predicted_anomaly_c",
            "elevation_residual_c",
            "local_contrast_c"
        ]
    ].to_string(index=False)
)

df.to_csv(OUTPUT, index=False)

print("\nSaved:", OUTPUT)
