

### 🧩 EKS Latency Issue: Debug & Optimization Steps

| Step | Area of Focus                   | Actions/Commands                                                                                 | Optimization Tips                                                                 |
|------|----------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 1    | **Identify Symptom**             | - Use `kubectl top pods/nodes` <br> - Review latency in app logs/APM                             | Determine if latency is at app, network, or infra level                           |
| 2    | **Node Resource Bottlenecks**    | - Check CPU/Memory via `kubectl top nodes` <br> - Look for throttling in CloudWatch              | Use larger instance types or optimize pod requests/limits                        |
| 3    | **Pod Resource Limits**          | - Inspect resource requests/limits using `kubectl describe pod`                                  | Set appropriate CPU/memory requests/limits to avoid over-commitment              |
| 4    | **HPA & Autoscaling**            | - Check HPA status with `kubectl get hpa`                                                        | Tune HPA thresholds or enable Cluster Autoscaler                                 |
| 5    | **Network Latency**              | - Test pod-to-pod latency using tools like `iperf` or `ping` <br> - Use VPC Flow Logs            | Place latency-sensitive services in same AZ or subnet                            |
| 6    | **DNS Resolution Delays**        | - Monitor CoreDNS with `kubectl -n kube-system logs -l k8s-app=kube-dns`                         | Increase CoreDNS replicas, enable caching, or switch to node-local DNS           |
| 7    | **Storage Bottlenecks**          | - Check EBS or EFS IOPS usage via CloudWatch <br> - Monitor PVC stats                            | Use GP3 volumes with provisioned IOPS or local SSD volumes                       |
| 8    | **Control Plane Issues**         | - Review CloudWatch metrics and API server logs                                                  | Minimize excessive API requests from misbehaving controllers                     |
| 9    | **App-Level Profiling**          | - Use APM tools like X-Ray, Datadog, Prometheus, Jaeger                                         | Optimize code paths, DB queries, or cache heavy operations                       |
| 10   | **Upgrade Components**           | - Ensure latest EKS/K8s version <br> - Upgrade CoreDNS, kube-proxy                              | Performance improvements in newer releases                                       |

