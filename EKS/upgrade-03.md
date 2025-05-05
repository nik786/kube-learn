

### EKS Upgrade Strategy in Production with Terraform, GitOps, and Blue-Green Deployments

| **Category**               | **Details** |
|---------------------------|-------------|
| **Approach**              | Staged, automated, and zero-downtime upgrade process for EKS clusters in production. |
| **Infrastructure as Code** | - All resources (EKS cluster, launch templates, node groups, add-ons) managed via **Terraform**.<br>- Changes are version-controlled in **Git**.<br>- **GitOps** tools like **Argo CD** or **Flux** are used for deployment automation. |
| **Pre-Upgrade Validation** | - Validated in **staging clusters**.<br>- Ensures compatibility with Kubernetes version, add-on behavior, and AMI functionality. |
| **Control Plane Upgrade** | - Performed using `aws eks update-cluster-version`.<br>- Monitored via CLI/automation until cluster status is `ACTIVE`. |
| **Blue-Green Node Upgrade** | - **New Launch Template** created with upgraded AMI.<br>- **New ASG** provisioned via Terraform.<br>- **New nodes** added gradually.<br>- Old nodes are **cordoned and drained one-by-one**.<br>- Terminate only after confirming workload health. |
| **Add-on Management**      | - Upgrade EKS-managed add-ons (`vpc-cni`, `kube-proxy`, `coredns`) using `aws eks update-addon`.<br>- Use `--resolve-conflicts OVERWRITE`.<br>- Validate with `describe-addon`. |
| **Monitoring & Observability** | - Use **Prometheus**, **Grafana**, and **CloudWatch**.<br>- Alerts enabled on pod/node metrics throughout the rollout. |
| **Rollback Strategy**     | - **Previous AMIs** and **Launch Template versions** retained.<br>- Rollback by reverting Git commits and reapplying Terraform. |
| **Post-Upgrade Validation** | - Verify with `kubectl get nodes`, readiness probes, and app-level health checks.<br>- Confirm all nodes are Ready and workloads are stable. |
