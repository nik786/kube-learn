
## Authentication in Istio

- Authentication verifies identity before allowing access
- In Istio, this means: Can service X access Service Y?
- Key components:
    - Principal: The requesting service
    - Action: The request type(GET,POST)
    - Object: The target service


## Identity in Istio

- Istio uses service accounts as workload identities
- X.509 certificates follow SPIEE(secure production identity framework for everyone)
- Identity is encoded in the Subject Alternate Name(SAN) field

- spiffe://cluster.local/ns/blue/sa/blue-sa


## Authentication in Sidecar and Ambient Modes

## Sidecar Mode

- Envoy Proxies handle authentication per workload
- Mutual TLS handshake verifies identity via the SAN field in certificates


## Ambient Mode

- zTunnel authenticates workloads at the node level.
- TLS handshakes validate identities before forwarding traffic

  
