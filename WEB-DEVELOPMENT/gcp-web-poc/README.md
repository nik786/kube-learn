# Fullstack App - React + Go

A containerized fullstack application with React frontend and Go backend.

## Architecture

- **Frontend**: React app running on port 3000
- **Backend**: Go (Gin) API running on port 8080

## Quick Start

### Using Docker Compose (Recommended)

```bash
# Build and start all services
docker-compose up --build

# Or run in background
docker-compose up --build -d
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8080

### Local Development

**Prerequisites:**
- Go 1.23+ installed ([Download](https://go.dev/dl/))
- Node.js 18+ and npm installed

#### Backend
```bash
cd backend
go mod download    # Download dependencies (first time only)
go run main.go     # Start the server on http://localhost:8080
```

Or using Make (if installed):
```bash
cd backend
make run    # or make dev for auto-reload with air
```

#### Frontend
```bash
cd frontend
npm install         # Install dependencies (first time only)
npm start           # Start development server on http://localhost:3000
```

**Note:** The frontend will automatically use `http://localhost:8080` for the backend API via the proxy configured in `package.json`.

## Environment Variables

The application uses build-time and runtime environment variables:

- **Build-time**: `REACT_APP_API_URL` - Sets the API URL in the React build
- **Runtime**: `API_URL` - Used by the Express server proxy

In Docker, these are configured in `docker-compose.yml`. For local development, create a `.env` file in the project root.

## How It Works

1. **Backend** (Go/Gin): Exposes RESTful API endpoints
   - `/health` - Health check endpoint
   - `/products` - Returns a list of products

2. **Frontend** (React): 
   - Fetches data from the backend API
   - Production build served by Express server
   - Express server proxies API requests to the backend container
   - Uses relative URLs that work in both Docker and local development

3. **CORS**: Backend is configured to allow cross-origin requests

### Networking
- **Local**: Frontend uses `http://localhost:8080` (from .env file)

## Stopping the Application

```bash
docker-compose down
```

## Project Structure

```
.
├── backend/
│   ├── main.go          # Go backend with Gin
│   ├── Dockerfile       # Backend container definition
│   └── go.mod          # Go dependencies
├── frontend/
│   ├── src/
│   │   ├── App.js      # Main React component
│   │   ├── api.js      # API client
│   │   └── index.js    # React entry point
│   ├── Dockerfile      # Frontend container definition
│   └── package.json    # Node dependencies
└── docker-compose.yml  # Multi-container orchestration
```

## Troubleshooting

- If the frontend can't connect to backend, check that both containers are running: `docker-compose ps`
- Check logs: `docker-compose logs frontend` or `docker-compose logs backend`
- Rebuild after changes: `docker-compose up --build`

