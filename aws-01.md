



| Instance Type | Processor Type        | Use Case                        | Memory    | Network Performance               | Storage Option        | Cost (Approx)        | Special Features                                                  |
|---------------|-----------------------|---------------------------------|-----------|-----------------------------------|-----------------------|----------------------|-------------------------------------------------------------------|
| **T2**        | Intel Xeon (Burstable) | Low to moderate performance     | 2-8 GB    | Low to moderate                  | EBS-Optimized         | Low (cost-effective)  | Burstable performance, cost-effective for low traffic applications |
| **M4**        | Intel Xeon (E5-2676 v3) | General-purpose workloads       | 16-64 GB  | High                              | EBS-Optimized         | Moderate             | High baseline performance, ideal for balanced workloads           |
| **M3**        | Intel Xeon E5-2670 v2  | Balanced performance            | 7.5-30.5 GB| Moderate                         | EBS-Optimized         | Moderate             | Good for multi-purpose workloads, stable performance              |
| **C3**        | Intel Xeon E5-2670 v2  | Compute-intensive workloads     | 7.5-30.5 GB| High                              | EBS-Optimized         | Moderate             | Optimized for CPU-intensive tasks, good for batch processing      |
| **C4**        | Intel Xeon E5-2666 v3  | High-performance compute        | 16-60 GB  | Very high                        | EBS-Optimized         | High                 | Superior network performance, ideal for compute-heavy applications|
| **G2**        | Intel Xeon E5-2670 v2  | Graphics workloads, GPU-based   | 15-60 GB  | High                              | EBS-Optimized         | High                 | GPU-based instance, suitable for rendering and machine learning  |
| **R3**        | Intel Xeon E5-2670 v2  | Memory-intensive workloads      | 30.5-244 GB| Moderate                         | EBS-Optimized         | High                 | High memory capacity, suitable for in-memory databases            |
| **I2**        | Intel Xeon E5-2670 v2  | High I/O performance workloads  | 30.5-488 GB| High                              | SSD-based storage     | High                 | SSD-backed storage for I/O-intensive workloads, low latency       |
| **D2**        | Intel Xeon E5-2670 v2  | Data warehousing and big data   | 64-768 GB | High                              | HDD-based storage     | High                 | Large storage capacity, cost-effective for big data workloads    |



### Key Features:

1. **T2**: 
   - Offers burstable CPU performance, making it cost-effective for applications with variable workloads.
   
2. **M4**: 
   - A balanced instance type, suitable for general-purpose applications with high baseline performance.

3. **M3**: 
   - Great for multi-purpose workloads that require consistent performance.

4. **C3**: 
   - Optimized for compute-intensive tasks, offering higher CPU performance.

5. **C4**: 
   - Focuses on high network throughput and superior compute performance for CPU-heavy applications.

6. **G2**: 
   - Equipped with GPU capabilities, ideal for graphics-heavy tasks like video rendering and machine learning.

7. **R3**: 
   - Designed for memory-intensive applications, such as in-memory caching and real-time analytics.

8. **I2**: 
   - Targets high I/O workloads with SSD-backed storage, providing low-latency access for storage-intensive tasks.

9. **D2**: 
   - Designed for large-scale data warehousing and big data workloads, with massive storage capacity and high throughput.
  


What are policies and what are the different types of policies?
-----------------------------------------------------------------
Policy is an object which is associated with a resource that defines the permissions. 
AWS evaluate these policies when user makes a request. 
Permissions in the policy determine whether to allow or to deny an action. Policies are stored in the form of a JSON documents.

AWS supports six types of policies:
------------------------------------

1. Identity-based policies
2. Resource-based policies
3. Permissions boundaries
4. Organizations SCPs
5. Access Control Lists
6. Session policies





| **Policy Type**                | **Definition**                                                                                                                                                  | **When to Use**                                                                                                                                                                      | **Reusability**                                                                                   | **Scope**                                                                                         | **Example Use Case**                                                                                                                                         |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Inline Policies**             | Policies directly embedded within a specific identity (user, group, or role). The policy is deleted if the identity is deleted.                                | When you need a policy tightly coupled to a particular identity.                                                                                                                     | Not reusable. Must manually replicate the policy for other users or roles if needed.              | Apply to a specific user, group, or role.                                                          | Attach a specific policy to a user for a unique access control requirement.                                                                 |
| **Resource-Based Policies**     | Policies attached directly to a resource (e.g., S3 bucket, KMS key, SNS topic). These policies define who can access the resource and what actions they can perform. | Useful for granting access to resources across different AWS accounts or external entities without modifying the identities' permissions.                                             | Can be managed centrally at the resource level.                                                  | Applies to the specific resource and allows cross-account access.                                  | Define permissions for accessing an S3 bucket or a KMS key.                                                                                       |
| **Service Control Policies (SCPs)** | Policies used in AWS Organizations to define the maximum available permissions for all accounts within an organizational unit (OU) or the root of the organization. SCPs restrict permissions but do not grant them. | Used for governance to restrict what permissions can be granted across multiple AWS accounts or within an OU.                                                                       | Applied at the organization or OU level to control policies across multiple AWS accounts.         | Applies to the entire AWS account or multiple accounts within an organizational unit (OU).        | Prevent certain actions (e.g., EC2 instance creation) across all accounts in an organization.                                                         |
| **Identity-Based Policies**     | Policies attached to a user, group, or role. They specify what actions the identity (e.g., a user or service) can perform, on which resources, and under what conditions. | When you need to specify what actions can be performed by a user, group, or role on resources.                                                                                         | Reusable and centrally managed.                                                                  | Applies specifically to a single user, group, or role.                                              | Assign a user the ability to access a specific resource (e.g., an S3 bucket or EC2 instance).                                                           |
| **Managed Policies**            | Standalone policies that can be attached to multiple users, groups, or roles. Managed policies are reusable and centrally controlled.                            | When you want to manage policies centrally and reuse them across multiple identities.                                                                                                 | Reusable and centrally controlled.                                                               | Can be attached to multiple identities.                                                              | Attach a managed policy like `AmazonS3ReadOnlyAccess` to multiple users to allow read-only access to S3.                                             |











| Feature                          | ALB                                                                 | ALB Ingress                                                                                   |
|----------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Type**                         | Fully managed Layer 7 load balancer for distributing web traffic.  | A Kubernetes controller that integrates ALB with Kubernetes Ingress resources.              |
| **Purpose**                      | Acts as a load balancer for web applications, routing traffic based on host and path. | Manages Ingress resources in Kubernetes, dynamically creating and configuring ALBs.        |
| **Traffic Routing**              | Routes HTTP/HTTPS traffic to targets like EC2, ECS, and Lambda.    | Provides Kubernetes native support to route traffic using ALB within a Kubernetes cluster.  |
| **TLS Termination**              | Supports TLS termination, where certificates can be uploaded and managed via AWS ACM. | TLS termination via ALB, with support for Kubernetes Secret integration for SSL certificates. |
| **Health Checks**                | Built-in health checks for targets.                               | Uses Kubernetes probes and health checks to configure ALB target health status.            |





| Aspect                  | Concurrency                                                                                      | Parallelism                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Definition**          | Managing multiple tasks and their interactions, allowing them to make progress concurrently.    | Breaking down tasks into smaller units of work that can be executed simultaneously.            |
| **Purpose**             | Improves responsiveness and resource utilization in systems with shared resources.              | Speeds up computations and achieves better throughput.                                         |
| **Focus**               | Task management and coordination.                                                               | Exploiting multi-core processors or distributed systems for simultaneous execution.            |
| **Example Use Case**    | Handling multiple user requests in a web server.                                                | Running large-scale data processing across multiple cores or machines.                         |
| **Key Benefit**         | Enhanced responsiveness and efficient use of shared resources.                                  | Higher performance and efficiency in computations.                                             |


| Aspect                     | NGINX Ingress                                                                               | ALB Ingress                                                                                 |
|----------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Controller Type**        | Open-source Ingress controller for Kubernetes.                                             | AWS-managed Ingress controller tightly integrated with ALB.                                |
| **Deployment**             | Runs as a pod within the Kubernetes cluster.                                               | Managed by AWS, with ALB created dynamically outside the cluster.                          |
| **Traffic Routing**        | Routes HTTP/HTTPS traffic based on rules defined in Ingress resources.                     | Leverages ALB for routing based on host, path, and headers.                                |
| **TLS Termination**        | Supports Kubernetes Secrets for SSL certificate management.                                | Integrates with AWS ACM or Kubernetes Secrets for SSL certificates.                        |
| **Scaling**                | Relies on Kubernetes autoscaling for pods.                                                 | Automatically scales with ALB, independent of Kubernetes cluster.                         |
| **Logging and Monitoring** | Uses Kubernetes-native logging and monitoring tools.                                       | Provides AWS CloudWatch integration for logs and metrics.                                  |
| **Platform Dependency**    | Platform-agnostic and can run on any Kubernetes environment.                               | AWS-specific and works only with Kubernetes clusters on AWS.                               |
| **Cost**                   | No additional cost for the controller; costs depend on cluster resources.                  | Additional costs for ALB usage and AWS data transfer fees.                                 |


| Aspect                             | EC2                                                                                     | AWS Lambda                                                                                |
|------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Type**                           | Virtual machines (instances) that run on AWS.                                           | Serverless compute service that runs code in response to events.                         |
| **Pricing**                        | Pay for the compute capacity (instance hours) based on the instance type.              | Pay per invocation and execution time.                                                  |
| **Scaling**                        | Manual or auto-scaling, requires configuration.                                         | Auto-scales automatically based on event triggers.                                       |
| **Control**                        | Full control over the VM, including OS, software, and configuration.                   | Fully managed, no need to worry about the underlying infrastructure.                     |
| **Use Case**                       | Ideal for long-running applications, legacy apps, custom environments.                 | Ideal for short-lived, event-driven tasks like file processing, web APIs, etc.           |
| **Start Time**                     | Longer start time due to instance provisioning.                                         | Fast start (cold starts may occur, but still typically faster than EC2).                 |
| **Maintenance**                    | Requires management of patches, security updates, and OS maintenance.                  | Managed by AWS, no need for OS-level maintenance.                                        |
| **Networking**                     | Full control over networking (VPC, subnets, IPs, etc.).                                | Limited control, but can connect to VPCs if needed.                                      |


| Code | Meaning               | Difference                                                                                   |
|------|-----------------------|---------------------------------------------------------------------------------------------|
| 200  | OK                    | Request succeeded, and the server responded with the requested data.                         |
| 201  | Created               | Request succeeded, and the server created a new resource.                                    |
| 301  | Moved Permanently     | The requested resource has been permanently moved to a new URL.                              |
| 302  | Found                 | The requested resource is temporarily located at a different URL.                           |
| 303  | See Other             | The response to the request can be found under a different URI using a GET method.           |
| 304  | Not Modified          | The resource has not been modified since the last request, so the cached version can be used.|
| 305  | Use Proxy             | The requested resource must be accessed through a proxy.                                     |
| 400  | Bad Request           | The server could not understand the request due to invalid syntax.                           |
| 403  | Forbidden             | The server understands the request, but the client does not have permission to access the resource. |
| 404  | Not Found             | The server cannot find the requested resource.                                               |
| 500  | Internal Server Error | The server encountered an error and could not complete the request.                          |
| 501  | Not Implemented       | The server does not support the functionality required to fulfill the request.               |
| 503  | Service Unavailable   | The server is temporarily unable to handle the request due to maintenance or overload.       |






| Component       | Description                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------|
| `def`           | Used to define a function. The handler name can be customized (e.g., `lambda_handler`).                  |
| **Handler Name** | The name of the function that AWS Lambda invokes (default is `lambda_handler`, but it can be changed).   |
| **Event**       | The input data passed to the handler function.                                                           |
| **Context**     | Provides runtime information to the handler, such as execution time, request ID, and log group details.  |


# LifeCycle Hook
---------------

| Aspect                        | Description                                                                                 |
|-------------------------------|---------------------------------------------------------------------------------------------|
| **Purpose**                   | Performs custom actions by pausing instances when an Auto Scaling group launches or terminates an instance. |
| **Wait State**                | When an instance is paused, it moves to a wait state.                                       |
| **Default Wait Time**         | By default, an instance remains in the wait state for 1 hour.                               |
| **Example Action**            | When a new instance is launched, the lifecycle hook pauses it, allowing custom configurations. |
| **Use Case**                  | Install software or ensure the instance is fully prepared to receive traffic while paused.   |



| Scaling Type      | Description                                                                                       | Triggers/Conditions                           | Use Case                                     | Advantages                                 | Limitations                              |
|-------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------|---------------------------------------------|-------------------------------------------|------------------------------------------|
| **Scheduled Scaling** | Scales based on a predefined schedule.                                                         | Predefined time intervals.                    | Known usage patterns, such as peak hours.   | Predictable and easy to configure.       | Inflexible to sudden changes in demand. |
| **Dynamic Scaling**   | Scales automatically based on current demand metrics.                                           | Real-time metric changes (e.g., CPU usage).   | Workloads with variable traffic patterns.   | Responsive to real-time demand.          | Requires accurate metric thresholds.    |
| **Event-Driven**      | Scales based on specific events or triggers, such as queue depth or custom events.             | Event-based triggers (e.g., SQS queue size).  | Event-based systems or workflows.           | Fast response to specific triggers.      | Requires event configuration.           |
| **Predictive Scaling**| Uses machine learning to forecast demand and adjusts capacity proactively.                     | Historical usage patterns and ML predictions. | Seasonal or predictable traffic patterns.   | Proactive scaling avoids latency issues. | Requires historical data for accuracy.  |
| **Target Tracking**   | Adjusts capacity to maintain a specified metric at a target value (e.g., 70% CPU utilization). | Metric thresholds and desired target value.   | Maintaining steady application performance. | Easy to configure and manage.            | May cause minor over-provisioning.      |
| **Step Scaling**      | Adjusts capacity in steps based on how much a metric deviates from thresholds.                 | Metric deviations exceeding thresholds.       | Gradual response to changing demand.        | Fine-grained control over scaling.       | Slower response compared to others.     |



| Feature                  | Launch Templates                                                                                     | Launch Configurations                                                                 |
|--------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Flexibility**          | More flexible with advanced configuration options like instance types, block device mappings, and network settings. | Simpler and less flexible, suitable for straightforward use cases.                  |
| **Versioning**           | Supports versioning, allowing multiple versions to be created and managed.                           | No versioning; any changes require creating a new launch configuration.             |
| **Tagging**              | Supports instance tagging directly within the template.                                              | Instance tagging is not directly supported; must be done separately or via User Data. |
| **T2/T3 Unlimited**      | Configurable directly in the template, enabling burstable performance for T2/T3 instances.            | Not configurable; must be set separately during instance creation.                  |
| **Instance Types**       | Allows multiple instance types in a single template; Auto Scaling chooses the best fit.              | Only a single instance type can be specified; multiple configurations needed for multiple types. |
| **Instance Market Options** | Configurable within the template, including Spot and On-Demand Instances.                           | Configured in the Auto Scaling group, not within the launch configuration.          |
| **Resource Constraints** | Configured within the template.                                                                      | Configured in the Auto Scaling group rather than the configuration itself.          |


| Storage Class                   | Description                                                                                             | Durability                          | Availability                          | Use Case                                          | Cost                            | Data Retrieval Speed                |
|---------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------|--------------------------------------------------|----------------------------------|-------------------------------------|
| **Standard (Frequently Accessed)** | General-purpose, high-performance storage for frequently accessed data.                                 | 99.999999999% (11 nines)            | 99.99%                                | Active data frequently accessed.                  | Highest storage cost.            | Immediate                           |
| **Standard-IA (Infrequently Accessed)** | Lower-cost storage for data accessed less frequently but still requires high availability.             | 99.999999999% (11 nines)            | 99.9%                                 | Data that needs to be retained long-term but accessed occasionally. | Lower than Standard.              | Immediate                           |
| **One-Zone-IA**                 | Lower-cost infrequent access storage for non-critical data stored in a single AZ.                        | 99.999999999% (11 nines)            | 99.5%                                 | Backups or easily reproducible data.              | Lower than Standard-IA.          | Immediate                           |
| **Glacier**                     | Archive storage for data that is rarely accessed but must be retained for long periods.                  | 99.999999999% (11 nines)            | N/A                                   | Archiving compliance or rarely accessed data.     | Lowest storage cost.             | Minutes to hours (based on retrieval tier). |
| **Glacier Deep Archive**        | Lowest-cost storage for data rarely accessed and retained for 7-10 years.                               | 99.999999999% (11 nines)            | N/A                                   | Long-term backups or compliance data.             | Even lower than Glacier.         | Hours                              |
| **RRS (Reduced Redundancy Storage)** | Low-cost storage with reduced durability for non-critical, reproducible data.                           | 99.99%                              | 99.99%                                | Non-critical, easily reproducible data.           | Lower than Standard.             | Immediate                           |




| Feature                        | Description                                                                                                     | Behavior and Configuration                                                                  |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **SSL Termination/Offloading** | Decrypts client requests and offloads the SSL decryption to the load balancer, reducing the load on backend servers. | SSL certificate must be installed on the load balancer. It reduces the CPU load on instances. |
| **Stick Sessions (Cookies)**   | Binds a user's session to a specific instance to ensure all requests in a session are routed to the same instance. | Session affinity is maintained via cookies, ensuring requests are directed to the same instance. |
| **Cross-zone Load Balancing**  | Distributes incoming requests evenly across all instances in enabled availability zones (AZs).                   | For Classic Load Balancers, needs to be manually enabled, while it is enabled by default for ALBs. |


| Feature                              | **Nginx**                                               | **Apache**                                           |
|--------------------------------------|---------------------------------------------------------|------------------------------------------------------|
| **Model**                            | Event-driven, asynchronous model                        | Process-driven, synchronous model                    |
| **Concurrency**                      | High concurrency, handles static content efficiently     | Better for handling dynamic content (via modules)     |
| **Configuration Syntax**            | Simpler, more straightforward configuration syntax       | More flexible but can be complex                     |
| **Resource Usage**                   | Lower memory and CPU usage under high loads             | Higher resource consumption, especially for large traffic |
| **Module Support**                   | Uses dynamic modules, requires recompiling for changes  | Supports dynamically loading modules at runtime       |



| Feature                                           | **AWS CloudTrail**                                         | **AWS Config**                                           |
|---------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| **Purpose**                                       | Tracks and logs API activity across your AWS account.       | Monitors and records AWS resource configurations over time. |
| **Focus**                                         | Event logging and auditing for API calls.                   | Configuration monitoring and compliance of resources.      |
| **What It Tracks**                                | API calls, user identity, time of request, source IP, and service events. | Resource configurations, relationships, and changes over time. |
| **Scope**                                         | Tracks activity for all AWS services and regions.           | Monitors configurations of specific resources you specify. |
| **Change Detection**                              | Detects changes based on API calls (who made the change and when). | Continuously tracks configuration changes and evaluates compliance. |




| Feature                                             | **ALB (Application Load Balancer)**                         | **NLB (Network Load Balancer)**                          |
|-----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| **Layer of OSI Model**                              | Operates at the application layer (Layer 7)                 | Operates at the transport layer (Layer 4)                 |
| **Traffic Routing**                                 | Routes traffic based on content                            | Deals with IP addresses and ports                         |
| **Target Types**                                    | Supports EC2 instances, IP addresses, and containers       | Primarily supports EC2 instances                          |
| **Protocols Supported**                             | Supports HTTP and HTTPS                                    | Supports TCP, UDP, and TLS (Transport Layer Security)     |
| **DNS and Scaling**                                 | Provides a single DNS name, automatically scales as traffic increases | Provides a static IP address per Availability Zone       |
| **Health Checks**                                   | Supports HTTP and HTTPS health checks                      | Supports TCP health checks                                |
| **Use Case**                                        | Ideal for advanced routing based on content or container services | Ideal for low-latency, high-throughput communication with TCP/UDP traffic |


| Feature                                             | **Classic ALB**                                             | **Application ALB**                                         |
|-----------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| **Layer of OSI Model**                              | Operates at Layer 4 (Transport layer)                       | Operates at Layer 7 (Application layer)                     |
| **Routing**                                         | Routes traffic based on IP and port                         | Routes traffic based on content (e.g., URL path, host)     |
| **Protocol Support**                                | Supports HTTP, HTTPS, and TCP                               | Supports HTTP, HTTPS, WebSockets, and HTTP/2                |
| **Target Types**                                    | Supports only EC2 instances                                 | Supports EC2 instances, IP addresses, and containers        |
| **Health Checks**                                   | Supports TCP and HTTP health checks                         | Supports HTTP, HTTPS, and TCP health checks                 |
| **SSL/TLS Termination**                             | Limited support for SSL/TLS termination                     | Full support for SSL/TLS termination and certificate management |
| **WebSocket Support**                               | Does not support WebSockets                                 | Supports WebSockets                                         |
| **Routing Rules**                                   | No advanced routing rules                                   | Supports host-based, path-based, and query string-based routing |


| Feature                                              | **SG (Security Group)**                                     | **NACL (Network Access Control List)**                      |
|------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| **Operates at**                                      | Instance level                                             | Subnet level                                                |
| **Rules Supported**                                  | Supports only allow rules                                  | Supports both allow and deny rules                          |
| **State**                                            | Stateful: Return traffic is automatically allowed regardless of any rules | Stateless: Return traffic must be explicitly allowed by rules |
| **Rule Evaluation**                                  | We evaluate all rules before deciding whether to allow traffic | We process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic |
| **Traffic Control**                                  | Controls both inbound and outbound traffic at the instance level | Controls both inbound and outbound traffic at the subnet level |




| Feature                               | **Resource**                                              | **Client**                                              |
|---------------------------------------|-----------------------------------------------------------|---------------------------------------------------------|
| **Service Access Level**              | Low-level service access                                  | Higher-level, object-oriented API                       |
| **Generation Source**                 | Generated from service description                         | Generated from resource description                      |
| **API Mapping**                       | Typically maps 1:1 with the service API                    | Uses identifiers and attributes                          |
| **Exposes**                            | Exposes subresources and collections                       |                                                         |



















#GSI
-----
A Global Secondary Index (GSI) in DynamoDB is an index that allows you to query data on non-primary key attributes, providing an alternative to the table's primary key. <br><br>
It supports both eventual and strongly consistent reads and can be created with different partition and sort keys from the table's primary key.


first four ip and last ip add in each subnet reserved

10.0.0.0 - network address
10.0.0.1  - vpc router
10.0.0.2  - reserved by aws
10.0.0.3 - reserved by aws
10.0.0.255 - broadcast address


https://aws.amazon.com/about-aws/whats-new/2017/08/amazon-virtual-private-cloud-vpc-now-allows-customers-to-expand-their-existing-vpcs/










