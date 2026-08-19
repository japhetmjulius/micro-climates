# Execution Playbook

This document is the operational sequence for building the project.

## Rule 1: Build the smallest scientifically useful version first

The first prototype should NOT attempt:
- Global weather prediction
- A giant neural network
- Real-time disaster warnings
- A complete agricultural forecasting system
- A nationwide microclimate map

The first prototype should answer one narrow question reliably.

Recommended first question:

> How do terrain characteristics influence localized temperature and rainfall patterns within a selected study area?

---

# Step 1 — Choose a study area

Select a relatively small area with meaningful terrain variation.

Ideal characteristics:
- Different elevations
- Valleys/ridges
- Multiple land-cover types
- Available historical weather data
- Available DEM
- Available rainfall information

Record the geographic boundary in the project documentation.

---

# Step 2 — Set up the repository

Create:

```text
micro-climate/
├── data/
├── src/
├── notebooks/
├── tests/
├── config/
└── docs/
```

Initialize Git.

Create:
- README.md
- .gitignore
- requirements.txt or pyproject.toml

---

# Step 3 — Build the first data pipeline

Create a Python ingestion script.

Responsibilities:

```text
download/read
    ↓
validate
    ↓
normalize
    ↓
save raw metadata
    ↓
save processed dataset
```

Do not mix data collection and modelling in the same script.

---

# Step 4 — Establish data provenance

For every dataset record:

```text
source
dataset
version
date acquired
coverage
resolution
units
license
processing
```

Create a data catalogue in:

```text
docs/DATA_CATALOGUE.md
```

---

# Step 5 — Perform exploratory analysis

Create notebooks for:

```text
01_data_quality.ipynb
02_weather_analysis.ipynb
03_terrain_analysis.ipynb
04_spatial_analysis.ipynb
```

Questions to answer:

- Where are the observations?
- Are there missing values?
- What are the seasonal patterns?
- Which locations are warmer?
- Which locations receive more rainfall?
- How does elevation correlate with temperature?
- Are there localized anomalies?

---

# Step 6 — Introduce terrain

Obtain a DEM.

Calculate:

- Elevation
- Slope
- Aspect

Join these features to weather observations.

Now your dataset starts becoming:

```text
timestamp
location
temperature
rainfall
humidity
elevation
slope
aspect
```

This is the beginning of the actual microclimate analysis.

---

# Step 7 — Build a first microclimate map

Use statistical methods and/or clustering to identify locations with similar environmental behavior.

Do not call clusters "microclimates" automatically.

First demonstrate that they have persistent and meaningful environmental differences.

---

# Step 8 — Build a baseline model

Example:

```text
temperature = f(elevation, season, location)
```

Start with linear regression.

Evaluate using a held-out time period.

Record:

```text
model
features
training period
test period
MAE
RMSE
R²
```

---

# Step 9 — Improve with machine learning

Try:

1. Random Forest
2. Gradient Boosting
3. XGBoost

Compare every model against the baseline.

Create:

```text
docs/MODEL_RESULTS.md
```

---

# Step 10 — Add uncertainty

Do not report predictions without understanding their limitations.

Record:

- Error
- Confidence/uncertainty where appropriate
- Geographic limitations
- Seasonal limitations
- Data limitations

---

# Step 11 — Add anomaly detection

Compare current observations with historical distributions.

Example:

```text
Current rainfall
        ↓
Historical rainfall distribution
        ↓
Percentile / anomaly
        ↓
Abnormality score
```

---

# Step 12 — Build the first hazard model

Choose ONE hazard.

Flood risk is a sensible candidate because it combines:

- Rainfall
- Terrain
- Slope
- Soil
- Drainage
- Land cover

Do not attempt every hazard simultaneously.

---

# Step 13 — Build a risk engine

The risk engine should combine validated indicators.

Example conceptual structure:

```text
rainfall anomaly
        +
soil saturation
        +
slope
        +
terrain/drainage
        ↓
flood susceptibility
```

Document the assumptions behind the score.

---

# Step 14 — Build an API

Once the scientific pipeline works:

```text
Python analysis
      ↓
FastAPI
      ↓
JSON
      ↓
Dashboard
```

Possible first endpoints:

```text
/weather
/terrain
/microclimates
/predictions
/risks
```

---

# Step 15 — Build the dashboard

First version:

- Map
- Current observations
- Historical chart
- Microclimate zones
- Risk indicator

Do not spend weeks making buttons pretty while the model is still statistically questionable.

---

# Step 16 — Automate

Move from:

```text
human runs script
```

to:

```text
scheduled job
    ↓
data ingestion
    ↓
processing
    ↓
model
    ↓
risk engine
    ↓
API/dashboard
```

---

# Step 17 — Add AI assistance

Only after the scientific pipeline is stable.

Useful functions:

- Explain unusual conditions
- Summarize model outputs
- Compare current conditions with historical events
- Generate research summaries
- Assist natural-language queries

Every AI-generated claim should be grounded in actual system data.

---

# Step 18 — Validate

Perform:

### Temporal validation
Train on past data, test on later data.

### Spatial validation
Test on locations not used during training.

### Event validation
Test against known historical extreme events.

### Baseline comparison
Compare against simple models.

Document failures as carefully as successes.

---

# Step 19 — Research documentation

Maintain:

```text
docs/
├── RESEARCH_QUESTIONS.md
├── DATA_CATALOGUE.md
├── METHODS.md
├── MODEL_RESULTS.md
├── LIMITATIONS.md
└── EXPERIMENT_LOG.md
```

The experiment log should record:

```text
Date
Experiment
Hypothesis
Dataset
Features
Model
Parameters
Result
Conclusion
Next action
```

---

# Step 20 — Deployment

Only after validation consider:

- Cloud hosting
- Automated data pipelines
- Production database
- Public API
- Dashboard hosting
- Monitoring
- Alerts

Operational disaster warnings require additional validation and appropriate institutional oversight.

---

# Definition of done for the first major milestone

The first serious milestone is complete when the system can:

1. Load historical weather data.
2. Load terrain data.
3. Clean and validate the data.
4. Associate terrain features with weather observations.
5. Analyze spatial and temporal patterns.
6. Identify statistically meaningful localized differences.
7. Visualize those differences on a map.
8. Build a baseline prediction model.
9. Evaluate the model on unseen data.
10. Document the complete process so another person can reproduce it.

That is enough for a strong first research prototype.

Do not add AI, mobile apps, fancy dashboards or real-time alerts before these ten things work.
