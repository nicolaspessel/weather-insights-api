# Architecture

## Objective

Consume hourly weather data from Open-Meteo,
transform it into daily summaries and expose those
summaries through our own HTTP API.


## Data flow

User → API Endpoint → Open-Meteo Client → Open-Meteo → Weather Service → JSON transformed response


## Python project structure

The project structure uses a packaged `src` layout and uv to manage 
the local development environment.

### Project structure

    weather-insights-api/
    ├── pyproject.toml
    ├── uv.lock
    ├── .venv/
    ├── src/
    │   └── weather_api/
    └── tests/

### Responsibilities

`pyproject.toml`
Declares project dependencies, supported Python versions, runtime 
dependencies, development dependencies and the build system.

`uv.lock`
Stores the dependency versions resolved by uv. It is generated and
managed by uv and commited to the version control.

`.venv`
Contains the actual isolated environment used on the local machine. 
It is generated from the project configuration and should not be commited
to the version control.

`uv`
Resolves dependencies, maintains the lockfile, synchronizes the virtual
environment and executes commands using the project environment.

`setuptools`
Acts as the build backend. It searches for `weather_api` package inside
of `src` and makes it installable.

`src/weather_api`
Contains the application's importable Python package.

### Environment flow

   pyproject.toml
          ↓
         uv
          ↓
       uv.lock
          ↓
       uv sync
          ↓
        .venv
          │
          ├── third-party dependencies
          │
          └── editable weather-insights-api installation
                         ↓
                  src/weather_api

During development, commands should normally be executed using:

    uv run <command>

Examples:

    uv run pytest
    uv run uvicorn weather_api.main:app --reload


## Modules

### main.py

Responsible for expose the internal API endpoints and handle HTTP 
layer operations.

It should not know how the HTTP requests to Open-Meteo are made.

### client.py

Responsible exclusively for communication with Open-Meteo.

It should not contain business rules or weather calculations.

### service.py

Responsible for transforming weather data.

It should not know how HTTP requests to Open-Meteo are made.