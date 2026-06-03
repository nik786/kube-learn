
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
| **12. Verify Node Status**          | `kubectl get nodes`     
