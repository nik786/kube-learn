



# Terraform Interview Questions – Advanced Scenario-Based

| **#** | **Question** | **Answer** |
|------|--------------|------------|
| 1 | What happens if your state file is accidentally deleted? | Terraform loses track of managed infrastructure. On the next apply, it may recreate everything, causing duplicates or failures. Recovery requires manual imports or restoring backups. Always enable versioning on S3 state storage. |
| 2 | How do you handle large-scale refactoring without downtime? | Use `terraform state mv` to rename resources without destroying them. Apply changes in stages with targeted applies. Break refactoring into multiple non-destructive PRs and carefully review plans. |
| 3 | What happens if a resource fails halfway through a `terraform apply`? | Terraform creates a partial deployment. Successful resources remain, failed ones are tainted. Use targeted applies and `-refresh-only` to recover and complete the deployment. |
| 4 | How do you manage secrets in Terraform? | Use external secret managers like Vault or AWS Secrets Manager. Enable state encryption, mark outputs as `sensitive`, and secure CI/CD integrations. For critical secrets, consider managing them entirely outside Terraform. |
| 5 | What happens if `terraform plan` shows no changes, but infrastructure was modified outside Terraform? | Terraform remains unaware until you run `terraform refresh`. Implement drift detection regularly in CI/CD to identify unauthorized or manual changes. |
| 6 | What happens if you delete a resource definition from your configuration? | Terraform will destroy the corresponding infrastructure. To avoid this, use `terraform state rm` or `lifecycle { prevent_destroy = true }` for critical resources. |
| 7 | What happens if Terraform provider APIs change between versions? | Compatibility issues can occur. Read release notes, use version constraints, and test in lower environments before upgrading. Use targeted updates to migrate gradually. |
| 8 | How do you implement zero-downtime infrastructure updates? | Use `create_before_destroy`, blue-green deployments, and health checks. For complex updates, manipulate state carefully. Use replicas or managed services with automatic failover for databases. |
| 9 | What happens if you have circular dependencies in your Terraform modules? | Terraform fails with a "dependency cycle" error. Refactor the module structure using outputs, data sources, or restructure resources to establish a clear dependency order. |
| 10 | What happens if you rename a resource in your Terraform code? | Terraform treats it as a destroy and recreate operation. Use `terraform state mv` to rename resources in the state file and preserve existing infrastructure. |
