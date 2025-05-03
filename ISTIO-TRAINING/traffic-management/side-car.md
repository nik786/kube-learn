


| Feature/Aspect                                | Description                                                                                                                                      |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose of Sidecar Resource**               | Describes the configuration of sidecar proxies.                                                                                                  |
| **Default Behavior**                          | All proxies in the mesh can reach every workload and accept traffic on all ports.                                                               |
| **Inbound Traffic Control**                   | Configures the set of ports/protocols that the proxy accepts when forwarding traffic.                                                           |
| **Outbound Traffic Restriction**              | You can restrict which services the proxy can reach when forwarding outbound traffic.                                                           |
| **Nature of Restriction**                     | Restriction is only in configuration; it does **not** act as a security boundary.                                                               |
| **Bypassing Restriction**                     | Services are still reachable; Istio simply doesn't propagate configuration for unlisted services to the proxy.                                  |



Below is an example of a sidecar proxy resource in the foo namespace
configures all workloads in that namespace to only see the workloads in the same namespace
and workloads in the istio-system namespace

```

apiVersion:
 networking.istio.io/v1alpha3
kind: Sidecar
metadata:
  name: default
  namespace: foo
spec:
  egress:
    - hosts:
      - "./*"
      - "istio-system/*"


```


      
| Feature/Aspect                        | Description                                                                                                                                              |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Deployment Scope**                 | A Sidecar resource can be deployed to one or more namespaces in the Kubernetes cluster.                                                                 |
| **Sidecar Resource Limit per NS**    | Only **one** Sidecar resource is allowed per namespace **if no workload selector** is defined.                                                          |
| **Components of Sidecar Resource**   | 1. **Workload Selector**<br>2. **Ingress Listener**<br>3. **Egress Listener**                                                                            |
| **Workload Selector Purpose**        | Determines which workloads the Sidecar configuration applies to.                                                                                        |
| **Namespace-wide Control**           | If no workload selector is defined, the configuration applies to **all sidecars** in that namespace.                                                    |
| **Targeted Control**                 | Adding a workload selector allows the Sidecar configuration to apply to **specific workloads** only.                                                    |
| **Example Behavior**                 | If no selector is defined (as in the example), the configuration affects **all proxies** inside the `default` namespace.                                |

 

```
 
apiVersion: networking.istio.io/v1alpha3
kind: Sidecar
metadata:
  name: default-sidecar
  namespace: default
spec:
  egress:
  - hosts:
    - "default/*"
    - "istio-system/*"
    - "staging/*"


```


 | Feature/Aspect                        | Description                                                                                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Egress Section Purpose**           | Specifies which namespaces the proxy can access services in.                                                                                              |
| **Example Egress Configuration**     | Proxies are allowed to access services in the `default`, `istio-system`, and `staging` namespaces.                                                       |
| **WorkloadSelector Usage**           | Limits the Sidecar resource to apply only to specific workloads based on labels.                                                                          |
| **Example WorkloadSelector**         | Setting `workloadSelector` to `version: v1` will apply the configuration **only** to workloads with the label `version: v1`.                             |


 ```
 
apiVersion: networking.istio.io/v1alpha3
kind: Sidecar
metadata:
  name: default-sidecar
  namespace: default
spec:
  workloadSelector:
    labels:
      version: v1
  egress:
  - hosts:
    - "default/*"
    - "istio-system/*"
    - "staging/*"


```
 | Feature/Aspect                          | Description                                                                                                                                      |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ingress Listener Purpose**           | Defines which **inbound traffic** is accepted by the proxy.                                                                                      |
| **Egress Listener Purpose**            | Specifies the properties for **outbound traffic** from the proxy.                                                                                |
| **Ingress Listener Requirement**       | Each ingress listener must define a **port** where it will receive traffic.                                                                     |
| **Default Ingress Endpoint Options**   | The default endpoint can be either a **loopback IP** (e.g., `127.0.0.1`) or a **Unix domain socket**.                                            |



```
  ingress:
  - port:
      number: 3000
      protocol: HTTP
      name: somename
    defaultEndpoint: 127.0.0.1:8080

```


| Feature/Aspect                        | Description                                                                                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ingress Listener Port Example**    | Configures listener to accept traffic on port `3000` and forward it to loopback IP on port `8080` where the service is running.                          |
| **`bind` Field**                     | Specifies the **IP address** or **Unix domain socket** where the proxy listens for incoming traffic.                                                     |
| **`captureMode` Field**              | Determines **how and if** traffic is captured by the proxy (e.g., `NONE`, `DEFAULT`).                                                                    |
| **Egress Listener Fields**           | Similar to ingress listener, with the **additional** field `hosts`.                                                                                      |
| **`hosts` Field Usage**              | Specifies service hosts using the format `namespace/dnsName`, e.g., `myservice.default` or `default/*`.                                                 |
| **Types of Services in `hosts`**     | Services can be from the **mesh registry**, **external services** (defined via `ServiceEntry`), or **virtual services**.                                |



```
egress:
  - port:
      number: 8080
      protocol: HTTP
    hosts:
    - "staging/*"
```


 
 With the YAML above, the sidecar proxies the traffic that’s bound for port 
 8080 for services running in the staging namespace.   
    



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
      
