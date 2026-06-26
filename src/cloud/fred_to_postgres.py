import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    "postgresql://homescope_user:homescope_pass@localhost:5432/homescope"
)


def handler(event=None, context=None):
    print("🚀 Lambda: FRED → PostgreSQL pipeline started")

    api_key = os.getenv("FRED_API_KEY")

    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": "MORTGAGE30US",
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 10,
    }

    response = requests.get(url, params=params)
    data = response.json()

    # -----------------------------
    # Convert to DataFrame
    # -----------------------------
    df = pd.DataFrame(data["observations"])

    df = df[["date", "value"]]
    df.columns = ["date", "mortgage_rate"]

    df["mortgage_rate"] = pd.to_numeric(df["mortgage_rate"])
    df["date"] = pd.to_datetime(df["date"])

    print("📊 Cleaned data preview:")
    print(df.head())

    # -----------------------------
    # Write to PostgreSQL
    # -----------------------------
    df.to_sql(
        "mortgage_rates",
        engine,
        if_exists="replace",
        index=False
    )

    print("💾 Successfully wrote to PostgreSQL")
    return df