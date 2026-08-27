import xarray as xr
import matplotlib.pyplot as plt

DATA ="data/raw/weather/era5/test_unpacked/data_stream-oper_stepType-instant.nc"

ds = xr.open_dataset(DATA,engine="netcdf4")

temperature = ds["t2m"]-273.15

snapshot = temperature.sel(valid_time="2025-01-01T12:00:00")

#regional mean temperature
regional_mean = snapshot.mean()

#temperautre anomaly relative to regional mean
anomaly = snapshot - regional_mean

anomaly.attrs["units"] = "°C"
anomaly.attrs["long_name"] = "Temperature anomaly"

print("Regional mean:",float(regional_mean), "°C")
print("Minimum  anomaly:",float(anomaly.min()), "°C")
print("Maximum anomaly:",float(anomaly.max()), "°C")

plt.figure(figsize=(10, 6))

anomaly.plot()

plt.title("ERA5 2m Temperature Anomaly - 2025-01-01 12:00 UTC")
plt.xlabel("longitude")
plt.ylabel("latitude")

plt.tight_layout()

plt.savefig("outputs/figures/era5_temperature_anomaly_20250101_1200.png",dpi=150)

