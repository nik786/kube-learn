

```

apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: tomcat-ingress
  namespace: nginx-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - host: tomcat.app.com
    http:
      paths:
      - path: /
        backend:
          serviceName: hello-world-svc
          servicePort: 8080

```

