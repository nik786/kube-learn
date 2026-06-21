
Azure DevOps / SRE Interview Quick Revision Guide
---------------------------------------------------
11. Jenkins Jobs Randomly Failing at Artifact Upload
    -------------------------------------------------

Memory Trick: DNPP
--------------------
```
D = Disk I/O
N = Network Bandwidth
P = Plugin Issues
P = Proxy / Timeout
Interview Answer

```

Interview Answer
------------------

| Area | Checks |
|--------|--------|
| **D = Disk** | - Check disk space on Jenkins agents.<br>- Verify disk I/O performance.<br>- Check filesystem health. |
| **N = Network** | - Verify network connectivity to the artifact repository.<br>- Check network latency and bandwidth. |
| **P = Plugin** | - Review Jenkins plugin versions.<br>- Check build logs for plugin-related errors. |
| **P = Proxy / Timeout** | - Validate proxy configurations.<br>- Review timeout settings.<br>- Implement retry mechanisms for transient failures. |
| **Repository Validation** | - Review artifact repository logs.<br>- Check Azure Blob Storage, Artifactory, or Nexus access logs. |

- **Repository Validation**
  - Review artifact repository logs.
  - Check Azure Blob Storage, Artifactory, or Nexus access logs.

## 12. Automated Rollback Strategy in Kubernetes

Memory Trick: PCHA

```text
P = Probes
C = Canary Deployment
H = Health Metrics
A = Auto Rollback
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **P = Probes** | - Configure readiness probes.<br>- Configure liveness probes.<br>- Detect unhealthy pods before routing traffic. |
| **C = Canary Deployment** | - Deploy new version gradually.<br>- Shift traffic incrementally.<br>- Validate stability before full rollout. |
| **H = Health Metrics** | - Monitor error rates.<br>- Monitor latency.<br>- Track application health indicators. |
| **A = Auto Rollback** | - Use Argo Rollouts or Flagger.<br>- Trigger rollback based on thresholds.<br>- Restore previous stable release automatically. |

---

## 13. Cost-Optimized Cloud Architecture for Nightly Reporting App

Memory Trick: FLAS

```text
F = Functions
L = Lifecycle Policy
A = Archive Storage
S = Spot Compute
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **F = Functions** | - Use Azure Functions or Container Apps Jobs.<br>- Schedule execution using timer triggers. |
| **L = Lifecycle Policy** | - Automate data movement between storage tiers.<br>- Reduce storage costs. |
| **A = Archive Storage** | - Move logs to Cool tier after 30 days.<br>- Move to Archive tier for long-term retention. |
| **S = Spot Compute** | - Use Spot VMs or ACI.<br>- Run workloads only when required. |

---

## 14. Zero-Downtime Database Migrations

Memory Trick: BFPD

```text
B = Backward Compatible
F = Feature Flags
P = Phased Rollout
D = Drop Later
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **B = Backward Compatible** | - Add new columns/tables first.<br>- Avoid breaking existing applications. |
| **F = Feature Flags** | - Enable new features gradually.<br>- Allow quick rollback. |
| **P = Phased Rollout** | - Deploy schema changes first.<br>- Upgrade applications incrementally. |
| **D = Drop Later** | - Remove legacy schema only after migration completion. |

---

## 15. Disaster Recovery for Stateful Applications

Memory Trick: BSRR

```text
B = Backup
S = Snapshot
R = Replication
R = Recovery Runbook
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **B = Backup** | - Schedule regular backups.<br>- Validate backup integrity. |
| **S = Snapshot** | - Take periodic volume snapshots.<br>- Enable point-in-time recovery. |
| **R = Replication** | - Replicate data across AZs or regions.<br>- Maintain secondary database replicas. |
| **R = Recovery Runbook** | - Document recovery steps.<br>- Perform DR drills regularly. |

---

## 16. Azure Function Throttling

Memory Trick: MSOT

```text
M = Monitor
S = Scale
O = Optimize
T = Tune
```

### Interview Answer

| Area | Checks |
|--------|--------|
| **M = Monitor** | - Review Azure Monitor metrics.<br>- Check Application Insights telemetry. |
| **S = Scale** | - Move to Premium Plan if needed.<br>- Increase capacity automatically. |
| **O = Optimize** | - Reduce execution duration.<br>- Optimize memory usage. |
| **T = Tune** | - Tune concurrency settings.<br>- Adjust batch sizes and triggers. |

---


