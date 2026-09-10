import pytest

from weather_api.service import summarize_forecast


def test_summarize_forecast():
    forecast = {
        "hourly": {
            "temperature_2m": [20.0, 10.0, 30.0],
            "precipitation": [3.0, 1.0, 2.0],
            "windspeed_10m": [15.0, 5.0, 10.0, 20.0],            
        }
    }

    result = summarize_forecast(forecast)

    assert result == {
        "temperature": {
            "min": 10.0,
            "max": 30.0,
            "average": 20.0,
        },
        "precipitation_total": 6.0,
        "average_wind_speed": 12.5,
    }

def test_summarize_forecast_with_negative_temperature():
    forecast = {
            "hourly": {
                "temperature_2m": [-5.0, -10.0, 0.0],
                "precipitation": [0.0, 0.0, 0.0],
                "windspeed_10m": [15.0, 5.0, 10.0, 20.0],            
            }
        }
    
    result = summarize_forecast(forecast)

    assert result == {
        "temperature": {
            "min": -10.0,
            "max": 0.0,
            "average": -5.0,
        },
        "precipitation_total": 0.0,
        "average_wind_speed": 12.5,
    }

def test_summarize_forecast_empty_values():
    temperature = {
        "hourly": {
            "temperature_2m": [],
        }
    }

    with pytest.raises(ValueError): 
        summarize_forecast(temperature)

    precipitation = {
        "hourly": {
            "precipitation": [],
        }
    }

    with pytest.raises(ValueError): 
            summarize_forecast(precipitation)

    windspeed = {
        "hourly": {
            "windspeed_10m": [],
        }
    }

    with pytest.raises(ValueError): 
            summarize_forecast(windspeed)