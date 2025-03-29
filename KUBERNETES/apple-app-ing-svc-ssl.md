
```

apiVersion: apps/v1
kind: Deployment
metadata:
  name: apple-app-2048
  labels:
    app.kubernetes.io/name: apple    
spec:
  replicas: 1      
  selector:
    matchLabels:
      app.kubernetes.io/name: apple
  template:
    metadata:
      labels:
        app.kubernetes.io/name: apple
    spec:
      containers:
      - image: hashicorp/http-echo
        name: apple-app
        args:
        - "-text=apple"
        






---

apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: apple
  name: apple-svc
spec:
  ports:
  - port: 5678
    protocol: TCP
    targetPort: 5678
  selector:
    app.kubernetes.io/name: apple
  type: ClusterIP


---

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: apple-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - www.linux.com  # Add the domain here for the TLS configuration
      secretName: my-tls-secret  # Secret that contains the TLS certificate
  rules:
    - host: www.linux.com  # Ensure the domain matches the one for SSL
      http:
        paths:
          - path: /apple
            pathType: Prefix
            backend:
              service:
                name: apple-svc
                port:
                  number: 5678


```
