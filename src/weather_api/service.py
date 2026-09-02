def summarize_forecast(data: dict) -> dict:
    hourly_params = data["hourly"]

    temperatures = hourly_params["temperature_2m"]
    precipitation = hourly_params["precipitation"]
    wind_speeds = hourly_params["windspeed_10m"]

    return {
        "temperature": {
            "min": min(temperatures),
            "max": max(temperatures),
            "average": sum(temperatures) / len(temperatures)
        },
        "precipitation_total": sum(precipitation),
        "average_wind_speed": sum(wind_speeds) / len(wind_speeds) 
    }