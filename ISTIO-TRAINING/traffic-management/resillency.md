

| Feature/Aspect                        | Description                                                                                                                                                 |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition of Resiliency**         | The ability to **maintain an acceptable level of service** in the face of faults.                                                                           |
| **Failure Handling Focus**           | Resiliency is not about avoiding failures, but about **responding effectively** to ensure **no downtime or data loss**.                                     |
| **Goal of Resiliency**               | To return the service to a **fully functional state** after a failure occurs.                                                                               |
| **Key Mechanism: Timeouts & Retries**| Implementing **timeouts** and **retry policies** is essential to making services resilient.                                                                 |
| **`timeout` Field Usage**            | Defines the **maximum duration** for an HTTP request. If exceeded, the **Envoy proxy drops the request** and returns **HTTP 408 (Request Timeout)**.       |
| **Connection Behavior After Timeout**| Even after a timeout, the **connection remains open**, unless **outlier detection** removes the host due to repeated faults.                               |


 
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










