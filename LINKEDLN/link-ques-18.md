

## 17. Blue-Green Deployment with Rollback

Memory Trick: DVSR

```text
D = Deploy
V = Validate
S = Switch
R = Rollback
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **D = Deploy** | - Deploy application to Green environment.<br>- Keep Blue environment active. |
| **V = Validate** | - Run health checks.<br>- Validate performance metrics. |
| **S = Switch** | - Route traffic using Front Door or Application Gateway.<br>- Monitor user impact. |
| **R = Rollback** | - Redirect traffic back to Blue environment instantly if required. |

---

## 18. End-to-End SLA Monitoring

Memory Trick: STMA

```text
S = Synthetic Monitoring
T = Tracing
M = Metrics
A = Alerts
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **S = Synthetic Monitoring** | - Execute health checks periodically.<br>- Simulate user transactions. |
| **T = Tracing** | - Use OpenTelemetry.<br>- Track requests across services. |
| **M = Metrics** | - Monitor latency, throughput, and availability.<br>- Visualize using Grafana. |
| **A = Alerts** | - Configure alerts for SLO breaches.<br>- Notify support teams proactively. |

---

## 19. Compute-Intensive vs I/O-Intensive Scaling

Memory Trick: CPU vs DATA

```text
CPU = Compute Workloads
DATA = I/O Workloads
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **CPU = Compute Workloads** | - Scale using CPU and memory metrics.<br>- Use HPA and VM Scale Sets. |
| **DATA = I/O Workloads** | - Optimize storage throughput.<br>- Use caching, queues, and asynchronous processing. |

---

## 20. Production Pipeline Blocked Due to Missing Approvals

Memory Trick: ENBD

```text
E = Escalate
N = Notify
B = Break-Glass
D = Document
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **E = Escalate** | - Contact managers and stakeholders.<br>- Follow on-call escalation procedures. |
| **N = Notify** | - Send notifications via Teams, Slack, or PagerDuty. |
| **B = Break-Glass** | - Use emergency access only if approved.<br>- Follow compliance requirements. |
| **D = Document** | - Record actions taken.<br>- Include decisions in post-incident review. |
