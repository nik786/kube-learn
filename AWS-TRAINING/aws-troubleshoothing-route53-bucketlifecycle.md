

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









