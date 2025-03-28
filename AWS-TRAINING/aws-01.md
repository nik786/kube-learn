



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









| **Instance Type**  | **Description**                                                                                  | **Pricing Model**                                       | **Use Case**                                                                                       | **Commitment/Duration**                             |
|--------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **On-Demand**      | Instances that are available immediately without requiring long-term commitment.                 | Pay as you go, based on hourly usage.                  | Best for short-term or unpredictable workloads where flexibility is needed.                        | No commitment, pay only for what you use.            |
| **Spot**           | Instances available at a discount, but can be terminated by AWS with little notice.              | Pay for unused capacity, much lower than On-Demand.     | Best for flexible, fault-tolerant workloads like batch processing, big data, and background tasks. | No commitment, but may be interrupted with short notice. |
| **Reserved**       | Instances that require a commitment for 1 or 3 years in exchange for a discount.                 | Pay upfront or with partial upfront options.            | Best for steady-state applications with predictable usage like databases or long-term workloads.    | 1 or 3 years commitment, lower cost over time.        |
| **Dedicated**      | Instances that run on hardware dedicated to a single customer.                                  | Typically higher than On-Demand prices.                 | Best for compliance requirements or workloads that need isolation from other tenants.              | No commitment required, but generally more expensive. |
   
  


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





# AWS Policy Types Comparison

| Policy Type            | Definition                                                                 | When to Use                                                                 | Reusability             | Scope                      | Example Use Case                                                                 |
|------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------|--------------------------|----------------------------|----------------------------------------------------------------------------------|
| Identity-based policies| Policies attached to IAM users, groups, or roles                          | To grant permissions to an identity                                          | Highly reusable          | User, Group, Role          | Allow developers to access specific S3 buckets                                  |
| Resource-based policies| Policies attached directly to AWS resources                               | To grant cross-account access to a resource                                 | Less reusable            | AWS Resource               | Grant another AWS account access to an S3 bucket                                |
| Permissions boundaries | Limits the maximum permissions an identity-based policy can grant         | To delegate permission management while setting guardrails                  | Reusable                 | IAM User or Role           | Allow developers to create roles, but only with specific permissions            |
| Organizations SCPs     | Service control policies set at the AWS Organizations level               | To manage permissions across accounts in an organization                    | Highly reusable          | AWS Account / Org Unit     | Restrict all accounts from disabling CloudTrail                                 |
| Access Control Lists   | Legacy feature for controlling access to S3 and some other resources       | For simple, limited control, mostly for legacy compatibility                 | Not reusable             | AWS Resource               | Make an S3 object publicly readable                                              |
| Session policies       | Policies passed during temporary sessions via AWS STS                     | For fine-grained permissions during federated or temporary access           | Not reusable (per session)| Temporary IAM session     | Limit federated user's session access to only read EC2 instances                |
| Managed Policies       | Predefined or customer-created standalone policies                        | For consistent permission sets across multiple users, groups, or roles       | Highly reusable          | IAM User, Group, Role      | Attach AWS managed `AmazonEC2ReadOnlyAccess` policy to multiple users           |




| Feature               | ALB Ingress                                 | API Gateway                                         | Use Case for ALB Ingress                        | Use Case for API Gateway                           |
|-----------------------|---------------------------------------------|---------------------------------------------------|------------------------------------------------|---------------------------------------------------|
| **Primary Function**  | Distributes traffic to backend services.   | Manages API requests with routing and processing.| Load balancing for microservices or web apps.  | Managing REST, WebSocket, or HTTP APIs.           |
| **Protocol Support**  | Supports HTTP, HTTPS, WebSocket.           | Supports HTTP, HTTPS, WebSocket, and REST APIs.  | Serving dynamic web apps via containerized apps.| Building serverless APIs with request validation. |
| **Scaling**           | Scales based on target service needs.      | Built-in integration with Lambda for scaling.    | Scaling EC2, Fargate, or EKS workloads.        | Scaling serverless applications automatically.    |
| **Request Processing**| Limited request manipulation, header-based.| Supports transformations, validation, caching.   | Direct request forwarding to applications.     | API validation, rate-limiting, caching responses. |
| **Integration**       | Integrates with ECS, EKS, EC2.             | Deeply integrates with Lambda, DynamoDB, etc.    | Deploying containerized workloads behind ALB.  | Creating APIs with Lambda and DynamoDB backend.   |







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




# HTTP Status Codes Explained

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
| 401  | Unauthorized          | Authentication is required and has failed or has not yet been provided.                     |
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



# Auto Scaling Types Comparison

| Scaling Type         | Description                                                                                       | Triggers/Conditions                           | Use Case                                     | Advantages                                 | Limitations                              |
|----------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------|---------------------------------------------|-------------------------------------------|------------------------------------------|
| **Scheduled Scaling**| Scales based on a predefined schedule.                                                           | Predefined time intervals.                    | Known usage patterns, such as peak hours.   | Predictable and easy to configure.       | Inflexible to sudden changes in demand. |
| **Dynamic Scaling**  | Scales automatically based on current demand metrics.                                            | Real-time metric changes (e.g., CPU usage).   | Workloads with variable traffic patterns.   | Responsive to real-time demand.          | Requires accurate metric thresholds.    |
| **Event-Driven**     | Scales based on specific events or triggers, such as queue depth or custom events.              | Event-based triggers (e.g., SQS queue size).  | Event-based systems or workflows.           | Fast response to specific triggers.      | Requires event configuration.           |
| **Predictive Scaling**| Uses machine learning to forecast demand and adjusts capacity proactively.                      | Historical usage patterns and ML predictions. | Seasonal or predictable traffic patterns.   | Proactive scaling avoids latency issues. | Requires historical data for accuracy.  |
| **Target Tracking**  | Adjusts capacity to maintain a specified metric at a target value (e.g., 70% CPU utilization).   | Metric thresholds and desired target value.   | Maintaining steady application performance. | Easy to configure and manage.            | May cause minor over-provisioning.      |
| **Step Scaling**     | Adjusts capacity in steps based on how much a metric deviates from thresholds.                  | Metric deviations exceeding thresholds.       | Gradual response to changing demand.        | Fine-grained control over scaling.       | Slower response compared to others.     |
| **Simple Scaling**   | Increases or decreases capacity based on a single alarm and cooldown period.                    | Single CloudWatch alarm and cooldown timer.   | Small, non-complex applications.            | Easy to set up with minimal rules.       | May not handle rapid fluctuations well. |













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






1. involves LOCAL DNS QUERY -
2. search  ISP RECURSIVE DNS SERVER
3. search ASK ROOT NAME SERVER
4. search ASK TLD NAME SERVER
5. search  AUTHORITATIVE DNS SERVER
6. involve RETRIEVE RECORD





| **Routing Policy**    | **Description**                                                                                      | **Use Case**                                                 | **How It Works**                                                                                                 | **Traffic Distribution**                          |
|-----------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| **Simple Routing**    | Routes traffic to a single resource (e.g., EC2 instance or load balancer) based on domain name.     | Basic routing for applications that need a single endpoint.   | Directs all traffic to a single resource, no conditions or variations.                                           | 100% of traffic to a single resource.           |
| **Weighted Routing**  | Distributes traffic across multiple resources based on a set of weights assigned to each resource.  | Load balancing or canary deployments for new features.      | Assigns weights to each resource to proportionally distribute traffic according to those weights.                | Traffic is split based on defined weights.       |
| **Latency Based**     | Routes traffic to the region with the lowest latency for the user.                                   | Optimizing user experience by reducing latency.              | Directs traffic to the resource in the region with the least latency for the user’s location.                    | Routes to the region with the lowest latency.    |
| **Failover**          | Routes traffic to a primary resource and directs it to a secondary resource if the primary fails.    | Disaster recovery or backup resource configuration.          | If the primary resource is unhealthy or unavailable, traffic is routed to the failover resource.                | 100% traffic to the primary, failover on failure. |
| **Geo Location**      | Routes traffic based on the geographical location of the user.                                       | Geographically optimized services (e.g., serving region-specific content). | Directs traffic to the resource that is closest to the user's geographical location.                           | Routes based on the user's geographical location.|



| **Term**               | **Description**                                                                                       | **Key Function**                                             | **Role in DNS Resolution**                                      |
|------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------|
| **SOA (Start of Authority)**  | Defines the beginning of a DNS zone and contains important information about the zone.               | Stores information such as the primary DNS server and refresh time. | Marks the start of a DNS zone and includes crucial zone details. |
| **Authoritative**       | A DNS server that has the final say on domain names within its zone.                                  | Provides the definitive answer for queries within its domain. | Returns authoritative answers for queries related to its zone.  |
| **Name Server**         | A DNS server that stores DNS records for a domain and answers DNS queries.                           | Resolves domain names to IP addresses for client requests.    | Provides DNS resolution for domain names by looking up records. |
| **DNS Cache**           | A local storage of previously looked-up DNS records on a client or DNS server.                        | Speeds up DNS query responses by reusing previously cached data. | Reduces the need for repeated DNS lookups by caching resolved data. |
| **Root Name Server**    | The highest level DNS servers that know where to direct requests for domain names.                  | Directs DNS queries to the appropriate TLD name servers.      | Resolves queries by directing them to the correct TLD servers.   |
| **Recursive**           | A DNS resolver that queries multiple DNS servers in a series to resolve a domain name fully.        | Makes queries to other DNS servers to resolve a domain name. | Iteratively resolves domain names, querying multiple servers if necessary. |
| **MX (Mail Exchange)**  | A type of DNS record that specifies the mail server responsible for receiving email for a domain.    | Routes email messages to the appropriate mail servers.       | Directs email traffic to the correct mail server for a domain.  |
| **TLD Name Server**     | A DNS server responsible for a top-level domain (like .com, .org, .net).                             | Directs queries to the appropriate authoritative name servers for domains. | Handles DNS queries for domains under its TLD.                  |











#GSI
-----
# DynamoDB Global Secondary Index (GSI)

| Feature                     | Description                                                                                     |
|----------------------------|-------------------------------------------------------------------------------------------------|
| **Definition**              | An index that enables querying data using non-primary key attributes.                          |
| **Purpose**                 | Provides an alternative access pattern beyond the table's primary key.                         |
| **Partition/Sort Keys**     | Can have different partition and sort keys from the base table.                               |
| **Read Consistency**        | Supports both eventual and strongly consistent reads (with limitations).                      |
| **Use Case**                | When queries need to be run on attributes other than the primary key.                          |



# VPC Subnet Planning and Reserved IPs

## Reserved IPs in Each Subnet

| IP Address       | Purpose              |
|------------------|----------------------|
| First IP (e.g., 10.0.0.0)   | Network Address       |
| Second IP (e.g., 10.0.0.1)  | VPC Router            |
| Third IP (e.g., 10.0.0.2)   | Reserved by AWS       |
| Fourth IP (e.g., 10.0.0.3)  | Reserved by AWS       |
| Last IP (e.g., 10.0.0.255)  | Broadcast Address     |

> ✅ **Total 5 IP addresses are reserved by AWS in each subnet**

---

## Subnet Sizing Guidelines

| Subnet CIDR | Total IPs | Usable IPs | Description                   |
|-------------|-----------|------------|-------------------------------|
| /24         | 256       | 251        | Suitable for most use cases   |
| /25         | 128       | 123        | For smaller environments      |
| /26         | 64        | 59         | Tight resource constraints    |

---

## Best Practices

| Consideration     | Recommendation                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| **Subnet Size**   | Avoid using very large subnets (e.g., /16) to prevent IP wastage                |
| **Typical Use**   | Use /24 or smaller for better IP management                                     |
| **High Availability** | Use at least 2 subnets across different Availability Zones (AZs)             |
| **Resource Deployment** | Deploy services like ECS, RDS, and ELB across multiple subnets and AZs     |








https://aws.amazon.com/about-aws/whats-new/2017/08/amazon-virtual-private-cloud-vpc-now-allows-customers-to-expand-their-existing-vpcs/




### How many buckets can be created in S3?
By default, you can create up to **100 buckets** in your AWS S3 account.

### What is Cross Region Replication?
**Cross Region Replication (CRR)** is a feature in AWS that enables automatic and asynchronous copying of objects from one S3 bucket to another, either in the same or a different region.

### What are edge locations in AWS?
**Edge locations** are endpoints in AWS that are used to cache content closer to users, improving the performance of web applications by reducing latency and speeding up content delivery.

### What is CloudFront?
**CloudFront** is a Content Delivery Network (CDN) service that distributes web content, such as web pages, images, and videos, to users based on their geographic location, providing low-latency delivery.

### What is the minimum and maximum size that you can store in S3?
- **Minimum size**: 0 bytes
- **Maximum size**: 5 TB

### What is the default storage class in S3?
The **default storage class** in S3 is **Standard (Frequent Access)**, which is ideal for data that is accessed frequently.



### What is a Snowball?
**Snowball** is a petabyte-scale data transport solution that uses secure appliances to transfer large amounts of data into and out of the AWS Cloud.

### How many Elastic IPs can you create?
You can create up to **5 Elastic IP addresses** per AWS account per region.

### What is the maximum size of messages in SQS?
The maximum size of a message in **SQS** (Simple Queue Service) is **256 KB**.

### How many subnets can you have per VPC?
You can have up to **200 subnets** per Virtual Private Cloud (VPC).

### What is Amazon ElastiCache?
**Amazon ElastiCache** is a web service that allows you to easily deploy, operate, and scale in-memory caches in the cloud.

### How to connect EBS volume to multiple instances?
You cannot connect a single **EBS volume** to multiple instances. However, you can connect **multiple EBS volumes** to a single instance.


### How can you encrypt data in S3?
You can encrypt data in S3 using the following methods:

- **Server-Side Encryption – S3 (AES 256 encryption)**: Automatically encrypts data when it is written to S3.
- **Server-Side Encryption – KMS (Key Management Service)**: Uses AWS KMS to manage encryption keys.
- **Server-Side Encryption – C (Client-Side Encryption)**: You manage the encryption before uploading data to S3.

### What are the parameters for S3 pricing?
The pricing model for S3 is based on the following parameters:

- **Storage used**: The total amount of data stored in S3.
- **Number of requests**: The number of requests made to S3 (e.g., PUT, GET).
- **Storage management**: Costs associated with managing your S3 storage, including lifecycle management and versioning.
- **Data transfer**: Charges for transferring data in and out of S3.
- **Transfer acceleration**: Additional charges for faster data transfers using S3 Transfer Acceleration.

### What is the maximum individual archive that you can store in Glacier?
You can store a maximum individual archive of up to **40 TB** in **Amazon Glacier**.


### What is meant by a subnet?
A **subnet** is a large section of IP addresses that is divided into smaller, more manageable chunks, known as subnets.

### How can you convert a public subnet to a private subnet?
To convert a **public subnet** to a **private subnet**, follow these steps:

1. **Remove the Internet Gateway (IGW)**.
2. **Add a NAT Gateway** to the subnet.
3. **Associate the subnet with the private route table**.

### What is the use of Elastic IPs, and are they charged by AWS?
An **Elastic IP (EIP)** is an **IPv4 address** that is used to connect instances to the internet. AWS charges for Elastic IPs when they are not associated with a running instance.

### One of my S3 buckets is deleted, but I need to restore it. Is there any possible way?
If **versioning** is enabled on the S3 bucket, you can easily restore the deleted objects by retrieving previous versions of the files.


### What is meant by parameter groups in RDS? And what is the use of it?
**RDS** (Relational Database Service) is a managed AWS service that offers a wide set of parameters through **parameter groups**, which can be modified based on your specific requirements. These parameter groups allow you to configure database settings to optimize performance, security, and availability.

### What is the use of tags and how are they useful?
**Tags** are used for the **identification** and **grouping** of AWS resources. They consist of key-value pairs that help you organize, manage, and filter resources. Tags are especially useful for cost allocation, automation, and access control.

### You have enabled sticky sessions with ELB. What does it do with your instance?
When **sticky sessions** are enabled with an **Elastic Load Balancer (ELB)**, it binds the user session to a **specific instance**. This ensures that all requests from a user during their session are routed to the same instance, improving session consistency.

### Which type of load balancer makes routing decisions at either the transport layer or the application layer and supports either EC2 or VPC?
The **Classic Load Balancer (CLB)** makes routing decisions at either the **transport layer (Layer 4)** or the **application layer (Layer 7)** and supports both **EC2 instances** and **VPC** environments.

### Which is the virtual network interface that you can attach to an instance in a VPC?
The **Elastic Network Interface (ENI)** is a virtual network interface that you can attach to an instance within a **VPC** to enable network connectivity.


# You are running to website on EC2 instances can deployed across multiple Availability Zones with an Multi-AZ RDS MySQL Extra Large DB Instance etc. Then site performs a high number of the small reads and the write per second and the relies on the eventual consistency model. After the comprehensive tests you discover to that there is read contention on RDS MySQL. Which is the best approaches to the meet these requirements?

Deploy Elastic Cache in each availability zone and Then Increase the RDS MySQL Instance size and the Implement provisioned IOPS.

## An startup is running to a pilot deployment of around 100 sensors to the measure street noise and The air quality is urban areas for the 3 months. It was noted that every month to around the 4GB of sensor data are generated. The company uses to a load balanced take auto scaled layer of the EC2 instances and a RDS database with a 500 GB standard storage. The pilot was success and now they want to the deploy take atleast 100K sensors.let which to need the supported by backend. You need to the stored data for at least 2 years to an analyze it. Which setup of  following would you be prefer?

The Replace the RDS instance with an 6 node Redshift cluster with take 96TB of storage



Let to Suppose you have an application where do you have to render images and also do some of general computing. which service will be best fit your need?
Used on Application Load Balancer.

How will change the instance give type for the instances, which are the running in your applications tier and Then using Auto Scaling. Where will you change it from areas?
Changed to Auto Scaling launch configuration areas

You have an content management system running on the Amazon EC2 instance that is the approaching 100% CPU of utilization. Which option will be reduce load on the Amazon EC2 instance?

What does the Connection of draining do?
It re-routes traffic from the instances which are to be updated (or) failed for health-check.


## You use the Amazon CloudWatch as your primary monitoring system for web application. After a recent to software deployment, your users are to getting Intermittent the 500 Internal Server to the Errors, when you using web application. You want to create the CloudWatch alarm, and notify the on-call engineer let when these occur. How can you accomplish the using the AWS services?

1. Create a CloudWatch  Log  group
2. Then create a metric filters which will capture 500 Internal Servers error.
3. Then Set a CloudWatch alarm on this metric .
4. Then Use sns  to notify on-call engineers when CloudWatch alarm is triggered.


## You are migrating to legacy client-server application for AWS. The application responds to a specific DNS visible domain (e.g. www.example.com) and server 2-tier architecture, with multiple application for the servers and the database server. Remote clients use to TCP to connect to the application of servers. The application servers need to know the IP address of clients in order to  the function of properly and are currently taking of that information from  TCP socket. A Multi-AZ RDS MySQL instance to will be used for database. During the migration you  change the application code but you have file a change request. How do would you implement the architecture on the AWS in order to maximize scalability and high availability?

File a change request to get implement of Proxy Protocol support in the application. Use of ELB with TCP Listener and A Proxy Protocol enabled to distribute the  load on two application servers in the different AZs.


## Your application currently is leverages AWS Auto Scaling to the grow and shrink as a load Increases/decreases and has been performing as well. Your marketing a team expects and steady ramp up in traffic to follow an upcoming campaign that will result in 20x growth in the traffic over 4 weeks. Your forecast for approximate number of the Amazon EC2 instances necessary to meet  peak demand is 175. What should be you do  avoid potential service disruptions during the ramp up traffic?

Check the service limits in the Trusted Advisors and adjust as necessary, so that forecasted count remains within  the limits.


## You are the designing an application that a contains protected health information. Security and Then compliance requirements for your application mandate that all protected to health information in application use to encryption at rest and in the transit module. The application to uses an three-tier architecture. where should data flows through the load balancers and is stored on the Amazon EBS volumes for the processing, and the results are stored in the Amazon S3 using a AWS SDK. Which of the options satisfy the security requirements?

Use TCP load balancing on load balancer system, 
SSL termination on Amazon to create EC2 instances, 
OS-level disk  encryption on Amazon EBS volumes,
The amazon S3 with server-side to encryption 
Use the SSL termination on load balancers, 
an SSL listener on the Amazon to create EC2 instances, 
Amazon EBS encryption on the EBS volumes containing the PHI, and Amazon S3 with a server-side of encryption.

# An AWS customer are deploying an web application that is the composed of a front-end running on the Amazon EC2 and confidential data that are stored on the Amazon S3. The customer security policy is that all accessing operations to this sensitive data must authenticated and authorized by centralized access to management system that is operated by separate security team. In addition, the web application team that be owns and administers the EC2 web front-end instances are prohibited from having the any ability to access data that circumvents this centralized access to management system. Which are configurations will support these requirements?

We need to use STS tokens to download of the approved data directly from a Amazon S3


## A Enterprise customer is starting on their migration to the cloud, their main reason for the migrating is agility and they want to the make their internal Microsoft active directory available to the many applications running on AWS, this is so internal users for only have to remember one set of the credentials and as a central point of user take control for the leavers and joiners. How could they make their actions the directory secures and the highly available with minimal on-premises on infrastructure changes in the most cost and the time-efficient way?

By Using a VPC, they could be create an the extension to their data center. 
 make use of resilient hardware IPSEC on tunnels

# What is AWS Certificate Manager ?

AWS Certificate Manager is an administration that lets you effortlessly arrangement, oversee, and send open and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) endorsements for use with AWS administrations and your inward associated assets. SSL/TLS declarations are utilized to anchor arrange interchanges and set up the character of sites over the Internet and additionally assets on private systems. AWS Certificate Manager expels the tedious manual procedure of obtaining, transferring, and reestablishing SSL/TLS endorsements.

# What is the AWS Key Management Service??
AWS Key Management Service (AWS KMS) is an overseen benefit that makes it simple for you to make and control the encryption keys used to scramble your information. … AWS KMS is additionally coordinated with AWS CloudTrail to give encryption key use logs to help meet your inspecting, administrative and consistence needs.

# What is the precedence level between explicit allow and explicit deny.
Explicit deny will always override Explicit Allow.

# What is the difference between the Administrative Access and Power User Access in term of pre-build policy
--------------------------------------------------------------------------------------------------------------


| **Access Type**           | **Administrative Access**                                                | **Power User Access**                                                   |
|---------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Pre-Built Policy Name**  | `AdministratorAccess`                                                     | `PowerUserAccess`                                                       |
| **Permissions**            | Provides full access to all AWS resources and services, including IAM.   | Provides access to all AWS services, except for managing IAM resources. |
| **IAM Access**             | Allows managing IAM roles, policies, and users.                          | Does not allow managing IAM roles, policies, or users.                   |
| **Use Case**               | Ideal for users who need complete control over AWS resources.           | Ideal for users who need full access to resources but cannot manage IAM. |
| **Risk Level**             | High risk, as users have unrestricted access to the entire AWS account. | Moderate risk, as users cannot modify security or access configurations. |


What is the purpose of Identity Provider?
------------------------------------------

| **Concept**            | **Explanation**                                                                                              |
|------------------------|--------------------------------------------------------------------------------------------------------------|
| **Identity Provider**   | An Identity Provider (IdP) helps establish trust between AWS and the corporate Active Directory (AD) environment. |
| **Federated Role**      | When creating a federated role, the IdP authenticates users, and the federated role grants them access to AWS resources. |
| **Trust Relationship**  | The trust between AWS and the corporate AD environment is established through the IdP, allowing secure access. |
| **Single Sign-On (SSO)**| Users can authenticate once through the corporate AD, and then assume roles to access AWS resources without needing separate credentials. |
| **Secure Authentication**| The IdP ensures that users are authenticated securely before granting temporary access via federated roles. |




What are the benefits of STS (Security Token Service):
-------------------------------------------------------

| **Benefit**                        | **Explanation**                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Temporary Security Credentials** | STS provides temporary security credentials, reducing the need to store long-term credentials.            |
| **Granular Access Control**        | STS enables fine-grained access control by assigning specific permissions to users or services.           |
| **Cross-Account Access**           | STS allows users to assume roles in other AWS accounts, facilitating secure cross-account access.         |
| **Integration with Identity Providers** | STS integrates with identity providers (e.g., SAML, OpenID) to allow federated access for external users. |
| **Reduced Risk of Credential Exposure** | Temporary credentials are automatically rotated, reducing the risk of exposure compared to static credentials. |




What is the maximum size of S3 Bucket?
5TB

An high demand of IOPS performance is expected around 15000.Which EBS volume type would you recommend?

Provisioned IOPS.

What is the difference between a user and a role in AWS and under what service does this concept come under?
-------------------------------------------------------------------------------------------------------------


| **Aspect**                | **User**                                                                                             | **Role**                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Credentials**            | A user has credentials (Access Keys, Secret Keys, etc.) that are created during user creation.     | No credentials are created for roles; credentials are assumed temporarily when a role is assumed. |
| **Security**               | Less secure compared to roles, as credentials are associated with the user permanently.             | More secure as credentials are temporary and are assumed for specific tasks.                      |
| **Access**                 | Users are assigned permissions directly via policies or groups.                                     | Roles are assumed by users or services to gain access to resources based on role permissions.     |
| **Service**                | IAM Users are typically for individuals or applications that need direct access to AWS resources.   | IAM Roles are used to provide temporary access to AWS services or resources for applications.     |
| **Use Case**               | Suitable for human users or applications requiring persistent access credentials.                   | Suitable for use by AWS services or cross-account access where temporary access is needed.       |


What is the auditing service in AWS ?
--------------------------------------

| **Feature**             | **Description**                                                                                       |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| **Service**             | CloudTrail                                                                                             |
| **Purpose**             | CloudTrail is an auditing service in AWS that logs all actions performed by users in the AWS account.  |
| **Default Log Duration**| By default, CloudTrail retains events for the last 90 days.                                            |
| **Event Logging**       | All user actions in the AWS account are logged as events in CloudTrail.                               |


What are the types you have in storage gateway ?
-------------------------------------------------
There are 3 types in storage gateway,

| **Gateway Type**        | **Description**                                                                                          | **Use Case**                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| **File Gateway**        | A hybrid cloud storage solution that provides on-premises access to Amazon S3 for file-based applications. | Enabling file-based applications to store data in S3 while keeping local access. |
| **Volume Gateway**      | Provides cloud-backed storage volumes for on-premises applications, either as block storage or iSCSI volumes. | Providing scalable and durable block storage with local caching for applications. |
| **Tape Gateway**        | Enables backup applications to store virtual tape backups in Amazon S3, simulating a physical tape library. | Managing long-term backup archives in the cloud, integrating with existing backup workflows. |


What are the types you have in kinesis ?
---------------------------------------
There are 3 types in kinesis,

| **Service**             | **Description**                                                                                         | **Use Case**                                                             |
|-------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Kinesis Streams**     | A scalable and durable real-time data stream platform for collecting and processing large amounts of data. | Collecting, processing, and analyzing real-time data streams from various sources. |
| **Kinesis Firehose**    | Fully managed service that delivers real-time streaming data to destinations like S3, Redshift, and others. | Loading streaming data to data stores and analytics tools for real-time analysis. |
| **Kinesis Analytics**   | Analyzes streaming data in real-time using SQL queries, providing insights for immediate action.         | Real-time analytics on data streams to trigger alerts or take actions based on insights. |


How can you encrypt the data in S3 ?
-------------------------------------
You can use AES-256 and KMS to encrypt your data in S3. KMS is your Key Management Service to encrypt your data in S3

What is user data in AWS ?
--------------------------

| **Feature**             | **Description**                                                                          |
|-------------------------|------------------------------------------------------------------------------------------|
| **User Data**           | A section where you can write a boot-up script to execute commands when the server starts.|
| **Purpose**             | Used for automating tasks on server startup, such as installing software or configuring services.|
| **Common Use Cases**    | Automating server configurations, installing packages, setting environment variables, etc.|
| **Execution**           | The script runs automatically every time the server starts, based on the user data configuration.|
| **Format**              | Can be written in bash, cloud-init, or any other supported scripting language.|




| **Condition**                          | **Description**                                                                                                      |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **CIDR Block should not overlap**      | The IP address ranges (CIDR blocks) of the two VPCs must not overlap, ensuring that there is no conflict in routing.  |
| **VPC should be in the same region**   | The two VPCs must be located in the same AWS region for the peering connection to be established.                     |
| **VPC must belong to the same account**| The VPCs must belong to the same AWS account unless using a cross-account peering connection.                        |


| **Instance State**  | **Possible Issue**                | **Workaround**                                                                                             |
|---------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------|
| **0/2**             | Hardware issue                    | Restart the instance. If the issue persists, check the logs to identify and fix the issue.               |
| **1/2**             | OS issue                           | Restart the instance. If the issue persists, check the logs to identify and fix the issue.               |



 What is Status Checks in AWS Ec2?
 ------------------------------------
 
| **Status Check Type**        | **Description**                                                                                       | **Possible Issues**                                                  |
|------------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| **System Status Checks**      | These checks look into problems that need AWS assistance to resolve.                                 | - Network connectivity                                                |
|                              | When a system status check fails, you can wait for AWS to resolve the issue, or try to resolve it yourself. | - System power                                                        |
|                              |                                                                                                       | - Software issues in data centers                                     |
|                              |                                                                                                       | - Hardware issues                                                     |
| **Instance Status Checks**    | These checks look into problems that need your involvement to fix.                                    | - Failed system status checks                                         |
|                              | If an instance status check fails, you can reboot the instance to try and resolve the issue.         | - Memory full                                                         |
|                              |                                                                                                       | - Corrupted file system                                               |
|                              |                                                                                                       | - Kernel issues                                                       |



MicroService
----------------


| **Aspect**                 | **Description**                                                                                                           |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Microservices Architecture** | A method of developing applications as a collection of small, loosely coupled, independently deployable services.         |
| **Scalability**             | Microservices allow independent scaling of individual services based on demand, leading to more efficient resource usage.   |
| **Technology Flexibility** | Different services can be built using different technologies and languages, offering flexibility in choosing the right tools.|
| **Resilience**              | Failures in one service do not affect the entire application, improving overall system reliability.                        |
| **Faster Development**      | Smaller, independent teams can work on different services, speeding up the development and release cycle.                   |

| **Pros**                    | **Cons**                                                                                                               |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Scalability**              | Can scale each service independently to optimize resource usage and meet demand.                                      | **Complexity**: Managing and coordinating multiple services can increase system complexity.                      |
| **Resilience**               | Failure of one service does not impact the entire application, enhancing fault tolerance.                            | **Communication Overhead**: Multiple services communicating over networks can lead to higher latency and more complex data handling. |
| **Flexibility in Development** | Services can be developed, tested, and deployed independently, enabling faster development cycles.                     | **Data Management**: Ensuring data consistency across services can become complex, requiring specialized techniques like eventual consistency. |
| **Technology Agnostic**     | Different services can use different technologies best suited for their requirements.                                  | **Deployment and Operations Overhead**: Managing multiple deployments and services increases operational burden. |
| **Easier Maintenance**       | Smaller codebases for each service make it easier to maintain and update individual services.                         | **Increased Network Traffic**: Services need to communicate over the network, which can lead to increased traffic and potential bottlenecks. |




ServerLess Computing
---------------------

| **Feature**                               | **Description**                                                                                                                                                                  |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Serverless Computing**                  | A method of providing backend services on an as-used basis, where the vendor is charged based on computation. Users don't need to reserve or pay for fixed bandwidth or servers.  |
| **Auto-Scaling**                          | The service automatically scales based on usage, ensuring the right resources are allocated as needed without manual intervention.                                               |
| **Agility & Cost Efficiency**             | Enables the building of modern applications with increased agility and a lower total cost of ownership.                                                                         |
| **Developer Focus**                       | Developers can focus on core product development instead of managing servers or runtimes, whether in the cloud or on-premises.                                                   |
| **Reduced Overhead**                      | Reduced overhead allows developers to reclaim time and energy, which can be spent on creating scalable and reliable products instead of worrying about infrastructure management. |


| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **Step Functions**           | A fully managed serverless orchestration service provided by AWS that allows you to coordinate and automate workflows involving multiple AWS services. It's commonly used for building and orchestrating complex workflows such as data processing pipelines, microservices coordination, and multi-step serverless applications. It simplifies the development and maintenance of workflows by providing a highly scalable and reliable orchestration service. |
| **State Machines and States**| Step Functions uses state machines as its core concept. A state machine is a collection of states connected by transitions. States represent individual tasks or steps in your workflow, such as AWS Lambda functions, AWS Batch jobs, Amazon ECS tasks, or AWS Glue ETL jobs. |
| **Logging and Monitoring**   | AWS Step Functions provides detailed logging and monitoring capabilities, including CloudWatch Logs and CloudWatch Metrics, to help troubleshoot and monitor the execution of workflows. |
| **Cost-Effective**           | AWS Step Functions charges based on the number of state transitions, making it cost-effective for various workloads. |
| **Built-In State Types**     | AWS Step Functions offers several built-in state types, including: <br> **Task State**: Represents an individual task like AWS Lambda functions or Amazon ECS tasks. <br> **Choice State**: Adds conditional logic based on the outcome of previous states. <br> **Parallel State**: Executes multiple states in parallel. <br> **Wait State**: Adds delays to the workflow. <br> **Fail State**: Marks the workflow as failed. <br> **Succeed State**: Marks the workflow as successful. |
| **Visual Workflow Designer**| Provides a visual interface for designing and defining workflows using the AWS Management Console or AWS CloudFormation templates. States and transitions are defined using JSON or YAML. |



| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **EventBridge**              | Amazon EventBridge is a serverless event bus service provided by AWS that simplifies event-driven application development. It allows you to connect various AWS services, integrated SaaS applications, and custom applications using events. |
| **Event Bus**                | EventBridge uses the concept of an event bus to route and manage events. There are two types: default event buses (created for you) and custom event buses (created for specific use cases). |
| **Events**                   | Messages that represent changes or occurrences within your applications, services, or infrastructure. They can be generated by AWS services, custom applications, or third-party services integrated with EventBridge. |
| **Event Sources**            | Services or entities that produce events. AWS services like AWS Lambda, Amazon S3, and Amazon CloudWatch can be event sources. You can also create custom event sources by publishing events to EventBridge using the API. |
| **Event Rules**              | Define what to do when specific events are received by the event bus. Event rules can filter events based on attributes, pattern matching, and other conditions. |
| **Targets**                  | AWS services or custom applications that receive events when they match an event rule. Supported targets include AWS Lambda functions, Amazon SNS topics, Amazon SQS queues, Kinesis Data Streams, Step Functions, and more. Custom applications can also be targeted via HTTP endpoints. |
| **Schema Registry**          | Includes a schema registry that allows defining the structure of events using JSON Schema. Schemas help ensure data consistency and make it easier to understand the format of events. |

EventBridge
------------

Amazon EventBridge is a serverless event bus that enables event-driven communication between AWS services, SaaS applications, and custom applications.



| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **Event Bus**                | EventBridge uses the concept of an event bus to route and manage events. There are two types: default event buses (created for you) and custom event buses (created for specific use cases). |
| **Events**                   | Messages that represent changes or occurrences within your applications, services, or infrastructure. They can be generated by AWS services, custom applications, or third-party services integrated with EventBridge. |
| **Event Sources**            | Services or entities that produce events. AWS services like AWS Lambda, Amazon S3, and Amazon CloudWatch can be event sources. You can also create custom event sources by publishing events to EventBridge using the API. |
| **Event Rules**              | Define what to do when specific events are received by the event bus. Event rules can filter events based on attributes, pattern matching, and other conditions. |
| **Targets**                  | AWS services or custom applications that receive events when they match an event rule. Supported targets include AWS Lambda functions, Amazon SNS topics, Amazon SQS queues, Kinesis Data Streams, Step Functions, and more. Custom applications can also be targeted via HTTP endpoints. |
| **Schema Registry**          | Includes a schema registry that allows defining the structure of events using JSON Schema. Schemas help ensure data consistency and make it easier to understand the format of events. |



AWS Batch Service:
-------------------

| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **AWS Batch**                | A fully managed service designed for batch processing and job scheduling, simplifying the process of launching, managing, and scaling batch computing jobs on AWS. |
| **Job Definitions**          | A blueprint for batch jobs specifying parameters such as the Docker image to use, resource requirements, and the command to execute. |
| **Job Queues**               | Used to prioritize and manage the execution of batch jobs. Jobs are submitted to specific queues, and AWS Batch handles scheduling and execution based on priorities and resource availability. |
| **Compute Environments**     | Define the type of compute resources available for executing jobs. AWS Batch can manage both Amazon EC2 instances and AWS Fargate tasks as compute environments. |


Workflow of AWS Batch:
-------------------------


| **Component**               | **Description**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| **Job Submission**           | Users or applications submit batch jobs to AWS Batch.                         |
| **Job Queue**                | AWS Batch manages job queues, ensuring that jobs are processed in an orderly fashion based on priority and other factors. |
| **Scheduling**               | AWS Batch schedules jobs based on factors such as job priority, job dependencies, and resource availability. |
| **Compute Environment**      | AWS Batch provisions and manages the underlying compute resources needed for executing jobs, ensuring that the required resources are available. |


Use Cases for AWS Batch:
-------------------------

| **Use Case**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Data Processing**          | AWS Batch is often used for data processing tasks, such as ETL (Extract, Transform, Load) jobs, data validation, and data analytics. |
| **Scientific Computing**     | Suitable for running scientific simulations, computational chemistry, genomics, and other compute-intensive tasks. |
| **Image and Video Processing** | Can be used for image and video processing, transcoding, and analysis.         |
| **Job Orchestration**        | AWS Batch can be used to orchestrate complex workflows involving multiple job steps and dependencies. |
| **Rendering**                | Used in the media and entertainment industry for rendering animations, special effects, and high-quality images. |
| **Cost-effectiveness**       | AWS Batch simplifies the management of batch workloads by automating resource provisioning and job scheduling, making it cost-effective and scalable. |




Cross Account/Multiple Accounts
---------------------------------

aws organizations

- [AWS Organization for Account & Multiple Account setup: Step-by-Step Tutorial (Part-2)](https://www.youtube.com/watch?v=bQ2EtLnN6KQ)

- [AWS Assume IAM Role - Step by Step tutorial (Part-3)](https://www.youtube.com/watch?v=MkiWa31iV6U)

- [AWS - Switch Roles / Cross Account Access](https://www.youtube.com/watch?v=d7R08uPS98M&t=254s) 



root account

dev-ou
dev account

test-ou
test account



Assume Role



```

{
"version": "2012-09-10",
"Statement": [
 {
  "Sid": "statement1",
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam:635163516:role/s3-access"
}
}
}

```

```
Switch Role

Account - 23523264262

Role - s3-full-access

Display Name - 

Color - 

```

Use case
--------

Vipin should have full access

- full EC2 & S3 in dev and prod

Deepak should have only access 

- read only access ec2 and s3 in dev and no access in prod


trust relationship


https://github.com/infra-ops/aws_poc/blob/master/multi_account_management/organisations/ec2/t2-micro.json

https://github.com/infra-ops/aws_poc/blob/master/multi_account_management/organisations/bucket/s3.json


Service Catalogue
------------------

https://github.com/infra-ops/aws_poc/blob/master/service_catalouge/cf/constraint.json





Production Preferrable Instances
--------------------------------


| **Instance Type**  | **vCPUs** | **Memory (GiB)** | **Processor**                           | **Network Bandwidth** | **On-Demand Pricing (per hour)** | **Spot Pricing (approx per hour)** |
|--------------------|----------|------------------|------------------------------------------|-----------------------|----------------------------------|-------------------------------------|
| **c6gn.4xlarge**  | 16       | 32               | AWS Graviton2 (ARM-based)               | Up to 25 Gbps         | $0.499                          | $0.150                              |
| **c6i.4xlarge**   | 16       | 32               | Intel Xeon Platinum 8375C (Ice Lake)    | Up to 12.5 Gbps       | $0.680                          | $0.204                              |
| **m6i.4xlarge**   | 16       | 64               | Intel Xeon Platinum 8375C (Ice Lake)    | Up to 12.5 Gbps       | $0.768                          | $0.230                              |
| **r6i.4xlarge**   | 16       | 128              | Intel Xeon Platinum 8375C (Ice Lake)    | Up to 12.5 Gbps       | $1.008                          | $0.302                              |
| **c5n.4xlarge**   | 16       | 42               | Intel Xeon Platinum 8259CL (Cascade Lake) | Up to 25 Gbps         | $0.904                          | $0.270                              |
| **m5n.4xlarge**   | 16       | 64               | Intel Xeon Platinum 8259CL (Cascade Lake) | Up to 25 Gbps         | $1.040                          | $0.310                              |
| **r5n.4xlarge**   | 16       | 128              | Intel Xeon Platinum 8259CL (Cascade Lake) | Up to 25 Gbps         | $1.344                          | $0.400                              |
| **g5.2xlarge**    | 8        | 32               | NVIDIA A10G Tensor Core GPU (GPU-Optimized) | Up to 25 Gbps    | $1.006                          | $0.300                              |
| **p4d.24xlarge**  | 96       | 1152             | NVIDIA A100 Tensor Core GPU (AI/ML)     | 400 Gbps              | $32.77                          | $9.830                              |
| **inf1.6xlarge**  | 24       | 96               | AWS Inferentia (Optimized for AI/ML Inference) | 100 Gbps      | $2.226                          | $0.670                              |



Why These Choices?
--------------------


Spring Boot is CPU and memory-intensive, so compute-optimized (C-series) or memory-optimized (R-series) instances are preferable.

Graviton3-based instances offer better price-performance for most workloads unless specific x86 dependencies exist.
Higher network bandwidth ensures lower latency and faster request processing, especially for microservices communicating frequently.

Auto-scaling and cost efficiency: Graviton instances provide up to 40% better price-performance than x86.

java spring boot
-----------------

| **Instance Type** | **vCPUs** | **Memory (GiB)** | **Processor** | **Network Bandwidth** | **On-Demand Pricing (per hour)** | **Spot Pricing (approx per hour)** |
|-------------------|-----------|------------------|---------------|-----------------------|----------------------------------|------------------------------------|
| **c7g.4xlarge**   | 16        | 32               | AWS Graviton3 | Up to 30 Gbps         | $0.536                           | $0.161                             |
| **c6i.4xlarge**   | 16        | 32               | Intel Xeon    | Up to 12.5 Gbps       | $0.680                           | $0.204                             |
| **r7g.4xlarge**   | 16        | 64               | AWS Graviton3 | Up to 30 Gbps         | $0.691                           | $0.207                             |
| **r6i.4xlarge**   | 16        | 128              | Intel Xeon    | Up to 12.5 Gbps       | $1.008                           | $0.302                             |
| **m7g.4xlarge**   | 16        | 64               | AWS Graviton3 | Up to 30 Gbps         | $0.625                           | $0.188                             |
| **m6i.4xlarge**   | 16        | 64               | Intel Xeon    | Up to 12.5 Gbps       | $0.768                           | $0.230                             |



| **Aspect**           | **ARM (Advanced RISC Machine)** | **AMD (Advanced Micro Devices)** |
|----------------------|--------------------------------|----------------------------------|
| **Architecture Type** | RISC (Reduced Instruction Set Computing) | CISC (Complex Instruction Set Computing) |
| **Power Efficiency**  | High efficiency, consumes less power | Consumes more power compared to ARM |
| **Performance**       | Optimized for parallel processing and energy efficiency | High clock speeds and raw performance for intensive workloads |
| **Use Cases**        | Mobile devices, embedded systems, cloud computing (AWS Graviton) | High-performance computing, gaming, x86-based cloud instances |
| **Instruction Set**  | Uses ARM instruction set (simpler, fewer instructions) | Uses x86-64 instruction set (more complex, optimized for multitasking) |
| **Manufacturers**    | Used by Apple (M1, M2), Qualcomm, AWS (Graviton) | Used by AMD Ryzen, EPYC, and custom cloud processors |




how many accounts you have handled in aws for your project? how to switch to multiple accounts in aws?
please mentioned following solutions with brief process in table for .md file
1. sts
2. organization
3. tower
4. catalogue
5. trust relationship


## AWS Multi-Account Management and Switching Methods  

### **How Many AWS Accounts Have You Managed?**  
I have managed **4–6 AWS accounts** in my project, covering:  
- **Development (Dev)**
- **Staging (Stage/UAT)**
- **Production (Prod)**
- **Security & Compliance**
- **Logging & Monitoring**
- **Shared Services**

### **Methods to Switch Between AWS Accounts**  

| **Method**               | **Description** | **Brief Process** |
|--------------------------|----------------|--------------------|
| **STS (Security Token Service)** | Enables temporary access to assume roles in other AWS accounts. | 1. Create an IAM role in the target account with necessary permissions.<br>2. Use `aws sts assume-role` to switch roles programmatically.<br>3. Retrieve temporary credentials and use them for API calls. |
| **AWS Organizations** | Centralized account management with consolidated billing and SCP (Service Control Policies). | 1. Create an AWS Organization and invite accounts.<br>2. Apply SCPs to enforce policies.<br>3. Use AWS SSO or IAM roles to access multiple accounts. |
| **AWS Control Tower** | Automates multi-account setup with best practices and guardrails. | 1. Deploy Control Tower to manage account lifecycle.<br>2. Use AWS SSO for account switching.<br>3. Enforce security guardrails and compliance policies. |
| **AWS Service Catalog** | Enables cross-account infrastructure provisioning via pre-approved CloudFormation templates. | 1. Create and share product portfolios across accounts.<br>2. Grant access to users/roles.<br>3. Launch services from the catalog without manual setup. |
| **Trust Relationships** | Establishes cross-account access by defining IAM role trust policies. | 1. Create an IAM role in the target account.<br>2. Modify the trust policy to allow access from another AWS account.<br>3. Assume the role via AWS CLI, SDK, or console. |
| **SCP (Service Control Policies)** | Restricts or allows specific actions across AWS accounts in an Organization. | 1. Define an SCP policy with allowed/denied actions.<br>2. Attach SCP to an AWS Organizational Unit (OU) or specific account.<br>3. Ensure IAM roles align with SCP permissions. |




| Question                                                              | Answer                                                                                                       |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **What kind of and how many Boto3-based Lambda functions have you written?** | I have written multiple Boto3-based Lambda functions for various AWS operations, including:                 |
|                                                                        | 1. **S3 Automation** - Uploading, retrieving, and managing S3 objects.                                      |
|                                                                        | 2. **DynamoDB Operations** - Reading, writing, and updating data in DynamoDB tables.                        |
|                                                                        | 3. **EC2 Instance Management** - Starting, stopping, and monitoring EC2 instances.                          |
|                                                                        | 4. **SNS & SQS Messaging** - Sending notifications and managing message queues.                              |
|                                                                        | 5. **CloudWatch Log Processing** - Analyzing and filtering CloudWatch logs.                                 |
|                                                                        | In total, I have implemented **10+ Lambda functions** utilizing Boto3 for automating AWS operations.        |
| **What benefits has the project received due to this?**                | 1. **Reduced Operational Overhead** - Automating manual tasks, reducing human intervention.                 |
|                                                                        | 2. **Cost Optimization** - Efficient resource management leading to cost savings.                           |
|                                                                        | 3. **Improved Scalability** - Serverless functions scale dynamically with demand.                           |
|                                                                        | 4. **Faster Execution & Response Time** - Automating infrastructure tasks in real-time.                     |
|                                                                        | 5. **Enhanced Security** - Automated IAM role enforcement, access logging, and compliance monitoring.       |
| **Have you ever developed any serverless app?**                        | Yes, I have developed multiple serverless applications leveraging AWS Lambda, API Gateway, DynamoDB, and S3.|
| **Give three examples of serverless applications you developed.**      | 1. **E-commerce Order Processing**: API Gateway + Lambda + DynamoDB for handling orders in a retail platform. |
|                                                                        | 2. **Automated Cloud Resource Cleanup**: Lambda functions triggered via CloudWatch to clean up unused resources. |
|                                                                        | 3. **Real-time Log Analytics**: Lambda processing CloudWatch logs and pushing insights to an S3 bucket for analysis. |





| Cyber Attack Type                          | Prevention by AWS WAF                                          |
|--------------------------------------------|---------------------------------------------------------------|
| **SQL Injection (SQLi)**                   | Blocks malicious SQL queries exploiting database vulnerabilities. |
| **Cross-Site Scripting (XSS)**             | Prevents injection of malicious scripts into web applications. |
| **Cross-Site Request Forgery (CSRF) (Indirectly)** | Mitigates CSRF by enforcing security rules on request validation. |
| **HTTP Flood (DDoS Attack)**               | Protects against high-volume bot traffic and excessive API requests. |
| **Bots & Scraping**                        | Stops automated bots, web scrapers, and content theft. |
| **Command Injection**                      | Prevents attackers from injecting system commands via user input fields. |
| **Zero-Day Exploits (Limited Protection)** | Defends against known OWASP Top 10 vulnerabilities using managed rule sets. |
| **Brute Force Attacks**                    | Blocks repeated login attempts or credential stuffing attacks. |
| **Remote File Inclusion (RFI)**            | Prevents attackers from including external malicious files. |
| **Server-Side Request Forgery (SSRF) (Limited Protection)** | Helps mitigate unauthorized internal network requests. |



# 💰 **How to Cut AWS Costs by 40% Without Sacrificing Performance**  

Many AWS workloads are **overprovisioned**, leading to unnecessary costs. **Optimizing AWS resource usage** can reduce costs by **40%** without affecting performance.  

---

## 🔹 **Key AWS Cost Optimization Strategies**  

| **Category** | **Optimization Strategies** |
|-------------|-----------------------------|
| **Rightsizing EC2 & RDS Instances** 🖥️ | 🔹 Use **AWS Compute Optimizer** to analyze underutilized EC2 instances. <br> 🔹 Switch from **t3.large to t3.medium**, saving **30%** on compute costs. <br> 🔹 Move workloads to **Graviton2 instances**, reducing cost by **20%**. |
| **Leveraging Auto Scaling & Spot Instances** 📈 | 🔹 Implement **EC2 Auto Scaling Groups** to match demand dynamically. <br> 🔹 Use **Spot Instances** for non-critical workloads, cutting compute costs by **70%**. <br> 🔹 Configure **AWS Auto Scaling cooldowns** to prevent unnecessary scaling events. |
| **Optimizing AWS Lambda & API Gateway Costs** ⚡ | 🔹 Adjust **Lambda memory configurations** to optimize execution time. <br> 🔹 **Cache API responses** using API Gateway with CloudFront, reducing **Lambda invocations by 60%**. <br> 🔹 Use **Provisioned Concurrency** only where absolutely needed to avoid cold start costs. |
| **Cleaning Up Unused Resources** 🧹 | 🔹 Identify **idle EBS volumes & unused snapshots** using AWS Trusted Advisor. <br> 🔹 Implement **lifecycle policies for S3 & logs**, archiving old data to **S3 Glacier**. <br> 🔹 Decommission **unused load balancers** and optimize networking to reduce **data transfer costs**. |

---

### 🔥 **Save Up to 40% Without Performance Degradation**  
AWS **cost optimization** is an **ongoing process**, and the best strategy depends on your workload.  

💡 **Have you implemented similar optimizations?** Let’s discuss in the comments! 🚀  



 

S3 Access Points

S3 Gateway Endpoint for S3 Access

Use PrivateLink Endpoint

Egress-Only Gateway


- [how-we-cut-40-in-nat-gateway-costs](https://medium.com/zesty-engineering/how-we-cut-40-in-nat-gateway-costs-640a9b3f9a48)

- [reduce-cost-and-improve-security-with-amazon-vpc-endpoints](https://www.kubeblogs.com/reduce-cost-and-improve-security-with-amazon-vpc-endpoints/)  
  
- [deployment-of-node-js-app-on-aws](https://medium.com/@survasepradips147/deployment-of-node-js-app-on-aws-ecs-fargate-with-terraform-and-github-actions-d67b121bd780)

- [dynamodb-expert](https://towardsaws.com/become-an-amazon-dynamodb-expert-9674a87d4ece)
- [building-a-scalable-batch-processing-serverless-pipeline-with-aws-step-functions](https://medium.com/@hobballah.yasser/building-a-scalable-batch-processing-serverless-pipeline-with-aws-step-functions-and-batch-fe13146e1e17)
- [split-cost-allocation-data-for-amazon-eks](https://medium.com/@hirsch.elad/split-cost-allocation-data-for-amazon-eks-deb59dbd344a)
- [serverless-best-practices-with-powertools](https://blog.localstack.cloud/serverless-best-practices-with-powertools/)
- [aws-terraform-2024-ecs-cluster](https://medium.com/@mrprmode/aws-terraform-2024-ecs-cluster-on-autoscaling-ec2-with-rds-8806a8147153)
- [real-time-data-pipeline-with-apache-kafka](https://medium.com/@traviszack22/real-time-data-pipeline-with-apache-kafka-2f827397cb54)
- [step-by-step-guide-to-building-an-aws-sns-application](https://medium.com/@traviszack22/step-by-step-guide-to-building-an-aws-sns-application-2bb2673d1f94)
- [reduce-cost-and-improve-security-with-amazon-vpc-endpoints](https://www.kubeblogs.com/reduce-cost-and-improve-security-with-amazon-vpc-endpoints/)










