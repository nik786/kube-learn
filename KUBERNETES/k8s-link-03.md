




57. You need to implement blue/green or canary deployments. How would you set that up using Kubernetes-native tools?


58. One of your worker nodes has disk pressure and is evicting pods. What’s your response and long-term fix?


59. Your logs show high CPU usage but metrics don’t reflect it. How do you correlate and analyze this discrepancy?


60. A Helm upgrade failed halfway. How do you recover and ensure consistency in the cluster?


61. You’ve been asked to create a multi-region active-active Kubernetes setup. What design principles and tools would you use?


62. How would you use Karpenter (or Cluster Autoscaler) to optimize workload placement dynamically?


63. Your CI/CD pipeline is deploying to the wrong namespace intermittently. How do you debug and prevent this?


64. A developer reports their pod is in CrashLoopBackOff. Walk them through the resolution process.


65. How do you implement pod disruption budgets to ensure availability during node maintenance?


66. You notice API server response times are increasing. How would you diagnose and tune it?


67. You've been tasked with hardening a Kubernetes cluster for financial data workloads. What's your plan?


68. There’s an unexpected increase in failed jobs. What monitoring and recovery mechanisms would you introduce?


# Monitoring and Recovery Mechanisms for Increased Failed Jobs

| Area | Monitoring Mechanism | Recovery Mechanism | Benefit | Example Tools |
|---|---|---|---|---|
| Job Failure Tracking | Monitor failed job count, exit codes, and retry metrics | Configure automatic retries with backoff strategy | Reduces transient failure impact | Prometheus, Grafana, Kubernetes Jobs |
| Alerting | Create real-time alerts for abnormal job failure spikes | Notify SRE/DevOps teams through PagerDuty/Slack | Faster incident response | Alertmanager, PagerDuty, Slack |
| Log Monitoring | Centralize and analyze application/job logs | Enable automated log-based troubleshooting workflows | Speeds up root cause analysis | ELK Stack, Loki, CloudWatch |
| Resource Monitoring | Monitor CPU, memory, disk, queue length, and DB connections | Enable autoscaling and resource optimization | Prevents failures caused by resource exhaustion | HPA, KEDA, Datadog |
| Self-Healing | Detect unhealthy pods/nodes/services continuously | Restart failed jobs/pods automatically using orchestration | Improves system availability and resiliency | Kubernetes, Argo Workflows, ECS |






69. How would you ensure cost optimization in a large-scale Kubernetes environment?


70. What tools and practices would you use to benchmark application performance within the cluster?
