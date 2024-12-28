1. How do you uncommit the changes that have already been pushed to GitHub? 
git revert <commit-hash> 
create a new commit that undoes the changes and push it with git push

2. If there is suddenly the file is deleted in git how do you get it back? 
Use git checkout HEAD <file-path> to restore the deleted file from the latest commit

3. Can you increase the size of the root volume without shutting down the instance?

Yes, you can increase the size of the root volume without shutting down the instance by modifying the volume in the 
AWS Management Console or using the AWS CLI with the modify-volume command. After resizing, extend the filesystem inside the running instance to utilize the new space

aws ec2 modify-volume --volume-id <volume-id> --size <new-size-in-GB>
aws ec2 describe-volumes-modifications --volume-id <volume-id>
resize2fs /dev/<root-device>
xfs_growfs /

4. If you lost the .pem file then how will you connect to EC2? 

If you lost the .pem file, create a new key pair in AWS, then access the EC2 instance via an existing user with proper access (like another admin). 
Alternatively, use the Systems Manager Session Manager or create a new key pair, update the instance's ~/.ssh/authorized_keys file via another instance or EBS volume attachment

5. S3 bucket having a policy for only read-only but you’re having full access for you? Can you modify s3 objects? 
No, you cannot modify S3 objects because the bucket policy enforces read-only access, and bucket policies override individual user permissions. To modify objects, the bucket policy must explicitly allow write access

6. Difference between Classic ELB and Application ELB?
7. How many subnets are assigned to the routing table? 

A single routing table can be associated with multiple subnets, but each subnet can be associated with only one routing table at a time
a routing table can be associated with up to 200 subnets by default



8. In your VPC all IPS are finished you require resources how to provision it? 

If all IPs in your VPC are used, you can either:

Add a new subnet with a larger or different CIDR block in the same VPC.
Expand the VPC's CIDR block using the VPC CIDR block association feature, if there's available IP space

9. Are you only using cloud watch for monitoring?
10.If your using load balancing in 2 availability zones den which load balancer you should use?


If you're using load balancing across two availability zones, you should use an Application Load Balancer (ALB) or a Network Load Balancer (NLB), depending on your use case:

ALB: Best suited for HTTP/HTTPS traffic with advanced routing, URL path-based routing, and SSL termination.
NLB: Ideal for handling TCP/UDP traffic with high performance and low latency, especially for non-HTTP traffic.

11. can you write docker file where Linux env condition deploy static webserver 
# Use an official Nginx image as the base
FROM nginx:latest

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy static website files to the web server's root directory
COPY ./static-site/ .

# Expose port 80 for the web server
EXPOSE 80

# Start Nginx web server
CMD ["nginx", "-g", "daemon off;"]


12. Is it possible to run any VM in AWS without creating any EC2 instance ? 
No, it is not possible to run a virtual machine (VM) in AWS without creating an EC2 instance, as EC2 (Elastic Compute Cloud) 
is the service that provides VM-like compute resources in AWS. If you need to run VMs, you must create EC2 instances.

However, you can use services like AWS Lightsail for simpler VM provisioning or AWS Fargate for containerized applications, 
but these still rely on EC2 under the hood

13. I want to create a pipeline in Jenkins which needs to have 10 different stages and based on my input it needs to execute some stages not every stages how you will configure that .



14. What are the Terraform modules? Have used any modules in the project?
15. Is it possible to configure communication between 2 servers those are having private access
16. What happens when you delete /var/lib/docker/overlay?
 deleting /var/lib/docker/overlay removes the filesystems of your containers, leading to potential data loss and failure of containers, 
 so it's advisable to be cautious when performing this action
 
17. Write a simple script that calls with “Foo” prints “bar” and when called with “bar” prints “foo”. Every other option should print “Try 
again”?

def respond(input_value):
    if input_value == "Foo":
        print("bar")
    elif input_value == "bar":
        print("foo")
    else:
        print("Try again")

# Test the function
input_value = input("Enter a value: ")
respond(input_value)


18. Tell all the scenarios too implement the security in Kubernetes.
Authentication and Authorization
RBAC (Role-Based Access Control): Implement RBAC policies to control user and service account permissions, ensuring that only authorized users or services can perform specific actions.
Service Accounts: Use service accounts for applications running in the cluster and limit their permissions to the minimum required.
API Server Authentication: Enable and configure authentication mechanisms (e.g., certificates, OpenID, or OAuth) for the Kubernetes API server.

 Network Security
Network Policies: Use Kubernetes Network Policies to control the communication between Pods and services, restricting access to sensitive applications.
Service Mesh: Implement a service mesh (e.g., Istio) to enforce mTLS (Mutual TLS) for encrypted communication between services.
Ingress and Egress Controls: Set up strict ingress and egress rules using Network Policies to control traffic flow in and out of the cluster

Secrets Management
Kubernetes Secrets: Store sensitive data such as passwords, tokens, and keys in Kubernetes Secrets, ensuring they're encrypted at rest.
External Secrets Management: Use tools like Vault, AWS Secrets Manager, or Google Secret Manager to securely store and manage secrets.
Encrypt Secrets at Rest: Enable encryption for Secrets in etcd to ensure sensitive data is encrypted at rest.


Container Security
Image Scanning: Regularly scan container images for vulnerabilities using tools like Clair, Trivy, or Anchore.
Image Signing and Verification: Use Notary or Cosign to sign and verify container images to ensure that only trusted images are deployed.
Use Read-Only File Systems: Run containers with read-only file systems to prevent any modifications to the container's filesystem

Patch Management and Upgrades
Regular Security Patches: Regularly update your Kubernetes components and container runtimes to patch security vulnerabilities. Automate patching where possible.
Version Management: Ensure that the cluster is running the latest stable Kubernetes version with security patches applied.
Security Audits and Compliance: Perform regular security audits and compliance checks to ensure your Kubernetes environment adheres to security best practices.

Logging and Monitoring
Centralized Logging: Set up centralized logging with tools like ELK Stack or Fluentd to collect logs from the entire Kubernetes cluster for security monitoring.
Prometheus and Grafana: Monitor resource usage and collect metrics with Prometheus, using Grafana for visualization. Set up alerts for suspicious activities like unusually high CPU/memory usage or failed login attempt

Cluster Security
API Server Security: Restrict access to the Kubernetes API server using IP whitelisting, authentication, and authorization.
etcd Encryption: Enable encryption for the etcd data store, which holds sensitive information, such as secrets and cluster configurations.
Control Plane Security: Use strong authentication mechanisms for your Kubernetes control plane components (e.g., etcd, API server), and secure inter-component communication using certificates.




19. Your EKS application is experiencing higher than expected traffic. How would you automatically scale the Pods?

Enable Horizontal Pod Autoscaler (HPA) in your EKS cluster to automatically scale the number of Pods based on CPU or memory usage.
Use metrics-server or Prometheus to gather resource metrics like CPU and memory for scaling decisions.
Define HPA using kubectl or YAML, specifying desired metrics (e.g., CPU > 80%) to trigger scaling up or down


20. Your team needs to be alerted when the CPU usage of any Pod in your EKS cluster exceeds 80% for more than 5 minutes. How would you set this up?

Use Amazon CloudWatch to collect Kubernetes metrics from your EKS cluster using the kube-state-metrics and cloudwatch-agent DaemonSet.
Create a CloudWatch alarm with a threshold of 80% CPU usage for more than 5 minutes for any pod.
Set up a CloudWatch alarm action to send notifications to an SNS topic, which will alert your team




21. Your team wants a Grafana dashboard to visualize the HTTP request latency of your applications running in EKS. How would you achieve this?

Set up Prometheus on your EKS cluster to scrape metrics from your applications using the Prometheus Operator or kube-prometheus.
Use Prometheus metrics like http_request_duration_seconds to collect HTTP request latency data.
Connect Grafana to Prometheus as a data source and create a dashboard to visualize the HTTP request latency metrics
