import xarray as xr


INPUT = (
    "data/raw/weather/era5/test_unpacked/"
    "data_stream-oper_stepType-instant.nc"
)


# Load ERA5 temperature data
ds = xr.open_dataset(INPUT, engine="netcdf4")

# Convert Kelvin to Celsius
temperature = ds["t2m"] - 273.15

# Study-area mean at each timestamp
spatial_mean = temperature.mean(
    dim=["latitude", "longitude"]
)

# Spatial temperature anomaly
anomaly = temperature - spatial_mean


# Calculate the 3x3 rolling sum.
# The center cell is included here temporarily.
rolling_sum = anomaly.rolling(
    latitude=3,
    longitude=3,
    center=True
).sum()


# Remove the center cell from the 3x3 sum.
neighbour_sum = rolling_sum - anomaly


# Calculate the mean of the 8 surrounding cells.
neighbour_mean = neighbour_sum / 8


# Local contrast:
# positive = warmer than neighbours
# negative = colder than neighbours
neighbourhood_contrast = anomaly - neighbour_mean


# Only keep cells with a complete 3x3 neighbourhood.
valid_contrast = neighbourhood_contrast.where(
    rolling_sum.notnull()
)


print("\n=== CLEAN NEIGHBOURHOOD ANALYSIS ===")

print("\nMaximum neighbourhood contrast:")
print(float(valid_contrast.max()), "°C")

print("\nMinimum neighbourhood contrast:")
print(float(valid_contrast.min()), "°C")

print("\nMean neighbourhood contrast:")
print(float(valid_contrast.mean()), "°C")

print("\nStandard deviation:")
print(float(valid_contrast.std()), "°C")


ds.close()