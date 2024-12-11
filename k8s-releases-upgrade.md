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
Reload: Tells systemd to re-scan its configuration files, such as service unit files, without restarting the entire system.






systemctl restart kubelet

kubectl uncordon <node-to-uncordon>

kubectl get nodes



EKS CLUSTER UPGARDE
Plan the Upgrade: Review AWS release notes and the Kubernetes changelog for your target version to understand feature changes and deprecations.<br><br>
Back Up: Before starting, take a backup of your cluster's resources (e.g., ETCD backup, configuration, etc.). Ensure that persistent data and stateful applications are backed up.<br><br>
Test in Non-Prod Environment: Perform the upgrade in a development or staging environment first to identify potential issues before applying it to production.<br><br>
Check Add-ons Compatibility: Ensure that any EKS-managed add-ons (e.g., kube-proxy, CoreDNS, VPC CNI) and custom add-ons (e.g., Helm, Prometheus) are compatible with the new Kubernetes version.<br><br>
Upgrade Control Plane First: Always upgrade the control plane (EKS master nodes) before upgrading worker nodes.<br><br>
Roll Nodes Gradually: Upgrade node groups one by one. Ensure workloads are successfully running on upgraded nodes before proceeding to the next.<br><br>
Monitor Cluster Health: During and after the upgrade, monitor the cluster health using AWS CloudWatch and Kubernetes tools (kubectl, eksctl
Plan for Downtime: While EKS supports in-place control plane upgrades, some downtime may occur if you have workloads that are incompatible with the new Kubernetes version. <br><br>
Plan accordingly and notify stakeholders.<br><br>


Upgrade Control Plane
To upgrade the control plane, use the following command:
eksctl upgrade cluster --name <cluster-name> --region <region> --approve
This command automatically upgrades the control plane to the latest supported version. 
If you want to specify a version, use --version <k8s-version>
Update EKS Managed Add-ons
After upgrading the control plane, you may need to update the add-ons
# Upgrade CoreDNS
eksctl utils update-coredns --cluster <cluster-name> --region <region> --approve
# Upgrade kube-proxy
eksctl utils update-kube-proxy --cluster <cluster-name> --region <region> --approve

EKS CLUSTER UPGARDE
----------------------
Upgrade Node Groups
----------------------
To upgrade the worker nodes, you’ll need to create a new node group with the new Kubernetes version and migrate your workloads. 
---------------------------------------------------------------------------------------------------------------------------------
Alternatively, you can update managed node groups directly:

Managed Node Group Upgrade
--------------------------------
eksctl upgrade nodegroup --cluster <cluster-name> --name <nodegroup-name> --region <region>

If you're using self-managed node groups, follow these steps:
Create a new node group.
------------------------------

Drain nodes in the old group and terminate them.
----------------------------------------------------
kubectl drain <node-name> --ignore-daemonsets --delete-local-data

After all the nodes are upgraded, uncordon them:
------------------------------------------------------
kubectl uncordon <node-name>

EKS CLUSTER UPGARDE
----------------------
Verify Cluster and Node Version
# Verify control plane version
-------------------------------
kubectl version --short

# Verify nodes version
kubectl get nodes


Monitor Cluster Health
-------------------------
Keep an eye on the cluster with CloudWatch or Kubernetes dashboard and ensure everything is functioning as expected.
kubectl get pods --all-namespaces
kubectl get nodes

Generic Upgrade process
---------------------------------
Kube-ApiServer-v1.10 control plane components
controller-manager-v1.10  kube-scheduler-v1.10 kubectlv1.10 
kubelet-v1.10 kube-proxy-v.10 data plane components 

First need to upgrade master components
Then we need to upgrade components in worker nodes
worker nodes - data plane

Stategy-1
all them upgrade at a time

dowtime
Strategy-2

upgrade one by one
shift workload to another node

Strategy-3
add new node with newer versions

Cordon:
--------

1. Purpose: Marks a node as unschedulable, preventing new pods from being scheduled on it.
2. Behavior: Existing pods continue running on a cordoned node, but no new pods will be scheduled.
3. Use Case: Temporary maintenance or updates when you don't want new pods to be scheduled on a node but still want the current workloads to run.

kubectl cordon <node-name>

Example: If you need to drain a node or upgrade it but want to keep existing pods running, cordon the node so that no new pods are scheduled while work is performed.

Taint
--------
1. Purpose: Adds a taint to a node, causing Kubernetes to repel pods that do not have a matching toleration.
2. Behavior: Only pods with a matching toleration are allowed to be scheduled on the tainted node. Any pod without a matching toleration will not be scheduled or, if already present, may be evicted depending on the taint effect.
3. Use Case: Situations where specific nodes are dedicated for certain workloads (e.g., GPU nodes for machine learning) or need strict scheduling rules.
kubectl taint nodes <node-name> <key>=<value>:<effect>

1. Key: Identifier for the taint.
2. Value: Optional value associated with the key.
3. Effect: Determines the taint effect:
4. NoSchedule: New pods without a matching toleration are not scheduled.
5. PreferNoSchedule: Kubernetes avoids scheduling pods without toleration but allows them if necessary.
6. NoExecute: Evicts existing pods without a matching toleration and prevents new pods from scheduli

Example: To ensure that only pods with a toleration can run on certain GPU nodes, you could taint those nodes with:
Summary of Differences:
-----------------------
Cordon: Prevents new pods from being scheduled temporarily, but does not affect existing pods.

Taint: Controls which pods can be scheduled based on tolerations, with the ability to prevent scheduling and evict incompatible pods.



Affinity and Anti-Affinity
----------------------------
In Kubernetes, affinity and anti-affinity are mechanisms that control how pods are placed on nodes based on specific rules.
Affinity
Purpose: Affinity rules specify conditions for preferential or required placement of a pod on nodes or in relation to other pods.
Types of Affinity:
Node Affinity: Controls on which nodes the pod can be scheduled based on node labels (similar to nodeSelector, but more flexible).
Pod Affinity: Specifies that the pod should be scheduled on the same node or close to other pods with certain labels.
Usage Scenarios:
Workload Segmentation: Assign specific types of workloads to certain nodes with certain hardware (e.g., GPU nodes).
Data Locality: Schedule pods close to other pods they frequently interact with to reduce network latency.


Example: Prefer to schedule a pod on nodes labeled with zone=us-west

```
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: zone
              operator: In
              values:
                - us-west

```

Anti-Affinity
------------------
Purpose: Anti-affinity rules specify that a pod should avoid being scheduled on the same node or close to other pods with certain labels.<br><br>
Types of Anti-Affinity:<br><br>
Pod Anti-Affinity: Ensures that pods are scheduled away from other pods based on labels, promoting distribution across nodes or zones.<br><br>
Usage Scenarios:<br><br>
High Availability: Spread replicas of the same application across multiple nodes or availability zones to improve resilience.<br><br>
Resource Isolation: Prevent certain pods from being scheduled on the same node to avoid resource contention.<br><br>

```
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
            - key: app
              operator: In
              values:
                - nginx
        topologyKey: "kubernetes.io/hostname"

```

Summary of Differences
-------------------------
Affinity: Defines conditions for preferring or requiring that a pod be scheduled on the same node or close to specific nodes/pods.

Anti-Affinity: Defines conditions for preferring or requiring that a pod be scheduled away from specific nodes/pods, promoting distribution and resilience.




1. Check the Current Cluster Version

   eksctl get cluster --name=<your-cluster-name> --region=<your-region>



2. Check Available Kubernetes Versions
    
eksctl utils describe-stacks --region=<your-region> --name=<your-cluster-name>


3. Update eksctl and AWS CLI

Make sure you are using the latest version of eksctl and the AWS CLI to ensure compatibility with the latest features and improvements:

eksctl version

aws --version


Update the EKS Cluster

eksctl upgrade cluster --name=prod-cluster --region=us-west-2 --kubernetes-version=1.25

Upgrade Node Groups (if needed)

eksctl upgrade nodegroup --name=prod-nodegroup --cluster=prod-cluster --region=us-west-2 --kubernetes-version=1.25

eksctl upgrade nodegroup --cluster=<your-cluster-name> --region=<your-region> --kubernetes-version=<desired-version> --all

Validate the Upgrade

kubectl version

kubectl get nodes

Test the Cluster

kubectl get pods --all-namespaces
kubectl get services --all-namespaces

Monitor the Cluster

















