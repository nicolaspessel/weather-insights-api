import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_forecast(latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": [
            "temperature_2m",
            "precipitation",
            "windspeed_10m"
        ],
        "forecast_days": 1,
    }

    response = requests.get(url=BASE_URL, params=params)

    response.raise_for_status()

    return response.json()