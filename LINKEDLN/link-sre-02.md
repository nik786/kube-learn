

31. Your kubelet is not registering new pods on a node. How do you identify and solve the root cause?

| Step                          | Action / Command                          | Description / Purpose                                    |
|-------------------------------|-----------------------------------------|---------------------------------------------------------|
| 1. Check kubelet status        | `systemctl status kubelet`               | Verify if kubelet service is running                     |
| 2. Inspect kubelet logs        | `journalctl -u kubelet -f`               | Look for errors or warnings preventing pod registration  |
| 3. Verify node status          | `kubectl get nodes`                      | Check if node is Ready or NotReady                        |
| 4. Describe node for details   | `kubectl describe node <node-name>`     | Look for conditions/events affecting pod scheduling      |
| 5. Check disk and memory       | `df -h` and `free -m`                    | Ensure sufficient resources; low disk space or memory can block pods |
| 6. Verify network connectivity | Ping API server from node                 | Confirm node can communicate with control plane          |
| 7. Check container runtime     | `systemctl status containerd` or `docker` | Ensure container runtime is running properly              |
| 8. Inspect pod logs and events | `kubectl get pods -o wide --field-selector spec.nodeName=<node-name>` and `kubectl describe pod <pod>` | Identify pod-level issues                                |
| 9. Restart kubelet             | `systemctl restart kubelet`              | Fix transient issues by restarting kubelet               |
| 10. Review kubelet config      | Check `/var/lib/kubelet/config.yaml` or kubelet startup parameters | Look for misconfigurations                                |
| 11. Check for taints           | `kubectl get nodes -o jsonpath='{.items[*].spec.taints}'` | Ensure node is not tainted preventing pod scheduling      |
| 12. Confirm Node IP and Hostname | Validate node's hostname and IP are correct and resolvable | Misconfigured hostname/IP can cause registration failure |



33. The horizontal pod autoscaler is not scaling pods under load. What are the steps to debug this behavior?

    # Debugging Horizontal Pod Autoscaler (HPA) Not Scaling Under Load

| Step                            | Description / Command                                                   | Purpose / Outcome                                                  |
|---------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------|
| Check Metrics Server            | `kubectl get deployment metrics-server -n kube-system`                  | Ensure metrics-server is deployed and running                        |
| Validate Metrics Availability   | `kubectl top pods` / `kubectl top nodes`                                | Confirms resource metrics are available to HPA                       |
| Inspect HPA Object              | `kubectl describe hpa <deployment-name>`                                | View current metrics, thresholds, and conditions for scaling         |
| Review Target Metrics           | Ensure correct `targetCPUUtilizationPercentage` or custom metric is set | Misconfigured thresholds can prevent scaling                         |
| Verify Resource Requests/Limits| Check pod specs for `resources.requests.cpu/memory`                     | HPA won't scale if requests are missing or misconfigured             |
| Observe Load Behavior           | Generate load and monitor pod CPU via `kubectl top pods`                | Determine if CPU/memory usage actually exceeds the threshold         |
| Check HPA Conditions            | In HPA description, check `Conditions` section for warnings/errors      | May show issues like "FailedGetMetrics" or "InvalidMetricSourceType"|
| Review Events and Logs         | `kubectl get events`                                                    | Reveals cluster-level errors or warnings related to HPA              |
| Check Metrics Server Logs      | `kubectl logs -n kube-system deployment/metrics-server`                 | Identifies issues in collecting and serving metrics                  |
| Check kube-controller-manager Logs | `kubectl logs -n kube-system <kube-controller-manager-pod>`          | HPA controller logic runs here; reveals scaling decisions or failures|
| Examine Cluster Limits          | Ensure node/pod quota or limits aren’t blocking scaling                 | Cluster constraints can silently block HPA from adding pods          |
| API Server Permissions          | Confirm HPA has access to required APIs (for custom metrics or external metrics) | Permissions issues may prevent metric retrieval                      |



34. You encounter frequent DeadlineExceeded errors from services. How do you approach this in a Kubernetes setup?

| Step                         | Action / Command                              | Description / Purpose                                      |
|------------------------------|---------------------------------------------|-----------------------------------------------------------|
| 1. Identify affected pods     | `kubectl get pods --field-selector=status.phase!=Running` or check logs | Find pods/services throwing DeadlineExceeded errors       |
| 2. Check pod logs             | `kubectl logs <pod-name>`                     | Inspect logs for timeout or error details                  |
| 3. Review request timeouts    | Check application & service timeout settings | Increase timeout values if too low                         |
| 4. Analyze resource usage     | `kubectl top pod <pod-name>`                   | Ensure pods have enough CPU/memory to avoid slow responses|
| 5. Examine readiness/liveness probes | `kubectl describe pod <pod-name>`           | Verify probes are correctly configured, not causing restarts |
| 6. Inspect network latency    | Use `ping`/`traceroute` between services       | Check network delays between microservices                 |
| 7. Check horizontal pod autoscaling | `kubectl get hpa`                           | Ensure autoscaling is triggered appropriately              |
| 8. Increase replicas          | `kubectl scale deployment <name> --replicas=<n>` | Add more pods to handle load                               |
| 9. Optimize backend processing| Profile and improve code or database queries   | Reduce processing time to avoid deadlines                  |
| 10. Adjust Kubernetes timeouts| Tune `activeDeadlineSeconds` and ingress/load balancer timeouts | Align with expected processing times                        |
| 11. Monitor with metrics      | Use Prometheus/Grafana to track latency and errors | Identify bottlenecks and trends                             |



36. You need to migrate a stateful application between availability zones. How would you plan this migration?

| Step | Description |
|------|-------------|
| 1. **Use Zone-Aware StatefulSets and StorageClasses** | Configure StatefulSets with topology-aware scheduling and use `StorageClass` with `volumeBindingMode: WaitForFirstConsumer`. |
| 2. **Replicate Data to Target AZ** | Use storage backend features (e.g., EBS snapshot copy, Portworx, Velero) to replicate or back up PVC data to the destination AZ. |
| 3. **Drain and Cordon Source AZ Nodes** | Safely cordon and drain nodes in the source AZ to trigger pod rescheduling without data loss. |
| 4. **Ensure DNS and Service Continuity** | Maintain stable service endpoints (e.g., Headless Service, ClusterIP) to avoid disruption during pod rescheduling across AZs. |
| 5. **Validate Post-Migration State** | Verify data integrity, application health, and performance in the target AZ before cleaning up source resources. |




37. A metrics pipeline starts dropping data points during peak hours. What architecture changes would you consider?


38. A critical alert was missed during an incident. How do you build alerting redundancy and accountability?

| Step | Description |
|------|-------------|
| 1. **Integrate Multiple Notification Channels** | Configure alerts to route through multiple channels (e.g., Slack, email, SMS, PagerDuty) to ensure delivery redundancy. |
| 2. **Use Escalation Policies** | Implement escalation chains in tools like PagerDuty or Opsgenie to notify backup responders if primary contacts don’t acknowledge alerts. |
| 3. **Set Up Alert Acknowledgment and Tracking** | Require manual acknowledgment of alerts and track response times to enforce accountability. |
| 4. **Conduct Regular Alert Audits and Drills** | Review alerting rules and simulate incidents to ensure alerts are triggered, delivered, and acted upon as expected. |
| 5. **Maintain an On-Call Rotation with Handover Logs** | Use structured on-call schedules with clear documentation and handovers to avoid alert ownership gaps. |


39. You notice your Fluentd/Fluentbit logs aren’t reaching your backend. How do you debug the log pipeline?


40. Your custom controller is consuming high CPU. What steps would you take to optimize its performance?


41. Application team reports that config changes are not taking effect. How do you validate ConfigMap rollout?


42. One namespace shows degraded performance. How do you isolate the problem and prevent blast radius?

| Step | Description |
|------|-------------|
| 1. **Monitor Namespace-Specific Metrics** | Use Prometheus and Grafana to filter metrics (CPU, memory, latency, errors) by namespace to pinpoint resource bottlenecks or abnormal behavior. |
| 2. **Inspect Events and Resource Quotas** | Run `kubectl get events -n <namespace>` and check `ResourceQuota` or `LimitRange` settings to detect resource contention or throttling. |
| 3. **Use Network Policies for Isolation** | Apply Kubernetes `NetworkPolicy` to restrict traffic between namespaces and limit impact from misbehaving services. |
| 4. **Enable Pod Disruption Budgets and PodAntiAffinity** | Use `PodDisruptionBudget` and `PodAntiAffinity` to ensure HA and prevent noisy neighbors from overloading shared nodes. |
| 5. **Cordon and Drain Affected Nodes (if needed)** | If degradation is node-related, isolate impacted workloads by cordoning/draining the node and observe namespace recovery. |



43. You need to enforce cluster-wide policy compliance. What tooling and workflows would you integrate?

| Step | Description |
|------|-------------|
| 1. **Integrate OPA/Gatekeeper for Policy Enforcement** | Use Open Policy Agent (OPA) with Gatekeeper to define and enforce custom policies (e.g., image restrictions, label requirements). |
| 2. **Adopt Kyverno for Native Kubernetes Policy Management** | Use Kyverno to write policies in YAML, enforce best practices, and mutate resources automatically at admission time. |
| 3. **Define Policies as Code in Git Repos** | Manage policies through GitOps tools like ArgoCD or Flux to apply, version, and audit policy changes declaratively. |
| 4. **Enable Audit and Violation Reporting** | Use Gatekeeper’s audit functionality or Kyverno’s reports to detect and log non-compliant resources across the cluster. |
| 5. **Automate Compliance Checks in CI/CD** | Shift left by integrating policy validation tools (e.g., `conftest`, `kube-score`) in CI pipelines to catch violations before deployment. |


44. The audit logs of your cluster are filling up the disk. How do you tune and manage auditing effectively?


45. You are tasked with designing blue-green deployment for a Kubernetes-based app. What are key steps?

| Step | Description |
|------|-------------|
| 1. **Create Separate Blue and Green Environments** | Deploy two identical environments (e.g., two Deployments or namespaces) running different versions of the application. |
| 2. **Use a Load Balancer or Ingress Controller for Traffic Switching** | Point the Ingress, Service, or external load balancer to either the Blue or Green environment to control live traffic. |
| 3. **Deploy New Version to Green Environment** | Roll out the new version to the Green environment while Blue continues serving users without disruption. |
| 4. **Perform Validation and Smoke Tests on Green** | Run automated tests or manual checks against the Green environment before switching traffic. |
| 5. **Switch Traffic and Monitor Closely** | Redirect traffic from Blue to Green and monitor metrics (latency, errors, logs). Roll back to Blue if issues arise. |



47. There's a memory leak in a container but no metrics to prove it. How do you approach deep container memory debugging?

| Step | Description |
|------|-------------|
| 1. **Exec into the Container and Use Debugging Tools** | Use `kubectl exec` to access the container and run tools like `top`, `htop`, `free`, or `ps` to inspect memory usage at runtime. |
| 2. **Capture Heap Dumps or Use Language-Specific Profilers** | Use tools like `gperftools`, `go tool pprof`, `jmap`, or `valgrind` based on the application's language to analyze memory allocation. |
| 3. **Run the Container with Debug Flags Enabled** | Enable verbose logging or memory tracking flags (e.g., `--inspect`, `--trace-gc`) to surface allocation patterns and leaks. |
| 4. **Use eBPF Tools or `perf` in the Host Namespace** | Run tools like `bcc`, `bpftop`, or `perf` on the node to analyze memory behavior of containerized processes from the host side. |
| 5. **Reproduce the Leak in a Controlled Environment** | Isolate the container locally or in a dev namespace and run long-duration load tests to analyze memory growth over time. |



48. You suspect a bad actor is scanning your services from inside the cluster. How do you detect and mitigate?


49. A misconfigured webhook is blocking all new pod creations. How do you recover quickly without disrupting workloads?


50. You need to simulate node failures to test app HA. How would you automate and verify this?

| Step | Description |
|------|-------------|
| 1. **Use Chaos Engineering Tools (e.g., Chaos Mesh, Litmus)** | Automate node failure scenarios like shutdown, network loss, or CPU pressure using chaos testing frameworks. |
| 2. **Simulate Node Drain or Shutdown via Scripts** | Use `kubectl drain <node>` or cloud CLI/SDK to stop or reboot nodes programmatically and observe app behavior. |
| 3. **Label HA-Critical Workloads with PodDisruptionBudgets (PDBs)** | Ensure workloads tolerate node failures by defining PDBs that control how many replicas can be unavailable. |
| 4. **Monitor Pod Rescheduling and Availability** | Use Prometheus/Grafana or `kubectl get pods -w` to verify that pods are rescheduled on healthy nodes without downtime. |
| 5. **Log and Alert on HA Metrics** | Set up alerts on metrics like pod availability, restart count, and service uptime to validate HA during simulations. |



51. You’re planning a global failover architecture using Kubernetes. What DNS and routing strategies do you consider?

| Step | Description |
|------|-------------|
| 1. **Use GeoDNS with Health Checks** | Configure providers like AWS Route 53, Cloudflare, or NS1 to route users to the closest healthy region using latency- or geo-based routing. |
| 2. **Implement Active-Passive or Active-Active Failover** | Choose between routing all traffic to one region (active-passive) or load-balancing across multiple (active-active) for resilience and performance. |
| 3. **Leverage Global Load Balancers (e.g., GCLB, Azure Front Door)** | Use cloud-native global load balancers that support automatic health checking and traffic steering across regions. |
| 4. **Deploy External-DNS in Each Cluster** | Automate DNS record management by syncing Kubernetes Services with DNS providers using External-DNS across all regions. |
| 5. **Test and Automate DNS Failover Scenarios** | Regularly simulate region failures and validate automatic traffic failover using monitoring tools and scripted failover drills. |




52. During a red team exercise, your SRE team needs to detect infrastructure drift. What tools help?


| Step | Description |
|------|-------------|
| 1. **Use Terraform with `terraform plan` and Drift Detection** | Detect changes by comparing live infrastructure with declared state; tools like `infracost` and `terraform-driftctl` enhance visibility. |
| 2. **Deploy `driftctl` for Deep Resource Scanning** | Analyze infrastructure state against IaC definitions across providers (e.g., AWS, GCP) to catch unmanaged or altered resources. |
| 3. **Use `kube-bench` and `kube-hunter` for Cluster Security Drift** | Detect configuration deviations, privilege escalations, or network exposure in Kubernetes clusters. |
| 4. **Leverage CSPM Tools (e.g., AWS Config, GCP Security Command Center)** | Continuously monitor and alert on changes in cloud resources and security configurations. |
| 5. **Implement GitOps with ArgoCD or Flux** | Track drift in Kubernetes resources by comparing the live cluster state to Git and alerting on mismatches. |


52. You want to track the cost of workloads per team in a shared cluster. How do you implement and manage this?

| Step | Description |
|------|-------------|
| 1. **Use Namespace-Based Cost Isolation** | Assign each team its own namespace to group workloads and associate costs clearly. |
| 2. **Apply Team Labels on Resources** | Use consistent labels (e.g., `team=frontend`) on pods, services, and workloads to enable cost attribution and filtering. |
| 3. **Integrate with Cost Monitoring Tools** | Deploy tools like Kubecost, CloudHealth, or OpenCost to collect, visualize, and report cost metrics by namespace, label, or resource. |
| 4. **Set Resource Requests and Limits Accurately** | Enforce `requests` and `limits` on CPU and memory to ensure fair allocation and accurate cost calculations. |
| 5. **Generate Periodic Reports and Budgets** | Automate cost reports and budgets per team using Kubecost or Prometheus/Grafana, and share insights with stakeholders. |


