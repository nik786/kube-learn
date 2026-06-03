
| **Step** | **Action** | **AWS CLI Command** | **Notes** |
|---------|------------|----------------------|-----------|
| **1** | Check current cluster version | `aws eks describe-cluster --name my-cluster --query 'cluster.version'` | Ensure you're upgrading from 1.29 to 1.30. |
| **2** | Upgrade the control plane | `aws eks update-cluster-version --name my-cluster --kubernetes-version 1.30` | AWS automatically upgrades control plane nodes one by one. |
| **3** | Monitor upgrade status | `aws eks describe-cluster --name my-cluster --query 'cluster.status'` | Wait until the status changes to `ACTIVE`. |
| **4** | List all EKS-managed add-ons | `aws eks list-addons --cluster-name my-cluster` | Identify installed add-ons before upgrading. |
| **5** | Upgrade each add-on | `aws eks update-addon --cluster-name my-cluster --addon-name <addon-name> --resolve-conflicts OVERWRITE` | Replace `<addon-name>` with add-on names like `vpc-cni`, `kube-proxy`, `coredns`. |
| **6** | Verify add-on upgrade | `aws eks describe-addon --cluster-name my-cluster --addon-name <addon-name>` | Ensure all add-ons are successfully upgraded. |
| **7** | Fetch current launch template ID and version | `aws ec2 describe-launch-templates --query 'LaunchTemplates[].{ID:LaunchTemplateId,Version:LatestVersionNumber}'` | Identify the latest launch template version used by the self-managed nodes. |
| **8** | Create a new launch template version | `aws ec2 create-launch-template-version --launch-template-id <template-id> --source-version <old-version> --launch-template-data '{"ImageId":"ami-new-k8s-1.30"}'` | Ensure the new version uses an AMI compatible with **EKS 1.30**. |
| **9** | Fetch the current self-managed node group ASG | `aws autoscaling describe-auto-scaling-groups --query 'AutoScalingGroups[].{Name:AutoScalingGroupName}'` | Identify the Auto Scaling Group (ASG) associated with the nodes. |
| **10** | Update ASG to use new launch template version | `aws autoscaling update-auto-scaling-group --auto-scaling-group-name <asg-name> --launch-template LaunchTemplateId=<template-id>,Version=<new-version>` | Ensures new nodes are launched with the updated version. |
| **11** | Drain old nodes gracefully | `kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data` | Prevents pod disruption and ensures safe termination of old nodes. |
| **12** | Scale out new nodes before terminating old ones | `aws autoscaling set-desired-capacity --auto-scaling-group-name <asg-name> --desired-capacity <new-count>` | Add new nodes first to avoid downtime. |
| **13** | Terminate old nodes | `aws autoscaling terminate-instance-in-auto-scaling-group --instance-id <old-instance-id> --no-should-decrement-desired-capacity` | Ensures rolling replacement without reducing capacity. |
| **14** | Verify node health | `kubectl get nodes` | Ensure all nodes are ready and running **EKS 1.30**. |
| **15** | Cleanup unused old launch template versions | `aws ec2 delete-launch-template-versions --launch-template-id <template-id> --versions <old-version>` | Remove outdated versions for security and best practices. |




| **Step** | **Action** | **AWS CLI Command** | **Notes** |
|---------|------------|----------------------|-----------|
| **1** | Check current cluster version | `aws eks describe-cluster --name gl-dev-cluster --region us-east-1 --query 'cluster.version'` | Ensure you're upgrading from 1.29 to 1.30. |
| **2** | Upgrade the control plane | `aws eks update-cluster-version --name gl-dev-cluster --region us-east-1 --kubernetes-version 1.30` | AWS automatically upgrades control plane nodes one by one. |
| **3** | Monitor upgrade status | `aws eks describe-cluster --name gl-dev-cluster --region us-east-1 --query 'cluster.status'` | Wait until the status changes to `ACTIVE`. |
| **4** | List all EKS-managed add-ons | `aws eks list-addons --cluster-name gl-dev-cluster --region us-east-1` | Identify installed add-ons before upgrading. |
| **5** | Upgrade each add-on | `aws eks update-addon --cluster-name gl-dev-cluster --region us-east-1 --addon-name <addon-name> --resolve-conflicts OVERWRITE` | Replace `<addon-name>` with add-ons like `vpc-cni`, `kube-proxy`, `coredns`. |
| **6** | Verify add-on upgrade | `aws eks describe-addon --cluster-name gl-dev-cluster --region us-east-1 --addon-name <addon-name>` | Ensure all add-ons are successfully upgraded. |
| **7** | Fetch current launch template ID and version | `aws ec2 describe-launch-templates --region us-east-1 --query 'LaunchTemplates[].{ID:LaunchTemplateId,Version:LatestVersionNumber}'` | Identify the latest launch template version used by self-managed nodes. |
| **8** | Create a new launch template version | `aws ec2 create-launch-template-version --region us-east-1 --launch-template-id <template-id> --source-version <old-version> --launch-template-data '{"ImageId":"ami-new-k8s-1.30"}'` | Ensure the new version uses an AMI compatible with **EKS 1.30**. |
| **9** | Fetch the current self-managed node group ASG | `aws autoscaling describe-auto-scaling-groups --region us-east-1 --query 'AutoScalingGroups[].{Name:AutoScalingGroupName}'` | Identify the Auto Scaling Group (ASG) associated with the nodes. |
| **10** | Update ASG to use new launch template version | `aws autoscaling update-auto-scaling-group --region us-east-1 --auto-scaling-group-name <asg-name> --launch-template LaunchTemplateId=<template-id>,Version=<new-version>` | Ensures new nodes are launched with the updated version. |
| **11** | Drain old nodes gracefully | `kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data` | Prevents pod disruption and ensures safe termination of old nodes. |
| **12** | Scale out new nodes before terminating old ones | `aws autoscaling set-desired-capacity --region us-east-1 --auto-scaling-group-name <asg-name> --desired-capacity <new-count>` | Add new nodes first to avoid downtime. |
| **13** | Terminate old nodes | `aws autoscaling terminate-instance-in-auto-scaling-group --region us-east-1 --instance-id <old-instance-id> --no-should-decrement-desired-capacity` | Ensures rolling replacement without reducing capacity. |
| **14** | Verify node health | `kubectl get nodes` | Ensure all nodes are ready and running **EKS 1.30**. |
| **15** | Cleanup unused old launch template versions | `aws ec2 delete-launch-template-versions --region us-east-1 --launch-template-id <template-id> --versions <old-version>` | Remove outdated versions for security and best practices. |
