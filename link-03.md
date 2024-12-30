
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
• Experience with GCP Cloud.
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
• What is DevOps, and how does it differ from traditional IT practices?
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
• What is the role of load balancers in a cloud architecture?
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
• What is a private module registry in Terraform?
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
• What permissions do you need to grant for that S3 bucket?
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
• Can you share your screen and write a Jenkins pipeline?
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
• How do you implement auto-scaling in AWS, and what are the configuration steps
involved



1. How do you uncommit the changes that have already been pushed to GitHub? 
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

Today, I had the opportunity to interview for a role that aligns perfectly with my expertise and career aspirations. The interview lasted 40 minutes and was both challenging and insightful!

The interview began with the question: "Can you briefly tell us about yourself, including your role and responsibilities in your current project?"

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




1.What are the different types of Load Balancers provided by AWS?
AWS offers three types of Load Balancers:
👉Application Load Balancer (ALB): Best for HTTP/HTTPS traffic with advanced routing.
👉Network Load Balancer (NLB): Optimized for TCP/UDP traffic with ultra-low latency.
👉Classic Load Balancer (CLB): Older generation, ideal for simple use cases.

🚦2.When would you choose ALB over NLB or CLB?
💡Use ALB for HTTP/HTTPS traffic when:
✔You need features like path-based or host-based routing.
✔You want integration with services like Lambda or Web Sockets.
💡Use NLB for:
✔High-performance, low-latency traffic.
✔Protocols like TCP/UDP or when handling millions of requests/sec.

📂3.What is a Target Group in ALB/NLB, and how does it work?
A Target Group is a set of resources (like EC2 instances or containers) that receive traffic from a Load Balancer.
🔍ALB: Routes traffic to targets based on listener rules (e.g., path /api).
🔍NLB: Distributes traffic to targets without inspecting packets.

🔄4.What is Cross-Zone Load Balancing?
Cross-Zone Load Balancing distributes traffic evenly across all registered targets in all availability zones, regardless of the request origin.
💡This improves performance and reduces bottlenecks in multi-AZ setups.

🔑5.What is SSL/TLS Termination, and how is it implemented in AWS ELB?
SSL/TLS Termination occurs when the Load Balancer handles encryption/decryption, offloading this task from backend servers.
🛠Implementation: Upload your SSL certificate to ELB via ACM (AWS Certificate Manager). ELB manages secure traffic on behalf of your application.

✅6.How does AWS Auto Scaling integrate with Elastic Load Balancing (ELB)?
Auto Scaling works with ELB to:
✔Automatically add or remove instances based on demand.
✔Register and deregister instances with the Load Balancer dynamically.

💻7.How does path-based routing work in an Application Load Balancer?
Path-based routing directs traffic to specific Target Groups based on the request URL.
💡For example:
✔/app1 → Target Group 1
✔/app2 → Target Group 2

🔒8.How can you secure your Load Balancer?
✔Enable HTTPS with SSL/TLS certificates.
✔Use Security Groups to allow traffic only from trusted IPs.
✔Implement WAF (Web Application Firewall) for additional protection.

📊9.What are the health checks in Elastic Load Balancer, and how do they work?
ELB uses health checks to monitor the status of registered targets.
💡It sends requests (e.g., HTTP GET) at regular intervals to a specific path (e.g., /health check).
❌Unhealthy targets: Removed from routing until they recover.

📡10.How do you monitor and troubleshoot issues with an AWS Load Balancer?
✔Use Cloud Watch for metrics like request count, latency, and 4xx/5xx errors.
✔Enable Access Logs for detailed traffic insights.
✔Check Target Group health for any failed instances.


𝗔𝗪𝗦 𝗦𝗰𝗲𝗻𝗮𝗿𝗶𝗼-𝗕𝗮𝘀𝗲𝗱 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀

1.Your team needs to deploy a web application across multiple regions for disaster recovery. How would you design the deployment to ensure minimal downtime during a regional failure?

2.A client’s application uses EC2 instances with EBS volumes, but they want to optimize storage costs. How would you identify and implement cost-saving measures?

3.An organization wants to centralize logs from multiple AWS accounts. How would you design a logging solution using AWS services?

4. How to secure sensitive environment variables for an ECS service that uses Fargate?

5.A real-time analytics application needs to process 1 TB of data daily. Which AWS services would you use to build an efficient pipeline, and why?

6.Your serverless application needs to connect to a MySQL database securely. What steps would you take to configure the connection?

📌𝗧𝗲𝗿𝗿𝗮𝗳𝗼𝗿𝗺

7. How to handle a requirement to deploy the same infrastructure across multiple AWS regions using Terraform?

8.Your team wants to enforce compliance policies for resources deployed with Terraform (eg. tagging). How would you achieve this?

9. During a terraform apply, a resource failed to provision, but others succeeded. How would you roll back changes while maintaining consistency?

10. You’re tasked with deploying resources for a temporary project using Terraform. How would you ensure easy cleanup after the project ends?

11. How would you prevent collaborators to accidentally overwriting each other’s changes. What strategies would you implement here?

12. A client requests a Terraform setup where they can provision only specific subsets of resources on demand. How would you design such a solution?




