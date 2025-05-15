

# Simple Routing 

▪ **VirtualService** is used to define traffic routing within the Istio service mesh.  
▪ Enables fine-grained control over how requests are directed to services.  
▪ Can be used for:
  ▪ Traffic shifting  
  ▪ Canary releases  
  ▪ A/B testing





Here’s how the VirtualService resource would look like for the above scenario:

```

apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: customers-route
spec:
  hosts:
  - customers.default.svc.cluster.local
  http:
  - name: customers-v1-routes
    route:
    - destination:
        host: customers.default.svc.cluster.local
        subset: v1
      weight: 70
  - name: customers-v2-routes
    route:
    - destination:
        host: customers.default.svc.cluster.local
        subset: v2
      weight: 30

```

## Traffic Routing Configuration

We want to configure the `VirtualService` to route the traffic to the `v1` version of the application.  
The routing to `v1` should happen for **70%** of the incoming traffic, 
while the remaining **30%** of requests should be sent to the `v2` version of the application.  
This enables gradual traffic shifting and can be useful for testing new versions or performing canary deployments.


## VirtualService Configuration Details

| **Field**     | **Description**                                                                                                                                   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `hosts`       | Defines the destination host. In this case: `customers.default.svc.cluster.local`, which is a Kubernetes service.                                 |
| `http`        | Contains an ordered list of route rules for HTTP traffic. Each rule defines how requests are matched and routed.                                  |
| `destination` | Refers to a service in Istio’s service registry. The request is sent to this service after applying routing rules.                                |
| `service registry` | Includes all Kubernetes services and any external services declared using the `ServiceEntry` resource.                                   |
| `weight`      | Specifies the proportion of traffic to send to each subset. The total weight must equal **100**. A single destination defaults to 100%.           |
| `gateways`    | Used to bind the `VirtualService` to specific gateways. You can define one or more gateway names to associate the `VirtualService` with.         |








With the gateways field, we can also specify the gateway names to which we want to bind this VirtualService. 

```
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: customers-route
spec:
  hosts:
    - customers.default.svc.cluster.local
  gateways:
    - my-gateway
  http:


```

## VirtualService Configuration Details

| **Field**     | **Description**                                                                                                                                   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `hosts`       | Defines the destination host. In this case: `customers.default.svc.cluster.local`, which is a Kubernetes service.                                 |
| `http`        | Contains an ordered list of route rules for HTTP traffic. Each rule defines how requests are matched and routed.                                  |
| `destination` | Refers to a service in Istio’s service registry. The request is sent to this service after applying routing rules.                                |
| `service registry` | Includes all Kubernetes services and any external services declared using the `ServiceEntry` resource.                                   |
| `weight`      | Specifies the proportion of traffic to send to each subset. The total weight must equal **100**. A single destination defaults to 100%.           |
| `gateways`    | Used to bind the `VirtualService` to specific gateways. You can define one or more gateway names to associate the `VirtualService` with.         |






## Gateway and VirtualService Hosts Matching Behavior

| **Gateway Hosts**                        | **VirtualService Hosts**                                  | **Behavior**                                                                                                                                                         |
|------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `*`                                      | `customers.default.svc.cluster.local`                      | Traffic is sent through to the `VirtualService` as `*` allows all hosts.                                                                                            |
| `customers.default.svc.cluster.local`    | `customers.default.svc.cluster.local`                      | Traffic is sent through as the hosts match.                                                                                                                          |
| `hello.default.svc.cluster.local`        | `customers.default.svc.cluster.local`                      | Does not work, hosts don’t match.                                                                                                                                    |
| `hello.default.svc.cluster.local`        | `["hello.default.svc.cluster.local", "customers.default.svc.cluster.local"]` | Only `hello.default.svc.cluster.local` is allowed. It will never allow `customers.default.svc.cluster.local` through the gateway. However, this is still valid if the `VirtualService` is also attached to a second `Gateway` that allows it. |

 
   
   
   
    








