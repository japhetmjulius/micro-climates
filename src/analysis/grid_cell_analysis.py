import xarray as xr
import pandas as pd

INPUT = (
    "data/raw/weather/era5/test_unpacked/"
    "data_stream-oper_stepType-instant.nc"
)

ds = xr.open_dataset(INPUT, engine="netcdf4")

# Kelvin → Celsius
temperature = ds["t2m"] - 273.15

# Spatial mean at each timestamp
spatial_mean = temperature.mean(
    dim=["latitude", "longitude"]
)

# Anomaly relative to the timestamp's spatial mean
anomaly = temperature - spatial_mean

# Strong anomaly masks
warm = anomaly >= 5
cold = anomaly <= -5

# Frequency through time
warm_frequency = warm.mean(dim="valid_time")
cold_frequency = cold.mean(dim="valid_time")

# Statistics for each grid cell
mean_temperature = temperature.mean(dim="valid_time")
minimum_temperature = temperature.min(dim="valid_time")
maximum_temperature = temperature.max(dim="valid_time")

mean_anomaly = anomaly.mean(dim="valid_time")
minimum_anomaly = anomaly.min(dim="valid_time")
maximum_anomaly = anomaly.max(dim="valid_time")

# Convert xarray data into a table
table = xr.Dataset({
    "mean_temperature_C": mean_temperature,
    "minimum_temperature_C": minimum_temperature,
    "maximum_temperature_C": maximum_temperature,
    "mean_anomaly_C": mean_anomaly,
    "minimum_anomaly_C": minimum_anomaly,
    "maximum_anomaly_C": maximum_anomaly,
    "warm_frequency": warm_frequency,
    "cold_frequency": cold_frequency,
}).to_dataframe().reset_index()

# Sort strongest warm cells first
table = table.sort_values(
    "warm_frequency",
    ascending=False
)

print("\n=== GRID CELL ANALYSIS ===\n")

print(table.to_string(index=False))

# Save for later analysis
OUTPUT = "outputs/grid_cell_analysis.csv"

table.to_csv(
    OUTPUT,
    index=False
)

print(f"\nSaved: {OUTPUT}")