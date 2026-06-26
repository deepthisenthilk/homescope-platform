import os
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def fetch_mortgage_rates():
    print("📡 Fetching FRED mortgage rates...")

    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": "MORTGAGE30US",
        "api_key": os.getenv("FRED_API_KEY"),
        "file_type": "json",
        "limit": 12,
        "sort_order": "desc"
    }

    r = requests.get(url, params=params)
    data = r.json()

    df = pd.DataFrame(data["observations"])
    df = df[["date", "value"]]
    df.columns = ["date", "mortgage_rate"]

    df["mortgage_rate"] = pd.to_numeric(df["mortgage_rate"], errors="coerce")

    print("✅ FRED data loaded")
    print(df.head())

    load_to_postgres(df)

    return df


def load_to_postgres(df):
    engine = create_engine(
        "postgresql://homescope_user:homescope_pass@localhost:5432/homescope"
    )

    df.to_sql(
        "mortgage_rates",
        engine,
        if_exists="append",
        index=False
    )

    print("💾 Data loaded into PostgreSQL")