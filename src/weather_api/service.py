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


def retrieve_latitude_longitude_from_geocoding(data: dict) -> dict:
    '''
    Searches for the latitude and longitude within a geocoding response.
    '''

    geo_params = data["results"][0]

    latitude = geo_params.get("latitude")
    longitude = geo_params.get("longitude")

    return (
        latitude, 
        longitude
    )


def parse_location(data: dict) -> dict:
    '''
    Parses the location from the received data from geocoding.
    '''

    geo_params = data["results"][0]

    id = geo_params.get("id")
    name = geo_params.get("name")
    country = geo_params.get("country")
    latitude = geo_params.get("latitude")
    longitude = geo_params.get("longitude")
    timezone = geo_params.get("timezone")

    return {
        "id": id,
        "name": name,
        "country": country,
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone
    }