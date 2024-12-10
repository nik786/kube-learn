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

Ques-02 
------------

1.What is AWS Landing Zone.

2.What is AWS Organizations.

3.Explain about S3 secured way of giving access to users?

4.IAM User vs Role?

5.IAM Assume Role?

6.What is a condition in IAM Policy?

7.What is the difference between a public subnet and a private subnet?

8.How to connect a private subnet or server from public?

9.What is Private Link in S3?

10.VPC Endpoint Types?

11.Have you ever configured a Transit Gateway?

12.What is the difference between a Security Group and NACL?

13.What is VPC Peering and its steps?

14.VPC Transit Gateway Steps?

15.On-premises to S3 connection?

16.Explain IAM Policy and all steps in that?

17.Terraform import - Explain with example?

18.Terraform Module?

19. .git-ci.yaml file for Terraform steps?
    
20.What have you done in Terraform?

21.What is a Statefile and where do you keep the Statefile?

22.How do you do patching for servers?

23.How do you monitor server patching?

24.How to secure the resources in AWS?

25.Encryption Types?

26.Encryption in REST vs Transit?

27.How do you encrypt in S3 and the types?

28.How to monitor VPC logs?

29.What observability tools do you use in projects?

30.What are GitLab Actions?

31.Is documentation of tasks good or bad?

32.What is Sentinel Policy?

33.What is Terraform Drift?

hashtag#Lambda Questions:
How to optimize Lambda function?

1.How to increase Lambda function performance?

2.Common issues you face in Lambda function?

3.GitLab actions

4.Event-driven architecture for Lambda

5.What resources do you use for event-driven Lambda?

6.Error handling in Lambda

7.How do you monitor Lambda?

8.How do you handle synchronous invocation?

9.How do you handle Lambda timeout?

10.How do you capture failed events?

11.Security in serverless architecture

12.Limitations of Lambda

Ques-03
------------

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


 Ques-04
------------

General Questions
1- Introduce yourself. 
2- Describe a challenge you faced as a devops engineer and how you overcame it. 
3- Would you like to work individually or in a team. 
4 - Tell me about something where you got a chance to learn and implement from scratch. 
5- How would you be handling a situation where you are not getting any help from your team members. 
 
AWS Questions: 
1- Launch template vs launch configuration. 
2- How do you communicate with AWS services privately without exposing to internet. 
3- NAT g/w vs NAT instance v/s Egress only IGW v/s IGW 
4- Design a 3 tier infrastructure using the AWS services which should be secure and highly available. 
5- Statefull v/s stateless firewalls. 
6- Differentiate between NLB and ALB. 
7- You want to redirect traffic from x.company.in to company.in/x, how to achieve it. 
8- Your database initially performs well, but after certain month you face slowness. How to troubleshoot and fix the same. 
 
K8s: 
1- K8s architecture 
2- Deployment v/s stateful set v/s replica set 
3- What is config map 
4- Role of etcd in kubernetes. 
5- How rolling updates work in a deployment? 
 
Docker: 
1- ADD v/s COPY 
2- Entrypoint v/s CMD 
3- How to remove all unwanted or unused docker objects from system? 
4- Multistage docker build. 
5- Is docker file immutable 
 
Terraform: 
1- What does terraform init do ? 
2- How to auto approve the terraform changes? 
3- count v/s foreach 
4- How to import an existing resource to terraform? 
5- Data black in terraform. 
6- What are provisioners in terraform? 
7- Remote backend. 
 
Linux: 
1- How to check the list of installed packages? 
2- Command to check kernel version. 
3- How to create a new user and add it as sudo? 
4- Command to check if a process called "a" is running or not. If running how stop it. 
5- Command to list all files less than 5mb. 
6- Hard link v/s soft link. 
7- Commands to check disk space usage and free RAM. 
 
CI/CD: 
1- Git fetch v/s Git pull 
2- Sonarqube quality gate vs quality profile. 
3- What is sonar runner. 
4- Types of pipeline in Jenkins. 
5- Scripted vs Declarative pipeline. 
6- Should we prefer artifactory to store artifacts or should we store them in s3. 
7- How to upgrade plugins in Jenkins. 
8- Usermanagement in Jenkins. 
9- Concepts about Gitlab runners. 
10- How to upgrade Jenkins. 
 
Ansible: 
1- loops in Ansible. 
2- Ansible Roles. 
3- Is Ansible idempotent? 
4- Ansible script to install nginx. 
5- Conditionals in Ansible. 

 Ques-05
------------

Azure Basics
--------------
1. What is Azure Cloud?
2. What are Azure Resource Groups?
3. What is the purpose of Azure Regions and Availability Zones?
4. Explain the concept of Azure Virtual Machines.
5. What is Azure App Service?
6. Differentiate between Azure Functions and Logic Apps.
7. What are Azure Managed Disks?
8. What is the use of Azure Monitor?
9. Explain Azure Load Balancer.
10.What is Azure Resource Manager (ARM)?


Azure Networking
-------------------
11.What is Azure Virtual Network (VNet)?
12.How does Azure Application Gateway differ from Azure Front Door?
13.What are NSGs (Network Security Groups) in Azure?
14.Explain VNet peering.
15.How do you design a secure and scalable network architecture in Azure?
16.What is an Azure ExpressRoute?
17.Describe the role of Azure Traffic Manager.
18.Explain the concept of Service Endpoints and Private Links.
19.How would you configure a site-to-site VPN in Azure?
20.Scenario: Design a highly available multi-region VNet setup for a global 


Azure Security
-------------------
21.What is Azure Key Vault?
22.How does Azure Policy differ from Azure RBAC?
23.What are Managed Identities in Azure?
24.How do you implement Azure Conditional Access?
25.What is Microsoft Defender for Cloud?
26.Describe the shared responsibility model in Azure.
27.How do you secure Azure Storage?
28.What are Just-in-Time VM access and its benefits?
29.Explain the Zero Trust model in Azure.
30.Scenario: Your web application on Azure is under a DDoS attack. How would
you respond?



Azure DevOps Fundamentals
----------------------------
31.What is Azure DevOps?
32.Explain Pipelines in Azure DevOps.
33.What are Build Agents?
34.How do you implement CI/CD in Azure DevOps?
35.What is YAML in the context of Azure Pipelines?
36.Describe Azure Artifacts.
37.How does Azure Repos differ from GitHub?
38.Explain Release Management in Azure DevOps.
39.What is a self-hosted agent in Azure DevOps?
40.Scenario: How would you set up a CI/CD pipeline for a Node.js application?


Advanced Azure DevOps
-----------------------
41.How do you implement infrastructure as code using Terraform in Azure
DevOps?
42.Explain the concept of Blue-Green Deployments.
43.What are Canary Releases, and how are they achieved in Azure Pipelines?
44.How do you secure secrets in Azure DevOps?
45.What is GitOps, and how does it work with Azure Kubernetes Service?
46.Describe Service Hooks in Azure DevOps.
47.How do you perform vulnerability scanning in Azure DevOps pipelines?
48.Scenario: Configure a Terraform pipeline for deploying a VNet in Azure.
49.How do you ensure rollback in case of a failed deployment?
50.Scenario: You are tasked with integrating SAST and DAST in your CI/CD
pipeline. Explain how.



Azure System Design and Solution Architecture
--------------------------------------------------------
Q51. Design a multi-tier application using Azure services.
Solution:
A multi-tier application typically consists of:
• Frontend Tier: Use Azure App Service or Azure Static Web Apps to host the
UI.
• Backend Tier: Implement business logic using Azure Functions or App
Service.
• Database Tier: Use Azure SQL Database or Cosmos DB for storing
structured/unstructured data.
• Networking: Protect communication using Azure Application Gateway with
WAF (Web Application Firewall).
• Scaling and Monitoring: Use Azure Monitor and Auto-scaling to handle
traffic surges.


Advanced Azure Networking
----------------------------
Q56. Troubleshoot a failing site-to-site VPN in Azure.
Solution:
1. Verify Gateway Configuration: Check that both ends (on-premises and Azure)
have matching settings (shared key, VPN type, and IPsec/IKE protocol).
2. Check NSGs: Ensure NSG rules allow VPN Gateway IP traffic.
3. Logs and Diagnostics: Enable Azure Network Watcher and VPN diagnostics
for insights.
4. Firewall Rules: Check on-premises firewalls for incorrect rule blocking.
5. Route Tables: Ensure UDR (User Defined Routes) directs traffic to the VPN
Gateway.

Azure Security
-------------------
Q29. Explain the Zero Trust model in Azure.
Solution:
The Zero Trust model assumes that every request is a potential threat and verifies
every access attempt.
1. Identity Verification: Use Azure AD MFA and Conditional Access Policies.
2. Least Privilege Access: Implement Role-Based Access Control (RBAC).
3. Network Segmentation: Use NSGs and Private Links.
4. Encryption: Encrypt data at rest with Azure Storage encryption and in transit
with SSL/TLS.
5. Monitoring and Alerts: Enable Azure Security Center for continuous
assessment.

 DevOps Pipeline Scenarios
 ----------------------------
Q50. Integrating SAST and DAST into a CI/CD pipeline.
Solution:
1. SAST (Static Application Security Testing):
• Use tools like SonarQube or Checkmarx.
• Integrate as a pre-build step in Azure Pipelines.
• Example YAML snippet:
steps:
 - task: SonarQubePrepare@4
 inputs:
 SonarQube: 'SonarQubeConnection'
 scannerMode: 'CLI'
 configMode: 'file'
 - script: sonar-scanner

. DAST (Dynamic Application Security Testing):
• Use tools like OWASP ZAP or Burp Suite.
• Run post-deployment tests against a staging environment.
Example for OWASP ZAP:
steps:
 - script: |


System Design and Solution Architecture
-------------------------------------------
51.Design a multi-tier application using Azure services.
52.Create a cost-effective disaster recovery plan for an e-commerce application
on Azure.
53.Optimize a large-scale database with unpredictable traffic.
54.Architect a real-time analytics platform using Azure services.
55.Scenario: Your application requires data replication across regions with
minimal latency.

Networking
-------------------
56.Troubleshoot a failing site-to-site VPN in Azure.
57.Design a private Kubernetes cluster with secure API access.
58.Scenario: An application requires a public IP while securing internal
communication.


Troubleshooting and Best Practices
------------------------------------
59.Debug an Azure Function with intermittent timeouts.
60.Troubleshoot high egress costs in Azure.


Ques-06
------------

What is a statefile?
• Where do you store the statefile?
• What is a null resource in Terraform?
• CI/CD workflow.
• Terraform code to deploy an EC2 instance.
• What will appear in the Terraform plan if you comment out a resource block?
• Script to find the largest and smallest elements in an array.
• Entry point vs CMD in a Dockerfile.
• Add vs Copy in Dockerfile.
• Describe Kubernetes architecture.
• Do you know Ansible?
• Difference between Secrets and ConfigMap in Kubernetes.
• Docker lifecycle.
• What is a ReplicaSet?
• Running Kubernetes in a single-node local environment.
• How to remove a file from Git without deleting it from the filesystem.
• Discovering if a Git branch has been merged.
• Application Load Balancer vs Network Load Balancer.
• What is Route53?

Experience with GCP Cloud.
• Difference between single and multiple Jenkins pipelines.
• Issues of using a single pipeline vs multiple pipelines in Jenkins.
• Current Jenkins version.
• Jenkins pipeline script for Terraform deployment.
• Creating 10 EC2 instances with incremental values.
• Terminating 9 EC2 instances while keeping one running.
• Connecting on-premise applications to a VPC cloud.
• Terraform taint.
• Terraform refresh.
• What happens if console resource values are changed and Terraform apply is
executed?
• Terraform module and its purpose.
• What is CloudTrail?
• Load Balancer and Auto Scaling.
• What is Databricks?

Ques-07
------------

What is DevOps, and how does it differ from traditional IT practices?
• Benefits of implementing DevOps.
• Description of the DevOps lifecycle.
• Explanation of CI/CD pipeline and its benefits.
• Importance of Infrastructure as Code (IaC).
• Tools used for configuration management and why.
• Managing version control in DevOps.
• Differences between Ansible, Puppet, and Chef.
• Which containerization platforms have you worked with?
• How do you monitor systems in a DevOps environment? What tools do you
recommend?
• What tools have you used for CI/CD, and how do they fit into the pipeline?
• How do you handle failures during deployments?
• Explain blue-green deployments and canary deployments.
• What are some challenges with automating CI/CD, and how do you address them?
• What cloud platforms have you worked with (AWS, Azure, GCP)?
• Explain the differences between scaling horizontally and vertically.
• How do you ensure high availability in a distributed system?

Ques-08
------------

What is the role of load balancers in a cloud architecture?
• What scripting languages do you use, and for what purpose in DevOps?
• How do you automate infrastructure provisioning?
• Can you explain how you troubleshoot failed scripts or pipelines?
• What monitoring tools have you used? How do you decide which metrics to
monitor?
• How do you ensure the security of your CI/CD pipelines?
• What is your approach to handling secrets and credentials in automation scripts?
• Tell me about a challenging project you worked on in DevOps. How did you handle
it?
• Describe a time when a production system failed. What steps did you take to resolve
it?
• How would you approach onboarding a new team to a DevOps culture?
• How do you handle conflicts between development and operations teams?
• How do you keep yourself updated with the latest DevOps trends and technologies?
• What do you think is the most critical aspect of collaboration in a DevOps team?
• What scripting languages are you familiar with?
• What are artifacts in GitLab CI?

What is a private module registry in Terraform?
• If you delete the local Terraform state file and it’s not stored in S3 or DynamoDB,
how can you recover it?
• How do you import resources into Terraform?
• What is a dynamic block in Terraform?
• How can you create EC2 instances in two different AWS accounts simultaneously
using Terraform?
• How do you handle an error stating that the resource already exists when creating
resources with Terraform?
• How does Terraform refresh work?
• How would you upgrade Terraform plugins?
• What are the different types of Kubernetes volumes?
• If a pod is in a crash loop, what might be the reasons, and how can you recover it?
• What is the difference between StatefulSet and DaemonSet?
• What is a sidecar container in Kubernetes, and what are its use cases?
• If pods fail to start during a rolling update, what strategy would you use to identify
the issue and rollback?
• How can we enable communication between 500 AWS accounts internally?
• How to configure a solution where a Lambda function triggers on an S3 upload and
updates DynamoDB?
• What is the standard port for RDP?
• How do you configure a Windows EC2 instance to join an Active Directory domain?
• How can you copy files from a Linux server to an S3 bucket?

Ques-09
------------

What permissions do you need to grant for that S3 bucket?
• What are the different types of VPC endpoints and when do you use them?
• How to resolve an image pullback error when using an Alpine image pushed to ECR
in a pipeline?
• What is the maximum size of an S3 object?
• What encryption options do we have in S3?
• Can you explain IAM user, IAM role, and IAM group in AWS?
• What is the difference between an IAM role and an IAM policy document?
• What are inline policies and managed policies?
• How can we add a load balancer to Route 53?
• What are A records and CNAME records?
• What is the use of a target group in a load balancer?
• If a target group is unhealthy, what might be the reasons?

Ques-10
------------

Can you share your screen and write a Jenkins pipeline?
• How do you write parallel jobs in a Jenkins pipeline?
• How do you store the state file, and how would you write an S3 bucket creation in
Terraform?
• Can you explain the process of creating an IAM role and attaching it to an EC2
instance?
• What is a Virtual Private Cloud (VPC)?
• Can you describe the purpose and functionality of Route 53?
• How do you access a private instance using a NAT gateway?
• What is the difference between CMD and ENTRYPOINT in a Dockerfile?
• What contents have you included in your Dockerfile?
• What is a Lambda function, and how does it work?
• Can you outline the stages of your Jenkins pipeline?
• How can you list the largest 10 files in a directory?
• What is a module in Terraform?
• Can you explain what a data resource is?
• What module have you developed that has been particularly useful for your team?
• What are your day-to-day activities in your current role?
• How do you troubleshoot a Docker container if it fails?
• What can you tell me about Prometheus?
• What are the steps to create custom metrics in CloudWatch?

Ques-11
------------

 How do you troubleshoot a Docker container if it fails?
• What can you tell me about Prometheus?
• What are the steps to create custom metrics in CloudWatch?
• What are some common Linux command-line interfaces (CLI) you use daily?
• What is a Lambda function, and how does it work?
• Can you outline the stages of your Jenkins pipeline?
• How can you list the largest 10 files in a directory?
• What is a module in Terraform?
• Can you explain what a data resource is?
• What module have you developed that has been particularly useful for your team?
• What are your day-to-day activities in your current role?
• How do you troubleshoot a Docker container if it fails?
• What can you tell me about Prometheus?
• What are the steps to create custom metrics in CloudWatch?
• What are some common Linux command-line interfaces (CLI) you use daily?
• How do you access JSON data in Python?
• Have you integrated SonarQube into your CI/CD pipeline?

How do you implement auto-scaling in AWS, and what are the configuration steps
involved

Ques-12
------------

 How do you uncommit the changes that have already been pushed to GitHub? 
2. If there is suddenly the file is deleted in git how do you get it back? 
3. Can you increase the size of the root volume without shutting down the instance?
4. If you lost the .pem file then how will you connect to EC2? 
5. S3 bucket having a policy for only read-only but you’re having full access for you? Can you modify s3 objects? 
6. Difference between Classic ELB and Application ELB?
7. How many subnets are assigned to the routing table? 
8. In your VPC all IPS are finished you require resources how to provision it? 
9. Are you only using cloud watch for monitoring?
10.If your using load balancing in 2 availability zones den which load balancer you should use?
11. can you write docker file where Linux env condition deploy static webserver 
12. Is it possible to run any VM in AWS without creating any EC2 instance ? 
13. I want to create a pipeline in Jenkins which needs to have 10 different stages and based on my input it needs to execute some stages not every stages how you will configure that .
14. What are the Terraform modules? Have used any modules in the project?
15. Is it possible to configure communication between 2 servers those are having private access
16. What happens when you delete /var/lib/docker/overlay?
17. Write a simple script that calls with “Foo” prints “bar” and when called with “bar” prints “foo”. Every other option should print “Try 
again”?
18. Tell all the scenarios too implement the security in Kubernetes.
19. Your EKS application is experiencing higher than expected traffic. How would you automatically scale the Pods?
20. Your team needs to be alerted when the CPU usage of any Pod in your EKS cluster exceeds 80% for more than 5 minutes. How would you set this up?
21. Your team wants a Grafana dashboard to visualize the HTTP request latency of your applications running in EKS. How would you achieve this?













   
