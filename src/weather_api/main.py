from fastapi import FastAPI, HTTPException, Query
from typing import Annotated

from .models.schemas import (
    Location, 
    LocationQuery, 
    ForecastQuery,
    ForecastLocation
)

from .client import (
    WeatherProviderError,
    fetch_forecast,
    fetch_geocoding
)
from .service import (
    summarize_forecast,
    parse_location
)

app = FastAPI()

@app.get("/forecast")
def get_forecast(params: Annotated[ForecastQuery, Query()]) -> dict:
    try:
        forecast = fetch_forecast(params.latitude, params.longitude, params)
        return summarize_forecast(forecast)

    except WeatherProviderError:
        raise HTTPException(
            status_code=502,
            detail="Could not retrieve weather data.",
        )   


@app.get("/forecast/location")
def get_forecast_by_location(params: Annotated[ForecastLocation, Query()]) -> dict:
    try:
        geocode = fetch_geocoding(params.name, params.language)
        location = parse_location(geocode)

        forecast = fetch_forecast(location.latitude, location.longitude, params)

        return summarize_forecast(forecast)

    except WeatherProviderError:
        raise HTTPException(
            status_code=502,
            detail="Could not retrieve weather data.",
        )


@app.get("/geocoding")
def get_geocoding(params: Annotated[LocationQuery, Query()]) -> Location:
    try:
        geocoding = fetch_geocoding(params.name, params.language)
        return parse_location(geocoding)

    except WeatherProviderError:
        raise HTTPException(
            status_code=502,
            detail="Could not retrieve geocoding data."
        )