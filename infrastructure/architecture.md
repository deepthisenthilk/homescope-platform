# HomeScope Data Platform Architecture

## Overview
HomeScope is a housing intelligence data platform that integrates real estate and macroeconomic data to compute affordability metrics.

---

## Data Sources
- FRED API (mortgage rates)
- CSV housing datasets (Zillow / sample housing data)

---

## Data Ingestion Layer
- Lambda-style Python handlers
- Fetches mortgage rate data from FRED API
- Loads structured data into PostgreSQL

---

## Storage Layer
- PostgreSQL database
- Tables:
  - housing_metrics
  - mortgage_rates
  - housing_affordability (analytics output)

---

## Processing Layer
- ETL pipeline (pandas-based)
- Data cleaning and transformation
- Date normalization and joins

---

## Analytics Layer
- Affordability index calculation:
  income / (rent * 12)
- Cross-dataset joins (housing + macro rates)

---

## Future Improvements
- AWS Lambda deployment
- S3 raw data storage layer
- EventBridge scheduled pipelines
- Dashboard (Streamlit / React)
- API layer (FastAPI)