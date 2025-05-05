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





# Blue-Green Deployment Strategy for EKS 1.30 Upgrade

| **Phase**        | **Blue-Green Action**                                                                 | **Explanation**                                                                 |
|------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **1. Preparation** | Treat existing nodes (EKS 1.29) as **Blue**. Create a new node group (EKS 1.30) as **Green** using a new launch template. | Runs both environments in parallel, reduces risk.                             |
| **2. Add Nodes**   | Deploy the Green ASG using the new launch template with EKS 1.30 compatible AMI.     | Use same capacity, taints, and labels as Blue to mirror environment.           |
| **3. Cordon Blue** | `kubectl cordon <blue-node>`                                                         | Prevents new pods from being scheduled on old nodes.                           |
| **4. Drain Blue**  | `kubectl drain <blue-node> --ignore-daemonsets --delete-emptydir-data`              | Safely migrates workloads to Green nodes.                                      |
| **5. Verify Green**| Monitor pod and node health using `kubectl get nodes`, `kubectl get pods`, and logs. | Ensure applications are stable on EKS 1.30.                                    |
| **6. Remove Blue** | Delete or scale down Blue ASG and clean up old launch template versions.             | Finalize the cutover to EKS 1.30 (Green).                                      |
| **7. Rollback**    | If issues arise, switch back to Blue nodes (EKS 1.29).                              | Quick recovery since Blue environment is preserved until success is confirmed. |
