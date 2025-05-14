
ServiceEntry
----------------

▪ With the `ServiceEntry` resource, we can add additional entries to Istio's internal service registry.

▪ This allows us to make **external services** or **internal services not part of the mesh** appear as if they are part of the service mesh.

▪ Once a service is added to the registry, we can apply **traffic routing**, **failure injection**, and other Istio features to it—just like we would with services already in the mesh.

▪ Here's an example of a `ServiceEntry` that declares an external API (`api.external-svc.com`) accessible over **HTTPS**.


```

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

```

▪ The `hosts` field can contain multiple external APIs. The Envoy sidecar checks these in the following order:

   - HTTP Authority header (in HTTP/2) and Host header (in HTTP/1.1)
   - SNI (Server Name Indication)
   - IP address and port

▪ If Envoy cannot inspect any of these, it moves to the next item in the order. If none can be inspected, it either blindly forwards the request or drops it—depending on the Istio installation configuration.

▪ The `resolution` field determines how service discovery is performed:

   - Use `DNS` for dynamic DNS resolution (e.g., when IPs change frequently)
   - Use `STATIC` for services with fixed IP addresses

▪ The `exportTo` field controls the **visibility** of the resource across namespaces:

   - By default, resources are exported to all namespaces (`*`)
   - To limit visibility, set `exportTo` to a list of namespaces (e.g., `[ "foo", "bar" ]`) or use `.` to restrict it to the **same namespace**

▪ The `WorkloadEntry` resource allows Istio to manage **VM workloads** as part of the mesh:

   - You specify details like name, address, and labels for the VM
   - Then, use the `workloadSelector` field in the `ServiceEntry` to associate VMs with services in the mesh

▪ For example, if the **customers** workload runs on two VMs and there are also Kubernetes Pods with the label `app: customers`, you can unify them under the same service entry using these resources.

  
  
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
  
apiVersion: networking.istio.io/v1
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

 
  
▪ The `location` field in a `ServiceEntry` defines whether a service is inside or outside the mesh.

▪ The `MESH_INTERNAL` setting indicates that the service is **part of the mesh**.

▪ `MESH_INTERNAL` is typically used when including workloads running on **unmanaged infrastructure**, such as virtual machines (VMs).

▪ The other value, `MESH_EXTERNAL`, is used for **external services** consumed through public or third-party **APIs**.

▪ The `MESH_INTERNAL` and `MESH_EXTERNAL` settings affect how **sidecars** communicate with the workloads, including whether **Istio mutual TLS** will be used by default.



Note: When applying Istio configurations, keep in mind that objects in the istio-system namespace act as global defaults and are applied across all namespaces. Namespace-specific configurations take precedence over global ones. This is particularly important for resources like Sidecar, where namespace-specific configurations can override global defaults.

  
  
    














  
  
