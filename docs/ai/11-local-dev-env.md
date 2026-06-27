# Local Development Environment

## Target Platform

Primary local development platform:

- Windows
- PowerShell
- Python 3.11+
- FastAPI backend
- SQLite metadata store

Future deployment may use Docker/Ubuntu, but Phase 1 should first run locally on Windows.

## Python Runtime

Preferred runtime in this Codex desktop environment:

```powershell
$py = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
```

For normal local development, a project virtual environment is acceptable:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
```

Phase 1 should choose one dependency file:

- `pyproject.toml`, preferred if using modern packaging.
- `requirements.txt`, acceptable for the smallest setup.

Do not introduce both unless there is a specific reason.

## Expected Phase 1 Dependencies

Minimum expected dependencies:

- `fastapi`
- `uvicorn`
- `pydantic`
- `pytest`
- `httpx` for FastAPI test client support if required by the chosen test style

SQLite should use Python standard library `sqlite3` unless an ORM is deliberately chosen later.

## Local Paths

Canonical project name:

```text
BidKnowledge
```

Current local checkout path:

```text
F:\BidKonwledge
```

The local folder name currently contains the historical `Konwledge` spelling. Do not hard-code this absolute path in tests; use the current working directory or configurable settings. Rename the local folder only as a separate repository-maintenance task.

Upload directory:

```text
data/uploads
```

Recommended SQLite file:

```text
data/app.sqlite3
```

These paths must be configurable through a settings module.

## Future Startup Shape

Expected command after Phase 1 implementation:

```powershell
cd F:\BidKonwledge
python -m uvicorn backend.app.main:app --reload
```

The exact command may change if Phase 1 chooses a different Python package layout. README must record the final command.

## Required Scripts

Before claiming development completion, run:

```powershell
.\scripts\ai_check.ps1
```

If shell tooling is available, also run:

```powershell
bash ./scripts/ai_check.sh
```

If one script cannot run on the current machine, record the reason in `.ai/verification.md`.
