import xarray as xr
INPUT = ("data/raw/weather/era5/test_unpacked/" "data_stream-oper_stepType-instant.nc")

ds = xr.open_dataset(INPUT,engine="netcdf4")

temperature = ds["t2m"] - 273.15

#spatial mean at each timestamp
spatial_mean = temperature.mean(dim=["latitude","longitude"])

#Temperature anomaly relative to that timestamp's spatial mean
anomaly = temperature - spatial_mean

print("\n=== SPATIAL ANOMALY ANALYSIS ===")

print("\nAnomaly dimensions:")
print(anomaly.dims)

print("\nAnomaly minimum:")
print(float(anomaly.min()),"°C")

print("\nAnomaly maximum:")
print(float(anomaly.max()),"°C")

print("\nAnomaly mean:")
print(float(anomaly.mean()),"°C")

print("\nStandard deviation:")
print(float(anomaly.std()),"°C")

warm = anomaly >= 5
cold = anomaly <= -5
warm_frequency = warm.mean(dim="valid_time")
cold_frequency = cold.mean(dim="valid_time")

print("\n=== PERSISTENCE ===")

print("\nMaximum warm-anomaly frequency:")
print(float(warm_frequency.max()))

print("\nMaximum cold_anomaly frequency:")
print(float(cold_frequency.max()))

persistent_warm = warm_frequency >= 0.5
persistent_cold = cold_frequency <= 0.5

print("\npersistent warm cells:")
print(persistent_warm.sum().item())

print("\npersistent cold cells:")
print(persistent_cold.sum().item())
