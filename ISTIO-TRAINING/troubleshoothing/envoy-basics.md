
## Envoy Basics

- Envoy is a high-performance proxy designed for cloud native applications
- It serves as the data plane in Istio
- Understanding Envoy helps with troubleshooting Istio issues.



## Core Concepts:

- Listeners: Named IP and Port where Envoy receives inbound traffic
- Routes: Define how traffic is handled once received by a listener
- Cluster: Logical groups of upstream endpoints
- Endpoints: The actual destination IPs and Ports that receive traffic


  ## How Envoy Works in Istio

  ## Sidecar Mode

  - Each workload has an Envoy proxy injected as a sidecar container
  - Traffic is redirected to the envoy using iptables rules.
  - Traffic flow:
        - Inbound Traffic - Redirected to 0.0.0.0:15006 - Envoy applies policies
        - Outbound Traffic - Redirected to 0.0.0.0:15001 - Envoy routes the request

  - Outbound Traffic Policy:
        - Allow_ANY(default0 - Routes unknown destination through PassthroughCluster
        - Register_Only - Blocks traffic to unknown destinations.


 
 ## Ambient Mode:
 - Removes per-pod sidecars and introduces

     -  Ztunnel(L4) - Secure Tcp traffic and provides transparent mTLS.
     -  Waypoint Proxies(l7) - Enforce policies at the service account level


## Traffic flow Changes:
    - ztunnel intercepts L4 traffic istead of per pod envoy sidecars
    - Waypoint proxies handle HTTP,gRPC, and other l7 requests

 - Envoy listeners on ports 15006 and 15001 are no longer relevant   











     











    
        
