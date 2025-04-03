
# Troubleshooting ECS Tasks Failing

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Check Task Logs**                            | Use **CloudWatch Logs** or `aws ecs describe-tasks` to view logs for failures. |
| **2**   | **Verify Container Exit Codes**                | Run `aws ecs describe-tasks --cluster <cluster-name> --tasks <task-id>` and check the `exitCode`. |
| **3**   | **Check Task Definitions**                     | Ensure correct image, CPU, memory limits, and essential containers are defined properly. |
| **4**   | **Inspect IAM Permissions**                    | Verify that the **ECS task role** has permissions for AWS services it interacts with. |
| **5**   | **Check for Port Conflicts**                   | Ensure that no conflicting ports are used in the task definition (especially for host mode). |
| **6**   | **Verify Networking Configuration**            | Ensure tasks are in the correct VPC/subnets and security groups allow inbound/outbound traffic. |
| **7**   | **Examine Load Balancer Health Checks**        | If using an ALB/NLB, check **target group health checks** under **EC2 > Target Groups**. |
| **8**   | **Check Service Auto Scaling Limits**          | If using ECS Service Auto Scaling, verify that the service has available capacity to launch tasks. |
| **9**   | **Look for Resource Constraints**              | If running on EC2 mode, check instance

