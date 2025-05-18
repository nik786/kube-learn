
A VPC endpoint is not working as expected. What do you check first?

# Troubleshooting a VPC Endpoint Issue

| Step No | Checkpoint                                    | Possible Issue & Solution |
|---------|----------------------------------------------|---------------------------|
| **1**   | **Verify Endpoint Type**                    | Ensure the correct **VPC endpoint type** is used: **Interface** or **Gateway**. Some AWS services require a specific type. |
| **2**   | **Check Security Groups**                   | For **Interface endpoints**, security groups may be blocking traffic. Allow inbound traffic on the required ports. |
| **3**   | **Verify Route Tables**                     | For **Gateway endpoints**, ensure the **route table** has the correct route pointing to the VPC endpoint. |
| **4**   | **Confirm DNS Resolution**                  | If using an **Interface endpoint**, ensure **private DNS** is enabled and test with `nslookup` or `dig`. |
| **5**   | **Check Network ACLs**                      | Ensure **Network ACLs** allow traffic between the **subnet** and the VPC endpoint. |
| **6**   | **Validate IAM Policies**                   | Ensure the **IAM policy** attached to the endpoint allows access to the required AWS service. |
| **7**   | **Use VPC Flow Logs**                       | Enable **VPC Flow Logs** to check if requests are reaching the **VPC endpoint**. |
| **8**   | **Verify Service Name**                     | Ensure the **AWS service name** used in the endpoint configuration matches the correct AWS region. |
| **9**   | **Test Connectivity**                       | Use `telnet <service-endpoint> <port>` or `curl` to test connectivity to the VPC endpoint. |
| **10**  | **Check AWS Service Availability**          | Ensure the AWS service you are trying to access is **available in the selected region**. |

### Conclusion:
By systematically verifying **network configurations, policies, and logs**, you can identify and resolve VPC endpoint issues effectively. 🚀  


A CloudFormation stack deployment fails. How do you troubleshoot?


# Troubleshooting a CloudFormation Stack Deployment Failure

| Step No | Checkpoint                                  | Possible Issue & Solution |
|---------|--------------------------------------------|---------------------------|
| **1**   | **Check the CloudFormation Events**       | Go to the AWS Console → **CloudFormation** → **Events**. Look for failed events and error messages. |
| **2**   | **Validate the Template Syntax**          | Use `aws cloudformation validate-template --template-body file://template.yaml` to check for syntax errors. |
| **3**   | **Check IAM Permissions**                 | Ensure that the **IAM roles** used have the required permissions to create/update AWS resources. |
| **4**   | **Verify Resource Limits**                | AWS has **limits on resources** (e.g., EC2 instances, VPCs). Check if you've exceeded these limits. |
| **5**   | **Check for Conflicting Resources**       | Ensure the stack isn't creating resources that **already exist**, which might cause conflicts. |
| **6**   | **Look at Logs (if applicable)**         | For **Lambda functions** or other compute resources, check **CloudWatch Logs** for detailed errors. |
| **7**   | **Check Dependencies**                    | Ensure that dependent resources (e.g., S3 buckets, IAM roles) exist **before** deploying the stack. |
| **8**   | **Review Parameter Values**               | Incorrect parameter values (e.g., invalid CIDR blocks) can cause failures. Double-check them. |
| **9**   | **Check Rollback Behavior**               | If rollback is enabled, AWS automatically deletes resources on failure. Disable rollback to debug (`--disable-rollback`). |
| **10**  | **Use Drift Detection**                   | If updating an existing stack, check for **drift** (`aws cloudformation detect-stack-drift`) to see if manual changes conflict with the template. |

### Conclusion:
By analyzing **CloudFormation Events, IAM roles, dependencies, and resource limits**, you can systematically identify and resolve deployment failures. 🚀  


 A user reports that AWS Config is not tracking changes. What could be the issue?

# AWS Config is Not Tracking Changes – Troubleshooting Guide

| Step No | Checkpoint                                  | Possible Issue & Solution |
|---------|--------------------------------------------|---------------------------|
| **1**   | **Check if AWS Config is Enabled**        | Go to **AWS Console → AWS Config** and verify if it is **enabled** for the account and region. |
| **2**   | **Verify Recording Rules**                | Ensure that the correct **resources** (EC2, S3, IAM, etc.) are selected for tracking under **"Recording rules"**. |
| **3**   | **Check IAM Permissions**                 | The AWS Config role must have the correct permissions (`AWSConfigRole`). Ensure it has `config:Put*` and `config:Describe*` permissions. |
| **4**   | **Verify Delivery Channel**               | AWS Config requires an **S3 bucket** and an **SNS topic** (if enabled). Check if the S3 bucket exists and is accessible. |
| **5**   | **Check AWS Config Logs**                 | Navigate to **CloudWatch Logs** (`/aws/config`) and check for errors or missing logs. |
| **6**   | **Confirm SNS Topic Subscription**        | If AWS Config is set to send notifications via SNS, check if the **SNS topic is active** and has valid subscribers. |
| **7**   | **Validate Configuration Recorder**       | Run `aws configservice describe-configuration-recorders` and check if the `recording` field is set to `true`. |
| **8**   | **Check for AWS Config Rules Status**     | Go to **AWS Config → Rules** and ensure rules are **active** and not in an `Evaluating` or `Failed` state. |
| **9**   | **Check for Region-Specific Issues**      | AWS Config is region-specific. Ensure you're checking in the **correct AWS region**. |
| **10**  | **Restart AWS Config Recording**          | Try stopping and restarting the configuration recorder:  
  ```sh
  aws configservice stop-configuration-recorder --configuration-recorder-name default
  aws configservice start-configuration-recorder --configuration-recorder-name default

```


A customer’s ELB is marked as unhealthy for all targets. What do you check?


# ELB Marked as Unhealthy for All Targets – Troubleshooting Guide

| Step No | Checkpoint                                   | Possible Issue & Solution |
|---------|---------------------------------------------|---------------------------|
| **1**   | **Check Target Group Health Status**       | Go to **EC2 → Target Groups** and check the **Health status** of targets. If all are **unhealthy**, proceed with further checks. |
| **2**   | **Verify Health Check Configuration**      | Ensure the **path**, **port**, **protocol**, and **intervals** for health checks are correctly configured under **Target Group → Health Checks**. |
| **3**   | **Check Security Groups**                  | The EC2 instances must allow **incoming traffic** on the **health check port** from the **ELB’s security group**. |
| **4**   | **Check Instance Subnet & Routing**        | Ensure that instances are in the correct **subnet**, have a **public/private route table**, and are reachable by the ELB. |
| **5**   | **Verify Application & Listener Port**     | Ensure the application is **running** and **listening** on the correct port. Use:  
  ```sh
  netstat -tulnp | grep LISTEN
  curl -v http://localhost:<PORT>
```



