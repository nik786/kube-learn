
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



##Configmaps
--------------

1. ConfigMaps are similar to Secrets
2. It is designed to more conveniently support working with strings that do not contain sensitive information
3. They can be used to store individual properties in form of key-value 	pairs


##This configuration data can then be used as:
----------------------------------------------

1. Environment variables
2. Command-line arguments for a container
3. Config files in a volume
4. A difference to the secrets concept is that ConfigMaps actually get 	updated without the 


##Secrets:
-----------
1. Secrets can be used for storing small amounts of sensitive information 	like passwords, keys, tokens, etc
2. Kubernetes creates and uses some secrets automatically (e.g. for accessing the 	API from a pod), but you can also create your own easily
3. Secrets are kept in a tmpfs and only on nodes that run pods that use those 	secrets
4. They 	are transmitted to and from the API server in plain text
5. Running pods won’t automatically pull the updated secret.You need to explicitly update your pods (for example using the rolling update functionality of deployments



ABAC, Attribute Based Access Control
--------------------------------------
It requires ssh and root filesystem access on the master VM of the cluster to make authorization policy changes. 
For permission changes to take effect the cluster API server must be restarted.

RBAC
------
RBAC permission policies are configured using kubectl or the Kubernetes API directly. Users can be authorized to make 
authorization policy changes using RBAC itself, making it possible to delegate resource management without giving away ssh access to the cluster master. 

Volumes and Persistent Volumes
-----------------------------------
Persistent volumes are a mechanism for abstracting more robust storage which is not tied to the pod life cycle. 
Instead, they allow administrators to configure storage resources for the cluster that users can request and claim for the pods they are running. 
Once a pod is done with a persistent volume, the volume's reclamation policy determines whether the volume is kept around until manually deleted or removed along with the data immediately.


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


| **Term**                | **Description**                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Pod**                 | The basic unit of deployment in Kubernetes. A pod is a collection of related Docker containers that need to coexist.            |
| **Containers**          | Docker containers are lightweight virtual machines, and also act as a software packaging and delivery platform.                  |
| **Docker Compose**      | A file that defines services (containers) for communication. It is inherently non-distributed and typically used for local setups. |
| **Headless Service**    | A service without a ClusterIP, allowing direct communication with pods without going through a proxy.                            |


emptyDir
----------
1. It is a type of volume which is created when a Pod is first assigned to a Node.
2. It remains active as long as the Pod is running on that node.
3. The volume is initially empty and the containers in the pod can read and write the files in the emptyDir volume.
4. Once the Pod is removed from the node, the data in the emptyDir is erased.

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





| **Probe Type**     | **Description**                                                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **livenessProbe**   | Indicates whether the container is running. If it fails, the kubelet kills the container, and the container is restarted according to its restart policy. Default state is Success if no probe is provided. |
| **readinessProbe**  | Indicates whether the container is ready to serve requests. If it fails, the endpoints controller removes the Pod’s IP address from all Services that match the Pod. |
| **startupProbe**    | Indicates whether the application inside the container has started. All other probes are disabled until it succeeds. If it fails, the kubelet kills the container, and it is restarted according to the restart policy. |


CASE-01
---------
1. Creating a Service and Discovering DNS Names in Kubernetes
2. Create an nginx deployment using the latest nginx image.
3. Verify the deployment has been created successfully.
4. Create a service from the nginx deployment created in the previous objective.
5. Verify the service has been created successfully.
6. Create a pod that will allow you to perform the DNS query.
7. Verify that the pod has been created successfully.
8. Perform the DNS query to the service created in an earlier objective.
9. Record the DNS name of the service.


Create an nginx deployment, and verify it was successful.
kubectl run nginx --image=nginx
Use this command to verify deployment was successful:
kubectl get deployments
Create a service, and verify the service was successful.
kubectl expose deployment nginx --port 80 --type NodePort
Use this command to verify the service was created:
kubectl get services


Create a pod that will allow you to perform the DNS query.
k create -f https://github.com/nik786/kube-learn/blob/master/pods/dns-pods/busy.yml
kubectl run tomcat --image=tomcat:8.0 --replicas=1  -n kube-system 
kubectl exec -ti  tomcat-74fb4fff95-tmqlc -n kube-system /bin/bash

nslookup kubernetes.default.svc.cluster.local
nslookup kubernetes.default.svc.cluster.local 10.254.0.20

Perform a DNS query to the service
kubectl exec busybox -- nslookup nginx
Perform a DNS query to the service.
<service-name>;.default.svc.cluster.local

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





| **Command**         | **Description**                                                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **kubectl create**   | An imperative command used to create resources by specifying all the details in the command itself. It will throw an error if the resource already exists. |
| **kubectl apply**    | A declarative command used to apply a configuration file describing the desired state of a resource. It can create or update a resource, and it merges the current state with the desired state. |



| **Command**          | **Description**                                                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **docker create**     | Creates a new container based on the specified image and configuration but does not start it immediately. The container is left in a stopped state. |
| **docker run**        | Creates and starts a new container based on the specified image, combining the `docker create` and `docker start` steps into a single command. |
| **docker attach**     | Connects to the main process of a running container, useful for interactive sessions with the main process. Does not allow running arbitrary commands. |
| **docker exec**       | Runs a command inside a running container, providing more flexibility for executing various commands. |



Why are both Kube-DNS and CoreDNS installed by default?
The reason for this is that kube-dns service is considered to be something that application depend on, so it remained unchanged when CoreDNS was introduced. It is by design.
If you check, you will see that kube-dns service points at CoreDNS pods. 
Take a look at the label selector it uses and run that selector against pods in the same namespace
kubectl describe -n kube-system service/kube-dns




| **Scaling Type**          | **Description**                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| **Vertical Scaling**       | Helps to scale compute power such as CPU and Memory to your existing machine.                             |
| **Horizontal Scaling**     | Involves increasing the number of nodes and distributing the tasks among different nodes.                |



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




| **Attribute**                               | **DevOps**                                                 | **SRE (Site Reliability Engineering)**                           |
|---------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------|
| **Ownership & Oversight**                   | DevOps teams can have ownership and oversight over a number of tools and platforms. | Focus on system health and operational reliability.                |
| **Automation Focus**                        | DevOps is focused on automating deployment, redundancy, and manual tasks to ensure system uptime. | SRE focuses on automating operational processes to maintain system reliability. |
| **Role of Engineers**                       | DevOps Engineers are ops-focused engineers who solve development pipeline problems. | SRE Engineers are development-focused engineers who solve operational, scaling, and reliability problems. |
| **Objective**                               | Increase software delivery velocity, improve service reliability, and build shared ownership among software stakeholders. | Outcome of combining system operations responsibilities with software development and engineering. |



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


Taints apply at node level ,allow a node to repel a set of pods.
Tolerations are applied to pods, and allow the pods to schedule onto nodes with matching taints
Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes
Taints and Toleartions are only mean to restrict nodes to accept certains pods

requiredDuringSchedulingIgnoredDuringExecution 
preferredDuringSchedulingIgnoredDuringExecution.

nodeSelector 
---------------
provides a very simple way to constrain pods to nodes with particular labels


| **Parameter**     | **Description**                                               |
|-------------------|---------------------------------------------------------------|
| **maxSurge**      | The maximum number of new pods that will be created at a time. |
| **maxUnavailable**| The maximum number of old pods that will be deleted at a time.|



Docker Volumes:
Purpose: Docker volumes provide a way to persist data generated by and used by Docker containers. They allow you to share data between containers, or between the host system and containers, in a way that is independent of the container's lifecycle.
Characteristics:
Volumes are stored outside the container filesystem.
They persist data even if the container is removed.
Can be named and managed independently of containers.
Can be mounted into one or multiple containers simultaneously.
Can be used for sharing data between the host and containers.
docker run -v /path/on/host:/path/in/container myimage


Storage Drivers:
Purpose: Storage drivers are responsible for managing how the Docker daemon interacts with the underlying storage infrastructure. They handle the details of how data is stored, retrieved, and managed on the host system.
Characteristics:
Storage drivers interact with the host's filesystem and manage the storage backend.
Different storage drivers have different performance characteristics and support different features.
Examples of storage drivers include overlay2, aufs, overlay, btrfs, and more.
The storage driver used can be configured when installing Docker or when starting the Docker daemon.


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
Using multi-stage builds in Dockerfiles offers several advantages that help optimize image size, improve build efficiency, and enhance security. Here’s how multi-stage builds are beneficial:
Reduced Image Size: Multi-stage builds allow you to keep only necessary files and dependencies in the final image, removing development tools, temporary files, and other intermediate components. This reduces the image size, making it more efficient to store, pull, and deploy.
Improved Build Efficiency: By separating each build phase (e.g., compiling, testing, packaging) into stages, Docker caches each stage. This caching enables faster rebuilds, as Docker only needs to rebuild the stages that changed, rather than the entire Dockerfile.
Enhanced Security: Removing unnecessary tools and packages from the final image minimizes the attack surface. Multi-stage builds can include dependencies only in the build stages, keeping the production stage clean, secure, and focused solely on runtime requirements.
Separation of Concerns: Each stage can focus on a specific part of the build process, such as dependencies, compiling code, and packaging. This modular approach simplifies the Dockerfile, making it more maintainable and reducing the risk of errors.
In short, multi-stage builds in Docker allow you to create lean, secure, and efficient images while maintaining a cleaner, more maintainable Dockerfile. This approach is especially useful for complex applications and production-grade containers where size, security, and performance are priorities.





𝐖𝐡𝐚𝐭 𝐡𝐚𝐩𝐩𝐞𝐧𝐬 𝐰𝐡𝐞𝐧 𝐰𝐞 𝐫𝐮𝐧 𝐤𝐮𝐛𝐞𝐜𝐭𝐥 𝐝𝐞𝐥𝐞𝐭𝐞 𝐩𝐨𝐝 𝐜𝐨𝐦𝐦𝐚𝐧𝐝? 
Let's break it down :
✅ With 'kubectl delete pod' action, the pod record in etcd will be updated by the API Server with two different fields "𝒅𝒆𝒍𝒆𝒕𝒊𝒐𝒏𝑻𝒊𝒎𝒆𝒔𝒕𝒂𝒎𝒑" and "𝒅𝒆𝒍𝒆𝒕𝒊𝒐𝒏𝑮𝒓𝒂𝒄𝒆𝑷𝒆𝒓𝒊𝒐𝒅𝑺𝒆𝒄𝒐𝒏𝒅𝒔"
✅ The endpoint controller checks whether the pod has reached 'terminating state' 
✅ Once the state is reached, it removes the endpoint of the pod from the associated services to prevent external traffic
✅ The endpoint starts getting removed from 𝐊𝐮𝐛𝐞-𝐩𝐫𝐨𝐱𝐲, 𝐈𝐏𝐭𝐚𝐛𝐥𝐞𝐬, 𝐈𝐧𝐠𝐫𝐞𝐬𝐬, 𝐂𝐨𝐫𝐞𝐃𝐍𝐒 and all other objects that hold endpoint information
✅ 𝐊𝐮𝐛𝐞𝐥𝐞𝐭 is notified of the pod being updated (Terminating). 
✅ If the 'preStop' exists, the hook is executed, if not, the kubelet immediately sends a 𝐒𝐈𝐆𝐓𝐄𝐑𝐌 signal to the main container
✅ After waiting for a graceful shutdown period, which is determined by the terminationGracePeriodSeconds and by default is '30' seconds, the container is forcibly stopped.
✅ Finally, the API Server removes the pod from ETCD completely.



𝑯𝒐𝒘 𝒕𝒐 𝒊𝒏𝒄𝒓𝒆𝒂𝒔𝒆 𝒕𝒉𝒆 𝒅𝒆𝒇𝒂𝒖𝒍𝒕 𝒑𝒐𝒅 𝒍𝒊𝒎𝒊𝒕?
It is possible to bypass the required pod limit by passing it to the field max-pods in the Kubernetes configuration file.
$KUBELET_EXTRA_ARGS — max-pods=240


Ensuring that your pods remain available even if the Kubernetes API server goes down involves implementing strategies to handle API server failures.  Here are some approaches you can take to achieve this:
Use Local kubelet Cache:
Configure kubelet on each node to cache Kubernetes resources locally. This allows pods to continue running even if the 
API server becomes temporarily unavailable. The kubelet will use the cached resources to maintain pod lifecycle operations.
Node-Level Resilience:
Ensure that your nodes are resilient to API server failures. Nodes should continue running workloads and manage pod lifecycle 
operations even if they lose connectivity to the API server. This requires robust node-level components such as kubelet, container runtime, and network plugins.
Deploy Workloads with --kubelet-preferred-address-types=InternalIP Flag:
When deploying pods, you can use the --kubelet-preferred-address-types=InternalIP flag to instruct the kubelet to use the internal 
IP address of the node for communication, bypassing the need for the API server. This allows pods to continue functioning even if the API server is unreachable.
Use Pod Disruption Budgets (PDBs):
Implement Pod Disruption Budgets to define the minimum number of pods that must remain available during disruptions. 
This ensures that even if the API server goes down, a sufficient number of pods are still running to maintain application availability.
Tolerate API Server Failures in Application Design:
Design your applications to tolerate temporary API server failures gracefully. This may involve implementing retry logic, 
caching data locally within pods, and using circuit breakers to handle intermittent communication failures.
Implement Multi-Region or Multi-AZ Clusters:
Deploy multi-region or multi-AZ Kubernetes clusters to improve resilience against API server failures. Spread your 
workload across multiple regions or availability zones to minimize the impact of a single API server failure.
Monitor and Auto-Recover:
Implement monitoring and alerting to detect API server failures quickly. Use tools like Prometheus and Grafana to 
monitor API server health and set up alerts to notify you of any issues. Additionally, consider using automated recovery
mechanisms to restart the API server or failover to standby instances.




Pod Eviction: Pods being evicted due to resource constraints, such as memory or CPU limits being exceeded.
ImagePullBackOff: Pods failing to start due to issues pulling container images from the specified repository.
CrashLoopBackOff: Pods repeatedly crashing and restarting due to application errors or misconfigurations.
NodeNotReady: Nodes being marked as not ready due to various reasons, such as network connectivity issues or resource exhaustion.
ErrorCreatingPodSandBox: Issues with creating the network namespace for a pod, often caused by networking plugins or misconfigurations.

PersistentVolumeClaimNotFound: Pods failing to start due to issues with accessing PersistentVolumeClaims (PVCs), typically caused by misconfigured storage classes or insufficient storage capacity.


ServiceUnavailable: Services being unavailable due to issues with endpoints or connectivity between pods.
InvalidConfiguration: Errors related to invalid configurations in Kubernetes resources, such as Pods, Deployments, or Services.
API Server Errors: Errors related to the Kubernetes API server, such as timeouts, authentication failures, or resource constraints.
ResourceQuotaExceeded: Workloads failing to start or being throttled due to exceeding resource quotas defined in the cluster.




Helm Installation
curl -O https://github.com/kubernetes/helm/archive/v2.7.2.tar.gz
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh

https://github.com/helm/helm/releases?after=v2.7.2
https://github.com/helm/helm/releases?after=v.3.4.0

wget https://github.com/kubernetes/helm/releases/download/v3.4.0/helm-v3.4.0-linux-amd64.tar.gz
wget https://get.helm.sh/helm-v3.0.2-linux-amd64.tar.gz

cp helm /usr/local/bin/

helm version

export KUBECONFIG=/etc/kubernetes/admin.conf


helm repo add stable https://kubernetes-charts.storage.googleapis.com/

helm repo list


HELM CONFIG FOR APACHE

 helm repo add bitnami https://charts.bitnami.com/bitnami

 helm search repo apache

mkdir chart/apache

Download of Helm Chart on particular directory
helm fetch bitnami/apache -d chart/apache/

INSTALLATION COMMANDS OF APACHE HELM CHARTS  FROM CUSTOM CONFIGS

helm install myapache  bitnami/apache -d chart/apache/
helm install demo-apache bitnami/apache  -f /tmp/values.yaml
helm install demo-apache-v1 bitnami/apache  -f /tmp/values1.yaml
helm upgrade demo-apache bitnami/apache  -f /tmp/values.yaml 

PROCESS TO CHECK CREATED SERVICE IN K8S 

kubectl get svc demo-apache -o wide

curl -k https://10.233.120.62:8443
curl -k https://10.233.120.62:8443


HELM CONFIG FOR TOMCAT

helm fetch  bitnami/tomcat -d tomcat/

docker build -t 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:tom-61 --pull=true --file=/var/lib/jenkins/hello-world/Dockerfiles/tomcat-dockerfile  /var/lib/jenkins/hello-world/Dockerfiles/

docker push 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:tom-60


helm install mytomcat ./tomcat --set image.registry=758637906269.dkr.ecr.us-east-1.amazonaws.com --set image.repository=connector-dev --set image.tag=tom-61  -n testing

helm uninstall tomcat-1585376255 -n testing

helm ls -n testing


HELM CONFIG FOR Nginx

docker build -t 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:nginx-60 --pull=true --file=/var/lib/jenkins/hello-world/Dockerfiles/nginx-dockerfile  /var/lib/jenkins/hello-world/Dockerfiles/

docker push 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:nginx-60

helm install mynginx ./nginx --set image.registry=758637906269.dkr.ecr.us-east-1.amazonaws.com --set image.repository=connector-dev --set image.tag=nginx-60  -n testing

kubectl get svc -n testing -o wide

kubectl get po -n testing -o wide

curl  http://192.168.56.145:30080

LOADTESTING

for i in {1..10};do ab -n 100 -c 2 http://10.233.22.155/;done

ab -n 1000 -c 2 http://10.233.68.224/
for i in {1..1000};do curl -I  http://10.233.119.203/;done
while true; do curl -I http://hpa-nginx/; done
while true; do ab -n 1000 -c 2 http://hpa-nginx/; done


kubectl config view
kubectl config use-context cluster1-context
export  KUBECONFIG=/opt/play/kubeconfig
kubectl config get-contexts
kubectl config use-context admin@cluster2
export KUBECONFIG=/opt/play/kubeconfig:/var/lib/jenkins/.kube/config:/var/lib/jenkins/config
Local Laptop
Export  KUBECONFIG=cluster1.kubeconfig 

jenkins@an-1:/opt/play/hello-tomcat-projects/k8s$ cat c3.sh 

SECRET_NAME=us-east-1-ecr-registry
TOK=`aws ecr --region=us-east-1 get-authorization-token --output text --query authorizationData[].authorizationToken | base64 -d | cut -d: -f2`
EMAIL=email@email.com
kubectl create secret docker-registry $SECRET_NAME --docker-server=https://758637906269.dkr.ecr.us-east-1.amazonaws.com --docker-username=AWS  --docker-password="${TOK}"  --docker-email="${EMAIL}" -n testing

kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"'$SECRET_NAME'"}]}' -n testing

echo ${BUILD_NUMBER}

aws ecr --region=us-east-1 get-authorization-token --output text --query authorizationData[].authorizationToken | base64 -d | cut -d: -f2



Difference Between RollingUpdate and Recreate:
RollingUpdate:

Gradual Transition: Pods are replaced one by one or a few at a time, allowing for a smooth transition with no complete downtime.
Service Availability: This keeps the service available during the update since only part of the replicas is updated at any given time.
Configuration Options: Can configure maxSurge and maxUnavailable to control the rollout pace and availability.
Recreate:

Complete Shutdown: All existing pods are terminated before new pods are created, which can cause a temporary service outage.
No Overlap: Ensures there is no overlap between old and new versions, as new pods are only created once all old pods are fully terminated.
Simplicity: This strategy is simpler and may be suitable for applications where downtime is acceptable, such as batch jobs.
In summary, RollingUpdate provides a way to update with zero downtime, while Recreate can result in downtime but is simpler and sometimes desirable for applications that cannot handle mixed versions.


Use Retain when data persistence is critical and you want to ensure that data is not lost immediately upon deletion of the PVC.
Use Delete when you want the storage to be automatically cleaned up and you do not need to retain the data after the PVC is gone.
Recycle (deprecated in newer versions of Kubernetes):
When the PVC is deleted, the PV is scrubbed (data is deleted), and it becomes available for another claim.



Application Charts:
These charts define how to deploy specific applications or services on Kubernetes. They include resources like Deployments, Services, ConfigMaps, and Ingress, which are configured to install and manage the lifecycle of an application.
Examples: WordPress, MySQL, Nginx, Redis.
Library Charts:
Library charts are reusable charts that define shared logic or templates that can be included in other charts. They don’t create Kubernetes resources on their own but provide common functionalities that can be used by other application charts.
Examples: A chart that defines a standard PodSecurityPolicy or a chart for configuring storage volumes that can be shared across different application charts.
Additionally, you can categorize charts based on their purpose:
Stable Charts: These are well-maintained and officially supported charts, usually found in the Helm stable repository.
Incubating Charts: Charts that are still being tested and developed, typically not yet ready for production but shared for experimentation and feedback.


Package a Chart
helm package my-chart/
Lint a Chart
helm lint my-chart/
Render Chart Templates Locally
helm template my-release nginx --namespace web-apps
History of a Release
helm history <release-name>
Diff a Release
helm plugin install https://github.com/databus23/helm-diff
helm diff upgrade <release-name> <chart-name>


Uninstall a Release
helm uninstall my-release --namespace web-apps
Search for Charts
helm search repo nginx
Add a Helm Repository
helm repo add bitnami https://charts.bitnami.com/bitnami
Update Helm Repositories
helm repo update
Show Chart Details
helm show chart bitnami/nginx
View Chart Values
helm show values bitnami/nginx


Helm Commands
Helm has several powerful commands:
helm install: Deploys a chart as a release to a Kubernetes cluster.
helm upgrade: Upgrades a release with updated chart configurations or a new version.
helm rollback: Rolls back a release to a previous version.
helm list: Lists all Helm releases in the cluster.
helm uninstall: Removes a release from the cluster.
Install a Helm Chart
helm install my-release nginx --namespace web-apps
List Installed Releases
helm list --namespace <namespace>
Upgrade a Release
helm upgrade my-release nginx --set replicaCount=3
Rollback a Release
helm rollback <release-name> <revision>




Helm Repositories
Helm repositories are collections of Helm charts. The default repository is the Helm Stable repo, but users can add others (like Bitnami, JFrog, or custom ones). Repositories enable Helm to search, update, and install charts from various sources
Templating Engine
Helm uses Go templates for chart templates, allowing dynamic and reusable resource definitions. Through templating, you can create resources that adapt based on the values specified at installation time, which makes Helm flexible and customizable.
Chart Dependencies
Helm allows charts to depend on other charts, defining these dependencies in the Chart.yaml file. Helm ensures dependencies are downloaded and managed, supporting complex applications that rely on multiple components, like databases or caching services
Helm Hooks
Helm hooks allow you to perform tasks at specific points in the release lifecycle, such as before installing or after upgrading a release. They are often used for tasks like database migrations or custom pre/post-deployment actions.
Helmfile for Multi-Chart Management
Helmfile is an open-source tool that helps manage multiple Helm releases with a single configuration file. It enables you to define, install, and upgrade multiple charts at once, making it useful for complex deployments that require multiple Helm charts and configurations.


What is Helm?
Helm is a Kubernetes package manager that allows you to define, install, and upgrade applications as collections of Kubernetes manifests called charts. It simplifies complex application deployments by grouping Kubernetes resources and configurations.
2. Helm Charts
A Helm Chart is a collection of files that describe a set of Kubernetes resources. It contains templates for Kubernetes resources, metadata, and values that can be customized. Charts can be shared or customized and are stored in Helm repositories.
3. Values Files
Helm charts come with a values.yaml file, which holds customizable parameters. During deployment, users can specify values in the values.yaml file or override them on the command line to adjust configurations without altering the core chart structure.
4. Release Management
When Helm installs a chart, it creates a release that represents an instance of that chart. Helm uses these releases to manage versions and upgrades, allowing you to roll back changes if necessary. Each release is tracked, making management and rollback easier.
















kubectl autoscale deployment nginx --cpu-percent=80 --min=2 --max=3











