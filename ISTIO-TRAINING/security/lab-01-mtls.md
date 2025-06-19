
Overview

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
















