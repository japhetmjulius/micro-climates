import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FILE = "data/processed/microclimate_residuals.csv"
OUTPUT = Path("outputs/figures/elevation_residual_map.png")

df = pd.read_csv(FILE)

# Average residual at each geographic cell
spatial = (
    df.groupby(["latitude", "longitude"])
    ["elevation_residual_c"]
    .mean()
    .reset_index()
)

pivot = spatial.pivot(
    index="latitude",
    columns="longitude",
    values="elevation_residual_c"
)

plt.figure(figsize=(10, 7))

plt.imshow(
    pivot.values,
    origin="upper",
    aspect="auto"
)

plt.colorbar(
    label="Elevation-model residual (°C)"
)

plt.xticks(
    range(len(pivot.columns)),
    [f"{x:.2f}" for x in pivot.columns],
    rotation=45
)

plt.yticks(
    range(len(pivot.index)),
    [f"{x:.2f}" for x in pivot.index]
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Temperature Residual After Removing Elevation Effect")

plt.tight_layout()

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT, dpi=150)

print("Saved:", OUTPUT)
