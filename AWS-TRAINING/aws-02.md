
A customer cannot SSH into their EC2 instance. How do you troubleshoot?

# Troubleshooting: Cannot SSH into EC2 Instance

| Check | Steps to Fix |
|-------|-------------|
| **Security Group** | Allow inbound SSH (port `22`) from your IP in EC2 security group. |
| **Network ACLs** | Ensure Network ACL allows inbound & outbound SSH (`22`). |
| **Key Pair** | Use the correct private key (`.pem`) when connecting. |
| **EC2 Instance State** | Check if the instance is running and not stopped or terminated. |
| **Public IP** | Use the correct public IP or Elastic IP to connect. |
| **User & Command** | Use the correct username: `ec2-user` (Amazon Linux), `ubuntu` (Ubuntu). Example: `ssh -i key.pem ec2-user@<public-ip>`. |
| **SSH Agent Issues** | If using an SSH agent, ensure the key is added (`ssh-add key.pem`). |
| **Disk Full** | If disk is full, try connecting via **EC2 Serial Console** or **SSM Session Manager**. |
| **Instance in Private Subnet** | Use a **bastion host** or **VPN** to access private instances. |
| **OS-Level SSH Config** | Check `/etc/ssh/sshd_config` for issues (`PermitRootLogin` and `PasswordAuthentication`). |


An S3 bucket is giving a 403 Forbidden error despite public access. What could be the issue?

# Troubleshooting: S3 Bucket 403 Forbidden Error

| Possible Issue | Steps to Fix |
|---------------|-------------|
| **Bucket Policy** | Ensure the bucket policy allows `s3:GetObject` for public access. |
| **Block Public Access** | Check if "Block all public access" is enabled in bucket settings. Disable if needed. |
| **Object ACL** | If using ACLs, ensure objects are marked as `public-read`. |
| **IAM Permissions** | Ensure your IAM user or role has `s3:GetObject` and `s3:ListBucket` permissions. |
| **Signed URLs Required** | If using signed URLs, verify they are valid and not expired. |
| **VPC Endpoint Restrictions** | If accessing via VPC endpoint, ensure correct permissions and endpoint policy. |
| **Bucket Ownership Settings** | If `BucketOwnerEnforced` is enabled, only bucket owners can grant access. |
| **Request Origin** | If accessing from a website, check CORS settings in the bucket. |



A Lambda function is timing out. How do you debug this?

# Troubleshooting: Lambda Function Timing Out

| Possible Issue | Steps to Fix |
|---------------|-------------|
| **Function Timeout Too Low** | Increase the timeout setting in Lambda (Max: 15 mins). |
| **Long-Running Code** | Optimize code logic, avoid unnecessary loops or delays. |
| **External API Calls** | Check for slow API responses; use asynchronous processing if needed. |
| **Database Queries** | Optimize queries, use indexes, and batch processing. |
| **VPC Configuration** | If inside a VPC, ensure proper security groups, subnets, and NAT gateway for internet access. |
| **Cold Start Delay** | Reduce cold start time by using **Provisioned Concurrency**. |
| **Logging & Monitoring** | Check **Amazon CloudWatch Logs** for function execution details. |
| **Memory Allocation** | Increase memory (more memory = better CPU performance). |
| **Deadlocks or Infinite Loops** | Check for infinite loops or unhandled recursive calls in your code. |




An RDS database is running slow. What steps do you take to identify the cause?


# Troubleshooting: RDS Database Running Slow

| Possible Issue | Steps to Fix |
|---------------|-------------|
| **High CPU or Memory Usage** | Check Amazon CloudWatch metrics and upgrade instance type if needed. |
| **Slow Queries** | Use `EXPLAIN ANALYZE` to identify slow queries and optimize indexes. |
| **Insufficient Indexing** | Add indexes to frequently queried columns to improve performance. |
| **Too Many Connections** | Check `max_connections` setting and scale up if needed. |
| **Storage Bottleneck** | Ensure enough storage and enable **Provisioned IOPS** if required. |
| **Long-Running Transactions** | Identify and terminate unoptimized or idle transactions. |
| **Read Query Overload** | Use **Read Replicas** for high read traffic workloads. |
| **Network Latency** | Check if RDS is in the same region as your application. |
| **Parameter Group Misconfiguration** | Tune database parameters like `work_mem`, `innodb_buffer_pool_size`. |
| **Background Processes** | Monitor and optimize background jobs like vacuuming (PostgreSQL) or auto-analyze. |



A user reports high AWS billing for S3. How do you investigate?

# Troubleshooting: High AWS S3 Billing

| Possible Issue | Steps to Investigate & Fix |
|---------------|----------------------------|
| **Storage Usage** | Check total storage size in **AWS S3 Storage Lens** or **AWS Cost Explorer**. Delete unnecessary objects. |
| **Versioning Enabled** | If **S3 Versioning** is enabled, old versions may increase storage costs. Enable **Lifecycle Policies** to delete old versions. |
| **High Data Transfer (Egress)** | Check if data is being accessed from outside AWS. Use **CloudFront** for caching or move resources closer to users. |
| **Frequent API Requests** | Use **AWS CloudTrail** to check excessive `GET`, `PUT`, or `LIST` requests. Optimize API calls. |
| **Glacier Retrieval Costs** | If using **S3 Glacier**, check retrieval requests. Optimize retrieval tiers to reduce costs. |
| **Cross-Region Replication** | If **CRR** is enabled, it may increase costs. Disable if not needed. |
| **Unnecessary Storage Classes** | Check if frequently accessed files are in **Glacier** or **Infrequent Access (IA)**, causing high retrieval costs. Adjust storage classes. |
| **Logging & Analytics Costs** | If **server access logging** is enabled, logs may consume storage. Review and optimize logging settings. |
| **Public Access or Misuse** | Ensure bucket is not publicly accessible. Check **AWS CloudTrail** for unauthorized access. |
| **Lifecycle Policies** | Set up lifecycle rules to automatically move or delete unused files and reduce costs. |







