import pandas as pd
from sqlalchemy import create_engine

print("Starting ETL pipeline...")

from src.config.db import get_db_url
from sqlalchemy import create_engine

engine = create_engine(get_db_url())

print("📥 Loading CSV...")
df = pd.read_csv("data/raw/sample_data.csv")
print("📊 Data loaded:")
print(df.head())

print("🔄 Transforming data...")
df["date"] = pd.to_datetime(df["date"])
df["rent_burden_ratio"] = df["median_rent"] / df["median_income"]
df["affordability_index"] = df["median_income"] / df["median_home_price"]

print("💾 Writing to PostgreSQL...")
df.to_sql(
    "housing_metrics",
    engine,
    if_exists="append",
    index=False
)

print("DONE — ETL completed successfully")