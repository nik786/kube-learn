
## Fault Injection for Service Resiliency

Fault injection can help improve service resiliency by allowing controlled simulation of failure scenarios. <br>
The following types of fault injection can be applied to HTTP traffic:


| **Fault Type** | **Description**                                                                 | **Purpose**                                                   |
|----------------|----------------------------------------------------------------------------------|---------------------------------------------------------------|
| Delay          | Delay the request before forwarding it to the destination service.              | Emulates a slow network or an overloaded upstream service.     |
| Abort          | Abort the HTTP request and return a specific HTTP error code to the caller.     | Simulates a faulty or unavailable upstream service.            |


Here’s an example of aborting HTTP requests and returning HTTP 404, for 30% of the incoming requests:

```
- route:
  - destination:
      host: customers.default.svc.cluster.local
      subset: v1
  fault:
    abort:
      percentage:
        value: 30
      httpStatus: 404

```
      
      
If we don’t specify the percentage, the Envoy proxy will abort all requests.
the fault injection affects services that use that VirtualService.

It does not affect all consumers of the service.

we can apply an optional delay to the requests using the fixedDelay.

```

- route:
  - destination:
      host: customers.default.svc.cluster.local
      subset: v1
  fault:
    delay:
      percentage:
        value: 5
      fixedDelay: 3s

```
      
  The above setting will apply 3 seconds of delay to 5% of the incoming requests.
  the fault injection will not trigger any retry policies we have set on the routes. 
  if we injected an HTTP 500 error, the retry policy configured to retry on the 
  HTTP 500 will not be triggered.
  
  
  
  
  
      




