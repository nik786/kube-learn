

An Auto Scaling Group is not launching new instances as expected. How do you debug?
------------------------------------------------------------------------------------


# Debugging Auto Scaling Group (ASG) Not Launching Instances

| Step No | Checkpoint                              | Action/Command |
|---------|----------------------------------------|---------------|
| **1**   | **Check ASG Desired vs. Current Count** | Verify if the **desired capacity** is greater than the **current instance count**. |
| **2**   | **Check Scaling Policies**            | Ensure there is an active **scaling policy** triggering instance launches. |
| **3**   | **Check EC2 Instance Quotas**         | `aws service-quotas list-service-quotas --service-code ec2` |
| **4**   | **Check Launch Template/Configuration** | Verify the correct **AMI, instance type, and security groups** are configured. |
| **5**   | **Check Instance Availability in Subnets** | Ensure that **subnets have capacity** to launch instances. |
| **6**   | **Check IAM Permissions**             | Ensure the ASG has the required **IAM role** to launch EC2 instances. |
| **7**   | **Check Spot Instance Capacity (if using Spot)** | If using **Spot instances**, check **availability of instance types**. |
| **8**   | **Check Scaling Activity History**    | `aws autoscaling describe-scaling-activities --auto-scaling-group-name <ASG_NAME>` |
| **9**   | **Check Instance State Transitions**  | `aws ec2 describe-instances --filters "Name=tag:aws:autoscaling:groupName,Values=<ASG_NAME>"` |
| **10**  | **Check ASG Health Check Settings**   | Verify if the health check type is correctly set to **EC2 or ELB**. |

This ensures a **structured debugging process** for fixing **Auto Scaling Group (ASG) issues**. 🚀




A customer is getting ThrottlingException errors in API Gateway. What should they do?
--------------------------------------------------------------------------------------

# Debugging ThrottlingException Errors in API Gateway

| Step No | Checkpoint                                  | Action/Command |
|---------|--------------------------------------------|---------------|
| **1**   | **Check API Gateway Throttling Limits**    | Go to **API Gateway Console** → Select API → Check **Throttle settings**. |
| **2**   | **Check Usage Plans and Rate Limits**      | Ensure the API key is linked to the correct **Usage Plan** with adequate rate limits. |
| **3**   | **Increase Throttling Limits**            | `aws apigateway update-stage --rest-api-id <API_ID> --stage-name <STAGE_NAME> --patch-operations op='replace',path='/throttle/rateLimit',value='<NEW_LIMIT>'` |
| **4**   | **Check CloudWatch Logs for Rate Exceeded Errors** | `aws logs filter-log-events --log-group-name /aws/apigateway/<API_NAME>` |
| **5**   | **Enable API Caching**                    | Enable **caching** in API Gateway to reduce backend load. |
| **6**   | **Check Lambda/Backend Service Throttling** | If API calls a **Lambda function**, check its **concurrent execution limits**. |
| **7**   | **Use AWS WAF to Rate-Limit Requests**    | Implement AWS **WAF rate-based rules** to control abusive traffic. |
| **8**   | **Use API Gateway v2 (WebSocket/HTTP APIs)** | Consider migrating to **HTTP APIs** for better scalability and cost efficiency. |
| **9**   | **Implement Retry Logic in Clients**      | Modify API clients to use **exponential backoff** when handling **429 errors**. |
| **10**  | **Request a Service Quota Increase**      | `aws service-quotas request-service-quota-increase --service-code apigateway --quota-code L-<QUOTA_ID> --desired-value <NEW_LIMIT>` |


A VPC peering connection is established but instances cannot communicate. Why?
--------------------------------------------------------------------------------


# Debugging VPC Peering Connection Issues

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Check VPC Peering Connection Status**       | Ensure the peering connection is in **"Active"** state in the **VPC console**. |
| **2**   | **Verify Route Tables**                       | Add a route in both VPCs' route tables pointing to the peered VPC CIDR. |
| **3**   | **Check Security Groups**                     | Allow inbound and outbound traffic between **peered VPC CIDRs** in security groups. |
| **4**   | **Check Network ACLs**                        | Ensure Network ACLs **do not block traffic** between the two VPCs. |
| **5**   | **Verify CIDR Overlap**                       | VPCs must have **non-overlapping CIDR blocks** for peering to work. |
| **6**   | **Check DNS Resolution (for Private Hostnames)** | Enable **DNS resolution** using `Modify VPC Peering Connection` option. |
| **7**   | **Check Subnet Association with Route Table** | Ensure that the correct **route table** is associated with the subnets. |
| **8**   | **Check if Traffic is Routed via NAT Gateway** | NAT Gateways do **not** support VPC peering traffic. Use **direct routes** instead. |
| **9**   | **Check Instance-Level Firewalls**           | If using EC2-based firewalls (e.g., `iptables`), ensure they allow VPC peering traffic. |
| **10**  | **Test Connectivity Using Ping and Telnet**  | Run `ping <destination IP>` or `telnet <destination IP> <PORT>` to debug network reachability. |

This structured approach will help identify and fix **VPC Peering communication issues** efficiently. 🚀


 A customer’s ALB (Application Load Balancer) is not routing traffic correctly. How do you troubleshoot?
 ---------------------------------------------------------------------------------------------------------


# Debugging ALB Routing Issues

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Check ALB Status**                          | Ensure ALB is **active** in the AWS console under **EC2 > Load Balancers**. |
| **2**   | **Verify Target Group Health**                | `aws elbv2 describe-target-health --target-group-arn <TARGET_GROUP_ARN>` |
| **3**   | **Check Listener Rules**                      | Go to **ALB Console > Listeners** and ensure correct **rules** are set for forwarding. |
| **4**   | **Validate Security Groups**                  | Security groups must **allow inbound traffic** on ALB’s listener ports (e.g., 80, 443). |
| **5**   | **Check Subnet Association**                  | ALB should be in **at least two subnets** in different **Availability Zones**. |
| **6**   | **Verify Route 53 or DNS Configuration**      | If using a custom domain, check **Route 53 records** point to the correct ALB. |
| **7**   | **Test ALB Access from Browser or Curl**      | Run `curl -v http://<ALB-DNS-NAME>` to check if the ALB responds. |
| **8**   | **Check VPC and Subnet Routing**              | Ensure the ALB subnets are correctly configured with a **default route to the internet/NAT** if required. |
| **9**   | **Check IAM Permissions for ALB**             | If ALB uses AWS services like WAF or Cognito, verify IAM roles and permissions. |
| **10**  | **Review CloudWatch Logs for Errors**         | `aws logs describe-log-groups --log-group-name /aws/elasticloadbalancing/<ALB_NAME>` |

This structured approach helps systematically troubleshoot **ALB routing issues** efficiently. 🚀










