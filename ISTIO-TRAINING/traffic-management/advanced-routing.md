# Traffic Routing and Request Matching in Istio

## Routing Traffic Using Proportions
Istio allows routing traffic between multiple subsets using the **weight field**. 
In some cases, pure weight-based traffic routing or splitting is sufficient.

Additionally, Istio enables routing based on parts of incoming requests by matching them to defined values. 
For example, you can match the **URI prefix** of incoming requests to route traffic accordingly.

---

## Matching Request Properties

Here are the properties you can use to match incoming requests:

1. **URI**  
   Match the request URI to the specified value.

2. **Schema**  
   Match the request schema (e.g., HTTP, HTTPS).

3. **Method**  
   Match the request method (e.g., GET, POST).

4. **Authority**  
   Match the request authority header.

5. **Headers**  
   Match the request headers. Headers must be lowercase and hyphen-separated.

---

## Matching Methods

Each property can be matched using one of the following methods:

- **Exact Match**  
  Example: `exact: "value"` matches the exact string.

- **Prefix Match**  
  Example: `prefix: "value"` matches the prefix only.

- **Regex Match**  
  Example: `regex: "value"` matches based on ECMAScript-style regex.

---

### Example: Matching URI
If the request URI looks like this:  
`https://dev.example.com/v1/api`

You can match the URI using the following snippet:
```yaml
http:
- match:
  - uri:
      prefix: /v1
```

This configuration matches the incoming request and routes it to the defined destination.

---

### Example: Matching Headers
Here’s how you can match a header using regex:
```yaml
http:
- match:
  - headers:
      user-agent:
        regex: '.*Firefox.*'
```

---

## Redirecting and Rewriting Requests

Matching headers and other request properties is useful, but sometimes you may need 
to rewrite or redirect requests. For example:

### Rewriting URI
Consider a scenario where incoming requests use `/v1/api`, but you want to 
route them to `/v2/api`. You can achieve this using the following configuration:
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

In this case, if the destination service doesn’t listen on `/v1/api`, 
Envoy rewrites the request to `/v2/api`.

---

### Redirecting Requests
You can redirect requests to a completely different service. 
Here’s how to match on a header and redirect:





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
> **Note:**  
> The `redirect` and `destination` fields are mutually exclusive.
> If you use `redirect`, you don’t need to set the `destination`.

---

## AND and OR Semantics

When matching requests, Istio supports both **AND** and **OR** semantics.

### AND Semantics
In the following example, both conditions must be true for the match to succeed:
```yaml
http:
  - match:
    - uri:
        prefix: /v1
      headers:
        my-header:
          exact: hello
```

### OR Semantics
In this example, Istio evaluates the matches sequentially:
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
- If the first match (URI prefix) is successful, the request is routed.
- If the first match fails, Istio evaluates the second match (header).

---

### Default Matching Behavior
If the `match` field is omitted, the route is continually evaluated as `true`.
```yaml
http:
  - route:
      - destination:
          host: default-service.default.svc.cluster.local
```

This configuration matches all requests.
