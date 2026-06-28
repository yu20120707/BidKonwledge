$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$bundledPython = "C:\Users\26561\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if ($env:PYTHON) {
    $python = $env:PYTHON
} elseif (Test-Path $bundledPython) {
    $python = $bundledPython
} else {
    $python = "python"
}

Write-Host "Using Python: $python"

Write-Host "Running compile check..."
& $python -m compileall backend/app

Write-Host "Running backend tests..."
& $python -m pytest backend/tests

Write-Host "Project checks passed."
