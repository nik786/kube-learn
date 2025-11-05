# ---------- Stage 1: Build ----------
FROM golang:1.23 AS builder

WORKDIR /app

# Copy go.mod and download dependencies
COPY go.mod ./
RUN go mod download

# Copy the rest of the source
COPY . .

# Build a statically linked binary
RUN CGO_ENABLED=0 GOOS=linux go build -o backend .

# ---------- Stage 2: Runtime ----------
FROM alpine:3.20

WORKDIR /root/

# Copy the compiled binary
COPY --from=builder /app/backend .

# Expose API port
EXPOSE 8080

# Run the binary
CMD ["./backend"]

