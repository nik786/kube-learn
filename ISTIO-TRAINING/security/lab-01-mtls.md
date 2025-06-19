
## Overview

- Deploy web Frontend (without envoy) and Customer service (with envoy) in istio sidecar mode
- Observe traffic behaviour in Permissive mode
- Enable STRICT mTLS and Analyse the impact
- Test Ambient mode for MTLS enforcement without sidecars


## Steps

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


```

Next, we will create the Web Frontend and the Customer service deployments and related Kubernetes services

kubectl label namespace default istio-injection-


With injection disabled, let’s deploy the web-frontend:


- [web-frontend](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/security/web-frontend.md)


 ```
  kubectl apply -f web-frontend.yaml

  kubectl get po
  NAME                           READY   STATUS    RESTARTS   AGE
  web-frontend-659f65f49-cbhvl   1/1     Running   0          7m31s 

  Let’s enable the automatic injection:

  kubectl label namespace default istio-injection=enabled
  namespace/default labeled
  
```

- [customer-v1](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/security/customer-v1.md)


```
 kubectl get po
NAME                            READY   STATUS    RESTARTS   AGE
customers-v1-7857944975-qrqsz   2/2     Running   0          4m1s
web-frontend-659f65f49-cbhvl    1/1     Running   0          13m

```


If we try and access the web page from the GATEWAY_URL, we will get the web page with the customer service’s response.


Accessing the GATEWAY_URL works because of the permissive mode, where plain text traffic gets sent to the services that don’t have the proxy. 
In this case, the ingress gateway sends plain text traffic to the Web frontend because there’s no proxy.


If we open Kiali with istioctl dash kiali and look at the Graph, you will notice that Kiali detects calls made 
from the ingress gateway to web-frontend. However, the calls made to the customers service are coming from unknown service.


Let’s update the customers VirtualService and attach the gateway to it. Attaching the gateway allows us to make calls directly to the customers service.

```
cat vs-customers-gateway.yaml

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: customers
spec:
  hosts:
    - 'customers.default.svc.cluster.local'
  gateways:
    - gateway
  http:
    - route:
        - destination:
            host: customers.default.svc.cluster.local
            port:
              number: 80

```

update the VirtualService using kubectl apply -f vs-customers-gateway.yaml.


We can now specify the Host header and we’ll be able to send the requests through the ingress gateway (GATEWAY_URL) to the customers service


curl -H "Host: customers.default.svc.cluster.local" http://$GATEWAY_URL;
[{"name":"Jewel Schaefer"},{"name":"Raleigh Larson"},{"name":"Eloise Senger"},{"name":"Moshe Zieme"},{"name":"Filiberto Lubowitz"},{"name":"Ms.Kadin Kling"},{"name":"Jennyfer Bergstrom"},{"name":"Candelario Rutherford"},{"name":"Kenyatta Flatley"},{"name":"Gianni Pouros"}]


To generate some traffic to both the Web frontend and Customers service through the ingress, open the two terminal windows and run one command in each:

// Terminal 1

while true; do curl -H "Host: customers.default.svc.cluster.local" http://$GATEWAY_URL; done


// Terminal 2

while true; do curl http://$GATEWAY_URL; done

Open Kiali and look at the Graph. From the Display dropdown, make sure we check the Security option.



## Enable mTLS in STRICT mode

We expect the calls from the frontend to the customer service to start failing because there’s no proxy injected to do the mTLS communication. 
On the other hand, the calls from the ingress gateway to the customer service will continue working.



```
cat strict-mtls.yaml

apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: default
  namespace: default
spec:
  mtls:
    mode: STRICT

```

create the PeerAuthentication resource

kubectl apply -f strict-mtls.yaml


If we still have the request loop running, we will see the ECONNRESET error message from the web frontend

On the other hand, the requests we’re making directly to the customers service continue to work 
because the customer service has an Envoy proxy running next to it and can do mutual TLS.



If we delete the PeerAuthentication resource deployed earlier (kubectl delete peerauthentication default), 
Istio returns to its default (PERMISSIVE mode), and the errors will disappear.


## Ambient Mode

If we deploy the Web Frontend and Customers service in Ambient Mode, the ztunnel handles mTLS without requiring sidecar injection. To test this


1. Label the namespace for Ambient Mode:

 kubectl label namespace default istio.io/dataplane-mode=ambient

2. Deploy the services as usual (without sidecars).

3. Enable STRICT mTLS

```
 
 apiVersion: security.istio.io/v1
 kind: PeerAuthentication
 metadata:
   name: default
   namespace: default
 spec:
   mtls:
     mode: STRICT
```

kubectl apply -f strict-mtls.yaml


4. Verify traffic:
   mTLS should work automatically for all services because ztunnel encrypts traffic.
   If an L7 policy is required, deploy a waypoint proxy for the namespace


















