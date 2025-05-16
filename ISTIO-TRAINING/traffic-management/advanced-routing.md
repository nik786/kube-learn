

Advanced Routing
-----------------

- Beyond weight-based traffic routing , Istio allows granular control using request properties
- Matching Criteria can include
     - URI Prefix
     - Request Method
     - Headers
     - Authority header
 

Matching Methods
------------------

ISTIO Supports different ways to match requests

| Property   | Description |
|------------|-------------|
| `uri`      | Match the request URI to the specified value |
| `schema`   | Match the request schema (HTTP, HTTPS, ...) |
| `method`   | Match the request method (GET, POST, ...) |
| `authority`| Match the request authority header |
| `headers`  | Match the request headers. Headers have to be lower-case and separated by hyphens (e.g. `x-my-request-id`). **Note:** If headers are used for matching, other properties (`uri`, `schema`, `method`, `authority`) are ignored |




- Matching Types:
    - Exact match: exact: "value" matches the exact string
    - Prefix match: e.g. prefix: "value" matches the prefix only
    - Regex match: e.g. regex: "value" matches based on the ECMAScript style regex



Example: URI Prefix Matching
------------------------------

Example of routing based on request URI Prefix:

URI: https://dev.example.com/v1/api

```

http:
- match:
  - uri:
      prefix: /v1

```

This rule directs requests starting with /v1 to the specified destination 


Example: Header Based Matching
--------------------------------

Example of matching requets based on a header

```
http:
- match:
  - headers:
      user-agent:
        regex: '.*Firefox.*'

```

Matches requests where the user-agent contains "Firefox"




## Redirecting and Rewriting Requests

Modify Request paths or redirect to different services


Example: URI Rewrite

```yaml
http:
  - match:
    - uri:
        prefix: /v1/api
    rewrite:
      uri: /v2/api
    route:
      - destination:
          host: customers.default.svc.cluster.local
```

Incoming  `/v1/api` requests are rewritten to  `/v2/api` before reaching the service



### Redirecting Requests

Redirect request to different service


```yaml
http:
  - match:
    - headers:
        my-header:
          exact: hello
    redirect:
      uri: /hello
      authority: my-service.default.svc.cluster.local:8000
```
Redirects requests with my-header: hello to another service





## AND and OR Semantics

AND MATCHING
------------

```yaml

http:
  - match:
    - uri:
        prefix: /v1
      headers:
        my-header:
          exact: hello
```

Matches requests where both the URI Prefix is /v1 AND the header my-header is hello


### OR Matching

```yaml

http:
  - match:
    - uri:
        prefix: /v1
  - match:
    - headers:
        my-header:
          exact: hello
```
- Matches if either the URI is /v1 OR the header is hello


Gateway API and HTTP Route
----------------------------

Gateway API is Kubernetes -native standard offering routing like ISTIO Virtual Service
Istio supports both HTTP Route and its own custom resources


```

apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: customers-route
spec:
  parentRefs:
  - name: my-gateway
    kind: Gateway
    namespace: default
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /v1
    - headers:
      - name: user-agent
        value: Firefox
        type: RegularExpression
    backendRefs:
    - name: customers-service
      port: 8080

```

This HTTPRoute example provides similar functionality to what we've seen with Istio VirtualService - matching on path prefixes and headers, then routing to a specific service. Gateway API represents the next evolution in Kubernetes service networking, with Istio gradually adopting and supporting these standardized resources alongside its traditional custom resources.

As you progress in your Istio journey, consider exploring both approaches to understand their benefits in different scenarios.

