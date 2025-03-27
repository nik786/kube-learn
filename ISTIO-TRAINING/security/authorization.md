

## Istio AuthorizationPolicy Overview

| Section | Description |
|---------|-------------|
| **Purpose** | Defines access control rules for workloads in the mesh using the `AuthorizationPolicy` resource. |
| **Function** | Answers: “Can user A send a GET request to the path /hello to service A?” |
| **Policy Scope** | Policies can be applied at mesh, namespace, or workload level. |
| **Supported Actions** | `ALLOW`, `DENY`, `AUDIT`, `CUSTOM` — decides what to do when a request matches the policy. |
| **Runtime Behavior** | Envoy proxy evaluates request context against policies and responds with ALLOW or DENY. |
| **Enforcement** | No extra setup is needed; defining an `AuthorizationPolicy` enables enforcement automatically. |
| **Integration** | Works with principals from `PeerAuthentication` and `RequestAuthentication`. |

---

## AuthorizationPolicy Components

| Field | Role |
|-------|------|
| **selector** | Selects workloads the policy applies to using `matchLabels`. |
| **action** | Specifies the action to take: `ALLOW`, `DENY`, or `AUDIT`. |
| **rules** | Defines conditions under which to apply the specified action. |

---

## Rules Structure

| Field | Meaning |
|-------|---------|
| **from** | Defines the source of the request (who can make the request). |
| **to** | Defines what operation is being performed (e.g., method, path). |
| **when** | Additional conditions the request must meet (e.g., headers, IPs). |

---

## Sample AuthorizationPolicy Breakdown

```yaml

apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
 name: customers-deny
 namespace: default
spec:
 selector:
   matchLabels:
     app: customers
     version: v2
 action: DENY
 rules:
 - from:
   - source:
       notNamespaces: ["default"]


```










| **Field**   | **Description** |
|-------------|-----------------|
| `selector`  | Uses `matchLabels` to select the workloads the policy applies to. In this case: `app: customers` and `version: v2`. |
| `action`    | Defines the action to take. Set to `DENY` in this example. |
| `rules`     | Contains the specific rules for matching requests. Each rule can have `from`, `to`, and `when` fields. |

### Example Rule Breakdown

| **Rule Section** | **Explanation** |
|------------------|-----------------|
| `from` | Specifies the source of the request. In this example: `notNamespaces: ["default"]`, meaning deny requests coming from outside the default namespace. |
| `to` | Specifies operations on the workload. Example: `methods: ["GET"]` – only applies to GET requests. |
| `when` | Specifies additional conditions the request must meet. Example: `request.headers[User-Agent] = Mozilla/*` – applies when the User-Agent header matches this pattern. |

### Summary

This policy denies **GET** requests to **customers v2** workloads if:
- The request **originates outside** the `default` namespace.
- The **User-Agent** header matches `Mozilla/*`.



       
```

apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
 name: customers-deny
 namespace: default
spec:
 selector:
   matchLabels:
     app: customers
     version: v2
 action: DENY
 rules:
 - from:
   - source:
       notNamespaces: ["default"]
 - to:
    - operation:
        methods: ["GET"]
 - when:
    - key: request.headers[User-Agent]
      values: ["Mozilla/*"]
 

```


### Expanded Use of `to` and `when` in Istio AuthorizationPolicy

| **Field**       | **Description** |
|-----------------|-----------------|
| `to`            | Defines **what actions** the policy applies to (e.g., HTTP methods, ports, paths, etc.) |
| `from`          | Defines **who** can take those actions (e.g., source namespace, IP, principal, etc.) |
| `when`          | Defines **conditions** or **properties** each request must meet (e.g., specific header values, source IPs, etc.) |
| `selector`      | Specifies **which workloads** the policy is applied to, using label selectors |

### Example Translation

| **Rule Logic** | **Explanation** |
|----------------|-----------------|
| `DENY` action | Denies GET requests to `customer v2` workloads |
| `from` field | Requests coming **from outside** the `default` namespace |
| `to` field | Specifies the operation – only `GET` method |
| `when` field | Condition – only if `User-Agent` header **matches `Mozilla/*` regex** |

### Policy Evaluation Order

| **Evaluation Step** | **Behavior** |
|---------------------|--------------|
| 1. Matching DENY policies | If any DENY policy matches, **deny the request** |
| 2. No ALLOW policies | If no ALLOW policies are defined, **allow the request** |
| 3. Matching ALLOW policy | If any ALLOW policy matches, **allow the request** |
| 4. No match in ALLOW | If no ALLOW policy matches, **deny the request** |

---

### Operations under `to` Field

| **Operation** | **Description** |
|---------------|-----------------|
| `hosts` / `notHosts` | Match or exclude based on request **hostnames** |
| `ports` / `notPorts` | Match or exclude based on **port numbers** |
| `methods` / `notMethods` | Match or exclude based on **HTTP methods** |
| `paths` / `notPaths` | Match or exclude based on **URL paths** |

> 💡 **AND semantic** is applied when multiple operations are specified.

Example:
```yaml
to:
  - operation:
      methods: ["GET"]
      paths: ["/api/*", "/admin"]
      ports: ["8080"]



The second part of a condition is the values or the notValues list of strings. 
Here’s a snippet of a when condition:

...
 - when:
    - key: source.ip
      notValues: ["10.0.1.1"]



### Sources in Istio AuthorizationPolicy

| **Field**           | **Example**                            | **Description** |
|---------------------|----------------------------------------|-----------------|
| `principals`        | `["my-service-account"]`               | Matches **any workload** using the specified **service account** |
| `notPrincipals`     | `["my-service-account"]`               | Matches **any workload except** the one using the specified service account |
| `requestPrincipals` | `["my-issuer/hello"]`                  | Matches workloads with a **valid JWT** and the specified **request principal** |
| `namespaces`        | `["default"]`                          | Matches any workload coming from the **`default` namespace** |
| `notNamespaces`     | `["default"]` *(in previous example)*  | Matches any workload **not in** the `default` namespace |
| `ipBlocks`          | `["1.2.3.4", "9.8.7.6/15"]`             | Matches any workload with **IP address `1.2.3.4`** or **any IP in CIDR `9.8.7.6/15`** |

> 🔹 You can mix and match these fields under the `from` block in an `AuthorizationPolicy`.

Example usage:
```yaml
from:
  - source:
      notNamespaces: ["default"]
      principals: ["cluster.local/ns/foo/sa/my-service-account"]
      ipBlocks: ["1.2.3.4"]


     
      
