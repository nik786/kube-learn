
EKS Managed Node Group (with eksctl or Console)
------------------------------------------------


# EKS Cluster Upgrade (Control Plane + Managed Node Groups)

Upgrade your EKS cluster (`ag-eks-cluster`) using `eksctl` with minimal or zero downtime. This includes upgrading the control plane, core add-ons, and the managed node group.

---

### Upgrade Process by EKSCTL Command with eks managed nodes

# EKS Cluster Upgrade using eksctl (Zero Downtime Approach)

| Step                                  | Command / Action                                                                                                   | Comment                                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **1. Upgrade Control Plane**          | `eksctl upgrade cluster --name ag-eks-cluster --region ap-south-1 --version 1.31 --approve`                       | Updates the Kubernetes control plane version.                                                    |
| **2. Upgrade CoreDNS Add-on**         | `eksctl utils update-coredns --cluster ag-eks-cluster --region ap-south-1 --approve`                              | Updates the CoreDNS add-on to be compatible with the new control plane version.                 |
| **3. Upgrade kube-proxy Add-on**      | `eksctl utils update-kube-proxy --cluster ag-eks-cluster --region ap-south-1 --approve`                           | Updates the kube-proxy add-on to match the control plane version.                               |
| **4. Create New Node Group**          | `eksctl create nodegroup --cluster ag-eks-cluster --name ag-eks-node-group-v131 --region ap-south-1 --version 1.31`| Creates a new node group using the upgraded AMI and Kubernetes version.                         |
| **5. New Node Group Joins Cluster**   | *(No manual step required)*                                                                                       | New node group auto-joins the cluster and becomes ready to run pods.                            |
| **6. Workloads Shift Automatically**  | *(No command needed if using Deployment/ReplicaSet)*                                                              | Kubernetes automatically schedules new pods on available (new) nodes as old nodes are drained.  |
| **7. Drain Old Nodes**                | `kubectl taint nodes <old-node-name> key=value:NoSchedule`<br>`kubectl drain <old-node-name> --ignore-daemonsets --delete-local-data` | Prevents new pods on old nodes and safely moves running pods to new nodes.                     |
| **8. Connect to EKS from CLI**        | `eksctl update kubeconfig --name ag-eks-cluster --region ap-south-1`                                               | Updates your kubeconfig to point to the upgraded EKS cluster.                                   |
| **9. Delete Old Node Group**          | `eksctl delete nodegroup --cluster ag-eks-cluster --name ag-eks-node-group --region ap-south-1`                   | Deletes the old node group after verifying all workloads are running fine on new nodes.         |
| **10. Verify Control Plane Version**  | `kubectl version --short`                                                                                          | Confirms that the control plane is upgraded successfully.                                       |
| **11. Verify Node Versions**          | `kubectl get nodes`                                                                                                | Lists current nodes to ensure only the upgraded ones are present.                               |
| **12. Check Pod Status**              | `kubectl get pods --all-namespaces`                                                                                | Verifies that all pods are running fine after the migration.                                   |
| **13. Monitor Cluster Health**        | Use tools like AWS CloudWatch, Prometheus, or Kubernetes Dashboard                                                 | Monitor cluster performance and logs after upgrade completion.                                  |


## **Best Practices**
- **Upgrade control plane first**, then add-ons, then worker nodes.
- Upgrade **one node group at a time** to avoid downtime.
- Always **use the latest AWS-recommended AMI** for Kubernetes compatibility.
- **Monitor logs in CloudWatch** during the upgrade.

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
