

### EKS Upgrade Strategy in Production with Terraform, GitLab, and Blue-Green Deployments

| **Category**               | **Details** |
|---------------------------|-------------|
| **Approach**              | We follow a step-by-step and automated process to upgrade EKS in production without any downtime. |
| **Infrastructure as Code** | - All resources (EKS cluster, launch templates, node groups, add-ons) are defined and managed using **Terraform**.<br>- Code changes are tracked in **GitLab**.<br>- We use **GitLab deployment pipelines** to apply infrastructure changes. |
| **Pre-Upgrade Validation** | - All upgrades are first tested in a **staging cluster**.<br>- This helps check Kubernetes version compatibility, add-on behavior, and AMI readiness. |
| **Control Plane Upgrade** | - Performed using the `aws eks update-cluster-version` command.<br>- We monitor the upgrade until the cluster becomes `ACTIVE`. |
| **Blue-Green Node Upgrade** | - Create a **new launch template** with the updated AMI.<br>- Deploy a **new Auto Scaling Group** using Terraform.<br>- Add new nodes slowly.<br>- Drain and remove old nodes one at a time after checking that workloads have moved safely. |
| **Add-on Management**      | - Upgrade add-ons like `vpc-cni`, `kube-proxy`, and `coredns` using `aws eks update-addon`.<br>- Use `--resolve-conflicts OVERWRITE` when needed.<br>- Confirm success with `describe-addon`. |
| **Monitoring & Observability** | - We monitor node and pod health using **Prometheus**, **Grafana**, and **CloudWatch**.<br>- Alerts are active during the entire upgrade process. |
| **Rollback Strategy**     | - We keep older AMIs and launch template versions.<br>- Rollback is done by reverting changes in GitLab and reapplying with Terraform. |
| **Post-Upgrade Validation** | - Use `kubectl get nodes` and application-level checks.<br>- Make sure all nodes are healthy and workloads are running fine. |
