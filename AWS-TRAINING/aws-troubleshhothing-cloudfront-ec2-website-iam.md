
A customer’s CloudFront distribution is not serving updated content. What could be wrong?

# Troubleshooting: CloudFront Not Serving Updated Content

| Possible Issue | Steps to Investigate & Fix |
|---------------|----------------------------|
| **Cached Old Content** | Invalidate the cache using **CloudFront Invalidation** or set a lower TTL for objects. |
| **S3 Object Versioning** | Enable **S3 Versioning** and update object URLs to ensure CloudFront fetches the latest content. |
| **Long TTL Settings** | Check **Cache-Control** and **Expires** headers in the origin response. Use a shorter TTL if needed. |
| **Serving from Edge Cache** | Wait for **CloudFront TTL expiry** or manually invalidate specific files. |
| **Origin is Not Updating** | Ensure the origin (S3, EC2, or another server) has the latest content. |
| **Wrong Behaviors Configured** | Verify **Cache Behavior Settings** in CloudFront and make sure caching rules match your needs. |
| **Compression Issues** | Ensure **gzip** or **Brotli compression** is correctly set up to avoid mismatched cached versions. |
| **Custom Headers Misconfiguration** | If using custom headers, ensure they are correctly forwarded to the origin. |
| **CloudFront Not Using Latest S3 Version** | If using an **S3 bucket origin**, try appending a version query string (e.g., `file.css?v=2`). |

```
In Amazon CloudFront, OAI stands for Origin Access Identity.

✅ Meaning:
An OAI is a special CloudFront user identity that you create to give CloudFront permission to access a private Amazon S3 bucket on your behalf.

✅ Why it's used:

When you store files in an S3 bucket, you usually don’t want them to be publicly accessible.

By creating an OAI and attaching it to your CloudFront distribution, only CloudFront can fetch objects from S3.

End users access content through CloudFront, not directly from S3.

✅ Workflow:

Create a CloudFront distribution.

Create an OAI.

Update the S3 bucket policy to allow access only from that OAI.

Disable direct public access to the bucket.

This way, your content is secure and served only through CloudFront.

```



# Troubleshooting: EC2 Instance Stopped & Won’t Start  

| Possible Issue | Steps to Investigate & Fix |
|---------------|----------------------------|
| **Instance Limit Reached** | Check **EC2 service quotas** in AWS Console and request a limit increase if needed. |
| **Insufficient Instance Type Capacity** | Try changing the instance type to one with available capacity in the selected AZ. |
| **Billing Issue** | Ensure your AWS account is active and there are no pending payments blocking instance start. |
| **Root Volume Issues** | Check if the **EBS root volume** is attached and not full or corrupted. |
| **EBS Volume in "Error" State** | Detach the volume, create a new instance, attach the volume, and repair filesystem issues. |
| **IAM Role or Permissions Issue** | Ensure the instance has the correct IAM role and permissions to start. |
| **Security Group or Network ACL Blocking** | Verify security groups and **Network ACLs** are not restricting network access. |
| **Kernel or OS Corruption** | If the instance is unbootable, create a rescue instance, attach the volume, and check logs. |
| **Instance State Lock** | If instance is locked due to **host failure**, AWS might need to intervene. Try stopping and starting it again. |
| **Instance Termination Protection** | If enabled, disable it and retry starting the instance. |


 A customer’s website running on AWS goes down. How do you perform an initial diagnosis?

 # Troubleshooting: AWS Website is Down  

| Possible Issue | Steps to Investigate & Fix |
|---------------|----------------------------|
| **Check Website Availability** | Use `ping` or `curl` to check if the website responds. Test from different locations. |
| **Domain and DNS Issues** | Verify **Route 53** settings and check if the domain name resolves using `nslookup` or `dig`. |
| **Load Balancer Issues** | Check **ELB (Elastic Load Balancer)** health checks and ensure targets are healthy. |
| **EC2 Instance Down** | Check if EC2 instances are running. Restart if needed. |
| **Auto Scaling Failure** | Verify if **Auto Scaling Group** has launched new instances if one failed. |
| **Security Group & NACL Issues** | Ensure Security Groups and **Network ACLs** allow inbound traffic on necessary ports. |
| **Application Errors** | Check web server logs (`/var/log/nginx/access.log`, `/var/log/httpd/error_log`, etc.) for errors. |
| **Database Issues** | If the site depends on a database (RDS, DynamoDB), check its status and query performance. |
| **S3 Website Hosting Issues** | Ensure S3 bucket settings allow public access (if using S3 for static hosting). |
| **CloudFront Issues** | Check if CloudFront is serving cached content or experiencing delays. |
| **AWS Outage** | Check the **AWS Health Dashboard** for any ongoing regional issues. |



An IAM user is unable to assume a role. What could be the possible reasons?

# Troubleshooting: IAM User Unable to Assume a Role  

| Possible Issue | Steps to Investigate & Fix |
|---------------|----------------------------|
| **Incorrect IAM Policy** | Ensure the IAM user has the correct `sts:AssumeRole` permission in their policy. |
| **Role Trust Policy Not Configured** | Verify the role's **Trust Policy** allows the user or their IAM group to assume it. |
| **Session Duration Too Long** | Check if the requested session duration exceeds the role’s `MaxSessionDuration` limit. |
| **MFA Requirement Not Met** | If MFA is required, ensure the user provides a valid MFA token when assuming the role. |
| **Wrong Role ARN Used** | Ensure the user is using the correct **Role ARN** when calling `aws sts assume-role`. |
| **Region Mismatch** | Ensure the request is being made in the correct AWS region where the role exists. |
| **IAM Identity Not Attached to Role** | If assuming via an EC2 instance, check if the instance profile is attached correctly. |
| **AWS Organizations SCP Restrictions** | Check if a **Service Control Policy (SCP)** is blocking role assumption. |
| **Temporary Credentials Expired** | If using temporary credentials, ensure they are still valid and not expired. |


