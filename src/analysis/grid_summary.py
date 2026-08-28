import xarray as xr

INPUT = (
    "data/raw/weather/era5/test_unpacked/"
    "data_stream-oper_stepType-instant.nc"
)

ds = xr.open_dataset(INPUT, engine="netcdf4")

t = ds["t2m"] - 273.15

print("\n=== GRID SUMMARY ===")

print("Latitude:")
print(ds.latitude.values)

print("\nLongitude:")
print(ds.longitude.values)

print("\nNumber of latitude points:", len(ds.latitude))
print("Number of longitude points:", len(ds.longitude))

print("\nGrid cells:", len(ds.latitude) * len(ds.longitude))

print("\nLatitude range:")
print(float(ds.latitude.min()), "to", float(ds.latitude.max()))

print("\nLongitude range:")
print(float(ds.longitude.min()), "to", float(ds.longitude.max()))

print("\nTemperature range:")
print(float(t.min()), "°C to", float(t.max()), "°C")

print("\nTime steps:")
print(len(ds.valid_time))

print("\nTime range:")
print(ds.valid_time.values[0])
print("to")
print(ds.valid_time.values[-1])