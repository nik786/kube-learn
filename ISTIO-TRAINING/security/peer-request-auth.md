## 🔐 Istio Authentication Overview


## Peer and Request Authentication

- Istio supports peer authentication(service-toservice) and request authentication(end-user authentication)
- Peer authentication enforces mutual TLS for secure service communication
- Request authentication validates end-user credentials via JSON Web Tokens(JWTs)
  

## Peer Authentication (Service-to-Service Authentication)

- Ensures services authenticate each other before communication
- Uses mTLS with SPIFFEE identities
- Configured via PeerAuthentication resource




```

apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: default
  namespace: default
spec:
  mtls:
    mode: STRICT

```

- STRICT mode: Requires mTLS for all traffic
- Permissive mode: Accepts both mTLS and plain-text traffic

mtls:
  mode: PERMISSIVE

  
## Request Authentication(End user Authentication)

- Validates user credentials at the HTTP layer
- Uses JWTS issued by external identity providers
- Configured via Request Authentication resource
- Ensures only authenticated users access services.



```

apiVersion: security.istio.io/v1
kind: RequestAuthentication
metadata:
  name: jwt-auth
  namespace: default
spec:
  jwtRules:
  - issuer: "https://auth.example.com"
    jwksUri: "https://auth.example.com/.well-known/jwks.json"


```


This policy enforces JWT validation for incoming requests, ensuring that only authenticated users can access services.



## Authentication in Sidecar and Ambient Modes

Both Sidecar mode and Ambient mode support PeerAuthentication and RequestAuthentication, but they enforce these policies differently:

- In Sidecar mode, each workload has an Envoy proxy that manages mTLS and JWT validation.
- In Ambient mode, ztunnel handles mTLS at the node level, and Waypoint proxies are required for HTTP-level authentication like JWT validation.





