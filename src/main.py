import requests
from fastapi import FastAPI, HTTPException

from weather_api.client import fetch_forecast
from weather_api.service import summarize_forecast

app = FastAPI()

@app.get("/forecast")
def get_forecast(latitude: float, longitude: float) -> dict:
    try:
        forecast = fetch_forecast(
            latitude=latitude, 
            longitude=longitude,
        )

        return summarize_forecast(forecast)

    except requests.RequestException:
        raise HTTPException(
            status_code=502, # Bad gateway
            detail="Could not retrieve weather data from Open-Meteo.",
        )