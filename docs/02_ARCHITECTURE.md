# System Architecture

## 1. High-level architecture

```text
                  ┌──────────────────────┐
                  │ Environmental Data   │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Data Ingestion       │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Quality Control      │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Storage              │
                  │ PostgreSQL/PostGIS   │
                  │ Files/Object Storage │
                  └──────────┬───────────┘
                             ↓
              ┌──────────────┴──────────────┐
              ↓                             ↓
      Geospatial Analysis            Time-series Analysis
              │                             │
              └──────────────┬──────────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Feature Engineering  │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Baseline Models      │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ ML / Forecast Models │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Risk Engine          │
                  └──────────┬───────────┘
                             ↓
                    ┌────────┴────────┐
                    ↓                 ↓
                 REST API          Research
                    ↓              outputs
              Dashboard
                    ↓
                 Alerts
```

## 2. Data layer

### Raw data

Never modify original downloaded datasets.

```text
data/raw/
```

Store them with source and acquisition metadata.

### Processed data

Cleaned, standardized datasets belong in:

```text
data/processed/
```

### External/reference data

Static geographic and reference datasets:

```text
data/external/
```

---

## 3. Suggested database entities

### locations

```text
location_id
latitude
longitude
elevation
geometry
```

### weather_observations

```text
observation_id
location_id
timestamp
temperature
humidity
pressure
rainfall
wind_speed
wind_direction
source
quality_flag
```

### terrain_features

```text
location_id
elevation
slope
aspect
ruggedness
land_cover
soil_type
```

### model_predictions

```text
prediction_id
model_version
location_id
prediction_time
target_time
variable
prediction
uncertainty
```

### risk_assessments

```text
assessment_id
location_id
timestamp
hazard
probability
severity
risk_level
model_version
```

---

## 4. Model architecture

Every model should have:

```text
Input data
    ↓
Feature engineering
    ↓
Model
    ↓
Prediction
    ↓
Uncertainty / confidence
    ↓
Evaluation
```

Models must be versioned.

Example:

```text
temperature_model_v001
temperature_model_v002
temperature_model_v003
```

---

## 5. API architecture

Potential endpoints:

```text
GET /locations
GET /weather
GET /terrain
GET /microclimates
GET /predictions
GET /risks
GET /alerts
```

Later:

```text
POST /analysis
POST /forecast
```

The API should never expose raw database internals unnecessarily.

---

## 6. Frontend

The dashboard should eventually provide:

- Interactive map
- Time slider
- Weather observations
- Microclimate zones
- Terrain layers
- Historical comparisons
- Forecasts
- Risk levels
- Model confidence
- Data source information

Recommended initial mapping stack:

```text
Leaflet + OpenStreetMap
```

---

## 7. AI layer

AI should sit above the validated scientific outputs.

```text
Validated environmental data
        ↓
Validated model
        ↓
Validated risk result
        ↓
AI explanation
```

Not:

```text
Raw data → LLM → "trust me bro"
```

The AI layer should never be the source of scientific measurements.
