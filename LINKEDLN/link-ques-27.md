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


You've been tasked with hardening a Kubernetes cluster for financial data workloads. What's your plan?

| Hardening Strategy                          | Description                                                                                           |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Enable Role-Based Access Control (RBAC)** | Apply least privilege principles by tightly controlling access using RBAC roles and service accounts. |
| **Use Network Policies**                    | Implement Kubernetes `NetworkPolicy` to restrict pod-to-pod and pod-to-service communications.        |
| **Encrypt Secrets at Rest and in Transit**  | Use envelope encryption with a KMS provider (e.g., AWS KMS) and enable TLS for all cluster traffic.   |
| **Audit and Monitor Everything**            | Enable audit logging, integrate with SIEM tools, and monitor security events using Falco or OPA Gatekeeper. |
| **Restrict Workload Capabilities**          | Use `PodSecurityPolicies` or `PodSecurityAdmission` to enforce rules like no root access or hostPath mounts. |


There’s an unexpected increase in failed jobs. What monitoring and recovery mechanisms would you introduce?

| Mechanism / Strategy                        | Description                                                                                           |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Enable Job Failure Alerts**               | Use Prometheus rules or Kubernetes event exporters to trigger alerts on high `JobFailed` metrics.     |
| **Centralized Logging for Job Pods**        | Aggregate logs using tools like EFK (Elasticsearch-Fluentd-Kibana) or Loki to analyze failure patterns.|
| **Implement Retry Policies**                | Configure `backoffLimit`, `restartPolicy`, and exponential backoff in Job specs for automatic retries.|
| **Job Execution Audits**                    | Track job runs with metadata (e.g., labels, annotations) and monitor execution duration and success rate over time. |
| **Auto-Healing with CronJobs or Controllers** | Use CronJobs or custom controllers to resubmit failed jobs and prevent long outages in batch processing. |


How would you ensure cost optimization in a large-scale Kubernetes environment?

| Cost Optimization Strategy                  | Description                                                                                           |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Use Karpenter or Cluster Autoscaler**     | Dynamically scale nodes based on demand, and right-size instances by leveraging spot capacity where possible. |
| **Implement Resource Requests & Limits**    | Enforce accurate CPU/memory requests and limits to avoid overprovisioning and wasted capacity.        |
| **Monitor with Cost Visibility Tools**      | Use tools like **Kubecost**, **OpenCost**, or **Cloud provider cost dashboards** to track cost per namespace, team, or workload. |
| **Leverage Horizontal Pod Autoscaling (HPA)** | Automatically scale workloads up/down based on usage metrics to match real-time demand.              |
| **Schedule Non-Prod Workloads Efficiently** | Use taints/tolerations or separate node pools to schedule dev/test workloads on cheaper instances or off-peak hours. |
