

1. What if the Terraform state file gets deleted?
 Terraform loses track of your infrastructure.
 ✅ Always back up state files (use S3 with versioning).
 ✅ Use terraform import if needed to reconnect resources.

🔹 2. How to refactor code without downtime?
 ✅ Use terraform state mv to rename or move resources.
 ✅ Apply changes safely using targeted applies and non-destructive PRs.

🔹 3. What happens if a resource fails during terraform apply?
 Partial deployment can occur.
 ✅ Use terraform apply -target=resource to fix.
 ✅ -refresh-only helps to sync your local state.

🔹 4. How to manage secrets with Terraform?
 ✅ Never hardcode secrets!
 ✅ Integrate Vault, AWS Secrets Manager, or SSM Parameter Store.
 ✅ Use sensitive = true for outputs.

🔹 5. What if external changes are made to infrastructure but terraform plan shows no changes?
 Terraform won’t detect changes automatically.
 ✅ Run terraform refresh.
 ✅ Set up drift detection in CI/CD pipelines.

🔹 6. What if you delete a resource from the Terraform configuration?
 Terraform will destroy the resource!
 ✅ Add prevent_destroy = true inside lifecycle block.
 ✅ Or use terraform state rm to safely remove tracking.

🔹 7. What if the cloud provider APIs change?
 Potential compatibility issues.
 ✅ Always use version constraints.
 ✅ Test provider upgrades in lower environments before production.

🔹 8. How to achieve zero-downtime deployments?
 ✅ Use create_before_destroy strategy.
 ✅ Implement blue-green deployments.
 ✅ Monitor resources with health checks.

🔹 9. What happens with circular dependencies?
 Terraform throws dependency errors.
 ✅ Refactor using data sources and outputs.
 ✅ Split large modules when needed.

🔹 10. What if you rename a resource in Terraform?
 Terraform will destroy and recreate it by default.
 ✅ Use terraform state mv to safely rename without downtime.

🌟 Bonus Pro Tips:
 ✅ Share Terraform modules through versioned Git repositories.
 ✅ Use remote backends like S3 + DynamoDB for team collaboration.
 ✅ Plan safe rollbacks by snapshotting infrastructure.
 ✅ Schedule automated drift detection.
