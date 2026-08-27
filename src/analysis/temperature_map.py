import xarray as xr
import matplotlib.pyplot as plt

DATA = "data/raw/weather/era5/test_unpacked/data_stream-oper_stepType-instant.nc"

ds=  xr.open_dataset(DATA,engine="netcdf4")

temperature = ds["t2m"] -273.15

snapshot = temperature.sel(valid_time="2025-01-01T12:00:00")
plt.figure(figsize=(10,6))

snapshot.attrs["units"] = "°C"
snapshot.attrs["long_name"] = "2 metre temperature"

plt.title("ERA5 2m Temperature - 2025-01-01 12:00 UTC")
plt.xlabel("longitude")
plt.ylabel("latitude")

plt.tight_layout()

plt.savefig("outputs/figures/era5_temperature_20250101_1200.png",dpi=150)

