# ALB Ingress vs NGINX Ingress - Pros and Cons

| **Feature**                       | **AWS ALB Ingress**                                                                                                                                  | **NGINX Ingress**                                                                                                                                                    |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Integration with Cloud Provider** | Native integration with AWS services like EC2, Lambda, and Route 53.                                                                                | Can be deployed on any cloud or on-premises environment with flexibility to integrate with various services.                                                           |
| **Scalability**                   | Auto-scaling based on AWS ALB's built-in auto-scaling capabilities.                                                                                 | Requires manual configuration for scaling, but supports auto-scaling when deployed on Kubernetes clusters with proper configuration.                                   |
| **Cost**                           | Free to use with AWS ALB, but you pay for ALB usage (traffic, hours, and scaling).                                                                  | Free and open-source, but requires resources for NGINX pods and potential additional licensing costs for advanced features.                                             |
| **Support for HTTP/2 and WebSockets** | Supports HTTP/2 and WebSocket natively.                                                                                                               | Supports HTTP/2 and WebSocket with proper configuration, but needs additional resources like NGINX Plus for some advanced features.                                   |
| **Custom Features**               | Limited to the ALB functionality provided by AWS, such as host/path-based routing, SSL termination, and WebSocket support.                           | Highly customizable with advanced features like rate limiting, request/response rewrites, and more. It provides more control over traffic handling and security.          |
| **SSL/TLS Termination**           | Built-in SSL/TLS termination at the load balancer level.                                                                                           | Supports SSL/TLS termination, but can be configured to do so at different layers (Ingress controller or application).                                                  |
| **Ease of Setup**                 | Simplified setup if running within AWS. Requires minimal configuration for AWS-based applications.                                                 | Requires setting up an NGINX controller and configuration files, which can be complex in certain environments.                                                       |
| **Logging and Monitoring**        | Provides basic monitoring and logging via AWS CloudWatch and ALB logs.                                                                             | Offers detailed logging and monitoring capabilities via integration with Prometheus, Grafana, and various logging tools like Fluentd.                                  |
| **Security**                      | Integrated with AWS security features, including IAM roles, security groups, and WAF (Web Application Firewall).                                     | Flexible security controls, but requires configuration for things like WAF or OAuth. Can be integrated with external security tools.                                  |
| **Community and Support**         | Limited to AWS support and forums.                                                                                                                  | Strong open-source community with contributions, extensive documentation, and support from NGINX.                                                                  |




# Special Features of AWS ALB Ingress

| **Feature**                          | **Description**                                                                                                                                                      |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Native AWS Integration**           | ALB Ingress is fully integrated with AWS services like EC2, Lambda, Route 53, and ECS, making it easy to manage within the AWS ecosystem.                            |
| **Automatic SSL/TLS Termination**    | Supports automatic SSL/TLS termination for secure connections, offloading the encryption process from backend services, reducing complexity and improving performance. |
| **Dynamic Scaling**                  | Built-in support for auto-scaling based on traffic, leveraging AWS ALB's scaling capabilities to adjust capacity automatically.                                        |
| **Path and Host-Based Routing**      | Allows routing traffic based on hostnames and URL paths, enabling fine-grained control over how requests are directed to different services or microservices.         |
| **AWS WAF and Security Features**    | ALB Ingress integrates seamlessly with AWS Web Application Firewall (WAF) for enhanced security and DDoS protection, as well as IAM roles and security groups.       |

# Special Features of NGINX Ingress Controller

| **Feature**                          | **Description**                                                                                                                                                      |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Highly Customizable**              | NGINX Ingress offers advanced configurations for request routing, load balancing, and custom error pages, allowing full control over traffic management.                |
| **Advanced Traffic Management**      | Supports features like rate limiting, request/response rewrites, load balancing algorithms, and session persistence for better traffic handling.                       |
| **Comprehensive SSL/TLS Termination**| Provides support for SSL/TLS termination with custom certificates, backend SSL, and integration with secret management tools for improved security.                     |
| **Integration with Prometheus and Grafana** | NGINX Ingress has built-in support for monitoring through Prometheus and Grafana, enabling detailed insights into traffic patterns and system performance.              |
| **Support for External Authentication** | NGINX Ingress integrates with external authentication systems such as OAuth, JWT, and third-party identity providers for secure API and service access.  |



| **Feature**                     | **Nginx Ingress**                                                                 | **ALB Ingress**                                                                 |
|----------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Management of Ingresses**      | Manages all Ingress resources of applications in EKS cluster.                     | Manages the life cycle of the Application Load Balancer instance.               |
| **Deployment Environment**       | Open-source, works across any Kubernetes environment (on-prem, cloud providers).  | AWS-specific, designed to work within AWS environments.                        |
| **Load Balancer**                | Uses Nginx as a reverse proxy and load balancer.                                  | Uses AWS Application Load Balancer (ALB).                                      |
| **Routing Type**                 | Routes traffic for Layer 7 (HTTP/HTTPS) and handles SSL termination.             | Routes traffic based on host headers, paths, and more (Layer 7 routing).       |
| **Customization**                | Feature-rich with extensive customization options for traffic routing and SSL termination. | Integrates with AWS services like AWS WAF and ACM, and leverages AWS-specific features. |
| **Integration with AWS Services**| Not integrated with AWS services.                                                 | Seamless integration with AWS services like WAF, ACM, and other AWS-native features. |

| **Feature**                     | **Static IP**                                                                 | **Elastic IP**                                                               |
|----------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Definition**                   | A Static IP is a fixed, non-changeable IP address that is assigned to a device or server. | An Elastic IP is a static IPv4 address designed for dynamic cloud computing. |
| **Use Case**                     | Typically used for on-premise devices or servers requiring a fixed IP address. | Primarily used in cloud environments like AWS to maintain a persistent IP even if resources are moved. |
| **Modification**                 | Once assigned, the IP address is fixed and cannot be changed.                 | Can be associated and disassociated with any instance in an AWS account.    |
| **Dynamic Assignment**           | Not dynamic. The IP is static and cannot be re-assigned to another instance without manual intervention. | Can be re-associated with any instance or resource in AWS without downtime. |
| **Cost**                         | Generally, there is no additional cost for a static IP address in traditional environments. | AWS charges for Elastic IP addresses when they are not associated with a running instance. |
| **Cloud Integration**            | Not specific to cloud environments; typically used for on-premises or traditional hosting. | Specifically designed for cloud services (e.g., AWS).                       |
| **Portability**                  | Static IPs are fixed and tied to the device or server.                        | Elastic IPs are portable within the cloud environment and can be reassigned. |
| **Failover/Redundancy**          | No automatic failover or redundancy built in.                                | Can be used for automatic failover and disaster recovery in cloud environments. |



What is an AWS identity provider?
Identity provider lets an external user have some permissions inside AWS. In our case, this identity provider will give permissions to the ALB ingress controller Service Account.
To create it, we need 3 elements: the identity provider type, the audience and the provider Url. The type will be “OpenId Connect” and the audience will be “sts.amazonaws.com”.
And to know the provider url you will need to execute the following command:
aws eks describe-cluster --name <CLUSTER_NAME> --query “cluster.identity.oidc.issuer” --output text


Ingress Creation
Following the steps in the numbered blue circles in the above diagram:
The controller watches for Ingress events from the API server. When it finds Ingress resources that satisfy its requirements, it starts the creation of AWS resources.
An ALB is created for the Ingress resource.
TargetGroups are created for each backend specified in the Ingress resource.
Listeners are created for every port specified as Ingress resource annotation. If no port is specified, sensible defaults (80 or 443) are used.
Rules are created for each path specified in your Ingress resource. This ensures that traffic to a specific path is routed to the correct TargetGroup created.



AWS ALB Ingress controller supports two traffic modes: instance mode and IP mode.
instance mode: Ingress traffic starts from the ALB and reaches the NodePort opened for your service. Traffic is then routed to the container Pods within cluster. The number of hops for the packet to reach its destination in this mode is always two.
ip mode: Ingress traffic starts from the ALB and reaches the container Pods within cluster directly. In order to use this mode, the networking plugin for the Kubernetes cluster must use a secondary IP address on ENI as pod IP, aka AWS CNI plugin for Kubernetes. 



Whenever an Ingress resource is created, The ingress controller will:
Create an ALB and Listener(80/443) if they do not exist yet
Create a target group on the ALB for each K8S service.
Update Path and Host ingress configs on each target group
Add only the VMs where the backend pods are running (instead of all VMs) to the target group


How does #kubelet manages the life-cycle of a #pod 
Pod Manifest Sync:
Kubelet continuously watches the directory /etc/kubernetes/manifests (or a specified directory) for pod manifest files. These manifest files contain the configuration details of the pods that should be running on the node.
Pod Creation:
When Kubelet detects a new pod manifest file, it reads the configuration and creates the pod's container(s) based on the specifications in the manifest
Pod Updates:
Kubelet monitors the pod manifest files for changes. If it detects an update (e.g., changes to the image version or configuration), it performs the necessary actions to update the running pod.
Updates may involve stopping the existing containers and creating new ones with the updated settings.

Health Monitoring:
Kubelet continually checks the health of the containers within the pods it manages. It can perform health checks defined in the pod's configuration, such as HTTP or TCP probes.
Garbage Collection:
Kubelet performs garbage collection to ensure that resources are cleaned up properly. It removes pods that are no longer needed or are past their TTL (time-to-live) based on policies defined in the pod's configuration.
Reporting Status:
Kubelet reports the status of the pods and their containers to the Kubernetes API server. This includes information about whether the pods are running, the state of their containers, and any issues or failures.

Resource Management:
Kubelet is responsible for enforcing resource constraints and limits defined in the pod's configuration. It ensures that pods do not consume more CPU or memory than allocated, and it can throttle or evict pods that exceed their limits
Pod Termination:
When a pod is no longer needed or has been deleted by the user, Kubelet gracefully terminates the pod by stopping its containers and cleaning up associated resources, including network, storage, and volumes.
Event Handling:
Kubelet generates events related to pod and container life cycle changes. These events are sent to the Kubernetes Event API and can be used for monitoring, debugging, and auditing purposes.

Overall, Kubelet acts as the node-level supervisor for pods, ensuring that they are created, updated, and terminated according to the desired configurations defined in the Kubernetes API server. It also takes care of health checks, resource management, and garbage collection to maintain the desired state of pods on the node.




















