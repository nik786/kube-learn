

# AWS IAM & Access Management Concepts

| Term               | Description                                                                                          | Key Purpose                                                                 |
|--------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| IAM User           | A unique identity for a person or application with long-term credentials.                            | Direct access to AWS resources using username/password or access keys.      |
| IAM Role           | An identity with permission policies that can be assumed by users, services, or accounts.            | Grant temporary access without long-term credentials.                        |
| IAM Group          | A collection of IAM users managed as a single entity.                                                | Simplify permission management across multiple users.                        |
| AWS SSO            | Centralized access management across multiple AWS accounts and business apps using SSO identity.     | Federated access using corporate credentials (e.g., Azure AD, Okta).         |
| Landing Zone       | A secure, scalable multi-account AWS environment based on best practices.                           | Establishes initial cloud foundation with governance, security, and network baselines. |
| AWS Organization   | A hierarchy of AWS accounts with consolidated billing and service control policies.                   | Manage multiple AWS accounts centrally under one root account.              |
| AWS Control Tower  | An AWS service to automate setup of a landing zone using AWS best practices.                         | Simplifies governance and compliance across multiple AWS accounts.          |
| Trust Relationship | A policy that defines which entities (users, roles, accounts) can assume a role.                     | Enables cross-account or service-to-service role assumption.                 |
| STS (Security Token Service) | A web service that issues temporary, limited-privilege credentials for IAM roles or federated users. | Provides secure, time-limited access to AWS resources.                      |




# Allowing Traffic to a Security Group

| Source Type        | How to Allow                                        | Example                            |
|--------------------|-----------------------------------------------------|------------------------------------|
| Specific Subnet    | Add CIDR (e.g., 10.0.1.0/24) as inbound source       | Allow HTTP from 10.0.1.0/24        |
| Another SG         | Add source as Security Group ID                     | Allow HTTPS from sg-bastion        |







AWS CloudTrail  vs AWS Config
--------------------------------


| Feature                                           | **AWS CloudTrail**                                         | **AWS Config**                                           |
|---------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| **Purpose**                                       | Tracks and logs API activity across your AWS account.       | Monitors and records AWS resource configurations over time. |
| **Focus**                                         | Event logging and auditing for API calls.                   | Configuration monitoring and compliance of resources.      |
| **What It Tracks**                                | API calls, user identity, time of request, source IP, and service events. | Resource configurations, relationships, and changes over time. |
| **Scope**                                         | Tracks activity for all AWS services and regions.           | Monitors configurations of specific resources you specify. |
| **Change Detection**                              | Detects changes based on API calls (who made the change and when). | Continuously tracks configuration changes and evaluates compliance. |


VPC Peering vs Transit Gateway
--------------------------------



| **Aspect**            | **VPC Peering**                                                   | **Transit Gateway**                                               |
|-----------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| **Connectivity**      | Point-to-point; connects two VPCs directly.                        | Hub-and-spoke model; connects multiple VPCs through a central hub. |
| **Scalability**       | Hard to scale with many VPCs; needs multiple peering connections. | Highly scalable; supports thousands of VPCs.                       |
| **Routing**           | Manual route setup in each VPC.                                   | Simplified routing through the central Transit Gateway.            |
| **Cost**              | No additional cost for the peering link (charged for data).       | Additional charges for Transit Gateway usage and data transfer.    |



HPA VS VPA
-------------

| Feature | HPA (Horizontal Scaling) | VPA (Vertical Scaling) |
|---------|--------------------------|------------------------|
| Scaling Type | Adds or removes instances based on CPU/memory usage. | Adjusts CPU/memory allocation for existing instances. |
| Use Case | Best for handling high traffic by launching more instances. | Best for optimizing resource usage of existing instances. |
| Impact on Instances | Creates new instances or terminates extra ones dynamically. | Restarts instances to apply new resource limits. |
| Works Well With | Stateless applications that can scale out easily. | Stateful applications where scaling out is not feasible. |



AWS NLB VS AWS ALB
--------------------

| Feature                                             | **ALB (Application Load Balancer)**                         | **NLB (Network Load Balancer)**                          |
|-----------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| **Layer of OSI Model**                              | Operates at the application layer (Layer 7)                 | Operates at the transport layer (Layer 4)                 |
| **Traffic Routing**                                 | Routes traffic based on content                            | Deals with IP addresses and ports                         |
| **Target Types**                                    | Supports EC2 instances, IP addresses, and containers       | Primarily supports EC2 instances                          |
| **Protocols Supported**                             | Supports HTTP and HTTPS                                    | Supports TCP, UDP, and TLS (Transport Layer Security)     |
| **DNS and Scaling**                                 | Provides a single DNS name, automatically scales as traffic increases | Provides a static IP address per Availability Zone       |
| **Health Checks**                                   | Supports HTTP and HTTPS health checks                      | Supports TCP health checks                                |
| **Use Case**                                        | Ideal for advanced routing based on content or container services | Ideal for low-latency, high-throughput communication with TCP/UDP traffic |



AWS ALB VS CLASSIC ALB
-------------------------

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


AWS ELB VS AWS NLB
-------------------

| **Aspect**          | **ELB (Classic Load Balancer)**                                       | **NLB (Network Load Balancer)**                                              |
|---------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Layer**           | Operates at Layer 4 (TCP) and Layer 7 (HTTP/HTTPS).                  | Operates strictly at Layer 4 (TCP, UDP).                                     |
| **Performance**     | Moderate performance; not suitable for extreme traffic.              | Ultra-high performance; handles millions of requests per second.             |
| **IP Support**      | No static IP; uses DNS-based name resolution.                        | Supports static IPs and Elastic IPs per AZ.                                  |
| **Target Types**    | Supports EC2 instances only.                                          | Supports EC2 instances, IP addresses, and Lambda functions.                  |
| **Health Checks**   | HTTP-based health checks.                                             | TCP, HTTP, HTTPS health checks with fast response.                           |



 ALB Ingress  vs API Gateway 
 -------------------------------

 

| No. | Feature                        | ALB Ingress                                      | API Gateway                                      |
|-----|--------------------------------|--------------------------------------------------|--------------------------------------------------|
| 1   | **Primary Use Case**           | Mainly used for load balancing HTTP/S traffic to Kubernetes or EC2 services. Ingress in Kubernetes primarily works at the Application Layer (Layer 7)  | Primarily used for managing and routing API requests to backend services.  API Gateway primarily operates at the Application Layer (Layer 7) |
| 2   | **Traffic Type**               | Supports HTTP, HTTPS, WebSocket, and gRPC protocols | Primarily designed for HTTP, REST, WebSocket, and HTTP/2 APIs |
| 3   | **Traffic Management**         | Routes traffic based on HTTP host and path rules | Supports more complex API routing, rate limiting, and authorization |
| 4   | **Scaling**                    | Automatically scales with traffic and integrates directly with Kubernetes Ingress | Automatically scales based on the number of API calls, supports throttling and rate limiting |
| 5   | **Authentication & Authorization** | Supports basic authentication and integration with AWS IAM for access control | Provides built-in support for AWS IAM, Lambda authorizers, and Amazon Cognito for API access control |


ALB VS ALB INGRESS
------------------------


| Feature                          | ALB                                                                 | ALB Ingress                                                                                   |
|----------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Type**                         | Fully managed Layer 7 load balancer for distributing web traffic.  | A Kubernetes controller that integrates ALB with Kubernetes Ingress resources.              |
| **Purpose**                      | Acts as a load balancer for web applications, routing traffic based on host and path. | Manages Ingress resources in Kubernetes, dynamically creating and configuring ALBs.        |
| **Traffic Routing**              | Routes HTTP/HTTPS traffic to targets like EC2, ECS, and Lambda.    | Provides Kubernetes native support to route traffic using ALB within a Kubernetes cluster.  |
| **TLS Termination**              | Supports TLS termination, where certificates can be uploaded and managed via AWS ACM. | TLS termination via ALB, with support for Kubernetes Secret integration for SSL certificates. |
| **Health Checks**                | Built-in health checks for targets.                               | Uses Kubernetes probes and health checks to configure ALB target health status.            |


APIGATEWAY VS ALB
------------------

| Aspect                | API Gateway                                                | Application Load Balancer (ALB)                                |
|------------------------|------------------------------------------------------------|------------------------------------------------------------------|
| **Use Case**           | Ideal for serverless apps, microservices, APIs             | Best for web applications, containers, microservices             |
| **Protocol Support**   | REST, HTTP, WebSocket                                       | HTTP, HTTPS                                                      |
| **OSI Layer**          | Layer 7 (Application Layer)                                 | Layer 7 (Application Layer)                                      |
| **Traffic Management** | Supports throttling, caching, rate limiting                | Handles high throughput with host/path-based routing             |
| **Security**           | Built-in request validation, throttling, WAF integration   | Integrates with AWS WAF and security groups                      |
| **High Traffic Suitability** | May need usage plan tuning; suitable for moderate to high loads | Handles large-scale traffic natively with auto scaling   |
| **Domain Handling**    | Requires mapping with custom domain                        | Provides AWS-managed DNS name out of the box                     |
| **Cost Model**         | Pay per request                                            | Pay per hour + Load Balancer Capacity Units (LCUs)              |



Nginx Ingress vs Gateway
--------------------------



| Feature                        | NGINX Ingress Controller                         | Kubernetes Gateway API                            | OSI Layer(s)       |
|-------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------|
| API Maturity                  | Stable and widely used since early K8s versions  | Relatively new, evolving Kubernetes standard     | Layer 7 (HTTP)     |
| Configuration Model           | Annotations, config maps, and Ingress resources  | Declarative CRDs (Gateway, HTTPRoute, etc.)      | Layer 7 (HTTP)     |
| Extensibility                 | Limited, relies on custom NGINX configs          | Extensible via standard resource model           | Layer 7 (HTTP)     |
| Layer of Operation            | Primarily L7 (HTTP/HTTPS), some L4 (TCP/UDP)     | Native L4 (TCP/UDP) and L7 (HTTP/HTTPS) support  | Layer 4 & Layer 7  |
| Multi-Tenant Support          | Limited, requires careful annotation use         | Built-in multi-tenancy with role separation       | Layer 7 (HTTP)     |
| Ecosystem & Controller Choice| NGINX-specific (open-source or plus edition)      | Multiple controllers (e.g., Istio, Envoy, HAProxy)| Layer 4 & 7        |
| Gateway Flexibility           | Single-purpose (mostly HTTP routing)             | Defines Gateways, Routes, Listeners independently| Layer 4 & 7        |
| TLS Management                | Via annotations and secrets per Ingress          | Native TLS config in Gateway and HTTPRoute CRDs  | Layer 6 (TLS)      |
| Traffic Splitting             | Basic support via annotations                    | First-class support (weighted routes, filters)   | Layer 7 (HTTP)     |
| Observability & Status        | Limited, varies by controller                    | Standardized status fields for Gateway & Route   | Layer 7 (HTTP)     |






Ingress Controller vs Ingress Resource
-----------------------------------------



| **Aspect**            | **Ingress Controller**                                                                       | **Ingress Resource**                                                                          |
|------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Definition**         | A Kubernetes component that implements the rules defined in Ingress resources.              | A Kubernetes object that defines routing rules for HTTP/S traffic to services in the cluster. |
| **Role**               | Acts as a load balancer or reverse proxy to enforce Ingress rules.                          | Specifies host/path-based routing, TLS settings, and backend services.                        |
| **Installation**       | Needs to be installed separately (e.g., NGINX, Traefik, HAProxy).                           | Created and managed via `kubectl` as a native Kubernetes resource.                            |
| **Function Dependency**| Cannot function without Ingress resources to interpret.                                     | Requires an Ingress Controller to actually enforce the defined rules.   









| **Aspect**              | **NGINX Ingress**                                                                 | **ALB Ingress**                                                                 |
|-------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Controller Type**     | Open-source controller running inside the Kubernetes cluster.                     | AWS-managed controller using ALB outside the cluster.                           |
| **Traffic Routing**     | Uses Ingress rules for routing based on host and path.                            | Uses ALB features for host, path, and header-based routing.                     |
| **TLS Termination**     | Uses Kubernetes Secrets for SSL certificates.                                     | Supports AWS ACM and Kubernetes Secrets for SSL.                                |
| **Scaling**             | Scales via Kubernetes HPA (Horizontal Pod Autoscaler).                            | Automatically scales with ALB, independent of cluster.                          |
| **Platform Dependency** | Platform-agnostic; works on any Kubernetes setup.                                 | AWS-specific; works only with EKS or Kubernetes clusters on AWS.                |


Nginx Vs Apache
-------------------


| Feature                              | **Nginx**                                               | **Apache**                                           |
|--------------------------------------|---------------------------------------------------------|------------------------------------------------------|
| **Model**                            | Event-driven, asynchronous model                        | Process-driven, synchronous model                    |
| **Concurrency**                      | High concurrency, handles static content efficiently     | Better for handling dynamic content (via modules)     |
| **Configuration Syntax**            | Simpler, more straightforward configuration syntax       | More flexible but can be complex                     |
| **Resource Usage**                   | Lower memory and CPU usage under high loads             | Higher resource consumption, especially for large traffic |
| **Module Support**                   | Uses dynamic modules, requires recompiling for changes  | Supports dynamically loading modules at runtime       |




NACL VS SG
---------------


| Feature                                              | **SG (Security Group)**                                     | **NACL (Network Access Control List)**                      |
|------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| **Operates at**                                      | Instance level                                             | Subnet level                                                |
| **Rules Supported**                                  | Supports only allow rules                                  | Supports both allow and deny rules                          |
| **State**                                            | Stateful: Return traffic is automatically allowed regardless of any rules | Stateless: Return traffic must be explicitly allowed by rules |
| **Rule Evaluation**                                  | We evaluate all rules before deciding whether to allow traffic | We process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic |
| **Traffic Control**                                  | Controls both inbound and outbound traffic at the instance level | Controls both inbound and outbound traffic at the subnet level |




AWS Fargate and EC2
--------------------


| Feature             | AWS Fargate                                         | Amazon EC2                                         |
|---------------------|-----------------------------------------------------|----------------------------------------------------|
| **Management**       | Fully managed by AWS (no server management)         | You manage the EC2 instances (OS, scaling, patching)|
| **Pricing**          | Pay per task based on CPU and memory                | Pay per running instance (regardless of usage)      |
| **Scalability**      | Auto-scales tasks automatically                     | Requires manual or auto-scaling setup               |
| **Use Case**         | Ideal for simple, serverless container workloads    | Suitable for full control over infrastructure       |

> ✅ Fargate is serverless and easier to manage, while EC2 offers more control and customization.




EC2 VS LAMBDA
---------------


| **Aspect**          | **EC2**                                                                 | **AWS Lambda**                                                                 |
|---------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Type**            | Virtual machines with full OS control.                                   | Serverless functions triggered by events.                                        |
| **Pricing**         | Pay for uptime (per second/hour).                                        | Pay per request and execution time (ms).                                         |
| **Scaling**         | Manual or auto-scaling (requires setup).                                 | Auto-scales instantly based on events.                                           |
| **Start Time**      | Slower start due to provisioning.                                        | Fast start; may have cold start delay.                                           |
| **Control**         | Full control over OS, software, and environment.                         | No server management; limited environment customization.                         |
| **Use Case**        | Ideal for long-running apps, custom stacks, and legacy systems.          | Ideal for short-lived, event-driven workflows like APIs, triggers, automation.   |






| Component       | Description                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------|
| `def`           | Used to define a function. The handler name can be customized (e.g., `lambda_handler`).                  |
| **Handler Name** | The name of the function that AWS Lambda invokes (default is `lambda_handler`, but it can be changed).   |
| **Event**       | The input data passed to the handler function.                                                           |
| **Context**     | Provides runtime information to the handler, such as execution time, request ID, and log group details.  |



| **Aspect**           | **ARM (Advanced RISC Machine)** | **AMD (Advanced Micro Devices)** |
|----------------------|--------------------------------|----------------------------------|
| **Architecture Type** | RISC (Reduced Instruction Set Computing) | CISC (Complex Instruction Set Computing) |
| **Power Efficiency**  | High efficiency, consumes less power | Consumes more power compared to ARM |
| **Performance**       | Optimized for parallel processing and energy efficiency | High clock speeds and raw performance for intensive workloads |
| **Use Cases**        | Mobile devices, embedded systems, cloud computing (AWS Graviton) | High-performance computing, gaming, x86-based cloud instances |
| **Instruction Set**  | Uses ARM instruction set (simpler, fewer instructions) | Uses x86-64 instruction set (more complex, optimized for multitasking) |
| **Manufacturers**    | Used by Apple (M1, M2), Qualcomm, AWS (Graviton) | Used by AMD Ryzen, EPYC, and custom cloud processors |





Parallelism vs Concurrency
------------------------------


| Aspect                  | Concurrency                                                                                      | Parallelism                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Definition**          | Managing multiple tasks and their interactions, allowing them to make progress concurrently.    | Breaking down tasks into smaller units of work that can be executed simultaneously.            |
| **Purpose**             | Improves responsiveness and resource utilization in systems with shared resources.              | Speeds up computations and achieves better throughput.                                         |
| **Focus**               | Task management and coordination.                                                               | Exploiting multi-core processors or distributed systems for simultaneous execution.            |
| **Example Use Case**    | Handling multiple user requests in a web server.                                                | Running large-scale data processing across multiple cores or machines.                         |
| **Key Benefit**         | Enhanced responsiveness and efficient use of shared resources.                                  | Higher performance and efficiency in computations.                                             |


                              

Placement Group
-----------------

| **Aspect**         | **Details**                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **Definition**     | A Placement Group is a logical grouping of EC2 instances within a single Availability Zone or across multiple AZs to influence instance placement. |
| **Types**          | - **Cluster**: Low latency, high throughput in a single AZ (ideal for HPC, tightly-coupled workloads).<br>- **Spread**: Distributes instances across hardware to reduce correlated failures (ideal for critical instances).<br>- **Partition**: Divides instances into isolated partitions (used in large distributed systems like HDFS or Cassandra). |
| **Use Cases**      | - High-performance computing (HPC) <br> - Distributed big data apps <br> - Resilient critical applications <br> - Low-latency workloads needing high network bandwidth |



AWS Shield VS AWS WAF
-----------------------


| **Aspect**                 | **AWS WAF (Web Application Firewall)**                                       | **AWS Shield**                                                                 |
|----------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Purpose**                | Protects web apps from common exploits like SQLi, XSS, etc.                  | Protects against DDoS attacks on AWS infrastructure and applications           |
| **Protection Type**        | Application-layer (Layer 7)                                                 | Network and transport-layer (Layer 3/4), with advanced DDoS mitigation         |
| **Custom Rules**           | Supports custom rules for filtering IPs, headers, query strings, etc.       | No custom rules; works automatically with standard or advanced protection      |
| **Integration**            | Integrates with ALB, CloudFront, and API Gateway                            | Works with all AWS services, enhanced with AWS Shield Advanced for deeper insights |
| **Pricing**                | Pay-per-request with rule-based charges                                     | Shield Standard: Free; Shield Advanced: Subscription-based                     |

### ✅ Sample Rule Set to Prevent Attacks

| **Attack Type**  | **Rule in AWS WAF**                                                   |
|------------------|------------------------------------------------------------------------|
| **DDoS**         | Use AWS Shield Standard/Advanced + WAF rate-based rule: <br> `RateLimit > 2000 requests/5 min from IP` |
| **XSS**          | Create WAF rule to match strings like `<script>` in query strings, body, headers. <br> Use `StringMatch`, `RegexPatternSet` to block malicious payloads |






User-Group-Policy-Roles
----------------------------


| AWS Concept | Definition | Purpose | Credential Type | Usage Scope |
|-------------|------------|---------|------------------|-------------|
| **User**    | Represents an individual identity with long-term credentials to access AWS. | Used to manage access for a person or application. | Username and password, or access keys. | Specific to one identity (e.g., a developer). |
| **Group**   | A collection of IAM users. Policies attached to a group apply to all users in it. | Used to manage permissions for multiple users at once. | Inherits from users within the group. | Easier permission management for teams. |
| **Policy**  | A JSON document that defines permissions for what actions are allowed or denied. | Grants or restricts access to AWS services and resources. | Not a credential, but a permission set. | Attached to users, groups, or roles. |
| **Role**    | An IAM identity with permission policies that can be assumed temporarily. | Grants temporary access to users, services, or apps without long-term credentials. | Uses temporary security credentials. | Ideal for cross-account access or AWS service access (e.g., EC2, Lambda). |



  
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



AWS Policy Types Comparison
----------------------------



| Policy Type            | Definition                                                                 | When to Use                                                                 | Reusability             | Scope                      | Example Use Case                                                                 |
|------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------|--------------------------|----------------------------|----------------------------------------------------------------------------------|
| Identity-based policies| Policies attached to IAM users, groups, or roles                          | To grant permissions to an identity                                          | Highly reusable          | User, Group, Role          | Allow developers to access specific S3 buckets                                  |
| Resource-based policies| Policies attached directly to AWS resources                               | To grant cross-account access to a resource                                 | Less reusable            | AWS Resource               | Grant another AWS account access to an S3 bucket                                |
| Permissions boundaries | Limits the maximum permissions an identity-based policy can grant         | To delegate permission management while setting guardrails                  | Reusable                 | IAM User or Role           | Allow developers to create roles, but only with specific permissions            |
| Organizations SCPs     | Service control policies set at the AWS Organizations level               | To manage permissions across accounts in an organization                    | Highly reusable          | AWS Account / Org Unit     | Restrict all accounts from disabling CloudTrail                                 |
| Access Control Lists   | Legacy feature for controlling access to S3 and some other resources       | For simple, limited control, mostly for legacy compatibility                 | Not reusable             | AWS Resource               | Make an S3 object publicly readable                                              |
| Session policies       | Policies passed during temporary sessions via AWS STS                     | For fine-grained permissions during federated or temporary access           | Not reusable (per session)| Temporary IAM session     | Limit federated user's session access to only read EC2 instances                |
| Managed Policies       | Predefined or customer-created standalone policies                        | For consistent permission sets across multiple users, groups, or roles       | Highly reusable          | IAM User, Group, Role      | Attach AWS managed `AmazonEC2ReadOnlyAccess` policy to multiple users           |



LifeCycle Hook
------------------

| Aspect                        | Description                                                                                 |
|-------------------------------|---------------------------------------------------------------------------------------------|
| **Purpose**                   | Performs custom actions by pausing instances when an Auto Scaling group launches or terminates an instance. |
| **Wait State**                | When an instance is paused, it moves to a wait state.                                       |
| **Default Wait Time**         | By default, an instance remains in the wait state for 1 hour.                               |
| **Example Action**            | When a new instance is launched, the lifecycle hook pauses it, allowing custom configurations. |
| **Use Case**                  | Install software or ensure the instance is fully prepared to receive traffic while paused.   |



Auto Scaling Types Comparison
-------------------------------


| Scaling Type         | K8s Type | Scaling Pattern    | Description                                                                                     | Trigger/Condition                         | Use Case                                   | Advantage                             | Limitation                            |
|----------------------|----------|---------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|-----------------------------------------|----------------------------------------|
| Scheduled Scaling    | None     | Time-based          | Scales at set times.                                                                             | Predefined schedule                        | Predictable traffic (e.g., business hours) | Simple, predictable                   | Not reactive to traffic spikes         |
| Dynamic Scaling      | HPA      | Resource-based       | Scales based on CPU/memory usage.                                                                | Real-time usage metrics                    | Variable workloads                        | Reactive, auto-adjusts                | Needs accurate metrics                 |
| Event-Driven         | None     | Event-based          | Scales on event count or depth (e.g., queue size).                                               | Event triggers (e.g., SQS)                 | Event-driven processing                   | Fast response                          | Custom config needed                   |
| Target Tracking      | HPA      | Metric target        | Maintains a target metric like 70% CPU.                                                          | Metric + target value                      | Steady performance                        | Easy to configure                      | Slight over-provisioning               |
| Step Scaling         | HPA      | Metric-based         | Scales in steps as metrics deviate from thresholds.                                              | Threshold breaches                         | Gradual demand shifts                    | Granular control                       | Slower reaction                        |
| Simple Scaling       | HPA      | Threshold + Delay    | Triggers on one alarm with cooldowns.                                                            | Single alarm + cooldown                    | Simple, small apps                        | Easy setup                             | Not good for rapid changes             |
| Predictive Scaling   | VPA      | ML-based forecast    | Uses historical patterns and ML to adjust resources ahead of time.                               | ML predictions from past usage             | Seasonal traffic                          | Prevents latency, proactive            | Needs history, may mispredict          |





Launch Template vs Launch Configuration
-------------------------------------------


| Feature                  | Launch Templates                                                                                     | Launch Configurations                                                                 |
|--------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Flexibility**          | More flexible with advanced configuration options like instance types, block device mappings, and network settings. | Simpler and less flexible, suitable for straightforward use cases.                  |
| **Versioning**           | Supports versioning, allowing multiple versions to be created and managed.                           | No versioning; any changes require creating a new launch configuration.             |
| **Tagging**              | Supports instance tagging directly within the template.                                              | Instance tagging is not directly supported; must be done separately or via User Data. |
| **T2/T3 Unlimited**      | Configurable directly in the template, enabling burstable performance for T2/T3 instances.            | Not configurable; must be set separately during instance creation.                  |
| **Instance Types**       | Allows multiple instance types in a single template; Auto Scaling chooses the best fit.              | Only a single instance type can be specified; multiple configurations needed for multiple types. |
| **Instance Market Options** | Configurable within the template, including Spot and On-Demand Instances.                           | Configured in the Auto Scaling group, not within the launch configuration.          |
| **Resource Constraints** | Configured within the template.                                                                      | Configured in the Auto Scaling group rather than the configuration itself.          |




Storage Class Types in S3
---------------------------

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






Boto3 Resource vs Client
--------------------------




| Feature                               | **Resource**                                              | **Client**                                              |
|---------------------------------------|-----------------------------------------------------------|---------------------------------------------------------|
| **Service Access Level**              | Low-level service access                                  | Higher-level, object-oriented API                       |
| **Generation Source**                 | Generated from service description                         | Generated from resource description                      |
| **API Mapping**                       | Typically maps 1:1 with the service API                    | Uses identifiers and attributes                          |
| **Exposes**                            | Exposes subresources and collections                       |                                                         |




DNS QUERY STEPS
------------------

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



# Load Balancer Strategies

| Strategy           | Description                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| Round Robin        | Distributes requests evenly across all servers in sequence.                                 |
| Least Connections  | Routes traffic to the server with the fewest active connections.                            |
| Weighted Round Robin | Distributes requests based on assigned weights; higher weight = more traffic.             |
| Weighted Least Connections | Sends traffic to servers based on least active connections and their assigned weights. |
| IP Hash            | Uses a hash of the client's IP address to consistently route to the same server.            |
| Random             | Selects a server at random for each request.                                                |
| URL Hash           | Routes based on a hash of the requested URL, useful for caching and consistency.            |
| Response Time      | Directs traffic to the server with the fastest response time.                               |
| Geolocation-Based  | Routes requests to the nearest server based on user’s geographic location.                  |





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



Static IP vs Elastic IP
------------------------

| **Feature**                | **Static IP**                                        | **Elastic IP (AWS)**                                 |
|----------------------------|------------------------------------------------------|-------------------------------------------------------|
| **Definition**             | A fixed IP address manually assigned to a device     | A static IPv4 address managed by AWS for cloud use    |
| **Scope**                  | Used in traditional on-premises or ISP networks      | Specific to AWS and allocated to AWS accounts         |
| **Reusability**            | Typically tied to a specific device or interface     | Can be remapped to different AWS EC2 instances        |
| **Cost**                   | Usually included in network services from ISPs       | Free when associated, but charged if left unused      |











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




# What is AWS Certificate Manager ?

AWS Certificate Manager is an administration that lets you effortlessly arrangement, oversee, and send open and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) endorsements for use with AWS administrations and your inward associated assets. SSL/TLS declarations are utilized to anchor arrange interchanges and set up the character of sites over the Internet and additionally assets on private systems. AWS Certificate Manager expels the tedious manual procedure of obtaining, transferring, and reestablishing SSL/TLS endorsements.

# What is the AWS Key Management Service??

# AWS Key Management Service (KMS) - Simplified

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **What is AWS KMS?**     | A managed service to create and manage encryption keys.                     |
| **Main Use**             | Helps you encrypt and protect your data.                                    |
| **Easy to Use**          | AWS handles the setup and management of keys for you.                       |
| **Integration**          | Works well with other AWS services like S3, RDS, Lambda, etc.               |
| **Security Logging**     | Integrated with AWS CloudTrail to log key usage for auditing and compliance.|
| **Compliance Help**      | Helps meet security and regulatory requirements.                            |

> ✅ **AWS KMS makes it easy to protect your data with encryption keys managed by AWS.**


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







What is the maximum size of S3 Bucket?
5TB

An high demand of IOPS performance is expected around 15000.Which EBS volume type would you recommend?

Provisioned IOPS.

     |


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










