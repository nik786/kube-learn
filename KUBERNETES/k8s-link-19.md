
 7. What steps would you take to optimize the performance of a cloud-based application that is experiencing latency issues?

| Step  | Action                          | What to Do                                                                              |
| ----- | ------------------------------- | --------------------------------------------------------------------------------------- |
| **C** | **Check Monitoring & Logs**     | Use CloudWatch, Datadog, or Prometheus to identify the source of latency.               |
| **A** | **Add Caching**                 | Implement Redis, CDN, or application-level caching to reduce repeated requests.         |
| **C** | **Compute Optimization**        | Right-size instances, optimize CPU/memory usage, and enable auto scaling.               |
| **H** | **Handle Database Bottlenecks** | Optimize queries, add indexes, and use read replicas when needed.                       |
| **E** | **Enhance Network Performance** | Use load balancers, CDNs, connection pooling, and minimize network hops.                |
| **R** | **Review Application Code**     | Profile the application, identify slow APIs/functions, and eliminate inefficient logic. |
| **S** | **Stress Test & Scale**         | Perform load testing to validate improvements and adjust scaling policies proactively.  |


Easy way to remember: CACHERS
-------------------------------

C → Check Monitoring & Logs
A → Add Caching
C → Compute Optimization
H → Handle Database Bottlenecks
E → Enhance Network Performance
R → Review Application Code
S → Stress Test & Scale



Networking Troubleshooting:
----------------------------

A cloud-based application is facing intermittent connectivity issues. How would you diagnose and resolve these networking problems?

| Step  | Action                           | What to Do                                                                                                     |
| ----- | -------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **T** | **Track the Issue**              | Review CloudWatch, VPC Flow Logs, and application logs to identify when and where connectivity failures occur. |
| **R** | **Review Network Configuration** | Verify Security Groups, NACLs, Route Tables, DNS settings, and firewall rules for misconfigurations.           |
| **A** | **Analyze Connectivity Paths**   | Use tools like `ping`, `traceroute`, `telnet`, `curl`, and `nslookup` to isolate the failing network segment.  |
| **C** | **Check Infrastructure Health**  | Inspect Load Balancers, VPNs, NAT Gateways, Transit Gateways, and instance health for faults.                  |
| **E** | **Eliminate & Resolve**          | Apply fixes, validate the solution through testing, and implement monitoring/alerts to prevent recurrence.     |



Cost Optimization:
------------------

How would you identify areas of unnecessary cloud spending, and what strategies would you use to optimize costs without sacrificing performance?   

| Step  | Action                                | What to Do                                                                                          |
| ----- | ------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **S** | **Study Cost Reports**                | Use Cost Explorer, AWS Budgets, or Azure Cost Management to identify spending trends and anomalies. |
| **M** | **Match Resources to Demand**         | Right-size underutilized instances, storage, and databases based on actual usage.                   |
| **A** | **Automate Savings**                  | Schedule non-production resources to shut down and enable auto scaling for dynamic workloads.       |
| **R** | **Reserve for Predictable Workloads** | Use Reserved Instances, Savings Plans, or committed-use discounts for steady-state applications.    |
| **T** | **Track and Govern**                  | Implement tagging, budgets, and cost alerts to continuously monitor and control spending.           |


Easy way to remember: SMART
----------------------------

S → Study Cost Reports
M → Match Resources to Demand
A → Automate Savings
R → Reserve for Predictable Workloads
T → Track and Govern





