import requests

from .models.schemas import ForecastOptions

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

class WeatherProviderError(Exception):
    pass


def fetch_forecast(latitude: float, longitude: float, options: ForecastOptions) -> dict:
    params = {
        "forecast_days": options.forecast_days,
        "timezone": options.timezone,

        "latitude": latitude,
        "longitude": longitude,
        
        "hourly": options.hourly,
        "daily": options.daily
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