

31. Your kubelet is not registering new pods on a node. How do you identify and solve the root cause?


32. The horizontal pod autoscaler is not scaling pods under load. What are the steps to debug this behavior?

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


35. You need to migrate a stateful application between availability zones. How would you plan this migration?


36. A metrics pipeline starts dropping data points during peak hours. What architecture changes would you consider?


37. A critical alert was missed during an incident. How do you build alerting redundancy and accountability?


38. You notice your Fluentd/Fluentbit logs aren’t reaching your backend. How do you debug the log pipeline?


39. Your custom controller is consuming high CPU. What steps would you take to optimize its performance?


40. Application team reports that config changes are not taking effect. How do you validate ConfigMap rollout?


41. One namespace shows degraded performance. How do you isolate the problem and prevent blast radius?


42. You need to enforce cluster-wide policy compliance. What tooling and workflows would you integrate?


43. The audit logs of your cluster are filling up the disk. How do you tune and manage auditing effectively?


44. You are tasked with designing blue-green deployment for a Kubernetes-based app. What are key steps?


45. There's a memory leak in a container but no metrics to prove it. How do you approach deep container memory debugging?


46. You suspect a bad actor is scanning your services from inside the cluster. How do you detect and mitigate?


47. A misconfigured webhook is blocking all new pod creations. How do you recover quickly without disrupting workloads?


48. You need to simulate node failures to test app HA. How would you automate and verify this?


49. You’re planning a global failover architecture using Kubernetes. What DNS and routing strategies do you consider?


50. During a red team exercise, your SRE team needs to detect infrastructure drift. What tools help?


51. You want to track the cost of workloads per team in a shared cluster. How do you implement and manage this?
