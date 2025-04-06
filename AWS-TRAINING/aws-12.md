
| **Category**                  | **Example 1**                                                  | **Example 2**                                                 | **Example 3**                                                 |
|------------------------------|----------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| **Account Provisioning**     | Creating AWS account via Control Tower                        | Setting up IAM roles/groups for new teams                    | Integrating SSO with Identity Provider (e.g., Okta, AD)       |
| **Policy Provisioning**      | Creating IAM policies for least-privilege access               | Enforcing SCPs for Org Units                                  | Applying tag policies across environments                     |
| **Network Support**          | Setting up VPC with subnets and route tables                  | Configuring VPN or Direct Connect                             | Implementing Transit Gateway for inter-VPC traffic            |
| **Resource Deployment**      | Automating EC2 provisioning using Terraform                    | Creating S3 buckets with lifecycle policies                   | Deploying EKS cluster using IaC                               |
| **Incident Support (Daily)** | Restarting failed EC2 instance                                 | Resolving disk space issues on RDS                            | Investigating failed Lambda invocation                        |
| **Security Incident Support**| Isolating compromised EC2 instance                             | Rotating IAM credentials after suspicious activity            | Analyzing GuardDuty alert for unauthorized access attempts    |



| **Security Breach Scenario**                                     | **Description**                                                                 | **Solution**                                                                                   |
|------------------------------------------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **1. S3 Bucket Public Access**                                   | Sensitive data exposed due to misconfigured public permissions                  | Enable **Block Public Access**, use **bucket policies**, and audit with **AWS Config Rules**  |
| **2. Leaked IAM Credentials**                                    | IAM access keys pushed to public repositories like GitHub                       | Use **AWS Secrets Manager** or **IAM roles**, and enable **Access Analyzer** for detections   |
| **3. Unrestricted Security Group**                               | Ports like 22/3389 open to the world                                            | Restrict IPs using **security group rules**, use **AWS Firewall Manager** for compliance      |
| **4. Lack of MFA on Root Account**                               | Unauthorized access to high-privilege account                                   | Enforce **MFA on root** and use **IAM Identity Center** (SSO) for controlled access           |
| **5. Overly Permissive IAM Roles**                               | Users/services have broader permissions than needed                             | Apply **least privilege** with **IAM Access Analyzer** and **policy boundaries**              |
| **6. Unencrypted Data at Rest/Transit**                          | Data stored or transmitted without encryption                                   | Use **KMS**, enforce **SSL/TLS**, enable **default encryption** on S3/EBS/RDS                 |
| **7. Malicious Lambda or EC2 Behavior**                          | Suspicious behavior from compute resources                                      | Use **GuardDuty**, **CloudTrail**, and **Security Hub** for detection and response            |
| **8. Misconfigured CloudTrail or Logging Disabled**              | Loss of visibility into AWS account activity                                    | Ensure **CloudTrail** is enabled in all regions, with logs sent to **S3 with SSE**            |
| **9. Unused Access Keys or Passwords**                           | Forgotten credentials become security risks                                     | Use **IAM credential reports**, rotate or delete old keys, enforce **password policies**      |
| **10. Disabled AWS Config or Lack of Monitoring**                | No audit trail of resource changes                                              | Enable **AWS Config**, define **rules for compliance**, integrate with **SNS for alerts**     |
