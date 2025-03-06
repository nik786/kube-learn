

Network-Policy
---------------

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: internal-policy
  
spec:
  podSelector:
    matchLabels:
      name: internal
  policyTypes:
  - Egress
  - Ingress
  ingress:
    - {}
  egress:
  - to:
    - podSelector:
        matchLabels:
          name: mysql
    ports:
    - port: 3306
      protocol: TCP
  - to:
    - podSelector:
        matchLabels:
          name: payroll
    ports:
     - port: 8080
       protocol: TCP
  - ports:
    - port: 53
      protocol: TCP
    - port: 53
      protocol: UDP

```

```

kubectl create clusterrole node-admin --verb=get,watch,list,create,delete --resource=nodes
kubectl create clusterrolebinding node-admin-binding --clusterrole=node-admin --user=michelle


kubectl create clusterrolebinding michelle-storage-admin -
-clusterrole=storage-admin --user=michellereate clusterrole storage-admin --verb=get,list,watch,create --resource=persistentvolumes,storageclasses


```



```

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
  generation: 1
  name: ingress-wear-watch
  namespace: app-space
spec:
  rules:
  - http:
      paths:
      - backend:
          service:
            name: wear-service
            port:
              number: 8080
        path: /wear
        pathType: Prefix
      - backend:
          service:
            name: video-service
            port:
              number: 8080
        path: /stream
        pathType: Prefix

          
      - backend:
          service:
            name: food-service
            port:
              number: 8080
        path: /eat
        pathType: Prefix

```


