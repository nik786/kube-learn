

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





