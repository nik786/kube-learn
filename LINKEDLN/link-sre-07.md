

You have a web application running on an EC2 instance behind an Application Load Balancer (ALB). You notice that the real client IP addresses are not appearing in your application logs — instead, you only see the ALB IP.
Question:
 How would you configure the application or environment to log the actual client IP addresses?

 | Step                                                 | Description                                                                 |
|------------------------------------------------------|-----------------------------------------------------------------------------|
| Enable and Parse the `X-Forwarded-For` Header         | ALB includes the original client IP in the `X-Forwarded-For` HTTP header — configure your application to log this value. |
| Update Web Server Config (e.g., Nginx, Apache)        | Modify logging format to include `X-Forwarded-For` (e.g., `$http_x_forwarded_for` in Nginx). |
| Disable Proxy Protocol (if Not Needed)                | ALB does not support Proxy Protocol — ensure your app isn’t expecting it, or traffic will be misinterpreted. |
| Adjust App-Level Logging Middleware                   | In frameworks (e.g., Express, Django), use middleware to extract and log `X-Forwarded-For`. |
| Secure Header Trust Only from ALB                     | Use security groups or reverse proxy trust settings to only accept `X-Forwarded-For` from ALB to avoid spoofing. |


 You have an EC2 instance that is part of an Auto Scaling group, but you notice that the instance is frequently marked unhealthy and terminated by the ASG.
Question:
 What could be causing this, and how would you troubleshoot and fix it?

 | Possible Cause                                 | Troubleshooting & Fix Strategy                                              |
|------------------------------------------------|-----------------------------------------------------------------------------|
| Failing Health Checks (ELB or EC2)             | Check ALB/ELB health check target group status and EC2 system logs. Adjust health check thresholds or paths as needed. |
| Application Startup Fails or Delays            | Verify user data scripts, startup logs (`/var/log/cloud-init.log`), and service availability post-boot. |
| Incorrect or Missing IAM Permissions           | Ensure instance role has necessary permissions for logging, metrics, or service discovery. |
| Resource Constraints (CPU, Memory, Disk)       | Monitor CloudWatch metrics for spikes or failures due to resource exhaustion. Tune instance type or app config. |
| ASG Lifecycle Hooks or Custom Scripts Failing  | Check if lifecycle hooks (e.g., warm-up scripts) are failing and causing instance replacement. |

