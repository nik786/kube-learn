# DestinationRule Subsets

When working with **Istio**, destinations can refer to different subsets of services. 
Each subset typically represents a specific version of the service.

## Example: Subsets for Customer Service

1. **Subsets**  
   - In this example, we define two subsets: `v1` and `v2`.
   - These subsets correspond to two different versions of the **Customer Service**.

2. **Subset Selection**  
   - Each subset uses a combination of key-value pairs (labels) to determine which Pods to include.

## Declaring Subsets

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

The **DestinationRule** allows us to define various traffic management settings, 
such as load balancing configuration, connection pool size, outlier detection, and more. 
These settings are defined under the `trafficPolicy` field.  

## Key Traffic Policy Settings

1. **Load Balancer Settings**  
2. **Connection Pool Settings**  
3. **Outlier Detection**  
4. **Client TLS Settings**  
5. **Port Traffic Policy**

---

## 1. Load Balancer Settings

With load balancer settings, we can control which load balancer algorithm is used for the destination.

### Example: Simple Load Balancer Configuration

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

We can configure hash-based load balancing using HTTP headers, cookies, or other request properties.

#### Example: Session Affinity Using a Cookie

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

Connection pool settings control the volume of connections at both the TCP and HTTP levels. 
These settings can limit concurrent requests or connections.  

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

Outlier detection implements circuit breaking to monitor the status of upstream hosts (Pods). 
If a host starts returning errors, it can be ejected from the load balancing pool temporarily.  

### Example: Outlier Detection Configuration

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

These settings define TLS-related configurations for connections to the upstream service.  

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

Using the `portLevelSettings` field, traffic policies can be applied to individual ports.

### Example: Per-Port Traffic Policy Configuration

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

---

This structured approach to **DestinationRule Traffic Policies** provides fine-grained
control over service behavior, ensuring optimized traffic management in the **Istio** service mesh.
    

        
   
  
