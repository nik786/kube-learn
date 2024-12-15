
##Kubernetes
-----------------
It allows us to run containers across multiple compute nodes (these can be VMs or a bare-metal servers). <br><br>
Once Kubernetes takes control over a cluster of nodes, containers can then spun up or torn down depending upon our need at any given time.


##Kube-Apiserver
-----------------

| **Feature**                                         | **Description**                                                                                                                                             |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Main Management Point**                          | The kube-apiserver serves as the main management point of the entire Kubernetes cluster.                                                                    |
| **Workload and Organizational Unit Configuration** | It allows users to configure Kubernetes' workloads and organizational units.                                                                                |
| **Bridge Between Components**                      | Acts as the bridge between various components to maintain cluster health.                                                                                   |
| **RESTful Interface**                              | The API server implements a RESTful interface, enabling many different tools and libraries to communicate with it.                                          |
| **Etcd Integration**                               | Responsible for ensuring that the etcd store contains service details of deployed containers.                                                               |


##Kube-Controller
-------------------

| **Feature**                                         | **Description**                                                                                                                 |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Manages Controllers**                            | Manages different controllers that regulate the state of the cluster.                                                         |
| **Workload Life Cycle Management**                 | Handles workload life cycles and performs routine tasks.                                                                      |
| **Replication Controller**                         | Ensures that the number of replicas defined for a pod matches the number currently deployed on the cluster.                   |
| **Desired State Fulfillment**                      | Detects changes, reads new information, and implements procedures to fulfill the desired state of the cluster.                |


##Kube-Scheduler
------------------

| **Feature**                                         | **Description**                                                                                                                 |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Workload Assignment**                            | Assigns workloads to specific nodes in the cluster.                                                                            |
| **Infrastructure Analysis**                        | Analyzes the current infrastructure environment and places workloads on acceptable node(s).                                    |
| **Capacity Tracking**                              | Tracks available capacity on each host to ensure workloads are not scheduled on nodes without sufficient capacity.             |

##Kubelet
---------------

| **Feature**                                         | **Description**                                                                                                                 |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Main Contact Point**                              | Serves as the main contact point for each node within the cluster group.                                                       |
| **Relay Information**                               | Responsible for relaying information to and from the control plane services.                                                   |
| **Etcd Interaction**                               | Interacts with the etcd store to read configuration details or write new values.                                               |
| **Cluster Authentication**                         | Communicates with the master components to authenticate to the cluster.                                                       |
| **Container Runtime Control**                      | Controls the container runtime to launch or destroy containers as needed.                                                     |
| **Workload Manifest**                              | Receives work in the form of a manifest, which defines the workload and the operating parameters.                              |

##Kube-Proxy
--------------

| **Feature**                                         | **Description**                                                                                                                 |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Host Subnet Management**                         | Manages individual host subnetting and ensures services are available to other components.                                     |
| **Request Forwarding**                             | Forwards requests to the correct containers.                                                                                   |
| **Load Balancing**                                 | Performs primitive load balancing and ensures the networking environment is predictable and accessible.                        |



## ConfigMaps and Secrets in Kubernetes

| **Feature**                          | **ConfigMaps**                                                                                      | **Secrets**                                                                                                    |
|--------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Purpose**                          | Designed to store configuration data as key-value pairs that are not sensitive.                    | Used for storing sensitive data like passwords, keys, and tokens.                                            |
| **Sensitivity**                      | For non-sensitive information.                                                                     | Specifically for sensitive information.                                                                       |
| **Examples**                         | Environment settings, configuration files, or command-line arguments.                              | Passwords, API keys, TLS certificates.                                                                       |
| **Storage Location**                 | Stored in the etcd database.                                                                       | Stored in the etcd database and kept in `tmpfs` on the nodes.                                                |
| **Updates**                          | Updates to ConfigMaps are reflected in mounted volumes without restarting pods.                    | Pods do not automatically update when Secrets are modified; explicit updates (e.g., rolling updates) are needed. |
| **Usage**                            | - Environment variables<br>- Command-line arguments<br>- Configuration files in a volume          | - As environment variables<br>- As a volume for sensitive file-based configurations.                         |
| **Automatic Creation by Kubernetes** | Not created automatically; must be defined by the user.                                            | Kubernetes creates some Secrets automatically, such as for API access from pods.                             |
| **Transmission**                     | Transmitted to and from the API server in plain text.                                              | Transmitted in plain text to and from the API server.                                                        |
| **Security Concerns**                | Less concern for security as it handles non-sensitive data.                                        | Requires careful handling since it deals with sensitive data.                                                |
| **Dynamic Updates**                  | Updates without restarting the pods in most cases.                                                 | Requires manual updates to pods to apply changes.                                                            |



## Comparison of ABAC and RBAC in Kubernetes

| **Feature**                          | **ABAC (Attribute-Based Access Control)**                                                                                   | **RBAC (Role-Based Access Control)**                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Definition**                       | Access control based on attributes associated with the request, such as user, resource, or action.                         | Access control based on roles assigned to users or groups.                                                  |
| **Configuration Method**             | Requires SSH and root filesystem access to the master VM to modify authorization policies.                                  | Configured using `kubectl` or the Kubernetes API directly.                                                   |
| **Policy Management**                | Changes to authorization policies require manual edits to configuration files on the master node.                          | Policies are managed through Kubernetes resources like `Role`, `ClusterRole`, `RoleBinding`, and `ClusterRoleBinding`. |
| **Cluster API Server Restart**       | The API server must be restarted for policy changes to take effect.                                                        | No need to restart the API server; changes are applied dynamically.                                          |
| **Delegation**                       | Cannot delegate access control management without providing SSH access to the cluster master.                              | Supports delegation of resource management by authorizing users to modify RBAC policies via RBAC itself.    |
| **Ease of Use**                      | Complex to manage, especially in dynamic environments.                                                                     | Simplified and flexible, with native support for Kubernetes resources.                                       |
| **Granularity**                      | Can be fine-grained but is harder to manage due to static file-based configurations.                                        | Granular and easier to manage using roles and bindings.                                                      |
| **Scalability**                      | Less scalable due to manual updates and dependency on master node access.                                                  | Highly scalable with dynamic configuration through the Kubernetes API.                                       |
| **Security Risks**                   | Higher risk due to direct access to the master VM and file-based policy changes.                                            | Reduced risk as no direct SSH access to the master node is required.                                         |
| **Flexibility**                      | Provides flexibility with custom attributes but is less integrated with Kubernetes tooling.                                 | Seamlessly integrated with Kubernetes and widely adopted for Kubernetes access control.                      |


Volumes and Persistent Volumes
-----------------------------------
## Persistent Volumes in Kubernetes

| **Feature**                   | **Description**                                                                                                                               |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**                | Persistent Volumes (PVs) abstract storage resources that are independent of a pod's lifecycle.                                               |
| **Purpose**                   | Provides robust, long-lasting storage for applications, unaffected by pod creation, deletion, or restarts.                                   |
| **Storage Configuration**     | Administrators configure storage resources for the cluster that can be requested and claimed by users.                                       |
| **Binding**                   | Users bind Persistent Volume Claims (PVCs) to PVs to access the storage in their pods.                                                      |
| **Decoupling from Pods**      | Storage exists independently of the pods that use it, ensuring data persistence beyond pod lifecycles.                                       |
| **Reclamation Policy**        | Determines the behavior after a pod is finished with a PV:                                                                                    |
|                               | - **Retain**: Keeps the volume until manually deleted by an administrator.                                                                   |
|                               | - **Delete**: Removes the volume and its data immediately when the pod is done using it.                                                     |
| **Flexibility**               | Supports multiple storage backends like NFS, iSCSI, cloud storage (e.g., AWS EBS, GCE Persistent Disks), and more.                          |
| **Accessibility**             | Can be accessed by one or more pods depending on the access mode (ReadWriteOnce, ReadOnlyMany, ReadWriteMany).                              |
| **Use Cases**                 | Ideal for stateful applications like databases, file systems, and other workloads requiring persistent storage.                              |
| **Administrator's Role**      | Responsible for provisioning and managing PVs, as well as configuring the appropriate reclamation policies.                                  |
| **User's Role**               | Creates Persistent Volume Claims (PVCs) to request storage resources configured as PVs.                                                     |




# PVC Type
------------

| PVC Type                    | Description                                                                                  | Use Case                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| **ReadWriteOnce (RWO)**      | A volume that can be mounted by a single node for read/write access.                          | Suitable for applications that require access from only one node at a time. |
| **ReadOnlyMany (ROX)**       | A volume that can be mounted by many nodes in read-only mode.                                 | Used for shared access to data where no write operations are needed. |
| **ReadWriteMany (RWX)**      | A volume that can be mounted by many nodes for read/write access.                             | Used for applications that need shared read/write access across multiple nodes. |
| **Block Storage**            | Persistent storage with block-level access (e.g., AWS EBS, GCE Persistent Disks).            | Suitable for databases or applications requiring block storage. |
| **File Storage**             | Persistent storage with file-level access (e.g., NFS, Amazon EFS).                          | Ideal for applications that require shared file storage among multiple nodes. |
| **Ephemeral Storage (EmptyDir)** | Temporary storage that is created and destroyed along with the pod.                            | Used for temporary storage, such as cache, during pod runtime.       |

# PV Reclam Policies
-----------------------

| Reclaim Policy  | Description                                                                                  | Use Case                                                        |
|-----------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| **Retain**      | Keeps the volume and its data even after the Persistent Volume Claim (PVC) is deleted.       | Use when you want to manually manage data after PVC deletion.   |
| **Recycle**     | The volume is scrubbed (e.g., deleted files) and made available for reuse after PVC deletion. | Deprecated in Kubernetes 1.14+. Previously used for simple cleanup of data. |
| **Delete**      | Deletes the volume (e.g., from cloud storage like AWS EBS, GCE Persistent Disk) when the PVC is deleted. | Use when you want the volume to be automatically deleted along with the PVC. |


| Storage Class | Description                                                                                             | Use Case                                                       | Provisioner          |
|---------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|----------------------|
| **General**   | Default storage class, typically backed by cloud provider’s default storage (e.g., AWS EBS, GCE Persistent Disk). | General-purpose storage with flexible provisioning and scaling. | cloud-provider-specific (e.g., `kubernetes.io/aws-ebs`) |
| **Local**     | Persistent storage backed by local disks on the nodes.                                                | Ideal for applications that require high-performance local storage. | `kubernetes.io/local-volume` |
| **NFS**       | A storage class that uses Network File System (NFS) for persistent storage.                             | Suitable for shared file storage across multiple pods.         | `kubernetes.io/nfs`    |
| **EBS**       | Persistent block storage from AWS Elastic Block Store (EBS), which is typically used for high-performance workloads. | Use when you need high-performance, persistent block storage.    | `kubernetes.io/aws-ebs`|
| **EFS**       | AWS Elastic File System (EFS) provides scalable, distributed file storage for Linux-based workloads.   | Best for applications requiring scalable, shared file storage across multiple instances. | `kubernetes.io/aws-efs` |


emptyDir
----------
1. It is a type of volume which is created when a Pod is first assigned to a Node.
2. It remains active as long as the Pod is running on that node.
3. The volume is initially empty and the containers in the pod can read and write the files in the emptyDir volume.
4. Once the Pod is removed from the node, the data in the emptyDir is erased.


# Create a Persistent Volume with the given specification: -


```
Volume name: pv-analytics

Storage: 100Mi

Access mode: ReadWriteMany

Host path: /pv/data-analytics


Is the volume name set?

Is the storage capacity set?

Is the accessMode set?

Is the hostPath set?

```


```

apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-analytics
spec:
  capacity:
    storage: 100Mi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /pv/data-analytics


```


Service
---------

1. Service is an abstract way to expose a set of pods (one or more) as a network service
2. It provides a consistent and stable endpoint (usually an IP address and port) to access the pods
3. Abstraction Layer: Services act as an abstraction layer that allows you to refer to a group of pods collectively by a single, stable DNS name or IP address
4. Selectors: Services use label selectors to determine which pods should be part of the service.


| **Service Type**          | **Description**                                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **ClusterIP**             | Services are reachable by pods/services within the cluster. A predictable static DNS address is created for the service in the default namespace. |
| **NodePort**              | Services are reachable by clients on the same LAN or clients who can ping the Kubernetes host nodes. For security, Kubernetes host nodes should be on a private subnet. |
| **LoadBalancer**          | Services are reachable by everyone connected to the internet. Typically, the L4 load balancer is publicly accessible, while Kubernetes host nodes remain on a private subnet. |
| **Headless Service**      | Services without a cluster IP. Used for direct pod-to-pod communication with a custom DNS configuration.                                      |


Daemon Sets
--------------
1. Specialized form of pod controller which run a copy of a pod on each node in the cluster
2. Collecting and forwarding logs, aggregating metrics, and running services that increase the capabilities of the node itself are popular candidates for daemon sets


Statefulset
-------------

| **Feature**                     | **Description**                                                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Stateful Workloads**          | Designed for managing stateful applications that require stable and unique network identifiers, persistent storage, and ordered deployment and scaling. |
| **Stable Network Identity**     | Maintains a stable network identity (hostname) for each pod, enabling consistent communication between stateful application components. |
| **Persistent Storage**          | Provides support for persistent storage volumes, ensuring data is retained across pod restarts or rescheduling.                    |
| **Ordered Deployment and Scaling** | Deploys and scales pods in a specific order, ensuring each pod is fully initialized and ready before the next one is created.          |



Deployment
------------

| **Feature**                     | **Description**                                                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Stateless Workloads**         | Designed for managing stateless applications that can scale horizontally and do not require stable network identities or persistent storage. |
| **Horizontal Scaling**          | Enables automatic scaling of application pods based on resource utilization or user-defined metrics to handle increased traffic and demand. |
| **Rolling Updates**             | Supports rolling updates to update applications gradually without causing downtime or service disruption.                         |
| **Pod Template Specification**  | Defines a pod template specification to specify the desired state of application pods, including container images, resource requirements, and environment variables. |


Stateless Applications
-----------------------

| **Feature**                     | **Description**                                                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Session Overhead Removal**    | Removes the overhead of creating or using sessions.                                                                                 |
| **Horizontal Scaling**          | Facilitates horizontal scaling by adding or removing application instances on demand.                                               |
| **Application Consistency**     | Ensures consistency across various application instances.                                                                           |
| **Reduced Memory Usage**        | Minimizes memory usage on the server-side.                                                                                          |
| **Eliminates Session Expiry**   | Avoids issues related to session expiry.                                                                                            |
| **Deployment Support**          | Stateless applications can be deployed efficiently using Deployments.                                                               |


Statefulsets
--------------

| **Feature**                         | **Description**                                                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **State Preservation**              | Used when you need to preserve the state of the application.                                                                        |
| **Volume Claim Templates**          | StatefulSets use volume claim templates/claims of persistent volumes to keep the state safe in case of crashes or restarts.          |
| **Faster Application**              | Stateful applications don’t need to call the database a second time as session info is stored on the server, making it faster.     |
| **Ordering and Uniqueness**         | Offers ordering and uniqueness, ensuring specific deployment order and identity for pods.                                          |
| **Data-Oriented Applications**      | Associated with data-oriented applications (e.g., databases) that need access to the same volumes even if rescheduled to a new node. |
| **Special Deployment Requirements** | Meets special requirements related to deployment ordering, persistent data, or stable networking.                                 |


ReplicationController VS ReplicaSet
-------------------------------------

1. Both of them ensure that a specified number of pod replicas are running at any given time
2. The difference comes with the usage of selectors to replicate pods
3. Replication is used for the core purpose of Reliability, Load Balancing, and Scaling.



| **Attribute**                           | **ReplicaSet**                                         | **ReplicationController**                               |
|-----------------------------------------|-------------------------------------------------------|--------------------------------------------------------|
| **Label Selector**                      | Uses equality-based requirement for matching labels in the matchLabels field. | Uses the set-based requirement for matching labels in the selector field. |
| **API Group**                           | Belongs to the `apps/v1` API group.                   | Belongs to the `v1` API group.                         |
| **Pod Selection**                       | Supports the use of the `matchLabels` and `matchExpressions` fields for selecting pods. | Supports only the `selector` field for pod selection.   |
| **Rolling Updates Control**             | Allows fine-grained control over rolling updates with features like `maxUnavailable` and `maxSurge`. | Supports a basic rolling update strategy with `rollingUpdate`. |








| **Command**    | **Description**                                                                                     | **Effect**                                                                                           | **Use Case**                                                                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **cordon**     | Marks a node as unschedulable, preventing new pods from being scheduled on it.                       | New pods will not be scheduled on the node, but existing pods continue running.                      | Useful when performing maintenance or upgrades on a node without affecting the running pods.                                                      |
| **uncordon**   | Marks a node as schedulable again, allowing new pods to be scheduled on it.                           | Node becomes schedulable again, allowing the scheduler to place new pods on the node.                | Used after maintenance or upgrades to bring the node back into service and allow new pods to be scheduled.                                        |
| **drain**      | Evicts all pods from the node (except mirror pods) and marks the node as unschedulable.              | Existing pods are gracefully terminated and rescheduled onto other nodes. Node becomes unschedulable. | Useful before performing maintenance or upgrades on a node, ensuring no pods are running during the process.                                      |


Label
-------
1. Label  is a semantic tag which can be attached to objects to mark them as a part of a group.
2. Services use labels to route traffic requests to backend pods
3. Labels are simple key-value pairs. Each unit can have more than one label, but each unit can only have one entry for each key

Annotations
-------------
1. It allows to attach arbitrary key-value information to an object
2. Annotations are more free-form and can contain less structured data


In summary, 
affinity is specifying preferences for scheduling based on certain conditions, 
while anti-affinity is specifying preferences to avoid scheduling based on certain conditions. 
These features provide flexibility and control over how pods are distributed across nodes in a Kubernetes cluster.

K8s Terms
-----------

| **Term**                | **Description**                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Pod**                 | The basic unit of deployment in Kubernetes. A pod is a collection of related Docker containers that need to coexist.            |
| **Containers**          | Docker containers are lightweight virtual machines, and also act as a software packaging and delivery platform.                  |
| **Docker Compose**      | A file that defines services (containers) for communication. It is inherently non-distributed and typically used for local setups. |
| **Headless Service**    | A service without a ClusterIP, allowing direct communication with pods without going through a proxy.                            |




Pod Lifecycle
---------------

| **Pod State**     | **Description**                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Pending**       | The Pod has been accepted by the Kubernetes system, but one or more container images have not been created. Includes time before scheduling and image downloads. |
| **Running**       | The Pod has been bound to a node, and all containers are created. At least one container is running, or in the process of starting or restarting. |
| **Succeeded**     | All containers in the Pod have terminated successfully and will not be restarted.                                                   |
| **Failed**        | All containers in the Pod have terminated, and at least one container has failed (exited with a non-zero status or terminated by the system). |
| **Unknown**       | The state of the Pod could not be obtained, typically due to a communication error with the host.                                    |
| **Waiting**       | Default state. If the container is not in Running or Terminated state, it is in Waiting. The container is still running required operations like pulling images or applying secrets. |
| **Evicted**       | The Pod was evicted due to resource shortages like insufficient memory, unavailable nodes, or image unavailability. This occurs due to Kubernetes limits and requests. |



Image pull policy overview
-----------------------------


| **Restart Policy** | **Description**                                                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Always**         | The container will be restarted regardless of the exit code (even if it exited with a zero exit code). Useful for ensuring the container is always running, such as for a web server. |
| **OnFailure**      | The container will be restarted only if it exited with a non-zero exit code (indicating an error). Useful when ensuring a task completes successfully and needs retrying on failure. |
| **Never**          | The container will not be restarted regardless of why it exited.                                                                    |


## Probes
-----------


| **Probe Type**     | **Description**                                                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **livenessProbe**   | Indicates whether the container is running. If it fails, the kubelet kills the container, and the container is restarted according to its restart policy. Default state is Success if no probe is provided. |
| **readinessProbe**  | Indicates whether the container is ready to serve requests. If it fails, the endpoints controller removes the Pod’s IP address from all Services that match the Pod. |
| **startupProbe**    | Indicates whether the application inside the container has started. All other probes are disabled until it succeeds. If it fails, the kubelet kills the container, and it is restarted according to the restart policy. |

## K8s Errors
---------------


| **Status**                           | **Description**                                                                                              |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Pod Eviction**                     | Pods being evicted due to resource constraints, such as memory or CPU limits being exceeded.                 |
| **ImagePullBackOff**                 | Pods failing to start due to issues pulling container images from the specified repository.                   |
| **CrashLoopBackOff**                 | Pods repeatedly crashing and restarting due to application errors or misconfigurations.                       |
| **NodeNotReady**                     | Nodes being marked as not ready due to various reasons, such as network connectivity issues or resource exhaustion. |
| **ErrorCreatingPodSandBox**          | Issues with creating the network namespace for a pod, often caused by networking plugins or misconfigurations. |
| **PersistentVolumeClaimNotFound**    | Pods failing to start due to issues with accessing PersistentVolumeClaims (PVCs), typically caused by misconfigured storage classes or insufficient storage capacity. |
| **ServiceUnavailable**               | Services being unavailable due to issues with endpoints or connectivity between pods.                        |
| **InvalidConfiguration**             | Errors related to invalid configurations in Kubernetes resources, such as Pods, Deployments, or Services.    |
| **API Server Errors**                | Errors related to the Kubernetes API server, such as timeouts, authentication failures, or resource constraints. |
| **ResourceQuotaExceeded**            | Workloads failing to start or being throttled due to exceeding resource quotas defined in the cluster.       |


## Deployment Strategy
------------------------

| **Strategy**        | **Description**                                                                 | **Deployment Flow**                                                                                                  | **Risk Level**           | **Use Cases**                                                                                          |
|---------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------|
| **Blue-Green**      | A deployment strategy where two environments (Blue and Green) are used. Only one environment (Blue) is live at a time. The new version is deployed to the Green environment, then traffic is switched to Green. | Blue is live, Green has the new version. Once Green is tested, traffic switches from Blue to Green.                    | Low, as rollback is easy | Ideal for large applications where a quick rollback is needed, or when the new version is significantly different. |
| **Canary**          | Gradually rolling out the new version to a small subset of users (the "canary") and monitoring for issues before full deployment. | Deploy to a small percentage of traffic, monitor, then gradually increase the rollout to the rest of users.           | Medium, due to gradual rollout | Useful when changes need to be tested with real user traffic or in cases where the new version may have unforeseen issues. |
| **A/B Testing**     | Two different versions of a feature or application are deployed, and user traffic is split between them to compare performance. | Traffic is split between two or more variants, results are analyzed, and the better-performing variant is selected.    | Medium, based on the complexity of changes | Best for comparing different features or versions of a service or product, especially in marketing and user experience testing. |
| **Recreate**        | The old version of the application is terminated before the new version is deployed, ensuring no overlap. | The current application is stopped, and the new application version is deployed from scratch.                        | High, as downtime is involved | Suitable for environments where downtime is acceptable, and the application is easy to redeploy. |
| **Rolling Update**  | Gradually replaces instances of the old version with the new version without downtime, ensuring that some instances are always available. | The old pods are replaced one by one by the new pods, ensuring minimal downtime during the update.                    | Low to Medium, based on configuration | Ideal for applications that require high availability during updates, with minimal downtime or service disruption. |



CASE-01
---------
| **Step** | **Question**                                                       | **Answer**                                                                                          |
|----------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **1.**   | **Creating a Service and Discovering DNS Names in Kubernetes**     | Create an nginx deployment and expose it via a service to perform DNS queries.                     |
| **2.**   | **How to create an nginx deployment using the latest nginx image?**| `kubectl create deployment nginx --image=nginx:latest`                                              |
| **3.**   | **How to verify that the nginx deployment has been created successfully?** | `kubectl get deployments` or `kubectl describe deployment nginx`                                  |
| **4.**   | **How to create a service from the nginx deployment?**             | `kubectl expose deployment nginx --port=80 --target-port=80 --name=nginx-service`                 |
| **5.**   | **How to verify that the service has been created successfully?**  | `kubectl get services` or `kubectl describe service nginx-service`                                |
| **6.**   | **How to create a pod to perform the DNS query?**                  | `kubectl run dns-query-pod --image=busybox --restart=Never --command -- sleep 3600`                |
| **7.**   | **How to verify that the pod has been created successfully?**      | `kubectl get pods` or `kubectl describe pod dns-query-pod`                                         |
| **8.**   | **How to perform the DNS query to the service?**                   | `kubectl exec dns-query-pod -- nslookup nginx-service`                                             |
| **9.**   | **How to record the DNS name of the service?**                     | The DNS name will be `nginx-service.<namespace>.svc.cluster.local`. Record it for future reference. |






CASE-02
---------

| **Step** | **Command**                                                                 | **Description**                                                                                          |
|----------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **1. Create Deployment (no resources)**                                      | `kubectl create deployment nginx-deploy --image=nginx:1.16 --dry-run=client -o yaml > deploy.yaml`         | Creates a deployment YAML file without creating resources in the cluster.                                  |
| **2. Apply Deployment**                                                      | `kubectl apply -f deploy.yaml --record`                                                                  | Applies the deployment to the cluster and records the rollout history.                                    |
| **3. Check Rollout History**                                                 | `kubectl rollout history deployment nginx-deploy`                                                        | Displays the rollout history of the `nginx-deploy` deployment.                                            |
| **4. Update Deployment Image**                                               | `kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record`                                    | Updates the deployment to use the `nginx:1.17` image and records the change.                             |
| **5. Display Updated Rollout History**                                       | `kubectl rollout history deployment nginx-deploy`                                                        | Displays the updated rollout history of the `nginx-deploy` deployment after the image update.            |
| **6. Rollback to Previous Version**                                          | `kubectl rollout undo deployment/nginx-deploy --to-revision=1`                                           | Rolls back the deployment to the previous version (nginx:1.16).                                           |


COREDNS
-----------


| **Feature**                                                        | **Description**                                                                                                                     |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Multi-threaded Design**                                           | CoreDNS leverages Go for a multi-threaded design, allowing efficient DNS resolution.                                                |
| **Negative Caching**                                                | CoreDNS supports negative caching, meaning it caches failed DNS queries as well as successful ones, which improves overall resolution speed and helps with external lookups. |
| **Lower Memory Requirement**                                        | CoreDNS has a lower memory requirement, making it suitable for clusters with smaller worker nodes.                                    |
| **Single Process (Written in Go)**                                  | CoreDNS is a single process written in Go, simplifying its architecture.                                                           |
| **Containerized DNS Resolution**                                    | A single container handles DNS query resolution, caching, health checks, and metrics.                                               |
| **Round-Robin Load Balancing**                                      | CoreDNS enhances DNS-based round-robin load balancing by randomizing the order in which it returns certain records.                 |
| **Autopath**                                                        | CoreDNS features autopath, which improves DNS response times for external hostnames by optimizing the iteration through search domain suffixes in `resolv.conf`. |



Create vs Apply
-----------------

| **Command**         | **Description**                                                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **kubectl create**   | An imperative command used to create resources by specifying all the details in the command itself. It will throw an error if the resource already exists. |
| **kubectl apply**    | A declarative command used to apply a configuration file describing the desired state of a resource. It can create or update a resource, and it merges the current state with the desired state. |


Docker Terms
----------------


| **Command**          | **Description**                                                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **docker create**     | Creates a new container based on the specified image and configuration but does not start it immediately. The container is left in a stopped state. |
| **docker run**        | Creates and starts a new container based on the specified image, combining the `docker create` and `docker start` steps into a single command. |
| **docker attach**     | Connects to the main process of a running container, useful for interactive sessions with the main process. Does not allow running arbitrary commands. |
| **docker exec**       | Runs a command inside a running container, providing more flexibility for executing various commands. |


Horizontal Scaling vs Vertical Scaling
----------------------------------------

| **Scaling Type**          | **Description**                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| **Vertical Scaling**       | Helps to scale compute power such as CPU and Memory to your existing machine.                             |
| **Horizontal Scaling**     | Involves increasing the number of nodes and distributing the tasks among different nodes.                |







Why are both Kube-DNS and CoreDNS installed by default?
--------------------------------------------------------
The reason for this is that kube-dns service is considered to be something that application depend on, so it remained unchanged when CoreDNS was introduced. It is by design.
If you check, you will see that kube-dns service points at CoreDNS pods. 
Take a look at the label selector it uses and run that selector against pods in the same namespace
kubectl describe -n kube-system service/kube-dns








Create Horizontal Pod Autoscaler
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#create-horizontal-pod-autoscaler
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10

| **Attribute**              | **INIT Containers**                                              | **Sidecar**                                                      |
|----------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| **Execution Order**         | Starts and executes before other containers in the same Pod.     | Runs alongside the main application container in the same Pod.  |
| **Shared Resources**        | Shares the same volume and network as the main container.        | Shares the same volume and network as the main container.       |
| **Purpose**                 | Performs tasks before the rest of the pod is deployed.           | Used for auxiliary tasks such as log shipping, log watching, or monitoring. |
| **Completion Requirement**  | Each Init Container must complete successfully before the next one starts. | Not required to complete before other containers, runs concurrently. |
| **Common Use Cases**        | Task initialization before the main application container starts. | Log shippers, monitoring agents.                               |


| **Attribute**         | **COPY**                                        | **ADD**                                          |
|-----------------------|-------------------------------------------------|--------------------------------------------------|
| **Basic Function**     | Only supports basic copying of local files into the container. | Supports local tar file auto extraction and remote URL support. |
| **Use Case**           | Simple file copying from host to container.    | Can copy files and also handle tar extraction and fetching from remote URLs. |




| **Attribute**          | **ATTACH**                                        | **EXEC**                                          |
|------------------------|---------------------------------------------------|---------------------------------------------------|
| **Function**            | Connects the standard input/output/error of the main process (PID 1) inside the container to the terminal. | Executes a new command or creates a new process in the container's environment. |
| **Main Process**        | Attaches to the process that runs in the container with PID 1. | Runs a new process within the container, independent of PID 1. |
| **Features**            | Directly connects to the main container process, useful for interacting with the existing process. | Allows you to run a process as a different user and provides various other features. |
| **Use Case**            | Used to interact with the main process inside the container. | Used to execute commands in a running container without exiting the container. |







ENTRYPOINT VS CMD
------------------

| **Attribute**                             | **ENTRYPOINT**                                          | **CMD**                                               |
|-------------------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| **Purpose**                               | Invoke executable service when the container is started. | Specifies the arguments which get passed to the ENTRYPOINT. |
| **Command Line Overwrite**                | Command and parameters will not be overwritten from the command line. | Default command and/or parameters, which can be overwritten from the command line. |
| **Syntax Example**                        | `ENTRYPOINT ["executable"]`                             | `CMD ["executable", "arg1", "arg2"]`                   |


| **Attribute**                             | **ENTRYPOINT**                                          | **CMD**                                               |
|-------------------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| **Purpose**                               | Invoke executable service when the container is started. | Specifies the arguments which get passed to the ENTRYPOINT. |
| **Command Line Overwrite**                | Command and parameters will not be overwritten from the command line. | Default command and/or parameters, which can be overwritten from the command line. |
| **Syntax Example**                        | `ENTRYPOINT ["executable"]`                             | `CMD ["executable", "arg1", "arg2"]`                   |



| **Network Type** | **Overlay**                                                       | **Bridge**                                                      | **Hostonly**                                                   |
|------------------|-------------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------|
| **Description**  | Connects containers across multiple hosts (nodes) over a virtual network. | Connects containers on a single host through an internal bridge. | Isolates virtual machines from the outside network; only accessible from the host. |
| **Use Case**     | Multi-host networking for distributed applications.              | Basic container communication on the same host.                | Local testing and development; isolated VMs.                  |
| **IP Assignment**| Each container gets a unique IP on the overlay network.           | Containers share the host’s bridge network subnet.              | Each VM receives an IP in the host-only subnet.                |
| **External Access** | Requires routing or a gateway for external access.             | Limited; needs port forwarding for external access.             | No direct external access; requires NAT for host internet.    |



| **Command**    | **Description**                                                                                     | **Effect**                                                                                           | **Use Case**                                                                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **cordon**     | Marks a node as unschedulable, preventing new pods from being scheduled on it.                       | New pods will not be scheduled on the node, but existing pods continue running.                      | Useful when performing maintenance or upgrades on a node without affecting the running pods.                                                      |
| **uncordon**   | Marks a node as schedulable again, allowing new pods to be scheduled on it.                           | Node becomes schedulable again, allowing the scheduler to place new pods on the node.                | Used after maintenance or upgrades to bring the node back into service and allow new pods to be scheduled.                                        |
| **drain**      | Evicts all pods from the node (except mirror pods) and marks the node as unschedulable.              | Existing pods are gracefully terminated and rescheduled onto other nodes. Node becomes unschedulable. | Useful before performing maintenance or upgrades on a node, ensuring no pods are running during the process.                                      |





1. Taints apply at node level ,allow a node to repel a set of pods.
2. Tolerations are applied to pods, and allow the pods to schedule onto nodes with matching taints
3. Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes
4. Taints and Toleartions are only mean to restrict nodes to accept certains pods

1. requiredDuringSchedulingIgnoredDuringExecution
2. preferredDuringSchedulingIgnoredDuringExecution.






nodeSelector 
---------------
provides a very simple way to constrain pods to nodes with particular labels


| **Parameter**     | **Description**                                               |
|-------------------|---------------------------------------------------------------|
| **maxSurge**      | The maximum number of new pods that will be created at a time. |
| **maxUnavailable**| The maximum number of old pods that will be deleted at a time.|



Docker Volumes:
----------------

Purpose: Docker volumes provide a way to persist data generated by and used by Docker containers. <br><br>
They allow you to share data between containers, or between the host system and containers, in a way that is independent of the container's lifecycle.<br><br>
Characteristics:

1. Volumes are stored outside the container filesystem.
2. They persist data even if the container is removed.
3. Can be named and managed independently of containers.
4. Can be mounted into one or multiple containers simultaneously.
5. Can be used for sharing data between the host and containers.
6. docker run -v /path/on/host:/path/in/container myimage


Storage Drivers:
-----------------
Purpose: Storage drivers are responsible for managing how the Docker daemon interacts with the underlying storage infrastructure. They handle the details of how data is stored, retrieved, and managed on the host system.
Characteristics:

1. Storage drivers interact with the host's filesystem and manage the storage backend.
2. Different storage drivers have different performance characteristics and support different features.
3. Examples of storage drivers include overlay2, aufs, overlay, btrfs, and more.
4. The storage driver used can be configured when installing Docker or when starting the Docker daemon.


In summary, Docker volumes are a high-level abstraction for persisting data across containers, providing a convenient and flexible way to manage data. 
Storage drivers, on the other hand, are lower-level components that interface with the host's storage system to implement the storage and retrieval of container filesystem layers. 
The choice of storage driver can impact performance, compatibility, and behavior of Docker on the host system.



| **Network Type**      | **Description**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| **Bridge Network**     | Connects containers on the same host.                                           |
|                       | Uses Linux bridge for container networking within a host.                       |
|                       | High performance with low latency since it's host-local.                        |
|                       | IPs are typically assigned from the host's local subnet.                        |
| **Overlay Network**    | Connects containers across multiple hosts.                                      |
|                       | Uses VXLAN tunneling for communication between hosts.                           |
|                       | Lower performance than bridge networks due to overhead from tunneling.          |
|                       | IPs are allocated from a network pool spanning multiple hosts.                  |








Multi Stage Docker Images
--------------------------

| **Aspect**               | **Description**                                                                                                                                                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reduced Image Size**    | Multi-stage builds allow you to keep only necessary files and dependencies in the final image, removing development tools, temporary files, and other intermediate components. This reduces the image size, making it efficient to store, pull, and deploy.                   |
| **Improved Build Efficiency** | By separating each build phase (e.g., compiling, testing, packaging) into stages, Docker caches each stage. This caching enables faster rebuilds, as Docker only needs to rebuild the stages that changed, rather than the entire Dockerfile.                                 |
| **Enhanced Security**     | Removing unnecessary tools and packages from the final image minimizes the attack surface. Multi-stage builds can include dependencies only in the build stages, keeping the production stage clean, secure, and focused solely on runtime requirements.                        |
| **Separation of Concerns**| Each stage can focus on a specific part of the build process, such as dependencies, compiling code, and packaging. This modular approach simplifies the Dockerfile, making it more maintainable and reducing the risk of errors.                                               |
| **Summary**               | Multi-stage builds in Docker allow you to create lean, secure, and efficient images while maintaining a cleaner, more maintainable Dockerfile. This approach is especially useful for complex applications and production-grade containers where size, security, and performance are priorities. |


```

# Stage 1: Build Stage
FROM node:18-alpine AS builder

# Install system dependencies for sharp
RUN apk add --no-cache \
    build-base \
    vips-dev \
    libmagic \
    bash \
    libc6-compat

# Create app directory
WORKDIR /usr/app

# Copy package.json and package-lock.json files to work directory
COPY package*.json ./

# Install app dependencies (including optional dependencies for sharp)
RUN npm install --include=optional sharp \
    && npm install passport-google-oauth20 \
    && npm install --save-dev @types/passport-google-oauth20

# Copy all source files into the container
COPY . .

# Build the production app
RUN npm run build

# Stage 2: Production Stage
FROM node:18-alpine

# Install runtime system dependencies
RUN apk add --no-cache \
    libmagic \
    bash \
    libc6-compat

# Create app directory
WORKDIR /usr/app

# Copy the build files and node_modules from the build stage
COPY --from=builder /usr/app/node_modules ./node_modules
COPY --from=builder /usr/app/dist ./dist
COPY --from=builder /usr/app/package*.json ./

# Expose the port on which the app will run
EXPOSE 3001

# Start the server using the production build
CMD ["npm", "run", "start:development"]

```


𝐖𝐡𝐚𝐭 𝐡𝐚𝐩𝐩𝐞𝐧𝐬 𝐰𝐡𝐞𝐧 𝐰𝐞 𝐫𝐮𝐧 𝐤𝐮𝐛𝐞𝐜𝐭𝐥 𝐝𝐞𝐥𝐞𝐭𝐞 𝐩𝐨𝐝 𝐜𝐨𝐦𝐦𝐚𝐧𝐝? 
-------------------------------------------------

| **Action/Step**                                                                                         | **Description**                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Kubectl Delete Pod Action**                                                                            | The pod record in etcd will be updated by the API Server with two fields: `deletionTimestamp` and `deletionGracePeriodSeconds`.                                             |
| **Endpoint Controller Checks Pod Termination**                                                          | The endpoint controller checks if the pod has reached the 'terminating state'.                                                                                              |
| **Remove Pod from Associated Services**                                                                  | Once the pod reaches the terminating state, the endpoint is removed from the associated services to prevent external traffic.                                                 |
| **Remove Endpoint from Objects**                                                                         | The endpoint starts getting removed from objects like Kube-proxy, IPtables, Ingress, CoreDNS, and all others that hold endpoint information.                                   |
| **Kubelet Notified of Pod Update (Terminating)**                                                         | Kubelet is notified when the pod is updated to 'Terminating' state.                                                                                                        |
| **PreStop Hook Execution**                                                                                | If the `preStop` hook exists, it will be executed. If not, the kubelet immediately sends a SIGTERM signal to the main container.                                           |
| **Graceful Shutdown Period**                                                                             | The container is allowed to gracefully shut down for a period determined by `terminationGracePeriodSeconds` (default: 30 seconds).                                          |
| **Force Stop Container**                                                                                 | After the graceful shutdown period, the container is forcibly stopped if not already terminated.                                                                            |
| **Pod Removed from ETCD**                                                                                 | Finally, the API Server removes the pod from ETCD completely after termination.                                                                                             |




𝑯𝒐𝒘 𝒕𝒐 𝒊𝒏𝒄𝒓𝒆𝒂𝒔𝒆 𝒕𝒉𝒆 𝒅𝒆𝒇𝒂𝒖𝒍𝒕 𝒑𝒐𝒅 𝒍𝒊𝒎𝒊𝒕?
------------------------------
It is possible to bypass the required pod limit by passing it to the field max-pods in the Kubernetes configuration file.
$KUBELET_EXTRA_ARGS — max-pods=240


## Ensuring that your pods remain available even if the Kubernetes API server goes down involves implementing strategies to handle API server failures.  

Here are some approaches you can take to achieve this:

| **Strategy**                                                  | **Description**                                                                                                                                                                     |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Use Local Kubelet Cache**                                   | Configure kubelet on each node to cache Kubernetes resources locally, allowing pods to continue running even if the API server becomes temporarily unavailable.                      |
| **Node-Level Resilience**                                     | Ensure that nodes are resilient to API server failures, allowing them to manage pod lifecycle operations even when disconnected from the API server.                                 |
| **Deploy Workloads with --kubelet-preferred-address-types=InternalIP Flag** | Use the `--kubelet-preferred-address-types=InternalIP` flag to instruct the kubelet to use the internal IP address for communication, bypassing the API server when unavailable.     |
| **Use Pod Disruption Budgets (PDBs)**                         | Implement Pod Disruption Budgets to ensure a minimum number of pods remain available during disruptions, even if the API server is down.                                             |
| **Tolerate API Server Failures in Application Design**        | Design applications to tolerate API server failures, with features like retry logic, local data caching, and circuit breakers for intermittent communication failures.                |
| **Implement Multi-Region or Multi-AZ Clusters**                | Deploy multi-region or multi-AZ clusters to improve resilience, spreading workloads across multiple zones or regions to minimize the impact of API server failures.                   |
| **Monitor and Auto-Recover**                                   | Implement monitoring and alerting (e.g., Prometheus, Grafana) to detect API server failures quickly and use automated recovery mechanisms for restarting or failover to standby instances. |


















kubectl create deployment test --image=nginx -n blue

 
## You are tasked with deploying an Nginx application using Kubernetes. Complete the following steps based on the provided tasks: 
 
| **Step** | **Command**                                                                 | **Description**                                                                                          |
|----------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **1. Create Deployment (no resources)**                                      | `kubectl create deployment nginx-deploy --image=nginx:1.16 --dry-run=client -o yaml > deploy.yaml`         | Creates a deployment YAML file without creating resources in the cluster.                                  |
| **2. Apply Deployment**                                                      | `kubectl apply -f deploy.yaml --record`                                                                  | Applies the deployment to the cluster and records the rollout history.                                    |
| **3. Check Rollout History**                                                 | `kubectl rollout history deployment nginx-deploy`                                                        | Displays the rollout history of the `nginx-deploy` deployment.                                            |
| **4. Update Deployment Image**                                               | `kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record`                                    | Updates the deployment to use the `nginx:1.17` image and records the change.                             |
| **5. Display Updated Rollout History**                                       | `kubectl rollout history deployment nginx-deploy`                                                        | Displays the updated rollout history of the `nginx-deploy` deployment after the image update.            |
| **6. Rollback to Previous Version**                                          | `kubectl rollout undo deployment/nginx-deploy --to-revision=1`                                           | Rolls back the deployment to the previous version (nginx:1.16).                                           |



## You are tasked with create nginx pod and expose service on 80 and use busybox to get dns details of nginx service and redirect to /root/CKA/nginx.svc
```
kubectl run nginx-resolver --image=nginx

kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP

kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service

kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service > /root/CKA/nginx.svc

 
kubectl get pod nginx-resolver -o wide
kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup <P-O-D-I-P.default.pod> > /root/CKA/nginx.pod


```

## Get the list of nodes in JSON format and store it in a file at /opt/outputs/nodes-z3444kd9.json
```
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}' > /root/CKA/node_ips

```




## Create a service messaging-service to expose the messaging application within the cluster on port 6379
kubectl expose po messaging --port=6379 --name=messaging-service


## Create a deployment named hr-web-app using the image kodekloud/webapp-color with 2 replicas.
kubectl expose po messaging --port=6379 --name=messaging-service

# Create a static pod named static-busybox on the controlplane node that uses the busybox image and the command sleep 1000
kubectl run po static-busybox --image=busybox --command sleep 1000


## Expose the hr-web-app created in the previous task as a service named hr-web-app-service, accessible on port 30082 on the nodes of the cluster.

kubectl expose deployment hr-web-app --type=NodePort --port=8080 --targetPort=30080 --name=hr-web-app-service  





# Use JSON PATH query to retrieve the osImages of all the nodes and store it in a file /opt/outputs/nodes_os_x43kj56.txt.

kubectl get nodes -o=jsonpath='{.items[*].status.nodeInfo.osImage}'










```

for i in {1..35}; do
   kubectl exec --namespace=kube-public curl -- sh -c 'test=`wget -qO- -T 2  http://webapp-service.default.svc.cluster.local:8080/info 2>&1` && echo "$test OK" || echo "Failed"';
   echo ""
done

```






Autoscale app
# kubectl autoscale deployment nginx --cpu-percent=80 --min=2 --max=3




git clone https://github.com/monitor-ops/metric-server.git

kubectl apply -f  metric-server

kubectl run hpa-nginx --image=nginx --requests=cpu=200m --expose --port=80

kubectl autoscale deployment hpa-nginx --cpu-percent=50 --min=1 --max=10

kubectl describe deployment/hpa-nginx

kubectl describe hpa

kubectl run tomcat --image=tomcat:8.0 --replicas=1

apt-get update
apt-get install curl wget net-tools telnet netcat dnsutils iputils-ping apach2-utils

nslookup kubernetes.default.svc.cluster.local
while true; do curl -I http://hpa-nginx/; done
while true; do ab -n 1000 -c 2 http://hpa-nginx/; done




1. kubectl config view
2. kubectl config use-context cluster1-context
3. export  KUBECONFIG=/opt/play/kubeconfig
4. kubectl config get-contexts
5. kubectl config use-context admin@cluster2
6. export KUBECONFIG=/opt/play/kubeconfig:/var/lib/jenkins/.kube/config:/var/lib/jenkins/config



jenkins@an-1:/opt/play/hello-tomcat-projects/k8s$ cat c3.sh 

SECRET_NAME=us-east-1-ecr-registry
TOK=`aws ecr --region=us-east-1 get-authorization-token --output text --query authorizationData[].authorizationToken | base64 -d | cut -d: -f2`
EMAIL=email@email.com
kubectl create secret docker-registry $SECRET_NAME --docker-server=https://758637906269.dkr.ecr.us-east-1.amazonaws.com --docker-username=AWS  --docker-password="${TOK}"  --docker-email="${EMAIL}" -n testing

kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"'$SECRET_NAME'"}]}' -n testing

echo ${BUILD_NUMBER}

aws ecr --region=us-east-1 get-authorization-token --output text --query authorizationData[].authorizationToken | base64 -d | cut -d: -f2

| Feature                  | API Gateway                         | ALB Ingress                               |
|--------------------------|--------------------------------------|-------------------------------------------|
| **Purpose**              | Manages APIs and facilitates API-first architectures. | Acts as a load balancer for HTTP/HTTPS traffic. |
| **Primary Use Case**     | Suitable for REST, HTTP, WebSocket APIs, and microservices. | Ideal for distributing traffic to backend services in Kubernetes. |
| **Protocol Support**     | Supports HTTP, HTTPS, and WebSocket. | Primarily supports HTTP and HTTPS protocols. |
| **Authentication**       | Offers built-in support for OAuth2, IAM, and Lambda Authorizers. | Requires external mechanisms for authentication (e.g., via annotations or custom configurations). |
| **Rate Limiting**        | Provides built-in rate limiting and throttling. | No native rate limiting; relies on additional tools like WAF or custom setups. |
| **Integration Options**  | Direct integration with AWS Lambda, DynamoDB, Step Functions, etc. | Integrates with Kubernetes services via Ingress Controller. |




| **Tier**         | **Components**                                      | **Description**                                                                                       |
|-------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Presentation**  | - React App (Frontend)                             | - Hosted in a Kubernetes Deployment. <br> - Served via an Ingress Controller (e.g., ALB or NGINX). <br> - Static files (HTML, CSS, JS) often stored in an S3 bucket and cached by CloudFront for performance. |
| **Application**   | - Node.js/Express Backend (API Layer)              | - Hosted in a Kubernetes Deployment as microservices. <br> - Scales based on traffic using Horizontal Pod Autoscaler (HPA). <br> - Exposes APIs consumed by the React app. |
| **Data**          | - RDS PostgreSQL <br> - DynamoDB (NoSQL)           | - RDS handles relational data such as user information, authentication. <br> - DynamoDB used for fast key-value lookups like session management or product catalogs. |
| **Common Services** | - Prometheus & Grafana <br> - Fluentd/CloudWatch Logs | - Monitoring and alerting with Prometheus and Grafana. <br> - Centralized logging using Fluentd or CloudWatch. |





```mermaid
graph TD
  User -->|Requests| ReactApp
  ReactApp -->|APIs| Backend
  Backend -->|Queries| RDS[(RDS PostgreSQL)]
  Backend -->|Lookups| DynamoDB[(DynamoDB)]


```


git clone https://github.com/monitor-ops/metric-server.git

kubectl apply -f  metric-server

kubectl run hpa-nginx --image=nginx --requests=cpu=200m --expose --port=80

kubectl autoscale deployment hpa-nginx --cpu-percent=50 --min=1 --max=10

kubectl describe deployment/hpa-nginx

kubectl describe hpa

kubectl run tomcat --image=tomcat:8.0 --replicas=1

apt-get update
apt-get install curl wget net-tools telnet netcat dnsutils iputils-ping apach2-utils

nslookup kubernetes.default.svc.cluster.local
while true; do curl -I http://hpa-nginx/; done
while true; do ab -n 1000 -c 2 http://hpa-nginx/; done


| **Aspect**                | **Description**                                                                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**             | A Static Pod is a pod managed directly by the kubelet on a specific node, rather than by the Kubernetes API server.                                 |
| **Management**             | Unlike regular pods, Static Pods are not managed by the Kubernetes control plane (API server) but by the kubelet on each node.                     |
| **Creation**               | Static Pods are created by placing their Pod configuration file (YAML or JSON) in the `/etc/kubernetes/manifests/` directory on the node.           |
| **Lifecycle**              | The kubelet on the node automatically creates and manages Static Pods. They are automatically restarted if they fail or get deleted.               |
| **Use Case**               | Often used for running essential cluster services like kube-apiserver, kube-controller-manager, kube-scheduler, and more, outside the control plane. |
| **Scaling**                | Static Pods are not scaled by Kubernetes controllers like Deployments or ReplicaSets; they must be manually managed if scaling is required.          |
| **Visibility**             | Static Pods are visible through the `kubectl get pods --all-namespaces` command but cannot be managed using typical Kubernetes controllers.         |
| **Example**                | A Static Pod is defined in a file like `kube-apiserver.yaml` and stored in `/etc/kubernetes/manifests/` on the node.                               |
| **Configuration**          | Static Pods require no replica management or resource scaling features. The configuration is handled through the kubelet directly.                 |

| **Topic**                                      | **Details**                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Design, deploy, and manage multi-tenant Kubernetes clusters** |                                                                                                   |
| 1. Define clear architecture for multi-tenant clusters.      | Ensure logical separation between tenants using namespaces or clusters.                          |
| 2. Use namespaces for logical tenant isolation.              | Assign each tenant a dedicated namespace with strict access controls.                            |
| 3. Implement pod security standards.                         | Enforce security policies such as PodSecurityPolicy or PodSecurityAdmission.                     |
| 4. Enable audit logging.                                     | Monitor all cluster activity for security and compliance.                                        |
| 5. Use custom controllers or operators.                      | Automate tenant lifecycle management and resource provisioning.                                  |
| 6. Configure autoscaling.                                    | Ensure cluster performance with Horizontal Pod Autoscaler (HPA) and Cluster Autoscaler.          |
| 7. Isolate storage resources.                                | Assign separate Persistent Volumes (PVs) or StorageClasses for tenant data.                      |
| 8. Use service mesh for communication.                       | Secure inter-tenant communication using service mesh (e.g., Istio, Linkerd).                     |
| 9. Encrypt secrets and sensitive data.                       | Use Kubernetes Secrets and integrate with external tools like Vault for secure secret management.|
| 10. Regularly update and patch clusters.                     | Apply updates to Kubernetes and related components for improved security and stability.           |

| **Topic**                                      | **Details**                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Implement RBAC Policies**                   |                                                                                                   |
| 1. Define roles for tenant-specific permissions.             | Use Role and ClusterRole objects to grant permissions at the required scope.                     |
| 2. Bind roles to users and service accounts.                 | Use RoleBinding and ClusterRoleBinding to associate roles with users or service accounts.        |
| 3. Use least privilege principle.                           | Grant only the minimum required permissions for tasks.                                           |
| 4. Create a default deny-all policy.                        | Start with no access and explicitly allow required actions.                                      |
| 5. Use custom groups for users.                             | Organize users into groups and manage access at the group level.                                 |
| 6. Audit RBAC changes.                                      | Track changes to roles and bindings using audit logs.                                            |
| 7. Regularly review and revoke unused roles.                | Remove outdated permissions and roles to maintain security.                                      |
| 8. Integrate with external identity providers.              | Use SSO systems like Okta or LDAP for centralized user management.                               |
| 9. Test RBAC policies in staging.                           | Validate policies in a non-production environment to ensure correctness.                         |
| 10. Document role definitions and bindings.                 | Maintain a record of RBAC configurations for future reference and audits.                       |

| **Topic**                                      | **Details**                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Implement Network Segmentation**            |                                                                                                   |
| 1. Use Kubernetes Network Policies.                        | Define ingress and egress rules for tenant pods.                                                 |
| 2. Isolate namespaces using network policies.              | Ensure tenants cannot access resources in other namespaces.                                      |
| 3. Use CNI plugins with segmentation features.             | Deploy plugins like Calico, Cilium, or WeaveNet for fine-grained network control.                |
| 4. Configure DNS resolution per tenant.                    | Restrict tenants to resolve only their resources.                                                |
| 5. Separate cluster ingress by tenant.                     | Use different ingress controllers or configurations for tenants.                                |
| 6. Monitor network traffic between pods.                   | Use tools like Istio or Kiali to visualize and control traffic flow.                             |
| 7. Enable encrypted communication (TLS).                   | Ensure all network communication is encrypted for security.                                      |
| 8. Implement egress controls.                              | Restrict outbound access to external networks based on tenant requirements.                      |
| 9. Use firewalls or security groups at the cloud level.     | Add another layer of security for network isolation.                                             |
| 10. Regularly test segmentation policies.                  | Perform penetration tests to identify and fix segmentation gaps.                                 |

| **Topic**                                      | **Details**                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Apply Resource Limits**                     |                                                                                                   |
| 1. Set CPU and memory limits for pods.                      | Define `limits` and `requests` in resource specifications to prevent overuse.                    |
| 2. Use ResourceQuotas per namespace.                       | Control the total resource allocation for a namespace.                                           |
| 3. Use LimitRanges for finer control.                      | Set default requests and limits for resources in a namespace.                                    |
| 4. Monitor resource usage with tools like Prometheus.      | Identify trends and potential bottlenecks in resource usage.                                     |
| 5. Enable Horizontal Pod Autoscaling (HPA).               | Scale pods automatically based on resource consumption.                                          |
| 6. Implement Vertical Pod Autoscaling (VPA).              | Adjust pod resource requests and limits automatically.                                           |
| 7. Avoid over-provisioning of resources.                  | Assign realistic resource limits to prevent wasted capacity.                                     |
| 8. Reserve resources for system components.               | Ensure critical system components have sufficient resources.                                     |
| 9. Use node selec




# Architecture Diagram

![Architecture Diagram](diagram/e1.png)



