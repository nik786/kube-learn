
Question 1: In Linux, the Nice command is used to prioritize the execution of processes.
a. Tell me more about it and if given a choice where do you think it will be useful in your existing project ?

 the nice command provides a flexible mechanism for managing process priorities and optimizing 
 system resource utilization in Unix-like operating systems. 
 It helps ensure fair allocation of CPU time and improves overall system responsiveness.



| **Topic**                                 | **Description**                                                                                                                                                                                                                                                                                              |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nice Command in Linux**                 | The `nice` command in Unix-like operating systems (including Linux) is used to adjust the priority of processes by setting a "niceness" value. Higher niceness values lower the priority of a process, while lower values (even negative) increase its priority.                                             |
| **Functionality**                         | The `nice` command modifies the process's priority, allowing system resources (like CPU) to be allocated more fairly among running processes. This is useful for managing background tasks, like batch jobs, without hindering the performance of interactive or foreground tasks.                            |
| **Usage Example**                         | Running a CPU-intensive task, such as compressing a file with gzip, with a lower priority: <br> `nice -n 10 gzip large_file.txt` <br> This ensures that the task consumes fewer CPU resources and other processes have more CPU time, maintaining system responsiveness.                                       |
| **Batch Job Management**                  | `nice` is useful in batch job management, where tasks are scheduled to run during periods of low system load. By reducing the priority of these jobs, they don't interfere with more critical, interactive workloads.                                                                                          |
| **Load Average**                          | Load average is the measure of the average number of processes waiting for CPU over a specified time period (1, 5, and 15 minutes). It helps in understanding system load and can signal if resources need to be upgraded or workloads need optimization.                                                    |
| **Key System Metric**                     | Load average is an indicator of how busy the system is. A high load average suggests that the system is overburdened and might need resource scaling or optimization of workloads to prevent bottlenecks.                                                                                                    |
| **Prioritizing Workloads in Docker & Kubernetes** | In Docker and Kubernetes, while there is no direct equivalent of the `nice` command, prioritizing workloads can be done using resource allocation and scheduling techniques.                                                                                                                             |
| **Resource Requests & Limits**            | In Kubernetes, resource requests and limits allow you to specify the minimum and maximum CPU and memory allocation for containers or pods. Higher resource requests give priority to those workloads when resources are limited.                                                                                   |
| **Quality of Service (QoS) Classes**      | Kubernetes assigns QoS classes to pods based on their resource requirements and usage. Pods with "guaranteed" QoS class (higher resource requirements) are given priority over "burstable" or "best-effort" QoS pods.                                                                                          |
| **Pod Priority & Preemption**             | Kubernetes allows assigning priority classes to pods, with higher priority pods preempting lower priority ones if resources are constrained. This ensures critical workloads are scheduled first.                                                                                                              |
| **Pod Disruption Budgets (PDBs)**         | PDBs ensure that a minimum number of pods are maintained during disruptions, like node maintenance or pod evictions. Configuring PDBs for critical workloads helps prevent their disruption during these events.                                                                                              |
| **Node Affinity & Anti-affinity**         | Kubernetes allows defining rules for pod placement based on node labels (node affinity) or ensuring pods are not placed together on the same node (anti-affinity). Critical workloads can be scheduled on nodes with better resources or higher performance characteristics using node affinity.                   |
| **Custom Schedulers & Admission Controllers** | Custom schedulers or admission controllers can be developed to implement scheduling logic based on workload priorities or specific criteria, enabling tailored resource allocation and workload prioritization in Kubernetes.                                                                                  |


Question 2 : What do you know about LINUX Signals, how does Inter-Process Communication happen 
with uses of signals.
Follow-up : How is it related to Kubernetes pod status and to Docker entry points ?



| **Topic**                                | **Description**                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Linux Signals**                        | Linux signals are software interrupts used for asynchronous notifications between processes or between the kernel and processes. They notify processes of events such as errors, termination requests, or user-defined events. Signals are identified by unique integers.                                                                                                     |
| **Signal Types**                         | Signals can be generated by the kernel, another process, or the process itself. Examples include: <br> - `SIGINT`: Interrupt signal (typically generated by pressing Ctrl+C) <br> - `SIGKILL`: Termination signal <br> - `SIGUSR1`: User-defined signal                                                                                                                |
| **Signal Handling**                      | Processes can handle signals in various ways: <br> - Ignore the signal <br> - Allow the default action to occur (e.g., terminate the process) <br> - Install a signal handler that performs custom actions before the default action occurs                                                                                          |
| **Inter-Process Communication (IPC)**    | Signals can be used for basic IPC to notify one process of an event or request termination. However, they are not suited for large data exchange or synchronous communication. They are more appropriate for signaling events rather than transferring data.                                                                          |
| **Kubernetes Pod Status**               | Kubernetes manages applications in pods. Pod statuses can change based on the signals sent to processes within the pods. Examples: <br> - If a process fails or terminates unexpectedly, Kubernetes may mark the pod as `Failed` or `CrashLoopBackOff`. <br> - Signals help Kubernetes detect and handle failures or lifecycle changes in pods. |
| **Docker Entry Points**                 | Docker entry points are commands or scripts executed when a container starts. They initialize the environment, set configurations, and start the main application. <br> - Signals can be used in entry point scripts to manage the lifecycle of applications. <br> - For example, signal handlers can ensure proper cleanup during container shutdown.                |
| **Role of Signals in Kubernetes & Docker** | Signals help manage the status of Kubernetes pods and Docker containers. They are used to monitor and react to process failures or state changes within the container. <br> - In Kubernetes, signals contribute to status transitions like `CrashLoopBackOff`. <br> - In Docker, signals can ensure that containers handle termination gracefully.                        |


Question 3 :What are the kubernetes probs that you have used in your deployments, explain their 
importance and pre-requisites for each one.
Follow up:
1. What are the check mechanisms that you used while implementing the probs apart form the httpGet
2. Probs seem very useful, Why doesn't Kubernetes mandate applications to have default probs ?
startup, readiness and liveness all are optional, why ?


| **Probe Type**       | **Importance**                                                                                                                                                                                                                                                                                                                        | **Pre-requisites**                                                                                                                                                                                                                                        |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Startup Probes**    | Used to determine if a container is ready to accept traffic. Executed once after the container starts. If the probe fails, Kubernetes restarts the container. Useful for applications that require initialization time before handling requests (e.g., loading datasets). | Requires the container to expose an endpoint that Kubernetes can access. The endpoint should return a success status code (2xx or 3xx) if the application is ready to accept traffic.                |
| **Readiness Probes**  | Used to determine if a container is ready to serve traffic. Continuously executed, and if it fails, Kubernetes stops routing traffic to the container until it passes. Ensures that only healthy containers receive traffic. | Requires the container to expose an endpoint for Kubernetes to perform the check. The endpoint should return a success status code when the application is ready to serve traffic.                    |
| **Liveness Probes**   | Used to determine if a container is still running correctly. Executed periodically, and if it fails, Kubernetes restarts the container. Helps in detecting and recovering from situations where the application becomes unresponsive or deadlocked. | Requires the container to expose an endpoint for Kubernetes to perform the check. The endpoint should return a success status code if the application is still running correctly.                      |
| **Additional Check Mechanisms** | Apart from `httpGet`, Kubernetes supports other types of probes like `tcpSocket` and `exec`, allowing checks beyond HTTP endpoints, such as checking a specific TCP port or executing a custom command inside the container. | - `tcpSocket`: Check if a TCP port is open. <br> - `exec`: Execute a custom command inside the container and check the result.                                                                  |
| **Why Aren't Probes Mandated?** | - **Flexibility**: Different applications have different requirements. Mandating probes could limit flexibility. <br> - **Legacy Systems**: Some applications may not support probe endpoints. <br> - **Resource Overhead**: Continuous probing can introduce resource overhead. <br> - **Developer Responsibility**: Kubernetes gives developers the choice to implement probes. | - Probes are not mandatory to allow flexibility for different application requirements, prevent unnecessary overhead, and give developers control over their application health checks. |





Question 4 : We spoke about IPC socket or Unix domain socket in Question 2 (find that question in previous posts), 
explain how inter-process communication workflow works in Docker Architecture.
Follow up:
1. What is the role of docker.sock file ?
2. How Docker socket work ?

| **Aspect**             | **Description**                                                                                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Client-Server Architecture** | Docker follows a client-server architecture where the Docker client interacts with the Docker daemon (server) to manage containers and images.                                                             |
| **Unix Socket Communication** | The Docker client communicates with the Docker daemon using Unix domain sockets, specifically the Docker socket located at `/var/run/docker.sock`.                                                         |
| **Daemon Processing**   | Upon receiving API requests from the Docker client, the Docker daemon processes the requests and performs the required actions such as managing container lifecycle, image storage, networking, and volumes. |
| **Response Transmission** | After completing the requested actions, the Docker daemon sends responses back to the Docker client through the Docker socket. These responses include success, error messages, and status updates.        |
| **Purpose**             | The Docker socket acts as the communication channel between the Docker client and the Docker daemon, allowing users to manage Docker containers and images using client commands.                     |


Question 5 : Design a Kubernetes deployment setup where you have 3 applications that need to run in 
HA to create a solution. 
However the applications have starting and running dependencies and requirements.
a. application 1 should always start first
b. application 2 should always start after application 1 is Ready
c. application 3 should always start after application 2 is Ready
Follow up:
1. How will you design a check mechanism for the applications in such a way that restarts and schedular 
reschedules dont break the dependence requirements
2. How will you plan to incorporate such check mechanism with CD tools where deployments are gitops driven


To design a Kubernetes deployment setup with three applications running in high availability (HA) while 
ensuring proper sequencing of startup and dependencies, we can use Kubernetes Deployments along with readiness 
probes and dependencies. Here's how:

Kubernetes Deployment Setup:

Create separate Deployments for each application.
Define readiness probes for each Deployment to ensure that each application is ready to serve traffic 
before proceeding to the next one.
Dependency Management:

Ensure that application 1 is started first by configuring its Deployment with appropriate resource 
requests, readiness probes, and startup delays if necessary.
Configure the readiness probes of application 2 to check for the readiness of application 1's 
endpoints before marking itself as ready.
Similarly, configure the readiness probes of application 3 to check for the readiness of application 
2's endpoints before marking itself as ready.
Example YAML Configuration:

yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app1
  template:
    metadata:
      labels:
        app: app1
    spec:
      containers:
      - name: app1
        image: <app1_image>
        readinessProbe:
          httpGet:
            path: /health
            port: 80
        # Add additional configuration as needed

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: app2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app2
  template:
    metadata:
      labels:
        app: app2
    spec:
      containers:
      - name: app2
        image: <app2_image>
        readinessProbe:
          httpGet:
            path: /health
            port: 80
        # Add additional configuration as needed
        dependsOn:
          - condition: "Ready"
            app: app1

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: app3
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app3
  template:
    metadata:
      labels:
        app: app3
    spec:
      containers:
      - name: app3
        image: <app3_image>
        readinessProbe:
          httpGet:
            path: /health
            port: 80
        # Add additional configuration as needed
        dependsOn:
          - condition: "Ready"
            app: app2
Follow-up:

Check Mechanism for Application Dependencies:

Use readiness probes configured to check the specific endpoints of dependent applications before 
marking each application as ready.
Implement retry and backoff policies in readiness probes to handle transient failures gracefully 
and prevent unnecessary restarts or rescheduling.
Incorporating Check Mechanism with CD Tools:

Incorporate readiness probe configurations into the GitOps repository alongside the application deployment manifests.
Utilize GitOps tools like Argo CD, Flux, or Jenkins X to automatically apply changes to Kubernetes 
clusters based on changes in the Git repository.
Ensure that CD pipelines include validation steps to verify the correctness of readiness probe 
configurations and dependency requirements before applying updates to the cluster.




Question 6 : Please explain your understanding of multilayer switches and what Layer 4 LAN switching does.
Follow up:
1. Which component of Kubernetes using this technology and how ?


| **Aspect**                | **Description**                                                                                                                                                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ingress Controller**     | Responsible for managing inbound traffic to Kubernetes services, acting as a Layer 7 (application layer) load balancer that routes external traffic to appropriate services within the cluster based on Ingress resource rules.                                                                                             |
| **Layer 4 Load Balancing** | Ingress controllers often rely on Layer 4 load balancing, distributing incoming traffic across multiple backend pods or nodes. Layer 4 load balancing operates at the transport layer (TCP/UDP) and makes routing decisions based on network information such as IP addresses and port numbers. |
| **Network Policies**       | Kubernetes Network Policies define rules to control traffic between pods or services within the cluster. These policies operate at Layer 3 (network layer) and Layer 4 (transport layer), controlling traffic based on IP addresses, ports, and protocols.                                                         |
| **Service Load Balancing** | Kubernetes Services provide an abstraction for accessing groups of pods or backend instances. Service load balancing can operate at Layer 4 (TCP/UDP load balancing) and Layer 7 (HTTP load balancing) depending on the service type and configuration.                                                              |
| **Ingress Resource Routing** | Ingress resources define rules for routing external HTTP/HTTPS traffic to specific Services within the cluster. Ingress controllers implement these rules and perform Layer 7 load balancing based on HTTP/HTTPS headers and paths.                                                                                |
| **Layer 4 and Layer 7 Interaction** | While Ingress controllers primarily operate at Layer 7 for HTTP/HTTPS traffic routing, they may interact with Layer 4 load balancers or switches for distributing traffic across backend pods or nodes. This ensures efficient traffic handling and optimal utilization of cluster resources. |




Question 7 : You have 3 applications that make a solution. UI application, business application and database application. 
All the three applications are installable stand alone and connect with one another via configurations and endpoints. 
UI application needs 100MB and 1CPU, business application needs 200MB and 2CPU while the database application needs 
300MB and 3CPU for every 1000 users payload. So think of this as 1:2:3 ratio in terms of resources.


| **Infrastructure**           | **Deployment Design**                                                                                                                                                                                                                                                                                                                      | **Cost-Optimization Strategies**                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **On VM**                     | - Deploy each application on separate VM instances. <br> - Allocate resources according to the specified ratios: <br>   - UI: 100MB, 1CPU <br>   - Business: 200MB, 2CPU <br>   - Database: 300MB per 1000 users, 3CPU per 1000 users. <br> - Adjust VM instances based on resource requirements and expected user load. | - Use cost-efficient VM instance types (e.g., reserved or spot instances). <br> - Implement auto-scaling policies to scale VMs based on usage. <br> - Optimize instance sizing to avoid over-provisioning during low demand periods, minimizing costs.                                                                                                                                                       |
| **On Docker Setup**          | - Containerize each application using Docker. <br> - Define resource constraints in Docker Compose or Dockerfiles for each container to ensure ratios are maintained. <br> - Use Docker Swarm for orchestration, if needed, to manage resource allocation. | - Optimize container images to reduce resource consumption. <br> - Use Docker Swarm or Kubernetes for efficient resource management and scaling. <br> - Ensure containers are scaled according to demand to avoid idle resources.                                                                                                                                                                                                                                                                 |
| **On Kubernetes (K8s)**       | - Create Kubernetes Deployments or StatefulSets for each application. <br> - Define resource requests and limits in pod specifications. <br> - Utilize Horizontal Pod Autoscaling (HPA) for database app based on user load. <br> - Use Kubernetes scheduler to distribute pods based on available resources. | - Leverage Horizontal Pod Autoscaling (HPA) and Cluster Autoscaler for dynamic resource allocation. <br> - Implement resource quotas and limits to avoid over-provisioning. <br> - Use managed Kubernetes services (e.g., GKE, EKS, AKS) for cost-effective infrastructure and automation. <br> - Optimize pod resource allocation to balance performance and cost. |



Question 8 : One of the main activity for devops enginner is to maintain the software versions of the platform. 
However, updating platform without having a downtime or customer impact is hard to achive. How are 
you updating your platform ?
How will you design a update statergy for k8s platform.


| **Strategy**                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cluster Configuration Management** | Use IaC tools like Terraform or Kubernetes manifests to manage cluster configuration. Ensures consistency and reproducibility across updates.                                                                                                                                                                                                  |
| **Test Environment**              | Maintain a staging environment that mirrors production. Test updates thoroughly using Kubernetes e2e tests, integration tests, and chaos engineering to identify potential issues before applying them to production.                                                                                                                             |
| **Rolling Updates**               | Use Kubernetes' built-in rolling update functionality for Deployments or StatefulSets. Gradually replaces old pods with new ones while keeping the application available throughout the process.                                                                                                                                                     |
| **Canary Deployments**            | Gradually shift traffic from the old version to the new one. Monitor key metrics (latency, error rates, resource usage) during the canary phase. Rollback if issues arise before full deployment.                                                                                                                                                    |
| **Blue-Green Deployments**        | Use blue-green deployment strategy with two identical environments (blue and green). Update one environment and switch traffic to it once validated.                                                                                                                                                                                             |
| **Backup and Restore**            | Implement a backup and restore strategy. Regularly backup critical data and configurations, and periodically validate the restore process to ensure quick recovery if needed.                                                                                                                                                                    |
| **Health Checks and Probes**      | Configure readiness and liveness probes to detect and handle unhealthy containers during updates.                                                                                                                                                                                                                                           |
| **Monitoring and Observability**  | Use monitoring tools like Prometheus and Grafana to track cluster health, resource usage, and application performance. Set up alerts for anomalies during updates.                                                                                                                                                                            |
| **Rollback Plan**                 | Always have a documented rollback plan. Automate rollback procedures to minimize downtime in case of issues.                                                                                                                                                                                                                                    |
| **Incremental Updates**           | Break down updates into smaller, incremental changes to reduce the risk of catastrophic failures and simplify troubleshooting.                                                                                                                                                                                                               |
| **Compatibility Testing**         | Before upgrading Kubernetes versions, thoroughly test compatibility with plugins, network configurations, storage solutions, and other dependencies. Use tools like Kubeadm upgrade to automate and validate the upgrade process.                                                                                                                |
| **Canary Testing**                | Perform canary testing in production-like environments to ensure updates don’t break critical functionality. Monitor closely and halt/rollback if necessary.                                                                                                                                                                                      |
| **Communication and Coordination**| Ensure clear communication and coordination between developers, operators, and third-party vendors. This ensures everyone is aligned on the update process and its impact.                                                                                                                                                                      |


| **Variable** | **Description**                                                                                                                                                 |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$#`         | Stores the number of command-line arguments passed to the shell program. It represents the number of arguments.                                                 |
| `$?`         | Stores the exit value of the last executed command.                                                                                                             |
| `$0`         | Stores the first word of the entered command (the name of the shell program or script).                                                                         |
| `$*`         | Stores all the arguments entered on the command line (e.g., `$1`, `$2`, ...).                                                                                   |
| `"$@"`       | Stores all the arguments entered on the command line, each individually quoted (`"$1" "$2" ...`). `$@` expands to the positional arguments passed to a function or script. |
| `$!`         | Shows the process ID (PID) of the last background process started.                                                                                             |
| `$$`         | Displays the process ID (PID) of the shell in which the script is running.                                                                                     |
| `#`          | In a script, `#` denotes a comment, and `#!` (shebang) directs the script to the appropriate interpreter location.                                                |
| `$-`         | Contains the shell’s flags currently active in your terminal, which determine how the shell functions.                                                           |
