


AWS Landing Zone
-----------------
An AWS Landing Zone is a pre-configured, secure, and scalable multi-account 
AWS environment that follows best practices for governance, security, and compliance.


Landing Zone
-------------

| **Aspect**                        | **Description**                                                                 |
|----------------------------------|---------------------------------------------------------------------------------|
| **1. Account Structure**         | Organize accounts by function (e.g., Security, Logging, Dev, Prod) using AWS Organizations. |
| **2. Identity & Access Management** | Implement centralized IAM via AWS SSO or IAM Identity Center for secure access control. |
| **3. Networking**                | Design a scalable VPC structure with private/public subnets, NAT gateways, and Transit Gateway. |
| **4. Security Baseline**        | Enforce Guardrails using AWS Control Tower, SCPs, and security services like AWS Config and CloudTrail. |
| **5. Logging & Monitoring**      | Centralize logs using AWS CloudTrail, CloudWatch, and AWS Config in a dedicated logging account. |
| **6. Automation & CI/CD**       | Use Infrastructure as Code (e.g., Terraform, CloudFormation) for repeatable and consistent deployments. |
| **7. Cost Management**           | Implement budget alarms, tagging strategy, and cost explorer for visibility and governance. |
| **8. Compliance & Governance**   | Apply service control policies, encryption, and region restrictions to meet compliance requirements. |




how many accounts you have handled in aws for your project? how to switch to multiple accounts in aws?
please mentioned following solutions with brief process in table for .md file
1. sts
2. organization
3. tower
4. catalogue
5. trust relationship


## AWS Multi-Account Management and Switching Methods  

### **How Many AWS Accounts Have You Managed?**  
I have managed **4–6 AWS accounts** in my project, covering:  
- **Development (Dev)**
- **Staging (Stage/UAT)**
- **Production (Prod)**
- **Security & Compliance**
- **Logging & Monitoring**
- **Shared Services**

### **Methods to Switch Between AWS Accounts**  

| **Method**               | **Description** | **Brief Process** |
|--------------------------|----------------|--------------------|
| **STS (Security Token Service)** | Enables temporary access to assume roles in other AWS accounts. | 1. Create an IAM role in the target account with necessary permissions.<br>2. Use `aws sts assume-role` to switch roles programmatically.<br>3. Retrieve temporary credentials and use them for API calls. |
| **AWS Organizations** | Centralized account management with consolidated billing and SCP (Service Control Policies). | 1. Create an AWS Organization and invite accounts.<br>2. Apply SCPs to enforce policies.<br>3. Use AWS SSO or IAM roles to access multiple accounts. |
| **AWS Control Tower** | Automates multi-account setup with best practices and guardrails. | 1. Deploy Control Tower to manage account lifecycle.<br>2. Use AWS SSO for account switching.<br>3. Enforce security guardrails and compliance policies. |
| **AWS Service Catalog** | Enables cross-account infrastructure provisioning via pre-approved CloudFormation templates. | 1. Create and share product portfolios across accounts.<br>2. Grant access to users/roles.<br>3. Launch services from the catalog without manual setup. |
| **Trust Relationships** | Establishes cross-account access by defining IAM role trust policies. | 1. Create an IAM role in the target account.<br>2. Modify the trust policy to allow access from another AWS account.<br>3. Assume the role via AWS CLI, SDK, or console. |
| **SCP (Service Control Policies)** | Restricts or allows specific actions across AWS accounts in an Organization. | 1. Define an SCP policy with allowed/denied actions.<br>2. Attach SCP to an AWS Organizational Unit (OU) or specific account.<br>3. Ensure IAM roles align with SCP permissions. |




scps

prevent memeber account from leaving organizations

block service access for the root user


prevent user from disabling aws config or changing its rule

require aws instance to use specfic type


prevent user from deleting vpc flow logs

prevent any vpc that does nt have internet access from getting it






Cross Account/Multiple Accounts
---------------------------------

aws organizations

- [AWS Organization for Account & Multiple Account setup: Step-by-Step Tutorial (Part-2)](https://www.youtube.com/watch?v=bQ2EtLnN6KQ)

- [AWS Assume IAM Role - Step by Step tutorial (Part-3)](https://www.youtube.com/watch?v=MkiWa31iV6U)

- [AWS - Switch Roles / Cross Account Access](https://www.youtube.com/watch?v=d7R08uPS98M&t=254s) 



root account

dev-ou
dev account

test-ou
test account



Assume Role



```

{
"version": "2012-09-10",
"Statement": [
 {
  "Sid": "statement1",
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam:635163516:role/s3-access"
}
}
}

```

```
Switch Role

Account - 23523264262

Role - s3-full-access

Display Name - 

Color - 

```

Use case
--------

Vipin should have full access

- full EC2 & S3 in dev and prod

Deepak should have only access 

- read only access ec2 and s3 in dev and no access in prod


trust relationship


https://github.com/infra-ops/aws_poc/blob/master/multi_account_management/organisations/ec2/t2-micro.json

https://github.com/infra-ops/aws_poc/blob/master/multi_account_management/organisations/bucket/s3.json


Service Catalogue
------------------

https://github.com/infra-ops/aws_poc/blob/master/service_catalouge/cf/constraint.json



What is the purpose of Identity Provider?
------------------------------------------

| **Concept**            | **Explanation**                                                                                              |
|------------------------|--------------------------------------------------------------------------------------------------------------|
| **Identity Provider**   | An Identity Provider (IdP) helps establish trust between AWS and the corporate Active Directory (AD) environment. |
| **Federated Role**      | When creating a federated role, the IdP authenticates users, and the federated role grants them access to AWS resources. |
| **Trust Relationship**  | The trust between AWS and the corporate AD environment is established through the IdP, allowing secure access. |
| **Single Sign-On (SSO)**| Users can authenticate once through the corporate AD, and then assume roles to access AWS resources without needing separate credentials. |
| **Secure Authentication**| The IdP ensures that users are authenticated securely before granting temporary access via federated roles. |




What are the benefits of STS (Security Token Service):
-------------------------------------------------------

| **Benefit**                        | **Explanation**                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Temporary Security Credentials** | STS provides temporary security credentials, reducing the need to store long-term credentials.            |
| **Granular Access Control**        | STS enables fine-grained access control by assigning specific permissions to users or services.           |
| **Cross-Account Access**           | STS allows users to assume roles in other AWS accounts, facilitating secure cross-account access.         |
| **Integration with Identity Providers** | STS integrates with identity providers (e.g., SAML, OpenID) to allow federated access for external users. |
| **Reduced Risk of Credential Exposure** | Temporary credentials are automatically rotated, reducing the risk of exposure compared to static credentials. |



