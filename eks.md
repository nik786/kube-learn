Configure ram User's Access to the Cluster
--------------------------------------------
EKS cluster permissions are typically managed through the Kubernetes Role or ClusterRole bindings in conjunction with aws-auth ConfigMap.

Add ram User to aws-auth ConfigMap

Edit the aws-auth ConfigMap:

kubectl edit configmap aws-auth -n kube-system


```
mapUsers: |
  - userarn: arn:aws:iam::ACCOUNT_ID:user/ram
    username: ram
    groups:
      - eks-user
```
# Create Kubernetes Role and RoleBinding for Namespace blue
--------------------------------------------------------------


role-blue.yaml
```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: blue
  name: namespace-access
rules:
- apiGroups: [""]
  resources: ["pods", "services", "deployments"]
  verbs: ["get", "list", "create", "update", "delete"]

```
rolebinding-blue.yaml

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: namespace-access-binding
  namespace: blue
subjects:
- kind: User
  name: ram
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: namespace-access
  apiGroup: rbac.authorization.k8s.io

```
kubectl apply -f role-blue.yaml

kubectl apply -f rolebinding-blue.yaml



Provide ram User Access to the Cluster
---------------------------------------
aws configure --profile ram

Update the Kubernetes configuration:
-------------------------------------

aws eks update-kubeconfig --region <region> --name <cluster_name> --profile ram

 Verify Access
 ---------------

kubectl get pods -n blue
