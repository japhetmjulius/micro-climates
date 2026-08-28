import xarray as xr
import matplotlib.pyplot as plt

INPUT = (
    "data/raw/weather/era5/test_unpacked/"
    "data_stream-oper_stepType-instant.nc"
)

ds = xr.open_dataset(INPUT, engine="netcdf4")

# Kelvin → Celsius
temperature = ds["t2m"] - 273.15

# Regional mean at every timestamp
spatial_mean = temperature.mean(
    dim=["latitude", "longitude"]
)

# Spatial anomaly
anomaly = temperature - spatial_mean

# Frequency of strong anomalies
warm_frequency = (anomaly >= 5).mean(dim="valid_time")
cold_frequency = (anomaly <= -5).mean(dim="valid_time")

# -------------------------
# WARM PERSISTENCE
# -------------------------

plt.figure(figsize=(10, 7))

warm_frequency.plot()

plt.title(
    "Frequency of Strong Warm Anomaly\n"
    "(Anomaly ≥ +5°C)"
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()

plt.savefig(
    "outputs/figures/warm_anomaly_persistence.png",
    dpi=150
)

plt.close()

# -------------------------
# COLD PERSISTENCE
# -------------------------

plt.figure(figsize=(10, 7))

cold_frequency.plot()

plt.title(
    "Frequency of Strong Cold Anomaly\n"
    "(Anomaly ≤ −5°C)"
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()

plt.savefig(
    "outputs/figures/cold_anomaly_persistence.png",
    dpi=150
)

plt.close()

print("Persistence maps created.")
