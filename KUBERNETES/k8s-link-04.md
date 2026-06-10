
1. Kubernetes Incident Management:
   
   Imagine you’re managing a production Kubernetes cluster and one of your critical services suddenly becomes unresponsive.

   What steps would you take to diagnose and resolve the issue?

| Step | Action | Purpose |
|------|--------|---------|
| 1 | Check Pod Status (`kubectl get pods -A`) | Identify pods that are in `CrashLoopBackOff`, `Pending`, `Error`, or `Terminating` states. |
| 2 | Review Logs (`kubectl logs <pod-name>`) | Analyze application logs for exceptions, crashes, connectivity issues, or resource-related errors. |
| 3 | Inspect Events (`kubectl describe pod <pod-name>`) | Check Kubernetes events for scheduling failures, image pull errors, OOMKills, or readiness/liveness probe failures. |
| 4 | Verify Service & Networking (`kubectl get svc`, `kubectl get endpoints`) | Ensure the service is correctly routing traffic and endpoints are healthy and registered. |
| 5 | Check Resource Utilization (`kubectl top pods`, `kubectl top nodes`) | Identify CPU, memory, or node resource exhaustion that may impact application performance. |
| 6 | Implement Fix & Validate | Apply the necessary fix (restart pod, scale deployment, rollback release, update configuration) and verify service health through monitoring and user testing. |
 
 3. Handling Traffic Spikes:

    How would you design a system in a cloud environment to handle sudden traffic spikes in a microservices architecture?
    
| Step | Design Principle | Purpose |
|------|------------------|---------|
| 1 | Use Load Balancers | Distribute incoming traffic evenly across multiple service instances to prevent overload. |
| 2 | Enable Auto Scaling | Automatically scale pods (HPA/KEDA) and nodes (Cluster Autoscaler/Karpenter) based on CPU, memory, or custom metrics. |
| 3 | Implement Caching | Use Redis/CloudFront/CDN to reduce backend load and improve response times for frequently accessed data. |
| 4 | Use Message Queues | Buffer traffic spikes with SQS, Kafka, or RabbitMQ to decouple services and handle requests asynchronously. |
| 5 | Design for Resilience | Apply circuit breakers, retries, rate limiting, and timeouts to prevent cascading failures. |
| 6 | Monitor & Optimize | Use Prometheus, Grafana, and cloud monitoring tools to detect spikes, scale proactively, and maintain service health. |

Easy Interview Mnemonic: L-A-C-Q-R-M

L → Load Balancer
A → Auto Scaling
C → Caching
Q → Queueing
R → Resilience
M → Monitoring

Just remember:

"LACQRM handles traffic storms."




 5. CI/CD Pipeline Troubleshooting:

    During a deployment, your CI/CD pipeline fails unexpectedly. What would be your approach to troubleshoot and fix the problem?
 
 7. Infrastructure as Code (IaC):

    Describe how you manage infrastructure changes using tools like Terraform or CloudFormation. What challenges have you encountered?

 8. Disaster Recovery Strategy:

    What disaster recovery strategies would you implement in a cloud environment to ensure high availability for critical services?

 10. Monitoring and Observability:
   
   How would you set up monitoring for a multi-region application? Which tools and metrics would you prioritize to ensure system health?


