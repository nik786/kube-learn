





```
terraform init
terraform workspace new dev
terraform plan -var-file="dev.tfvars"
terraform apply -var-file="dev.tfvars"
```

# EKS Architecture Design: HA, Scalable, Secure, Multi-Account with Governance

| Area | Strategy / Implementation |
|------|----------------------------|
| **VPC & Subnet Design** | - VPC with **private subnets** across 3 AZs<br>- NAT Gateway in public subnet for outbound traffic<br>- Subnet tagging for ALB, EFS, and EKS compatibility |
| **EKS Cluster Deployment** | - EKS control plane launched in **private subnets**<br>- Enabled **OIDC**, **IRSA**, **control plane logging**, and **encryption with KMS**<br>- Deployed via **Terraform** in Landing Zone accounts |
| **EFS Integration** | - Mounted **EFS CSI Driver** with EKS for persistent, scalable shared storage<br>- Used with workloads like Jenkins, ML models, shared configs<br>- Deployed EFS in multiple AZs for HA |
| **RDS (Relational Database)** | - Used **RDS PostgreSQL/MySQL** for transactional workloads<br>- Enabled **multi-AZ**, **automated backups**, **encryption**, **IAM auth**<br>- Subnet group and security groups configured with Terraform |
| **DynamoDB (NoSQL)** | - Used for session store, product catalogs, user preferences<br>- Enabled **point-in-time recovery**, **auto-scaling**, and **global tables** when needed<br>- IAM roles scoped to DynamoDB tables via IRSA |
| **Kafka (MSK)** | - Used **Amazon MSK** for real-time streaming<br>- Private connectivity with EKS over VPC peering<br>- Created **IAM roles for service accounts** to integrate Kafka producers/consumers securely |
| **Redis (Elasticache)** | - Used **Redis Cluster Mode** for fast caching and leaderboard use cases<br>- Launched in private subnets with **TLS** and **auth token enabled**<br>- Managed security group rules for EKS to connect |
| **ALB Ingress & Route53** | - ALB Ingress Controller for app exposure<br>- Route53 for DNS<br>- ACM certificates for HTTPS; WAF attached to ALB |
| **API Management** | - API Gateway for public APIs<br>- Used **API keys, throttling, logging**, and **custom domain** with Route53 |
| **Security Tools** | - Enabled **AWS WAF**, **SecurityHub**, **GuardDuty**, **Inspector**<br>- SCPs and IAM boundaries for account-level restrictions |
| **ECR & Lifecycle** | - Container images stored in **ECR**<br>- Lifecycle policy retained last N images<br>- Scanned images for CVEs using **ECR image scan** |
| **Static Hosting** | - React UI hosted on **S3** with **CloudFront** CDN<br>- OAI for access control; versioned buckets for rollback |
| **Tagging** | - Enforced **mandatory tags** via AWS Config<br>- Used for cost reporting, ownership, app tracking |
| **Secrets Management** | - Used **AWS Secrets Manager** to store credentials securely<br>- Integrated with IRSA and rotation enabled for DB secrets |
| **External Secrets Operator (ESO)** | - Used ESO to sync secrets from Secrets Manager/SSM to Kubernetes<br>- Managed via Helm + Terraform; secure and auditable |
| **SSM Parameter Store** | - Used for non-sensitive configurations<br>- Structured with naming conventions (`/env/app/key`) and access via IRSA |
| **AWS Service Catalog** | - Published standard infrastructure products (e.g., EKS baseline, S3, VPC)<br>- Governed access via portfolios and principals<br>- Integrated with Terraform using `aws_servicecatalog_*` resources |
| **Terraform Modules** | - Modularized components: VPC, EKS, ALB, RDS, IAM<br>- Used **Terragrunt** and **workspaces** for multi-env support |
| **Terraform Challenges** | - Provider aliasing in multi-account → solved via proper alias blocks<br>- State drift & locking → used S3 backend + DynamoDB lock<br>- Cilium integration for IP exhaustion mitigation |
| **Latency & Observability** | - Prometheus + Grafana for golden signals (latency, errors, saturation, traffic)<br>- Used CloudWatch metrics, alarms, dashboards for critical workloads<br>- HPA + VPA used for auto-scaling |




# Terraform Role, Challenges & Solutions in EKS Multi-Account Setup

| Area | How Terraform Helped | Challenges | Solutions |
|------|-----------------------|------------|-----------|
| **Multi-Account EKS Setup** | Created reusable modules to deploy EKS clusters in Landing Zone accounts | Managing providers across accounts | Used `provider` aliasing with role assumption and `terraform.workspace` for env mapping |
| **Private EKS with VPC** | Automated VPC, NAT, subnets, and routing for EKS | EKS not launching in correct subnets | Ensured subnets were tagged (`kubernetes.io/cluster/cluster-name`) properly |
| **IRSA** | Bound IAM Roles with Kubernetes ServiceAccounts securely | Trust policy errors, OIDC missing | Used Terraform to fetch OIDC and generate trust policy block dynamically |
| **EFS CSI Integration** | Provisioned EFS with mount targets for persistent volumes | Pod mount failures | Fixed NFS security group, added IAM policies via Terraform |
| **Kafka, Redis, RDS** | Managed DB and cache infra using modules and secrets | Security group misconfigurations | Used `for_each` to modularize infra, ensured DB credentials were securely pulled from Secrets Manager |
| **DynamoDB** | Provisioned global tables, autoscaling, TTLs | Conflict during replication setup | Used staged rollout and explicit AWS region configurations |
| **API Gateway** | Managed APIs, stages, logging, rate-limiting | Issues with domain association | Used `depends_on` and separated domain resource module |
| **ALB Ingress + Route53** | Set up ingress controllers and domain routing | DNS mismatch, SSL cert issues | Managed certs via ACM Terraform, used `external_dns` for sync |
| **SecurityHub, GuardDuty** | Enabled org-wide with Terraform | Multi-region config issues | Used `for_each` over AWS regions and enabled aggregation from delegated admin |
| **WAF on ALB** | Applied WAF via Terraform | Drift caused by console edits | Prevented console changes with `lifecycle { prevent_destroy = true }` |
| **CloudFront + S3** | Hosted frontend with versioning and caching | Stale content post-deploy | Automated `aws cloudfront create-invalidation` post-deploy |
| **ECR Lifecycle Policies** | Cleaned up old container images automatically | Missed stale tags initially | Fine-tuned lifecycle regex using Terraform variables |
| **Secrets Manager** | Stored sensitive data like DB creds securely | Secrets rotation tracking | Terraform provisioned secrets and tags, rotation configured separately |
| **SSM Parameter Store** | Managed configuration parameters centrally | Missing path naming standards | Used Terraform `locals` to enforce naming conventions (e.g., `/env/app/key`) |
| **External Secrets Operator** | Synced secrets into EKS from Secrets Manager & SSM | RBAC issues, sync failure | Used Helm provider to deploy ESO with IRSA and `secretStore` configuration in Terraform |
| **AWS Service Catalog** | Provisioned standard compliant infrastructure | Integration with org permissions | Used Terraform to publish products, portfolios and managed principal associations |
| **Golden Signals & Monitoring** | Built CloudWatch Dashboards, alarms for latency, error rate, etc. | Inconsistent metrics across clusters | Used Terraform to push unified dashboards + `cloudwatch-agent` on nodes |
| **Cilium for IP Exhaustion** | Solved pod IP exhaustion with Cilium IPAM | Pending pods due to lack of IPs | Switched from VPC CNI to Cilium, tuned `eniConfig`, assigned dedicated subnets |
| **Tag Enforcement** | Applied `default_tags` in provider block | Resources lacked cost tags | Enforced `tag_policies` via AWS Organizations + Terraform tag locals |
