import json
from pathlib import Path

import cdsapi


PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_FILE = PROJECT_ROOT / "config" / "study_area.json"
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "weather" / "era5"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_study_area():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def download_era5():
    study_area = load_study_area()
    bbox = study_area["bbox"]

    client = cdsapi.Client()

    request = {
        "product_type": ["reanalysis"],
        "variable": [
            "2m_temperature",
            "total_precipitation",
        ],
        "year": ["2025"],
        "month": ["01"],
        "day": ["01", "02", "03"],
        "time": [
            "00:00",
            "06:00",
            "12:00",
            "18:00"
        ],
        "data_format": "netcdf",
        "download_format": "unarchived",
        "area": [
            bbox["north"],
            bbox["west"],
            bbox["south"],
            bbox["east"]
        ]
    }

    output_file = OUTPUT_DIR / "era5_test.nc"

    print("Requesting ERA5 data...")
    print(f"Study area: {study_area['name']}")
    print(f"Output: {output_file}")

    client.retrieve(
        "reanalysis-era5-single-levels",
        request,
        str(output_file)
    )

    print("Download completed.")


if __name__ == "__main__":
    download_era5()