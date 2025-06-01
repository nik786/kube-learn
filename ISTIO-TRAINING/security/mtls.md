
## Mutual TLS(mTLS)

- mTLS ensures encrypted communication b/w services
- Both client and server present certificates for authentication
- Supported in sidecar mode(Envoy proxies) and ambient mode(ztunnel)
- Configured using PeerAuthentication and DestinationRule policies


 | Feature         | Sidecar Mode (Envoy)    | Ambient Mode (Ztunnel)     |
|----------------|--------------------------|-----------------------------|
| TLS Handling   | Per-workload proxy       | Node-level proxy            |
| Identity Check | Verified per request     | Verified at node level      |



## Configuring mTLS with Peer Authentication

- STRICT mTLS (Required for all traffic)


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

PERMISSIVE Mode(Allows Both mTLS and Plaintext)
```

apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: default
  namespace: default
spec:
  mtls:
    mode: PERMISSIVE

```




  
## Controlling TLS With DestinationRule
  

 ```

apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: example-destination
  namespace: default
spec:
  host: example-service.default.svc.cluster.local
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL

```

## TLS Modes in DestinationRule

 - DISABLE: No TLS connection (plaintext traffic allowed)
 - SIMPLE: Uses TLS without client authentication
 - MUTUAL: Uses mutual TLS (mTLS) with manually specified certificates
 - ISTIO_MUTUAL: Uses Istio-generated certificates for mTLS (recommended)




## Enforcing Global mTLS

- To apply STRICT mTLS across the entire service mesh, define a PeerAuthentication policy in the istio-system namespace:


```

apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: global-mtls
  namespace: istio-system
spec:
  mtls:
    mode: STRICT

```

- Applies MTLS across the entire service mesh.
- Ensures all traffic within Istio is encrypted and authenticated.



  
