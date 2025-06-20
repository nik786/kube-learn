
## Observing failure injection and delays in Grafana, Zipkin and Kiali

- Deploy Web Frontend and Customer v1 services
- Inject failures and delays in Istio
- Observe the impact in Grafana, Zipkin and Kiali
  


In this lab, we will deploy the Web Frontend and Customers v1 service. We will then inject a failure, a delay, and observe both in Zipkin, Kiali, and Grafana.

Let's start by deploying the Gateway

```

apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: gateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - '*'

kubectl apply -f gateway.yaml.

```

Next, we will deploy the Web Frontend, Service, and VirtualService

```

 cat web-frontend.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-frontend
  labels:
    app: web-frontend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web-frontend
  template:
    metadata:
      labels:
        app: web-frontend
        version: v1
    spec:
      containers:
        - image: gcr.io/tetratelabs/web-frontend:1.0.0
          name: web
          ports:
            - containerPort: 8080
          env:
            - name: CUSTOMER_SERVICE_URL
              value: 'http://customers.default.svc.cluster.local'
---
kind: Service
apiVersion: v1
metadata:
  name: web-frontend
  labels:
    app: web-frontend
spec:
  selector:
    app: web-frontend
  ports:
    - port: 80
      name: http
      targetPort: 8080
---
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: web-frontend
spec:
  hosts:
    - '*'
  gateways:
    - gateway
  http:
    - route:
        - destination:
            host: web-frontend.default.svc.cluster.local
            port:
              number: 80
```


- Deploy the Customers v1 and related resources.

```

cat customers.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: customers-v1
  labels:
    app: customers
    version: v1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: customers
      version: v1
  template:
    metadata:
      labels:
        app: customers
        version: v1
    spec:
      containers:
        - image: gcr.io/tetratelabs/customers:1.0.0
          name: svc
          ports:
            - containerPort: 3000
---
kind: Service
apiVersion: v1
metadata:
  name: customers
  labels:
    app: customers
spec:
  selector:
    app: customers
  ports:
    - port: 80
      name: http
      targetPort: 3000
---
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: customers
spec:
  host: customers.default.svc.cluster.local
  subsets:
    - name: v1
      labels:
        version: v1
---
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers
spec:
  hosts:
    - 'customers.default.svc.cluster.local'
  http:
    - route:
        - destination:
            host: customers.default.svc.cluster.local
            port:
              number: 80
            subset: v1

kubectl apply -f customers.yaml

```


We will inject the delay in the customers VirtualService


```
cat customers-delay.yaml

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers
spec:
  hosts:
    - 'customers.default.svc.cluster.local'
  http:
    - route:
        - destination:
            host: customers.default.svc.cluster.local
            port:
              number: 80
            subset: v1
      fault:
        delay:
          percentage:
            value: 50
          fixedDelay: 5s

```

To generate some traffic, let's open a separate terminal window and start making requests to the GATEWAY_URL in an endless loop:

```
while true; do curl http://$GATEWAY_URL/; done

```

```
GATEWAY_URL=$(kubectl get svc -n istio-system istio-ingressgateway -ojsonpath='{.status.loadBalancer.ingress[0].ip}')
```


Let's open Grafana from a separate terminal window and observe these delays.

```
istioctl dashboard grafana
```


On the dashboard, make sure to select the customers.default.svc.cluster.local in the Service dropdown and source in the Reporter dropdown.


If you expand the Client Workloads panel, you'll notice the increased duration on the Client Request Duration graph, as shown in the figure below.


Open Zipkin with 

istioctl dashboard zipkin


On the main screen, select the serviceName and web-frontend.default, then add the minDuration criteria and 
enter 5s and click the Run query button to find traces


Click the SHOW button one of the traces to open the details. On the details page, we will notice the duration is 5 seconds



Let's update the VirtualService again, and this time, we will inject a fault and return HTTP 500 for 50% of the requests.




```
cat customers-fault.yaml

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers
spec:
  hosts:
    - 'customers.default.svc.cluster.local'
  http:
    - route:
        - destination:
            host: customers.default.svc.cluster.local
            port:
              number: 80
            subset: v1
      fault:
        abort:
          httpStatus: 500
          percentage:
            value: 50

kubectl apply -f customers-fault.yaml.

```

Just like before, we will start noticing failures from the request loop. If we go back to Grafana and open the 
Istio Service Dashboard (make sure you select source from the Reporter dropdown), 
we will notice the client success rate dropping and the increase in the 500 responses on the Incoming Requests by Source and Response Code graph


There's a similar story in Zipkin. If we search for traces again (we can remove the min duration), 
we will notice the traces with errors will show up in red color, as shown below









Let's also open Kiali (istioctl dash kiali) and look at the service graph by clicking the Graph item

If we click on the web-frontend service and look at the sidebar on the right, you will notice the details of the HTTP requests. 
The graph shows the percentage of success and failures. Both numbers are around 50%, which corresponds to the percentage value we set in the VirtualService.



## Cleanup

```

kubectl delete deploy web-frontend customers-v1
kubectl delete svc customers web-frontend
kubectl delete vs customers web-frontend
kubectl delete dr customers
kubectl delete gateway gateway

```








































































































































