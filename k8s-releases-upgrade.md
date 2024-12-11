# Kubernetes 1.29, 1.30, and 1.31 Release Features and Deprecations

| **Release Version** | **Feature**                                                                                  | **Deprecation**                                                                                |
|---------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Kubernetes 1.29**  | - ReadWriteOncePod PersistentVolume access mode becomes stable.                               | - Deprecated support for cloud controller manager in kube-controller-manager.                  |
|                     | - AppArmor support becomes stable for container security.                                     | - Removal of `in-tree` volume plugins for cloud providers (move to external cloud volume plugins).|
|                     | - NetworkPolicy API stability improvements.                                                   | - Removing deprecated HTTP version 1.1 API for communication between pods.                    |
|                     | - Enhancements for kubectl diff to show output better and enable better auditing.             | - Deprecated API versions will no longer be available after v1.30.                             |
|                     | - Support for `local ephemeral storage` resources for Pod scheduling.                         | - Deprecation of certain flags like `--allow-privileged` in Kubernetes API server configuration.|
| **Kubernetes 1.30**  | - Service proxy (kube-proxy) improves ingress connectivity reliability.                        | - Deprecation of the `in-tree` NFS provisioner.                                                |
|                     | - Support for dynamic configuration of external IP addresses for LoadBalancer services.      | - Removal of the legacy cgroups v1 support for the `kubelet`.                                   |
|                     | - New `PodOverhead` feature for better resource management.                                   | - Deprecation of certain flags in `kubectl` commands related to debugging.                     |
|                     | - Support for `PodSecurity` policy enforcement through OPA-Gatekeeper.                        | - Removal of older deprecated API versions.                                                    |
|                     | - Features around `kubectl` to improve usability in managing Kubernetes workloads.            | - Deprecation of certain internal metrics APIs.                                                |
| **Kubernetes 1.31**  | - Stable support for `AppArmor` profiles in container `securityContext`.                      | - Removal of deprecated CNI plugins.                                                           |
|                     | - Enhanced Kubelet to improve node reliability and control.                                  | - Deprecation of older security-related APIs in the kube-apiserver.                           |
|                     | - Support for new CRI features to manage container runtime configurations.                    | - Removal of deprecated flags in control plane components.                                     |
|                     | - Improvements in Horizontal Pod Autoscaling (HPA) metrics and scaling behaviors.             | - Deprecated `Docker` runtime support, with emphasis on containerd and CRI-O.                  |
|                     | - Introduction of more flexible and configurable `KubeProxy` settings for advanced networking. | - Removal of legacy endpoint slices and deprecation of older features in cluster DNS.          |

For more information on the Kubernetes releases, you can check out the official release notes:
- [Kubernetes 1.29 Release Notes](https://kubernetes.io/docs/setup/release/notes/)
- [Kubernetes 1.30 Release Notes](https://kubernetes.io/docs/setup/release/notes/)
- [Kubernetes 1.31 Release Notes](https://kubernetes.io/docs/setup/release/notes/)


cat /etc/*releases*

https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/
https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg


echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

apt-get update
apt-cache madison kubeadm
apt-get update && apt-get install -y kubeadm='1.31.x-*'


kubeadm version

kubeadm upgrade plan

kubeadm upgrade apply v1.31.x

kubectl drain <node-to-drain> --ignore-daemonsets




apt-get update && apt-get install -y kubelet='1.31.x-*' kubectl='1.31.x-*'
apt-mark hold kubelet kubectl


systemctl daemon-reload

The systemctl daemon-reload command is used to instruct systemd, the init system used by many Linux distributions, 
to reload its configuration. This command is typically run after making changes to service unit files or configuration file

Daemon: Refers to background services or processes that are running on a system.
Reload: Tells systemd to re-scan its configuration files, such as service unit files, without restarting the entire system.






systemctl restart kubelet

kubectl uncordon <node-to-uncordon>

kubectl get nodes



EKS CLUSTER UPGARDE
Plan the Upgrade: Review AWS release notes and the Kubernetes changelog for your target version to understand feature changes and deprecations.
Back Up: Before starting, take a backup of your cluster's resources (e.g., ETCD backup, configuration, etc.). Ensure that persistent data and stateful applications are backed up.
Test in Non-Prod Environment: Perform the upgrade in a development or staging environment first to identify potential issues before applying it to production.
Check Add-ons Compatibility: Ensure that any EKS-managed add-ons (e.g., kube-proxy, CoreDNS, VPC CNI) and custom add-ons (e.g., Helm, Prometheus) are compatible with the new Kubernetes version.
Upgrade Control Plane First: Always upgrade the control plane (EKS master nodes) before upgrading worker nodes.
Roll Nodes Gradually: Upgrade node groups one by one. Ensure workloads are successfully running on upgraded nodes before proceeding to the next.
Monitor Cluster Health: During and after the upgrade, monitor the cluster health using AWS CloudWatch and Kubernetes tools (kubectl, eksctl
Plan for Downtime: While EKS supports in-place control plane upgrades, some downtime may occur if you have workloads that are incompatible with the new Kubernetes version. Plan accordingly and notify stakeholders.











