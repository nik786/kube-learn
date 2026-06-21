You've detected increased latency in inter-pod communication. What tools and steps would you use to troubleshoot?

| Step | Description |
|------|-------------|
| 1. **Use Distributed Tracing Tools** | Implement tools like Jaeger or OpenTelemetry to trace requests between services and pinpoint high-latency hops. |
| 2. **Check CNI Plugin Health and Logs** | Inspect logs and status of the Container Network Interface (e.g., Cilium, Calico, Weave) for errors, delays, or misconfigurations. |
| 3. **Run Network Performance Tests Between Pods** | Use tools like `iperf3`, `ping`, or `netperf` between pods in different nodes or namespaces to measure raw latency. |
| 4. **Analyze Network Policies and QoS** | Ensure `NetworkPolicy` rules are not introducing unnecessary routing or restrictions; check QoS classes for throttling. |
| 5. **Monitor Node and Interface Metrics** | Use Prometheus to monitor metrics like `node_network_transmit_queue_length` or `container_network_latency_seconds` for congestion signs. |


You need to enforce specific resource limits and security controls on multi-tenant workloads. How would you implement that?

| Strategy | Description |
|----------|-------------|
| 1. **Use Namespaces with Resource Quotas and LimitRanges** | Enforce CPU/memory usage caps per tenant using `ResourceQuota` and `LimitRange` objects in each namespace. |
| 2. **Apply PodSecurity Standards or OPA/Gatekeeper Policies** | Restrict privilege escalation, host access, and unsafe capabilities using built-in PodSecurity levels or custom Gatekeeper constraints. |
| 3. **Isolate Network Traffic with NetworkPolicies** | Use Kubernetes `NetworkPolicy` to limit communication between tenants, enforcing strict inter-namespace traffic boundaries. |
| 4. **Use RBAC for Tenant-Specific Access Control** | Define RoleBindings and ClusterRoleBindings to grant least-privilege access to tenant teams within their namespaces. |
| 5. **Monitor and Audit with Multi-Tenant Observability Tools** | Integrate tools like Prometheus, Loki, and Kyverno with label-based scoping to track and enforce tenant-specific usage and policy compliance. |




A Helm upgrade failed halfway. How do you recover and ensure consistency in the cluster?

| Step | Description |
|------|-------------|
| 1. **Check Helm Release History** | Run `helm history <release-name>` to identify the failed revision and assess what changes were attempted during the upgrade. |
| 2. **Rollback to Last Known Good Revision** | Use `helm rollback <release-name> <previous-revision>` to restore the last successful state of the application. |
| 3. **Inspect Logs and Resources for Inconsistencies** | Review pod logs, events (`kubectl describe`) and resource states to ensure partial changes didn’t leave the app in a broken state. |
| 4. **Manually Clean Up Orphaned or Failed Resources** | Identify and delete partially applied resources (e.g., PVCs, Services) using `kubectl get all` to avoid future deployment issues. |
| 5. **Use `--atomic` and `--cleanup-on-fail` in Future Upgrades** | Ensure future upgrades are safer by using `helm upgrade --atomic --cleanup-on-fail` to auto-rollback if errors occur. |


You’ve been asked to create a multi-region active-active Kubernetes setup. What design principles and tools would you use?

| Design Principle / Tool                  | Description                                                                                      |
|------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Global Load Balancing (e.g., GSLB)**   | Use tools like **Cloudflare Load Balancer**, **AWS Route 53**, or **NGINX Global Load Balancer** to route traffic intelligently between regions based on health and proximity. |
| **Federated Clusters / Multi-Cluster Management** | Use tools like **KubeFed**, **Rancher**, or **Anthos** to manage workloads and policies across multiple clusters. |
| **Data Replication & Consistency**       | Ensure real-time or near real-time data sync using **multi-region databases** (e.g., CockroachDB, YugabyteDB, or Amazon Aurora Global). |
| **Service Mesh (e.g., Istio, Linkerd)**  | Use service mesh with **multi-cluster support** for secure, reliable service-to-service communication across regions. |
| **CI/CD with Multi-Region Awareness**    | Implement pipelines using **ArgoCD** or **Flux** with cluster selectors to deploy apps regionally or globally based on configuration. |
