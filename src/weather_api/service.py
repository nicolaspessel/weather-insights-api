def summarize_forecast(data: dict) -> dict:
    '''
    Summarizes the received data from forecast.
    '''

    hourly_params = data["hourly"]

    temperatures = hourly_params.get("temperature_2m")
    precipitation = hourly_params.get("precipitation")
    wind_speeds = hourly_params.get("windspeed_10m")

    return {
        "temperature": {
            "min": min(temperatures),
            "max": max(temperatures),
            "average": sum(temperatures) / len(temperatures)
        },
        "precipitation_total": sum(precipitation),
        "average_wind_speed": sum(wind_speeds) / len(wind_speeds) 
    }


def retrieve_coordinates(data: dict) -> tuple:
    '''
    Retrieves latitude and longitude from a geocoding dictionary.
    '''

    geo_params = data["results"][0]

    return (
        geo_params["latitude"],
        geo_params["longitude"],
    )


def parse_location(data: dict) -> dict:
    '''
    Parses the location from the received data from geocoding.
    '''

    geo_params = data["results"][0]

    return {
        "name": geo_params["name"],
        "country": geo_params["country"],
        "latitude": geo_params["latitude"],
        "longitude": geo_params["longitude"],
        "timezone": geo_params["timezone"], 
    }