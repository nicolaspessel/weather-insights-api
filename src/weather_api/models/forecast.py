from datetime import date
from typing import Literal
from pydantic import BaseModel, Field, model_validator


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

TemperatureUnit = Literal["celsius", "fahrenheit"]

WindSpeedUnit = Literal["kmh", "ms", "mph", "kn"]

PrecipitationUnit = Literal["mm", "inch"]

TimeFormat = Literal["iso8601", "unixtime"]


class ForecastOptions(BaseModel):
    hourly: list[HourlyVariables] | None = None
    daily: list[DailyVariables] | None = None

    timezone: str = "auto"
    temperature_unit: TemperatureUnit = None
    wind_speed_unit: WindSpeedUnit = None
    precipitation_unit: PrecipitationUnit = None
    timeformat: TimeFormat = None

    forecast_days: int | None = Field(default=7, ge=1, le=16)
    past_days: int | None = Field(default=0, ge=0, le=92)

    forecast_hours: int | None = Field(default=None, ge=1, le=24)
    past_hours: int | None = Field(default=None, ge=1, le=24)

    start_date: date | None = None
    end_date: date | None = None


    @model_validator(mode="after")
    def validate_time_range(self):
        has_start = self.start_date is not None
        has_end = self.end_date is not None

        if has_start != has_end:
            raise ValueError("start_date and end_date must be provided together.")
        
        if has_start and has_end and self.start_date > self.end_date:
            raise ValueError("start_date must be before or equal to end_date.")

        day_mode = (
            self.forecast_days is not None
            or self.past_hours is not None
        )        

        hour_mode = (
            self.forecast_hours is not None
            or self.past_hours is not None
        )

        date_mode = has_start and has_end

        if sum((day_mode, hour_mode, date_mode)) > 1:
            raise ValueError("Choose only one time range mode: days, hours or dates.")

        return self


class ForecastQuery(ForecastOptions):
    latitude: float
    longitude: float


class ForecastLocation(ForecastOptions):
    name: str
    language: str = "english"


class ForecastResponse(BaseModel):
    pass