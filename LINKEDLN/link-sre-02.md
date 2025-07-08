

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


39. You notice your Fluentd/Fluentbit logs aren’t reaching your backend. How do you debug the log pipeline?


40. Your custom controller is consuming high CPU. What steps would you take to optimize its performance?


41. Application team reports that config changes are not taking effect. How do you validate ConfigMap rollout?


42. One namespace shows degraded performance. How do you isolate the problem and prevent blast radius?


43. You need to enforce cluster-wide policy compliance. What tooling and workflows would you integrate?


44. The audit logs of your cluster are filling up the disk. How do you tune and manage auditing effectively?


45. You are tasked with designing blue-green deployment for a Kubernetes-based app. What are key steps?


46. There's a memory leak in a container but no metrics to prove it. How do you approach deep container memory debugging?


47. You suspect a bad actor is scanning your services from inside the cluster. How do you detect and mitigate?


48. A misconfigured webhook is blocking all new pod creations. How do you recover quickly without disrupting workloads?


49. You need to simulate node failures to test app HA. How would you automate and verify this?


50. You’re planning a global failover architecture using Kubernetes. What DNS and routing strategies do you consider?


51. During a red team exercise, your SRE team needs to detect infrastructure drift. What tools help?


52. You want to track the cost of workloads per team in a shared cluster. How do you implement and manage this?
