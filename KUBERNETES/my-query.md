

- [command-example](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/command-example.md)
- [nginx-deploy](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/nginx-deploy.md)


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


## Helm

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


cat dev/s3/terragrunt.hcl

terraform {
  source = "../../tg-modules/s3-bucket"
}


inputs = {
  bucket_name = "my-terragrunt-s3-bucket"
  tags = {
    Environment = "Dev"
    ManagedBy   = "Terragrunt"
  }
}





- cd envs/dev/s3
- terragrunt init
- terragrunt apply

```


```
self-managed/
├── envs/
│   ├── dev/
│   │   ├── eks/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   ├── outputs.tf
│   │   │   ├── dev.tfvars
│   │   │   └── backend.tf
│   │   └── bastion/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       ├── dev.tfvars
│   │       └── backend.tf
│   └── uat/
│       ├── eks/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   ├── outputs.tf
│       │   ├── uat.tfvars
│       │   └── backend.tf
│       └── bastion/
│           ├── main.tf
│           ├── variables.tf
│           ├── uat.tfvars
│           └── backend.tf
├── modules/
│   ├── eks/
│   │   ├── main.tf
│   │   └── variables.tf
│   └── bastion/
│       ├── main.tf
│       └── variables.tf


```

Helmfile
--------


```
.
├── base/                           # Kustomize base templates (reused across envs)
│   ├── cm.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   └── kustomization.yaml
│
├── overlays/                       # Environment-specific Kustomize overlays
│   ├── dev/
│   │   ├── cm.yaml
│   │   ├── ingress.yaml
│   │   ├── ns.yaml
│   │   └── kustomization.yaml
│   ├── staging/
│   └── prod/
│       └── ...
│
├── helm/                           # Raw Helm chart and environment-specific values
│   ├── Chart.yaml
│   ├── values.yaml                 # default values
│   └── values/                     # per-env overrides
│       ├── dev-values.yaml
│       ├── staging-values.yaml
│       └── prod-values.yaml
│
├── helmfile/                       # Helmfile environment definitions
│   ├── helmfile.yaml               # shared helmfile, can reference envs dynamically
│   └── environments.yaml           # maps dev/staging/prod to their values files
│
└── kubeconfig/                     # Per-cluster kubeconfigs (for CI or local use)
    └── cluster01/
        └── kubeconfig


```

```
if __name__ == "__main__": checks whether the script is being run directly.
If true, it calls the main() function to start program execution.

```

- NACL is stateless because it evaluates each packet individually without tracking connection state
- Security Groups are stateful and remember traffic sessions.


- RTO (Recovery Time Objective) is the maximum acceptable downtime after a failure,
- RPO (Recovery Point Objective) is the maximum acceptable data loss measured in time.



# Solving Latency and Performance Issues in RDS and DynamoDB

| Database    | Issue Area                | Solutions / Optimizations                                   | Benefits                                                     |
|-------------|---------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
| **RDS**    | Query Performance          | Use indexing, query optimization (analyze and rewrite slow queries), and caching (e.g., Amazon ElastiCache) | Faster query execution and reduced DB load                    |
|             | Scaling                   | Use read replicas, vertical scaling (larger instances), Aurora Serverless | Handles higher read throughput and adapts to demand          |
|             | Connection Management     | Use RDS Proxy to pool and manage connections efficiently, reducing overhead | Improves application scalability and reduces connection storms |
|             | Storage Latency           | Use provisioned IOPS SSD storage                             | Ensures consistent, low-latency I/O performance               |
|             | Monitoring & Tuning       | Enable Performance Insights, slow query logs, and use EXPLAIN plans to analyze query execution | Identifies bottlenecks and helps optimize query plans         |
| **DynamoDB**| Read/Write Latency        | Use DAX (DynamoDB Accelerator) caching                        | Sub-millisecond response times by caching frequently accessed data |
|             | Capacity Planning         | Use on-demand mode or provisioned capacity with autoscaling | Avoids throttling during traffic spikes                        |
|             | Data Modeling             | Design with partition keys for even data distribution to avoid hot partitions | Improves throughput and reduces latency                        |
|             | Query Efficiency          | Use efficient queries by leveraging Query operations (instead of Scan) and using Global Secondary Indexes (GSI) and Local Secondary Indexes (LSI) for alternate access patterns | Minimizes latency by fetching only relevant data               |
|             | Global Tables             | Deploy Global Tables for multi-region replication            | Reduces read/write latency by serving data closer to users    |
|             | Monitoring & Alerts       | Use CloudWatch alarms for throttling, latency, and consumed capacity | Proactive detection and mitigation of performance degradation  |

### Key Concepts:
- **RDS Proxy:** A managed database proxy that pools and shares connections to RDS, improving scalability and reducing failover times.
- **Query Optimization (RDS):** Analyzing slow queries with EXPLAIN plans to rewrite and add indexes for faster execution.
- **Global Secondary Index (GSI) (DynamoDB):** An alternate index allowing efficient queries on non-primary key attributes with eventual consistency.
- **Local Secondary Index (LSI) (DynamoDB):** An index on the same partition key but different sort key, providing strongly consistent queries on alternate sort keys.
- **Query vs Scan (DynamoDB):** Query retrieves items based on primary key or indexes efficiently; Scan reads entire table, causing higher latency and cost.


# Differences Between ReplicationController and ReplicaSet

| Aspect                   | ReplicationController                          | ReplicaSet                                    |
|--------------------------|-----------------------------------------------|----------------------------------------------|
| Selector Type            | Uses **equality-based selectors** only         | Supports **set-based selectors** (more flexible) |
| API Version              | Introduced in Kubernetes v1 (older API)         | Introduced in v1 as the next-gen replacement for RC |
| Usage                    | Mostly deprecated; replaced by ReplicaSet       | Preferred controller for managing pod replicas  |
| Integration with Deployments | Used by Deployments but less flexible           | Used by Deployments by default for better selector support |


uptime
 09:11:44 up 9 days, 15:07,  1 user,  load average: 4.60, 2.48, 1.84

# Explanation of `uptime` Command Output

| Field               | Description                                                   |
|---------------------|---------------------------------------------------------------|
| `09:11:44`          | Current system time (hours:minutes:seconds)                   |
| `up 9 days, 15:07`  | System uptime – how long the system has been running (9 days and 15 hours 7 minutes) |
| `1 user`            | Number of users currently logged into the system              |
| `load average: 4.60, 2.48, 1.84` | System load averages for the last 1, 5, and 15 minutes, representing the average number of processes waiting to run |



# Resolving "Filesystem Full" Due to Exhausted Inodes on Linux Node

| Issue                         | Solution / Action                                              | Description                                                     | Commands / Notes                                                   |
|-------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| Check inode usage              | Identify inode exhaustion                                      | Find which filesystem is out of inodes                          | `df -i`                                                          |
| Remove unnecessary small files | Delete old logs, temp files, or many small unused files       | Frees up inodes by removing files                               | `rm -rf /path/to/files/*`                                        |
| Archive and delete files       | Compress and delete originals                                  | Reduces number of files, freeing inodes                         | `tar czf archive.tar.gz /path/to/files/ && rm -rf /path/to/files/*` |
| Run filesystem check           | Repair filesystem errors                                       | Ensures filesystem consistency before formatting                | `fsck -f /dev/sdXn` (replace with actual device)                 |
| Reformat filesystem with higher inode count | Recreate filesystem with more inodes (data backup required)  | Inode count fixed at creation, increases number of inodes       | `mkfs.ext4 -N <number_of_inodes> /dev/sdXn`                      |
| Switch to different filesystem | Use FS with dynamic inode allocation (e.g., XFS)               | XFS dynamically manages inodes better than ext4                 | `mkfs.xfs /dev/sdXn`                                             |
| Restore data and remount       | After reformat, restore data and remount                       | Data restore needed after formatting                             | Use backup tools like `rsync` or `tar`                           |
| Monitor inode usage regularly  | Setup monitoring/alerts on inode usage                         | Prevents surprise inode exhaustion                               | Use monitoring tools like `nagios`, `prometheus`                 |


```
---
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: akshay
spec:
  groups:
  - system:authenticated
  request: <Paste the base64 encoded value of the CSR file>
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth

```


```
signerName: kubernetes.io/kube-apiserver-client
  usages:
  - digital signature
  - key encipherment
  - server auth
  username: agent-x

```

- kubectl config view
- kubectl config view --kubeconfig my-kube-config
- kubectl config current-context --kubeconfig my-kube-config
- kubectl config use-context research --kubeconfig  my-kube-config
- kubectl set serviceaccount deploy/web-dashboard dashboard-sa

```

annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"

```


```
progressDeadlineSeconds: 600
revisionHistoryLimit: 10
dnsPolicy: ClusterFirst
```



- trivy image --severity HIGH,CRITICAL --format table nginx:latest

- 









