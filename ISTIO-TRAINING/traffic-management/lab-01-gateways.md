
## Creating a deployment and exposing it using istio gateway and kubernetes gateway api

- Deploy a hello world application and exposing it using:
      - Istio Gateway
      - Kubernetes Gateway Api
 - Learn different ways to manage ingress traffic in istio


   ## Option 1: Using Istio Gateway

   We will deploy an Istio Gateway resource to handle external traffic.
   The hosts field is set to *, allowing access to the ingress gateway directly via its external IP

```

cat istio-gateway.yaml

   apiVersion: networking.istio.io/v1
   kind: Gateway
   metadata:
     name: istio-gateway
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

kubectl apply -f istio-gateway.yaml

Get the external IP of the ingress gateway:

kubectl get svc -n istio-system istio-ingressgateway




```



## Deploying the Hello World Application


```

apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
  labels:
    app: hello-world
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - image: gcr.io/tetratelabs/hello-world:1.0.0
          imagePullPolicy: Always
          name: svc
          ports:
            - containerPort: 3000
---
kind: Service
apiVersion: v1
metadata:
  name: hello-world
  labels:
    app: hello-world
spec:
  selector:
    app: hello-world
  ports:
    - port: 80
      name: http
      targetPort: 3000

kubectl apply -f hello-world.yaml


```

## Binding the VirtualService to the Gateway

```
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: hello-world
spec:
  hosts:
    - "*"
  gateways:
    - istio-gateway
  http:
    - route:
        - destination:
            host: hello-world.default.svc.cluster.local
            port:
              number: 80



kubectl apply -f vs-hello-world.yaml

curl -v http://$GATEWAY_URL/

```

## Option 2: Using Kubernetes Gateway API


## Creating the Gateway API Resource

```

apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: http-gateway
spec:
  gatewayClassName: istio
  listeners:
    - name: http
      protocol: HTTP
      port: 80
      allowedRoutes:
        namespaces:
          from: All

kubectl apply -f gateway-api.yaml


```


## Creating an HTTPRoute


Unlike Istio's VirtualService, the Kubernetes Gateway API uses an HTTPRoute resource:



```

apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: hello-world-route
spec:
  parentRefs:
    - name: http-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: hello-world
          port: 80

kubectl apply -f http-route.yaml


```

## Accessing the Service in Minikube


If you are running this lab in Minikube, the LoadBalancer service does not automatically assign an external IP. 
Instead, use the following command to get the correct access URL


minikube service http-gateway-istio --url


curl -v http://127.0.0.1:$PORT/


## Cleanup

```

kubectl delete deploy hello-world
kubectl delete service hello-world
kubectl delete vs hello-world
kubectl delete gateway istio-gateway
kubectl delete gateway http-gateway
kubectl delete httproute hello-world-route

```


















































