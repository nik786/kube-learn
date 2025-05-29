
# kubectl explain Cheat Sheet for CKA

| Command                                                                                     | Description                                            |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `kubectl explain pod`                                                                       | Base pod object                                        |
| `kubectl explain pod.spec`                                                                  | Pod spec section                                       |
| `kubectl explain pod.spec.containers`                                                       | Container array definition                             |
| `kubectl explain pod.spec.containers.resources`                                             | Resource limits and requests                           |
| `kubectl explain pod.spec.securityContext`                                                  | Pod-level security context                             |
| `kubectl explain pod.spec.containers.securityContext`                                       | Container-level security context                       |
| `kubectl explain pod.spec.containers.securityContext.capabilities`                          | Linux capabilities section                             |
| `kubectl explain pod.spec.containers.securityContext.capabilities.add`                      | Capabilities to add                                    |
| `kubectl explain pod.spec.containers.securityContext.privileged`                            | Run container in privileged mode                       |
| `kubectl explain pod.spec.containers.securityContext.readOnlyRootFilesystem`                | Mount root FS as read-only                             |
| `kubectl explain pod.spec.containers.securityContext.allowPrivilegeEscalation`              | Prevent privilege escalation                           |
| `kubectl explain pod.spec.containers.securityContext.runAsUser`                             | Run container with specific UID                        |


