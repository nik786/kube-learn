
# Cloud Architecture & DevOps Scenario-Based Q&A

| #  | Scenario | Recommended Architecture / Strategy |
|----|----------|--------------------------------------|
| 1  | Migrate 3-tier on-prem app to Azure without downtime | Use Azure Migrate with *blue-green deployment* or *canary strategy*, replicate using Azure Site Recovery, cut over traffic with Azure Front Door, and perform DNS switchover post-validation. |
| 2  | Secure healthcare platform with HIPAA compliance | Use Azure Policy for HIPAA blueprint, encryption at rest & transit, private endpoints, Azure Monitor for audit logs, Azure Key Vault for secrets, and BAA with Microsoft. |
| 3  | AWS latency issues in India and Australia | Deploy workloads in Mumbai & Sydney regions, use Route 53 latency-based routing, CloudFront CDN, and Global Accelerator to reduce latency. |
| 4  | Handle unpredictable retail traffic surges | Use AWS ALB + Auto Scaling Groups + Spot Instances + RDS Aurora Serverless, leverage CloudFront for static content, scale with EventBridge & Lambda. |
| 5  | Spike in cloud spend after go-live | Analyze billing reports (Cost Explorer, AWS Budgets), identify expensive services, check misconfigured autoscaling, orphaned resources, and sudden traffic surges. |
| 6  | Weekly deploy of 50+ microservices | Implement GitOps with ArgoCD or Flux, CI/CD with GitHub Actions/GitLab, use Canary/Blue-Green deployments, service mesh (Istio/Linkerd), centralized logging, and secure pipelines. |
| 7  | Real-time analytics for IoT data | Use Azure IoT Hub + Event Hubs + Stream Analytics + Data Lake + Synapse Analytics. Apply autoscaling and partitioning strategies for ingestion. |
| 8  | On-prem data residency with cloud compute | Use Azure Stack HCI or AWS Outposts for local compute, integrate with cloud services via ExpressRoute or Direct Connect, ensure compliance with data location laws. |
| 9  | Poorly documented cloud environment | Use Azure Resource Graph or AWS Config to inventory resources, apply naming standards via policies, automate tagging, create landing zones with IaC. |
| 10 | Connect on-prem AD with Azure AD | Set up Azure AD Connect for hybrid identity, sync password hash or use pass-through auth, secure with conditional access and MFA, monitor via Azure AD logs. |
| 11 | Multi-cloud for financial workloads | Use data replication tools (Azure Site Recovery, AWS DMS), use DNS failover (Route 53 / Traffic Manager), store encrypted data on both clouds, keep infra IaC-driven. |
| 12 | Secure PII access by third parties | Tokenize or encrypt data at field level, use Azure API Management or AWS API Gateway with OAuth2, enable detailed auditing via CloudTrail / Azure Monitor. |
| 13 | DB is a single point of failure | Use multi-AZ or regional replicas (Aurora/RDS, Cosmos DB), implement automated failover, DNS-based routing, and read-replicas to offload reads. |
| 14 | ML inference with real-time scoring | Deploy with Kubernetes + KServe/SageMaker Endpoints, use GPU node pools, autoscale with KEDA/Karpenter, use Redis or feature store cache for pre-processing. |
| 15 | Centralized logging/monitoring for 100+ services | Use Azure Monitor + Log Analytics or AWS CloudWatch + OpenSearch, ship logs via Fluent Bit, alert via PagerDuty/Splunk/Prometheus-Grafana, use Azure Lighthouse for cross-subscription view. |
| 16 | Avoid vendor lock-in | Use open-source tools (K8s, Terraform, Prometheus), containerize workloads, avoid PaaS lock-ins, use abstraction layers like Crossplane or Anthos. |
| 17 | Intermittent timeout errors in production | Correlate app logs with APM (New Relic, Azure App Insights), check VPC/network security groups, latency at backend DB, trace with X-Ray or Dapr observability. |
| 18 | Secure Dev/Test/Prod environments | Use separate subscriptions or accounts, enforce RBAC/IAM, deploy via IaC, isolate VNETs, monitor with tagging, enable CI/CD with environment promotion gates. |
| 19 | Deploy internal LLM on GPU-optimized K8s cluster | Use node pools with NVIDIA A100/GPU, model server with Triton or vLLM, use KServe or custom deployment with autoscaler, EBS or EFS for model artifacts. |
| 20 | Fintech app with sub-second latency & data residency | Use regional deployments with read/write segregation, serve latency-critical APIs from memory DB (Redis), store PII in regional storage with local encryption & audit policies. |
