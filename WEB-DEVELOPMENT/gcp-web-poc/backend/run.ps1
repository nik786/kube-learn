# Backend Development Runner for Windows
# Run this script to start the backend server

Write-Host "Starting Backend Development Server..." -ForegroundColor Cyan
Write-Host ""

# Check if Go is installed
if (!(Get-Command go -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Go is not installed." -ForegroundColor Red
    Write-Host "Please install Go from: https://go.dev/dl/" -ForegroundColor Yellow
    exit 1
}

# Show Go version
Write-Host "Go version: $(go version)" -ForegroundColor Green

# Download dependencies if needed
if (!(Test-Path "go.sum")) {
    Write-Host "Downloading dependencies..." -ForegroundColor Yellow
    go mod download
}

Write-Host ""
Write-Host "Starting server on http://localhost:8080" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

# Run the server
go run main.go

