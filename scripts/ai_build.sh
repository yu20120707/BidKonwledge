#!/usr/bin/env sh
set -eu

cat <<'EOF'
Placeholder: replace scripts/ai_build.sh with this project's real build commands.

Guidance:
- This is a Python/FastAPI backend project.
- Keep dependency installation outside this script.
- Once Phase 1 creates packaging files, this script should run import/build checks only.
- Keep debug and release paths distinct.
- Do not install dependencies here.
- Do not modify business source code here.

Example shape only, not a default:
  python -m compileall backend/app
  python -m pip check
EOF
