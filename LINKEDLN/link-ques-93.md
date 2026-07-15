
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


Write 4–5 answers in a table format for a GitHub Markdown (.md) file using simple, easy-to-understand English and short sentences.

> **Interview One-Line Answer:**  
> **"Deploy the application in multiple regions, use Route 53 for automatic failover, replicate the database and storage, so users are redirected to a healthy region if one region goes down."**

3. A client’s application uses EC2 instances with EBS volumes, but they want to optimize storage costs. How would you identify and implement cost-saving measures?

| Step | What to Check | Cost-Saving Action |
|------|---------------|--------------------|
| 1 | Find unused EBS volumes | Delete volumes that are not attached to any EC2 instance. |
| 2 | Check EBS volume type | Change expensive **io1/io2** volumes to **gp3** if high performance is not needed. |
| 3 | Check volume size | Reduce oversized volumes after checking actual disk usage. |
| 4 | Review old snapshots | Delete old or unnecessary EBS snapshots to save storage cost. |
| 5 | Enable monitoring | Use AWS Cost Explorer and CloudWatch to track storage usage and find savings regularly. |

5. An organization wants to centralize logs from multiple AWS accounts. How would you design a logging solution using AWS services?
| Step | AWS Service | Why Use It |
|------|-------------|------------|
| 1 | Amazon CloudWatch Logs | Collect logs from EC2, Lambda, and other AWS services in each account. |
| 2 | CloudWatch Log Subscription Filter | Send logs from all AWS accounts to a central logging account. |
| 3 | Amazon Kinesis Data Firehose | Stream logs to a storage service automatically. |
| 4 | Amazon S3 | Store all logs securely at a low cost for long-term retention. |
| 5 | Amazon OpenSearch Service | Search, analyze, and visualize logs from one central location. |


7. How to secure sensitive environment variables for an ECS service that uses Fargate?  

8. A real-time analytics application needs to process 1 TB of data daily. Which AWS services would you use to build an efficient pipeline, and why?

| Step | AWS Service | Why Use It |
|------|-------------|------------|
| 1 | Amazon Kinesis Data Streams | Collect real-time data from applications with low delay. |
| 2 | AWS Lambda | Process data automatically without managing servers. |
| 3 | Amazon Kinesis Data Firehose | Deliver processed data to storage with less setup. |
| 4 | Amazon S3 | Store large amounts of data at a low cost. |
| 5 | Amazon Athena or Amazon Redshift | Query and analyze the stored data quickly. |

10. Your serverless application needs to connect to a MySQL database securely. What steps would you take to configure the connection?  
