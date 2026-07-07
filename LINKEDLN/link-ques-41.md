
18. Tell all the scenarios too implement the security in Kubernetes.

# Kubernetes Security Best Practices

| **Category** | **Control** | **Best Practice** |
|---------------|-------------|-------------------|
| **Authentication & Authorization** | RBAC | Grant only required permissions (Least Privilege). |
| | Service Accounts | Use dedicated service accounts with minimal access. |
| | API Authentication | Enable certificate, OIDC, or OAuth authentication. |
| **Network Security** | Network Policies | Restrict Pod-to-Pod and service communication. |
| | Service Mesh (mTLS) | Encrypt service-to-service communication. |
| | Ingress/Egress Control | Allow only required inbound and outbound traffic. |
| **Secrets Management** | Kubernetes Secrets | Store passwords, tokens, and keys securely. |
| | External Secret Manager | Use Vault, AWS Secrets Manager, or Google Secret Manager. |
| | Encrypt Secrets | Enable etcd encryption for Secrets at rest. |
| **Container Security** | Image Scanning | Scan images regularly using Trivy, Clair, or Anchore. |
| | Image Signing | Verify trusted images using Cosign or Notary. |
| | Read-Only Filesystem | Run containers with a read-only root filesystem. |
| **Patch Management** | Security Patching | Apply Kubernetes and runtime security updates regularly. |
| | Version Management | Keep the cluster on the latest supported version. |
| | Security Audits | Perform regular security and compliance checks. |
| **Logging & Monitoring** | Centralized Logging | Collect cluster logs using ELK or Fluentd. |
| | Monitoring | Monitor metrics with Prometheus and Grafana. |
| | Alerting | Configure alerts for abnormal activity and failures. |
| **Cluster Security** | API Server Security | Restrict API access with RBAC, authentication, and IP allowlists. |
| | etcd Security | Encrypt etcd data and restrict access. |
| | Control Plane Security | Secure control plane communication using TLS certificates. |

## Quick Revision

| **Area** | **Remember** |
|----------|--------------|
| Authentication | RBAC + Service Accounts + API Authentication |
| Network | Network Policies + mTLS + Ingress/Egress Rules |
| Secrets | Kubernetes Secrets + External Secret Manager + Encryption |
| Containers | Scan + Sign + Read-Only Filesystem |
| Patching | Update + Upgrade + Audit |
| Monitoring | Logs + Metrics + Alerts |
| Cluster | Secure API Server + Encrypt etcd + Protect Control Plane |




19. Your EKS application is experiencing higher than expected traffic. How would you automatically scale the Pods?

Enable Horizontal Pod Autoscaler (HPA) in your EKS cluster to automatically scale the number of Pods based on CPU or memory usage.
Use metrics-server or Prometheus to gather resource metrics like CPU and memory for scaling decisions.
Define HPA using kubectl or YAML, specifying desired metrics (e.g., CPU > 80%) to trigger scaling up or down


20. Your team needs to be alerted when the CPU usage of any Pod in your EKS cluster exceeds 80% for more than 5 minutes. How would you set this up?

Use Amazon CloudWatch to collect Kubernetes metrics from your EKS cluster using the kube-state-metrics and cloudwatch-agent DaemonSet.
Create a CloudWatch alarm with a threshold of 80% CPU usage for more than 5 minutes for any pod.
Set up a CloudWatch alarm action to send notifications to an SNS topic, which will alert your team




21. Your team wants a Grafana dashboard to visualize the HTTP request latency of your applications running in EKS. How would you achieve this?

Set up Prometheus on your EKS cluster to scrape metrics from your applications using the Prometheus Operator or kube-prometheus.
Use Prometheus metrics like http_request_duration_seconds to collect HTTP request latency data.
Connect Grafana to Prometheus as a data source and create a dashboard to visualize the HTTP request latency metrics
