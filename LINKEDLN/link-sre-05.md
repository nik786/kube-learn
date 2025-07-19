
# Cloud Architecture Interview Questions – Scenario Based (with Answers)

| **#** | **Question** | **Answer** |
|------|--------------|------------|
| 1 | Legacy 3-tier app migration to Azure with no downtime? | Use **Azure Migrate** with a **blue-green deployment**, **Traffic Manager**, and **incremental cutover** to avoid downtime. |
| 2 | Design a HIPAA-compliant healthcare platform? | Use **Azure Policy**, **Private Endpoints**, **encryption (at-rest and in-transit)**, **logging**, and **BAA agreement** with Microsoft. |
| 3 | AWS latency in India & Australia? | Use **Global Accelerator**, deploy app in **multiple regions**, use **Route 53 latency-based routing** and **CloudFront**. |
| 4 | Handle traffic surges for retail? | Use **autoscaling groups**, **serverless (Lambda/Fargate)**, and **event-driven architecture** with **CDN caching** for cost-efficiency. |
| 5 | Spike in cloud costs? | Analyze **Cost Explorer**, enable **budgets**, check for **unattached resources**, review **instance types**, and optimize with **Reserved Instances**. |
| 6 | Push 50+ microservices weekly? | Implement **CI/CD pipelines** with **canary deployments**, **service mesh** (Istio/Linkerd), and **centralized logging/tracing** (ELK, OpenTelemetry). |
| 7 | Real-time IoT analytics platform? | Use **Azure IoT Hub / AWS IoT Core**, **Stream Analytics / Kinesis**, **Data Lake**, and **Kafka + Spark** for real-time processing. |
| 8 | On-prem data residency with cloud agility? | Use **Azure Stack HCI / AWS Outposts**, **hybrid connectivity** (VPN/ExpressRoute), and **Edge compute** with **central cloud orchestration**. |
| 9 | Poorly documented cloud infra? | Use **Azure Resource Graph / AWS Config**, **tag policies**, apply **naming standards**, and **Terraform/ARM/Bicep templates** for consistency. |
| 10 | Connect on-prem AD with Azure AD? | Use **Azure AD Connect**, enable **password hash sync or pass-through auth**, ensure **conditional access policies** are in place. |
| 11 | Multi-cloud for financial workloads? | Use **Active-Active** DBs (e.g., Cosmos DB/Aurora Global), **replication**, **BGP routing**, **shared IAM policies**, and **Terraform** for infra-as-code. |
| 12 | Secure PII data access by 3rd parties? | Use **tokenized APIs**, **RBAC**, **Key Vault**, **logging with Azure Monitor / AWS CloudTrail**, and **network isolation**. |
| 13 | DB is SPOF and causes downtime? | Redesign using **RDS Multi-AZ / Cosmos DB / SQL HA**, enable **auto-failover**, add **replica nodes** and **read-write separation**. |
| 14 | ML inference with low latency? | Use **GPU-based nodes** (AKS/EKS), **model caching**, **ONNX optimizations**, **autoscaling**, and **API gateway with rate-limiting**. |
| 15 | Centralized logging and monitoring for 100+ services? | Use **Azure Monitor + Log Analytics**, **AWS CloudWatch + OpenTelemetry**, central SIEM like **Sentinel**, and **alerting with Action Groups**. |
| 16 | Minimize vendor lock-in? | Use **open-source stacks** (K8s, Kafka, PostgreSQL), **multi-cloud CI/CD**, **Terraform**, and avoid **proprietary PaaS where feasible**. |
| 17 | Intermittent timeout errors, no cloud issues? | Check **app logs**, **DNS resolution**, **network latency**, use **packet capture**, and monitor **dependency timeouts** (e.g., DB or API). |
| 18 | Isolated Dev/Test/Prod environments? | Create **separate subscriptions or accounts**, apply **RBAC**, enforce **naming and tagging policies**, and use **Landing Zones**. |
| 19 | Deploy internal LLM on GPU Kubernetes cluster? | Use **GPU-enabled nodes (AKS/EKS with NVIDIA)**, deploy model via **Kubeflow/Triton**, use **persistent volume for caching**, and **inference autoscaling**. |
