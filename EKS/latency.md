

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



You notice high latency when accessing a cloud-based application. 
What factors could be contributing, and how would you mitigate them


| **Factor** | **Possible Causes** | **Mitigation Strategies** |
|-----------|------------------|------------------------|
| **Network Latency** | Long geographical distance between users and servers. | Deploy CDN (CloudFront, Cloudflare) and use multi-region deployments. |
| **High API Response Time** | Backend services taking too long to process requests. | Optimize database queries, use caching (Redis, Memcached), and enable asynchronous processing. |
| **DNS Resolution Delay** | Slow DNS lookups or incorrect DNS configurations. | Use low TTL values and DNS providers with fast resolution (e.g., AWS Route 53, Google DNS). |
| **Database Bottlenecks** | Slow queries, unoptimized indexes, or high connection load. | Optimize indexes, use read replicas, and implement connection pooling. |
| **Resource Contention** | CPU, memory, or disk I/O saturation on application servers. | Autoscale instances, optimize instance sizing, and enable vertical/horizontal scaling. |
| **Poor Load Balancing** | Traffic not distributed efficiently across instances. | Use load balancers (AWS ALB/ELB, NGINX, HAProxy) and enable health checks. |
| **Excessive HTTP Requests** | Too many HTTP requests causing congestion. | Enable HTTP/2, reduce unnecessary API calls, and batch requests where possible. |
| **Inefficient Frontend Performance** | Large assets, unoptimized JavaScript, and high render time. | Minify JS/CSS, use lazy loading, and optimize images using WebP format. |
| **Container Orchestration Issues** | Slow pod scheduling, resource limits in Kubernetes. | Tune Kubernetes resource requests/limits, and enable Cluster Autoscaler. |
| **Serverless Cold Starts** | Delay in spinning up serverless functions (Lambda, Cloud Functions). | Use provisioned concurrency, keep functions warm with scheduled invocations. |
| **TLS/SSL Overhead** | Expensive encryption/decryption processes. | Use TLS session resumption and enable HTTP/2 to reduce handshake overhead. |
| **Cloud Provider Throttling** | Hitting API rate limits or cloud service quotas. | Upgrade service tiers, increase rate limits, and implement exponential backoff for retries. |
| **Packet Loss & Network Jitter** | Poor internet connectivity between users and cloud. | Implement TCP optimizations, use Anycast routing, and enable QoS settings. |
| **Application Code Inefficiencies** | Poorly written code causing delays. | Profile code performance using APM tools (New Relic, Datadog) and optimize bottlenecks. |



