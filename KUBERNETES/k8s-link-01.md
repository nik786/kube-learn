



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

7. How do you configure and use an Admission Controller in Kubernetes?

8. What strategies would you use to minimize container startup time?

9. What are Mutating and Validating Webhooks in Kubernetes, and when would you use them?

10. How does the kubectl drain command behave, and what does it do under the hood?




26. Describe how Kubernetes handles rolling back a failed deployment.

27. How can you use Network Policies to secure communication within a namespace?

28. What are some common issues with Helm chart templating, and how do you handle them?

29. How do you inspect pod logs for a job that has already completed?

30. Describe the process of configuring Kubernetes audit logging for compliance tracking.












