| Feature/Aspect                           | Description                                                                                                                                           |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose of `ServiceEntry`**           | Adds external services (or internal non-mesh services) to **Istio’s internal service registry**.                                                     |
| **Service Visibility**                  | Makes these services appear as if they are part of the **Istio service mesh**.                                                                       |
| **Benefit of Registry Inclusion**       | Once in the registry, services can benefit from **traffic routing**, **failure injection**, and **other mesh features** like any other mesh service. |


Here’s an example of a ServiceEntry resource that declares an external 
API (api.external-svc.com) we can access over HTTPS.


apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: external-svc
spec:
  hosts:
    - api.external-svc.com
  ports:
    - number: 443
      name: https
      protocol: TLS
  resolution: DNS
  location: MESH_EXTERNAL
  
  
 | Feature/Aspect                        | Description                                                                                                                                     |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **`hosts` Field Capability**         | Can include **multiple external APIs** or services.                                                                                             |
| **Envoy Host Evaluation**            | Envoy inspects `hosts` based on a **defined hierarchy/order**.                                                                                  |
| **Fallback Mechanism**               | If Envoy **cannot inspect** a host entry (e.g., due to resolution failure or config mismatch), it automatically **moves to the next** in order. |

  
  
| Feature/Aspect                             | Description                                                                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Header Matching**                        | Envoy uses **HTTP `Authority` (HTTP/2)** or **`Host` (HTTP/1.1)** headers, **SNI**, **IP address**, and **port** to inspect traffic.                         |
| **Request Handling Behavior**             | If none of the values can be inspected, Envoy will either **blindly forward** or **drop** the request, depending on Istio's configuration.                  |
| **Purpose of `WorkloadEntry`**            | Defines the **details of a VM-based workload** (e.g., address, ports, labels) for integrating with the mesh.                                                 |
| **VM and ServiceEntry Integration**       | Use `workloadSelector` in `ServiceEntry` to associate VM workloads (defined in `WorkloadEntry`) with the **Istio service registry**.                        |
| **Migration Support**                     | Enables **gradual migration** of **VM workloads to Kubernetes** while maintaining service mesh capabilities.                                                 |
  


For example, let’s say the customers workload is running on two VMs.
Additionally, we already have Pods running in Kubernetes with the app:
customers label

Let’s define the WorkloadEntry resources like this:



```
apiVersion: networking.istio.io/v1alpha3
kind: WorkloadEntry
metadata:
  name: customers-vm-1
spec:
  serviceAccount: customers
  address: 1.0.0.0
  labels:
    app: customers
    instance-id: vm1
    
 apiVersion: networking.istio.io/v1alpha3
kind: WorkloadEntry
metadata:
  name: customers-vm-2
spec:
  serviceAccount: customers
  address: 2.0.0.0
  labels:
    app: customers
    instance-id: vm2

```
    
    
We can now create a ServiceEntry resource that spans both the workloads running 
in Kubernetes as well as the VMs

```
  
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: customers-svc
spec:
  hosts:
  - customers.com
  location: MESH_INTERNAL
  ports:
  - number: 80
    name: http
    protocol: HTTP
  resolution: STATIC
  workloadSelector:
    labels:
      app: customers
  
 ```

 
  
  With MESH_INTERNAL setting in the location field, we say that this service is part of the mesh. 
  This value is typically used in cases when we include workloads on unmanaged infrastructure (VMs). 
  The other value for this field, MESH_EXTERNAL, is used for external services consumed through APIs.
  
  
  The MESH_INTERNAL and MESH_EXTERNAL settings control how sidecars in the mesh attempt to 
  communicate with the workload  
  including whether they’ll use Istio mutual TLS by default.
  
  
    














  
  
