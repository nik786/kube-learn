
# AWS Troubleshooting – Common Scenarios with Solutions

| **#** | **Issue** | **Solution / Troubleshooting Steps** |
|------|-----------|----------------------------------------|
| 1 | Cannot SSH into EC2 | Check **SG & NACL**, **key pair**, instance state, **public IP**, **route table**. |
| 2 | S3 403 error despite public access | Check **Block Public Access settings**, **bucket policy**, and **object ACLs**. |
| 3 | Lambda timeout | Increase timeout, review **CloudWatch logs**, optimize function logic or **external call latency**. |
| 4 | Slow RDS performance | Check **Enhanced Monitoring**, **slow query logs**, **CPU/memory**, indexing, and **connections**. |
| 5 | High S3 billing | Use **Cost Explorer**, check **storage class**, **versioning**, **lifecycle policy**, and **data transfer**. |
| 6 | CloudFront not showing updates | Check for **cache invalidation**, **origin config**, and **TTL settings**. |
| 7 | EC2 won’t start | Check **system logs**, **instance limits**, **EBS status**, and **status checks**. |
| 8 | Website down | Check **instance health**, **ALB/NLB**, **DNS resolution**, **logs**, and **network settings**. |
| 9 | IAM role assume failure | Check **trust policy**, **permissions**, correct **ARN**, and **MFA** if required. |
| 10 | ASG not launching | Check **launch template**, **instance limits**, **subnets**, and **desired capacity**. |
| 11 | API Gateway ThrottlingException | Increase **throttle limits**, apply **usage plans**, or request a **limit increase**. |
| 12 | VPC peering but no communication | Check **route tables**, **NACLs**, **SGs**, and **DNS resolution settings**. |
| 13 | ALB not routing correctly | Check **listener rules**, **target health**, **SGs**, and **DNS target**. |
| 14 | Route 53 not resolving | Check **TTL**, **record type**, **NS delegation**, and **propagation delays**. |
| 15 | S3 lifecycle policy not deleting | Verify **prefix match**, **versioning**, and **policy rules format**. |
| 16 | API Gateway 5XX errors | Check **backend integration**, **Lambda logs**, **timeout**, and **permissions**. |
| 17 | CloudWatch alarm not triggering | Validate **metrics**, **thresholds**, **data points**, and **period settings**. |
| 18 | ECS tasks failing | Check **task definition**, **IAM roles**, **logs**, **memory/CPU**, and **container exit codes**. |
| 19 | EC2 high CPU | Check **CloudWatch**, optimize app, consider **vertical scaling** or **load balancing**. |
| 20 | EBS volume attach fails | Check **AZ mismatch**, **volume state**, **instance limits**, and **permissions**. |
| 21 | DynamoDB latency | Check for **hot partitions**, use **LSI/GSIs**, enable **DAX**, optimize **query patterns**. |
| 22 | Lambda permission error | Check **IAM role**, attached **policies**, and **resource-based permissions**. |
| 23 | VPC endpoint not working | Verify **route tables**, **SGs**, **DNS settings**, and endpoint **policy**. |
| 24 | CloudFormation stack fails | Check **Events tab**, **template syntax**, **IAM permissions**, and **dependencies**. |
| 25 | AWS Config not tracking | Ensure **Config recorder** is enabled, right **resources selected**, and **IAM permissions**. |
| 26 | ELB unhealthy targets | Check **health check path/port**, **target status**, **SGs**, and **logs**. |
| 27 | CloudTrail missing events | Check **trail scope**, **multi-region settings**, **log delivery**, and **filters**. |
| 28 | Redshift performance issues | Analyze with **Query Performance tab**, **WLM queues**, **vacuum**, **analyze stats**. |
| 29 | S3 replication not working | Check **replication config**, **IAM roles**, **versioning**, and **object ownership**. |
| 30 | EKS node not joining | Check **IAM role**, **kubelet logs**, **user-data script**, and **security groups**. |
