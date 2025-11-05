package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
)


// enableCORS sets permissive CORS headers for all responses
func enableCORS(w http.ResponseWriter) {
    w.Header().Set("Access-Control-Allow-Origin", "*")
    w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
    w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Origin, Accept, Authorization")
}

func main() {
    r := gin.Default()

    // Global middleware for CORS
    r.Use(func(c *gin.Context) {
        enableCORS(c.Writer)
        if c.Request.Method == "OPTIONS" {
            c.AbortWithStatus(http.StatusOK)
            return
        }
        c.Next()
    })

    // Health endpoint
    r.GET("/api/fleet-app/v1/health-check", func(c *gin.Context) {
        enableCORS(c.Writer)
        c.JSON(http.StatusOK, gin.H{"message": "service is healthy"})
    })

    // Products endpoint
    r.GET("/api/fleet-app/v1/products", func(c *gin.Context) {
        enableCORS(c.Writer)
        products := []map[string]interface{}{
            {"id": 1, "name": "network cameras", "price": 75000},
            {"id": 2, "name": "4g/5g cameras", "price": 1200},
            {"id": 3, "name": "hd recorders", "price": 2400},
        }
        c.JSON(http.StatusOK, products)
    })

    // Run on all interfaces
    r.Run("0.0.0.0:8080")
}

