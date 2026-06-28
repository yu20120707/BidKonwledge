#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
cd "$REPO_ROOT"

PYTHON_BIN=${PYTHON:-python}

echo "Using Python: $PYTHON_BIN"

echo "Running compile check..."
"$PYTHON_BIN" -m compileall backend/app

echo "Running backend tests..."
"$PYTHON_BIN" -m pytest backend/tests

echo "Project checks passed."
