# Debugging Kubernetes Pod Failures ☸️

## Pod Startup Errors

| **Error**            | **Description**                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------------|
| `ImagePullBackoff`    | Kubernetes can't retrieve the image for one of the containers in the Pod. Common causes:           |
| `ImageInspectError`   | Image inspection failure (invalid image format or missing metadata).                              |
| `ErrImagePull`        | Error pulling the container image (e.g., invalid image name or tag).                              |
| `ErrImageNeverPull`   | Image cannot be pulled from a registry (missing credentials for private registry).               |
| `RegistryUnavailable` | Registry is unavailable (e.g., network issues or unreachable registry).                           |
| `InvalidImageName`    | The specified image name is invalid or malformed.                                                 |

## Pod Runtime Errors

| **Error**               | **Description**                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------|
| `CrashLoopBackOff`       | Container crashes continuously due to an application error or misconfiguration.                |
| `RunContainerError`      | Error when Kubernetes cannot run the container before the application starts.                   |
| `KillContainerError`     | Error when Kubernetes cannot terminate a container gracefully.                                  |
| `VerifyNonRootError`     | Error due to running a container as root when it's not allowed by policy.                       |
| `RunInitContainerError`  | Error when the initialization container cannot be started.                                      |
| `CreatePodSandboxError`  | Error when the pod sandbox cannot be created (could be due to resource constraints).            |
| `ConfigPodSandboxError`  | Configuration error when setting up the pod sandbox.                                             |
| `KillPodSandboxError`    | Error when Kubernetes fails to terminate the pod sandbox.                                        |
| `SetupNetworkError`      | Network setup failure, typically caused by misconfigured network policies.                      |
| `TeardownNetworkError`   | Failure when tearing down the network after the pod's lifecycle ends.                           |

## Common Kubernetes Pod Issues

### ImagePullBackoff

- **Cause:** Kubernetes cannot pull the image for the container.
- **Common Causes:**
  - Invalid image name or non-existent tag.
  - Missing credentials for private registry.
- **Solution:**
  - Verify the image name and tag.
  - Ensure the credentials for the private registry are available in a Secret.

### RunContainerError

- **Cause:** The container fails to start before the application can run.
- **Common Causes:**
  - Mounting non-existent volumes (e.g., ConfigMap, Secret).
  - Mounting a read-only volume as read-write.
- **Solution:** Inspect the `kubectl describe` output for more details on the error.

### CrashLoopBackOff

- **Cause:** Container crashes continuously.
- **Common Causes:**
  - Application error preventing the container from starting.
  - Misconfiguration of the container.
  - Failed Liveness probe.
- **Solution:** Check the application logs for any errors and review the configuration.

### Pods in a Pending State

- **Cause:** Pod stays in a Pending state without being scheduled.
- **Common Causes:**
  - Insufficient resources (CPU, memory) in the cluster.
  - Namespace ResourceQuota exceeded.
  - Pod bound to a Pending PersistentVolumeClaim.
- **Solution:** Use `kubectl describe` to inspect events and resource availability.

## Assigning an IP Address to Pods

| **Step**                | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| `kube-controller-manager` | Assigns a podCIDR to each node in the cluster.                                                             |
| `Pod IP assignment`      | Pods on a node are assigned an IP address from the podCIDR subnet.                                         |
| `CNI Plugin`             | The CNI plugin is responsible for configuring the pod network and assigning the IP address.               |

### Kubernetes Pod IP Assignment Process:

1. **PodCIDR**: Each node in the cluster gets a range of IP addresses (podCIDR).
2. **Pod Scheduling**: When a pod is scheduled on a node, the kubelet calls the CRI plugin to create the pod.
3. **Network Provider Agent**: The agent ensures the pod gets the appropriate IP address from the assigned range.

## Increasing the Default Pod Limit

| **Aspect**               | **Description**                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------|
| `Default Pod Limit`      | The default limit is 110 pods per node in Kubernetes.                                                     |
| `CIDR Block`             | Kubernetes assigns a `/24` CIDR block (256 addresses) per node, accommodating 110 pods.                   |
| `Limit Adjustment`       | You can override this limit by adjusting the `max-pods` parameter in the kubelet configuration.           |

### How to Increase the Default Pod Limit:

1. Add the following to the kubelet configuration:
   ```bash
   $KUBELET_EXTRA_ARGS="--max-pods=240"



## Replacing IPTables with eBPF in kube-proxy

| **Aspect**              | **Description**                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------|
| **IPTables Limitations**   | High latency, poor performance with large clusters, and difficulty debugging.                      |
| **eBPF Advantages**        | Lower CPU overhead, efficient hash tables, better scalability, and improved performance.            |
| **eBPF in Kubernetes**     | Cilium, a CNI provider based on eBPF, replaces kube-proxy for improved networking performance.      |

## Benefits of Using eBPF Over IPTables

| **Benefit**             | **Description**                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------|
| **Efficiency**           | eBPF reduces CPU overhead and scales better.                                                      |
| **Performance**          | Improved load balancing and TCP performance.                                                      |
| **Scalability**          | eBPF enables handling large clusters more efficiently.                                             |

## Simplifying Database Migration on Kubernetes

| **Method**                   | **Description**                                                                                          | **Pros**                                                     | **Cons**                                                   |
|------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------|
| **Init Containers**           | Use init containers to perform database migrations before the app containers are deployed.               | Isolated process, simplified manifests.                     | Limited flexibility, increased resource consumption.       |
| **Continuous Deployment Pipelines** | Integrate migration scripts into the CI/CD pipeline.                                                      | Automated, version-controlled.                              | Complexity, tight coupling, exposed database credentials.  |
| **Separate Helm Chart**       | Use Helm to package and deploy a Kubernetes job that runs the migration script.                          | Reusable, scalable migration.                               | Requires separate Helm chart for database migration.       |

   
