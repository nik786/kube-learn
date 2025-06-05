

  


## Exposing Services Using Gateway Resource

  - Ingress Gateway: Handles inbound traffic to the cluster
  - Egress Gateway: Manages outbound traffic leaving the cluster
  - Both gateways use Envoy proxies as load balancers at the edge of the mesh




## Istio Gateway vs Kubernetes Gateway API



| Feature                        | Istio Gateway                           | Kubernetes Gateway API                      |
|-------------------------------|-----------------------------------------|---------------------------------------------|
| **Origin**                    | Istio-specific custom resource          | Kubernetes standard (SIG Network project)   |
| **Purpose**                   | Manage ingress/egress in Istio          | Flexible, role-based traffic routing        |
| **Resource Type**             | `Gateway` (Istio CRD)                   | `Gateway`, `HTTPRoute`, etc. (K8s API)      |
| **Standardization**           | Istio-specific implementation           | Vendor-neutral, community-driven standard   |
| **Adoption in Istio**         | Traditional/default approach            | Now supported by Istio as an alternative    |
| **Flexibility**               | Less modular                            | More modular and extensible                 |
| **Separation of Concerns**    | Limited                                 | Encourages role-based separation (e.g., infra vs app) |



## Istio Gateway Resource

  - Defines exposed ports,protocols and certficates for envoy proxies
  - Example configurations:

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




## Kubernetes Gateway API with Istio


- The Kubernetes Gateway API is an advanced alternative to the traditional Ingress and Istio Gateway resources. 
- Requires Gateway API CRDS Installations

```
  kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.2.1" | kubectl apply -f -; }

```

## Example Kubernetes Gateway Resources:


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




## Attaching Routes to Kubernetes Gateway

- Uses HTTP Route instead of Virtual Service
- Example Configuration:

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


- This configuration routes /hello requests to hello-service on port 8080. 
- Kubernetes Gateway API provides a more modular and extensible approach to managing traffic policies in a service mesh.




## Understanding Load Balancer Behaviour

- Ingress Gateway creates a Kubernetes Loadbalancer service
- Example service status: 



```
kubectl get svc -n istio-system
NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)                                                                      AGE
istio-egressgateway    ClusterIP      10.0.146.214   <none>           80/TCP,443/TCP,15443/TCP                                                     7m56s
istio-ingressgateway   LoadBalancer   10.0.98.7      XX.XXX.XXX.XXX   15021:31395/TCP,80:32542/TCP,443:31347/TCP,31400:32663/TCP,15443:31525/TCP   7m56s
istiod                 ClusterIP      10.0.66.251    <none>           15010/TCP,15012/TCP,443/TCP,15014/TCP,853/TCP                                8m6s

```



## Egress Gateway

- Controls outbound traffic leaving the mesh
- Enforces logging, security policies and access control.
- Example configuration:

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


## Deploying Gateways
-----------------------

# Install with default profile (includes ingress gateway)
- istioctl install --set profile=default

# Install with demo profile (includes both ingress and egress gateways)
- istioctl install --set profile=demo

## Using Helm
--------------


# Install Istio base chart
- helm install istio-base istio/base -n istio-system

# Install istiod chart
- helm install istiod istio/istiod -n istio-system --wait

# Install ingress gateway
- helm install istio-ingress istio/gateway -n istio-system

# Install egress gateway
- helm install istio-egress istio/gateway \
  -n istio-system \
  --set service.type=ClusterIP \
  --set labels.app=istio-egress \
  --set labels.istio=egressgateway









- [gateways](https://academy.tetrate.io/courses/take/istio-fundamentals/lessons/19067696-4-1-gateways)

