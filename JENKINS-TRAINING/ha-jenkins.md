

# Active-Active Jenkins Architecture in AWS

| **Step** | **Description** |
|----------|-----------------|
| **1. Set Up a VPC** | Create a VPC with multiple Availability Zones (AZs) for fault tolerance. Set up public and private subnets. |
| **2. Launch Multiple Jenkins Master EC2 Instances** | Launch at least two EC2 instances in different AZs. Install Jenkins on them or use an AMI with Jenkins pre-installed. |
| **3. Set Up Application Load Balancer (ALB)** | Create an ALB to distribute traffic between Jenkins Masters. Set up health checks and configure SSL if needed. |
| **4. Set Up Shared Jenkins Home Directory** | Use Amazon EFS (Elastic File System) or S3 to store Jenkins' home directory, ensuring data consistency across masters. |
| **5. Set Up Amazon RDS for Jenkins Database** | Set up Amazon RDS (MySQL or PostgreSQL) with Multi-AZ deployment for high availability of Jenkins' database. |
| **6. Configure Jenkins Auto Scaling (for Jenkins Masters)** | Set up an Auto Scaling Group (ASG) for Jenkins Masters with scaling policies based on traffic or CPU utilization. |
| **7. Set Up Jenkins Agents (Optional, for Scalability)** | Set up Jenkins agents on EC2, ECS, or use spot instances to scale Jenkins builds based on demand. |
| **8. Configure Route 53 for DNS Management** | Set up Route 53 DNS records pointing to the ALB for consistent access to Jenkins. |
| **9. Backup and Disaster Recovery Setup** | Regularly back up EFS and RDS data. Use AWS Backup or custom solutions to back up Jenkins configurations and job data. |
| **10. Monitoring and Alerts** | Use CloudWatch to monitor Jenkins instances, RDS, ALB, and Auto Scaling. Set up alarms for critical metrics and send notifications via SNS. |

---

## Diagram of Active-Active Jenkins Architecture in AWS:





## Advantages of Active-Active Jenkins Architecture:
- **No Single Point of Failure:** Both Jenkins Masters are fully operational at all times, ensuring continuous availability.
- **Scalability:** Jenkins Masters and Agents scale horizontally based on demand, allowing you to handle a large number of simultaneous builds.
- **Fault Tolerance:** Multi-AZ setup for Jenkins Masters, ALB, and RDS ensures that if one AZ fails, the other can continue handling requests.
- **Load Balancing:** ALB distributes traffic evenly across Jenkins Masters to ensure optimal performance.
- **High Availability:** Amazon EFS and Multi-AZ RDS ensure that critical data is always available, even if one of the instances or AZs fails.



```

Just run this code step by step it will 

sudo apt update

sudo apt install openjdk-17-jre

java -version
 
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update

sudo apt-get install jenkins

sudo systemctl start jenkins.service

sudo systemctl status jenkins
```


   ```
                    |  Route 53   |
                    | (DNS)       |
                    +-------------+
                          |
                          |
                   +--------------+
                   |  ALB (8080)  | <---> Jenkins Masters
                   +--------------+
                   /                \
         +----------------+    +------------------+
         | Jenkins Master |    | Jenkins Master   |
         |   EC2 (AZ 1)   |    |   EC2 (AZ 2)     |
         +----------------+    +------------------+
                   |                    |
             +-------------+    +-------------+
             |   EFS       |    |   RDS       |
             | (Shared     |    | (Database)  |
             | Home)       |    |             |
             +-------------+    +-------------+
                   |
         +----------------------+
         |    Jenkins Agents    |
         | (EC2 / ECS / Containers) |
         +----------------------+

```
