
You are an engineer who owns SAS platform where all services run on K8s . How would  you manage below tasks . (Use programming language of your choice to create a tool )


1. You have 20 physical nodes and totally running 100 pods (~5 POD per  Ec2 machine/ VM) and would like to test connectivity and make sure all pods are healthy and running as expected. (Assuming there are no 3rd party tools/monitoring framework)
2. You want to detect  pods which are under heavy load and underperforming
3. You want to manage/update a subset of pods and update some configs.
4. You want to automate 2 heavy services running on pods that never run on the same nodes. 


| Task                                                                                   | Solution                                                                                   |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Test connectivity and ensure all pods are healthy and running**                      | Use Python with `kubectl` commands or Kubernetes Python client (`kubernetes` library).     |
|                                                                                        | - List all pods across namespaces.                                                        |
|                                                                                        | - Perform a health check using pod status.                                                |
|                                                                                        | - Use `ping` or HTTP checks to verify connectivity between pods.                          |
|                                                                                        | - Example:                                                                                 |
|                                                                                        | ```python                                                                                 |
|                                                                                        | from kubernetes import client, config                                                    |
|                                                                                        | config.load_kube_config()                                                                |
|                                                                                        | v1 = client.CoreV1Api()                                                                  |
|                                                                                        | pods = v1.list_pod_for_all_namespaces(watch=False)                                        |
|                                                                                        | for pod in pods.items:                                                                   |
|                                                                                        |     print(f"{pod.metadata.name} - {pod.status.phase}")                                    |
|                                                                                        | ```                                                                                      |
| **Detect pods under heavy load and underperforming**                                   | Use Python to query metrics from Kubernetes Metrics Server or by inspecting pod resource usage. |
|                                                                                        | - Example:                                                                               |
|                                                                                        | ```python                                                                                |
|                                                                                        | from kubernetes import client, config                                                   |
|                                                                                        | config.load_kube_config()                                                               |
|                                                                                        | custom = client.CustomObjectsApi()                                                      |
|                                                                                        | metrics = custom.list_namespaced_custom_object(                                         |
|                                                                                        |     group="metrics.k8s.io", version="v1beta1", namespace="default",                     |
|                                                                                        |     plural="pods")                                                                      |
|                                                                                        | for pod in metrics['items']:                                                            |
|                                                                                        |     usage = pod['containers'][0]['usage']                                               |
|                                                                                        |     print(f"{pod['metadata']['name']} CPU: {usage['cpu']}, Memory: {usage['memory']}")   |
|                                                                                        | ```                                                                                     |
| **Manage/update a subset of pods and update configurations**                          | Use `kubectl patch` or Python client to update specific configurations on targeted pods. |
|                                                                                        | - Example:                                                                               |
|                                                                                        | ```python                                                                                |
|                                                                                        | v1.patch_namespaced_pod(name="pod-name", namespace="default", body={...})               |
|                                                                                        | ```                                                                                     |
| **Automate 2 heavy services to never run on the same nodes**                          | Use Kubernetes pod affinity/anti-affinity rules.                                         |
|                                                                                        | - Define rules in pod YAML or programmatically update via Kubernetes client.             |
|                                                                                        | - Example:                                                                               |
|                                                                                        | ```python                                                                                |
|                                                                                        | affinity = {                                                                            |
|                                                                                        |     "podAntiAffinity": {                                                               |
|                                                                                        |         "requiredDuringSchedulingIgnoredDuringExecution": [                            |
|                                                                                        |             {                                                                          |
|                                                                                        |                 "labelSelector": {                                                    |
|                                                                                        |                     "matchExpressions": [                                             |
|                                                                                        |                         {                                                             |
|                                                                                        |                             "key": "app",                                             |
|                                                                                        |                             "operator": "In",                                         |
|                                                                                        |                             "values": ["heavy-service"]                               |
|                                                                                        |                         }                                                             |
|                                                                                        |                     ]                                                                  |
|                                                                                        |                 },                                                                     |
|                                                                                        |                 "topologyKey": "kubernetes.io/hostname"                                |
|                                                                                        |             }                                                                          |
|                                                                                        |         ]                                                                              |
|                                                                                        |     }                                                                                  |
|                                                                                        | }                                                                                      |
|                                                                                        | v1.patch_namespaced_pod(name="pod-name", namespace="default", body={"spec": {"affinity": affinity}}) |
|                                                                                        | ```                                                                                     |





Test Pod Connectivity and Health – Check if pods are healthy and running as expected.

Detect Heavy Load/Underperforming Pods – Monitor CPU/Memory usage and identify underperforming pods.

Manage/Update Pods and Configurations – Update specific pod configurations and manage a subset of them.

Automate Heavy Services Running on Different Nodes – Ensure that two heavy services always run on different nodes using affinity/anti-affinity rules.


ansible-galaxy collection install community.kubernetes


1. Test Pod Connectivity and Health
---------------------------------

```
---
- name: Check Kubernetes Pods Health
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Gather Kubernetes pod facts
      community.kubernetes.k8s_facts:
        kubeconfig: "/path/to/kubeconfig"  # Specify your kubeconfig path
      register: pod_facts

    - name: Check pod health and status
      debug:
        msg: |
          Pod "{{ item.metadata.name }}" in namespace "{{ item.metadata.namespace }}" is {{ item.status.phase }}
      loop: "{{ pod_facts.resources }}"
      when: item.status.phase != 'Running'



```

2. Detect Pods Under Heavy Load

```


---
- name: Detect Heavy Load on Pods
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Gather pod stats (CPU and Memory usage)
      community.kubernetes.k8s_facts:
        kubeconfig: "/path/to/kubeconfig"
      register: pod_stats

    - name: Check if pods have heavy load
      debug:
        msg: |
          Pod "{{ item.metadata.name }}" in namespace "{{ item.metadata.namespace }}" is under heavy load with CPU: {{ item.spec.containers[0].resources.requests.cpu }} and Memory: {{ item.spec.containers[0].resources.requests.memory }}
      loop: "{{ pod_stats.resources }}"
      when: item.spec.containers[0].resources.requests.cpu is defined and item.spec.containers[0].resources.requests.memory is defined
      # Modify conditions for heavy load (e.g., CPU > 80% or Memory > 80%)


```

3. Update Pods with New Configurations

```


- name: Update Pod Configurations
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Update pod with new environment variable
      community.kubernetes.k8s:
        kubeconfig: "/path/to/kubeconfig"
        namespace: "default"  # Specify namespace
        name: "example-pod"  # Specify pod name
        kind: Pod
        patch:
          spec:
            containers:
              - name: "example-container"  # Specify container name
                env:
                  - name: "NEW_CONFIG"
                    value: "new_value"  # Specify new config value
      register: update_result

    - name: Show update result
      debug:
        msg: "Pod {{ update_result.resources.metadata.name }} updated with new config"

```


   
4. Enforce Pod Anti-Affinity to Run Heavy Services on Different Nodes

```
---
- name: Enforce Anti-Affinity for Heavy Services
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Apply Anti-Affinity for Heavy Services
      community.kubernetes.k8s:
        kubeconfig: "/path/to/kubeconfig"
        namespace: "default"  # Specify namespace
        name: "heavy-service-pod"  # Specify pod name for heavy service
        kind: Pod
        patch:
          spec:
            affinity:
              podAntiAffinity:
                requiredDuringSchedulingIgnoredDuringExecution:
                  - labelSelector:
                      matchExpressions:
                        - key: "app"
                          operator: In
                          values:
                            - "heavy-service"  # Modify with the label of your heavy service
                    topologyKey: "kubernetes.io/hostname"  # Ensures that pods with the same label won't run on the same node

    - name: Confirm Anti-Affinity applied
      debug:
        msg: "Anti-Affinity applied to pod {{ item.metadata.name }}"
      loop: "{{ pod_facts.resources }}"

```

```

ansible-playbook check_pod_health.yml
ansible-playbook detect_heavy_load_pods.yml
ansible-playbook update_pod_config.yml
ansible-playbook apply_anti_affinity.yml

```

















