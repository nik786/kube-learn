
Subsets and DestinationRule:
------------------------------

- **Subsets** represent different versions of a service in Istio.

- **DestinationRule**:
  - Defines policies for:
    - Routing
    - Load balancing
    - Connection management
  - Helps control service traffic behavior after routing decisions.


Subsets can be declared in a resource type called **DestinationRule**.  

Below is an example configuration for subsets:



```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: customer-service
spec:
  host: customers.default.svc.cluster.local
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2


```

# Traffic Policies in DestinationRule

1. **Load Balancer Settings**  
2. **Connection Pool Settings**  
3. **Outlier Detection**  
4. **Client TLS Settings**  
5. **Port Traffic Policy**

---




## 1. Load Balancer Settings

- Configures load balancing strategy.
- Example: Round Robin load balancing.



```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: customers-destination
spec:
  host: customers.default.svc.cluster.local
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

### Hash-Based Load Balancing with Session Affinity

- Provides Session affinity based on request properties
- Example using cookie for session affinity:



```yaml
trafficPolicy:
  loadBalancer:
    consistentHash:
      httpCookie:
        name: location
        ttl: 4s
```

---

## 2. Connection Pool Settings

- Controls connection limits to upstream service
- Example of limiting concurrent requests


### Example: Limiting Concurrent HTTP2 Requests

```yaml

spec:
  host: myredissrv.prod.svc.cluster.local
  trafficPolicy:
    connectionPool:
      http:
        http2MaxRequests: 50
```

---

## 3. Outlier Detection

- Removes unhealthy instance from loadbalancing pool

- Example configuration




```yaml
trafficPolicy:
  connectionPool:
    http:
      http2MaxRequests: 500
      maxRequestsPerConnection: 10
  outlierDetection:
    consecutiveErrors: 10
    interval: 5m
    baseEjectionTime: 10m
```





- **`http2MaxRequests`**: Maximum concurrent HTTP2 requests.  
- **`maxRequestsPerConnection`**: Maximum requests per connection.  
- **`consecutiveErrors`**: Number of consecutive errors before ejection.  
- **`interval`**: Time interval for scanning hosts.  
- **`baseEjectionTime`**: Duration a host remains ejected.

---

## 4. Client TLS Settings
- Configure TLS for Secure Connections
- Example of mutual tls configuration


### Example: Mutual TLS Configuration

```yaml
trafficPolicy:
  tls:
    mode: MUTUAL
    clientCertificate: /etc/certs/cert.pem
    privateKey: /etc/certs/key.pem
    caCertificates: /etc/certs/ca.pem
```

### Supported TLS Modes:
- **`DISABLE`**: No TLS connection.  
- **`SIMPLE`**: Originate a TLS connection to the upstream endpoint.  
- **`ISTIO_MUTUAL`**: Use Istio-provided certificates for mTLS.

---

## 5. Port Traffic Policy

- Allows defining traffic policies per port
- Example:


```yaml
trafficPolicy:
  portLevelSettings:
  - port:
      number: 80
    loadBalancer:
      simple: LEAST_CONN
  - port:
      number: 8000
    loadBalancer:
      simple: ROUND_ROBIN
```




    

        
   
  
