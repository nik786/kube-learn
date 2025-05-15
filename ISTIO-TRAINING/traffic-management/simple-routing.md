

# Simple Routing 

- **VirtualService** is used to define traffic routing within the Istio service mesh.
- Enables fine-grained control over how requests are directed to services.
- Can be used for:
  - Traffic shifting  
  - Canary releases  
  - A/B testing



Gateway API
-------------------

Usecase:
---------

- Consider two versions of the `customers` application:
  - `customers-v1`
  - `customers-v2`

- Pods have the following labels:
  - `version: v1`
  - `version: v2`

- Traffic split:
  - 70% to `v1`
  - 30% to `v2`

  

Gateway Api Example
---------------------

. Use HTTP Route to define traffic rules in the gateway API
. Weight based backend references split traffic across services




```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: customers-route
spec:
  parentRefs:
  - name: example-gateway
    namespace: default
  hostnames:
  - "customers.default.svc.cluster.local"
  rules:
  - backendRefs:
    - name: customers-v1
      port: 80
      weight: 70
    - name: customers-v2
      port: 80
      weight: 30

```

The HTTPRoute directs traffic based on the specified weights to our two backend services. 
The weights determine what percentage of traffic goes to each service, with the total adding up to 100.




VirtualService
---------------

We can also use the VirtualService resource for traffic routing within the Istio service mesh. With a VirtualService, we can define traffic routing rules and apply them when the client 
tries to connect to the service.



The following configuration routes traffic b/w versions: 

```
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers-route
spec:
  hosts:
  - customers.default.svc.cluster.local
  http:
  - route:
    - destination:
        host: customers.default.svc.cluster.local
        subset: v1
      weight: 70
    - destination:
        host: customers.default.svc.cluster.local
        subset: v2
      weight: 30


```

Under the hosts field, we specify the host name for this VirtualService. The host name can be any string value, typically it's set to the full host name the VirtualService routes the traffic to or, when attached to a Gateway, an actual host name we want to expose the Kubernetes service from. A more detailed explanation of the hosts field matching is at the end of this module. We'll use the customers.default.svc.cluster.local host name in this example.


The following field is http, and this field contains an ordered list of route rules for HTTP traffic. The destination refers to a service in the service registry and the destination to which the request will be sent after processing the routing rule. The Istio's service registry contains all Kubernetes services and any services declared with the ServiceEntry resource.

We are also setting the weight on each of the destinations. The weight equals the proportion of the traffic sent to each of the subsets. The sum of all weight should be 100. If we have a single destination, the weight is assumed to be 100.




Binding VirtualService to Gateway
---------------------------------

The gateways field attaches virtualservices to an istio gateway


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




The above YAML binds the customers-route VirtualService to the gateway named my-gateway. 
Adding the gateway name to the gateways list in the VirtualService exposes 
the destination routes through the gateway.

When a VirtualService is attached to a Gateway, only the hosts defined in the Gateway resource will be allowed. The following table explains how the hosts field in a Gateway resource acts as a filter and the hosts field in the VirtualService as a match.





## Gateway and VirtualService Hosts Matching Behavior

| **Gateway Hosts**                        | **VirtualService Hosts**                                  | **Behavior**                                                                                                                                                         |
|------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `*`                                      | `customers.default.svc.cluster.local`                      | Traffic is sent through to the `VirtualService` as `*` allows all hosts.                                                                                            |
| `customers.default.svc.cluster.local`    | `customers.default.svc.cluster.local`                      | Traffic is sent through as the hosts match.                                                                                                                          |
| `hello.default.svc.cluster.local`        | `customers.default.svc.cluster.local`                      | Does not work, hosts don’t match.                                                                                                                                    |
| `hello.default.svc.cluster.local`        | `["hello.default.svc.cluster.local", "customers.default.svc.cluster.local"]` | Only `hello.default.svc.cluster.local` is allowed. It will never allow `customers.default.svc.cluster.local` through the gateway. However, this is still valid if the `VirtualService` is also attached to a second `Gateway` that allows it. |

 
   
   
   
    








