


Sidecar
------------


▪ Whenever we update resources such as Kubernetes deployments, pods, services, or Istio resources, Istio's control plane (`istiod`) automatically rebuilds the configuration and, by default, pushes the updated configuration to all proxies (data plane) in the cluster.

▪ In large clusters with many resources and frequent updates, this can lead to performance challenges.

▪ To optimize performance and reduce unnecessary configuration propagation, we can use the **Sidecar** resource to limit the scope of configurations that Istio pushes to the proxies.
                              |


Example: Restricting Configuration Scope
------------------------------------------

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

If a new deployment is created in the bar namespace, workloads in foo will not receive any configuration updates related to it. However, updates in foo or istio-system will be applied.

Reducing the number of services a proxy needs to track improves performance in large deployments.


Workload Selector
-------------------

By default, a Sidecar resource applies to all workloads in a namespace. 
However, we can target specific workloads using the workloadSelector field. 
For example, this configuration applies only to workloads labeled with version: v1:


```

apiVersion: networking.istio.io/v1
kind: Sidecar
metadata:
  name: versioned-sidecar
  namespace: default
spec:
  workloadSelector:
    labels:
      version: v1
  egress:
  - hosts:
    - "default/*"
    - "istio-system/*"

```

This is useful for applying different routing configurations based on workload versions.


Ingress and Egress Listeners
------------------------------

A Sidecar resource can define ingress listeners (for inbound traffic) and 
egress listeners (for outbound traffic).


Ingress Listener (Inbound Traffic Control)
------------------------------------------
Each ingress listener specifies:

The port on which the proxy should listen.<br>
The default endpoint where the traffic is forwarded.


```
apiVersion: networking.istio.io/v1
kind: Sidecar
metadata:
  name: ingress-sidecar
  namespace: default
spec:
  ingress:
  - port:
      number: 3000
      protocol: HTTP
      name: somename
    defaultEndpoint: 127.0.0.1:8080

```

This configuration listens on port 3000 and forwards traffic to 127.0.0.1:8080.

Egress Listener (Outbound Traffic Control)
-------------------------------------------

```

apiVersion: networking.istio.io/v1
kind: Sidecar
metadata:
  name: egress-sidecar
  namespace: default
spec:
  egress:
  - port:
      number: 8080
      protocol: HTTP
    hosts:
    - "staging/*


```

This ensures that traffic bound for port 8080 is allowed only to services in the staging namespace.


Best Practices for Sidecar Configuration
------------------------------------------

▪ Use **Sidecar** resources in large clusters to optimize configuration distribution and reduce memory consumption in **Envoy** proxies.  
▪ Restrict **egress traffic** to limit communication scope and improve security.  
▪ Ensure predictable behavior by defining clear **scoping rules**.  
▪ Apply **workload selectors** to fine-tune configuration at a granular level.




      
 
    



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
      
