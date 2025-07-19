

# Kubernetes & SRE Interview Questions – Scenario-Based

| **#** | **Question** | **Answer** |
|------|--------------|------------|
| 1️⃣ | Why might a Kubernetes service fail to resolve another service using DNS? | Check the **CoreDNS** status, verify the **service name and namespace**, ensure **DNSPolicy is ClusterFirst**, and inspect **NetworkPolicies or firewalls** that may block DNS traffic. |
| 2️⃣ | What is an Error Budget, and how does it guide release decisions? | It’s the **maximum allowable downtime/failure** within an SLO. If the error budget is exhausted, **halt risky deployments**. It enforces a balance between **release velocity** and **system reliability**. |
| 3️⃣ | How do you design a CI/CD pipeline for microservices? | Design **loosely coupled pipelines** with independent build, test, and deploy stages. Include **canary deployments**, **automated rollbacks**, and **observability integration**. |
| 4️⃣ | What are golden signals, and why are they important? | The four golden signals: **Latency**, **Traffic**, **Errors**, **Saturation**. These metrics are key to **detecting and diagnosing issues** in distributed systems. |
| 5️⃣ | How do you handle secrets in your CI/CD pipeline? | **Never commit secrets**. Use secret managers like **Vault**, **AWS Secrets Manager**, or **GitHub Encrypted Secrets**, and inject secrets securely at **runtime**. |
| 6️⃣ | What happens when you scale a StatefulSet in Kubernetes? | Each pod has a **persistent identity** and **stable storage**. Scaling requires careful handling of **volume claims** and **headless service endpoints**. |
| 7️⃣ | Can infrastructure be immutable and still be scalable? | ✅Yes. Use tools like **Terraform** with **image baking tools (e.g., Packer)** to scale using **prebuilt artifacts**, avoiding in-place modifications. |
| 8️⃣ | What’s your approach to zero-downtime deployments? | Use **blue-green**, **canary**, or **rolling updates** with proper **health checks** and **circuit breakers**. **Feature flags** help fine-tune control. |
| 9️⃣ | What are some anti-patterns in monitoring and alerting? | Examples include **too many alerts**, alerting only on **symptoms not root causes**, and ignoring **business metrics**. Avoid **alert fatigue** by tuning thresholds. |
| 🔟 | How do you troubleshoot a failed deployment fast? | Start with **logs**, then check **metrics**, then analyze **traces**. Use tools like **ELK**, **Prometheus + Grafana**, or **OpenTelemetry** for a structured observability approach. |
