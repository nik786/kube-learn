

Your application pods keep restarting frequently in production. Walk through your debugging approach.

| Step | Description |
|------|-------------|
| 1. **Check Pod Events and Status** | Use `kubectl describe pod <pod-name>` to inspect events for crash reasons like OOMKilled, CrashLoopBackOff, or failed probes. |
| 2. **Inspect Container Logs** | Run `kubectl logs <pod-name> --previous` to view logs from the last failed container instance and identify errors or panics. |
| 3. **Review Resource Requests and Limits** | Ensure CPU and memory requests/limits are configured appropriately; frequent restarts may indicate resource exhaustion. |
| 4. **Validate Liveness and Readiness Probes** | Misconfigured probes can cause the kubelet to kill healthy pods; verify probe paths, ports, and timing thresholds. |
| 5. **Monitor for Dependency or Config Failures** | Confirm that environment variables, ConfigMaps, Secrets, and dependent services (e.g., databases) are correctly configured and available. |


You've been asked to migrate from a self-managed Kubernetes cluster to EKS. What key considerations and steps would you follow?

A deployment rollout is stuck. How do you troubleshoot and fix the issue?

| Step | Description |
|------|-------------|
| 1. **Check Rollout Status** | Run `kubectl rollout status deployment/<name>` to see if it's waiting on unavailable pods or failing health checks. |
| 2. **Describe the Deployment and Pods** | Use `kubectl describe deployment <name>` and `kubectl describe pod <pod-name>` to inspect events like image pull errors or probe failures. |
| 3. **Review Pod Logs** | Run `kubectl logs <pod-name>` and `kubectl logs <pod-name> --previous` to catch runtime or init container issues during startup. |
| 4. **Inspect ReplicaSet and Strategy Settings** | Confirm the `maxUnavailable` and `maxSurge` settings aren't blocking progress; check if the new ReplicaSet is scaling up. |
| 5. **Pause, Fix, and Resume the Rollout** | Pause the rollout using `kubectl rollout pause`, fix the issue (e.g., image, config), and then resume with `kubectl rollout resume`. |


How would you handle a Kubernetes cluster upgrade with zero downtime?

| Step | Description |
|------|-------------|
| 1. **Plan Upgrade with Compatibility Checks** | Review release notes, deprecated APIs, and validate Helm charts and CRDs using tools like `pluto` or `kube-no-trouble`. |
| 2. **Use a Blue-Green or Rolling Node Upgrade Strategy** | Upgrade nodes one by one using `kubectl drain` and `kubectl cordon` to safely move workloads without disruption. |
| 3. **Enable PodDisruptionBudgets (PDBs)** | Define PDBs to ensure critical workloads maintain minimum availability during node reboots or evictions. |
| 4. **Upgrade Control Plane Before Worker Nodes** | Follow proper order—upgrade control plane first, then nodes—to maintain cluster stability and scheduling capabilities. |
| 5. **Monitor Workloads and Metrics During Upgrade** | Use Prometheus/Grafana and `kubectl get pods -A -w` to monitor service health, restarts, and performance throughout the process. |


A service that depends on persistent volumes is randomly failing. How would you investigate and resolve the issue?

| Step | Description |
|------|-------------|
| 1. **Check Pod Events and Volume Mount Errors** | Use `kubectl describe pod <name>` to look for volume mount failures, timeouts, or permission issues in the events section. |
| 2. **Verify PVC and PV Binding Status** | Run `kubectl get pvc` and `kubectl describe pvc <name>` to ensure the PersistentVolumeClaim is properly bound to a healthy PV. |
| 3. **Inspect Storage Class and Provisioner Logs** | Check if the dynamic provisioner (e.g., EBS, AzureDisk, Ceph) is misconfigured or experiencing intermittent issues. |
| 4. **Check Node Availability and Volume Attachments** | Use `kubectl get nodes` and your cloud provider console/CLI to confirm that the volume is correctly attached to the hosting node. |
| 5. **Review Filesystem Health and Access Patterns** | Exec into the pod to inspect filesystem integrity (`df -h`, `ls`, `touch`), and monitor if shared volumes are being accessed simultaneously in unsupported modes. |


You've detected increased latency in inter-pod communication. What tools and steps would you use to troubleshoot?

| Step | Description |
|------|-------------|
| 1. **Use Distributed Tracing Tools** | Implement tools like Jaeger or OpenTelemetry to trace requests between services and pinpoint high-latency hops. |
| 2. **Check CNI Plugin Health and Logs** | Inspect logs and status of the Container Network Interface (e.g., Cilium, Calico, Weave) for errors, delays, or misconfigurations. |
| 3. **Run Network Performance Tests Between Pods** | Use tools like `iperf3`, `ping`, or `netperf` between pods in different nodes or namespaces to measure raw latency. |
| 4. **Analyze Network Policies and QoS** | Ensure `NetworkPolicy` rules are not introducing unnecessary routing or restrictions; check QoS classes for throttling. |
| 5. **Monitor Node and Interface Metrics** | Use Prometheus to monitor metrics like `node_network_transmit_queue_length` or `container_network_latency_seconds` for congestion signs. |


You need to enforce specific resource limits and security controls on multi-tenant workloads. How would you implement that?

| Strategy | Description |
|----------|-------------|
| 1. **Use Namespaces with Resource Quotas and LimitRanges** | Enforce CPU/memory usage caps per tenant using `ResourceQuota` and `LimitRange` objects in each namespace. |
| 2. **Apply PodSecurity Standards or OPA/Gatekeeper Policies** | Restrict privilege escalation, host access, and unsafe capabilities using built-in PodSecurity levels or custom Gatekeeper constraints. |
| 3. **Isolate Network Traffic with NetworkPolicies** | Use Kubernetes `NetworkPolicy` to limit communication between tenants, enforcing strict inter-namespace traffic boundaries. |
| 4. **Use RBAC for Tenant-Specific Access Control** | Define RoleBindings and ClusterRoleBindings to grant least-privilege access to tenant teams within their namespaces. |
| 5. **Monitor and Audit with Multi-Tenant Observability Tools** | Integrate tools like Prometheus, Loki, and Kyverno with label-based scoping to track and enforce tenant-specific usage and policy compliance. |


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


One of your worker nodes has disk pressure and is evicting pods. What’s your response and long-term fix?

| Step | Description |
|------|-------------|
| 1. **Identify the Affected Node and Pods** | Use `kubectl describe node <node-name>` to confirm `DiskPressure` status and see which pods were evicted. |
| 2. **Clean Up Unused Images and Containers** | SSH into the node or use a DaemonSet to run `docker system prune -a` or containerd equivalents to free up disk space. |
| 3. **Adjust Eviction Thresholds and Alerts** | Configure `kubelet` with `--eviction-hard` and `--eviction-soft` flags to fine-tune disk pressure response, and set up alerts in Prometheus. |
| 4. **Resize or Add Disk Storage** | Attach larger disks or move to storage-optimized instances to prevent repeated pressure events on high-usage nodes. |
| 5. **Implement Quotas and Cleanup Automation** | Set `EmptyDir` size limits, use `ttlSecondsAfterFinished` on jobs, and schedule regular cleanup jobs for logs, cache, or temp data. |


Your logs show high CPU usage but metrics don’t reflect it. How do you correlate and analyze this discrepancy?

| Step | Description |
|------|-------------|
| 1. **Verify Metric Collection Intervals and Sources** | Ensure Prometheus or your monitoring system is scraping the correct targets and at a high enough resolution to capture spikes. |
| 2. **Check for Throttling or Aggregation Loss** | Container runtimes may throttle CPU but not report it properly; check `container_cpu_cfs_throttled_seconds_total` for evidence. |
| 3. **Correlate Timestamps in Logs vs Metrics** | Align timestamps between log entries and metric samples to confirm whether spikes are being missed due to timing gaps. |
| 4. **Use Node-Level and Kernel Metrics** | Compare application metrics with node-level metrics (`node_exporter`, `top`, `htop`) to see if host-level CPU use is accurately tracked. |
| 5. **Enable Enhanced Logging or Profiling** | Use eBPF tools (e.g., `bcc`, `perf`, `pyroscope`) or language-specific profilers to capture short-lived CPU spikes not visible in metrics. |


A Helm upgrade failed halfway. How do you recover and ensure consistency in the cluster?

| Step | Description |
|------|-------------|
| 1. **Check Helm Release History** | Run `helm history <release-name>` to identify the failed revision and assess what changes were attempted during the upgrade. |
| 2. **Rollback to Last Known Good Revision** | Use `helm rollback <release-name> <previous-revision>` to restore the last successful state of the application. |
| 3. **Inspect Logs and Resources for Inconsistencies** | Review pod logs, events (`kubectl describe`) and resource states to ensure partial changes didn’t leave the app in a broken state. |
| 4. **Manually Clean Up Orphaned or Failed Resources** | Identify and delete partially applied resources (e.g., PVCs, Services) using `kubectl get all` to avoid future deployment issues. |
| 5. **Use `--atomic` and `--cleanup-on-fail` in Future Upgrades** | Ensure future upgrades are safer by using `helm upgrade --atomic --cleanup-on-fail` to auto-rollback if errors occur. |


You’ve been asked to create a multi-region active-active Kubernetes setup. What design principles and tools would you use?

How would you use Karpenter (or Cluster Autoscaler) to optimize workload placement dynamically?

Your CI/CD pipeline is deploying to the wrong namespace intermittently. How do you debug and prevent this?

A developer reports their pod is in CrashLoopBackOff. Walk them through the resolution process.

How do you implement pod disruption budgets to ensure availability during node maintenance?

You notice API server response times are increasing. How would you diagnose and tune it?

You've been tasked with hardening a Kubernetes cluster for financial data workloads. What's your plan?

There’s an unexpected increase in failed jobs. What monitoring and recovery mechanisms would you introduce?

How would you ensure cost optimization in a large-scale Kubernetes environment?

What tools and practices would you use to benchmark application performance within the cluster?
