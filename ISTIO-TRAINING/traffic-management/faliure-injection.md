
## Fault Injection for Service Resiliency

Fault Injection helps test service resiliency
Simulates faliures by injecting:
  Delays to mimic slow network
  Aborts to simulate failed upstream services
Helps validate how applications handle faliures


  


HTTP Request Aborts
---------------------

Aborts simulate upstream service failures
Example: Returning HTTP 404 for 30% of requests


```
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers-service
  namespace: default
spec:
  hosts:
  - "customers.example.com"
  gateways:
  - my-gateway
  http:
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

Notice how the fault injection is configured at the HTTP route level and applies specifically to traffic being routed to the v1 subset of the customers service. This means you can target failure injection to specific routes and destinations within your VirtualService.


HTTP Request Delay
---------------------

Delays simulate slow network or overloaded services
Example: Applying a 3 seconds delay to 5% of requests



```

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers-service
  namespace: default
spec:
  hosts:
  - "customers.example.com"
  gateways:
  - my-gateway
  http:
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

Note that the fault injection will not trigger any retry policies we have set on the routes. For example, if we injected an HTTP 500 error, the retry policy configured to retry on the HTTP 500 will not be triggered


Fault Injection Considerations
--------------------------------

1. Fault only affect traffic defined in the virtualservice
2. Percentage defines the probablity of injection
3. Injected faults do not trigger retry policies



Note: The Gateway API specification, which is the Kubernetes-native successor to Istio's traffic management APIs, does not yet provide these fault injection capabilities. If your application requires this level of traffic control and resiliency testing, Istio's VirtualService remains the recommended approach.


      

  
  
  
  
  
      




