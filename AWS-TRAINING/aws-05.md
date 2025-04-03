

A Route 53 DNS record is not resolving properly. How do you investigate?


# Debugging Route 53 DNS Resolution Issues

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Check Record Configuration in Route 53**    | Verify the record type (A, CNAME, ALIAS) and value in the Route 53 console. |
| **2**   | **Verify Domain Registration & Expiry**       | Ensure the domain is registered and not expired in Route 53 or another registrar. |
| **3**   | **Check Name Server (NS) Records**           | Run `whois <yourdomain.com>` and verify if the NS records match the Route 53 settings. |
| **4**   | **Verify Route 53 is Authoritative**         | Run `nslookup -type=ns <yourdomain.com>` to check the authoritative name servers. |
| **5**   | **Test DNS Resolution Using Dig or Nslookup** | `dig <yourdomain.com>` or `nslookup <yourdomain.com>` to check if DNS records are resolving. |
| **6**   | **Check DNS Propagation Status**             | If recent changes were made, use tools like [https://dnschecker.org](https://dnschecker.org) to check propagation. |
| **7**   | **Validate Health Check (If Used)**          | If the record uses health checks, verify their status in Route 53 console. |
| **8**   | **Check TTL (Time-To-Live) Settings**        | Lower TTL if recent updates are not reflecting quickly. |
| **9**   | **Check Firewall & Network Configurations**  | Ensure local network settings, VPNs, or firewalls are not blocking DNS resolution. |
| **10**  | **Verify ALIAS or CNAME Targets (For AWS Resources)** | Ensure the ALIAS record points to the correct AWS resource (e.g., ALB, S3, CloudFront). |

This structured guide helps systematically debug **Route 53 DNS resolution issues** efficiently. 🚀

# Debugging Route 53 DNS Resolution Issues

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Check Record Configuration in Route 53**    | Verify the record type (A, CNAME, ALIAS) and value in the Route 53 console. |
| **2**   | **Verify Domain Registration & Expiry**       | Ensure the domain is registered and not expired in Route 53 or another registrar. |
| **3**   | **Check Name Server (NS) Records**           | Run `whois <yourdomain.com>` and verify if the NS records match the Route 53 settings. |
| **4**   | **Verify Route 53 is Authoritative**         | Run `nslookup -type=ns <yourdomain.com>` to check the authoritative name servers. |
| **5**   | **Test DNS Resolution Using Dig or Nslookup** | `dig <yourdomain.com>` or `nslookup <yourdomain.com>` to check if DNS records are resolving. |
| **6**   | **Check DNS Propagation Status**             | If recent changes were made, use tools like [https://dnschecker.org](https://dnschecker.org) to check propagation. |
| **7**   | **Validate Health Check (If Used)**          | If the record uses health checks, verify their status in Route 53 console. |
| **8**   | **Check TTL (Time-To-Live) Settings**        | Lower TTL if recent updates are not reflecting quickly. |
| **9**   | **Check Firewall & Network Configurations**  | Ensure local network settings, VPNs, or firewalls are not blocking DNS resolution. |
| **10**  | **Verify ALIAS or CNAME Targets (For AWS Resources)** | Ensure the ALIAS record points to the correct AWS resource (e.g., ALB, S3, CloudFront). |

This structured guide helps systematically debug **Route 53 DNS resolution issues** efficiently. 🚀


An S3 bucket lifecycle policy is not deleting objects. What could be the issue?

# Debugging S3 Lifecycle Policy Not Deleting Objects

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Verify Lifecycle Policy in S3 Console**     | Go to **S3 Console > Bucket > Management > Lifecycle rules** and check if the policy exists. |
| **2**   | **Check Rule Status**                         | Ensure the lifecycle rule is **enabled** and applies to the correct prefix or objects. |
| **3**   | **Verify Object Age**                         | Objects must meet the **age condition** (e.g., `Expiration: 30 days`) before deletion. |
| **4**   | **Check Object Versioning**                   | If **versioning is enabled**, the lifecycle policy should include both **current and noncurrent versions**. |
| **5**   | **Validate Policy Actions**                   | Ensure the rule has **Delete action** enabled for the required object types. |
| **6**   | **Check Object Tags (If Used)**               | If the rule applies to specific tags, verify that objects have the correct tags using: `aws s3api get-object-tagging --bucket <BUCKET_NAME> --key <OBJECT_KEY>` |
| **7**   | **Check Permissions (IAM Role & Bucket Policy)** | Ensure the IAM role associated with S3 has `s3:DeleteObject` permissions. |
| **8**   | **Validate Expired Object Delete Marker (For Versioned Buckets)** | If `ExpiredObjectDeleteMarker` is missing, add it to delete expired objects. |
| **9**   | **Check AWS S3 Eventual Consistency**         | AWS S3 applies lifecycle rules asynchronously. Wait up to **24-48 hours** for changes to take effect. |
| **10**  | **Use AWS CLI to Simulate Lifecycle Rule**    | Run `aws s3api list-objects --bucket <BUCKET_NAME> --query 'Contents[?LastModified<=\`YYYY-MM-DD\`].Key'` to check if objects match the rule conditions. |

This structured guide helps systematically debug **S3 lifecycle policies not deleting objects**. 🚀


A customer reports intermittent 5XX errors from their API Gateway. How do you debug?

# Debugging Intermittent 5XX Errors in API Gateway

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Check API Gateway Logs (CloudWatch)**       | Run `aws logs tail /aws/apigateway/YOUR-API-NAME --follow` to check for error messages. |
| **2**   | **Verify Backend Health**                     | If using AWS Lambda, check CloudWatch logs for failures. If using an HTTP backend, ensure it's reachable. |
| **3**   | **Inspect API Gateway Execution Logs**        | Enable execution logs in **API Gateway > Stages > Logs/Tracing** and check CloudWatch. |
| **4**   | **Check Latency Issues**                      | Run `aws apigateway get-metrics --metric-name IntegrationLatency` to check if high latency is causing timeouts. |
| **5**   | **Review Throttling & Rate Limits**           | Verify if requests exceed API Gateway limits using `aws apigateway get-usage-plan`. |
| **6**   | **Test Backend Endpoint Directly**           | Use `curl -v <backend-url>` or `Postman` to check if the backend returns **5XX errors** independently. |
| **7**   | **Check API Gateway Integration Settings**    | Ensure the integration type (`AWS_PROXY`, `HTTP`, `MOCK`) is correct and properly configured. |
| **8**   | **Validate IAM Permissions (If Using AWS Services)** | Ensure API Gateway's IAM role has the correct permissions to invoke backend services. |
| **9**   | **Check for Recent Deployments or Changes**   | If the issue started after a deployment, rollback to a previous stable version. |
| **10**  | **Enable X-Ray Tracing**                      | In **API Gateway > Stages > Enable X-Ray**, analyze request flow to identify bottlenecks. |

This structured guide helps systematically debug **intermittent 5XX errors in API Gateway** efficiently. 🚀


A CloudWatch alarm is not triggering as expected. What steps do you take?



# Debugging a CloudWatch Alarm That Is Not Triggering

| Step No | Checkpoint                                     | Action/Command |
|---------|-----------------------------------------------|---------------|
| **1**   | **Verify the Alarm State**                   | Check the alarm status in **CloudWatch > Alarms** to see if it is in `ALARM`, `OK`, or `INSUFFICIENT_DATA`. |
| **2**   | **Check the Metric Data**                    | Go to **CloudWatch > Metrics**, select the metric, and verify if it is reporting data correctly. |
| **3**   | **Ensure the Threshold is Correct**          | Confirm that the alarm threshold matches the expected value range. |
| **4**   | **Check the Evaluation Period**              | If the evaluation period is long, the alarm might take time to trigger. Reduce the period if needed. |
| **5**   | **Verify Alarm Conditions**                  | Ensure the condition (`GreaterThanThreshold`, `LessThanThreshold`, `GreaterThanOrEqualToThreshold`) is set correctly. |
| **6**   | **Inspect Data Gaps**                        | If no data is reported, the alarm won't trigger. Check for missing metric data in CloudWatch. |
| **7**   | **Check for Missing Permissions**            | If using SNS notifications, ensure the alarm has permissions to publish to the SNS topic. |
| **8**   | **Test SNS Notification (If Configured)**    | Manually publish a message to the SNS topic using: `aws sns publish --topic-arn <sns-topic-arn> --message "Test Message"` |
| **9**   | **Check for Alarm Suppression**              | If the alarm is part of an AWS Auto Scaling policy, ensure no cooldown periods or policies are preventing it from triggering. |
| **10**  | **Manually Trigger the Alarm for Testing**   | Temporarily lower the threshold or create a test alarm to confirm if it triggers. |

This step-by-step guide ensures a structured approach to troubleshooting **CloudWatch alarms not triggering**. 🚀







