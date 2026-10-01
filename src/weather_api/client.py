import requests

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

class WeatherProviderError(Exception):
    pass


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

    try:
        response = requests.get(
            FORECAST_URL, 
            params=params,
            timeout=10.0
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as re:
        raise WeatherProviderError(
            "Could not retrieve weather data from Open-Meteo."
        ) from re


def fetch_geocoding(name: str, language: str):
    params = {
        "name": name, 
        "language": language
    }

    try:
        response = requests.get(
            GEOCODING_URL,
            params=params,
            timeout=10.0
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as re:
        raise WeatherProviderError(
            "Could not retrieve geocoding data from Open-Meteo."
        ) from re