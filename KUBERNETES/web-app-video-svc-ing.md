

```

apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
  name: webapp-video
spec:
  replicas: 1
  selector:
    matchLabels:
      app: webapp-video
  template:
    metadata:
      labels:
        app: webapp-video
    spec:
      containers:
      - image: kodekloud/ecommerce:video
        name: simple-webapp
        ports:
        - containerPort: 8080

---


apiVersion: v1
kind: Service
metadata:
  name: video-service
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    app: webapp-video
  type: ClusterIP



---



apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-watch       
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
    kubernetes.io/ingress.class: nginx
  
spec:
  rules:
  - http:
      paths:
      - backend:
          service:
            name: video-service
            port:
              number: 8080
        path: /watch
        pathType: Prefix

```





```
