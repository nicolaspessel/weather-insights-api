from fastapi import FastAPI, HTTPException

from .client import (
    WeatherProviderError,
    fetch_forecast,
    fetch_geocoding,
)
from .service import (
    summarize_forecast,
    parse_location,
    retrieve_coordinates,
)

app = FastAPI()


@app.get("/forecast")
def get_forecast(latitude: float, longitude: float) -> dict:
    try:
        forecast = fetch_forecast(latitude, longitude)
        return summarize_forecast(forecast)

    except WeatherProviderError:
        raise HTTPException(
            status_code=502,
            detail="Could not retrieve weather data.",
        )


@app.get("/forecast/location")
def get_forecast(name: str, language: str) -> dict:
    try:
        geocoding = fetch_geocoding(name, language)
        latitude, longitude = retrieve_coordinates(geocoding)

        forecast = fetch_forecast(latitude, longitude)

        return summarize_forecast(forecast)

    except WeatherProviderError:
        raise HTTPException(
            status_code=502,
            detail="Could not retrieve weather data.",
        )


@app.get("/geocoding")
def get_geocoding(name: str, language: str) -> dict:
    try:
        geocoding = fetch_geocoding(name, language)
        return parse_location(geocoding)

    except WeatherProviderError:
        raise HTTPException(
            status_code=502,
            detail="Could not retrieve geocoding data."
        )