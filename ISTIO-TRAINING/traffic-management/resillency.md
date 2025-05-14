

Resiliency
-----------

▪ **Resiliency** ensures service availability even during failures.

▪ Istio provides resiliency through the following features:

   - **Timeouts**
   - **Retry Policies**
   - **Circuit Breaking**
   - **Outlier Detection**

▪ These features help prevent **cascading failures** and improve **overall system stability**.






Timeouts
------------------------------

1. Set limits on how long a request should wait before failing.
2. Prevents slow requests from consuming resources indefinitely.
3. Example timeout configuration:



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

1. Retries failed requests based on conditions
2. Prevents transient faliure from causing downtime
3. Example retry policy:

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



Circuit Breaking 
--------------------------------------------

1. Limits the number of requests a service can handle
2. Prevents overloading unhealthy services
3. Example circuit breaking configuration:



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


```





Outlier Detection
----------------------

1. Detect failing instances and temporarily removes them from load balancing
2. Eaxmple outlier detection configuration





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




If a service returns 5 consecutive 5xx errors, it will be ejected for 30 seconds.
The system checks for failures every 10 seconds.

Circuit breaking ensures that failed instances are temporarily removed from the loadbalancing pool, allowing healthy instances to handle traffic.


Resiliency in Ambient Mode
--------------------------

Istio Ambient Mode handles resiliency at different layers
 1. ztunnel(L4) manages timeouts and retries at the transport layer
 2. waypoint proxies (L7) manage HTTP based retry policies and circuit breaking
 3. Ensures resiliency without requiring sidecars









