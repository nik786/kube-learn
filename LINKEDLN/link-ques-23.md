

| Question | Key Areas | Interview Answer |
|----------|-----------|------------------|
| **Describe a time you optimized a DevOps pipeline for a complex application.** | MSCSD | - Broke monolithic pipelines into smaller services.<br>- Enabled parallel test execution.<br>- Containerized workloads using Docker and Kubernetes.<br>- Added security scanning early in the pipeline.<br>- Implemented canary deployment strategies. |
| **How would you reduce downtime during monthly patching activities?** | DKIVH | - Use rolling updates or blue-green deployments.<br>- Drain Kubernetes nodes before patching.<br>- Use pre-baked AMIs or VM images.<br>- Validate changes in staging first.<br>- Perform automated health checks after patching. |
| **Why is close monitoring important, and what tools do you use?** | APMRA | - Detect issues before users are impacted.<br>- Monitor availability and performance metrics.<br>- Reduce MTTR through proactive alerting.<br>- Support troubleshooting and root cause analysis.<br>- Use Prometheus, Grafana, CloudWatch, Azure Monitor, ELK, Datadog, and Alertmanager. |
| **Describe a security incident you have handled.** | DCRAP | - Detected exposed credentials in CI/CD logs.<br>- Revoked and rotated affected secrets immediately.<br>- Audited access and IAM permissions.<br>- Implemented secret scanning tools.<br>- Improved secure secret management practices. |
| **What compliance standards are you familiar with?** | GASAM | - Worked with GDPR, HIPAA, SOC 2, ISO 27001, and PCI-DSS requirements.<br>- Implemented compliance controls using AWS Config and Azure Policy.<br>- Enabled CloudTrail and Azure Activity Logs.<br>- Integrated SIEM platforms for auditing.<br>- Automated compliance monitoring and reporting. |


MSCSD
M = Microservices
S = Security
C = Containers
S = Speed (Parallel Tests)
D = Deployment Strategy

DKIVH
D = Deployment Strategy
K = Kubernetes
I = Images
V = Validation
H = Health Checks

APMRA
A = Availability
P = Performance
M = Monitoring
R = RCA
A = Alerting

DCRAP
D = Detection
C = Containment
R = Remediation
A = Auditing
P = Prevention

GASAM
G = Governance
A = Auditing
S = Security Controls
A = Automation
M = Monitoring
