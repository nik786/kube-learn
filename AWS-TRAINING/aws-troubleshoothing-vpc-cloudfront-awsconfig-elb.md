
A VPC endpoint is not working as expected. What do you check first?

# Troubleshooting a VPC Endpoint Issue

| Step | Check | Quick Reminder |
|------|-------|----------------|
| 1 | Endpoint Type | Verify **Interface vs Gateway** endpoint. |
| 2 | Security Groups | Ensure required ports are allowed. |
| 3 | Route Tables | Confirm routes point to the endpoint. |
| 4 | DNS Resolution | Check Private DNS and name resolution. |
| 5 | IAM Policies | Verify endpoint and IAM permissions. |
| 6 | Network ACLs | Ensure subnet traffic is not blocked. |
| 7 | VPC Flow Logs | Check if traffic reaches the endpoint. |
| 8 | Connectivity Test | Use `curl` or `telnet` to validate access. |


Endpoint → SG → Route → DNS → IAM → NACL → Flow Logs → Connectivity

Or remember:

"ESRDINFC"

E = Endpoint Type
S = Security Groups
R = Route Tables
D = DNS
I = IAM
N = Network ACLs
F = Flow Logs
C = Connectivity Test



### Conclusion:
By systematically verifying **network configurations, policies, and logs**, you can identify and resolve VPC endpoint issues effectively. 🚀  


A CloudFormation stack deployment fails. How do you troubleshoot?


# Troubleshooting a CloudFormation Stack Deployment Failure

| Step | Check | Quick Reminder |
|------|-------|----------------|
| 1 | Events | Check CloudFormation Events for errors. |
| 2 | Template | Validate template syntax and format. |
| 3 | IAM | Verify required permissions and roles. |
| 4 | Parameters | Check parameter values and inputs. |
| 5 | Dependencies | Ensure dependent resources exist. |
| 6 | Resource Limits | Verify AWS service quotas are not exceeded. |
| 7 | Logs | Check CloudWatch Logs for detailed errors. |


Easy Interview Sequence

Events → Template → IAM → Parameters → Dependencies → Limits → Logs

Or remember:

"ETIPDLL"

E = Events
T = Template
I = IAM
P = Parameters
D = Dependencies
L = Limits
L = Logs


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



