

1. You are observing an increase in 500 errors from a Kubernetes-hosted API. Describe how you would identify the root cause and remediate it.

| Step | Description |
|------|-------------|
| 1. **Check Pod Logs** | Use `kubectl logs <pod-name>` to inspect recent logs for stack traces or error messages that indicate application-level issues. |
| 2. **Inspect Kubernetes Events** | Run `kubectl describe pod <pod-name>` and check `kubectl get events` to identify OOMKills, restarts, or readiness probe failures. |
| 3. **Monitor Resource Usage** | Use tools like `kubectl top pod` or Prometheus/Grafana to check CPU, memory, and disk usage. High usage may lead to instability. |
| 4. **Review Application & Config Maps** | Validate configuration files, secrets, and environment variables for incorrect values or recent changes. |
| 5. **Check Upstream/Dependency Health** | Investigate APIs, databases, or services the app depends on. Failures in dependencies often lead to 500 errors. |


2. A critical job runs daily at midnight but failed silently last night. How do you implement observability for jobs in Kubernetes to prevent this in future?

| Step | Description |
|------|-------------|
| 1. **Use `spec.backoffLimit` and `restartPolicy`** | Configure `backoffLimit` and `restartPolicy` in the Job spec to control retries and ensure failures don’t go unnoticed. |
| 2. **Enable Alerting on Job Status** | Set up Prometheus alerts or K8s event-based triggers to notify on job failures, completions, or missed runs. |
| 3. **Log Aggregation and Monitoring** | Stream job logs to centralized logging systems like EFK, Loki, or CloudWatch for long-term analysis and alerting. |
| 4. **Use CronJob `successfulJobsHistoryLimit` and `failedJobsHistoryLimit`** | Retain job history to inspect past executions and detect patterns of failure. |
| 5. **Implement Completion & Failure Metrics** | Expose custom metrics (e.g., via a sidecar or exporter) to track job success/failure counts, durations, and emit alerts accordingly. |


3. Your application’s pods are being OOMKilled frequently. How do you handle memory allocation and limits, and how do you monitor these at scale?

| Step | Description |
|------|-------------|
| 1. **Set Resource Requests and Limits** | Define `resources.requests.memory` and `resources.limits.memory` in pod specs to control memory allocation and prevent overcommitment. |
| 2. **Analyze Historical Usage** | Use metrics from Prometheus or `kubectl top pod` to assess typical memory usage and adjust limits accordingly. |
| 3. **Enable OOM Alerts** | Set up Prometheus alerts or Cloud provider monitoring to notify on OOMKilled events or high memory usage. |
| 4. **Use Vertical Pod Autoscaler (VPA)** | Deploy VPA to automatically recommend or apply appropriate memory settings based on observed usage trends. |
| 5. **Centralized Dashboards** | Use Grafana or similar tools to visualize memory usage, OOMKills, and trends across namespaces or workloads. |


4. A deployment was mistakenly rolled out to production causing outages. How do you implement safe deployment strategies in Kubernetes to prevent this?

| Step | Description |
|------|-------------|
| 1. **Use Rolling Updates with Readiness Probes** | Configure rolling updates and readiness probes to ensure only healthy pods receive traffic during deployment, minimizing downtime. |
| 2. **Adopt Canary or Blue-Green Deployment Strategies** | Deploy changes gradually (Canary) or switch between production environments (Blue-Green) to validate stability before full rollout. |
| 3. **Automate Rollbacks on Failures** | Use Kubernetes' built-in rollout history and health checks to detect failures and automatically rollback using `kubectl rollout undo`. |
| 4. **Integrate GitOps or CI/CD with Approval Gates** | Use tools like ArgoCD or Flux for Git-driven deployments with manual approvals and policy enforcement for production releases. |
| 5. **Monitor and Alert on Deployment Health** | Set up Prometheus/Grafana to monitor pod restarts, error rates, and latency spikes to detect and respond to issues quickly. |



5. Latency between microservices has increased in your Kubernetes environment. What are your investigation steps, and what tools would you use?

| Step | Description |
|------|-------------|
| 1. **Check Service Metrics and Latency Histograms** | Use Prometheus metrics (e.g., `histogram_quantile`) to identify which services are experiencing increased latency. |
| 2. **Inspect Network Policies and DNS Resolution** | Ensure network policies aren’t restricting traffic and CoreDNS is functioning properly (`kubectl logs -n kube-system`). |
| 3. **Use Distributed Tracing** | Implement tools like Jaeger or OpenTelemetry to trace requests end-to-end and pinpoint slow service calls. |
| 4. **Analyze Pod and Node Resource Usage** | Use `kubectl top` or Grafana dashboards to detect CPU/memory pressure that may delay service responses. |
| 5. **Monitor Network Latency and Packet Loss** | Use Cilium, Istio, or Calico with flow visibility to trace network hops and diagnose network-level issues. |


8. How would you set up and test multi-region disaster recovery for a stateful Kubernetes workload?

| Step | Description |
|------|-------------|
| 1. **Deploy to Multiple Regions with Active-Passive or Active-Active Setup** | Use separate clusters per region with data replication across them. Choose architecture (active-passive or active-active) based on workload tolerance. |
| 2. **Replicate Persistent Data Across Regions** | Use tools like Velero, Portworx, or storage backend replication (e.g., S3, EBS multi-region replication) to sync PVC data. |
| 3. **Use Global Load Balancer or DNS Failover** | Set up a global load balancer (e.g., AWS Route 53, GCP Cloud DNS) with health checks to reroute traffic on failure. |
| 4. **Automate Failover and Bootstrap** | Use IaC tools (Terraform, ArgoCD) to rehydrate workloads and configurations quickly in the failover region. |
| 5. **Regular DR Drills and Validation** | Simulate outages and test failover by disabling the primary region, ensuring data consistency and application availability in secondary region. |


10. You’ve been alerted that a node is flapping between Ready and NotReady. How would you go about resolving this and preventing recurrence?

| Step | Description |
|------|-------------|
| 1. **Check Node and Kubelet Logs** | Use `journalctl -u kubelet` or check `/var/log` on the node to identify root causes like crashes, timeouts, or resource pressure. |
| 2. **Verify Node Resource Usage** | Use `kubectl top node` or monitoring tools to check for CPU, memory, or disk exhaustion that could cause instability. |
| 3. **Inspect Network and DNS Connectivity** | Ensure the node has stable network access to the API server and DNS resolution is functioning properly. |
| 4. **Run Node Draining and Cordon if Needed** | Use `kubectl cordon <node>` and `kubectl drain <node>` to isolate the node for investigation without impacting workloads. |
| 5. **Implement Node Health Monitoring and Auto-Replacement** | Use node auto-repair (e.g., in GKE) or monitoring tools like Prometheus to detect flapping early and replace unstable nodes automatically. |


11. During a cluster upgrade, a custom resource fails to reconcile. How do you identify which operator or controller is responsible and how do you fix it?

| Step | Description |
|------|-------------|
| 1. **Inspect the Custom Resource (CR) Status** | Use `kubectl describe <cr>` and `kubectl get <cr> -o yaml` to check for status conditions, error messages, or event logs. |
| 2. **Identify the Responsible Controller** | Use `kubectl get crd <crd-name> -o yaml` to find the `controller` or operator managing the CR via annotations or owner references. |
| 3. **Check Logs of the Operator Pod** | Locate the operator's deployment (`kubectl get pods -n <namespace>`) and view logs with `kubectl logs` to find reconciliation errors. |
| 4. **Verify Compatibility with New K8s Version** | Check the operator’s documentation or GitHub issues for version compatibility; upgrade the operator if needed. |
| 5. **Test Reconciliation Post-Fix** | Reapply or patch the CR and watch the operator logs or resource status to confirm successful reconciliation. |


13. You notice a spike in Evicted pods in one node pool. What are the most common causes and how do you proactively monitor this condition?

14. A client complains of intermittent DNS resolution failures. How do you debug and tune CoreDNS within Kubernetes?

15. Your Prometheus instance has stopped scraping metrics intermittently. How do you ensure HA and scrape reliability?

16. You find inconsistencies in metrics between Prometheus and the application’s own metrics endpoint. How do you resolve this discrepancy?

17. A pod is in ImagePullBackOff. What advanced diagnostics can you apply beyond logs and describe?

18. You are tasked with auditing a Kubernetes cluster for best practices and SRE compliance. What key areas would you focus on?

19. During high traffic, pods are scaling up but traffic is still being dropped. How would you approach diagnosing and resolving this?

| Step | Description |
|------|-------------|
| 1. **Check Load Balancer and Ingress Limits** | Verify if the cloud load balancer or ingress controller has hit connection or throughput limits, causing traffic drops. |
| 2. **Inspect Readiness and Liveness Probes** | Ensure new pods are marked Ready before receiving traffic; misconfigured probes may route traffic to unhealthy pods. |
| 3. **Analyze HPA and Scaling Latency** | Use Prometheus to assess Horizontal Pod Autoscaler behavior—pods may scale up too slowly to handle sudden traffic spikes. |
| 4. **Review Network and Node Capacity** | Check for pod-to-pod network bottlenecks, node CPU saturation, or insufficient ENIs/IPs that might throttle traffic routing. |
| 5. **Use Connection Queue Monitoring and Tuning** | Monitor application-level connection queues and tune web server settings (e.g., NGINX worker connections) to absorb bursts. |


21. You are getting alerts for container CPU throttling. What steps do you take to analyze and fix this?

| Step | Description |
|------|-------------|
| 1. **Inspect CPU Limits in Pod Specs** | Check if `resources.limits.cpu` is too low; throttling occurs when container usage exceeds this limit. |
| 2. **Review Throttling Metrics** | Use Prometheus metrics like `container_cpu_cfs_throttled_seconds_total` to identify which containers are being throttled. |
| 3. **Compare Requests vs. Limits** | Ensure `resources.requests.cpu` and `limits.cpu` are appropriately set; avoid setting equal values for bursty workloads. |
| 4. **Tune Application Threads or Concurrency** | Optimize app-level concurrency (e.g., thread pools, workers) to match available CPU without exceeding limits. |
| 5. **Adjust CPU Limits or Use Guaranteed QoS** | Increase CPU limits or remove limits entirely (with equal request/limit) to give critical pods higher scheduling priority. |


23. A network policy accidentally blocked service communication. What monitoring would you put in place to detect such issues faster?

| Step | Description |
|------|-------------|
| 1. **Enable Network Flow Logging** | Use CNI plugins like Calico or Cilium with flow logging to monitor and audit traffic flows and policy drops in real time. |
| 2. **Set Up Prometheus Alerts on Connection Errors** | Track metrics like `http_request_errors`, `tcp_connection_failures`, or pod-level error rates to catch communication failures. |
| 3. **Implement Distributed Tracing** | Use tools like Jaeger or OpenTelemetry to trace service calls and identify broken or blocked communication paths. |
| 4. **Monitor NetworkPolicy Events** | Watch for `kubectl get events` and audit logs for applied or updated `NetworkPolicy` resources that could affect connectivity. |
| 5. **Create Synthetic Health Checks Between Services** | Deploy lightweight probes or blackbox exporters to simulate and alert on cross-service communication failures. |


22. A newly deployed Ingress route is failing to resolve for some users. How do you debug this and ensure DNS propagation is healthy?

| Step | Description |
|------|-------------|
| 1. **Check Ingress Resource and Controller Logs** | Verify the `Ingress` YAML is correctly defined and inspect the ingress controller logs (e.g., NGINX, Traefik) for errors. |
| 2. **Validate DNS Records** | Use `dig`, `nslookup`, or online tools to confirm the domain resolves to the correct ingress/load balancer IP. |
| 3. **Confirm External DNS Sync** | If using ExternalDNS, check logs to ensure DNS records were created/updated successfully in the provider (e.g., Route 53, Cloud DNS). |
| 4. **Test from Multiple Locations** | Use tools like `dig +trace` or `dnschecker.org` to test DNS resolution globally and identify propagation delays. |
| 5. **Check TTL and Caching Behavior** | Ensure low TTL values during updates and clear local DNS cache (`systemd-resolve --flush-caches`, browser flush, etc.) if necessary. |


24. Persistent volume claims are stuck in pending state. What are the advanced steps you take to investigate the provisioner behavior?

25. You are facing high API server latency. How would you measure and scale the control plane under load?



| Step | Description |
|------|-------------|
| 1. **Measure API Server Latency with Metrics** | Use Prometheus metrics like `apiserver_request_duration_seconds` to monitor slow requests by verb (GET, LIST, WATCH). |
| 2. **Check etcd Health and Latency** | Use `etcdctl endpoint health` and monitor `etcd_request_duration_seconds` to ensure etcd is not a performance bottleneck. |
| 3. **Audit API Server Logs** | Inspect logs for throttling, timeouts, or high cardinality operations (e.g., heavy LIST/WATCH calls from controllers). |
| 4. **Horizontally Scale API Servers (if supported)** | In managed services (like EKS, GKE), request increased API server capacity or upgrade the control plane tier. |
| 5. **Reduce Load with Caching or Client Backoff** | Implement client-side caching, increase request backoff, and review controllers/operators making excessive API calls. |
