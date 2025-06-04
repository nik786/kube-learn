

## Application Error


| #  | Error Description                                      | Possible Cause                                                                 | Suggested Solution                                                                 |
|----|--------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 1  | `CrashLoopBackOff`                                     | Application is crashing repeatedly on startup                                   | Check container logs for exceptions; validate configuration and dependencies       |
| 2  | `ImagePullBackOff` / `ErrImagePull`                    | Kubernetes cannot pull the container image                                      | Verify image name, tag, and repository access credentials                           |
| 3  | `Readiness/Liveness probe failed`                      | Health checks are misconfigured or app is not ready                             | Adjust probe configuration and increase initial delay if needed                    |
| 4  | `OutOfMemoryError: Java heap space`                    | Java application is using more memory than allocated                            | Tune JVM memory settings (`-Xmx`, `-Xms`) and resource requests/limits in manifest |
| 5  | `Connection refused` when accessing services           | Services or endpoints are misconfigured                                         | Verify service definitions, ports, and DNS resolution                              |
| 6  | `Request timeout` or `504 Gateway Timeout`             | Application is taking too long to respond                                       | Check application performance and increase timeout values in ingress/load balancer |
| 7  | Secrets not mounted                                     | Kubernetes secrets are not available in the container                           | Check `volumeMounts` and `volumes` configuration                                   |
| 8  | `java.net.UnknownHostException`                        | Application cannot resolve hostnames                                            | Verify DNS configuration and service names                                         |
| 9  | `403 Forbidden` from AWS services (e.g., S3, RDS)      | Missing or misconfigured IAM permissions                                        | Attach correct IAM roles using IRSA (IAM Roles for Service Accounts)               |
| 10 | `Database connection failed` / `SQLException`          | Incorrect database configuration or networking issues                           | Verify DB endpoint, credentials, and security group/firewall settings              |


## EKS Infra Error


| #  | Error Description                                      | Possible Cause                                                                 | Suggested Solution                                                                 |
|----|--------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 1  | `Nodes not joining the cluster`                        | Incorrect IAM roles or missing bootstrap configuration                         | Verify worker node IAM role and node group setup                                   |
| 2  | `Insufficient CPU/Memory` errors during pod scheduling | Cluster resources exhausted                                                     | Scale node group or optimize resource requests/limits                              |
| 3  | `Pod stuck in Pending state`                           | No available nodes meet the scheduling requirements                             | Check taints, tolerations, and resource requirements                               |
| 4  | `Unauthorized` or `AccessDenied` from AWS APIs         | Misconfigured IAM roles or lack of IRSA                                         | Ensure correct IAM role bindings and policies are in place                         |
| 5  | `Service load balancer not provisioning`               | Incorrect service annotations or missing permissions                           | Use correct service type (LoadBalancer) and verify controller permissions          |
| 6  | `PersistentVolumeClaims stuck in Pending`              | Storage class misconfiguration or unavailable volume                           | Check StorageClass and ensure backing volume type is available                     |
| 7  | `Cluster autoscaler not scaling`                       | Missing IAM permissions or incorrect annotations                               | Confirm autoscaler IAM policy and deployment annotations                           |
| 8  | `DNS resolution issues inside pods`                    | CoreDNS misconfigured or crashing                                               | Check CoreDNS logs, deployment status, and ConfigMap                               |
| 9  | `NetworkPolicy blocking traffic`                       | Misconfigured NetworkPolicy rules                                               | Review and adjust network policies to allow intended traffic                       |
| 10 | `Security group rules blocking access`                 | Inbound/outbound rules not allowing required traffic                           | Update EKS node security group and VPC/subnet settings                             |

## HPA Issue

| #  | Probable Cause                                        | Suggested Solution                                                                 |
|----|--------------------------------------------------------|-------------------------------------------------------------------------------------|
| 1  | Metrics Server not deployed or not working             | Ensure `metrics-server` is installed and healthy; check logs and API availability  |
| 2  | Resource requests/limits not defined on pods           | Define `resources.requests.cpu` and/or `memory` in pod spec to allow metric tracking |
| 3  | Incorrect HPA target metrics configuration             | Verify `targetCPUUtilizationPercentage` or custom metric definitions                |
| 4  | Application load is bursty or short-lived              | Use `--horizontal-pod-autoscaler-downscale-delay` and `--horizontal-pod-autoscaler-upscale-delay` flags to tune HPA responsiveness |
| 5  | Max replicas already reached                           | Check HPA definition for `maxReplicas` value and increase if needed                |
| 6  | Cluster lacks available resources for scaling          | Ensure enough CPU/memory is available; consider adding more nodes or scaling up    |
