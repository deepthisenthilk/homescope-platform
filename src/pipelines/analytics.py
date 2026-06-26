import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://homescope_user:homescope_pass@localhost:5432/homescope"
)


def build_affordability_table():
    print("📊 Loading clean warehouse tables...")

    housing = pd.read_sql("SELECT * FROM housing_metrics", engine)
    rates = pd.read_sql("SELECT * FROM mortgage_rates", engine)

    # normalize
    housing["date"] = pd.to_datetime(housing["date"])
    rates["date"] = pd.to_datetime(rates["date"])

    # IMPORTANT: rates is global time series → no duplication
    rates = rates.drop_duplicates(subset=["date"]).sort_values("date")

    # JOIN ONLY HERE (analytics layer responsibility)
    merged = housing.merge(
        rates,
        on="date",
        how="left"
    )

    # forward fill rates (time series continuity)
    merged["mortgage_rate"] = merged["mortgage_rate"].ffill()

    # feature engineering
    merged["affordability_index"] = (
        merged["median_income"] / (merged["median_rent"] * 12)
    )

    # final dataset
    result = merged[
        [
            "zip_code",
            "date",
            "median_rent",
            "median_home_price",
            "median_income",
            "mortgage_rate",
            "rent_burden_ratio",
            "affordability_index"
        ]
    ]

    # persist derived table
    result.to_sql(
        "housing_affordability",
        engine,
        if_exists="replace",
        index=False
    )

    print("💾 Affordability table built successfully")
    return result


if __name__ == "__main__":
    build_affordability_table()