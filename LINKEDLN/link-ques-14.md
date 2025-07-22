


# DevOps Interview Q&A

| #  | Question | Answer |
|----|----------|--------|
| 1 | How do you pass parameters between stages in a Jenkins declarative pipeline? | Use `environment` or `script` block with `env` variables. Shared variables can be declared globally or passed via `stash/unstash`, or `write/read` files if needed. |
| 2 | What is an agent in Jenkins? How do you configure a pipeline to run on a specific agent? | An agent defines where the pipeline or a stage runs. Use `agent { label 'my-agent' }` to assign a specific node. |
| 3 | Explain how you use shared libraries in Jenkins. | Shared libraries are reusable code stored in SCM. You load them using `@Library('my-shared-lib')` and define logic in `vars/` and `src/` folders. |
| 4 | Have you handled parallel execution in a pipeline? How and why? | Yes, using `parallel` block in declarative or scripted pipelines to speed up builds or run independent jobs like tests in parallel. |
| 5 | How do you implement approval gates in a Jenkins pipeline? | Use `input` step inside a `stage` for manual approvals, e.g., before deploying to production. |
| 6 | What is the difference between rebase and merge? | Rebase rewrites commit history; merge preserves it. In CI/CD, rebase is useful for clean history; merge is safer for team workflows. |
| 7 | How do you manage version control for infrastructure (Terraform/Ansible) in Git? | Maintain separate branches or folders per environment, use PRs for changes, and tag stable releases. |
| 8 | How do you trigger a pipeline based on a Git tag push? | Use a trigger like `when { tag "*" }` or configure Git webhooks for tag events. |
| 9 | Have you used Git hooks or automation to enforce commit message standards? | Yes, using pre-commit hooks with regex or tools like `commitlint` to enforce message formats. |
| 10 | How do you manage sensitive variables and secrets in Terraform? | Use `terraform.tfvars` excluded from VCS, or better, external secret managers like AWS Secrets Manager, Azure Key Vault, or Vault. |
| 11 | What happens if someone manually changes infra outside of Terraform? | Terraform shows drift in `terraform plan`. To fix, either `import` changes or reapply desired state. |
| 12 | What is the difference between `terraform taint` and `terraform import`? | `taint` forces resource recreation; `import` brings existing resources under Terraform control. |
| 13 | How do you organize Terraform code for a multi-environment setup? | Use workspace-based isolation, or directory structure per environment (`env/dev`, `env/prod`) with shared modules. |
| 14 | What is the difference between Azure Resource Group and AWS VPC? | Resource Group is a logical container; VPC is a virtual network. They serve different purposes. |
| 15 | How do you automate VM provisioning in Azure or AWS with Terraform? | Define `azurerm_virtual_machine` or `aws_instance`, configure image, networking, and credentials. |
| 16 | What is Azure DevOps YAML pipeline? | It's a code-defined CI/CD pipeline in YAML. Use `stages`, `jobs`, and `steps` for structure and reuse templates. |
| 17 | Explain Azure Service Principal in DevOps pipelines. | It's a non-interactive identity used to authenticate scripts/apps with Azure via RBAC. |
| 18 | What cloud-native monitoring/logging solutions have you used? | AWS CloudWatch, Azure Monitor & Log Analytics, Prometheus + Grafana. |
| 19 | Container runs locally but fails on Jenkins – how do you debug? | Check Dockerfile path context, Jenkins agent capabilities, volume mounts, and network settings. |
| 20 | How do you use Kubernetes probes? | `livenessProbe` restarts unhealthy containers; `readinessProbe` controls traffic routing. Helps in high availability and stability. |
| 21 | How do you do Helm-based deployments in Kubernetes? | Use `helm upgrade --install`, manage charts in Git, and use values.yaml for customization. |
| 22 | Difference between StatefulSet and Deployment in Kubernetes? | Deployment is for stateless apps, StatefulSet for stateful apps with stable identities and volumes. |
| 23 | How do you store/access persistent data in Kubernetes? | Use Persistent Volumes (PVs) and Persistent Volume Claims (PVCs), backed by cloud storage. |
| 24 | How do you audit and rotate credentials in DevOps tools? | Use centralized secret managers, enable audit logs, rotate via automation or expiry policies. |
| 25 | Approach to shift-left testing in DevOps? | Run unit, lint, and security tests early in the pipeline using tools like `pytest`, `eslint`, `trivy`. |
| 26 | What tools have you used for vulnerability scanning? | Trivy, Aqua, Snyk, Clair, and Checkov for IaC scanning. |
| 27 | How do you enable RBAC in K8s or IAM in cloud? | Define Roles and RoleBindings (K8s) or IAM policies (AWS/Azure) with least privilege principles. |
| 28 | How do you manage post-deployment monitoring and alerts? | Use Prometheus, Grafana, CloudWatch, Azure Monitor. Set up alerts for SLIs, errors, and latency thresholds. |
