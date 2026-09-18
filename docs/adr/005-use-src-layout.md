# ADR 0005 — Use a packaged src layout

## Status

Accepted

## Context

The application's Python source code needs a predictable import structure
that behaves consistently when running the application tests and 
development tools.

Keeping source code directly importable from the root repository 
can allow imports to succeed because of the current working directory, 
even when the project has not been properly instaled.

The project also needs clear separation between repository files
and the Python package that represents the application.

## Decision

Organize the Python source code using a src layout:

    src/
    └── weather_api/
        ├── __init__.py
        ├── main.py
        ├── client.py
        └── service.py

`weather_api` is the application importable Python package.
`src` is only the source root and must not appear is application
imports.

The projct will use setuptools as its build backend and package 
discovery will search inside `src`.

Because a build system is declared, uv will install the project in 
the project environment. During developmetn, the installation will 
remain editable so source changes are immediately available wihout 
reinstalling the package.

Imports outside the package should use:
    
    from weather_api.main import app

Internal modules may use relative paths such as:

    from .client import fetch_forecast

## Consequences

Positive: 
- Imports do not depended on executing Python from a particular 
directory.
- Tests and the running application use the same installed package.
- The environment more closely resembles how an installed Python
package behaves.
- Editable installation preserves a fast development workflow.

Negative: 
- The project must be corrected installed or synchronized before 
imports work.
- The packaging configuration introduces concepts such as build 
backends and package discovery.
- Direct execution of files within the package may no longer be the
appropriate way to run the application module.