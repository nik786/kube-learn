# 📘 Runbook: EKS Cluster Upgrade with Zero Downtime (Terraform + Self-Managed Nodes)

We use **Terraform with the EKS module** to perform zero-downtime upgrades of our EKS cluster.  
This guide covers upgrading the **control plane, add-ons, and worker nodes** safely.

---

## 🔧 Prerequisites
- Terraform installed on local machine.  
- EKS module repo cloned and customized as per requirements.  
- IAM permissions for EKS, EC2, IAM, and related services.  
- Backup of current Terraform state and cluster configuration.  
- Upgrade path reviewed (EKS supports only **sequential minor upgrades**).  

---

## 🚀 Upgrade Steps

### **1. Prepare for Upgrade**
- Review [AWS EKS release notes](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html).  
- Ensure tools are updated: `kubectl`, `aws-cli`, Terraform.  
- Backup state and manifests:
  ```bash
  terraform state pull > state-backup.json
  kubectl get all --all-namespaces -o yaml > cluster-backup.yaml




2. Upgrade the EKS Control Plane

Update EKS version in your Terraform eks module:

module "eks" {
  source          = "./modules/eks/terraform-aws-eks"
  cluster_name    = local.cluster_name
  cluster_version = "1.31" # target version
  ...
}


Apply the changes:

terraform plan
terraform apply


Verify cluster version:

aws eks describe-cluster --name gl-dev --query cluster.version

3. Upgrade Cluster Add-ons

Update add-ons (VPC CNI, CoreDNS, kube-proxy, CSI drivers) via Terraform or AWS CLI:

aws eks update-addon --cluster-name gl-dev \
  --addon-name vpc-cni --addon-version latest


Verify add-on pods:

kubectl get pods -n kube-system

4. Update Worker Nodes with Latest AMI

We dynamically fetch the latest EKS ARM64 AMI using a data "aws_ami" block:

data "aws_ami" "eks_arm64" {
  most_recent = true
  owners      = ["602401143452"] # Amazon EKS AMI Account
  filter {
    name   = "name"
    values = ["amazon-eks-arm64-node-1.31-v*"]
  }
  filter {
    name   = "architecture"
    values = ["arm64"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}


Ensure your self-managed node groups reference this AMI:

self_managed_node_groups = {
  core = {
    name             = "${local.environment_name}-core"
    instance_types   = ["t4g.small"]
    desired_capacity = 1
    ami_id           = data.aws_ami.eks_arm64.id
    ...
  }
}


Apply Terraform:

terraform apply

5. Blue-Green Node Group Upgrade Strategy

Instead of directly replacing nodes, we use a Blue-Green upgrade for safer rollouts:

Create a new node group (Green) with the latest AMI and desired capacity.

self_managed_node_groups = {
  core-blue = { ... old config ... }
  core-green = {
    name             = "${local.environment_name}-core-green"
    instance_types   = ["t4g.small"]
    desired_capacity = 2
    ami_id           = data.aws_ami.eks_arm64.id
    ...
  }
}


Apply Terraform to provision the Green group:

terraform apply


Cordon & drain old Blue nodes:

kubectl cordon <blue-node-name>
kubectl drain <blue-node-name> --ignore-daemonsets --delete-emptydir-data


Validate workloads are rescheduled on Green nodes:

kubectl get pods -o wide


Remove Blue node group from Terraform after validation:

self_managed_node_groups = {
  core-green = { ... latest config ... }
}


Apply changes to remove Blue nodes:

terraform apply


✅ Benefit: If anything breaks, you can roll workloads back to the Blue node group without downtime.

6. Validate Traffic Flow

Verify ALB Ingress → ALB → Pods routing.

Confirm app health via CloudWatch metrics and logs.

7. Post-Upgrade Validation

Run smoke tests on workloads.

Validate versions:

kubectl version
aws eks describe-cluster --name gl-dev --query cluster.version


Document new cluster and AMI versions.

✅ Best Practices

Always upgrade lower environments first, then production.

Use Blue-Green Node Groups instead of in-place node replacement.

Upgrade add-ons before workloads that depend on them.

Enable Terraform remote state backend with locking (S3+DynamoDB or GCS+locking).

Keep rollback plan ready (old AMIs + Terraform state).

Automate health checks using probes and test suites.

📝 Example Terraform Workflow
# Step 1: Pull the latest state
terraform state pull > state-backup.json

# Step 2: Update EKS version in eks module (cluster_version)
vim main.tf

# Step 3: Apply control plane upgrade
terraform plan
terraform apply

# Step 4: Provision Green worker node group with latest AMI
terraform apply

# Step 5: Verify Green nodes
kubectl get nodes

# Step 6: Cordon & drain Blue nodes
kubectl cordon <blue-node-name>
kubectl drain <blue-node-name> --ignore-daemonsets --delete-emptydir-data

# Step 7: Remove Blue node group after validation
terraform apply

# Step 8: Validate workloads and traffic flow
kubectl get pods -o wide


This runbook ensures zero downtime EKS upgrades using Terraform with self-managed ARM64 nodes and a Blue-Green upgrade strategy.
