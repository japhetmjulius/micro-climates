import xarray as xr
import matplotlib.pyplot as plt


INPUT = (
    "data/raw/weather/era5/test_unpacked/"
    "data_stream-oper_stepType-instant.nc"
)

OUTPUT = "outputs/figures/neighborhood_contrast_20250101_1200.png"


# Load ERA5 temperature
ds = xr.open_dataset(INPUT, engine="netcdf4")

# Convert Kelvin to Celsius
temperature = ds["t2m"] - 273.15

# Select the same snapshot we've been studying
temperature = temperature.sel(
    valid_time="2025-01-01T12:00:00"
)

# Calculate spatial anomaly
spatial_mean = temperature.mean(
    dim=["latitude", "longitude"]
)

anomaly = temperature - spatial_mean


# 3x3 rolling sum
rolling_sum = anomaly.rolling(
    latitude=3,
    longitude=3,
    center=True
).sum()


# Remove the centre cell
neighbour_sum = rolling_sum - anomaly

# Mean of the 8 surrounding cells
neighbour_mean = neighbour_sum / 8

# Local temperature contrast
neighbourhood_contrast = anomaly - neighbour_mean

# Keep only cells with a complete neighbourhood
valid_contrast = neighbourhood_contrast.where(
    rolling_sum.notnull()
)


# Create map
plt.figure(figsize=(10, 7))

valid_contrast.plot(
    cmap="RdBu_r",
    center=0,
    cbar_kwargs={
        "label": "Temperature contrast relative to 8 neighbours (°C)"
    }
)

plt.title(
    "Local Temperature Contrast\n"
    "ERA5 — 1 January 2025, 12:00"
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()

plt.savefig(OUTPUT, dpi=150)

print(f"\nMap saved to: {OUTPUT}")

ds.close()