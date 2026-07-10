
# Questions and Answers  

1. What scripting languages are you familiar with?  

2. What are artifacts in GitLab CI?  

3. What is a private module registry in Terraform?  

4. If you delete the local Terraform state file and it's not stored in S3 or DynamoDB, how can you recover it?  

5. How do you import resources into Terraform?  



























# Questions and Answers  



 




 















1. What are the different types of Load Balancers provided by AWS?  

2. When would you choose ALB over NLB or CLB?  

3. What is a Target Group in ALB/NLB, and how does it work?  

4. What is Cross-Zone Load Balancing?  

5. What is SSL/TLS Termination, and how is it implemented in AWS ELB?  

6. How does AWS Auto Scaling integrate with Elastic Load Balancing (ELB)?  

7. How does path-based routing work in an Application Load Balancer?  

8. How can you secure your Load Balancer?  

9. What are the health checks in Elastic Load Balancer, and how do they work?  

10. How do you monitor and troubleshoot issues with an AWS Load Balancer?  

### AWS Scenario-Based Questions  

1. Your team needs to deploy a web application across multiple regions for disaster recovery. How would you design the deployment to ensure minimal downtime during a regional failure?  

2. A client’s application uses EC2 instances with EBS volumes, but they want to optimize storage costs. How would you identify and implement cost-saving measures?  

3. An organization wants to centralize logs from multiple AWS accounts. How would you design a logging solution using AWS services?  

4. How to secure sensitive environment variables for an ECS service that uses Fargate?  

5. A real-time analytics application needs to process 1 TB of data daily. Which AWS services would you use to build an efficient pipeline, and why?  

6. Your serverless application needs to connect to a MySQL database securely. What steps would you take to configure the connection?  

### Terraform  

7. How to handle a requirement to deploy the same infrastructure across multiple AWS regions using Terraform?  

8. Your team wants to enforce compliance policies for resources deployed with Terraform (eg. tagging). How would you achieve this?  

9. During a terraform apply, a resource failed to provision, but others succeeded. How would you roll back changes while maintaining consistency?  

10. You’re tasked with deploying resources for a temporary project using Terraform. How would you ensure easy cleanup after the project ends?  

11. How would you prevent collaborators from accidentally overwriting each other’s changes? What strategies would you implement here?  

12. A client requests a Terraform setup where they can provision only specific subsets of resources on demand. How would you design such a solution?



# Technical Questions for Linux, DevOps, and Cloud Infrastructure

1. Securing a Linux Server  
   You are tasked with securing a Linux server that hosts a web application. The server is currently exposed to the internet and has a weak root password. Describe the steps you would take to secure the server.

2. Recovering Data from a Corrupted File System  
   One of your team members accidentally ran a command that corrupted the file system on a critical Linux server. The server is no longer booting, and you need to recover the data. Walk me through the steps you would take to recover the file system.

3. Backup Script for Remote Server  
   Your team uses a backup script to download the latest backup file from a remote server. However, the script is currently not working due to changes in the remote server's configuration. Write a script that downloads the latest backup file from the remote server using SSH.

4. Terraform Taint and Untaint Commands  
   You are using Terraform to manage your infrastructure, and you notice that one of your resources is not being updated correctly. Describe how you would use Terraform's taint and untaint commands to resolve the issue. Additionally, explain the difference between stateful and stateless resources in Terraform.

5. Jenkins Master-Slave Architecture  
   Your team is using Jenkins for continuous integration and continuous deployment (CI/CD). Describe the master-slave architecture of Jenkins and how it enables distributed builds and deployments.

6. Implementing a CI/CD Pipeline  
   You are tasked with implementing a CI/CD pipeline from scratch for a web application. Describe the steps you would take to implement the pipeline, including how you would ensure zero downtime deployments and implement rollbacks.

7. Shift-Left in DevOps  
   Explain the concept of shift-left in DevOps and how it enables teams to detect and fix issues earlier in the development cycle.

8. ADD vs COPY in a Dockerfile  
   What is the difference between the ADD and COPY instructions in a Dockerfile?

9. Removing Sensitive Information from Git  
   You accidentally committed sensitive information to a Git repository. Describe the steps you would take to remove the sensitive information from the repository's history.

10. Recovering a Deleted Git Branch  
    One of your team members accidentally deleted a critical branch in a Git repository. Describe the steps you would take to recover the deleted branch.

11. Origin vs Upstream in Git  
    Explain the difference between the origin and upstream remotes in a Git repository.

12. Docker Container Lifecycle  
    Describe the lifecycle of a Docker container, including how it is created, started, stopped, and deleted.

13. Kubernetes ReplicaSet  
    Explain the concept of a ReplicaSet in Kubernetes and how it ensures that a specified number of replicas of a pod are running at any given time.

14. Configuring a NAT Gateway in AWS  
    Describe how to configure a NAT gateway in AWS to enable outbound internet access for instances in a private subnet.

15. Deleting `/var/lib/docker/overlay` on a Docker Host  
    What happens when you delete the `/var/lib/docker/overlay` directory on a Docker host?

16. Running a VM Without EC2 in AWS  
    Is it possible to run a virtual machine (VM) in AWS without creating an EC2 instance? If so, how?

17. Stopping vs Terminating EC2 Instances  
    Explain the difference between stopping and terminating an EC2 instance. Additionally, describe the concept of EC2 hibernation and how it enables instances to be restarted from a saved state.










