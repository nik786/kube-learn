
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


| Step | Check | Quick Reminder |
|------|-------|----------------|
| 1 | Config Enabled | Verify AWS Config is enabled. |
| 2 | Recorder | Check Configuration Recorder is running. |
| 3 | Recording Rules | Ensure required resources are being tracked. |
| 4 | IAM | Verify AWS Config role permissions. |
| 5 | Delivery Channel | Check S3 bucket and SNS configuration. |
| 6 | Rules Status | Ensure Config Rules are active and compliant. |
| 7 | Logs | Review CloudWatch Logs for errors. |


Easy Interview Sequence

Enabled → Recorder → Rules → IAM → Delivery → Rules Status → Logs

Or remember:

"ERRIDRL"

E = Enabled
R = Recorder
R = Recording Rules
I = IAM
D = Delivery Channel
R = Rules Status
L = Logs

A simple interview answer:

"I would first check whether AWS Config is enabled, verify the recorder and recording rules, 
validate IAM permissions, check the delivery channel (S3/SNS), 
review Config rule status, and finally inspect CloudWatch Logs for errors."




  ```sh
  aws configservice stop-configuration-recorder --configuration-recorder-name default
  aws configservice start-configuration-recorder --configuration-recorder-name default

```


A customer’s ELB is marked as unhealthy for all targets. What do you check?


# ELB Marked as Unhealthy for All Targets – Troubleshooting Guide

| Step | Check | Quick Reminder |
|------|-------|----------------|
| 1 | Target Health | Check target group health status. |
| 2 | Health Check | Verify path, port, and protocol. |
| 3 | Security Groups | Allow ELB traffic to instances. |
| 4 | Network Routing | Check subnet, routes, and reachability. |
| 5 | Application Port | Ensure application is running and listening. |
| 6 | Listener Rules | Verify ELB listener forwards traffic correctly. |
| 7 | Logs | Check application and ELB access logs. |



Easy Interview Sequence

Health → Check → SG → Network → App → Listener → Logs

Or remember:

"HCSNALL"

H = Target Health
C = Health Check
S = Security Groups
N = Network Routing
A = Application
L = Listener Rules
L = Logs

A concise interview answer:

I would first check target health, validate health check settings, verify security groups and network routing, 
ensure the application is listening on the correct port, confirm listener rules, and review logs for detailed errors.





  ```sh
  netstat -tulnp | grep LISTEN
  curl -v http://localhost:<PORT>
```



