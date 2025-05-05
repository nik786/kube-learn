

# EKS Upgrade Strategy in Production with Terraform, GitLab, and Blue-Green Deployments

| **Category**               | **Details** |
|----------------------------|-------------|
| **Approach**               | A fully automated and staged upgrade process using **Terraform** for stateful infrastructure management and **GitLab pipelines** for deploying updates. |
| **Infrastructure as Code** | - All resources (EKS control plane, worker nodes, launch templates, add-ons) are defined using **Terraform**.<br>- **Terraform `null_resource`** is used only for imperative actions like draining nodes, but the main infrastructure management is handled by **Terraform resources**.<br>- **GitLab deployment pipelines** trigger **Terraform runs**. |
| **Control Plane Upgrade**  | - Use **Terraform `aws_eks_cluster`** to upgrade the EKS cluster control plane version.<br>Example: `aws_eks_cluster` resource is updated with the desired Kubernetes version.<br>- Update with `terraform apply`.<br>- The control plane upgrade is automatically tracked and managed as part of the **Terraform state**. |
| **Blue-Green Node Upgrade** | - Create a new **`aws_launch_template`** with updated AMI and userdata.<br>- Update the **`aws_autoscaling_group`** to reference the new launch template version.<br>- Gradually add new nodes by scaling the new ASG using **Terraform**.<br>- Drain old nodes using `kubectl` via **Terraform `null_resource`**.<br>Example: `kubectl cordon` and `kubectl drain` commands are executed with `null_resource`.<br>- Once workload is confirmed healthy, terminate the old nodes via **Terraform `aws_autoscaling_group`**. |
| **Worker Node Group Management** | - Self-managed worker nodes are created and updated using **`aws_launch_template`** and **`aws_autoscaling_group`** resources.<br>- Node group versions are handled by updating the launch template in **Terraform**.<br>- **Terraform** manages scaling events and replacement of nodes in a **blue-green upgrade** process.<br>- **`aws_autoscaling_group`** is used to manage and scale the worker node groups. |
| **Add-on Management**      | - **Terraform** manages add-on upgrades directly using the **`aws_eks_addon`** resource.<br>Example: `aws_eks_addon` resource for `vpc-cni`, `kube-proxy`, and `coredns` is used to upgrade the add-ons.<br>- **Terraform** handles conflicts and version updates for these add-ons without needing **`null_resource`**.<br>Example: `aws_eks_addon` resource for `vpc-cni`.<br>`aws_eks_addon` automatically applies the version updates when the cluster is upgraded. |
| **Monitoring & Observability** | - Use **Prometheus**, **Grafana**, and **CloudWatch** to monitor node and pod health.<br>- Alerts on readiness, pod failures, and ASG scaling events are integrated. |
| **Pod Health Validation**  | - Kubernetes Pods are configured with **readinessProbes** and **livenessProbes**.<br>- Ensures safe scheduling of pods and traffic is routed only to healthy containers. |
| **Post-Deployment Health Check** | - **ALB Ingress Controller** provisions ALBs via Kubernetes ingress.<br>- Use **AWS ALB target group health checks** via **Terraform** to ensure traffic is routed to only healthy pods.<br>Example: `aws elbv2 describe-target-health` command is executed with **Terraform `null_resource`** for manual validation. |
| **Rollback Strategy**      | - Rollback is done by reverting to previous **Launch Template** versions and reapplying **Terraform** configurations.<br>- **Terraform** handles rollback of ASG, node groups, and control plane, ensuring no drift in the state. |
| **Post-Upgrade Validation** | - Validate node health with `kubectl get nodes`.<br>- Perform validation of pods with `kubectl get pods` and verify readiness with the probes.<br>- Validate application behavior using smoke tests and endpoint checks.<br>- **ALB health checks** and **manual validation** are part of the post-upgrade checks. |



```

resource "null_resource" "drain_old_node" {
  provisioner "local-exec" {
    command = "kubectl drain ${var.node_name} --ignore-daemonsets --delete-emptydir-data"
  }

  triggers = {
    node_name = var.node_name
  }
}


```


```


1. Create or Update Launch Template for Self-Managed Nodes:
-------------------------------------------------------------

aws ec2 create-launch-template \
  --launch-template-name my-node-template \
  --version-description v1 \
  --launch-template-data '{"imageId": "<ami-id>", "instanceType": "t3.medium", "userData": "<base64-encoded-user-data>"}'

###TF CODE

variable "ami_id" {
  description = "AMI ID for EKS worker nodes"
  type        = string
}

variable "environment" {
  description = "Environment tag"
  type        = string
}


resource "aws_launch_template" "self_managed_nodes" {
  name_prefix   = "my-node-template-"
  description   = "Launch template for self-managed EKS nodes"
  image_id      = var.ami_id
  instance_type = "t3.medium"

  user_data = base64encode(file("${path.module}/userdata.sh"))

  lifecycle {
    create_before_destroy = true
  }

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name        = "eks-self-managed-node"
      Environment = var.environment
    }
  }

  metadata_options {
    http_endpoint = "enabled"
    http_tokens   = "required"
  }
}




userdata.sh

#!/bin/bash
set -o xtrace
/etc/eks/bootstrap.sh <cluster-name> \
  --kubelet-extra-args '--node-labels=node.kubernetes.io/lifecycle=normal' \
  --b64-cluster-ca '<base64-cluster-ca>' \
  --apiserver-endpoint '<cluster-api-endpoint>'









For subsequent updates, you would create a new version of the launch template:
---------------------------------------------------------------------------------

aws ec2 create-launch-template-version \
  --launch-template-name my-node-template \
  --version-description v2 \
  --launch-template-data '{"imageId": "<new-ami-id>", "instanceType": "t3.medium", "userData": "<base64-encoded-user-data>"}'



#TF CODE

resource "aws_launch_template" "self_managed_nodes" {
  name_prefix   = "my-node-template-"
  description   = "Launch template for self-managed EKS nodes"
  image_id      = var.new_ami_id               # <--- Update AMI here
  instance_type = "t3.medium"

  user_data = base64encode(file("${path.module}/userdata.sh"))

  lifecycle {
    create_before_destroy = true
  }

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name        = "eks-self-managed-node"
      Environment = var.environment
    }
  }

  metadata_options {
    http_endpoint = "enabled"
    http_tokens   = "required"
  }
}




optional



Attach Launch Template to ASG
-------------------------------


resource "aws_autoscaling_group" "eks_nodes" {
  desired_capacity     = 2
  max_size             = 3
  min_size             = 1
  vpc_zone_identifier  = var.subnet_ids
  launch_template {
    id      = aws_launch_template.self_managed_nodes.id
    version = "$Latest"
  }

  tag {
    key                 = "kubernetes.io/cluster/${var.cluster_name}"
    value               = "owned"
    propagate_at_launch = true
  }
}

















2. Update Auto Scaling Group (ASG) with New Launch Template Version:
------------------------------------------------------------------------

aws autoscaling update-auto-scaling-group \
  --auto-scaling-group-name <asg-name> \
  --launch-template LaunchTemplateName=my-node-template,Version=<new-version>



#TF CODE


resource "aws_autoscaling_group" "eks_nodes" {
  name                      = "my-eks-node-asg"
  desired_capacity          = 2
  min_size                  = 1
  max_size                  = 3
  vpc_zone_identifier       = var.subnet_ids
  health_check_type         = "EC2"
  health_check_grace_period = 300

  launch_template {
    name    = aws_launch_template.self_managed_nodes.name
    version = var.launch_template_version  # e.g., "2" or "$Latest"
  }

  tag {
    key                 = "kubernetes.io/cluster/${var.cluster_name}"
    value               = "owned"
    propagate_at_launch = true
  }

  lifecycle {
    create_before_destroy = true
  }
}










3. Create New Node Group with Updated Launch Template:
--------------------------------------------------------------

eksctl create nodegroup \
  --cluster <cluster-name> \
  --name <new-nodegroup-name> \
  --node-type t3.medium \
  --nodes 2 \
  --kubernetes-version 1.30 \
  --launch-template <template-id> \
  --region us-east-1



###TF CODE

resource "aws_autoscaling_group" "self_managed_asg" {
  name_prefix            = "eks-self-managed-"
  desired_capacity       = 2
  min_size               = 1
  max_size               = 3
  vpc_zone_identifier    = var.subnet_ids
  health_check_type      = "EC2"
  health_check_grace_period = 300

  launch_template {
    id      = aws_launch_template.self_managed_nodes.id
    version = "$Latest"
  }

  tag {
    key                 = "kubernetes.io/cluster/${var.cluster_name}"
    value               = "owned"
    propagate_at_launch = true
  }

  lifecycle {
    create_before_destroy = true
  }
}









4. Cordon and Drain Old Nodes:
----------------------------------


resource "null_resource" "cordon_old_node" {
  provisioner "local-exec" {
    command = "kubectl cordon ${var.node_name}"
  }
  
  triggers = {
    node_name = var.node_name
  }
}



resource "null_resource" "drain_old_node" {
  provisioner "local-exec" {
    command = "kubectl drain ${var.node_name} --ignore-daemonsets --delete-emptydir-data"
  }
  
  triggers = {
    node_name = var.node_name
  }
}


Cordon the old node to mark it as unschedulable:
-------------------------------------------------

kubectl cordon <node-name>



Drain the old node to safely migrate the workloads:
-----------------------------------------------------

kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data




5.Terminate Old Nodes:
----------------------

aws autoscaling terminate-instance-in-auto-scaling-group \
  --instance-id <old-instance-id> \
  --no-should-decrement-desired-capacity


resource "null_resource" "terminate_instance" {
  triggers = {
    instance_id = var.old_instance_id
  }

  provisioner "local-exec" {
    command = "aws autoscaling terminate-instance-in-auto-scaling-group --instance-id ${var.old_instance_id} --no-should-decrement-desired-capacity"
  }
}






6. Check Node Health and Status:
------------------------------------

kubectl get nodes



7. Add-on Management:
------------------------



aws eks update-addon --cluster-name <cluster-name> --addon-name vpc-cni --region us-east-1 --resolve-conflicts OVERWRITE <br>
aws eks update-addon --cluster-name <cluster-name> --addon-name kube-proxy --region us-east-1 --resolve-conflicts OVERWRITE<br>

aws eks update-addon --cluster-name <cluster-name> --addon-name coredns --region us-east-1 --resolve-conflicts OVERWRITE<br>


##TF CODE


provider "aws" {
  region = "us-east-1"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
}

resource "aws_eks_addon" "vpc_cni" {
  cluster_name             = var.cluster_name
  addon_name               = "vpc-cni"
  resolve_conflicts        = "OVERWRITE"
}

resource "aws_eks_addon" "kube_proxy" {
  cluster_name             = var.cluster_name
  addon_name               = "kube-proxy"
  resolve_conflicts        = "OVERWRITE"
}

resource "aws_eks_addon" "coredns" {
  cluster_name             = var.cluster_name
  addon_name               = "coredns"
  resolve_conflicts        = "OVERWRITE"
}







8. Post-Upgrade Validation:
------------------------------


Check Node Status:
-------------------

kubectl get nodes



Check ALB Health:
-------------------

Ensure that the ALB target group health checks are passing after deployment

aws elbv2 describe-target-health --target-group-arn <target-group-arn>



Check Pod Health:
-------------------

kubectl describe pod <pod-name> | grep "Readiness"
kubectl describe pod <pod-name> | grep "Liveness"



Rollback Strategy:
-------------------



aws autoscaling update-auto-scaling-group \
  --auto-scaling-group-name <asg-name> \
  --launch-template LaunchTemplateName=my-node-template,Version=<previous-version>


###TF CODE

resource "aws_launch_template" "eks_nodes" {
  name          = "my-node-template"
  image_id      = var.ami_id
  instance_type = "t3.medium"

  # Optional: Add user_data, key_name, etc.
}

resource "aws_autoscaling_group" "eks_nodes_asg" {
  name                      = "my-eks-node-asg"
  max_size                  = 3
  min_size                  = 1
  desired_capacity          = 2
  vpc_zone_identifier       = var.subnet_ids
  health_check_type         = "EC2"
  health_check_grace_period = 300

  launch_template {
    id      = aws_launch_template.eks_nodes.id
    version = var.launch_template_version  # This is where you pin the version
  }

  tag {
    key                 = "kubernetes.io/cluster/${var.cluster_name}"
    value               = "owned"
    propagate_at_launch = true
  }
}
















```

Final Thoughts:
-----------------

By using self-managed node groups with Launch Templates, you're able to maintain full control over the node  infrastructure. <br>
This allows for a more customized setup and a clearer upgrade path that aligns with your blue-green deployment strategy while ensuring zero downtime. <br>
You can automate most of the upgrade steps using Terraform, eksctl, and kubectl commands, making the process repeatable, reliable, and seamless.<br>















