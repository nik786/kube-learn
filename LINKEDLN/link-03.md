
# Questions and Answers  

1. What scripting languages are you familiar with?  

2. What are artifacts in GitLab CI?  

3. What is a private module registry in Terraform?  

4. If you delete the local Terraform state file and it's not stored in S3 or DynamoDB, how can you recover it?  

5. How do you import resources into Terraform?  

6. What is a dynamic block in Terraform?  

7. How can you create EC2 instances in two different AWS accounts simultaneously using Terraform?  

8. How do you handle an error stating that the resource already exists when creating resources with Terraform?  

9. How does Terraform refresh work?  

10. How would you upgrade Terraform plugins?  

11. What are the different types of Kubernetes volumes?  

12. If a pod is in a crash loop, what might be the reasons, and how can you recover it?  

13. What is the difference between StatefulSet and DaemonSet?  

14. What is a sidecar container in Kubernetes, and what are its use cases?  

15. If pods fail to start during a rolling update, what strategy would you use to identify the issue and rollback?  

16. How can we enable communication between 500 AWS accounts internally?  

17. How to configure a solution where a Lambda function triggers on an S3 upload and updates DynamoDB?  

18. What is the standard port for RDP?  

19. How do you configure a Windows EC2 instance to join an Active Directory domain?  

20. How can you copy files from a Linux server to an S3 bucket?  

21. What permissions do you need to grant for that S3 bucket?  

22. What are the different types of VPC endpoints and when do you use them?  

23. How to resolve an image pullback error when using an Alpine image pushed to ECR in a pipeline?  

24. What is the maximum size of an S3 object?  

25. What encryption options do we have in S3?  

26. Can you explain IAM user, IAM role, and IAM group in AWS?  

27. What is the difference between an IAM role and an IAM policy document?  

28. What are inline policies and managed policies?  

29. How can we add a load balancer to Route 53?  

30. What are A records and CNAME records?  

31. What is the use of a target group in a load balancer?  

32. If a target group is unhealthy, what might be the reasons?  

33. Can you share your screen and write a Jenkins pipeline?  

34. How do you write parallel jobs in a Jenkins pipeline?  






AWS
------
1. You are unable to ssh ec2 instance in public subnet. What could be the issue.
2. Design a highly available and scalable 3 tier architecture in AWS.
3. How to block traffic from a particular country/region.
4. Your primary region suddenly goes down. How to move application to Disaster Recovery region.
5. Write a policy which have list access of ec2 instance and s3 bucket.
6. Lambda function is unable to access database(any) which is hosted on ec2 instance. What could be the issue.
7. Database is in private subnet. What is the secure way to download required package for database.

Terraform
----------
1. Write a script to create a ec2 instance and a S3 bucket.
2. Write a module to create ec2 instance.
3. Where you keep your state file and why.
4. What is workspace in terraform. 
5. What is state locking in terraform.

Kubernetes 
------------
1. Explain the architecture of kubernetes.
2. Explain the end to end pipeline (all stages)
3. Difference between dockerfile and Docker compose
4. What are the content of service.yaml and deployment.yaml
5. What is multistage docker file.
6. How to secure kubernetes cluster
7. How pods access secrets 
8. What is headless service and sidecar container.
9. How to upgrade kubernetes cluster. Please explain step by step.



# Questions and Answers  

1. What is AWS Landing Zone?  

2. What is AWS Organizations?  

3. Explain about S3 secured way of giving access to users?  

4. IAM User vs Role?  

5. IAM Assume Role?  

6. What is a condition in IAM Policy?  

7. What is the difference between a public subnet and a private subnet?  

8. How to connect a private subnet or server from public?  

9. What is Private Link in S3?  

10. VPC Endpoint Types?  

11. Have you ever configured a Transit Gateway?  

12. What is the difference between a Security Group and NACL?  

13. What is VPC Peering and its steps?  

14. VPC Transit Gateway Steps?  

15. On-premises to S3 connection?  

16. Explain IAM Policy and all steps in that?  

17. Terraform import - Explain with example?  

18. Terraform Module?  

19. `.git-ci.yaml` file for Terraform steps?  

20. What have you done in Terraform?  

21. What is a Statefile and where do you keep the Statefile?  

22. How do you do patching for servers?  

23. How do you monitor server patching?  

24. How to secure the resources in AWS?  

25. Encryption Types?  

26. Encryption in REST vs Transit?  

27. How do you encrypt in S3 and the types?  

28. How to monitor VPC logs?  

29. What observability tools do you use in projects?  

30. What are GitLab Actions?  

31. Is documentation of tasks good or bad?  

32. What is Sentinel Policy?  

33. What is Terraform Drift?  

# Questions and Answers  

1. How to optimize Lambda function?  

2. How to increase Lambda function performance?  

3. Common issues you face in Lambda function?  

4. GitLab actions  

5. Event-driven architecture for Lambda  

6. What resources do you use for event-driven Lambda?  

7. Error handling in Lambda  

8. How do you monitor Lambda?  

9. How do you handle synchronous invocation?  

10. How do you handle Lambda timeout?  

11. How do you capture failed events?  

12. Security in serverless architecture  

13. Limitations of Lambda  







******DevOps & AWS Interview Questions****** 
 
# General Questions  

1. Introduce yourself.  
2. Describe a challenge you faced as a DevOps engineer and how you overcame it.  
3. Would you like to work individually or in a team?  
4. Tell me about something where you got a chance to learn and implement from scratch.  
5. How would you handle a situation where you are not getting any help from your team members?  

# AWS Questions  

1. Launch template vs launch configuration.  
2. How do you communicate with AWS services privately without exposing to the internet?  
3. NAT gateway vs NAT instance vs Egress-only IGW vs IGW.  
4. Design a 3-tier infrastructure using AWS services that is secure and highly available.  
5. Stateful vs stateless firewalls.  
6. Differentiate between NLB and ALB.  
7. You want to redirect traffic from x.company.in to company.in/x, how to achieve it?  
8. Your database initially performs well, but after some months, you face slowness. How to troubleshoot and fix the issue?  

# Kubernetes (K8s)  

1. K8s architecture.  
2. Deployment vs StatefulSet vs ReplicaSet.  
3. What is ConfigMap?  
4. Role of etcd in Kubernetes.  
5. How do rolling updates work in a deployment?  

# Docker  

1. ADD vs COPY.  
2. Entrypoint vs CMD.  
3. How to remove all unwanted or unused Docker objects from the system?  
4. Multistage Docker build.  
5. Is a Dockerfile immutable?  

# Terraform  

1. What does `terraform init` do?  
2. How to auto-approve Terraform changes?  
3. Count vs for_each.  
4. How to import an existing resource into Terraform?  
5. Data block in Terraform.  
6. What are provisioners in Terraform?  
7. Remote backend.  

# Linux  

1. How to check the list of installed packages?  
2. Command to check the kernel version.  
3. How to create a new user and add it as sudo?  
4. Command to check if a process called "a" is running or not. If running, how to stop it.  
5. Command to list all files less than 5MB.  
6. Hard link vs soft link.  
7. Commands to check disk space usage and free RAM.  

# CI/CD  

1. Git fetch vs Git pull.  
2. SonarQube quality gate vs quality profile.  
3. What is Sonar Runner?  
4. Types of pipelines in Jenkins.  
5. Scripted vs Declarative pipeline.  
6. Should we prefer Artifactory to store artifacts or store them in S3?  
7. How to upgrade plugins in Jenkins?  
8. User management in Jenkins.  
9. Concepts about GitLab runners.  
10. How to upgrade Jenkins.  

# Ansible  

1. Loops in Ansible.  
2. Ansible Roles.  
3. Is Ansible idempotent?  
4. Ansible script to install Nginx.  
5. Conditionals in Ansible.  

1. What is a statefile?  
2. Where do you store the statefile?  
3. What is a null resource in Terraform?  
4. CI/CD workflow.  
5. Terraform code to deploy an EC2 instance.  
6. What will appear in the Terraform plan if you comment out a resource block?  
7. Script to find the largest and smallest elements in an array.  
8. Entry point vs CMD in a Dockerfile.  
9. Add vs Copy in Dockerfile.  
10. Describe Kubernetes architecture.  
11. Do you know Ansible?  
12. Difference between Secrets and ConfigMap in Kubernetes.  
13. Docker lifecycle.  
14. What is a ReplicaSet?  
15. Running Kubernetes in a single-node local environment.  
16. How to remove a file from Git without deleting it from the filesystem.  
17. Discovering if a Git branch has been merged.  
18. Application Load Balancer vs Network Load Balancer.  
19. What is Route53?  
20. Experience with GCP Cloud.  
21. Difference between single and multiple Jenkins pipelines.  
22. Issues of using a single pipeline vs multiple pipelines in Jenkins.  
23. Current Jenkins version.  
24. Jenkins pipeline script for Terraform deployment.  
25. Creating 10 EC2 instances with incremental values.  
26. Terminating 9 EC2 instances while keeping one running.  
27. Connecting on-premise applications to a VPC cloud.  
28. Terraform taint.  
29. Terraform refresh.  
30. What happens if console resource values are changed and Terraform apply is executed?  
31. Terraform module and its purpose.  
32. What is CloudTrail?  
33. Load Balancer and Auto Scaling.  
34. What is Databricks?  
35. What is DevOps, and how does it differ from traditional IT practices?  
36. Benefits of implementing DevOps.  
37. Description of the DevOps lifecycle.  
38. Explanation of CI/CD pipeline and its benefits.  
39. Importance of Infrastructure as Code (IaC).  
40. Tools used for configuration management and why.  
41. Managing version control in DevOps.  
42. Differences between Ansible, Puppet, and Chef.  
43. Which containerization platforms have you worked with?  
44. How do you monitor systems in a DevOps environment? What tools do you recommend?  
45. What tools have you used for CI/CD, and how do they fit into the pipeline?  
46. How do you handle failures during deployments?  
47. Explain blue-green deployments and canary deployments.  
48. What are some challenges with automating CI/CD, and how do you address them?  
49. What cloud platforms have you worked with (AWS, Azure, GCP)?  
50. Explain the differences between scaling horizontally and vertically.  
51. How do you ensure high availability in a distributed system?  
52. What is the role of load balancers in a cloud architecture?  
53. What scripting languages do you use, and for what purpose in DevOps?  
54. How do you automate infrastructure provisioning?  
55. Can you explain how you troubleshoot failed scripts or pipelines?  
56. What monitoring tools have you used? How do you decide which metrics to monitor?  
57. How do you ensure the security of your CI/CD pipelines?  
58. What is your approach to handling secrets and credentials in automation scripts?  
59. Tell me about a challenging project you worked on in DevOps. How did you handle it?  
60. Describe a time when a production system failed. What steps did you take to resolve it?  
61. How would you approach onboarding a new team to a DevOps culture?  
62. How do you handle conflicts between development and operations teams?  
63. How do you keep yourself updated with the latest DevOps trends and technologies?  
64. What do you think is the most critical aspect of collaboration in a DevOps team?  
65. What scripting languages are you familiar with?  
66. What are artifacts in GitLab CI?  
67. What is a private module registry in Terraform?  
68. If you delete the local Terraform state file and it’s not stored in S3 or DynamoDB, how can you recover it?  
69. How do you import resources into Terraform?  
70. What is a dynamic block in Terraform?  
71. How can you create EC2 instances in two different AWS accounts simultaneously using Terraform?  
72. How do you handle an error stating that the resource already exists when creating resources with Terraform?  
73. How does Terraform refresh work?  
74. How would you upgrade Terraform plugins?  
75. What are the different types of Kubernetes volumes?  
76. If a pod is in a crash loop, what might be the reasons, and how can you recover it?  
77. What is the difference between StatefulSet and DaemonSet?  
78. What is a sidecar container in Kubernetes, and what are its use cases?  
79. If pods fail to start during a rolling update, what strategy would you use to identify the issue and rollback?  
80. How can we enable communication between 500 AWS accounts internally?  
81. How to configure a solution where a Lambda function triggers on an S3 upload and updates DynamoDB?  
82. What is the standard port for RDP?  
83. How do you configure a Windows EC2 instance to join an Active Directory domain?  
84. How can you copy files from a Linux server to an S3 bucket?  
85. What permissions do you need to grant for that S3 bucket?  
86. What are the different types of VPC endpoints and when do you use them?  
87. How to resolve an image pullback error when using an Alpine image pushed to ECR in a pipeline?  
88. What is the maximum size of an S3 object?  
89. What encryption options do we have in S3?  
90. Can you explain IAM user, IAM role, and IAM group in AWS?  
91. What is the difference between an IAM role and an IAM policy document?  
92. What are inline policies and managed policies?  
93. How can we add a load balancer to Route 53?  
94. What are A records and CNAME records?  
95. What is the use of a target group in a load balancer?  
96. If a target group is unhealthy, what might be the reasons?  
97. Can you share your screen and write a Jenkins pipeline?  
98. How do you write parallel jobs in a Jenkins pipeline?  
99. How do you store the state file, and how would you write an S3 bucket creation in Terraform?  
100. Can you explain the process of creating an IAM role and attaching it to an EC2 instance?  
101. What is a Virtual Private Cloud (VPC)?  
102. Can you describe the purpose and functionality of Route 53?  
103. How do you access a private instance using a NAT gateway?  
104. What is the difference between CMD and ENTRYPOINT in a Dockerfile?  
105. What contents have you included in your Dockerfile?  
106. What is a Lambda function, and how does it work?  
107. Can you outline the stages of your Jenkins pipeline?  
108. How can you list the largest 10 files in a directory?  
109. What is a module in Terraform?  
110. Can you explain what a data resource is?  
111. What module have you developed that has been particularly useful for your team?  
112. What are your day-to-day activities in your current role?  
113. How do you troubleshoot a Docker container if it fails?  
114. What can you tell me about Prometheus?  
115. What are the steps to create custom metrics in CloudWatch?  
116. What are some common Linux command-line interfaces (CLI) you use daily?  
117. How do you access JSON data in Python?  
118. Have you integrated SonarQube into your CI/CD pipeline?  
119. How do you implement auto-scaling in AWS, and what are the configuration steps involved?  



1. How do you uncommit the changes that have already been pushed to GitHub?  
2. If there is suddenly the file is deleted in git how do you get it back?  
3. Can you increase the size of the root volume without shutting down the instance?  
4. If you lost the .pem file then how will you connect to EC2?  
5. S3 bucket having a policy for only read-only but you’re having full access for you? Can you modify s3 objects?  
6. Difference between Classic ELB and Application ELB?  
7. How many subnets are assigned to the routing table?  
8. In your VPC all IPS are finished you require resources how to provision it?  
9. Are you only using CloudWatch for monitoring?  
10. If you're using load balancing in 2 availability zones then which load balancer should you use?  
11. Can you write a Dockerfile where Linux environment conditions deploy a static web server?  
12. Is it possible to run any VM in AWS without creating any EC2 instance?  
13. I want to create a pipeline in Jenkins which needs to have 10 different stages and based on my input it needs to execute some stages, not every stage. How would you configure that?  
14. What are Terraform modules? Have you used any modules in the project?  
15. Is it possible to configure communication between 2 servers that have private access?  
16. What happens when you delete /var/lib/docker/overlay?  
17. Write a simple script that calls with “Foo” prints “bar” and when called with “bar” prints “foo”. Every other option should print “Try again”?  
18. Tell all the scenarios to implement security in Kubernetes.  
19. Your EKS application is experiencing higher than expected traffic. How would you automatically scale the Pods?  
20. Your team needs to be alerted when the CPU usage of any Pod in your EKS cluster exceeds 80% for more than 5 minutes. How would you set this up?  
21. Your team wants a Grafana dashboard to visualize the HTTP request latency of your applications running in EKS. How would you achieve this?



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










