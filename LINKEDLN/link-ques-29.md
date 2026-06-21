
How would you use Karpenter (or Cluster Autoscaler) to optimize workload placement dynamically?

| Strategy / Feature                               | Description                                                                                          |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Node Affinity & Taints/Tolerations**           | Define pod-level scheduling rules to guide autoscalers to place workloads on optimal instance types or zones. |
| **Provisioner Constraints (Karpenter)**          | Use `Provisioner` specs with constraints like `zones`, `instanceTypes`, `capacityType`, and `architecture` to align nodes with workload needs. |
| **Spot and On-Demand Mix**                       | Leverage Karpenter’s support for spot instances to lower costs while automatically falling back to on-demand during capacity shortages. |
| **Dynamic Right-Sizing**                         | Karpenter selects the best-fitting instance type at runtime based on resource requests, reducing overprovisioning. |
| **Topology-Aware Scheduling**                    | Combine autoscaler with `topologySpreadConstraints` and `PodTopologySpread` to distribute pods evenly across zones/regions. |



Your CI/CD pipeline is deploying to the wrong namespace intermittently. How do you debug and prevent this?

| Step / Best Practice                              | Description                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Review Pipeline Configuration**                 | Inspect CI/CD YAML or pipeline scripts for hardcoded or dynamically injected namespace values.         |
| **Use Namespace Validation in Manifests**         | Set explicit `namespace:` fields in all Kubernetes manifests to prevent defaulting to the wrong one.    |
| **Enable `kubectl config view` Logging**          | Log the active context and namespace (`kubectl config view --minify`) during deploy steps for visibility.|
| **Restrict Namespace Access via RBAC**            | Apply RoleBindings to limit CI/CD service accounts to only deploy into specific, approved namespaces.   |
| **Add Pre-Deploy Namespace Checks**               | Include CI pipeline steps to verify the target namespace exists and matches the expected environment.   |


A developer reports their pod is in CrashLoopBackOff. Walk them through the resolution process.

| Step                              | Description                                                                                          |
|-----------------------------------|------------------------------------------------------------------------------------------------------|
| **Check Pod Logs**                | Use `kubectl logs <pod-name> -c <container>` to view error messages and determine why the container is crashing. |
| **Inspect Events and Status**     | Run `kubectl describe pod <pod-name>` to check events, exit codes, and restart count for deeper insight. |
| **Validate Startup Command & Image** | Ensure the container's `command`, `args`, and image are correct and compatible with the container runtime. |
| **Check Resource Limits & Probes**| Review CPU/memory limits and readiness/liveness probes that might be too strict, causing premature restarts. |
| **Test Locally or Debug Pod**     | Reproduce the issue locally or use an ephemeral debug container (`kubectl debug`) to inspect runtime environment. |


How do you implement pod disruption budgets to ensure availability during node maintenance?

| Step / Principle                          | Description                                                                                          |
|-------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Define `minAvailable` or `maxUnavailable`** | Set a `PodDisruptionBudget` with either `minAvailable` (e.g., 2) or `maxUnavailable` (e.g., 1) to control how many pods can be evicted at once. |
| **Apply PDB to Critical Workloads**        | Attach PDBs to deployments or stateful sets that must remain highly available during voluntary disruptions. |
| **Use with Cluster Autoscaler or Karpenter** | Ensure autoscalers respect PDBs by preventing scale-in actions that violate the budget constraints.  |
| **Test During Maintenance Windows**        | Simulate drain operations (`kubectl drain`) to validate that the PDBs block disruptions as intended. |
| **Monitor Eviction Behavior**              | Use `kubectl get pdb` to track allowed disruptions and ensure PDBs are not overly restrictive (i.e., blocking upgrades). |




