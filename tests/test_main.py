from unittest.mock import patch
from fastapi.testclient import TestClient

from weather_api.main import app


client = TestClient(app)


@patch("weather_api.main.fetch_forecast")
def test_get_forecast_returns_summary(mock_fetch):
    mock_fetch.return_value = {
        "hourly": {
            "temperature_2m": [20.0, 10.0, 30.0],
            "precipitation": [3.0, 1.0, 2.0],
            "windspeed_10m": [15.0, 5.0, 10.0, 20.0],            
        }
    }

    response = client.get(
        "/forecast",
        params = {
            "latitude": -29.68,
            "longitude": -51.13,
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "temperature": {
            "min": 10.0,
            "max": 30.0,
            "average": 20.0,
        },
        "precipitation_total": 6.0,
        "average_wind_speed": 12.5,
    }