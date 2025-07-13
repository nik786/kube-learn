

1. How would you implement immutable infrastructure using containers and Infrastructure-as-Code tools like Terraform?

| Strategy                                                                 | Description                                                                                                 |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Use Container Images for All Deployments                                 | Build versioned, self-contained container images (e.g., with Docker) to package your applications and dependencies. |
| Define Complete Infrastructure in Terraform                              | Use Terraform to declaratively define cloud resources like compute instances, networking, and storage.     |
| Replace Instead of Modify                                                | Design your Terraform code and container pipelines to destroy and recreate infrastructure during updates.  |
| Use Versioned AMIs or Base Images                                        | Use immutable, version-tagged base images or custom AMIs to ensure consistent environments.                |
| Automate CI/CD with Image + IaC Deployment Pipelines                     | Integrate Terraform and container image builds into CI/CD pipelines for consistent, automated rollouts.    |



2. Pick any DevOps tool you’ve worked with and explain its most common failure modes in production. How do you mitigate them?


| Failure Mode                                | Description                                                                 | Mitigation Strategy                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Host Unreachability                         | Ansible fails when target machines are down or have SSH/network issues.    | Implement inventory validation, use `ping` module checks before major playbooks run.  |
| Idempotency Breaks                          | Tasks make unintended changes when run multiple times.                     | Ensure playbooks are idempotent using `when`, `creates`, `changed_when` logic.        |
| Variable Conflicts and Scope Issues         | Overlapping variables from different sources cause unpredictable behavior. | Use clear variable precedence and structure with group/host vars and role defaults.   |
| Silent Failures in Tasks                    | Tasks that fail silently due to missing `failed_when` or poor error checks.| Use `failed_when`, `register`, and `debug` for better visibility into task outcomes.  |
| Long Execution Times and Serial Bottlenecks | Playbooks executing serially take too long on large fleets.               | Use `serial`, `async`, `poll`, and parallel execution to improve performance.         |


| Failure Mode                                | Description                                                                 | Mitigation Strategy                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| State File Corruption or Loss               | Losing or corrupting the state file can break environment tracking.        | Store state remotely using backends like S3 with locking (e.g., DynamoDB).            |
| Resource Drift                              | Manual changes in cloud console cause drift from declared state.           | Run `terraform plan` regularly and use `terraform drift detection` tools or policies. |
| Improper Resource Dependencies              | Missing `depends_on` causes incorrect resource creation order.             | Explicitly define dependencies where required to ensure proper orchestration.         |
| Concurrent Updates                          | Multiple people applying changes at the same time cause conflicts.         | Use remote state locking and CI pipelines to serialize Terraform operations.          |
| Destroying Resources Unintentionally        | Misconfigurations can delete critical infrastructure during `apply`.       | Use `lifecycle` rules like `prevent_destroy` and review plans carefully before apply. |


3. Describe a task or workflow you intentionally chose not to automate. Why did you make that decision?

| Task or Workflow                                | Reason for Not Automating                                                    |
|-------------------------------------------------|-------------------------------------------------------------------------------|
| One-time Infrastructure Migration               | Automation overhead not justified for a task done only once.                  |
| Manual Approval for High-Risk Deployments       | Human judgment required to validate changes in sensitive environments.        |
| Ad-hoc Debugging and Incident Response          | Dynamic and unpredictable steps make automation unreliable or inefficient.    |
| Frequent Business Logic Changes                 | Constantly changing rules make automation brittle and costly to maintain.     |
| Stakeholder Review and Sign-off Processes       | Requires contextual input, discussions, or decisions that can’t be scripted.  |



4.  How would you manage application rollouts across multiple Kubernetes clusters in different environments?


| Strategy                                              | Description                                                                 |
|-------------------------------------------------------|-----------------------------------------------------------------------------|
| Use GitOps for Declarative Deployments                | Manage environment-specific manifests in Git using tools like ArgoCD or Flux. |
| Environment-Specific Configuration via Helm/Kustomize | Templatize values per environment using tools like Helm charts or Kustomize. |
| Progressive Delivery with Feature Flags or Canary     | Gradually roll out changes using canary deployments or feature flag tools.   |
| Centralized CI/CD Pipeline with Environment Targets   | Use pipelines that promote builds from dev → staging → prod with approvals. |
| Cluster-Aware Deployment Automation                   | Use tools/scripts that understand context (cluster name, region, env) before deploying. |



5. Your monthly cloud bill is higher than expected, and you find unused volumes and load balancers. How do you track, clean, and prevent this?

| Action Step                                       | Description                                                                 |
|--------------------------------------------------|-----------------------------------------------------------------------------|
| Use Cloud Cost and Resource Monitoring Tools      | Leverage tools like AWS Cost Explorer, Azure Cost Management, or GCP Billing to identify unused resources. |
| Tag Resources with Owner and Lifecycle Info       | Enforce tagging policies to include metadata like owner, environment, and expiration. |
| Implement Scheduled Cleanup Jobs or Alerts        | Set up automation (e.g., Lambda, cronjobs) to delete unused volumes/ELBs or alert on idle state. |
| Audit with IaC Drift Detection Tools              | Use tools like Terraform Drift Detection or `infracost` to detect orphaned or unmanaged resources. |
| Enforce Resource Quotas and TTL Policies          | Apply policies via governance tools (e.g., AWS Config, OPA/Gatekeeper) to limit sprawl and enforce time-to-live. |


6. Your Kubernetes cluster’s autoscaler is launching too many nodes during peak hours, causing budget concerns. How do you control autoscaling more efficiently?


| Strategy                                           | Description                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------|
| Set Resource Requests and Limits Appropriately     | Ensure accurate CPU/memory requests to prevent over-provisioning by the autoscaler. |
| Use Priority Classes and Pod Disruption Budgets    | Control which workloads can scale or be evicted during peak demand.         |
| Tune Cluster Autoscaler or Use Karpenter/Fargate   | Customize scaling thresholds and leverage cost-aware autoscaling tools like Karpenter or Fargate. |
| Schedule Workloads to Off-Peak Hours               | Use `nodeAffinity` or `taints/tolerations` to defer non-critical jobs to off-peak periods. |
| Implement Horizontal Pod Autoscaler with Limits    | Cap autoscaling using `maxReplicas` and combine with vertical autoscaler for efficiency. |

7. You are designing a multi-region Kubernetes disaster recovery strategy for a regulated enterprise. How do you plan backup, failover, and restoration?

| DR Strategy Component                        | Description                                                                 |
|---------------------------------------------|-----------------------------------------------------------------------------|
| Scheduled Backups of Cluster State & Volumes | Use tools like Velero or Kasten to back up etcd data, PVCs, and metadata to a secure, remote location. |
| Active-Passive or Active-Active Cluster Design | Deploy clusters in multiple regions with DNS-based traffic routing and defined failover policies. |
| Replicate Persistent Data Across Regions     | Use cloud-native solutions (e.g., Amazon EBS Snapshots, GCP Filestore backup) or storage replication to keep data in sync. |
| Automate Restoration Workflows               | Script and test cluster recovery steps using IaC (Terraform, Helm) and GitOps workflows. |
| Regular DR Drills and Compliance Auditing    | Perform scheduled failover tests and log all activities for compliance reporting and SLAs. |


8. Your Kubernetes HPA (Horizontal Pod Autoscaler) is not scaling down even when CPU usage is low. What could be the root causes


| Root Cause                                         | Description                                                                 |
|----------------------------------------------------|-----------------------------------------------------------------------------|
| Misconfigured CPU Requests or Limits               | If CPU requests are set too low, HPA might think usage is higher than it actually is. |
| Cooldown Period or Stabilization Window            | HPA has built-in delay mechanisms (e.g., `stabilizationWindowSeconds`) that prevent rapid scale-down. |
| Minimum Replicas (`minReplicas`) Set Too High      | HPA will never scale below the `minReplicas` value, even if usage is low.   |
| Metrics Server Delay or Inaccuracy                 | HPA depends on metrics-server; stale or missing metrics can block scaling actions. |
| Non-CPU Based Bottlenecks                          | Low CPU may not trigger scale-down if other resources (like memory or custom metrics) are still high. |



9. You are required to perform maintenance on a node without causing service disruption. How would you safely drain the node and ensure high availability?

| Step                                               | Description                                                                 |
|----------------------------------------------------|-----------------------------------------------------------------------------|
| Cordon the Node                                    | Prevent new pods from being scheduled using `kubectl cordon <node-name>`.   |
| Drain the Node with Pod Rescheduling               | Use `kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data` to safely evict pods. |
| Ensure PodDisruptionBudgets (PDBs) Are Respected   | Configure PDBs to avoid evicting too many replicas at once and ensure HA.   |
| Verify Rescheduled Pods Are Running                | Monitor that evicted pods are rescheduled and running on other nodes successfully. |
| Uncordon After Maintenance (If Applicable)         | Bring node back into the pool using `kubectl uncordon <node-name>` if returning it to service. |


   



















