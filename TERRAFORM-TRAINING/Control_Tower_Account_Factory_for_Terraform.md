

Control_Tower_Account_Factory_for_Terraform
---------------------------------------------

- [terraform-aws-control_tower_account_factory](https://github.com/aws-ia/terraform-aws-control_tower_account_factory)
- https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html




| **Section**                          | **Summary** |
|--------------------------------------|-------------|
| **Overview**                         | AFT integrates with AWS Control Tower to provide GitOps-style account provisioning and customization using Terraform. Stores metadata/audit history, applies tags, and supports feature flags like CloudTrail data events, default VPC deletion, and Enterprise Support enrolment. Requires an existing Control Tower landing zone and creates a separate “AFT management account” :contentReference[oaicite:1]{index=1}. |
| **Key Features**                     | Supports open-source, Terraform Cloud/Enterprise, and CodeCommit/GitHub/Bitbucket. Enables account-level tags, global or targeted customizations, and optional enforcement of compliance best practices :contentReference[oaicite:2]{index=2}. |
| **Architecture & Workflow**         | Operations run in the AFT management account. Workflow: submit request → Control Tower provisioning → global customizations → account-level customizations. Requests are queued first-in-first-out :contentReference[oaicite:3]{index=3}. |
| **Core Components**                 | Leverages AWS services including CodePipeline, CodeBuild, Lambda, Step Functions, DynamoDB, S3, EventBridge, CloudWatch, IAM roles/policies, KMS (with key rotation), and optional organization-level CloudTrail and AWS Enterprise Support enrollment :contentReference[oaicite:4]{index=4}. |
| **Setup Steps**                     | 1. Ensure Control Tower landing zone.<br>2. Create dedicated OU & provision AFT management account.<br>3. Prepare Terraform environment (v0.15+).<br>4. Invoke AFT Terraform module with required variables.<br>5. Secure backend state, allow 30 min deployment, set STS credentials long enough :contentReference[oaicite:5]{index=5}. |
| **Customization Repos**            | Uses four git repos:<br>– `aft-account-request` – for initiating provisioning<br>– `aft-global-customizations` – Terraform applied to all accounts<br>– `aft-account-customizations` – per-account Terraform customizations<br>– `aft-account-provisioning-customizations` – for Step Functions / Lambda integrations :contentReference[oaicite:6]{index=6}. |
| **Importing Existing Accounts**     | Supported since AFT v1.3.1. Imported via Terraform manifest in `aft-account-request` repo, enabling management and customization through the AFT pipeline :contentReference[oaicite:7]{index=7}. |
| **Limitations & Best Practices**    | No GUI dashboard or metrics for AFT; testing updates is difficult because only default branch is allowed. Recommended to secure Terraform state, use long-duration credentials, and follow CI/CD best practices :contentReference[oaicite:8]{index=8}. |



Step 1: Launch your AWS Control Tower landing zone
Before launching AFT, you must have a working AWS Control Tower landing zone in your AWS account. 
You will configure and launch AFT from the AWS Control Tower management account.

Step 2: Create a new organizational unit for AFT (recommended)
We recommend that you create a separate OU in your AWS Organization, where you will deploy the AFT management account. 
Create an OU through your AWS Control Tower management account.

Step 3: Provision the AFT management account
AFT requires a separate AWS account to manage and orchestrate its own requests. 
From the AWS Control Tower management account that's associated with your AWS Control Tower landing zone, you'll provision this account for AFT.

Step 4: Ensure that the Terraform environment is available for deployment
This step assumes that you are experienced with Terraform, and that you have procedures in place for executing Terraform. 
AFT supports Terraform Version 0.15.x or later.

Step 5: Call the Account Factory for Terraform module to deploy AFT
The Account Factory for Terraform module must be called while you are authenticated with AdministratorAccess credentials in your AWS Control Tower management account.



```

module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"
  
  # VPC configuration
  aft_customer_vpc_id = "vpc-0123456789abcdef0"
  aft_customer_private_subnets = ["subnet-0123456789abcdef0", "subnet-0123456789abcdef1"]
  
  # Other AFT parameters...
}


```      

```
module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"
  
  # Project name configuration
  terraform_project_name = "my-organization-aft"
  
  # Other AFT parameters...
}

```


```
module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"
  
  # Custom tags configuration
  tags = {
    Environment = "Production"
    CostCenter = "IT-12345"
    Project = "AFT-Deployment"
    Owner = "platform-team@example.com"
  }
  
  # Other AFT parameters...
}

```






