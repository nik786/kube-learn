
- [gateways](https://academy.tetrate.io/courses/take/istio-fundamentals/lessons/19067696-4-1-gateways)
  


# Exposing Services Using Gateway Resource

| Feature                         | Description                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| Istio Gateways                  | Istio includes **Ingress** and **Egress** gateways, both running Envoy proxy.                            |
| Function of Ingress Gateway     | Handles **inbound connections**; acts as a load balancer at the edge of the mesh.                        |
| Function of Egress Gateway      | Handles **outbound connections** leaving the mesh.                                                       |
| Traffic Routing                 | Ingress gateway allows **route rules** to control traffic entering the cluster.                          |
| External IP                     | A **single external IP** can route to multiple services using **host headers**.                          |
| Gateway Resource Purpose        | Configures exposed **ports, protocols, SNI**, and other settings for the gateway.                        |
| Envoy Listener Configuration    | Controls how Envoy **listens** on network interfaces and which **TLS certificates** it presents.         |


Deploying Gateways
-------------------

Using Istio Profiles


# Install with default profile (includes ingress gateway)
istioctl install --set profile=default

# Install with demo profile (includes both ingress and egress gateways)
istioctl install --set profile=demo

Using Helm
-----------

```
# Install Istio base chart
helm install istio-base istio/base -n istio-system

# Install istiod chart
helm install istiod istio/istiod -n istio-system --wait

# Install ingress gateway
helm install istio-ingress istio/gateway -n istio-system

# Install egress gateway
helm install istio-egress istio/gateway \
  -n istio-system \
  --set service.type=ClusterIP \
  --set labels.app=istio-egress \
  --set labels.istio=egressgateway

```

Istio Gateway vs Kubernetes Gateway API
--------------------------------------------


| Feature                        | Istio Gateway                           | Kubernetes Gateway API                      |
|-------------------------------|-----------------------------------------|---------------------------------------------|
| **Origin**                    | Istio-specific custom resource          | Kubernetes standard (SIG Network project)   |
| **Purpose**                   | Manage ingress/egress in Istio          | Flexible, role-based traffic routing        |
| **Resource Type**             | `Gateway` (Istio CRD)                   | `Gateway`, `HTTPRoute`, etc. (K8s API)      |
| **Standardization**           | Istio-specific implementation           | Vendor-neutral, community-driven standard   |
| **Adoption in Istio**         | Traditional/default approach            | Now supported by Istio as an alternative    |
| **Flexibility**               | Less modular                            | More modular and extensible                 |
| **Separation of Concerns**    | Limited                                 | Encourages role-based separation (e.g., infra vs app) |



Istio Gateway Resource
-----------------------

```
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: my-gateway
  namespace: default
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - dev.example.com
    - test.example.com

```

This configuration exposes port 80 on the Istio ingress gateway 
and allows traffic only for dev.example.com and test.example.com. 
To forward this traffic to internal services, a VirtualService needs to be attached to this Gateway.


Kubernetes Gateway API with Istio
----------------------------------

The Kubernetes Gateway API is an advanced alternative to the traditional Ingress and Istio Gateway resources. 
It introduces a role-based, extensible API that decouples different networking concerns and offers better support for multiple controllers, traffic policies, and advanced routing features.

To use the Kubernetes Gateway API with Istio, you need to install the Gateway API CRDs:

kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.2.1" | kubectl apply -f -; }


  Then, you can define a Gateway resource using the Kubernetes Gateway API:

```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-k8s-gateway
  namespace: default
spec:
  gatewayClassName: istio
  listeners:
  - protocol: HTTP
    port: 80
    allowedRoutes:
      namespaces:
        from: Same

```

This configuration defines a Kubernetes Gateway that listens on port 80 and allows routes only from the same namespace.


Attaching Routes to Kubernetes Gateway
----------------------------------------


Instead of using an Istio VirtualService, in Kubernetes Gateway API, 
we define HTTPRoute to manage traffic routing:

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: my-route
  namespace: default
spec:
  parentRefs:
  - name: my-k8s-gateway
  rules:
  - matches:
    - path:
        type: Prefix
        value: /hello
    backendRefs:
    - name: hello-service
      port: 8080

```


This configuration routes /hello requests to hello-service on port 8080. Kubernetes Gateway API provides a more modular and extensible approach to managing traffic policies in a service mesh.




Understanding Load Balancer Behavior
-------------------------------------

The Ingress Gateway deployed in Istio creates a Kubernetes LoadBalancer service, assigning an external IP for incoming traffic



```
kubectl get svc -n istio-system
NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)                                                                      AGE
istio-egressgateway    ClusterIP      10.0.146.214   <none>           80/TCP,443/TCP,15443/TCP                                                     7m56s
istio-ingressgateway   LoadBalancer   10.0.98.7      XX.XXX.XXX.XXX   15021:31395/TCP,80:32542/TCP,443:31347/TCP,31400:32663/TCP,15443:31525/TCP   7m56s
istiod                 ClusterIP      10.0.66.251    <none>           15010/TCP,15012/TCP,443/TCP,15014/TCP,853/TCP                                8m6s

```

The way a LoadBalancer Kubernetes service works depends on the cluster environment. For cloud-managed clusters (GCP, AWS, Azure), an external load balancer is provisioned. On local clusters like Minikube, minikube tunnel may be required to expose services.

Egress Gateway
---------------

In addition to the Ingress Gateway, Istio also supports Egress Gateway, which controls and filters outbound traffic leaving the mesh. Configuring an Egress Gateway helps centralize outgoing traffic, enforcing logging, authorization, and security policies.

A sample Egress Gateway configuration using the Istio Gateway resource:

```
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: egress-gateway
  namespace: istio-system
spec:
  selector:
    istio: egressgateway
  servers:
  - port:
      number: 443
      name: https
      protocol: HTTPS
    hosts:
    - external-service.com

```

By combining Ingress, Egress, and the new Kubernetes Gateway API, Istio provides a flexible and scalable way to manage service mesh traffic, improving security, observability, and performance across distributed applications.
























  


















```
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: my-gateway
  namespace: default
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - dev.example.com
    - test.example.com

```
    
# Gateway and VirtualService Configuration

| Feature                             | Description                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Load Balancer Exposure              | Gateway configures the **Envoy proxy** to expose **port 80** for ingress traffic.                             |
| Deployment Namespace                | The Istio ingress gateway is deployed in the **istio-system** namespace.                                      |
| Gateway Selector Label              | The ingress gateway uses the label: `istio: ingressgateway`.                                                  |
| Gateway Resource Scope              | Only configures the **load balancer** behavior (e.g., ports, protocols, and hosts).                           |
| Hosts Field in Gateway              | Acts as a **filter**, allowing only traffic destined for `dev.example.com` and `test.example.com`.            |
| VirtualService Requirement          | To forward traffic to internal Kubernetes services, a **VirtualService** must be configured.                  |
| Host Matching in VirtualService     | The VirtualService must match the hostnames (`dev.example.com`, `test.example.com`) defined in the Gateway.   |
| Gateway Attachment to VirtualService| The VirtualService must **attach the Gateway** to route traffic correctly.                                    |




