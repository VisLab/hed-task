# setup.ps1 - Initial setup script for hed-task on Windows

Write-Host "Setting up hed-task development environment..." -ForegroundColor Green

# Check if uv is installed
if (!(Get-Command "uv" -ErrorAction SilentlyContinue)) {
    Write-Host "Installing uv..." -ForegroundColor Yellow
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

    # Refresh environment variables
    $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH", "User")
}

Write-Host "uv is available!" -ForegroundColor Green

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
uv sync --all-extras

# Install pre-commit hooks
Write-Host "Installing pre-commit hooks..." -ForegroundColor Yellow
uv run pre-commit install

# Create .env file if it doesn't exist
if (!(Test-Path ".env")) {
    Write-Host "Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
}

Write-Host "Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Activate the virtual environment: .venv\Scripts\activate"
Write-Host "2. Run tests: uv run pytest"
Write-Host "3. Start API server: uv run uvicorn hed_task.api:app --reload"
Write-Host "4. Run CLI: uv run hed-task --help"
Write-Host ""
Write-Host "For more information, see docs/development.md" -ForegroundColor Gray
