# Backend Service

Go backend API with Gin framework.

## Quick Start

### Prerequisites
- Go 1.23+ installed ([Download](https://go.dev/dl/))

### Running Locally

```bash
# Navigate to backend directory
cd backend

# Download dependencies (first time only)
go mod download

# Run the server
go run main.go
```

The server will start on `http://localhost:8080`

## Using Make (Optional)

If you have `make` installed:

```bash
# Run the server
make run

# Run with auto-reload (requires air)
make dev

# Download dependencies
make deps

# Build binary
make build

# Run the built binary
make start
```

## API Endpoints

- `GET /health` - Health check
- `GET /products` - Get list of products

## Development

The server runs on all interfaces (`0.0.0.0:8080`) so it's accessible from:
- `localhost:8080` (from your machine)
- `0.0.0.0:8080` (from Docker containers)
- `backend:8080` (from other Docker containers in the same network)

## Testing

```bash
# Test health endpoint
curl http://localhost:8080/health

# Test products endpoint
curl http://localhost:8080/products
```

## With Docker

```bash
# Build
docker build -t backend .

# Run
docker run -p 8080:8080 backend
```

## Environment

The backend runs on port `8080` by default. You can change this by modifying `main.go` line 47:
```go
r.Run("0.0.0.0:PORT")
```
