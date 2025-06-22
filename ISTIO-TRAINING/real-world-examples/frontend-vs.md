

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: frontend-ingress
spec:
  hosts:
    - '*'
  gateways:
    - frontend-gateway
  http:
  - route:
    - destination:
        host: frontend
        port:
          number: 80
        subset: original
