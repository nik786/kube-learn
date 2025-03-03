

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

kubectl create clusterrole node-admin --verb=get,watch,list,create,delete --resource=nodes
kubectl create clusterrolebinding node-admin-binding --clusterrole=node-admin --user=michelle


```
