# HomeScope Cloud Data Architecture

## Overview
HomeScope is a cloud-style data platform that ingests housing and macroeconomic data to compute affordability metrics.

---

## Architecture Flow

### 1. Data Ingestion Layer
- AWS Lambda (simulated in Python jobs)
- Fetches mortgage rates from FRED API
- Stores data into PostgreSQL (RDS equivalent)

---

### 2. Data Storage Layer
- PostgreSQL database
- Tables:
  - housing_metrics
  - mortgage_rates
  - housing_affordability

---

### 3. Processing Layer
- ETL pipelines using Python (pandas)
- Data cleaning, transformation, and normalization
- Feature engineering (affordability index)

---

### 4. Orchestration Layer
- run_pipeline.py simulates AWS Step Functions
- Sequential execution of ingestion → analytics

---

### 5. Event-Driven Design (Future)
- AWS EventBridge triggers Lambda on schedule
- Fully automated daily ingestion pipeline

---

## Key Metrics
- Affordability Index = income / (rent * 12)
- Mortgage rate trends from FRED API
- ZIP-level housing comparisons

---

## Future Enhancements
- Deploy ingestion as AWS Lambda
- Move database to AWS RDS
- Store raw API responses in S3
- Build dashboard using Streamlit or React