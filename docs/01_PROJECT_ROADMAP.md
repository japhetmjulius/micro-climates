# Project Roadmap

## Phase 0 — Project definition

### Objectives
- Define the geographic study area.
- Define the first environmental questions.
- Define measurable outputs.
- Establish data sources.
- Establish a reproducible repository.

### Deliverables
- Project README
- Research questions
- Initial architecture
- Data-source register
- Git repository

### Exit criteria
You can explain exactly what the first prototype is supposed to discover and measure.

---

## Phase 1 — Development environment

### Learn
- Linux/Ubuntu
- Git/GitHub
- Python
- Virtual environments
- VS Code
- Basic testing

### Build
- Python project structure
- Virtual environment
- requirements.txt or pyproject.toml
- Git workflow
- Basic logging

### Exit criteria
A clean machine can clone the repository and reproduce the development environment.

---

## Phase 2 — Data acquisition

### Collect
- Temperature
- Rainfall
- Humidity
- Wind speed/direction
- Pressure
- Elevation
- Land cover
- Soil information
- Satellite observations where useful

### Sources to investigate
- Kenya Meteorological Department
- ECMWF / ERA5
- NASA Earth observation datasets
- ESA Copernicus / Sentinel
- CHIRPS
- GPM
- WorldClim
- SoilGrids
- OpenStreetMap
- Other authoritative regional datasets

### Exit criteria
At least one reliable historical environmental dataset and one geographic dataset can be downloaded, documented and reproduced.

---

## Phase 3 — Data engineering

### Implement
- Data ingestion
- Unit normalization
- Timestamp normalization
- Missing-value handling
- Duplicate detection
- Outlier detection
- Data validation
- Metadata/provenance tracking

### Deliverables
A repeatable pipeline:

```text
raw data → validation → cleaning → processed data
```

### Exit criteria
The same input dataset produces the same processed output when the pipeline is rerun.

---

## Phase 4 — GIS and terrain analysis

### Learn
- Raster/vector data
- CRS
- DEMs
- Slope
- Aspect
- Elevation
- Watersheds
- Land cover
- Spatial interpolation

### Tools
- QGIS
- GeoPandas
- Rasterio
- GDAL
- Shapely
- PostGIS later

### First research question
How strongly do elevation, slope and terrain orientation relate to observed temperature/rainfall differences?

### Exit criteria
A map can display terrain features together with environmental observations.

---

## Phase 5 — Exploratory climate analysis

### Analyze
- Daily/monthly/seasonal trends
- Temperature distributions
- Rainfall distributions
- Humidity patterns
- Extreme events
- Spatial differences
- Temporal anomalies
- Correlations between terrain and weather

### Deliverables
- Reproducible notebooks
- Charts
- Maps
- Statistical summaries
- Research notes

### Exit criteria
You can identify at least one measurable localized environmental pattern and support it with data.

---

## Phase 6 — Microclimate identification

### Goal

Identify zones that exhibit statistically distinguishable environmental behavior.

### Candidate methods
- Clustering
- Classification
- Spatial statistics
- Interpolation
- Regression

### Possible output

```text
Zone A: cooler / wetter / elevated
Zone B: warmer / drier / low elevation
Zone C: high rainfall variability
```

### Exit criteria
The zones are reproducible and have measurable characteristics rather than being arbitrary map colors.

---

## Phase 7 — Baseline prediction

Before machine learning, create simple baselines.

### Examples
- Historical mean
- Seasonal mean
- Linear regression
- Simple time-series models

### Metrics
- MAE
- RMSE
- R²
- Appropriate classification metrics where applicable

### Exit criteria
You have a benchmark against which advanced models can be compared.

---

## Phase 8 — Machine learning

### Start with
- Random Forest
- Gradient Boosting
- XGBoost
- Other interpretable models

### Later
- LSTM
- Temporal CNN
- Transformers
- Spatiotemporal models

### Rules
- Avoid data leakage.
- Use time-aware validation.
- Test geographically separated regions where appropriate.
- Record model versions and parameters.
- Compare every model against the baseline.

### Exit criteria
The ML model demonstrably improves a defined metric over the baseline.

---

## Phase 9 — Hazard and risk analysis

### Candidate hazards
- Flooding
- Drought
- Extreme heat
- Landslide susceptibility
- Agricultural stress
- Extreme rainfall
- Strong winds
- Wildfire-conducive conditions

### Framework

```text
Observed conditions
        ↓
Environmental indicators
        ↓
Hazard probability
        ↓
Potential consequence
        ↓
Risk classification
```

### Exit criteria
The risk engine produces explainable, testable outputs.

---

## Phase 10 — Real-time pipeline

### Build
- Automated data ingestion
- Scheduled processing
- Database
- Model inference
- Risk calculation
- API
- Dashboard
- Alert mechanism

### Candidate technologies
- FastAPI
- PostgreSQL/PostGIS
- Redis
- Docker
- Leaflet
- Plotly

### Exit criteria
New data can enter the system automatically and produce updated analysis without manual processing.

---

## Phase 11 — AI-assisted analysis

### Appropriate AI roles
- Explain model outputs
- Summarize anomalies
- Compare current conditions with historical events
- Generate research hypotheses
- Help query environmental datasets
- Produce human-readable reports

### Avoid
- Allowing an LLM to invent measurements
- Treating generated explanations as scientific evidence
- Allowing AI to override validated models
- Using AI as a substitute for domain expertise

---

## Phase 12 — Research and validation

### Validate against
- Ground observations
- Independent datasets
- Historical events
- Geographic holdout regions
- Alternative models

### Produce
- Technical report
- Dataset documentation
- Model documentation
- Accuracy evaluation
- Limitations
- Reproducibility instructions

### Final objective

A defensible environmental intelligence system whose conclusions can be tested rather than merely demonstrated.
