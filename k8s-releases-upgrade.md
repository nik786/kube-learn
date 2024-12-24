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

Daemon: Refers to background services or processes that are running on a system.<br><br>
Reload: Tells systemd to re-scan its configuration files, such as service unit files, 
without restarting the entire system.



systemctl restart kubelet

kubectl uncordon <node-to-uncordon>

kubectl get nodes



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


| Concept  | Cordon                                           | Taint                                                       |
|----------|--------------------------------------------------|-------------------------------------------------------------|
| **Purpose** | Marks a node as unschedulable, preventing new pods from being scheduled on it. | Adds a taint to a node, causing Kubernetes to repel pods that do not have a matching toleration. |
| **Behavior** | Existing pods continue running on a cordoned node, but no new pods will be scheduled. | Only pods with a matching toleration are allowed to be scheduled on the tainted node. Pods without a matching toleration may be evicted depending on the effect. |
| **Use Case** | Temporary maintenance or updates when you don't want new pods to be scheduled on a node but still want the current workloads to run. | Used for situations where specific nodes are dedicated for certain workloads (e.g., GPU nodes for machine learning) or need strict scheduling rules. |
| **Command** | `kubectl cordon <node-name>`                     | `kubectl taint nodes <node-name> <key>=<value>:<effect>`     |
| **Effect Options** | N/A                                              | - `NoSchedule`: New pods without a matching toleration are not scheduled. <br> - `PreferNoSchedule`: Kubernetes avoids scheduling pods without toleration but allows them if necessary. <br> - `NoExecute`: Evicts existing pods without a matching toleration and prevents new pods from scheduling. |
| **Example** | Cordon a node for maintenance: `kubectl cordon <node-name>` | Taint a node for GPU workloads: `kubectl taint nodes <node-name> gpu=true:NoSchedule` |
| **Summary** | Prevents new pods from being scheduled temporarily, but does not affect existing pods. | Controls which pods can be scheduled based on tolerations, with the ability to prevent scheduling and evict incompatible pods. |


| Concept           | Affinity                                                              | Anti-Affinity                                                        |
|-------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------|
| **Purpose**       | Specifies conditions for preferential or required placement of a pod on nodes or in relation to other pods. | Specifies that a pod should avoid being scheduled on the same node or close to other pods with certain labels. |
| **Types**         | - **Node Affinity**: Controls on which nodes the pod can be scheduled based on node labels (more flexible than `nodeSelector`).<br>- **Pod Affinity**: Specifies that the pod should be scheduled on the same node or close to other pods with certain labels. | - **Pod Anti-Affinity**: Ensures that pods are scheduled away from other pods based on labels. |
| **Usage Scenarios** | - **Workload Segmentation**: Assign workloads to specific nodes with certain hardware (e.g., GPU nodes).<br>- **Data Locality**: Schedule pods close to other pods they frequently interact with to reduce network latency. | - **High Availability**: Spread replicas of the same application across multiple nodes or availability zones to improve resilience.<br>- **Resource Isolation**: Prevent certain pods from being scheduled on the same node to avoid resource contention. |
| **Example**       | Prefer to schedule a pod on nodes labeled with `zone=us-west`:<br>```yaml<br>affinity:<br>  nodeAffinity:<br>    requiredDuringSchedulingIgnoredDuringExecution:<br>      nodeSelectorTerms:<br>        - matchExpressions:<br>            - key: zone<br>              operator: In<br>              values:<br>                - us-west<br>``` | Ensure pods with label `app=nginx` are scheduled away from other `nginx` pods: <br>```yaml<br>affinity:<br>  podAntiAffinity:<br>    requiredDuringSchedulingIgnoredDuringExecution:<br>      - labelSelector:<br>          matchExpressions:<br>            - key: app<br>              operator: In<br>              values:<br>                - nginx<br>        topologyKey: "kubernetes.io/hostname"<br>``` |
| **Summary**       | Defines conditions for preferring or requiring a pod to be scheduled on the same node or close to specific nodes/pods. | Defines conditions for preferring or requiring that a pod be scheduled away from specific nodes/pods, promoting distribution and resilience. |



| Step                           | Command                                                                                 | Description |
|--------------------------------|-----------------------------------------------------------------------------------------|-------------|
| **1. Check the Current Cluster Version** | `eksctl get cluster --name=<your-cluster-name> --region=<your-region>`                   | Check the current Kubernetes version of your EKS cluster. |
| **2. Check Available Kubernetes Versions** | `eksctl utils describe-stacks --region=<your-region> --name=<your-cluster-name>`         | List available Kubernetes versions for the cluster. |
| **3. Update eksctl and AWS CLI** | `eksctl version`<br>`aws --version`                                                     | Ensure you are using the latest version of eksctl and AWS CLI for compatibility. |
| **4. Update the EKS Cluster** | `eksctl upgrade cluster --name=prod-cluster --region=us-west-2 --kubernetes-version=1.25` | Upgrade the EKS cluster to the specified Kubernetes version. |
| **5. Upgrade Node Groups (if needed)** | `eksctl upgrade nodegroup --name=prod-nodegroup --cluster=prod-cluster --region=us-west-2 --kubernetes-version=1.25` | Upgrade the node group to the desired Kubernetes version. |
| **6. Upgrade All Node Groups** | `eksctl upgrade nodegroup --cluster=<your-cluster-name> --region=<your-region> --kubernetes-version=<desired-version> --all` | Upgrade all node groups to the specified Kubernetes version. |
| **7. Validate the Upgrade** | `kubectl version`<br>`kubectl get nodes`                                               | Validate that the upgrade was successful by checking the version and node status. |
| **8. Test the Cluster**      | `kubectl get pods --all-namespaces`<br>`kubectl get services --all-namespaces`          | Verify that all pods and services are running correctly after the upgrade. |
























