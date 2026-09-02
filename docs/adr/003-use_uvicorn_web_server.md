# ADR 0003 — Use UVICORN as ASGI server

## Status

Accepted

## Context

The application requires a way to handle HTTP requests that
integrates with FastAPI web framework. 

An ASGI (Asynchronous Server Gateway Interface) defines a standard 
communication interface between Python web servers and web applications 
that provides support to asychronous events.

Uvicorn is a ASGI server commonly used with FastAPI. It handles network
connections, HTTP protocol communication and invokes the FastAPI
application through the ASGI interface.

FastAPI remains responsible for application-level behavior such as 
routing, request validation, response serialization and HTTP status 
handling.

## Decision

Use Uvicorn as the ASGI server for the FastAPI application.

## Consequences

Positive:
- Commonly used with FastAPI.
- Supports ASGI and asynchronous request handling.
- Simple development workflow and configuration.
- Keeps network server responsibilities separate from 
  application responsibilities.

Negative: 
- Adds an external server dependency.
- Production deployment may require additional configuration.