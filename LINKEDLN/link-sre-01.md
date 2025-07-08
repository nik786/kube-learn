

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
| 1. **Use Rolling Updates with Readiness Probes** | Ensure new pods are only added to the service after passing readiness checks, reducing downtime during deployment. |
| 2. **Enable Deployment Strategies like Canary or Blue-Green** | Gradually shift traffic to new versions (Canary) or swap environments (Blue-Green) to validate stability before full rollout. |
| 3. **Automate Rollbacks on Failure** | Use health checks and monitoring to automatically detect failed deployments and trigger rollbacks using `kubectl rollout undo`. |
| 4. **Implement GitOps or CI/CD with Approval Gates** | Use tools like ArgoCD or Flux to manage deployments via Git with mandatory manual approvals for production. |
| 5. **Monitor and Alert on Deployment Metrics** | Track pod restarts, error rates, and latency post-deployment using Prometheus/Grafana to detect issues early. |


5. Latency between microservices has increased in your Kubernetes environment. What are your investigation steps, and what tools would you use?

   | Step | Description |
|------|-------------|
| 1. **Check Service Metrics and Latency Histograms** | Use Prometheus metrics (e.g., `histogram_quantile`) to identify which services are experiencing increased latency. |
| 2. **Inspect Network Policies and DNS Resolution** | Ensure network policies aren’t restricting traffic and CoreDNS is functioning properly (`kubectl logs -n kube-system`). |
| 3. **Use Distributed Tracing** | Implement tools like Jaeger or OpenTelemetry to trace requests end-to-end and pinpoint slow service calls. |
| 4. **Analyze Pod and Node Resource Usage** | Use `kubectl top` or Grafana dashboards to detect CPU/memory pressure that may delay service responses. |
| 5. **Monitor Network Latency and Packet Loss** | Use Cilium, Istio, or Calico with flow visibility to trace network hops and diagnose network-level issues. |


8. How would you set up and test multi-region disaster recovery for a stateful Kubernetes workload?

9. You’ve been alerted that a node is flapping between Ready and NotReady. How would you go about resolving this and preventing recurrence?

10. During a cluster upgrade, a custom resource fails to reconcile. How do you identify which operator or controller is responsible and how do you fix it?

11. You notice a spike in Evicted pods in one node pool. What are the most common causes and how do you proactively monitor this condition?

12. A client complains of intermittent DNS resolution failures. How do you debug and tune CoreDNS within Kubernetes?

13. Your Prometheus instance has stopped scraping metrics intermittently. How do you ensure HA and scrape reliability?

14. You find inconsistencies in metrics between Prometheus and the application’s own metrics endpoint. How do you resolve this discrepancy?

15. A pod is in ImagePullBackOff. What advanced diagnostics can you apply beyond logs and describe?

16. You are tasked with auditing a Kubernetes cluster for best practices and SRE compliance. What key areas would you focus on?

17. During high traffic, pods are scaling up but traffic is still being dropped. How would you approach diagnosing and resolving this?

18. You are getting alerts for container CPU throttling. What steps do you take to analyze and fix this?

19. A network policy accidentally blocked service communication. What monitoring would you put in place to detect such issues faster?

20. A newly deployed Ingress route is failing to resolve for some users. How do you debug this and ensure DNS propagation is healthy?

21. Persistent volume claims are stuck in pending state. What are the advanced steps you take to investigate the provisioner behavior?

22. You are facing high API server latency. How would you measure and scale the control plane under load?
