




## multi
--------

```

~/k8s-project# tree
.
├── base
│   ├── cm.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── kustomisation.yaml
│   └── service.yaml
├── helm
│   ├── Chart.yaml
│   ├── values
│   │   ├── dev-values.yaml
│   │   ├── prod-values.yaml
│   │   └── staging-values.yaml
│   └── values.yaml
├── helmfile
├── kubeconfig
│   └── cluster01
│       └── kubeconfig
└── overlays
    └── dev
        ├── cm.yaml
        ├── ingress.yaml
        ├── kustomisation.yaml
        └── ns.yml

7 directories, 16 files





```


```
tree
.
├── green-app
│   ├── Chart.yaml
│   ├── templates
│   │   ├── deployment.yaml
│   │   ├── ingress.yaml
│   │   └── service.yaml
│   └── values.yaml
└── helmfile.yaml
```








k8s/
├── deployment1.yaml
├── deployment2.yaml
└── kustomization.yaml

# kustomization.yaml
resources:
  - deployment1.yaml
  - deployment2.yaml


kustomize build k8s/ | kubectl apply -f -

overlays/cluster1/kustomization.yaml

bases:
  - ../../base
patchesStrategicMerge:
  - deployment-patch.yaml


overlays/cluster1/deployment-patch.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: your-deployment-name
spec:
  replicas: 3  # Specific for Cluster 1

  


kustomize build overlays/cluster1 | kubectl apply -k - --context=cluster1-context

kustomize build overlays/cluster2 | kubectl apply -k - --context=cluster2-context

kubectl config use-context cluster1-context



helm

helm create my-app

my-app/
├── charts/
├── templates/
├── values.yaml
└── Chart.yaml

Define Resources in the Chart: In the templates directory, define your resources (e.g., deployments, services, configmaps, etc.).

For example, templates/deployment.yaml will define the Deployment resource for your application.

values-cluster1.yaml
replicaCount: 3
image:
  repository: my-repo/my-app
  tag: cluster1-version
resources:
  limits:
    cpu: 500m
    memory: 512Mi

values-cluster2.yaml

replicaCount: 5
image:
  repository: my-repo/my-app
  tag: cluster2-version
resources:
  limits:
    cpu: 1000m
    memory: 1Gi

helm upgrade --install my-app ./my-app --kube-context cluster1-context -f values-cluster1.yaml




my-app/
├── charts/
├── templates/
├── values.yaml
├── values-cluster1.yaml
├── values-cluster2.yaml
└── Chart.yaml



aws eks --region <region> update-kubeconfig --name <cluster_name>

kubectl cluster-info

    

Step 1: Create an IAM policy to limit mike's EKS access.
Step 2: Attach the IAM policy to user mike.
Step 3: Update kubeconfig for mike to allow EKS cluster access.
Step 4: Modify the aws-auth ConfigMap to map mike to a Kubernetes username.
Step 5: Create Kubernetes RBAC roles and bindings to limit what mike can do within the cluster.


```
tree
.
├── green-app
│   ├── Chart.yaml
│   ├── templates
│   │   ├── deployment.yaml
│   │   ├── ingress.yaml
│   │   └── service.yaml
│   └── values.yaml
└── helmfile.yaml
```

```



```




  

  
