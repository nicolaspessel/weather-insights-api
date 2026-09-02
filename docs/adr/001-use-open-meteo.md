# ADR 0001 — Use Open-Meteo as weather provider

## Status

Accepted

## Context

The application requires hourly weather data.

For the first version, we want to avoid authentication
and infrastructure unrelated to the learning objective.

## Decision

Use Open-Meteo as the external weather provider.

## Consequences

Positive:
- No API key required.
- Easy local development.
- Hourly forecast available.

Negative:
- Our application becomes dependent on Open-Meteo's
  response format and availability.