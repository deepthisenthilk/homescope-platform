import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_mortgage_rates(limit=10):
    api_key = os.getenv("FRED_API_KEY")

    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": "MORTGAGE30US",
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["observations"]