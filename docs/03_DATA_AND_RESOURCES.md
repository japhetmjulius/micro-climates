# Data, Resources and Tools

## 1. Programming

### Python

Primary language for:
- Data processing
- Scientific analysis
- GIS
- Machine learning
- APIs
- Automation

Core libraries:
- NumPy
- Pandas
- SciPy
- Matplotlib
- Scikit-learn
- Statsmodels

---

## 2. GIS

### QGIS

Use for:
- Inspecting geographic data
- Creating maps
- Terrain analysis
- Raster/vector operations
- Validating Python geospatial results

### Python geospatial stack

- GeoPandas
- Rasterio
- GDAL
- Shapely
- xarray
- rioxarray

### Database

PostgreSQL + PostGIS

Use when the project grows beyond simple files.

---

## 3. Meteorological and climate data

Investigate access to:

- Kenya Meteorological Department
- ECMWF / ERA5
- NASA Earth observation datasets
- ESA Copernicus
- Sentinel
- CHIRPS
- GPM
- WorldClim

Always document:
- Provider
- Dataset name
- Dataset version
- Spatial resolution
- Temporal resolution
- Units
- License
- Acquisition date
- Processing performed

---

## 4. Terrain and geographic data

Useful sources:

- USGS
- Copernicus DEM
- OpenStreetMap
- NASA Earth observation products
- SoilGrids

Potential variables:

- Elevation
- Slope
- Aspect
- Land cover
- Water bodies
- Roads
- Buildings
- Soil properties

---

## 5. Remote sensing

Learn:

- Sentinel-1
- Sentinel-2
- Landsat
- MODIS
- NDVI
- Land Surface Temperature
- Soil moisture products

Useful tools:

- Google Earth Engine
- QGIS
- Rasterio
- xarray

---

## 6. Machine learning

Start with:

- Scikit-learn
- Random Forest
- Gradient Boosting
- XGBoost

Later:

- PyTorch
- LSTM
- Transformers
- Spatiotemporal neural networks

For explainability:

- SHAP

For experiment tracking later:

- MLflow

---

## 7. Backend

Recommended:

- FastAPI
- PostgreSQL
- PostGIS

Later if necessary:

- Redis
- Celery
- Docker

Do not add infrastructure merely because a tutorial mentioned it. Every additional service is another thing that can fail at 2 a.m. for reasons that will be described as "configuration."

---

## 8. Visualization

Start with:

- Matplotlib
- Plotly
- QGIS

For interactive maps:

- Leaflet

Later:

- React
- TypeScript
- Map libraries appropriate to the chosen frontend

---

## 9. Development tools

Recommended:

- VS Code
- Ubuntu/WSL
- Git
- GitHub
- Python virtual environments
- Jupyter
- Docker later

---

## 10. Scientific learning

### Meteorology
- Atmospheric dynamics
- Thermodynamics
- Precipitation
- Boundary-layer processes
- Orographic effects

### Climate science
- Climate variability
- Trends
- Extremes
- Seasonality
- Climate datasets

### Hydrology
- Runoff
- Infiltration
- Soil moisture
- Watersheds
- Flood processes

### GIS
- CRS
- Raster/vector analysis
- DEMs
- Spatial statistics

### Statistics
- Regression
- Time series
- Probability
- Uncertainty
- Hypothesis testing

### Machine learning
- Feature engineering
- Cross-validation
- Regression
- Classification
- Forecasting
- Model evaluation

---

## 11. Recommended books

### Statistics / machine learning
An Introduction to Statistical Learning

### Machine learning implementation
Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow — Aurélien Géron

### Meteorology
An Introduction to Dynamic Meteorology — James R. Holton

### Remote sensing
Remote Sensing and Image Interpretation — Lillesand, Kiefer & Chipman

### GIS
GIS Fundamentals — Paul Bolstad

Use books to understand principles and official documentation to implement current tools. Software documentation ages much more quickly than textbooks.
