from src.services.fred_service import fetch_mortgage_rates
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://homescope_user:homescope_pass@localhost:5432/homescope"
)


def run_job():
    print("🚀 INGESTION JOB STARTED")

    data = fetch_mortgage_rates()

    # convert API response → DataFrame
    df = pd.DataFrame(data)[["date", "value"]]
    df.columns = ["date", "mortgage_rate"]

    df["date"] = pd.to_datetime(df["date"])
    df["mortgage_rate"] = df["mortgage_rate"].astype(float)

    print("📊 Preview:")
    print(df.head())

    # write to Postgres
    df.to_sql(
        "mortgage_rates",
        engine,
        if_exists="replace",
        index=False
    )

    print("💾 Ingestion complete → PostgreSQL updated")


if __name__ == "__main__":
    run_job()