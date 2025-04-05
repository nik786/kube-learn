

Imagine you’re managing a production Kubernetes cluster and one of your critical services suddenly becomes 
unresponsive. What steps would you take to diagnose and resolve the issue?

# 🛠️ Kubernetes: Troubleshooting Unresponsive Production Service

| Step                          | Action                                                                 | Purpose                                                                                  | Example / Command                                                        |
|-------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **1. Check Pod Status**       | Inspect the current state of the pods                                 | Identify if pods are `CrashLoopBackOff`, `Pending`, or `Terminating`                    | `kubectl get pods -n <namespace>`                                       |
| **2. Describe the Pod**       | Get detailed info on the pod                                           | Reveal events, error messages, container restarts                                        | `kubectl describe pod <pod-name> -n <namespace>`                        |
| **3. Check Pod Logs**         | View container logs                                                    | Discover runtime issues like exceptions, failed connections, etc.                        | `kubectl logs <pod-name> -n <namespace>`                                |
| **4. Check Deployment/ReplicaSet** | Ensure deployment state is as expected                               | Verify if pods are being recreated or stuck                                              | `kubectl get deployment <deployment-name> -n <namespace>`               |
| **5. Inspect Node Health**    | Review node resource usage (CPU, memory, disk)                        | Identify if node pressure is impacting pod scheduling                                    | `kubectl describe node <node-name>` or `kubectl top nodes`              |
| **6. Validate Network/Ingress**| Test service DNS, ingress rules, and port mappings                    | Ensure traffic can correctly reach the pod                                               | `kubectl exec -it <pod> -- curl <service-name>:<port>`                  |
| **7. Check ConfigMaps/Secrets**| Review for misconfigured environment variables or credentials         | Misconfigurations can cause app crashes                                                  | `kubectl get configmap|secret -n <namespace>`                           |
| **8. Review HPA/Scaling Events**| Look for auto-scaling or throttling issues                           | Too few replicas may not serve the load                                                  | `kubectl get hpa -n <namespace>`                                        |
| **9. Audit Recent Changes**   | Check for recent deployments, config changes, or PR merges            | Identify regressions due to new code/config                                              | Use GitOps, `kubectl rollout history`, or CI/CD pipeline logs           |
| **10. Restart / Rollback**    | Redeploy or rollback to a previous stable version                     | Restore service availability while continuing diagnosis                                  | `kubectl rollout undo deployment <deployment-name> -n <namespace>`      |





In a dynamic microservices architecture, how do you manage service discovery 
to ensure smooth communication between services?


# 🔍 Managing Service Discovery in Microservices Architecture

| Strategy / Tool                | Description                                                                 | Benefits                                                               | Example / Tooling                    |
|-------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------|
| **Kubernetes DNS-Based Discovery** | Kubernetes assigns a DNS name to each service                              | Automatic service registration and discovery via DNS                   | `my-service.my-namespace.svc.cluster.local` |
| **Service Mesh (e.g., Istio, Linkerd)** | Sidecars manage traffic routing and service discovery                      | Fine-grained control, resilience (e.g., retries, timeouts), observability | Istio’s Envoy sidecar auto-discovers services |
| **Client-Side Discovery**     | Clients query a registry for instance location and route themselves         | Greater control on client logic, resilience with custom policies       | Netflix Eureka + Ribbon (Spring Cloud) |
| **Server-Side Discovery**     | A load balancer queries the registry and forwards traffic                   | Simplifies clients, centralized logic                                  | AWS ALB with ECS Service Discovery   |
| **External Service Registry** | Use a dedicated service registry like Consul or etcd                       | Works outside of Kubernetes, supports multi-platform                   | HashiCorp Consul, Apache ZooKeeper   |
| **Environment Variable Injection** | Inject host/IP/port information at runtime or via config                  | Simplified setup for small systems                                     | Docker Compose or Spring Boot config |


If you notice unusual traffic patterns that could indicate a security breach, what steps would 
you take to investigate and mitigate the threat?



# 🛡️ Investigating and Mitigating Security Breaches from Unusual Traffic Patterns

| Step                             | Action                                                                 | Purpose                                                               | Example / Tooling                         |
|----------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------|
| **1. Detect and Acknowledge**    | Identify anomalies in traffic (spikes, foreign IPs, unexpected ports) | Confirm whether the traffic is malicious or a false positive          | Use IDS/IPS (e.g., Suricata, AWS GuardDuty) |
| **2. Inspect Logs and Metrics**  | Analyze logs from ingress controllers, firewalls, app logs, and API gateways | Pinpoint source and nature of traffic                                | ELK, Grafana, Prometheus, AWS CloudWatch   |
| **3. Trace Network Flows**       | Track traffic flow and communication between services                  | Identify lateral movement and affected services                       | `kubectl logs`, `kubectl describe`, Flow logs |
| **4. Isolate Affected Resources**| Temporarily restrict access to compromised services or pods           | Prevent further damage or data exfiltration                           | Use NetworkPolicies, security groups       |
| **5. Verify Authentication Logs**| Check user login activity and access tokens                            | Detect unauthorized access attempts or stolen credentials             | IAM logs, AWS CloudTrail, Auth0 logs       |
| **6. Apply Patches / Fix Configs**| Update vulnerable software or misconfigured services                   | Close security loopholes                                              | Patch libraries, rotate secrets            |
| **7. Enable Throttling / Rate Limits**| Limit excessive traffic from suspicious sources                       | Reduce the impact of brute-force or DDoS-like attacks                 | NGINX Ingress rate limiting, API Gateway quota |
| **8. Notify Stakeholders & Report**| Inform security teams and affected users                              | Ensure accountability and transparency                                | Incident reports, email/Slack alerts       |
| **9. Conduct Forensics Review**  | Review impacted systems, gather evidence for root cause                | Understand breach mechanism and ensure no persistence remains         | Audit tools, forensic snapshots            |
| **10. Improve Detection Rules**  | Tune alert thresholds and rules based on findings                      | Prevent future false negatives and positives                          | Update SIEM rules, IDS signatures          |



