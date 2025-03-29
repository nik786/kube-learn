

| Feature                          | Managed Node Group                        | Self-Managed Node Group                  |
|----------------------------------|-------------------------------------------|------------------------------------------|
| Upgrade specific node            | ❌ Not supported                           | ✅ Possible manually                      |
| Upgrade entire group (rolling)   | ✅ Supported via `eksctl`                  | ✅ Supported via ASG + Launch Template    |
| Auto rejoin after upgrade        | ✅ Yes                                     | ✅ With proper bootstrap script           |
| Node control granularity         | ❌ Group-based only                        | ✅ Per-node control                       |




# Troubleshooting Internal Server Error in Java Spring Boot Microservices on EKS

| **Step**                   | **Action**                                                                                                                                                                     | **Command/Details**                                                                                                                                                     |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Check Logs**             | Inspect logs for errors like stack traces, configuration issues, or resource connection failures.                                                                             | `kubectl logs <pod-name>`                                                                                                                                              |
| **Inspect Pod Status**     | Check if pods are in error states like `CrashLoopBackOff`.                                                                                                                    | `kubectl get pods -o wide`                                                                                                                                             |
| **Analyze Pod Events**     | Look for deployment issues or resource constraints in pod events.                                                                                                             | `kubectl describe pod <pod-name>`                                                                                                                                      |
| **Verify Environment Variables** | Ensure that required environment variables are correctly set for database connections, API keys, etc.                                                                     | Check `env` section in the Kubernetes Deployment YAML file.                                                                                                            |
| **Test Service Connectivity** | Verify if services and APIs are reachable from the pod.                                                                                                                     | `kubectl exec -it <pod-name> -- curl http://<service-name>:<port>`                                                                                                     |
| **Check DNS Resolution**   | Ensure DNS is resolving correctly for Kubernetes services.                                                                                                                    | `kubectl exec -it <pod-name> -- nslookup <service-name>`                                                                                                               |
| **Validate Probes**        | Ensure readiness and liveness probes are correctly configured and functional.                                                                                                 | Check the Deployment YAML for `readinessProbe` and `livenessProbe` configuration.                                                                                      |
| **Monitor Resource Usage** | Check if resource limits or requests are causing issues.                                                                                                                      | Use `kubectl top pod <pod-name>` to analyze CPU and memory usage.                                                                                                      |
| **Port Forwarding**        | Debug the application locally by forwarding the port.                                                                                                                         | `kubectl port-forward <pod-name> 8080:8080`                                                                                                                            |
| **Exec into Pod**          | Access the container shell to check configurations and logs directly.                                                                                                         | `kubectl exec -it <pod-name> -- /bin/bash`                                                                                                                             |
| **Check EKS Security**     | Validate that security groups, IAM roles, and network permissions are correctly set up.                                                                                       | Review EKS configuration in AWS Management Console or via CLI.                                                                                                        |
| **Inspect Ingress Rules**  | Verify ingress configurations and load balancer logs for any misconfigurations.                                                                                               | `kubectl describe ingress <ingress-name>`                                                                                                                              |
| **Database Connectivity**  | Ensure the database is accessible and connection pool settings are appropriate.                                                                                               | Check database logs and `application.properties`/`application.yml` for configuration.                                                                                 |
| **Redeploy Application**   | Restart the application after fixes to apply changes.                                                                                                                         | `kubectl rollout restart deployment <deployment-name>`                                                                                                                 |
| **Helm Debugging**         | Use Helm commands to debug if the application is deployed via Helm.                                                                                                           | `helm status <release-name>`                                                                                                                                           |
| **Cluster-Level Debugging**| Ensure all nodes in the EKS cluster are healthy and inspect node logs for issues.                                                                                              | `kubectl describe node <node-name>`                                                                                                                                    |
| **Resource Drift**         | Verify resource state in EKS matches the desired state defined in the configuration.                                                                                          | Check deployment YAML files and Terraform/Helm state if applicable.                                                                                                    |





21. Your team wants a Grafana dashboard to visualize the HTTP request latency of your applications running in EKS. How would you achieve this?

# Set Up Prometheus and Grafana on EKS

| **Step**                              | **Action**                                                                                                                                                                                             | **Command/Details**                                                                                                               |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Install Prometheus Operator**       | Deploy the Prometheus Operator to your EKS cluster to manage Prometheus resources such as scrapers and service monitors.                                                                                  | `kubectl create -f https://raw.githubusercontent.com/coreos/kube-prometheus/master/manifests/setup/prometheus-operator-setup.yaml` |
| **Install kube-prometheus**           | Install the `kube-prometheus` bundle, which includes Prometheus, Alertmanager, and Grafana, with configurations for monitoring Kubernetes clusters and applications.                                         | `kubectl create -f https://raw.githubusercontent.com/coreos/kube-prometheus/master/manifests/prometheus-operator.yaml`            |
| **Verify Prometheus Installation**    | Ensure that Prometheus and other components are successfully deployed to the cluster.                                                                                                                   | `kubectl get pods -n monitoring`                                                                                                 |
| **Configure Prometheus Scraping**     | Define which applications and metrics Prometheus should scrape. Use the `http_request_duration_seconds` metric to track HTTP request latency.                                                              | Update the `Prometheus` resource or `ServiceMonitor` to include scraping for the application metric `http_request_duration_seconds`.|
| **Example Prometheus Scrape Config**  | Update the `ServiceMonitor` to scrape the latency metric.                                                                                                                                               | Example YAML:
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: example-service-monitor
  labels:
    release: prometheus
spec:
  selector:
    matchLabels:
      app: example-app
  endpoints:
  - port: web
    path: /metrics
    interval: 30s

```



20. Your team needs to be alerted when the CPU usage of any Pod in your EKS cluster exceeds 80% for more than 5 minutes. How would you set this up?

# Set Up Amazon CloudWatch for Kubernetes Metrics in EKS

| **Step**                                | **Action**                                                                                                                                                                                                                                                                     | **Command/Details**                                                                                                         |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Install kube-state-metrics**          | Deploy the `kube-state-metrics` DaemonSet to gather Kubernetes resource metrics (like CPU and memory usage) for CloudWatch.                                                                                                                                                       | `kubectl apply -f https://github.com/kubernetes/kube-state-metrics/releases/latest/download/kube-state-metrics.yaml`        |
| **Install CloudWatch Agent**            | Deploy the `cloudwatch-agent` DaemonSet to collect and send metrics to CloudWatch.                                                                                                                                                                                                | Follow [CloudWatch agent installation steps](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-eks-install.html) for the CloudWatch Agent. |
| **Configure CloudWatch Agent**          | Configure the CloudWatch agent to collect Kubernetes metrics and log data.                                                                                                                                                                                                       | Create `cloudwatch-agent-config.json` for Kubernetes metrics and logs collection, then apply it with:                       |
|                                         |                                                                                                                                                                                                                                                                                 | `kubectl apply -f cloudwatch-agent-config.json`                                                                              |
| **Verify Metrics Collection**           | Verify that CloudWatch is receiving metrics from your EKS cluster after deploying the DaemonSets.                                                                                                                      | In CloudWatch Console, check the "Logs" and "Metrics" sections to ensure data is coming in from the `cloudwatch-agent`.     |
| **Create CloudWatch Alarm**             | Create a CloudWatch alarm to monitor CPU usage over 80% for more than 5 minutes for any pod in your cluster.                                                                                                            | Use CloudWatch Console or the AWS CLI to create an alarm with the following configuration:                                  |
| **CloudWatch Alarm Configuration**      | Set the alarm to trigger when CPU usage exceeds 80% for 5 minutes.                                                                                                                                                                                                             | `aws cloudwatch put-metric-alarm --alarm-name "High-CPU-Usage" --metric-name "CPUUtilization" --namespace "AWS/EC2" --statistic "Average" --period 300 --threshold 80 --comparison-operator "GreaterThanThreshold" --dimensions Name=ClusterName,Value=<ClusterName> --evaluation-periods 1 --alarm-actions <SNS-ARN>` |
| **Set Alarm Actions**                   | Configure the CloudWatch alarm action to send notifications to an SNS topic.                                                                                                                                                                                                  | In the alarm configuration, specify the SNS topic ARN in the `--alarm-actions` parameter. Use AWS SNS for notifications.      |
| **Create SNS Topic**                    | Create an SNS topic for alert notifications when the alarm is triggered.                                                                                                                                                                                                       | `aws sns create-topic --name "CPU-Alert-Topic"`                                                                             |
| **Subscribe to SNS Topic**              | Subscribe an email address (or other endpoint) to the SNS topic for receiving alerts.                                                                                                                                                                                           | `aws sns subscribe --topic-arn <SNS-Topic-ARN> --protocol email --notification-endpoint <your-email@example.com>`           |
| **Test the Alarm**                      | Trigger the alarm by artificially increasing CPU usage to over 80% for 5 minutes and verify that the SNS notifications are sent to the subscribed email.                                                                                                                       | Stress test the application to simulate high CPU usage or temporarily modify the CPU usage threshold for testing.           |
| **Monitor and Adjust**                  | Monitor the CloudWatch metrics and alarms to ensure proper configuration. Adjust the thresholds, notification settings, and other parameters as needed.                                                                                                                           | Use the CloudWatch Console or CLI to adjust alarm thresholds, actions, and monitoring parameters as needed.                  |



19. Your EKS application is experiencing higher than expected traffic. How would you automatically scale the Pods?
# Enable Horizontal Pod Autoscaler (HPA) in EKS

| **Step**                                | **Action**                                                                                                                                                          | **Command/Details**                                                                                                           |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Install Metrics Server**             | Install the Metrics Server in the EKS cluster to gather CPU and memory usage data for HPA.                                                                         | `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`                  |
| **Verify Metrics Server**              | Check if the Metrics Server is running correctly.                                                                                                                   | `kubectl get deployment metrics-server -n kube-system`                                                                         |
| **Install Prometheus (optional)**      | Install Prometheus if you want to gather more detailed metrics for scaling decisions.                                                                               | Use Helm or apply Prometheus YAML from [Prometheus Helm chart](https://github.com/prometheus-community/helm-charts).             |
| **Define HPA**                          | Create a Horizontal Pod Autoscaler (HPA) using either `kubectl` or a YAML file.                                                                                   | `kubectl autoscale deployment <deployment-name> --cpu-percent=80 --min=1 --max=10`                                            |
| **Define HPA using YAML**              | Define HPA with specific resource limits and scaling criteria (e.g., CPU > 80%).                                                                                   | Example YAML:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: <deployment-name>-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: <deployment-name>
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 80
```




