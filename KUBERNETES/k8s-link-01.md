



1. What are the key differences between a Deployment and a StatefulSet in Kubernetes?

2. How would you safely perform a node upgrade in a Kubernetes cluster?

  - [EKS-UPGRADE-BY-TERRAFORM](https://github.com/nik786/kube-learn/blob/master/EKS/EKS-Cluster-Upgrade-Zero-Downtime-Terraform-Self-Managed-Nodes.md)
  - [EKS-UPGRADE-BY-EKSCTL](https://github.com/nik786/kube-learn/blob/master/EKS/EKS_Cluster_Upgrade_using_eksctl.md)
  - [K8S-UPGRADE-ON-PREM](https://github.com/nik786/kube-learn/blob/master/EKS/k8s_upgrade_onprem.md)
  - [EKS-UPGRADE-BY-AWSCLI](https://github.com/nik786/kube-learn/blob/master/EKS/EKS-CLUSTER-UPGRADE-AWSCLI.md)
  - [K8S-RELAESE-NOTES](https://github.com/nik786/kube-learn/blob/master/EKS/K8S-CLUSTER-REALEASE-NOTES.md)



4. How do you handle Kubernetes manifest version mismatches across environments?
   
| # | Approach                        | Description                                                                                                                                           |
| - | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Standardize Kubernetes Versions | Keep development, staging, and production clusters on closely aligned Kubernetes versions to minimize API compatibility issues.                       |
| 2 | Use Helm or Kustomize           | Maintain a single source of truth for manifests and apply environment-specific overrides using Helm values or Kustomize overlays.                     |
| 3 | Validate in CI/CD               | Use tools such as `kubectl --dry-run`, `kubeconform`, or `kubeval` to validate manifests against the target cluster version before deployment.        |
| 4 | Track API Deprecations          | Regularly review Kubernetes release notes and migrate deprecated APIs (e.g., `extensions/v1beta1` to `networking.k8s.io/v1`) before cluster upgrades. |
| 5 | Implement GitOps Practices      | Use GitOps tools like Argo CD or Flux to ensure consistent manifest versions across environments and quickly detect configuration drift.              |


6. What happens to a pod if the node it’s running on suddenly crashes?

| # | Behavior                      | Description                                                                                                                                                      |
| - | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Pod Becomes Unreachable       | When a node crashes, the pods running on that node stop responding because the underlying container runtime is no longer available.                              |
| 2 | Node Marked NotReady          | The Kubernetes control plane detects missed heartbeats from the node and marks it as `NotReady` after a grace period.                                            |
| 3 | Pods Marked Failed or Unknown | Pods on the failed node transition to `Unknown` or `Terminating` state as Kubernetes determines that the node is unavailable.                                    |
| 4 | Replacement Pods Scheduled    | If the pods are managed by a Deployment, ReplicaSet, or StatefulSet, Kubernetes creates replacement pods on healthy nodes to maintain the desired replica count. |
| 5 | Service Traffic Redirected    | Kubernetes Services automatically stop routing traffic to the failed pods and direct requests to healthy pod replicas running on other nodes.                    |


8. How do you configure and use an Admission Controller in Kubernetes?

| No. | Answer  |
|------|--------|
| 1 | Admission Controllers are Kubernetes components that intercept API requests after authentication and authorization but before objects are stored in etcd. |
| 2 | They are configured by enabling built-in admission plugins using the `--enable-admission-plugins` flag on the API Server or by deploying Mutating/Validating Admission Webhooks and registering them with Kubernetes. |
| 3 | Admission Controllers are used to enforce security, compliance, and operational policies, such as requiring resource limits, restricting privileged containers, or automatically injecting sidecars. |
| 4 | Unlike RBAC, which controls **who can perform an action**, Admission Controllers control **what can be created or modified** and can inspect or alter resource configurations. |
| 5 | Benefits include centralized policy enforcement, improved security, automated resource standardization, reduced manual configuration, and prevention of misconfigured workloads. |
| 6 | Example: A Validating Admission Webhook can reject Pod creation requests if containers are configured to run as root, ensuring compliance with organizational security standards. |


10. What strategies would you use to minimize container startup time?

| # | Strategy                          | Description                                                                                                                                      |
| - | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Use Smaller Base Images           | Choose lightweight images such as Alpine, Distroless, or minimal runtime images to reduce image download and startup time.                       |
| 2 | Optimize Image Layers             | Use multi-stage builds, remove unnecessary packages, and minimize layers to reduce image size and improve pull performance.                      |
| 3 | Pre-Pull Images on Nodes          | Configure nodes to cache frequently used container images so pods can start without waiting for image downloads.                                 |
| 4 | Reduce Application Initialization | Optimize application startup logic by avoiding heavy initialization tasks, large dependency loading, and unnecessary database calls during boot. |
| 5 | Tune Kubernetes Resources         | Set appropriate CPU and memory requests/limits to avoid scheduling delays and ensure containers receive sufficient resources during startup.     |


12. What are Mutating and Validating Webhooks in Kubernetes, and when would you use them?



| # | Answer |
|---|--------|
| 1 | Mutating Webhooks automatically modify Kubernetes resources before they are stored, enabling default configurations, labels, annotations, or sidecar injection. |
| 2 | Validating Webhooks evaluate resource requests and either approve or reject them based on defined policies and compliance requirements. |
| 3 | Mutating Webhooks run before Validating Webhooks, ensuring all modifications are applied prior to policy enforcement. |
| 4 | Mutating Webhooks are commonly used to inject service mesh sidecars, add security settings, and apply organizational standards automatically. |
| 5 | Validating Webhooks are used to enforce security controls, restrict container privileges, validate resource specifications, and ensure policy compliance. |
| 6 | Both webhook types are implemented as external HTTPS services and registered with Kubernetes through webhook configuration resources to enforce custom admission policies. |










