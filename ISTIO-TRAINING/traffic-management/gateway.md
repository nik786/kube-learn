
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



The Ingress gateway we deployed as part of the demo Istio installation created a Kubernetes service with the 
LoadBalancer type that gets an external IP assigned to it, for example:


kubectl get svc -n istio-system



Using the egress gateway allows us to centralize all outgoing traffic, logging, and authorization.
