
## Working with VM workloads

- VM workloads can join the Istio service mesh in sidecar mode
- Two key resources for managing workloads
    - WorkloadGroup: Defines common metadata for a group of VMs (like a Kubernetes deployment)
    - Workload Entry: Represents an individual VM instance(similar to a pod)
 

## Single-Network Architecture

- Kubernetes cluster and VMs share the same network(L3 Connectivity)
- VM workloads can reach Istiod and other pods directly by IP
- Control-plane traffic can optionally go through an ingress gateway, but it is not required.
- Auto-registration simplifies the workload of onboarding


  ## Multi-Network Architecture

- VM Workloads reside in a different network from Kubernetes
- Istio east-west gateways bridge communication b/w clusters and VM workloads
- Both control-plane and data-plane traffic flow through the gateway
- The VM must be configured to reach the address of the gateway for Istiod connectivity and mTLS Security


## Representing VM Workloads in Istio

- WorkloadGroup: Defines common metadata, labels, and port information for a group of VM instances.
- Workload Entry: Represents a single VM instance, including its IP and labels
- Kubernetes Service(optional): Enables VMS to share a hostname with Kubernetes services for load balancing.



Here's an example of a WorkloadGroup resource:

```

apiVersion: networking.istio.io/v1
kind: WorkloadGroup
metadata:
  name: customers-workload
  namespace: vm-namespace
spec:
  metadata:
    labels:
      app: customers
  template:
    serviceAccount: customers
    ports:
      http: 8080

```


- Auto-registration creates workload entry when a VM joins the mesh.
- Ensure the VM can reach the Istio gateway for multi-network deployments
