import pandas as pd
import numpy as np
from scipy.stats import pearsonr

FILE = "data/processed/microclimate_analysis.csv"

df = pd.read_csv(FILE)

# Remove rows where local contrast is unavailable.
analysis = df.dropna(subset=["local_contrast_c"]).copy()

print("\n=== ELEVATION vs TEMPERATURE ===")

# Temperature vs elevation
r_temp, p_temp = pearsonr(
    analysis["elevation_mean_m"],
    analysis["temperature_c"]
)

# Temperature anomaly vs elevation
r_anom, p_anom = pearsonr(
    analysis["elevation_mean_m"],
    analysis["temperature_anomaly_c"]
)

# Local contrast vs terrain variability
r_contrast, p_contrast = pearsonr(
    analysis["elevation_std_m"],
    analysis["local_contrast_c"]
)

print(f"\nTemperature vs mean elevation:")
print(f"Correlation: {r_temp:.4f}")
print(f"P-value:     {p_temp:.6f}")

print(f"\nTemperature anomaly vs mean elevation:")
print(f"Correlation: {r_anom:.4f}")
print(f"P-value:     {p_anom:.6f}")

print(f"\nLocal contrast vs elevation variability:")
print(f"Correlation: {r_contrast:.4f}")
print(f"P-value:     {p_contrast:.6f}")

print("\n=== BASIC TERRAIN STATISTICS ===")

print(
    analysis[
        [
            "elevation_mean_m",
            "elevation_range_m",
            "elevation_std_m"
        ]
    ].describe()
)

print("\n=== STRONGEST TERRAIN/TEMPERATURE RELATIONSHIPS ===")

# Average temperature by elevation quartile
analysis["elevation_group"] = pd.qcut(
    analysis["elevation_mean_m"],
    4,
    labels=["Lowest", "Low-Medium", "Medium-High", "Highest"]
)

grouped = analysis.groupby(
    "elevation_group",
    observed=True
)["temperature_c"].agg(["mean", "min", "max"])

print(grouped)

