

1) What happens if the state file is deleted?
Terraform loses track of the current infrastructure, potentially leading to duplication. Recovery involves manual imports or restoring from backups. To mitigate, enable versioning on your S3 backend.

2) How can you refactor configurations without causing downtime?
Use terraform state mv to rename resources safely. Apply changes selectively and organize them into non-destructive pull requests.

3) What if a resource fails during apply?
Terraform might leave the environment in a partially deployed state. Use targeted applies and the -refresh-only flag to recover cleanly.

4) How do you handle secrets in Terraform?
Store secrets securely using services like Vault or AWS Secrets Manager. Ensure encryption at rest and mark sensitive outputs accordingly.

5) Why might terraform plan show no changes even after infrastructure has been modified externally?
Terraform won’t detect external changes until terraform refresh is executed. Integrate drift detection into your CI/CD pipeline.

6) What happens if you remove a resource from the configuration?
Terraform interprets this as a signal to destroy the resource. To prevent accidental destruction, use terraform state rm or add a lifecycle rule like prevent_destroy = true.

7) What if the provider API changes?
These changes can cause compatibility issues. Always review release notes, use provider version constraints, and test upgrades in staging before applying them in production.

8) How do you perform zero-downtime updates?
Leverage strategies like create_before_destroy, blue-green deployments, and health checks to maintain availability during updates.

9) What should you do about circular dependencies?
Terraform will fail with an error. Break the loop by refactoring with data sources or outputs to clearly define dependencies.

10) What if you rename a resource?
Terraform sees this as a new resource and will destroy the old one. Avoid this by using terraform state mv to preserve state and prevent downtime.
