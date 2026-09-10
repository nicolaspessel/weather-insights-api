from fastapi import FastAPI, HTTPException

from .client import (
    WeatherProviderError,
    fetch_forecast
)
from .service import summarize_forecast


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