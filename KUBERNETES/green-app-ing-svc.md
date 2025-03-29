Example-01: green-app
-----------------------

```

apiVersion: apps/v1
kind: Deployment
metadata:
  name: green-app
  labels:
    app.kubernetes.io/name: green    
spec:
  replicas: 1      
  selector:
    matchLabels:
      app.kubernetes.io/name: green
  template:
    metadata:
      labels:
        app.kubernetes.io/name: green
    spec:
      containers:
      - image: 891377203384.dkr.ecr.us-east-1.amazonaws.com/ag-py:49
        name: green-app
        
        

---

apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: green
  name: green-svc
spec:
  ports:
  - port: 3001
    protocol: TCP
    targetPort: 3001
  selector:
    app.kubernetes.io/name: green
  type: ClusterIP

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: green-ing-03
  annotations:
  
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/group.name: "mygroup"
    alb.ingress.kubernetes.io/load-balancer-name: plato-dev-alb
    alb.ingress.kubernetes.io/subnets: subnet-0f34c7cbfa1474f73,subnet-0da6236ee352eb657
 

spec:
  ingressClassName: alb    
  rules:
    - http:
        paths:
        - path: /fleet-app/v1/health-check
          pathType: Prefix
          backend:
            service:
              name: green-svc
              port:
                number: 3001 
        - path: /book-details
          pathType: Prefix
          backend:
            service:
              name: green-svc
              port:
                number: 3001

```
