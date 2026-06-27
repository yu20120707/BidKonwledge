# Python Packaging Guidance

## Environment Discovery

- Inspect `pyproject.toml`, `requirements*.txt`, `setup.cfg`, `setup.py`, `tox.ini`, `noxfile.py`, or project docs before running commands.
- Prefer existing project tooling such as `uv`, `poetry`, `hatch`, `pip-tools`, `tox`, or `nox` when already configured.
- Do not add a package manager or formatter only because it is familiar.

## Dependency Risk

- Treat dependency changes as security, lockfile, and deployment compatibility risk.
- Keep runtime, development, test, and optional dependencies distinct.
- When lockfiles exist, update them consistently with the project convention.

## Verification

- Record the exact environment and command used when running tests or checks.
- Prefer virtual environments such as `venv` or the project-defined tool environment.
