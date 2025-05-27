

## Multi-Cluster Deployments

- Multi-Cluster deployments offer higher availability and stronger isolation
- Increased complexity in setup and operations
- High availability typically involves deploying clusters across multiple zones and regions
- A cluster can reside in a single network or span multiple networks


## Network Deployment Models

- Multi-network deployment requires Istio gateways for inter-cluster communication
- Benefits of multiple networks:
    - Better fault tolerance
    - Addressing overlapping IP ranges or address exhaustion
- In a multi-network setup:
    - Pod IPs may not be routable across networks
    - Cross-network traffic relies on east-west gateways

- Configuration options:
   - Istio Gateway + VirtualService + DestinationRule
   - Kubernetes Gateway ApI

 ## Control Plane Deployment Models
  
  - Single Control Plane
      - All clusters share a single Istiod instance
       - Centralised Operations but fewer isolations

  - External Control Plane
      - Managed Istio control plane outside your clusters
      - Simplifies upgrades and certificate management
 
  - Multiple Control planes
      -  Each cluster has its own Istiod instance
      -  Higher availability and regional independence
      -  Optionally supports failover to secondary control Planes



## Mesh Deployment Models

- Single-mesh: All services belong to one logical mesh
- Multi-mesh: Multiple distinct meshes federated together
   - Enables cross-mesh communication with trust relationships
   - Useful for large organisations needing strict isolation
     
- Federated meshes require shared Certificate Authorities and configured policies


## Tenancy Models

- Soft multi-tenancy
   - isolations via namespaces and authorisation policies
   - Same namespace across clusters is treated as one by Istio 

- Strong isolation:
    - Separate meshes per cluster
    - Explicit cross-mesh communication policies 

 

## Best Multi-Cluster Deployment

- Running an Istio control plane in each cluster is the most robust approach
- Benefits:
    - High availability: Cluster failures are isolated
    - Independent configuration and upgrades
    - Clear troubleshooting boundaries
- Use ingress or east-west gateways for cross-cluster traffic
- Avoid direct pod-to-pod connectivity across clusters to reduce complexity.



## Key Takeaways
  - Deploy a full Istiod per cluster for high availability
  - Use a gateway for cross-network/cluster traffic
  - For multi-tenancy, use namespace-based policies or multiple meshes
  














    

    
