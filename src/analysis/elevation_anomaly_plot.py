import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FILE = "data/processed/microclimate_analysis.csv"
OUTPUT = Path("outputs/figures/elevation_vs_anomaly.png")

df = pd.read_csv(FILE)

df = df.dropna(
    subset=[
        "elevation_mean_m",
        "temperature_anomaly_c"
    ]
)

plt.figure(figsize=(9, 6))

plt.scatter(
    df["elevation_mean_m"],
    df["temperature_anomaly_c"],
    alpha=0.35
)

plt.xlabel("Mean elevation (m)")
plt.ylabel("Temperature anomaly (°C)")
plt.title("Elevation vs Spatial Temperature Anomaly")

plt.grid(True, alpha=0.2)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT, dpi=150, bbox_inches="tight")

print("Saved:", OUTPUT)

