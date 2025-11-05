.PHONY: run dev clean

# Run the application
run:
	go run main.go

# Run with auto-reload (requires air: go install github.com/cosmtrek/air@latest)
dev:
	@if command -v air > /dev/null; then \
		air; \
	else \
		echo "Installing air for auto-reload..."; \
		go install github.com/cosmtrek/air@latest; \
		air; \
	fi

# Download dependencies
deps:
	go mod download

# Clean build artifacts
clean:
	go clean
	rm -f backend

# Build binary
build:
	go build -o backend .

# Run the built binary
start:
	./backend
