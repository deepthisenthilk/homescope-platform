# src/core/schema_contract.py

HOUSING_METRICS_COLUMNS = [
    "zip_code",
    "date",
    "median_rent",
    "median_home_price",
    "median_income"
]

MORTGAGE_RATES_COLUMNS = [
    "date",
    "mortgage_rate"
]

AFFORDABILITY_COLUMNS = [
    "zip_code",
    "date",
    "median_rent",
    "median_income",
    "mortgage_rate",
    "affordability_index"
]