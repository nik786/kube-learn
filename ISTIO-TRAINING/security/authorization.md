
## Understanding Authorisation in Istio
- Determines who can access what within the mesh
- Uses Authorisation Policy to enforce access control
- Applies to sidecar mode(Envoy Proxies and Ambientmode(ztunnel and waypointproxies)



| **Feature**     | **Sidecar Mode (Envoy)**       | **Ambient Mode (ztunnel and waypoint)**                   |
|-----------------|--------------------------------|------------------------------------------------------------|
| **Enforcement** | L4 & L7 (Envoy proxy)          | L4 (ztunnel), L7 (waypoint proxy)                         |
| **Policy Scope**| Workload level                 | Node-level (ztunnel), Service-level (waypoint)            |
| **L7 Control**  | Available                      | Requires waypoint proxy                                   |




## Defining an Authorisation Policy

- Example: Allow GET requests to the customer service from the default namespace

```

apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: allow-customers-get
  namespace: default
spec:
  selector:
    matchLabels:
      app: customers
  action: ALLOW
  rules:
  - from:
    - source:
        namespaces: ["default"]
    to:
    - operation:
        methods: ["GET"]

```


## Policy Evaluation Order

 - CUSTOM Policies: Evaluated first; if any deny the request, it is denied.
 - DENY Policies: If any match the request, it is denied.
 - ALLOW Policies: If none exist for the workload, the request is allowed by default.
 - Default Deny: If no policies match, the request is denied.


## Source Matching in Authorisation Policies

| **Source**           | **Example**                               | **Explanation**                                                                 |
|-----------------------|-------------------------------------------|---------------------------------------------------------------------------------|
| **principals**        | `principals: ["my-service-account"]`      | Any workload using `my-service-account`                                        |
| **notPrincipals**     | `notPrincipals: ["my-service-account"]`   | Any workload except `my-service-account`                                       |
| **requestPrincipals** | `requestPrincipals: ["my-issuer/hello"]`  | Any workload with a valid JWT and request principal `my-issuer/hello`          |
| **notRequestPrincipals** | `notRequestPrincipals: ["*"]`          | Any workload without a request principal (only valid JWT tokens)               |
| **namespaces**        | `namespaces: ["default"]`                 | Any workload from the `default` namespace                                      |
| **notNamespaces**     | `notNamespaces: ["prod"]`                 | Any workload not in the `prod` namespace                                       |
| **ipBlocks**          | `ipBlocks: ["1.2.3.4", "9.8.7.6/15"]`     | Any workload with the IP address `1.2.3.4` or an IP address from the CIDR block |
| **notIpBlock**        | `notIpBlock: ["1.2.3.4/24"]`              | Any IP address that’s outside of the CIDR block                                |



## Defining Allowed Operations

- Hosts: Match destination host(hosts: ["example.com"])
- Methods: Match HTTP methods(methods: ["POST"])
- Paths: Match request paths(paths: ["/api/*"])

  Example:
```
  rules:
    - to:
       - operations:
           methods: ["POST"]
           paths: ["/admin"]

```



## Using Conditions in Authorisation Policies

- Conditions allow granular access control by evaluating request attributes
- Example: Deny access to traffic from 10.0.1.1

```
- when
  - key: source.ip
    notValues: ["10.0.1.1"]

```

         




  











