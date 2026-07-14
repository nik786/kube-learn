
### AWS Scenario-Based Questions  

1. Your team needs to deploy a web application across multiple regions for disaster recovery. How would you design the deployment to ensure minimal downtime during a regional failure?

## Multi-Region Deployment for Disaster Recovery

| Step | What to Do | Example AWS Service |
|------|------------|---------------------|
| **1. Deploy in Multiple Regions** | Run the application in two or more AWS regions. | Amazon EKS / EC2 |
| **2. Use a Global Load Balancer** | Route users to the nearest healthy region. | Route 53 (Failover or Latency Routing) |
| **3. Replicate the Database** | Keep data synchronized between regions. | Amazon RDS Cross-Region Replica / DynamoDB Global Tables |
| **4. Store Files in Multiple Regions** | Replicate application files and backups. | Amazon S3 Cross-Region Replication (CRR) |
| **5. Enable Automatic Failover** | If one region fails, traffic automatically moves to the healthy region. | Route 53 Health Checks |

### Easy to Remember

```text
Deploy in Multiple Regions
           ↓
Global Load Balancer
           ↓
Replicate Database
           ↓
Replicate Storage
           ↓
Automatic Failover
```

> **Interview One-Line Answer:**  
> **"Deploy the application in multiple regions, use Route 53 for automatic failover, replicate the database and storage, so users are redirected to a healthy region if one region goes down."**

3. A client’s application uses EC2 instances with EBS volumes, but they want to optimize storage costs. How would you identify and implement cost-saving measures?  

4. An organization wants to centralize logs from multiple AWS accounts. How would you design a logging solution using AWS services?  

5. How to secure sensitive environment variables for an ECS service that uses Fargate?  

6. A real-time analytics application needs to process 1 TB of data daily. Which AWS services would you use to build an efficient pipeline, and why?  

7. Your serverless application needs to connect to a MySQL database securely. What steps would you take to configure the connection?  
