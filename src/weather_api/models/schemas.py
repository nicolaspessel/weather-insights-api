from typing import Annotated, Literal
from pydantic import BaseModel, Field


HourlyVariables = Literal[
    "temperature_2m",
    "relative_humidity_2m",
    "windspeed_10m",
    "wind_direction_10m",
    "rain",
    "precipitation",
    "precipitation_probability",
    "weather_code",
    "cape"
]

DailyVariables = Literal[
    "temperature_2m_max",
    "temperature_2m_min",
    "temperature_2m_mean",
    "relative_humidity_2m_mean",
    "windspeed_10m_mean",
    "windspeed_10m_domininant",
    "rain_sum",
    "precipitation_sum",
    "precipitation_probability_mean"
    "weather_code",
    "cape_mean"
]

'''
ConfigurationVariables = Literal[
    "forecast_days", # forecast length
    "past_days",
    "start_date",    # time interval
    "end_date",
    "timezone"
]
'''

'''
HourlyAdditionalVariables = Literal[
    "forecast_hours",
    "past_hours",
    "temporal_resolution", 
]
'''



# ──── Forecast models ──────────────────────
class ForecastOptions(BaseModel):
    forecast_days: int = Field(default=7, ge=1, le=16)
    timezone: str = "auto"

    hourly: list[HourlyVariables] | None = None
    daily: list[DailyVariables] | None = None


class ForecastQuery(ForecastOptions):
    latitude: float
    longitude: float


class ForecastLocation(ForecastOptions):
    name: str
    language: str = "English"


class ForecastResponse(BaseModel):
    pass


# ──── Geocoding models ─────────────────────
class LocationQuery(BaseModel):
    name: Annotated[str, Field(min_length=2)]
    language: str = "English"


class Location(BaseModel):
    name: str
    country: str
    latitude: float
    longitude: float
    timezone: str