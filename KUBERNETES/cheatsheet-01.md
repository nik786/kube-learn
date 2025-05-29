
# kubectl explain Cheat Sheet for CKA

| Resource         | Command                                                                                     | Description                                           |
|------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Pod**          | `kubectl explain pod`                                                                       | Base pod object                                       |
|                  | `kubectl explain pod.spec`                                                                  | Pod spec section                                      |
|                  | `kubectl explain pod.spec.containers`                                                       | Container array definition                            |
|                  | `kubectl explain pod.spec.containers.resources`                                             | Resource limits and requests                          |
|                  | `kubectl explain pod.spec.securityContext`                                                  | Pod-level security context                            |
|                  | `kubectl explain pod.spec.containers.securityContext`                                       | Container-level security context                      |
|                  | `kubectl explain pod.spec.containers.securityContext.capabilities`                          | Linux capabilities section                            |
|                  | `kubectl explain pod.spec.containers.securityContext.capabilities.add`                      | Capabilities to add                                   |
|                  | `kubectl explain pod.spec.containers.securityContext.privileged`                            | Run container in privileged mode                      |
|                  | `kubectl explain pod.spec.containers.securityContext.readOnlyRootFilesystem`                | Mount root FS as read-only                            |
|                  | `kubectl explain pod.spec.containers.securityContext.allowPrivilegeEscalation`              | Prevent privilege escalation                          |
|                  | `kubectl explain pod.spec.containers.securityContext.runAsUser`                             | Run container with specific UID                       |

| **NetworkPolicy**| `kubectl explain networkpolicy`                                                             | Base network policy object                            |
|                  | `kubectl explain networkpolicy.spec`                                                        | Spec section                                          |
|                  | `kubectl explain networkpolicy.spec.podSelector`                                            | Select pods to apply policy                           |
|                  | `kubectl explain networkpolicy.spec.policyTypes`                                            | Define ingress/egress                                 |
|                  | `kubectl explain networkpolicy.spec.ingress`                                                | Ingress rules                                         |
|                  | `kubectl explain networkpolicy.spec.ingress.from`                                           | Ingress sources                                       |
|                  | `kubectl explain networkpolicy.spec.ingress.from.podSelector`                               | Pod selector as source                                |
|                  | `kubectl explain networkpolicy.spec.egress`                                                 | Egress rules                                          |

| **Ingress**      | `kubectl explain ingress`                                                                   | Base ingress object                                   |
|                  | `kubectl explain ingress.spec`                                                              | Ingress spec section                                  |
|                  | `kubectl explain ingress.spec.rules`                                                        | List of host rules                                    |
|                  | `kubectl explain ingress.spec.rules.http`                                                   | HTTP rule section                                     |
|                  | `kubectl explain ingress.spec.rules.http.paths`                                             | URL path rules                                        |
|                  | `kubectl explain ingress.spec.rules.http.paths.backend.service`                             | Backend service (v1.19+)                              |
|                  | `kubectl explain ingress.spec.rules.http.paths.backend`                                     | Backend (older versions)                              |

| **PersistentVolume** | `kubectl explain pv`                                                                    | Base persistent volume object                         |
|                      | `kubectl explain pv.spec`                                                               | PV spec section                                       |
|                      | `kubectl explain pv.spec.capacity`                                                      | Define storage capacity                               |
|                      | `kubectl explain pv.spec.accessModes`                                                   | ReadWriteOnce, ReadOnlyMany, etc.                     |
|                      | `kubectl explain pv.spec.persistentVolumeReclaimPolicy`                                 | Reclaim policy (Retain, Delete, etc.)                 |
|                      | `kubectl explain pv.spec.storageClassName`                                              | Storage class binding                                 |
|                      | `kubectl explain pv.spec.hostPath`                                                      | Volume source type (or use nfs/awsElasticBlockStore)  |

