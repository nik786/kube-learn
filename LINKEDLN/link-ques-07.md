

Why might a Kubernetes service fail to resolve another service using DNS? ✅Check the CoreDNS status, verify the service name and namespace, ensure the correct DNS policy is set (ClusterFirst), and review any network policies or firewalls that might be blocking DNS traffic.

2️⃣What is an Error Budget, and how does it guide release decisions? ✅It’s the max allowable downtime or failure within an SLO. If you’ve used it up, no more risky deployments. It forces balance between velocity and reliability.

3️⃣How do you design a CI/CD pipeline for microservices? ✅Think loosely coupled: independent build, test, and deploy stages. Add canary deployments, automated rollbacks, and integration with observability tools.

4️⃣What are golden signals, and why are they important? ✅Latency, traffic, errors, saturation. These 4 metrics help you detect and debug issues quickly in distributed systems.

5️⃣How do you handle secrets in your CI/CD pipeline? ✅Never commit them. Use secret managers (Vault, AWS Secrets Manager, GitHub Encrypted Secrets) and inject them during runtime.

6️⃣What happens when you scale a StatefulSet in Kubernetes? ✅Unlike Deployments, each pod in a StatefulSet has a persistent identity. Scaling needs extra care with storage volumes and service endpoints.

7️⃣Can infrastructure be immutable and still be scalable? ✅Yes! That’s the whole point. Tools like Terraform + image baking (e.g., Packer) allow infra to scale via prebuilt artifacts, not patching live systems.

8️⃣What’s your approach to zero-downtime deployments? ✅Blue-green, canary, or rolling updates with health checks + circuit breakers. Add feature flags for extra control.

9️⃣What are some anti-patterns in monitoring and alerting? ✅Too many alerts, alerting on symptoms not causes, or missing business metrics entirely. Alert fatigue is real.

1️⃣0️⃣How do you troubleshoot a failed deployment fast? ✅Start from logs, then metrics, then traces. Use a structured observability stack like ELK, Prometheus + Grafana, or OpenTelemetry.
