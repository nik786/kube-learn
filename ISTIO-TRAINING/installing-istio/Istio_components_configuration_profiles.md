
## Istio Components

  - ControlPlane: istiod manages service discovery, policy enforcement and config distribution
  - DataPlane:   Two modes
      - Sidecar Proxy: Envoy is injected into each pod, handling traffic and security
      - Ambient Mesh: ztunnel for layer 4, optional waypoint proxies for layer 7

   - Gateways:
       - Ingress Gateway: Manages inbound traffic
       - Egress Gateway:  Controls outbound traffic  


## Istio Configuration Profiles

  - default: standard production setup, includes Istiod and ingress gateway
  - minimal: only installs istiod, no gateways
  - demo: Includes the istiod, both gateways and extensive tracing
  - empty: No components, full customisation
  - preview: Experimental features for early adopters
  - remote: used for multi-cluster setups
  - ambient: Installs istiod and ztunnel, with optional waypoint proxies


    
