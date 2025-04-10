



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
| **Terraform Modules** | - Modularized components: VPC, EKS, ALB, RDS, IAM<br>- Used **Terragrunt** and **workspaces** for multi-env support |
| **Terraform Challenges** | - Provider aliasing in multi-account → solved via proper alias blocks<br>- State drift & locking → used S3 backend + DynamoDB lock<br>- Cilium integration for IP exhaustion mitigation |
| **Latency & Observability** | - Prometheus + Grafana for golden signals (latency, errors, saturation, traffic)<br>- Used CloudWatch metrics, alarms, dashboards for critical workloads<br>- HPA + VPA used for auto-scaling |
| **Useful Terraform Commands** |
```bash
terraform init
terraform workspace new dev
terraform plan -var-file="dev.tfvars"
terraform apply -var-file="dev.tfvars"
