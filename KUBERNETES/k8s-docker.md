
##Kubernetes
-----------------
It allows us to run containers across multiple compute nodes <br>
Once Kubernetes takes control over a cluster of nodes, it can start or stop containers <br>
anytime based on what we need.

- [python-app-dockerfile](https://github.com/infra-ops/kub-poc/blob/master/cloud_k8s_platform/eks/infra_deployment/zero-click-eks-deployment/app-build/greendockerfile)
- [multi-stage-dockerfile](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/multi-stage-nodejs-dockerfile)
- [networkpolicy](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/np01.md)
- [pv-pvc](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/pv-pvc-01.md)

- [efs-pv-pvc](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/efs-pv-pvc.md)

- [vertical-scaling](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/vertical-scaling.md)

Ingress
------------

- [apple-app-ing-svc](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/green-app-ing-svc.md)
- [apple-app-ing](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/apple-app-ing.md)
- [apple-app-ing-ssl-svc](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/apple-app-ing-svc-ssl.md)
- [web-app-ing-video](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/web-app-video-svc-ing.md)  
- [kibana-ing](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/kibana-ing.md)
- [tomcat-ing](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/tomcat-ing.md)

Generic
------------

- [Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/)
- [Certificate Rotation](https://kubernetes.io/docs/tasks/tls/certificate-rotation/)
- [Best Practises](https://kubernetes.io/docs/setup/best-practices/)
- [K8s-Blog](https://kubernetes.io/blog/)
- [Workloads](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Usecases](https://vlinkinfo.com/blog/top-kubernetes-use-cases/)
- [medium-ckad](https://medium.com/bb-tutorials-and-thoughts/practice-enough-with-these-questions-for-the-ckad-exam-2f42d1228552)
  
- [my-cka](https://github.com/nik786/kube-learn/blob/master/cka.yml)

- [medium-cka](https://medium.com/@sensri108/practice-examples-dumps-tips-for-cka-ckad-certified-kubernetes-administrator-exam-by-cncf-4826233ccc27)
- [prac-medium](https://medium.com/bb-tutorials-and-thoughts/practice-enough-with-these-questions-for-the-ckad-exam-2f42d1228552)
- [cka-02](https://github.com/walidshaari/Kubernetes-Certified-Administrator)
- [cka-03](https://github.com/nik786/kube-learn/blob/master/ques-and-ans/medium-ques-ans.yml)




| Feature         | Endpoint                                 | TargetPort                               |
|-----------------|------------------------------------------|------------------------------------------|
| Definition      | Actual IP and port of the backend Pod.   | Port on the Pod where the app listens.   |
| Purpose         | Used by Service to route traffic to Pods.| Defines where Service forwards traffic.  |




| Feature | HPA (Horizontal Scaling) | VPA (Vertical Scaling) |
|---------|--------------------------|------------------------|
| Scaling Type | Adds or removes instances based on CPU/memory usage. | Adjusts CPU/memory allocation for existing instances. |
| Use Case | Best for handling high traffic by launching more instances. | Best for optimizing resource usage of existing instances. |
| Impact on Instances | Creates new instances or terminates extra ones dynamically. | Restarts instances to apply new resource limits. |
| Works Well With | Stateless applications that can scale out easily. | Stateful applications where scaling out is not feasible. |


 ALB Ingress  vs API Gateway 
 -------------------------------

 

| No. | Feature                        | ALB Ingress                                      | API Gateway                                      |
|-----|--------------------------------|--------------------------------------------------|--------------------------------------------------|
| 1   | **Primary Use Case**           | Mainly used for load balancing HTTP/S traffic to Kubernetes or EC2 services | Primarily used for managing and routing API requests to backend services |
| 2   | **Traffic Type**               | Supports HTTP, HTTPS, WebSocket, and gRPC protocols | Primarily designed for HTTP, REST, WebSocket, and HTTP/2 APIs |
| 3   | **Traffic Management**         | Routes traffic based on HTTP host and path rules | Supports more complex API routing, rate limiting, and authorization |
| 4   | **Scaling**                    | Automatically scales with traffic and integrates directly with Kubernetes Ingress | Automatically scales based on the number of API calls, supports throttling and rate limiting |
| 5   | **Authentication & Authorization** | Supports basic authentication and integration with AWS IAM for access control | Provides built-in support for AWS IAM, Lambda authorizers, and Amazon Cognito for API access control |



## Comparison of Ingress Controller and Ingress Resources

| **Aspect**            | **Ingress Controller**                                                                       | **Ingress Resource**                                                                          |
|------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Definition**         | A Kubernetes component that implements the rules defined in Ingress resources.              | A Kubernetes object that defines routing rules for HTTP/S traffic to services in the cluster. |
| **Role**               | Acts as a load balancer or reverse proxy to enforce Ingress rules.                          | Specifies host/path-based routing, TLS settings, and backend services.                        |
| **Installation**       | Needs to be installed separately (e.g., NGINX, Traefik, HAProxy).                           | Created and managed via `kubectl` as a native Kubernetes resource.                            |
| **Function Dependency**| Cannot function without Ingress resources to interpret.                                     | Requires an Ingress Controller to actually enforce the defined rules.                         |





### What happens when we execute the kubectl apply command?
-----------------------------------------------------------------------------


```plaintext
Commands Execution (Kubectl)  
      ↓  
Yaml Validation (Kube-API)  
      ↓  
API Request Preparation (Kube-API)  
      ↓  
Authentication & Authorization (Kube-API)  
      ↓  
Object Validation (Kube-API)  
      ↓  
Etcd Write (Etcd)  
      ↓  
Controller Trigger (Kube-Controller)  
      ↓  
Pod Scheduling (Scheduler)  
      ↓  
Pod Creation (Kubelet)  
      ↓  
Status Update (Etcd)


Once we execute the kubectl apply command, the Kubernetes API server validates
the YAML configuration.
Then, the API server prepares the API request.
Next, it performs authentication and authorization, followed by object validation.
After that, the configuration is stored in etcd.
Then, the kube-controller is triggered.
The kube-scheduler schedules the pod, and the kubelet creates the pod on the assigned node.
Finally, the pod status is updated in etcd.


```


### What happens when we execute the kubectl delete command?

```plaintext
kubectl delete pod nginx  
      ↓  
Pod Record in ETCD Updated with DeletionTimestamp and DeletionGracePeriodSeconds  
      ↓  
Endpoint Controller Checks Pod Termination  
      ↓  
Remove Pod from Associated Services  
      ↓  
Remove Endpoint from Objects  
      ↓  
Kubelet Notified of Pod Update (Terminating)  
      ↓  
PreStop Hook Execution  
      ↓  
Graceful Shutdown Period  
      ↓  
Force Stop Container  
      ↓  
Pod Removed from ETCD  


```


## What happens when we execute the `kubectl set image` Command?

```

kubectl: Sends the request.  
  ↓  
API Server: Validates and updates the Deployment.  
  ↓  
etcd: Stores the updated state.  
  ↓  
Controller Manager: Manages ReplicaSets and scaling.  
  ↓  
Scheduler: Assigns Nodes to new Pods.  
  ↓  
Kubelet: Manages Pods on Nodes.  
  ↓  
Container Runtime: Pulls and runs the container.  
  ↓  
Kube Proxy: Updates networking.  
  ↓  
Deployment Controller: Ensures a smooth rollout.  

```






𝐖𝐡𝐚𝐭 𝐡𝐚𝐩𝐩𝐞𝐧𝐬 𝐰𝐡𝐞𝐧 𝐰𝐞 𝐫𝐮𝐧 𝐤𝐮𝐛𝐞𝐜𝐭𝐥 𝐝𝐞𝐥𝐞𝐭𝐞 𝐩𝐨𝐝 𝐜𝐨𝐦𝐦𝐚𝐧𝐝? 
-------------------------------------------------
| No. | **Action/Step**                                                                                   | **Description**                                                                                                                                 |
|-----|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | **Kubectl Delete Pod Action**                                                                      | The pod record in etcd will be updated by the API Server with two fields: `deletionTimestamp` and `deletionGracePeriodSeconds`.                 |
| 2   | **Endpoint Controller Checks Pod Termination**                                                     | The endpoint controller checks if the pod has reached the 'terminating state'.                                                                  |
| 3   | **Remove Pod from Associated Services**                                                            | Once the pod reaches the terminating state, the endpoint is removed from the associated services to prevent external traffic.                  |
| 4   | **Remove Endpoint from Objects**                                                                   | The endpoint starts getting removed from objects like Kube-proxy, IPtables, Ingress, CoreDNS, and all others that hold endpoint information.    |
| 5   | **Kubelet Notified of Pod Update (Terminating)**                                                   | Kubelet is notified when the pod is updated to 'Terminating' state.                                                                             |
| 6   | **PreStop Hook Execution**                                                                         | If the `preStop` hook exists, it will be executed. If not, the kubelet immediately sends a SIGTERM signal to the main container.                |
| 7   | **Graceful Shutdown Period**                                                                       | The container is allowed to gracefully shut down for a period determined by `terminationGracePeriodSeconds` (default: 30 seconds).              |
| 8   | **Force Stop Container**                                                                           | After the graceful shutdown period, the container is forcibly stopped if not already terminated.                                                |
| 9   | **Pod Removed from ETCD**                                                                          | Finally, the API Server removes the pod from ETCD completely after termination.                                                                 |





## What happens when we execute `kubectl apply -f nginx.yml`
-------------------------------------------------------

| No. | Step Description                                                                                          |
|-----|----------------------------------------------------------------------------------------------------------|
| 1   | **Command Execution:** The `kubectl` CLI parses the command and reads the `nginx.yml` file.              |
| 2   | **YAML Validation:** The file is validated for correct syntax and structure according to Kubernetes API specs. |
| 3   | **API Request Preparation:** `kubectl` converts the YAML file into a JSON payload for the Kubernetes API server. |
| 4   | **Authentication and Authorization:** The API server verifies the user’s credentials (via kubeconfig) and checks permissions (RBAC). |
| 5   | **Object Validation:** The API server validates the resource specifications, such as ensuring required fields are present. |
| 6   | **Etcd Write:** The API server writes the resource configuration to etcd, the Kubernetes cluster's key-value store. |
| 7   | **Controller Trigger:** Relevant Kubernetes controllers (e.g., Deployment, ReplicaSet) detect changes and start reconciling the desired state. |
| 8   | **Pod Scheduling:** The Scheduler assigns Pods (if applicable) to appropriate nodes based on resource availability and constraints. |
| 9   | **Pod Creation:** The kubelet on the target node pulls the required container images (e.g., `nginx`) and starts the containers. |
| 10  | **Status Update:** The API server updates the resource status in etcd, and `kubectl` fetches the status to display output to the user. |




| Optimization Step | Description |
|------------------|------------|
| 1. Use a smaller base image | Choose a lightweight base image like `alpine` to reduce image size and improve security. |
| 2. Minimize layers | Combine commands using `&&` and use multi-line `RUN` statements to reduce the number of image layers. |
| 3. Use `.dockerignore` | Exclude unnecessary files (like `node_modules`, `.git`, or logs) from the Docker build to speed up the process. |
| 4. Leverage multi-stage builds | Use multi-stage builds to keep only the necessary files in the final image, reducing size and improving performance. |
| 5. Set a fixed `CMD` or `ENTRYPOINT` | Define a default command or entrypoint to ensure the container runs as expected without manual intervention. |




## Multi-Stage Docker Images (Simple Version)

| **#** | **Aspect**            | **Simple Explanation**                                                                 |
|------:|------------------------|----------------------------------------------------------------------------------------|
| 1     | **Smaller Images**     | Only needed files are kept in the final image, making it lighter and faster to use.   |
| 2     | **Faster Builds**      | Docker reuses unchanged parts of the build, so rebuilding is quicker.                 |
| 3     | **More Secure**        | Unnecessary tools are removed from the final image, reducing security risks.          |
| 4     | **Cleaner Structure**  | Each stage does one job (like build or package), keeping the Dockerfile neat.         |
| 5     | **Quick Summary**      | Multi-stage builds make your image smaller, safer, and faster, with a clean structure. |








Kubernetes Platform Speficiation
----------------------------------


| **Key Feature**                                      | **Description**                                                                                          |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Continuous Development, Integration, and Deployment** | Streamlines the development lifecycle by automating build, test, and deployment processes.               |
| **Containerized Infrastructure**                    | Applications run in isolated containers, ensuring consistency and portability across environments.      |
| **Application-Centric Management**                  | Focuses on managing applications rather than individual servers or infrastructure components.           |
| **Auto-Scalable Infrastructure**                    | Automatically scales infrastructure resources up or down based on workload demands.                     |
| **Environment Consistency Across Development, Testing, and Production** | Ensures that environments remain identical, minimizing "works on my machine" issues.                     |
| **Loosely Coupled Infrastructure**                  | Each component operates independently, allowing for easier maintenance and updates.                     |
| **Higher Density of Resource Utilization**          | Optimizes resource usage by running multiple containers on the same infrastructure.                     |
| **Predictable Infrastructure**                     | Provides reliable and repeatable infrastructure deployments, reducing manual intervention.              |


##Docker Image
-------------
A Docker image is a lightweight, standalone, and executable software package 
that includes everything needed to run an application, such as code, runtime, libraries, 
and dependencies.

| **Aspect**            | **Docker Image**                                                                                         | **Docker Container**                                                                |
|-----------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Definition**         | A lightweight, immutable package that contains everything needed to run an application (code, runtime, libraries, etc.). | A running instance of a Docker image.                                               |
| **State**              | Static — it doesn’t change once created.                                                                | Dynamic — its state can change while running.                                       |
| **Purpose**            | Used as a blueprint to create containers.                                                               | Executes the application or service defined in the image.                           |
| **Storage**            | Stored on disk as a read-only layer.                                                                    | Adds a writable layer on top of the image for runtime changes.                      |
| **Lifecycle**          | Persists until manually deleted.                                                                        | Exists while running, and disappears when stopped or removed (unless restarted).    |





CloudTrail vs AwsConfig
-------------------------

| Service      | Purpose                                                    |
|--------------|------------------------------------------------------------|
| CloudTrail   | Tracks API activity and records event history for auditing. |
| AWS Config   | Monitors and evaluates resource configurations for compliance. |



Ansible Role
--------------
Ansible role is a reusable, structured way to organize automation tasks into separate directories, including variables, files, templates, and handlers. 
It simplifies and standardizes playbook creation for managing complex environments









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

| **Feature**              | **ConfigMaps**                                                                 | **Secrets**                                                                 |
|--------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Purpose**              | Stores non-sensitive configuration data as key-value pairs.                   | Stores sensitive data like passwords, tokens, and keys.                     |
| **Sensitivity**          | Intended for non-sensitive information.                                       | Specifically designed for sensitive information.                            |
| **Usage**                | Used as environment variables, CLI args, or config files via volumes.         | Used as environment variables or mounted as files for secure configurations.|
| **Storage Location**     | Stored in `etcd`.                                                              | Stored in `etcd` and cached in `tmpfs` on nodes.                            |
| **Updates**              | Updates are reflected without pod restarts in most cases.                     | Manual action (e.g., pod restart) required to reflect changes.             |
| **Security Concerns**    | Minimal, since data is non-sensitive.                                         | Requires strict access controls due to sensitive nature.                    |




## Comparison of ABAC and RBAC in Kubernetes

| **Feature**              | **ABAC (Attribute-Based Access Control)**                                                   | **RBAC (Role-Based Access Control)**                                                         |
|--------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Definition**           | Access is granted based on attributes of the user, resource, and action.                    | Access is granted based on roles assigned to users or groups.                               |
| **Configuration Method** | Requires editing files on the master node and restarting the API server.                    | Managed through Kubernetes-native resources via `kubectl` or the API.                       |
| **Policy Management**    | Static and file-based, requiring manual intervention.                                       | Dynamic and declarative using Roles and Bindings.                                           |
| **Ease of Use**          | Complex and less user-friendly, especially at scale.                                        | Simple, flexible, and well-integrated with Kubernetes.                                      |
| **Scalability**          | Poor scalability due to manual processes.                                                   | Highly scalable with dynamic configuration.                                                 |
| **Security**             | Higher risk due to master node access for policy changes.                                   | Safer with no need for direct access to the control plane.                                  |




## Persistent Volumes in Kubernetes

| **Feature**              | **Description**                                                                                      |
|--------------------------|------------------------------------------------------------------------------------------------------|
| **Definition**           | Persistent Volumes (PVs) abstract storage resources that exist independently of pod lifecycles.     |
| **Purpose**              | Provides durable, long-lasting storage unaffected by pod restarts, deletions, or recreations.       |
| **Binding**              | Users create Persistent Volume Claims (PVCs) to bind and access PVs in their pods.                  |
| **Reclamation Policy**   | Defines behavior when a volume is released: `Retain` or `Delete`.                                   |
| **Flexibility**          | Supports various backends like NFS, iSCSI, AWS EBS, GCE PD, and more.                               |





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



| **Parameter**     | **Description**                                               |
|-------------------|---------------------------------------------------------------|
| **maxSurge**      | The maximum number of new pods that will be created at a time. |
| **maxUnavailable**| The maximum number of old pods that will be deleted at a time.|

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

| **Step** | **Description**                                                                                          |
|----------|----------------------------------------------------------------------------------------------------------|
| **1.**   | Taints apply at node level, allowing a node to repel a set of pods.                                       |
| **2.**   | Tolerations are applied to pods, and allow the pods to schedule onto nodes with matching taints.         |
| **3.**   | Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes.      |
| **4.**   | Taints and tolerations are only meant to restrict nodes to accept certain pods.                           |



## NodeSelector vs Affinity vs Anti-Affinity

| **Aspect**           | **NodeSelector**                                              | **Affinity**                                                     | **Anti-Affinity**                                                 |
|----------------------|---------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| **Purpose**           | Ensures pods are scheduled on specific nodes based on labels. | Allows more flexible rules to control pod placement using expressions. | Ensures pods are not scheduled on nodes with specific conditions. |
| **Syntax**            | Uses simple key-value pair syntax.                           | Uses a more expressive and flexible set of rules with operators. | Similar to affinity, but negates pod placement.                  |
| **Granularity**       | Basic and rigid; only supports exact matches on node labels. | More granular; supports soft (preferred) or hard (required) constraints. | More granular; allows specifying "required" or "preferred" constraints for anti-affinity rules. |

## requiredDuringSchedulingIgnoredDuringExecution vs preferredDuringSchedulingIgnoredDuringExecution

| **Aspect**                          | **requiredDuringSchedulingIgnoredDuringExecution**                            | **preferredDuringSchedulingIgnoredDuringExecution**                          |
|-------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Behavior**                        | Specifies hard constraints that must be met for scheduling the pod. If the conditions are not met, the pod will not be scheduled. | Specifies soft constraints. The scheduler will try to meet the conditions, but the pod can still be scheduled if they are not met. |
| **Impact on Scheduling**            | The pod cannot be scheduled if the required conditions are not satisfied.   | The pod can still be scheduled even if the preferred conditions are not fully met. |




## Labels vs Annotations

| **Aspect**            | **Labels**                                                | **Annotations**                                             |
|-----------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| **Purpose**           | Attach semantic tags to objects, marking them as part of a group. | Attach arbitrary key-value information to objects.         |
| **Use Case**          | Used by services to route traffic requests to backend pods. | Used for storing less structured data, such as metadata.   |
| **Format**            | Key-value pairs.                                          | Key-value pairs, but more flexible and free-form.           |
| **Multiplicity**      | Each unit can have multiple labels, but only one entry per key. | Can have multiple annotations for each object.             |
| **Storage**           | Typically used for grouping or organizing objects in a meaningful way. | Used for attaching additional, often non-critical data.    |
| **Length and Size**   | Labels are typically short, with a strict format.         | Annotations can be longer and more detailed.               |
| **Efficiency**        | Lightweight, used for identifying and selecting objects for grouping. | Can store larger amounts of data, typically non-critical.  |






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


## Comparison of Namespace Selector, IP Selector, and Pod Selector

| **Aspect**                | **Namespace Selector**                                                | **IP Selector**                                                      | **Pod Selector**                                                      |
|---------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| **Purpose**                | Selects resources within specific namespaces.                         | Selects resources based on the IP addresses of the pods or nodes.    | Selects resources based on labels assigned to pods.                  |
| **Command/Usage**          | Used in Network Policies to select namespaces.                       | Used in network policies or services to select resources by IP.      | Used in services, deployments, or network policies to select pods.    |
| **Example**                | `namespaceSelector: {matchLabels: {env: production}}`                 | `ipBlock: {cidr: "10.0.0.0/24", except: ["10.0.0.5/32"]}`           | `podSelector: {matchLabels: {app: myapp}}`                           |


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


## Comparison of docker export, docker save, and docker commit

| **Aspect**                 | **docker export**                                          | **docker save**                                              | **docker commit**                                              |
|----------------------------|-----------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------|
| **Purpose**                 | Exports the filesystem of a container as a tarball.       | Saves an image to a tarball file for distribution or backup. | Creates a new image from a container's changes.                |
| **Command**                 | `docker export <container_id> > <filename>.tar`           | `docker save -o <filename>.tar <image_name>`                 | `docker commit <container_id> <new_image_name>`                |
| **Data Included**           | Only includes the filesystem of the container (no metadata or history). | Includes the image layers, metadata, and tags.               | Captures the changes made to a container, including files and environment variables. |





ENTRYPOINT VS CMD
------------------

| **Attribute**                             | **ENTRYPOINT**                                          | **CMD**                                               |
|-------------------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| **Purpose**                               | Invoke executable service when the container is started. | Specifies the arguments which get passed to the ENTRYPOINT. |
| **Command Line Overwrite**                | Command and parameters will not be overwritten from the command line. | Default command and/or parameters, which can be overwritten from the command line. |
| **Syntax Example**                        | `ENTRYPOINT ["executable"]`                             | `CMD ["executable", "arg1", "arg2"]`                   |



## Pause Container: Key Points

| **Feature**            | **Explanation**                                                                 |
|------------------------|----------------------------------------------------------------------------------|
| **Namespace Holder**   | It holds shared settings (like network and PID) for all containers in a Pod.    |
| **First to Start**     | Kubernetes starts the pause container first when creating a Pod.                |
| **Networking Role**    | It sets up the Pod’s network and gives all containers the same IP address.      |
| **Lightweight**        | It's very small and runs a simple process like `sleep`, using minimal resources.|
| **Stability Provider** | It keeps network and settings stable even if other containers restart.          |









                    |

## Comparison of Docker Volumes and Storage Drivers

| **Aspect**         | **Docker Volumes**                                                                                      | **Storage Drivers**                                                                                  |
|--------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Purpose**        | Persist and share data between containers, independent of container lifecycle.                         | Handle how Docker stores and manages images and container layers on the host filesystem.              |
| **Persistence**    | Data persists even after container deletion; stored outside the container filesystem.                  | Data persists based on the underlying filesystem managed by the storage driver.                       |
| **Mounting**       | Can be mounted into one or more containers; enables data sharing with host.                            | Not directly mountable; works behind the scenes to manage layered storage.                            |
| **Configuration**  | Configured using `-v` flag or through Docker Compose volumes section.                                  | Configured during Docker installation or daemon start; not typically modified by users.               |
| **Examples**       | Use for persisting DB data, configs, logs. Example: `docker run -v data:/app/data myimage`.            | Common drivers: `overlay2`, `aufs`, `btrfs`, managed automatically by Docker.                         |



## Comparison of Docker Storage Drivers

| **Driver**  | **Key Features**                                                                                       | **Performance**                                               | **Compatibility & Notes**                                                                 |
|-------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **overlay2**| Uses a layered filesystem; preferred and default in most modern Docker installations.                  | Efficient with lower inode usage; great for most workloads.   | Recommended for modern Linux kernels (4.x+); replaces `aufs`.                            |
| **aufs**    | Advanced multi-layered unification filesystem supporting many writable branches.                       | Good performance but higher inode and memory usage.           | Deprecated in favor of `overlay2`; requires extra kernel module installation.            |
| **btrfs**   | Copy-on-write, snapshots, checksums, and built-in volume management.                                   | Rich features, but performance varies with kernel support.    | Requires specific kernel support; good for advanced use cases needing snapshots.         |
| **zfs**     | Advanced filesystem with compression, snapshots, cloning, and error correction.                        | High performance with rich data integrity features.           | Not included in mainline Linux; often used in enterprise setups; needs manual setup.     |



In summary, Docker volumes are a high-level abstraction for persisting data across containers, providing a convenient and flexible way to manage data. 

Storage drivers, on the other hand, are lower-level components that interface with the host's storage system to implement the storage and retrieval of container filesystem layers. 
The choice of storage driver can impact performance, compatibility, and behavior of Docker on the host system.



















𝑯𝒐𝒘 𝒕𝒐 𝒊𝒏𝒄𝒓𝒆𝒂𝒔𝒆 𝒕𝒉𝒆 𝒅𝒆𝒇𝒂𝒖𝒍𝒕 𝒑𝒐𝒅 𝒍𝒊𝒎𝒊𝒕?
------------------------------
It is possible to bypass the required pod limit by passing it to the field max-pods in the Kubernetes configuration file.
$KUBELET_EXTRA_ARGS — max-pods=240


## Ensuring that your pods remain available even if the Kubernetes API server goes down 
--------------------------------------------------------------------------------------------

| **#** | **Strategy**                                                  | **Description**                                                                                                                                                                     |
|-------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | **Use Local Kubelet Cache**                                   | Configure kubelet on each node to cache Kubernetes resources locally, allowing pods to continue running even if the API server becomes temporarily unavailable.                      |
| 2     | **Node-Level Resilience**                                     | Ensure that nodes are resilient to API server failures, allowing them to manage pod lifecycle operations even when disconnected from the API server.                                 |
| 3     | **Deploy Workloads with --kubelet-preferred-address-types=InternalIP Flag** | Use the `--kubelet-preferred-address-types=InternalIP` flag to instruct the kubelet to use the internal IP address for communication, bypassing the API server when unavailable.     |
| 4     | **Use Pod Disruption Budgets (PDBs)**                         | Implement Pod Disruption Budgets to ensure a minimum number of pods remain available during disruptions, even if the API server is down.                                             |
| 5     | **Tolerate API Server Failures in Application Design**        | Design applications to tolerate API server failures, with features like retry logic, local data caching, and circuit breakers for intermittent communication failures.                |
| 6     | **Implement Multi-Region or Multi-AZ Clusters**               | Deploy multi-region or multi-AZ clusters to improve resilience, spreading workloads across multiple zones or regions to minimize the impact of API server failures.                   |
| 7     | **Monitor and Auto-Recover**                                  | Implement monitoring and alerting (e.g., Prometheus, Grafana) to detect API server failures quickly and use automated recovery mechanisms for restarting or failover to standby instances. |








## You are tasked with deploying an Nginx application using Kubernetes
------------------------------------------------------------------------
 
| **Step** | **Command**                                                                 | **Description**                                                                                          |
|----------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **1. Create Deployment (no resources)**                                      | `kubectl create deployment nginx-deploy --image=nginx:1.16 --dry-run=client -o yaml > deploy.yaml`         | Creates a deployment YAML file without creating resources in the cluster.                                  |
| **2. Apply Deployment**                                                      | `kubectl apply -f deploy.yaml --record`                                                                  | Applies the deployment to the cluster and records the rollout history.                                    |
| **3. Check Rollout History**                                                 | `kubectl rollout history deployment nginx-deploy`                                                        | Displays the rollout history of the `nginx-deploy` deployment.                                            |
| **4. Update Deployment Image**                                               | `kubectl set image deployment/nginx-deploy nginx=nginx:1.17 --record`                                    | Updates the deployment to use the `nginx:1.17` image and records the change.                             |
| **5. Display Updated Rollout History**                                       | `kubectl rollout history deployment nginx-deploy`                                                        | Displays the updated rollout history of the `nginx-deploy` deployment after the image update.            |
| **6. Rollback to Previous Version**                                          | `kubectl rollout undo deployment/nginx-deploy --to-revision=1`                                           | Rolls back the deployment to the previous version (nginx:1.16).                                           |


| **Step** | **Task**                                                                                       | **Command**                                                                                                          |
|----------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **1.**   | **Create a service messaging-service to expose the messaging application within the cluster on port 6379** | `kubectl expose po messaging --port=6379 --name=messaging-service`                                                 |
| **2.**   | **Create a deployment named hr-web-app using the image kodekloud/webapp-color with 2 replicas**  | `kubectl expose po messaging --port=6379 --name=messaging-service`                                                 |
| **3.**   | **Create a static pod named static-busybox on the controlplane node using the busybox image with the command sleep 1000** | `kubectl run po static-busybox --image=busybox --command sleep 1000`                                                |
| **4.**   | **Expose the hr-web-app created in the previous task as a service named hr-web-app-service, accessible on port 30082 on the nodes of the cluster** | `kubectl expose deployment hr-web-app --type=NodePort --port=8080 --targetPort=30080 --name=hr-web-app-service`     |




# Kubernetes Tasks and Solutions

| **Task** | **Command(s)** |
|---------|----------------|
| **1. Create an nginx pod** | `kubectl run nginx-resolver --image=nginx` |
| **2. Expose the nginx pod as a service on port 80** | `kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP` |
| **3. Use busybox to get DNS details of nginx service** | `kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service` |
| **4. Redirect DNS lookup output to a file** | `kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service > /root/CKA/nginx.svc` |
| **5. Get pod IP address and run DNS lookup on it** | `kubectl get pod nginx-resolver -o wide`<br>`kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup <P-O-D-I-P.default.pod> > /root/CKA/nginx.pod` |
| **6. Get list of nodes in JSON format and save to file** | `kubectl get nodes -o json > /opt/outputs/nodes-z3444kd9.json` |
| **7. Get Internal IPs of all nodes** | `kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}' > /root/CKA/node_ips` |
| **8. Get osImages of all nodes using JSONPath** | `kubectl get nodes -o=jsonpath='{.items[*].status.nodeInfo.osImage}' > /opt/outputs/nodes_os_x43kj56.txt` |











```

for i in {1..35}; do
   kubectl exec --namespace=kube-public curl -- sh -c 'test=`wget -qO- -T 2  http://webapp-service.default.svc.cluster.local:8080/info 2>&1` && echo "$test OK" || echo "Failed"';
   echo ""
done

```






Autoscale app
---------------

## Commands for Setting Up and Scaling Applications

| **Command**                                                                                               | **Explanation**                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git clone https://github.com/monitor-ops/metric-server.git`                                               | Clone the Metric Server repository from GitHub.                                                                                                            |
| `kubectl apply -f metric-server`                                                                            | Apply the Metric Server configuration to the Kubernetes cluster.                                                                                          |
| `kubectl run hpa-nginx --image=nginx --requests=cpu=200m --expose --port=80`                              | Create an nginx deployment with CPU resource requests and expose it on port 80.                                                                            |
| `kubectl autoscale deployment hpa-nginx --cpu-percent=50 --min=1 --max=10`                                 | Enable Horizontal Pod Autoscaling (HPA) for the `hpa-nginx` deployment, with CPU-based autoscaling and replica limits.                                     |
| `kubectl describe deployment/hpa-nginx`                                                                   | Describe the details of the `hpa-nginx` deployment, including the scaling configuration.                                                                 |
| `kubectl describe hpa`                                                                                   | Display the details of the Horizontal Pod Autoscaler (HPA) resource.                                                                                      |
| `kubectl run tomcat --image=tomcat:8.0 --replicas=1`                                                      | Create a Tomcat deployment with one replica.                                                                                                               |
| `apt-get update`                                                                                          | Update the list of available packages in the apt repository.                                                                                              |
| `apt-get install curl wget net-tools telnet netcat dnsutils iputils-ping apach2-utils`                    | Install useful networking and diagnostic tools in the system.                                                                                             |
| `nslookup kubernetes.default.svc.cluster.local`                                                           | Perform DNS lookup to resolve the Kubernetes service address for `kubernetes.default.svc.cluster.local`.                                                    |
| `while true; do curl -I http://hpa-nginx/; done`                                                          | Continuously send HTTP requests to the `hpa-nginx` service and output the response headers.                                                              |
| `while true; do ab -n 1000 -c 2 http://hpa-nginx/; done`                                                  | Continuously send HTTP requests using Apache Benchmark (`ab`) to test the load performance of the `hpa-nginx` service with 1000 requests and 2 concurrency. |




Kubeconfig and use context
----------------------------

1. kubectl config view
2. kubectl config use-context cluster1-context
3. export  KUBECONFIG=/opt/play/kubeconfig
4. kubectl config get-contexts
5. kubectl config use-context admin@cluster2
6. openssl x509 -in /etc/kubernetes/pki/ca.crt -text -noout
7. kubectl config view --kubeconfig my-kube-config
8. kubectl config current-context --kubeconfig my-kube-config
9. kubectl config --kubeconfig=/root/my-kube-config use-context research
10. 



I would like to use the dev-user to access test-cluster-1. Set the current context to the right one so I can do that.


Once the right context is identified, use the kubectl config use-context command.





## Three Tier Setup on K8s
------------------------------

| **Tier**         | **Components**                                      | **Description**                                                                                       |
|-------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Presentation**  | - React App (Frontend)                             | - Hosted in a Kubernetes Deployment. <br> - Served via an Ingress Controller (e.g., ALB or NGINX). <br> - Static files (HTML, CSS, JS) often stored in an S3 bucket and cached by CloudFront for performance. |
| **Application**   | - Node.js/Express Backend (API Layer)              | - Hosted in a Kubernetes Deployment as microservices. <br> - Scales based on traffic using Horizontal Pod Autoscaler (HPA). <br> - Exposes APIs consumed by the React app. |
| **Data**          | - RDS PostgreSQL <br> - DynamoDB (NoSQL)           | - RDS handles relational data such as user information, authentication. <br> - DynamoDB used for fast key-value lookups like session management or product catalogs. |
| **Common Services** | - Prometheus & Grafana <br> - Fluentd/CloudWatch Logs | - Monitoring and alerting with Prometheus and Grafana. <br> - Centralized logging using Fluentd or CloudWatch. |


## Static Pod
----------------


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







## Backup, and Restore By Velero
----------------------------------------------------

| **Command**                                                                                               | **Explanation**                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `wget https://github.com/vmware-tanzu/velero/releases/download/v1.9.0/velero-v1.9.0-linux-amd64.tar.gz`     | Download the Velero v1.9.0 release for Linux.                                                                                                               |
| `tar -xf velero-v1.9.0-linux-amd64.tar.gz`                                                                 | Extract the Velero tarball.                                                                                                                                  |
| `cp velero /usr/bin`                                                                                        | Copy the `velero` binary to the `/usr/bin` directory for easy execution from anywhere.                                                                     |
| `chmod 777 /usr/bin/velero`                                                                                 | Grant full permissions to the `velero` binary.                                                                                                            |
| `velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.0.1 --bucket valero-backup-123 --backup-location-config region=us-east-1 --snapshot-location-config region=us-east-1 --secret-file /root/.aws/credentials` | Install Velero with AWS provider and configure the backup and snapshot locations with AWS plugin and credentials.                                         |
| `kubectl get all -n velero`                                                                                 | List all resources in the `velero` namespace.                                                                                                             |
| `kubectl describe po velero-7577d46b56-x9phw -n velero`                                                    | Describe the Velero pod for detailed information.                                                                                                         |
| `kubectl logs velero-7577d46b56-x9phw -n velero`                                                           | View the logs of the Velero pod.                                                                                                                           |
| `kubectl get all -n velero`                                                                                 | List all resources in the `velero` namespace again to check for changes or updates.                                                                     |
| `kubectl create namespace test`                                                                             | Create a new namespace called `test`.                                                                                                                     |
| `kubectl create deployment web --image=gcr.io/google-samples/hello-app:1.0 -n test`                         | Create a new deployment `web` in the `test` namespace with a sample hello-app image.                                                                    |
| `kubectl create deployment nginx --image=nginx -n test`                                                    | Create a new `nginx` deployment in the `test` namespace.                                                                                                 |
| `velero backup create test1 --include-namespaces test`                                                     | Create a backup named `test1` that includes the `test` namespace.                                                                                         |
| `velero backup describe test1`                                                                              | Describe the `test1` backup to view its status and details.                                                                                             |
| `kubectl delete namespace test`                                                                             | Delete the `test` namespace to simulate a recovery scenario.                                                                                              |
| `kubectl get ns`                                                                                            | List the namespaces after deletion of the `test` namespace.                                                                                              |
| `velero restore create --from-backup test1`                                                                 | Restore the `test1` backup to recover the `test` namespace and its resources.                                                                            |
| `kubectl get ns`                                                                                            | List namespaces again to verify that the `test` namespace has been restored.                                                                            |


## Port Numbers
-------------


| **Kubernetes Component** | **Default Port** | **Description**                                                                                   |
|---------------------------|------------------|---------------------------------------------------------------------------------------------------|
| **Kubelet**              | 10250            | Port for Kubelet to perform health checks and communication with the Kubernetes control plane.    |
| **Kube-API Server**       | 6443             | Secure port for Kubernetes API server communication (HTTPS).                                      |
| **Kube-Scheduler**        | 10251            | Port used by the scheduler for leader election and communication.                                 |
| **Kube-Proxy**            | 10256            | Port for health and metrics endpoint for Kube-proxy.                                              |
| **Kube-Controller**       | 10252            | Port used by the controller manager for leader election and communication.                        |
| **etcd**                 | 2379             | Client communication port for etcd (key-value store).                                             |
| **etcd (Peer)**          | 2380             | Port for internal etcd cluster communication between peers.                                       |


## How to Run etcd as a service
--------------------------------

```

[Unit]
Description=etcd key-value store
Documentation=https://etcd.io
Wants=network.target
After=network.target

[Service]
User=etcd
Type=notify
ExecStart=/usr/local/bin/etcd \
  --name <NODE_NAME> \
  --data-dir=/var/lib/etcd \
  --listen-peer-urls=https://<PRIVATE_IP>:2380 \
  --listen-client-urls=https://<PRIVATE_IP>:2379,https://127.0.0.1:2379 \
  --advertise-client-urls=https://<PRIVATE_IP>:2379 \
  --initial-advertise-peer-urls=https://<PRIVATE_IP>:2380 \
  --initial-cluster=<NODE_NAME>=https://<PRIVATE_IP>:2380,<PEER_NODE_1>=https://<PEER_IP_1>:2380,<PEER_NODE_2>=https://<PEER_IP_2>:2380 \
  --initial-cluster-token=<CLUSTER_TOKEN> \
  --initial-cluster-state=new \
  --client-cert-auth \
  --trusted-ca-file=/etc/etcd/ca.crt \
  --cert-file=/etc/etcd/server.crt \
  --key-file=/etc/etcd/server.key \
  --peer-cert-auth \
  --peer-trusted-ca-file=/etc/etcd/ca.crt \
  --peer-cert-file=/etc/etcd/peer.crt \
  --peer-key-file=/etc/etcd/peer.key
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

















## Comparison b/w Cluster Autoscaler,Vertical Autoscaler and Horizontal Autoscaler
------------------------------------------------------------------------------------


| Feature                          | Cluster Autoscaler                                      | Vertical Pod Autoscaler (VPA)                      | Horizontal Pod Autoscaler (HPA)                  |
|----------------------------------|--------------------------------------------------------|---------------------------------------------------|-------------------------------------------------|
| **Purpose**                      | Scales the number of nodes in a cluster.               | Adjusts CPU/Memory for a single pod.              | Scales the number of pod replicas.              |
| **Scope**                        | Works at the node level.                               | Works at the pod level (resources).               | Works at the deployment level.                  |
| **Triggers**                     | Node resource demand (unscheduled pods).               | Resource usage (CPU/Memory).                      | CPU/Memory usage or custom metrics.             |
| **Use Case**                     | Manage overall cluster capacity.                       | Optimize resource requests/limits.                | Handle traffic/load dynamically.                |
| **Commands**                     | **Scale Nodes**:                                       | **Install VPA**:                                  | **Scale Pods**:                                 |
|                                  | ```shell                                              | ```shell                                          | ```shell                                        |
|                                  | kubectl scale nodes <node-group> --replicas=<count>    | kubectl apply -f vpa-nginx.yaml                   | kubectl autoscale deployment nginx-deployment --min=2 --max=10 --cpu-percent=80 |
|                                  | ```                                                   | **Example `vpa-nginx.yaml`:**                     | ```                                             |
|                                  | **Example:**                                          | ```yaml                                           | **Check HPA Status:**                            |
|                                  | ```shell                                              | apiVersion: autoscaling.k8s.io/v1                 | ```shell                                        |
|                                  | kubectl scale nodes my-nodegroup --replicas=5          | kind: VerticalPodAutoscaler                       | kubectl get hpa                                 |
|                                  | ```                                                   | metadata:                                         | ```                                             |
|                                  |                                                      |   name: vpa-nginx                                 |                                                 |
|                                  |                                                      | spec:                                             |                                                 |
|                                  |                                                      |   targetRef:                                      |                                                 |
|                                  |                                                      |     apiVersion: "apps/v1"                         |                                                 |
|                                  |                                                      |     kind: Deployment                              |                                                 |
|                                  |                                                      |     name: nginx-deployment                        |                                                 |
|                                  |                                                      |   updatePolicy:                                   |                                                 |
|                                  |                                                      |     updateMode: "Auto"                            |                                                 |
|                                  |                                                      | ```                                              |                                                 |








## Rolling Update and Rollout Process
------------------------------------------


| **Action**                                 | **Command**                                                                                      | **Description**                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Check Current Status of a Deployment**   | `kubectl rollout status deployment/<deployment-name>`                                           | Shows the current status of the deployment rollout, including replicas and updated pods.         |
| **Perform a Rolling Update**               | `kubectl set image deployment/<deployment-name> <container-name>=<new-image>`                  | Updates the deployment with a new image (e.g., updating nginx to a specific version).            |
|                                           | Example: `kubectl set image deployment/nginx-deployment nginx=nginx:1.21.0`                     |                                                                                                  |
| **Monitor Rollout Progress**               | `kubectl rollout status deployment/<deployment-name>`                                           | Monitors the progress of the rolling update and ensures all pods are updated successfully.       |
| **Pause a Rolling Update**                 | `kubectl rollout pause deployment/<deployment-name>`                                            | Temporarily pauses a rollout, which can be resumed later.                                        |
| **Resume a Rolling Update**                | `kubectl rollout resume deployment/<deployment-name>`                                           | Resumes a previously paused rollout.                                                            |
| **Rollback to the Previous Version**       | `kubectl rollout undo deployment/<deployment-name>`                                             | Rolls back the deployment to its previous stable state.                                         |
| **Rollback to a Specific Revision**        | `kubectl rollout undo deployment/<deployment-name> --to-revision=<revision-number>`             | Rolls back the deployment to a specific revision (if applicable).                               |
| **View Deployment Rollout History**        | `kubectl rollout history deployment/<deployment-name>`                                          | Displays the revision history of a deployment.                                                  |
| **Force Restart a Deployment**             | `kubectl rollout restart deployment/<deployment-name>`                                          | Restarts all the pods in the deployment without changing the image.                              |







Observability
----------------

| No. | Aspect            | Description                                                                                                      |
|-----|-------------------|------------------------------------------------------------------------------------------------------------------|
| 1   | **Definition**     | Observability refers to the ability to measure and understand the internal state of a system based on its external outputs. |
| 2   | **Features**       | - **Metrics**: Quantitative data about system performance (e.g., CPU usage, memory consumption).<br>- **Logs**: Detailed records of events and activities within a system.<br>- **Traces**: Tracks the flow of requests through the system, allowing identification of bottlenecks and performance issues.<br>- **Alerts**: Automated notifications triggered by certain predefined thresholds or anomalies. |
| 3   | **Benefits**       | - **Improved Performance**: Helps identify bottlenecks and performance degradation in real-time.<br>- **Faster Issue Resolution**: Logs and traces help pinpoint issues, reducing debugging time.<br>- **Proactive Monitoring**: Alerts notify teams of issues before they impact users.<br>- **Better User Experience**: By ensuring system health, observability contributes to more reliable services.<br>- **Optimized Resource Utilization**: Insights from metrics can guide capacity planning and scaling decisions. |










```mermaid
graph TD
  User -->|Requests| Route53[Route 53]
  Route53 -->|DNS Routing| ALB[ALB Ingress]
  ALB -->|TLS Termination| CertManager[Cert Manager]
  ALB -->|Load Balancing| ReactApp[React Application]
  ReactApp -->|APIs| Backend
  Backend -->|Queries| RDS[(RDS PostgreSQL)]
  Backend -->|Lookups| DynamoDB[(DynamoDB)]
  Backend -->|Secrets| SecretsManager[Secrets Manager]

  subgraph Certificate Management
    CertManager --> ALB
    CertManager --> Route53
  end

  subgraph Secrets Management
    SecretsManager -->|Provides| Backend
    SecretsManager -->|RDS Credentials| RDS
  end





```
```
Core Concepts (13%)
Multi-Container Pods (10%)
Pod Design (20%)
State Persistence (8%)
Configuration (18%)
Observability (18%)
Services and Networking (13%)
```




18. Tell all the scenarios too implement the security in Kubernetes.

## Kubernetes Security Best Practices

| **Category**              | **Practice**                                                                                                                                      |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Authentication & Access** | - Use **RBAC**: `kubectl create role`, `kubectl create rolebinding` <br> - Limit **service account** permissions <br> - Enable OIDC or token-based auth |
| **Secrets Management**    | - Use **Kubernetes Secrets**: `kubectl create secret` <br> - Use **HashiCorp Vault**, **AWS Secret Manager**, or **Google Secret Manager** <br> - Integrate **External Secrets Operator** <br> - Enable etcd encryption: `--encryption-provider-config` |
| **Certificates & Keys**   | - Use **cert-manager** for automatic TLS certs <br> - Set up **key rotation** and **cert rotation** policies <br> - Enforce TLS via Ingress annotations |
| **Network Security**      | - Enforce **Network Policies**: `kubectl apply -f netpol.yaml` <br> - Use **Service Mesh (Istio)** for mTLS <br> - Secure Ingress with **TLS** and **modsecurity** |
| **Container & Image**     | - Scan with **Trivy**: `trivy image nginx:latest` <br> - Sign/verify with **Cosign**: `cosign sign` <br> - Use `readOnlyRootFilesystem: true` in PodSpec |
| **Policy Enforcement**    | - Enforce policies with **Kyverno** or **OPA Gatekeeper** <br> - Deny privileged pods: `kubectl apply -f deny-privileged.yaml` |
| **Monitoring & Logging**  | - Use **Prometheus + Grafana** for metrics and alerts <br> - Aggregate logs with **ELK Stack** or **Fluentd** <br> - Alert on anomalies and audit events |
| **Cost Visibility**       | - Use **Kubecost** to monitor resource usage and control spend <br> - Set budgets and track overprovisioning |
| **Vulnerability Testing** | - Run **kube-hunter** for pen testing <br> - Test resilience with **Kube-monkey** <br> - Review audit logs and scan RBAC with `audit2rbac` |
| **Patching & Upgrades**   | - Use `kubectl drain` + `kubectl cordon` for safe node upgrades <br> - Automate image updates with **FluxCD** or **ArgoCD** <br> - Patch regularly: `kubectl rollout restart deploy` |







































































# Architecture Diagram

![Architecture Diagram](diagram/e1.png)



