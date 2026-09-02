# Architecture

## Objective

Consume hourly weather data from Open-Meteo,
transform it into daily summaries and expose those
summaries through our own HTTP API.

## Data flow

User → Our API → Open-Meteo Client → Open-Meteo → API → Weather Service → Transformed response

## Modules

### client.py

Responsible exclusively for communication with Open-Meteo.

It should not contain business rules or weather calculations.

### service.py

Responsible for transforming weather data.

It should not know how HTTP requests to Open-Meteo are made.