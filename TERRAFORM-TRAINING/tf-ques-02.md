



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

```
terraform init
terraform workspace new dev
terraform plan -var-file="dev.tfvars"
terraform apply -var-file="dev.tfvars"
```


# Terraform Role, Challenges & Solutions in EKS Multi-Account Setup

| Area | How Terraform Helped | Challenges | Solutions |
|------|-----------------------|------------|-----------|
| **Multi-Account EKS Setup** | Created reusable modules to deploy EKS clusters in Landing Zone accounts | Managing providers for multiple AWS accounts (prod/dev/test) | Used `provider` aliasing and `terraform.workspace` with role assumption |
| **Private EKS with VPC** | Automated creation of VPC, subnets, NAT gateways, routing tables, etc. | Subnet misalignment caused EKS nodes to fail | Added subnet tagging (`kubernetes.io/role/internal-elb`, `shared=true`) and validated CIDRs |
| **IRSA Integration** | Integrated IAM roles with Kubernetes ServiceAccounts | Hard to debug trust relationships and missing OIDC | Used Terraform data sources for OIDC and validated trust policy with AWS console |
| **EFS CSI Integration** | Provisioned EFS file systems and mount targets | Permission denied errors on pods | Fixed IAM policy via IRSA and security group access from EKS worker nodes |
| **Kafka, Redis, RDS** | Deployed and managed stateful services in isolated subnets with Terraform modules | RDS subnet groups missing or wrong SGs | Used Terraform modules with `for_each` to create subnet groups, security rules correctly |
| **API Gateway** | Used Terraform to configure stages, logging, throttling, and custom domains | Dependency ordering issues when deploying with custom domains | Split modules and added explicit `depends_on` |
| **CloudFront + S3** | Configured static hosting for frontend with versioned S3 and secure CloudFront | Cache invalidation wasn't handled | Added automated invalidation in deployment scripts |
| **SecurityHub, GuardDuty** | Enabled org-wide security tools with Terraform | Hard to enable in all regions and link with master account | Used `for_each` on enabled regions, and separate account-level modules |
| **WAF on ALB** | Applied WAF WebACLs to ALB with Terraform | Terraform drifted due to console changes | Locked down console changes and added `lifecycle { prevent_destroy = true }` |
| **ECR Lifecycle Rules** | Applied cleanup policies to retain latest images only | Older images were not removed initially | Refined regex match rules for untagged/stale images |
| **Golden Signals & Monitoring** | Created Dashboards and Alert policies via Terraform | HPA/VPA had no effect due to metric server issues | Deployed metric server via Helm module with correct RBAC |
| **Cilium & IP Exhaustion** | Enabled Cilium for better IP management (IPAM, BPF) | Pods stuck in `Pending` due to IP exhaustion | Switched from AWS VPC CNI to Cilium, adjusted `eniConfig` and subnet sizes |
| **Tag Enforcement & Cost Allocation** | Automated tagging with `default_tags` and enforced compliance | Resources missing cost tags | Used AWS Config rules + Terraform `locals` to apply standard tags |
