
7️⃣Can infrastructure be immutable and still be scalable?

✅Yes! That’s the whole point. Tools like Terraform + image baking (e.g., Packer) allow infra to scale via prebuilt artifacts, not patching live systems.

8️⃣What’s your approach to zero-downtime deployments?

✅Blue-green, canary, or rolling updates with health checks + circuit breakers. Add feature flags for extra control.

9️⃣What are some anti-patterns in monitoring and alerting?

✅Too many alerts, alerting on symptoms not causes, or missing business metrics entirely. Alert fatigue is real.

1️⃣0️⃣How do you troubleshoot a failed deployment fast?

✅Start from logs, then metrics, then traces. Use a structured observability stack like ELK, Prometheus + Grafana, or OpenTelemetry.
