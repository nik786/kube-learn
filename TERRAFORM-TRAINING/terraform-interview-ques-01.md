

# Terraform Module Experience – AWS Projects

| Aspect | Details |
|--------|---------|
| **Modules Written** | - **VPC Module**: Custom VPC with public/private subnets, route tables, internet/NAT gateways, IGW/NGW configuration<br>- **EKS Module**: Provisioning EKS cluster, managed/unmanaged node groups, `aws-auth` config updates, IAM roles<br>- **EC2 Module**: Reusable EC2 module with AMI lookup, security groups, volumes, userdata, and key pair attachment<br>- **S3 Module**: S3 buckets with lifecycle rules, encryption, versioning, replication, and public access block<br>- **CloudFront + Route 53**: Static website hosting with S3 origin, OAI, custom domain with ACM and Route 53 records<br>- **IAM Module**: Creation of roles, policies, and trust relationships (used for IRSA and cross-account access)<br>- **RDS Module**: MySQL/Postgres setup with parameter groups, subnet groups, backup and maintenance windows |
| **Challenges Faced** | - **State File Conflicts**: Team members overwriting Terraform state<br>- **Cross-Module Dependencies**: Referencing outputs across environments<br>- **Reusability for Multi-env**: Making modules generic for dev/stage/prod<br>- **IAM Policy Debugging**: Incorrect policies causing access issues<br>- **IRSA Setup**: Aligning IAM roles with service accounts for Kubernetes pods<br>- **Data Lookups and Count Conflicts**: Mixing `count` with `for_each` for dynamic resource creation |
| **Resolutions** | - Used **remote backend** (S3 + DynamoDB) for state locking and isolation<br>- Structured environment-specific files and **used workspaces** for separation<br>- Extracted outputs cleanly and used **`terraform_remote_state`** where applicable<br>- Used **`jsondecode()`** and **`terraform console`** to debug IAM policies<br>- For IRSA, created IAM roles with specific trust policy and annotated K8s service accounts<br>- Used conditional logic with `count`, `for_each`, and `dynamic` blocks carefully |

