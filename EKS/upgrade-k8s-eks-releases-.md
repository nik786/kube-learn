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
- [Kubernetes Upgrades](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

- [Kubernetes 1.29 Release Notes](https://v1-29.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Kubernetes 1.30 Release Notes](https://v1-30.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Kubernetes 1.31 Release Notes](https://v1-31.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Kubernetes Blog](https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/)
- [udemy upgrade video](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/learn/lecture/24458188#overview)
  

Upgrade Process on Bare metal
-------------------------------

# Kubernetes Upgrade Steps

## Control Plane Nodes

| Step                                | Command                                                                                                         | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **1. Kubernetes Upgrade Docs**      | [Kubernetes Upgrade Documentation](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) | Read through the official Kubernetes upgrade documentation.                 |
| **2. Check the Nodes Version**      | `kubectl get nodes`                                                                                            | Verify the current Kubernetes version of all nodes in the cluster.          |
| **3. Check the OS Version**         | `cat /etc/*release*`                                                                                           | Check the operating system version of the nodes.                            |
| **4. Changing Package Repository**  | `echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /" \| sudo tee /etc/apt/sources.list.d/kubernetes.list` | Add Kubernetes apt repository for version 1.29. |
| **5. Import the Kubernetes APT GPG Key** | `curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg` | Import the GPG key for the Kubernetes repository. |
| **6. Update Package Information**   | `apt-get update`                                                                                               | Update the local package index.                                             |
| **7. Check Available Versions of kubeadm** | `apt-cache madison kubeadm`                                                                                  | List the available versions of `kubeadm` for installation.                  |
| **8. Install Specific Version of kubeadm** | `apt-get update && apt-get install -y kubeadm=1.30.0-1.1`                                                    | Install the specified version of `kubeadm`.                                 |
| **9. Check kubeadm Version**        | `kubeadm version`                                                                                             | Verify the installed version of `kubeadm`.                                  |
| **10. Check Upgrade Plan**          | `kubeadm upgrade plan`                                                                                        | Display the upgrade plan for the cluster.                                   |
| **11. Apply Upgrade**               | `kubeadm upgrade apply v1.30.0`                                                                               | Apply the upgrade to Kubernetes control plane components.                   |
| **12. Drain Node**                  | `kubectl drain controlplane --ignore-daemonsets`                                                              | Drain a node to prepare for upgrading or maintenance.                       |
| **13. Install New Versions of kubelet, kubectl** | `apt-get update && apt-get install -y kubelet=1.30.0 kubectl=1.30.0`                                         | Install the new versions of `kubelet` and `kubectl`.                        |
| **14. Reload and Restart kubelet**  | `systemctl daemon-reload && systemctl restart kubelet`                                                        | Reload and restart the `kubelet` service to apply changes.                  |
| **15. Uncordon Node**               | `kubectl uncordon controlplane`                                                                               | Mark the node as schedulable after maintenance.                             |
| **16. Verify Node Status**          | `kubectl get nodes`                                                                                           | Check the status of all nodes in the cluster.                               |

## Worker Nodes

| Step                                | Command                                                                                                         | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **1. Changing Package Repository**  | `echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /" \| sudo tee /etc/apt/sources.list.d/kubernetes.list` | Add Kubernetes apt repository for version 1.29. |
| **2. Import the Kubernetes APT GPG Key** | `curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg` | Import the GPG key for the Kubernetes repository. |
| **3. Update Package Information**   | `apt-get update`                                                                                               | Update the local package index.                                             |
| **4. Check Available Versions of kubeadm** | `apt-cache madison kubeadm`                                                                                  | List the available versions of `kubeadm` for installation.                  |
| **5. Install Specific Version of kubeadm** | `apt-get update && apt-get install -y kubeadm=1.30.0-1.1`                                                    | Install the specified version of `kubeadm`.                                 |
| **6. Check kubeadm Version**        | `kubeadm version`                                                                                             | Verify the installed version of `kubeadm`.                                  |
| **7. Upgrade Node**                 | `kubeadm upgrade node`                                                                                        | Upgrade the worker node components.                                         |
| **8. Drain Node**                   | `kubectl drain node01 --ignore-daemonsets`                                                                    | Drain a node to prepare for upgrading or maintenance.                       |
| **9. Install New Versions of kubelet, kubectl** | `apt-get update && apt-get install -y kubelet=1.30.0 kubectl=1.30.0`                                         | Install the new versions of `kubelet` and `kubectl`.                        |
| **10. Reload and Restart kubelet**  | `systemctl daemon-reload && systemctl restart kubelet`                                                        | Reload and restart the `kubelet` service to apply changes.                  |
| **11. Uncordon Node**               | `kubectl uncordon node01`                                                                                     | Mark the node as schedulable after maintenance.                             |
| **12. Verify Node Status**          | `kubectl get nodes`                                                                                           | Check the status of all nodes in the cluster.                               |










| Command                | Description                                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| **systemctl daemon-reload** | Instructs `systemd` to reload its configuration, typically after changes to service unit files or configuration files. |
| **Daemon**              | Refers to background services or processes running on a system.                                                   |
| **Reload**              | Tells `systemd` to re-scan its configuration files (e.g., service unit files) without restarting the entire system. |







EKS CLUSTER UPGARDE Process
---------------------
| Step | Action                                                                                                   |
|------|----------------------------------------------------------------------------------------------------------|
| 1    | **Plan the Upgrade:** Review AWS release notes and the Kubernetes changelog for your target version to understand feature changes and deprecations. |
| 2    | **Back Up:** Before starting, take a backup of your cluster's resources (e.g., ETCD backup, configuration, etc.). Ensure that persistent data and stateful applications are backed up. |
| 3    | **Test in Non-Prod Environment:** Perform the upgrade in a development or staging environment first to identify potential issues before applying it to production. |
| 4    | **Check Add-ons Compatibility:** Ensure that any EKS-managed add-ons (e.g., kube-proxy, CoreDNS, VPC CNI) and custom add-ons (e.g., Helm, Prometheus) are compatible with the new Kubernetes version. |
| 5    | **Upgrade Control Plane First:** Always upgrade the control plane (EKS master nodes) before upgrading worker nodes. |
| 6    | **Roll Nodes Gradually:** Upgrade node groups one by one. Ensure workloads are successfully running on upgraded nodes before proceeding to the next. |
| 7    | **Monitor Cluster Health:** During and after the upgrade, monitor the cluster health using AWS CloudWatch and Kubernetes tools (kubectl, eksctl). |
| 8    | **Plan for Downtime:** While EKS supports in-place control plane upgrades, some downtime may occur if you have workloads that are incompatible with the new Kubernetes version. Plan accordingly and notify stakeholders. |



| Feature                          | Managed Node Group                        | Self-Managed Node Group                  |
|----------------------------------|-------------------------------------------|------------------------------------------|
| Upgrade specific node            | ❌ Not supported                           | ✅ Possible manually                      |
| Upgrade entire group (rolling)   | ✅ Supported via `eksctl`                  | ✅ Supported via ASG + Launch Template    |
| Auto rejoin after upgrade        | ✅ Yes                                     | ✅ With proper bootstrap script           |
| Node control granularity         | ❌ Group-based only                        | ✅ Per-node control                       |





| Step                               | Command                                                                                                 |
|------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Upgrade Control Plane**          | `eksctl upgrade cluster --name <cluster-name> --region <region> --approve`                               |
|                                    | *(Optional: To specify a version)* `eksctl upgrade cluster --name <cluster-name> --region <region> --version <k8s-version>` |
| **Update EKS Managed Add-ons**     | *After upgrading the control plane, update the add-ons:*                                                |
| **Upgrade CoreDNS**                | `eksctl utils update-coredns --cluster <cluster-name> --region <region> --approve`                       |
| **Upgrade kube-proxy**             | `eksctl utils update-kube-proxy --cluster <cluster-name> --region <region> --approve`                    |












EKS CLUSTER UPGARDE
----------------------
| Step                                  | Command/Action                                                                                             |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Upgrade Node Groups**               | To upgrade the worker nodes, create a new node group with the new Kubernetes version and migrate workloads. |
| **Managed Node Group Upgrade**        | `eksctl upgrade nodegroup --cluster <cluster-name> --name <nodegroup-name> --region <region>`                |
| **Self-managed Node Groups**          | *For self-managed node groups, follow these steps:*                                                         |
| **Create a New Node Group**           | Follow the procedure to create a new node group with the new version.                                      |
| **Drain Nodes in Old Group**          | `kubectl drain <node-name> --ignore-daemonsets --delete-local-data`                                         |
| **Terminate Old Nodes**               | Terminate the old node group nodes once drained.                                                           |
| **Uncordon Nodes After Upgrade**     | `kubectl uncordon <node-name>`                                                                               |
| **Verify Control Plane Version**      | `kubectl version --short`                                                                                  |
| **Verify Nodes Version**              | `kubectl get nodes`                                                                                         |
| **Monitor Cluster Health**            | Keep an eye on the cluster health using CloudWatch or Kubernetes dashboard.                                |
| **Check Pods**                        | `kubectl get pods --all-namespaces`                                                                          |
| **Check Nodes**                       | `kubectl get nodes`                                                                                         |


Generic Upgrade process
---------------------------------



| Step                                | Description                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Control Plane Components**        | *Upgrade the master components first:*                                                                    |
|                                     | - `Kube-ApiServer-v1.10`                                                                                  |
|                                     | - `controller-manager-v1.10`                                                                               |
|                                     | - `kube-scheduler-v1.10`                                                                                   |
|                                     | - `kubectl v1.10`                                                                                         |
|                                     | - `kubelet-v1.10`                                                                                         |
|                                     | - `kube-proxy-v1.10`                                                                                      |
| **Worker Nodes (Data Plane)**       | *After upgrading control plane, upgrade components in worker nodes (data plane).*                        |
| **Upgrade Strategies**              | *Choose one of the following upgrade strategies:*                                                        |
| **Strategy 1: Upgrade All at Once** | Upgrade all components (control plane and worker nodes) at the same time. Expect downtime.                |
| **Strategy 2: Upgrade One by One** | Upgrade components one by one, shifting workloads to other nodes to minimize downtime.                    |
| **Strategy 3: Add New Node**       | Add new nodes with newer versions, then migrate workloads to these new nodes. No downtime.                |

| Feature              | Cordon                                                              | Drain                                                                |
|----------------------|---------------------------------------------------------------------|----------------------------------------------------------------------|
| **Definition**        | Marks a node as unschedulable, preventing new pods from being scheduled on it. | Evicts all pods from a node, safely terminating them and making the node ready for maintenance. |
| **Effect on Pods**    | Does not affect the pods already running on the node.               | Evicts pods from the node, terminating them and triggering rescheduling if needed. |
| **Use Case**          | Used when you want to stop new pods from being scheduled on a node but keep existing pods running. | Used when preparing a node for maintenance or upgrade by evacuating all pods from the node. |
| **Pod Rescheduling**  | Existing pods remain on the node until manually removed or terminated. | Pods are rescheduled on other nodes, provided they are not marked with `NoSchedule` taints or similar constraints. |
| **Command**           | `kubectl cordon <node-name>`                                         | `kubectl drain <node-name> --ignore-daemonsets`                       |

| Feature              | Taint                                                               | Toleration                                                           |
|----------------------|---------------------------------------------------------------------|----------------------------------------------------------------------|
| **Definition**        | A taint is applied to a node to repel pods from being scheduled on it unless they tolerate the taint. | A toleration is applied to a pod to allow it to be scheduled on nodes with specific taints. |
| **Use Case**          | Used to prevent pods from being scheduled on certain nodes unless explicitly allowed. | Used to allow pods to be scheduled on nodes with taints. |
| **Effect on Pods**    | Taints affect which pods can be scheduled on the node. Pods that do not tolerate the taint will not be scheduled. | Tolerations enable pods to be scheduled on nodes with matching taints. |
| **Applied By**        | Taints are applied to nodes.                                        | Tolerations are applied to pods.                                      |
| **Command**           | `kubectl taint nodes <node-name> <key>=<value>:<effect>`             | `tolerations` field in the pod specification (YAML)                   |








| Concept            | Affinity                                                                 | Anti-Affinity                                                          |
|--------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Purpose**        | Specifies conditions for preferential or required placement of a pod on nodes or in relation to other pods. | Specifies that a pod should avoid being scheduled on the same node or close to other pods with certain labels. |
| **Types**          | - **Node Affinity**: Controls on which nodes the pod can be scheduled based on node labels (more flexible than `nodeSelector`).<br>- **Pod Affinity**: Specifies that the pod should be scheduled on the same node or close to other pods with certain labels. | - **Pod Anti-Affinity**: Ensures that pods are scheduled away from other pods based on labels. |
| **Usage Scenarios**| - **Workload Segmentation**: Assign workloads to specific nodes with certain hardware (e.g., GPU nodes).<br>- **Data Locality**: Schedule pods close to other pods they frequently interact with to reduce network latency. | - **High Availability**: Spread replicas of the same application across multiple nodes or availability zones to improve resilience.<br>- **Resource Isolation**: Prevent certain pods from being scheduled on the same node to avoid resource contention. |
| **Summary**        | Defines conditions for preferring or requiring a pod to be scheduled on the same node or close to specific nodes/pods. | Defines conditions for preferring or requiring that a pod be scheduled away from specific nodes/pods, promoting distribution and resilience. |







1. **How does Amazon EKS handle node group upgrades, and what strategies can be used to minimize downtime during the upgrade process?**
   



# Steps to Upgrade EKS Cluster Control Plane and Worker Nodes Using Terraform Without Downtime






How can I detach a worker node from an EKS cluster, perform patching, and then automatically 
rejoin it to the cluster once patching is complete? The entire process needs to be automated.

Solution-1
-----------

| Step | Action | Description |
|------|--------|-------------|
| 1 | **Enable SSM on EC2 Worker Nodes** | Ensure each worker node has the SSM Agent installed, running, and attached to an IAM role with `AmazonSSMManagedInstanceCore`. Tag nodes with `PatchGroup=eks-workers`. |
| 2 | **Create Lifecycle Hook in ASG** | Add a lifecycle hook to pause EC2 instance termination (or detachment) to allow patching operations to complete before node replacement. |
| 3 | **Cordon and Drain Node** | Use `kubectl cordon` and `kubectl drain` to safely evict workloads from the node before patching. |
| 4 | **Patch Node Using SSM Patch Manager** | Use Patch Manager to patch based on a predefined baseline. Patch can be triggered on-demand or scheduled. |
| 5 | **Reboot and Resume ASG Lifecycle** | After patching (and reboot if needed), call `complete-lifecycle-action` to continue the node's ASG lifecycle. |
| 6 | **Rejoin Node to EKS** | The node will automatically rejoin the EKS cluster via the Auto Scaling Group and EKS node group configuration. Verify with `kubectl get nodes`. |
| 7 | **Optional: Automate via Lambda or Step Functions** | Use EventBridge + Lambda to handle cordon, patching, and lifecycle actions automatically based on ASG events. |



Solution-2
------------











Self-managed Node Group (ASG with Launch Template)
---------------------------------------------------


| Step | Task                          | Command/Details                                                                                     |
|------|-------------------------------|------------------------------------------------------------------------------------------------------|
| 1    | Update Launch Template        | Create a new version with updated AMI or configuration using AWS Console or CLI.                    |
| 2    | Trigger Instance Refresh      | `aws autoscaling start-instance-refresh --auto-scaling-group-name <asg-name> \                      |
|      |                               | --preferences '{"MinHealthyPercentage":90,"InstanceWarmup":300}'`                                   |
| 3    | Verify New Nodes              | `kubectl get nodes -o wide`                                                                         |
| 4    | Cordon Old Nodes              | `kubectl cordon <old-node-name>`                                                                    |
| 5    | Drain Old Nodes               | `kubectl drain <old-node-name> --ignore-daemonsets --delete-emptydir-data`                         |
| 6    | Optional: Terminate Old Nodes| AutoScaling will terminate them post-refresh or do manually if needed.                             |
| 7    | Optional: Scale Desired Count| `aws autoscaling update-auto-scaling-group --auto-scaling-group-name <asg-name> \                   |
|      |                               | --desired-capacity <count>`                                                                         |




EKS Managed Node Group (with eksctl or Console)
------------------------------------------------


| Step | Task                          | Command/Details                                                                                     |
|------|-------------------------------|------------------------------------------------------------------------------------------------------|
| 1    | Update Launch Template        | Create a new version of the launch template with updated AMI.                                       |
| 2    | Upgrade Nodegroup             | `eksctl upgrade nodegroup --name <nodegroup-name> --cluster <cluster-name> \                        |
|      |                               | --launch-template-version <version> --approve --region <region>`                                    |
| 3    | Verify New Nodes              | `kubectl get nodes -o wide`                                                                         |
| 4    | Cordon Old Nodes              | `kubectl cordon <old-node-name>`                                                                    |
| 5    | Drain Old Nodes               | `kubectl drain <old-node-name> --ignore-daemonsets --delete-emptydir-data`                         |
| 6    | Wait for Auto Replace         | EKS handles draining and replacement; old nodes will be terminated automatically.                   |
| 7    | Optional Monitoring           | Watch rolling update progress via `eksctl` or AWS Console.                                          |














