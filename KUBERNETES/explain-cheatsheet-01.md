
# kubectl explain Cheat Sheet for CKA

## Pod

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



## NP

| Command                                                                                     | Description                                            |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `kubectl explain networkpolicy`                                                             | Base network policy object                             |
| `kubectl explain networkpolicy.spec`                                                        | Spec section                                           |
| `kubectl explain networkpolicy.spec.podSelector`                                            | Select pods to apply policy                            |
| `kubectl explain networkpolicy.spec.policyTypes`                                            | Define ingress/egress                                  |
| `kubectl explain networkpolicy.spec.ingress`                                                | Ingress rules                                          |
| `kubectl explain networkpolicy.spec.ingress.from`                                           | Ingress sources                                        |
| `kubectl explain networkpolicy.spec.ingress.from.podSelector`                               | Pod selector as source                                 |
| `kubectl explain networkpolicy.spec.egress`                                                 | Egress rules                                           |

```

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: internal-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      name: internal
  policyTypes:
  - Egress
  - Ingress
  ingress:
    - {}
  egress:
  - to:
    - podSelector:
        matchLabels:
          name: mysql
    ports:
    - protocol: TCP
      port: 3306

  - to:
    - podSelector:
        matchLabels:
          name: payroll
    ports:
    - protocol: TCP
      port: 8080

  - ports:
    - port: 53
      protocol: UDP
    - port: 53
      protocol: TCP

```


## INGRESS

| Command                                                                                     | Description                                            |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `kubectl explain ingress`                                                                   | Base ingress object                                    |
| `kubectl explain ingress.spec`                                                              | Ingress spec section                                   |
| `kubectl explain ingress.spec.rules`                                                        | List of host rules                                     |
| `kubectl explain ingress.spec.rules.http`                                                   | HTTP rule section                                      |
| `kubectl explain ingress.spec.rules.http.paths`                                             | URL path rules                                         |
| `kubectl explain ingress.spec.rules.http.paths.backend.service`                             | Backend service (v1.19+)                               |
| `kubectl explain ingress.spec.rules.http.paths.backend`                                     | Backend (older versions)                               |

## PV

| Command                                                                                     | Description                                            |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `kubectl explain pv`                                                                        | Base persistent volume object                          |
| `kubectl explain pv.spec`                                                                   | PV spec section                                        |
| `kubectl explain pv.spec.capacity`                                                          | Define storage capacity                                |
| `kubectl explain pv.spec.accessModes`                                                       | ReadWriteOnce, ReadOnlyMany, etc.                      |
| `kubectl explain pv.spec.persistentVolumeReclaimPolicy`                                     | Reclaim policy (Retain, Delete, etc.)                  |
| `kubectl explain pv.spec.storageClassName`                                                  | Storage class binding                                  |
| `kubectl explain pv.spec.hostPath`                                                          | Volume source type (or use nfs/awsElasticBlockStore)   |


## 📦 Deployment: `kubectl explain` Commands

| Command                                                                                     | Description                                                                 |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `kubectl explain deployment.spec.template.spec.imagePullSecrets`                            | Explains the `imagePullSecrets` field used to define private registry secrets. |
| `kubectl explain deployment.spec.template.spec.imagePullSecrets --recursive`                | Shows the detailed structure (fields) of each item in `imagePullSecrets`.   |
| `kubectl explain deployment.spec.template.spec`                                              | Explains all fields inside the Pod spec section of the Deployment.          |
