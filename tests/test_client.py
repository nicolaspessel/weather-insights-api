import requests
import pytest
from unittest.mock import patch

from weather_api.client import (
    WeatherProviderError,
    fetch_forecast
)


# Substitutes requests.get, used by the client, for mock.get
@patch("weather_api.client.requests.get")
def test_fetch_forecast_response(mock_get):
    expected_data = {
        "hourly": {
            "temperature_2m": [10.0, 20.0],
        }
    }

    # -- Mock configuration

    # Object returned by requests.get()
    mock_response = mock_get.return_value

    # Dictionary returned by mock_response.json
    mock_response.json.return_value = expected_data

    result = fetch_forecast(
        latitude=-29.68,
        longitude=-51.13,
    )

    assert result == expected_data

@patch("weather_api.client.requests.get")
def test_fetch_forecast_sends_correct_parameters(mock_get):
    fetch_forecast(
        latitude=-29.68,
        longitude=-51.13,
    )

    mock_get.assert_called_once_with(
        "https://api.open-meteo.com/v1/forecast",
        params = {
            "latitude": -29.68,
            "longitude": -51.13,
            "hourly": [
                "temperature_2m",
                "precipitation",
                "windspeed_10m",
            ],
            "forecast_days": 1
        },
        timeout = 10,
    )

@patch("weather_api.client.requests.get")
def test_fetch_forecast_raises_provider_error_when_request_fails(mock_get):
    # Injects a RequestException when trying to make a request
    mock_get.side_effect = requests.RequestException()

    with pytest.raises(WeatherProviderError):
        fetch_forecast(
            latitude=-29.68,
            longitude=-51.13,
        )