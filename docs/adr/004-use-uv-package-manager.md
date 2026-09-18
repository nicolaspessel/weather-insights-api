# ADR 0004 — Use uv for Python project and dependency management

## Status

Accepted

## Context

The project requires isolated and reproducible Python environments, 
dependency management and a consistent way to execute development 
commands, regardles of the the IDE.

Previously, dependencies were installed directly with pip into a 
manually created virtual environment. This required separate steps 
to manage the project: creating the environment, installing dependencies 
and keeping the environment synchronized with the project configuration.

As the application grows, development dependencies such as testing tools 
also need to be distinguished from basic runtime dependencies.

uv provides dependency resolution, virtual environment management, 
lockfile generation and command execution  while using the standart 
pyproject.toml project configuration.

## Decision

Use uv as the primary tool for managing project's environment and dependencies.

Dependencies will be declared in pyproject.toml and resolved into uv.lock.

The project environment will be synchronized with `uv sync` and project 
commands should preferably be executed with `uv run`.

uv.lock will be commited to version control, while .venv, holding all
the dependecies itself, will not.

## Consequences

Positive:
- A single tool manages dependency resolution and the project environment.
- Dependencies are declared in pyproject.toml instead of relying 
  on manually installed packages.
- uv.lock provides reproducible dependency resolution.
- The .venv environment can be recreated from project configuration.
- uv automatically installs the packaged project in editable mode
  during development.
- `uv run` provides a constant way to execute commands inside the
  project environment.

Negative: 
- Developers needs to install uv to use the preferred project workflow.
- The project introduces uv.lock as an additional managed file.
- Knowledge of the underlying Python packaging concepts is still 
  necessary even though uv automates many operations.