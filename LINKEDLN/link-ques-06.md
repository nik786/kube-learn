
Best Practices & Operations

What are liveness and readiness probes? How do they impact pod behavior?

How do you perform rolling updates and rollbacks in Kubernetes?

| Step | Description | Command |
|------|-------------|---------|
| 1. **Perform Rolling Update by Modifying Deployment** | Update the image, environment, or config in the Deployment to trigger a rolling update. | `kubectl set image deployment/<name> <container>=<new-image>` |
| 2. **Monitor the Rolling Update Progress** | Watch rollout status to ensure the update proceeds without issues. | `kubectl rollout status deployment/<name>` |
| 3. **Pause and Resume Rollouts (if needed)** | Pause a rollout to inspect or apply other changes before resuming. | `kubectl rollout pause deployment/<name>` / `kubectl rollout resume deployment/<name>` |
| 4. **View Rollout History** | List previous revisions of the deployment to prepare for a potential rollback. | `kubectl rollout history deployment/<name>` |
| 5. **Rollback to a Previous Revision** | Revert the deployment to the last working version in case of issues. | `kubectl rollout undo deployment/<name>` |


What’s the use of a PodDisruptionBudget?

How can you achieve blue/green deployments in Kubernetes?

What metrics do you monitor for ensuring Kubernetes cluster health?

| Metric Category | Description |
|-----------------|-------------|
| 1. **Node Health Metrics** | Monitor `node_ready` status, CPU/memory usage, disk pressure, and network availability to detect unhealthy or overloaded nodes. |
| 2. **Pod and Container Metrics** | Track `container_cpu_usage_seconds_total`, `container_memory_usage_bytes`, restart counts, and OOMKilled events to ensure workload stability. |
| 3. **Control Plane Metrics** | Monitor API server latency (`apiserver_request_duration_seconds`), etcd health (`etcd_server_has_leader`), and scheduler performance. |
| 4. **Cluster Autoscaler and Scheduling Metrics** | Check pending pods, unschedulable pod count, and HPA/VPA activity to identify scaling or scheduling bottlenecks. |
| 5. **Network and DNS Metrics** | Observe service response time, dropped packets, and CoreDNS metrics like `coredns_dns_request_count_total` to ensure reliable service discovery. |


CI/CD & Observability

How do you integrate Kubernetes with a CI/CD pipeline?

What are your preferred logging solutions for Kubernetes?

How would you monitor a Kubernetes cluster?

Explain how you would debug a sudden increase in latency across services in Kubernetes.

What is the difference between a Job and a CronJob in Kubernetes?

What is Helm and how does it help in Kubernetes application management?

How do you manage secrets in Helm charts?

How do you roll back a Helm release?

What are Helm hooks and how are they used?

How do you handle multi-environment Helm chart deployments?
