
A misconfigured network policy is blocking traffic to essential services. How do you identify and fix it?

| Step | Description |
|------|-------------|
| 1. **Inspect Current Network Policies** | Use `kubectl get networkpolicy -A` and `kubectl describe networkpolicy <name>` to review existing rules and affected namespaces. |
| 2. **Test Pod Connectivity with Netshoot or BusyBox** | Deploy a diagnostic pod (e.g., Netshoot or BusyBox) to simulate traffic and test access to services using `curl`, `nc`, or `ping`. |
| 3. **Check Namespace and Label Selectors** | Ensure that the `podSelector`, `namespaceSelector`, and `matchLabels` in the policy correctly match the intended pods and namespaces. |
| 4. **Temporarily Remove or Isolate the Policy** | Safely disable or isolate the suspected NetworkPolicy and test traffic flow to verify if it's the root cause. |
| 5. **Apply a Least-Privilege, Allow-Listed Policy** | Re-create or refine the policy to explicitly allow required ingress/egress traffic while maintaining necessary restrictions. |



Describe your approach to managing secrets across multiple namespaces securely.

| Strategy | Description |
|----------|-------------|
| 1. **Use External Secret Management Tools** | Integrate tools like HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault with Kubernetes to centralize and securely inject secrets. |
| 2. **Leverage External Secrets Operator (ESO)** | Use ESO to sync secrets from external managers into specific namespaces, with RBAC-scoped access and lifecycle automation. |
| 3. **Namespace-Scoped RBAC Controls** | Restrict secret access using fine-grained RoleBindings and ClusterRoles to limit visibility to only authorized service accounts. |
| 4. **Encrypt Secrets at Rest and in Transit** | Ensure secrets are encrypted using KMS providers via Kubernetes EncryptionConfiguration and use TLS for all secret communications. |
| 5. **Audit and Rotate Secrets Regularly** | Enable auditing on secret usage and implement automatic rotation mechanisms via external tools or CI/CD pipelines to minimize exposure. |


What is your disaster recovery plan for a production Kubernetes cluster?

| Step | Description |
|------|-------------|
| 1. **Etcd Backup and Restore Strategy** | Schedule regular `etcd` snapshots and securely store them in remote storage (e.g., S3); test restores periodically. |
| 2. **Automated Cluster Infrastructure as Code (IaC)** | Use Terraform, Pulumi, or CloudFormation to recreate the cluster infrastructure reliably in another region or account. |
| 3. **Backup of Persistent Volumes** | Implement volume snapshotting or backup solutions like Velero to back up PVs used by stateful workloads. |
| 4. **Application Configuration Backup** | Store all manifests (Deployments, Services, ConfigMaps, Secrets) in Git with GitOps tools like ArgoCD or Flux for easy redeployment. |
| 5. **Run Disaster Recovery Drills** | Regularly simulate failure scenarios (e.g., region loss) and validate recovery time objectives (RTO) and recovery point objectives (RPO). |


You need to implement blue/green or canary deployments. How would you set that up using Kubernetes-native tools?

| Step | Description |
|------|-------------|
| 1. **Use Native Deployments with Labels and Selectors** | For blue/green, deploy two versions (e.g., `v1` and `v2`) with distinct labels; switch the Service selector to cut over. |
| 2. **Implement Canary Rollouts with Progressive Traffic Shifts** | Gradually shift traffic using `Deployment` with `maxUnavailable` and `maxSurge` or use tools like Argo Rollouts for fine-grained control. |
| 3. **Use Kubernetes Services for Traffic Management** | Manage routing between versions by updating the `Service` selector or using Ingress-based routing strategies for traffic control. |
| 4. **Monitor Metrics and Logs in Real-Time** | Integrate Prometheus, Grafana, and Loki to observe performance and errors during rollout to detect regressions quickly. |
| 5. **Automate Rollbacks on Failure** | Use health checks and `kubectl rollout undo deployment/<name>` or Argo Rollouts to trigger rollback if metrics breach thresholds. |


