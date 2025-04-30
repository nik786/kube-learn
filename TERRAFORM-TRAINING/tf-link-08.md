

1. What if the Terraform state file gets deleted?
   
 Terraform loses track of your infrastructure. <br>
 
 ✅ Always back up state files (use S3 with versioning). <br>
 ✅ Use terraform import if needed to reconnect resources.

🔹 2. How to refactor code without downtime?<br>
 ✅ Use terraform state mv to rename or move resources.<br>
 ✅ Apply changes safely using targeted applies and non-destructive PRs.

🔹 3. What happens if a resource fails during terraform apply?<br>

 Partial deployment can occur.<br>
 ✅ Use terraform apply -target=resource to fix.<br>
 ✅ -refresh-only helps to sync your local state.

🔹 4. How to manage secrets with Terraform?<br>

 ✅ Never hardcode secrets!<br>
 ✅ Integrate Vault, AWS Secrets Manager, or SSM Parameter Store.<br>
 ✅ Use sensitive = true for outputs.<br>

🔹 5. What if external changes are made to infrastructure but terraform plan shows no changes?<br>
 Terraform won’t detect changes automatically.<br>
 ✅ Run terraform refresh.<br>
 ✅ Set up drift detection in CI/CD pipelines.<br>

🔹 6. What if you delete a resource from the Terraform configuration?<br>
 
 Terraform will destroy the resource!<br>
 ✅ Add prevent_destroy = true inside lifecycle block.<br>
 ✅ Or use terraform state rm to safely remove tracking.<br>

🔹 7. What if the cloud provider APIs change?<br>

 Potential compatibility issues.<br>
 ✅ Always use version constraints.<br>
 ✅ Test provider upgrades in lower environments before production.<br>

🔹 8. How to achieve zero-downtime deployments?<br>

 ✅ Use create_before_destroy strategy.<br>
 ✅ Implement blue-green deployments.<br>
 ✅ Monitor resources with health checks.<br>

🔹 9. What happens with circular dependencies?<br>

 Terraform throws dependency errors.<br>
 
 ✅ Refactor using data sources and outputs.<br>
 ✅ Split large modules when needed.<br>

🔹 10. What if you rename a resource in Terraform? <br>

 Terraform will destroy and recreate it by default.<br>
 ✅ Use terraform state mv to safely rename without downtime.<br>

🌟 Bonus Pro Tips:

 ✅ Share Terraform modules through versioned Git repositories.<br>
 ✅ Use remote backends like S3 + DynamoDB for team collaboration.<br>
 ✅ Plan safe rollbacks by snapshotting infrastructure.<br>
 ✅ Schedule automated drift detection.<br>
