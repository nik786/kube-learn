
```

apiVersion: v1
kind: Pod
metadata:
  name: red
  namespace: default
spec:
  containers:
  - image: busybox:1.28
    name: red-container
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
    
  initContainers:
  - image: busybox
    name: red-init
    command: ["sleep", '20'] 

```

```
apiVersion: v1
kind: Pod
metadata:
  name: red
  namespace: default
spec:
  containers:
  - command:
    - sh
    - -c
    - echo The app is running! && sleep 3600
    image: busybox:1.28
    name: red-container
  initContainers:
  - command:
    - "sleep"
    - "20"
    image: busybox:1.28
    name: red-init
```

```

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 7
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
        resources:
         requests:
           cpu: 100m
         limits:
           cpu: 200m

---
apiVersion: v1
kind: Service
metadata:
  name: flask-web-app-service
spec:
  type: ClusterIP
  selector:
    app: flask-app
  ports:
   - port: 80
     targetPort: 80  

```

```

cat autoscale.yml 
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  creationTimestamp: null
  name: nginx-deployment
spec:
  maxReplicas: 3
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  targetCPUUtilizationPercentage: 80
status:
  currentReplicas: 0
  desiredReplicas: 0

```

Pod delete is a user-initiated action that removes the pod from the cluster.

Pod terminate is the process Kubernetes follows during deletion, 
where the pod gracefully shuts down before being removed




```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "S3ReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:GetBucketLocation",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    },

```

```

 {
      "Sid": "ECRReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "ecr:DescribeRepositories",
        "ecr:DescribeImages",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:GetAuthorizationToken"
      ],
      "Resource": "*"
    }
  ]
}

```
Policies
----------
## Generic


- AmazonEC2ContainerRegistryReadOnly
- AmazonS3ReadOnlyAccess
- AmazonS3FullAccess


Storageclasses
---------------


- local-storage               kubernetes.io/no-provisioner
- local-storage does nt support dynamic provisioning
- waitforfirstconsumer
- portworx-io-priority-high   kubernetes.io/portworx-volume   Delete          Immediate              false                  9s



The StorageClass used by the PVC uses WaitForFirstConsumer volume binding mode. 
This means that the persistent volume will not bind to the claim until a pod makes use of the PVC to request storage.

```
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer

```

In which layer does API Gateway work?

API Gateway primarily operates at the Application Layer (Layer 7)

In which layer does ALB Ingress work?

ALB Ingress primarily operates at the Application Layer (Layer 7)



# 🏗️ Web Architecture Overview (Three-Tier Model + OSI Layer Mapping)

This architecture follows the **Three-Tier Architecture Pattern**, where each tier corresponds to distinct responsibilities and OSI layers.

---

## 🎨 1. Presentation Tier  
### 👉 S3 + CloudFront (Static Website Hosting)
- **Purpose:** Deliver static content (HTML, CSS, JS) to users
- **OSI Layer:** `Application Layer (Layer 7)`
- **Responsibilities:**
  - S3 serves static assets
  - CloudFront provides:
    - Content Delivery (CDN)
    - SSL/TLS termination
    - Caching
    - URL-based routing

---

## ⚙️ 2. Application Tier  
### 👉 API Gateway → VPC Link → ECS Backend
- **Purpose:** Handle dynamic requests and business logic
- **OSI Layer:** `Application Layer (Layer 7)`
- **Responsibilities:**
  - **API Gateway:**
    - Handles HTTP methods, rate limiting, and auth
  - **VPC Link:**
    - Secure routing into private ECS services (internally Layer 3/4)
  - **ECS (Fargate or EC2):**
    - Hosts containerized microservices and APIs

---

## 🗄️ 3. Data Tier  
### 👉 ECS → DynamoDB / RDS
- **Purpose:** Data persistence and retrieval
- **OSI Layers:**
  - `Transport Layer (Layer 4)` – TCP connections
  - `Application Layer (Layer 7)` – Data protocols
- **Responsibilities:**
  - **DynamoDB:** NoSQL access via HTTPS (Layer 7)
  - **RDS:** Relational access via SQL over TCP (Layer 4/7)

---

## 📌 Summary Table

| Tier             | Component Flow                    | OSI Layer(s)                            |
|------------------|-----------------------------------|-----------------------------------------|
| 🎨 Presentation   | S3 + CloudFront                   | 🌐 `Application Layer (L7)`             |
| ⚙️ Application    | API Gateway → VPC Link → ECS      | 🌐 `Application Layer (L7)`             |
| 🗄️ Data          | ECS → DynamoDB / RDS              | 🛰️ `Transport Layer (L4)` + 🌐 `Application Layer (L7)` |

---

## ✅ Architecture Type: `Three-Tier Architecture`
- **Scalable**: Each tier can scale independently
- **Secure**: VPC Link isolates internal traffic
- **Performant**: CloudFront caching, ECS auto-scaling, and managed databases


## 🌱 What is Terragrunt?

**Terragrunt** is a thin wrapper for Terraform that provides extra tooling for managing remote state, DRY configurations, and module dependencies.  
It simplifies infrastructure management by promoting reusable, maintainable, and consistent Terraform code across environments.



```

root@controller:/home/nik/Desktop/git_ops/helm/nginx/nginx# tree
.
├── Chart.lock
├── charts
│   └── common
│       ├── Chart.yaml
│       ├── README.md
│       ├── templates
│       │   ├── _affinities.tpl
│       │   ├── _capabilities.tpl
│       │   ├── _compatibility.tpl
│       │   ├── _errors.tpl
│       │   ├── _images.tpl
│       │   ├── _ingress.tpl
│       │   ├── _labels.tpl
│       │   ├── _names.tpl
│       │   ├── _resources.tpl
│       │   ├── _secrets.tpl
│       │   ├── _storage.tpl
│       │   ├── _tplvalues.tpl
│       │   ├── _utils.tpl
│       │   ├── validations
│       │   │   ├── _cassandra.tpl
│       │   │   ├── _mariadb.tpl
│       │   │   ├── _mongodb.tpl
│       │   │   ├── _mysql.tpl
│       │   │   ├── _postgresql.tpl
│       │   │   ├── _redis.tpl
│       │   │   └── _validations.tpl
│       │   └── _warnings.tpl
│       └── values.yaml
├── Chart.yaml
├── cmd.sh
├── README.md
├── templates
│   ├── deployment.yaml
│   ├── extra-list.yaml
│   ├── health-ingress.yaml
│   ├── _helpers.tpl
│   ├── hpa.yaml
│   ├── ingress-tls-secret.yaml
│   ├── ingress.yaml
│   ├── networkpolicy.yaml
│   ├── NOTES.txt
│   ├── pdb.yaml
│   ├── prometheusrules.yaml
│   ├── server-block-configmap.yaml
│   ├── serviceaccount.yaml
│   ├── servicemonitor.yaml
│   ├── stream-server-block-configmap.yaml
│   ├── svc.yaml
│   └── tls-secret.yaml
├── values.schema.json
└── values.yaml

```



```
tree
.
├── envs
│   ├── dev
│   │   └── s3
│   │       └── terragrunt.hcl
│   └── uat
│       └── s3
│           └── terragrunt.hcl
└── tg-modules
    └── s3-bucket
        └── main.tf

- cd envs/dev/s3
- terragrunt init
- terragrunt apply

```




