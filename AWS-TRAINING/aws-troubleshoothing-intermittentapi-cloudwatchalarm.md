A customer reports intermittent 5XX errors from their API Gateway. How do you debug?

# Debugging Intermittent 5XX Errors in API Gateway

| Step No | Checkpoint                                      | Action/Command |
|---------|------------------------------------------------|---------------|
| **1**   | **Check API Gateway Logs (CloudWatch)**       | Run `aws logs tail /aws/apigateway/YOUR-API-NAME --follow` to check for error messages. |
| **2**   | **Verify Backend Health**                     | If using AWS Lambda, check CloudWatch logs for failures. If using an HTTP backend, ensure it's reachable. |
| **3**   | **Inspect API Gateway Execution Logs**        | Enable execution logs in **API Gateway > Stages > Logs/Tracing** and check CloudWatch. |
| **4**   | **Check Latency Issues**                      | Run `aws apigateway get-metrics --metric-name IntegrationLatency` to check if high latency is causing timeouts. |
| **5**   | **Review Throttling & Rate Limits**           | Verify if requests exceed API Gateway limits using `aws apigateway get-usage-plan`. |
| **6**   | **Test Backend Endpoint Directly**           | Use `curl -v <backend-url>` or `Postman` to check if the backend returns **5XX errors** independently. |
| **7**   | **Check API Gateway Integration Settings**    | Ensure the integration type (`AWS_PROXY`, `HTTP`, `MOCK`) is correct and properly configured. |
| **8**   | **Validate IAM Permissions (If Using AWS Services)** | Ensure API Gateway's IAM role has the correct permissions to invoke backend services. |
| **9**   | **Check for Recent Deployments or Changes**   | If the issue started after a deployment, rollback to a previous stable version. |
| **10**  | **Enable X-Ray Tracing**                      | In **API Gateway > Stages > Enable X-Ray**, analyze request flow to identify bottlenecks. |

This structured guide helps systematically debug **intermittent 5XX errors in API Gateway** efficiently. 🚀


A CloudWatch alarm is not triggering as expected. What steps do you take?



# Debugging a CloudWatch Alarm That Is Not Triggering

| Step No | Checkpoint                                     | Action/Command |
|---------|-----------------------------------------------|---------------|
| **1**   | **Verify the Alarm State**                   | Check the alarm status in **CloudWatch > Alarms** to see if it is in `ALARM`, `OK`, or `INSUFFICIENT_DATA`. |
| **2**   | **Check the Metric Data**                    | Go to **CloudWatch > Metrics**, select the metric, and verify if it is reporting data correctly. |
| **3**   | **Ensure the Threshold is Correct**          | Confirm that the alarm threshold matches the expected value range. |
| **4**   | **Check the Evaluation Period**              | If the evaluation period is long, the alarm might take time to trigger. Reduce the period if needed. |
| **5**   | **Verify Alarm Conditions**                  | Ensure the condition (`GreaterThanThreshold`, `LessThanThreshold`, `GreaterThanOrEqualToThreshold`) is set correctly. |
| **6**   | **Inspect Data Gaps**                        | If no data is reported, the alarm won't trigger. Check for missing metric data in CloudWatch. |
| **7**   | **Check for Missing Permissions**            | If using SNS notifications, ensure the alarm has permissions to publish to the SNS topic. |
| **8**   | **Test SNS Notification (If Configured)**    | Manually publish a message to the SNS topic using: `aws sns publish --topic-arn <sns-topic-arn> --message "Test Message"` |
| **9**   | **Check for Alarm Suppression**              | If the alarm is part of an AWS Auto Scaling policy, ensure no cooldown periods or policies are preventing it from triggering. |
| **10**  | **Manually Trigger the Alarm for Testing**   | Temporarily lower the threshold or create a test alarm to confirm if it triggers. |

This step-by-step guide ensures a structured approach to troubleshooting **CloudWatch alarms not triggering**. 🚀
