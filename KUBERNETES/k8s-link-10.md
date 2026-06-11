9. How do you troubleshoot slow image pulls in Kubernetes?

10. What is an emptyDir volume and how does it behave during pod restarts?

11. Describe how you would use Kubernetes to run scheduled data pipelines.

12. How does Kubernetes handle IP address assignment for pods?

| Step | Kubernetes IP Assignment |
|------|--------------------------|
| 1 | Each Pod gets a unique IP address from the cluster Pod CIDR. |
| 2 | The CNI plugin (Calico, Cilium, Flannel, AWS VPC CNI) assigns the Pod IP. |
| 3 | Pods on the same node communicate directly using Pod IPs. |
| 4 | Pods across different nodes communicate through the CNI network overlay/routing. |
| 5 | Pod IPs are ephemeral and change when Pods are recreated. |
| 6 | Services provide stable virtual IPs (ClusterIP) to access Pods reliably. |

Easy Mnemonic: P-C-C-R-E-S
P → Pod gets a unique IP
C → CNI assigns the IP
C → Communication within the node
R → Routing across nodes
E → Ephemeral Pod IPs
S → Services provide Stable IPs
20-Second Interview Answer

"In Kubernetes, each Pod receives a unique IP from the Pod CIDR through the CNI plugin. Pods communicate directly using Pod IPs, while the CNI handles routing across nodes. Since Pod IPs are ephemeral, Kubernetes Services provide stable virtual IPs to ensure reliable service discovery and communication."

14. Explain the differences between using ConfigMaps and environment variables for configuration.

15. What is a ResourceQuota and how is it enforced in a namespace?

16. How do you use the Horizontal Pod Autoscaler with custom metrics?

| Step | HPA with Custom Metrics |
|------|-------------------------|
| 1 | Expose application metrics (e.g., queue length, RPS, active users). |
| 2 | Collect metrics using Prometheus. |
| 3 | Use Prometheus Adapter to expose metrics to Kubernetes Metrics API. |
| 4 | Configure HPA to use custom metrics instead of CPU/Memory. |
| 5 | Define min/max replicas and target metric thresholds. |
| 6 | Monitor scaling behavior and tune thresholds as needed. |


Easy Mnemonic: E-C-A-H-T-M

E → Expose Metrics
C → Collect (Prometheus)
A → Adapter (Prometheus Adapter)
H → HPA Configuration
T → Thresholds
M → Monitor & Tune
20-Second Interview Answer

"For HPA with custom metrics, I expose application metrics such as queue length or requests per second, collect them using Prometheus, and use Prometheus Adapter to make them available to Kubernetes. I then configure the HPA with target thresholds and min/max replicas, and continuously monitor and tune the scaling behavior for optimal performance."




18. What are Kubernetes finalizers and why might a resource be stuck in Terminating state because of one?
