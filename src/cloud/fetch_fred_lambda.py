import os
import requests
from dotenv import load_dotenv

load_dotenv()

def handler(event=None, context=None):
    print("🚀 FRED Lambda triggered")

    api_key = os.getenv("FRED_API_KEY")

    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": "MORTGAGE30US",
        "api_key": api_key,
        "file_type": "json",
        "limit": 5,
        "sort_order": "desc"
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("📊 Latest rates:", data["observations"][:2])

    return data