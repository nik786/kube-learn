# What happens when we run `kubectl delete pod` command? 🤔

| **Step** | **Action** |
|----------|------------|
| 1 | The pod record in etcd is updated by the API Server with two fields: `deletionTimestamp` and `deletionGracePeriodSeconds`. |
| 2 | The Endpoint Controller checks whether the pod has reached the 'terminating' state. |
| 3 | Once the state is reached, it removes the pod's endpoint from associated services to prevent external traffic. |
| 4 | The endpoint starts getting removed from: <br> - Kube-Proxy <br> - IPTables <br> - Ingress <br> - CoreDNS <br> - Any other objects that hold endpoint information |
| 5 | Kubelet is notified that the pod is being updated (Terminating). |
| 6 | If a `preStop` hook exists, it is executed; otherwise, Kubelet sends a SIGTERM signal to the main container. |
| 7 | The container waits for a graceful shutdown period, which is defined by `terminationGracePeriodSeconds` (default is 30 seconds). |
| 8 | After the shutdown period, the container is forcibly stopped. |
| 9 | Finally, the pod is completely removed from etcd by the API Server. |

---

# Kubelet, Container Runtime, and CNI Plugins - How they are stitched together 🤔 ☸

| **Step** | **Action** |
|----------|------------|
| 1 | Kubelet calls the CRI plugin via the CRI runtime service API to create a pod. |
| 2 | The CRI plugin uses containerd to create and start a pause container (the sandbox container) inside the pod’s cgroups and namespace. |
| 3 | CRI configures the pod's network namespace using CNI. |
| 4 | Kubelet calls CRI's image service API to pull the application container image. |
| 5 | If the image is not present, CRI uses containerd to pull it. |
| 6 | Kubelet calls the CRI plugin again to create and start the application container inside the pod using the pulled image. |
| 7 | CRI uses containerd to create the application container, places it inside the pod’s cgroups and namespace, and starts the container. |
| 8 | The pod and its corresponding application container are now created and running. |

---

# What should I do if a pod fails to pull the image? 🤔

| **Error Message** | **Probable Cause** | **Validation Steps** |
|-------------------|--------------------|----------------------|
| Failed to pull image "xxx": `rpc error: code = Unknown desc = Error response from daemon: Get xxx: denied: You may not login yet` | You have not logged in to the image repository. | Check if `ImagePullSecret` is specified when creating a workload. |
| Failed to pull image "nginx:v1.1": `rpc error: code = Unknown desc = Error response from daemon: Get https://lnkd.in/gKbUxgPb: dial tcp: lookup registry-1.docker.io: no such host` | The image address is incorrectly configured. | Validate whether the image address is correct and if the Secret is used correctly when using third-party images. |
| Failed to pull image "https://lnkd.in/gUGY4AWu": `rpc error: code = Unknown desc = Error response from daemon: Get https://lnkd.in/gKbUxgPb: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)` | Failed to connect to the image repository due to a disconnected network. | Check network policies/firewall and connectivity to the image repository. |
| Failed to create pod sandbox: `rpc error: code = Unknown desc = failed to create a sandbox for pod "nginx-6dc48bf8b6-l8xrw": Error response from daemon: mkdir xxxxx: no space left on device` | Disk space is insufficient. | Validate whether there is sufficient disk space on worker nodes. |
| Failed to pull image "xxx": `rpc error: code = Unknown desc = error pulling image configuration: xxx x509: certificate signed by unknown authority` | An unknown or insecure certificate is used by the image repository. | Verify if the remote image repository uses an unknown or insecure certificate. |
| Failed to pull image "xxx": `rpc error: code = Unknown desc = error pulling image configuration: xxx x509: certificate signed by unknown authority` | Image size is too large. | Check if the image size is too large. |

---

# What happens when we execute `kubectl exec`? 🤔 ❓

| **Step** | **Action** |
|----------|------------|
| 1 | When `kubectl exec` is executed on a pod, the request is first handed over to the Kubernetes API Server. |
| 2 | The API Server calls the Kubelet Exec API. |
| 3 | The Kubelet calls the CRI's Exec interface, which does not directly invoke any container runtime but returns a URL to the Kubelet. |
| 4 | The Kubelet sends this URL to the API Server as a redirection. |
| 5 | The API Server then initiates a real '/exec' request to the Streaming Server via the redirection, establishing a long connection. |
