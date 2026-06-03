



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

9. What strategies would you use to minimize container startup time?

10. What are Mutating and Validating Webhooks in Kubernetes, and when would you use them?














