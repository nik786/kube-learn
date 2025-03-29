
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: kibana-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - host: kibana.monitor.in
    http:
      paths:
      - path: /
        backend:
          serviceName: kibana
          servicePort: 80

```
