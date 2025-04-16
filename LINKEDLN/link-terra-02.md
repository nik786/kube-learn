

Having conducted many DevOps interviews, let me share what really matters when it comes to Terraform questions.

1) What happens if your state file is accidentally deleted?
Answer: Terraform loses track of managed infrastructure. On next apply, it attempts to recreate everything, causing duplicates or failures. Recovery requires manual imports or restoring backups. Always enable versioning on S3 state storage.

2) How do you handle large-scale refactoring without downtime?
Answer: Use "terraform state mv" to rename resources without destroying them. Control changes with targeted applies. Split refactoring into multiple non-destructive PRs and verify plans carefully to prevent resource destruction.

3) What happens if a resource fails halfway through a terraform apply?
Answer: Terraform creates a partial deployment with successful resources running but failed ones marked as tainted. Use targeted applies and "-refresh-only" to recover systematically.

4) How do you manage secrets in Terraform?
Answer: Use external secret stores (Vault, AWS Secrets Manager), ensure state encryption, mark outputs as sensitive, and integrate securely with CI/CD. For highly sensitive values, consider managing them outside Terraform completely.

5) What happens if terraform plan shows no changes but infrastructure was modified outside Terraform?
Answer: Terraform remains unaware until "terraform refresh" is run. Implement regular drift detection in your CI/CD process to catch unauthorized changes.

6) What happens if you delete a resource definition from your configuration?
Answer: Terraform destroys the corresponding infrastructure. Either use "terraform state rm" first or implement "lifecycle { prevent_destroy = true }" for critical resources.

7) What happens if Terraform provider APIs change between versions?
Answer: Compatibility issues may arise. Always read release notes, use version constraints, test upgrades in lower environments, and consider targeted updates for gradual migration.

8) How do you implement zero-downtime infrastructure updates?
Answer: Use "create_before_destroy" lifecycle blocks, blue-green deployments, health checks, and state manipulation for complex scenarios. For databases, use replicas or managed services with failover capabilities.

9) What happens if you have circular dependencies in your Terraform modules?
Answer: Terraform fails with "dependency cycle" errors. Refactor module structure using data sources, outputs, or restructuring resources to establish clear dependency hierarchy.

10) What happens if you rename a resource in your Terraform code?
Answer: Terraform sees this as destroying and recreating the resource. Use "terraform state mv" to update state while preserving infrastructure, avoiding rebuilds and downtime.
