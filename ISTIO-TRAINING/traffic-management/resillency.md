

Resiliency
-----------

▪ **Resiliency** ensures service availability even during failures.

▪ Istio provides resiliency through the following features:

   - **Timeouts**
   - **Retry Policies**
   - **Circuit Breaking**
   - **Outlier Detection**

▪ These features help prevent **cascading failures** and improve **overall system stability**.






Timeouts and Retry Policies
------------------------------

A crucial element in making services resilient is defining timeouts and retry policies when making service requests. We can configure both on Istio's VirtualService.

Timeout Configuration
-----------------------

Using the timeout field, we can define a timeout for HTTP requests. If the request takes longer than the value specified in the timeout field, the Envoy proxy will drop the request and return an HTTP 408 (Request Timeout). The connections remain open unless outlier detection is triggered.

Example timeout configuration:
-------------------------------


```

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers-service
  namespace: default
spec:
  hosts:
  - customers.default.svc.cluster.local
  http:
  - route:
    - destination:
        host: customers.default.svc.cluster.local
        subset: v1
    timeout: 10s


```

In this example, requests to customers.default.svc.cluster.local will timeout after 10 seconds if no response is received.


Retry Policy Configuration
--------------------------


In addition to timeouts, Istio allows us to configure retry policies. We can specify the number of retry attempts, the timeout per try, and the conditions for retries. Istio allows retries only for idempotent requests to prevent unintended duplication of requests


Example retry policy:



```

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers-service
  namespace: default
spec:
  hosts:
  - customers.default.svc.cluster.local
  http:
  - route:
    - destination:
        host: customers.default.svc.cluster.local
        subset: v1
    retries:
      attempts: 3
      perTryTimeout: 2s
      retryOn: 5xx,connect-failure,reset

```

This retry policy will:

Attempt up to 3 retries when a failure occurs.
Each retry attempt will timeout after 2 seconds.
Retries will happen for 5xx errors, connection failures, and resets.



Circuit Breaking and Outlier Detection
--------------------------------------------
Istio supports circuit breaking and outlier detection to prevent cascading failures when a service becomes unhealthy or overloaded.


```

apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: customers-destination
spec:
  host: customers.default.svc.cluster.local
  trafficPolicy:
    connectionPool:
      http:
        maxRequestsPerConnection: 1
        maxRetries: 3
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 10s
      baseEjectionTime: 30s

```

This configuration does the following:

Limits 1 request per connection to prevent overloading services.
Allows a maximum of 3 retries per request.
If a service returns 5 consecutive 5xx errors, it will be ejected for 30 seconds.
The system checks for failures every 10 seconds.

Circuit breaking ensures that failed instances are temporarily removed from the load balancing pool, allowing healthy instances to handle traffic.


Resiliency in Ambient Mode
--------------------------

| **Aspect**                     | **Traditional Istio (Sidecar)**                          | **Istio Ambient Mode**                                                                 |
|-------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Resiliency Mechanism**      | Handled by sidecar proxy (Envoy)                         | Split between `ztunnel` (L4) and `waypoint proxy` (L7)                                  |
| **Timeouts & Retries (L4)**   | Handled in Envoy sidecar                                 | Managed by `ztunnel`                                                                   |
| **HTTP Policies (L7)**        | Handled in Envoy sidecar                                 | Require `waypoint proxy` for the specific service                                       |
| **Policy Definition**         | Defined in `VirtualService`                              | Still defined in `VirtualService`                                                      |
| **Enforcement Layer (L4)**    | Handled by sidecar                                       | Enforced at `ztunnel`                                                                  |
| **Enforcement Layer (L7)**    | Handled by sidecar                                       | Enforced at `waypoint proxy`                                                           |
| **Deployment Complexity**     | Sidecar injected per pod                                 | No sidecar; optionally deploy `waypoint proxy` for L7 features                          |
| **Circuit Breaking (L7)**     | Supported in sidecar                                     | Requires `waypoint proxy` for HTTP circuit breaking                                    |





















 
 Here’s an example of setting a timeout for a route:
 
 ```
- route:
  - destination:
      host: customers.default.svc.cluster.local
      subset: v1
  timeout: 10s
```

| Feature/Aspect                            | Description                                                                                                                                                   |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Granular Retry Policy**                | Allows configuring the **number of retries** and **timeout per try** for each request.                                                                        |
| **Client-Side Behavior**                 | Both **retries and timeouts** are handled **on the client-side** by the Envoy proxy.                                                                          |
| **Retry Conditions**                     | Retries occur only if the upstream server returns a **5xx error**.                                                                                            |
| **Custom Retry Conditions**              | You can retry on specific **gateway errors** (`502`, `503`, `504`) or specify **retriable status codes** in the request headers.                             |
| **Failed Endpoint Handling**             | If an endpoint returns a retriable error, it is **excluded from the load balancing pool** during retries.                                                    |
| **Example Scenario**                     | If a service has 3 endpoints and one fails, Envoy will **retry the request on the remaining healthy endpoints**, not the one that previously failed.         |


Here’s an example of how to set a retry policy for a particular destination:

```
- route:
  - destination:
      host: customers.default.svc.cluster.local
      subset: v1
  retries:
    attempts: 10
    perTryTimeout: 2s
    retryOn: connect-failure,reset
```



| Feature/Aspect                           | Description                                                                                                                                                  |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Retry on Connect Failure or Reset**   | Retry attempts are triggered on **connect failures** (e.g., connect-timeout) or if the server does not respond at all (**reset errors**).                    |
| **Per-Try Timeout Configuration**       | If the **per-try attempt timeout** is set to 2 seconds, each individual retry will have a maximum wait time of 2 seconds.                                    |
| **Total Timeout with Retries**          | If both **retries** and **timeouts** are set, the total **timeout value** is the maximum wait time for the request, even if multiple retries are attempted. |
| **Example Timeout Scenario**            | For example, with a **10-second timeout** and **10 retries**, the request will only wait a maximum of 10 seconds, even if retries occur.                   |










