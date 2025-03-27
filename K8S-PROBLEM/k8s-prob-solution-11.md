# Kubernetes Performance and Security Strategies

## QoS Classes in Kubernetes

| **QoS Class**         | **Description**                                                                                                                                               | **Ideal Use Case**                                                                                           |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Guaranteed QoS**     | Pods with guaranteed QoS are allocated the highest priority. They are assured a certain amount of CPU and memory resources.                                     | Suitable for applications with strict performance requirements. Dedicated resources ensure no resource contention. |
| **Burstable QoS**      | Pods with burstable QoS are given a certain amount of CPU and memory resources, but they can consume more when available. They have no strict guarantees.       | Ideal for applications with varying resource demands. Performance may fluctuate during high demand periods.    |
| **Best Effort QoS**    | Pods with best-effort QoS have the lowest priority. They only receive resources if available and are the first to be evicted in case of resource shortage.     | Best for non-critical tasks that can tolerate interruptions or occasional slowdowns.                          |

## Kubernetes Security Strategies

| **Security Focus Area**         | **Strategy**                                                                                                                                                         |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Authentication & Authorization** | - Avoid using the `system:masters` group for user or component authentication after bootstrapping. <br> - Ensure the kube-controller-manager is running with `--use-service-account-credentials` enabled. <br> - Protect root certificates with offline or managed CA with access control. <br> - Set expiration date of intermediate and leaf certificates to no more than 3 years. <br> - Avoid running kube-controller-manager as `system:masters`. |
| **Network Security**             | - Apply ingress and egress network policies to all workloads. <br> - Implement default network policies denying everything. <br> - Use a service mesh for encrypting communications. <br> - Ensure Kubernetes API, kubelet API, and etcd are not exposed publicly. <br> - Filter access from workloads to cloud metadata API. <br> - Restrict use of LoadBalancer and ExternalIPs. |
| **Pod Security**                 | - Grant RBAC rights for creating, updating, patching, or deleting workloads only when necessary. <br> - Enforce appropriate Pod Security Standards. <br> - Set memory and CPU limits for workloads. <br> - Enable seccomp with appropriate syscall profiles. <br> - Enable AppArmor or SELinux on nodes that support it. |
| **Logs and Auditing**            | - Protect audit logs from general access. <br> - Disable the `/logs` API. <br> - Limit `/var/log` content to Kubernetes API server logs only. |
| **Secrets**                       | - Do not store confidential data in ConfigMaps. <br> - Enable encryption at rest for the Secret API. <br> - Use third-party storage mechanisms to inject secrets if needed. <br> - Avoid mounting service account tokens in unnecessary pods. <br> - Use bound service account token volumes instead of non-expiring tokens. |
| **Images**                        | - Minimize unnecessary content in container images. <br> - Run container images as unprivileged users. <br> - Reference container images by sha256 digests instead of tags. <br> - Regularly scan images for vulnerabilities and patch known issues. |

## Kubernetes Cluster Availability and Reliability Parameters

| **Parameter**                  | **Description**                                                                                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **node-status-update-frequency**| Configures the frequency of kubelet node status updates.                                                                                                          |
| **monitor-grace-period**        | Defines the grace period for the controller manager to wait before marking a node as unhealthy. The combination of both parameters defines a retry mechanism.      |
| **node-monitor-grace-period**   | A retry period for the kubelet to wait before declaring a node as unhealthy. The default is set to try 5 times before marking the node as unhealthy.               |
| **pod-eviction-timeout**        | The grace period for deleting pods from a node. By default, set to 5 minutes.                                                                                   |
| **node-monitor-period**         | Period in which the controller manager checks the status of nodes in the cluster. Defines how frequently the node status is checked for failure.                 |
