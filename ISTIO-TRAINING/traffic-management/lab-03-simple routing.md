
Simple Traffic Routing

- Deploy web frontend and customers v1 and v2 services
- Route traffic b/w different service versions using virtualservice and destinationarule
- Gradually shift traffic from v1 to v2 using weighted routing



```

cat gateway.yaml

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

kubectl apply -f gateway.yaml

```


Next, we will create the Web Frontend and the Customer service deployments and corresponding Kubernetes services.


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

```

Notice we are setting an environment variable called CUSTOMER_SERVICE_URL that points to the customers service we will deploy next.

The Web Frontend uses that URL to make a call to the Customer service.



That's because we will create the subsets in the DestinationRule, and those will apply 
The additional version label to the selector, allowing us to reach the Pods running specific versions.


```
cat customers-v1.yaml


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


kubectl apply -f customers-v1.yaml


kubectl get pod
NAME                            READY   STATUS    RESTARTS   AGE
customers-v1-7857944975-5lxc8   2/2     Running   0          36s
web-frontend-659f65f49-jz58r    2/2     Running   0          3m38s



```

We can now create a VirtualService for the web-frontend and bind it to the Gateway resource:


```
cat web-frontend-vs.yaml
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

kubectl apply -f web-frontend-vs.yaml

```

```
GATEWAY_URL=$(kubectl get svc -n istio-system istio-ingressgateway -ojsonpath='{.status.loadBalancer.ingress[0].ip}')
```


If we deployed the Customer service version v2, the responses we'd get back when calling the http://customers.default.svc.cluster.local would be random. 
They would either come from the v2 or v1 version of the Customer Service.


We need to create the DestinationRule for the Customers service and define the two subsets, representing v1 and v2 versions. Then, we can create a VirtualService 
and route all traffic to the v1 subset. After that, we can deploy the v2 version of the Customers service without impacting the existing services


Let's start with the DestinationRule and two subsets:


```

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
    - name: v2
      labels:
        version: v2

kubectl apply -f customers-dr.yaml.

```


We can create the VirtualService and specify the v1 subset in the destination:

```

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

```

Save the above YAML to customers-vs.yaml and create the VirtualService using kubectl apply -f customers-vs.yaml


Let's create the Customers v2 deployment. 
We don't need to deploy the Kubernetes Services because we've already deployed one with the v1 version.



```

cat customers-v2.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: customers-v2
  labels:
    app: customers
    version: v2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: customers
      version: v2
  template:
    metadata:
      labels:
        app: customers
        version: v2
    spec:
      containers:
        - image: gcr.io/tetratelabs/customers:2.0.0
          name: svc
          ports:
            - containerPort: 3000


```

The deployment is nearly identical to the v1 deployment. 
The only differences are in the Docker image version used and the v2 value set to the version label.


Because of the VirtualService we created earlier, all traffic will be going to the subset v1. 
Let's use the weight field and modify the VirtualService. We'll send 50% of the traffic to the v1 subset and the other 50% to the v2 subset.




To do that, we will create a second destination with the same hostname but with a different subset. 
We will also add the weight: 50 to destinations to split the traffic between both versions equally



```
cat customers-50-50.yaml


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
          weight: 50
        - destination:
            host: customers.default.svc.cluster.local
            port:
              number: 80
            subset: v2
          weight: 50

kubectl apply -f customers-50-50.yaml.

```

To change the proportion of the traffic sent to one or the other version, we can update the VirtualService. 
Similarly, we could add v3 or v4 versions as well and split the traffic between those version


## Cleanup

```

kubectl delete deploy web-frontend customers-{v1,v2}
kubectl delete svc customers web-frontend
kubectl delete vs customers web-frontend
kubectl delete dr customers
kubectl delete gateway gateway

```













