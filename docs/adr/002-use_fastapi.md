# ADR 0002 — Use FastApi as web framework

## Status

Accepted

## Context

The application exposes an HTTP API that serves transformed data 
obtained from an external weather provider.

The project requires a web framework that allows HTTP endpoints
to be implemented with little initial configuration while providing
request validation and API documentation.

FastApi is a high used Python framework when building APIs that
supports both synchronous and asynchronous programming, uses Python 
type hints for request validation and generates interactive 
documentation (Swagger UI).   

## Decision

Use FastApi as web framework for the application's HTTP API.

## Consequences

Positive:
- Simple for begginers.
- Automatic request validation based on Python type hints.
- Automatic and interactive API documentation.

Negative:
- FastAPI doesn't provide a built-in ORM or database abstraction,
  requires external libraries.
- Smaller and younger ecosystem when compared to Django