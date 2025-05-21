You’ve been asked to design a central identity solution for a multinational corporation using Azure and AWS. What approach would you take to unify authentication and RBAC across clouds?

2. A mission-critical cloud service needs to be patched without downtime. What’s your strategy for zero-downtime updates and patching?

   | Scenario                                    | Strategy / Action                          | Description                                                                                         | Example / Tools                                                                                     |
|---------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Zero-downtime updates and patching for mission-critical cloud service | Use blue-green or canary deployment       | Deploy new version alongside old, gradually shift traffic to new version, then retire old version | Kubernetes: Deploy new pods in separate deployment, use service selectors to switch traffic       |
|                                             | Load balancer traffic shifting             | Use load balancer to route traffic away from instances being patched                              | AWS ALB/ELB weighted routing or Azure Traffic Manager                                            |
|                                             | Rolling updates with health checks         | Update instances one by one, only mark ready when healthy                                        | Kubernetes rolling update strategy or AWS Auto Scaling group rolling updates                       |
|                                             | Use container orchestration                 | Orchestrators like Kubernetes handle pod replacement with zero downtime                          | `kubectl rollout restart deployment/myapp`                                                       |
|                                             | Automate rollback                            | Monitor metrics and automatically rollback if new version fails                                  | Use monitoring tools + pipeline logic (Jenkins, ArgoCD)                                           |
|                                             | Use maintenance windows with redundancy     | Patch subsets in staggered windows ensuring other instances handle traffic                        | Schedule patching in off-peak hours with redundancy                                               |


4. Your architecture is failing under unexpected load spikes despite autoscaling. What diagnostics and redesign options would you explore?

5. A financial client requires all logs and data events to be immutable and auditable. How would you implement this in a cloud-native way?

6. You’re working with a large media company needing low-latency content delivery worldwide. How do you architect a performant and scalable CDN-backed system?

7. You need to design a centralized backup and disaster recovery strategy for all production workloads across AWS and Azure. What’s your approach?

8. A client uses multiple cloud services across departments but lacks cost visibility. How would you help them gain granular cost insights and governance?

9. Your architecture must meet stringent SLA, RTO, and RPO requirements. How do you ensure compliance through architecture and tooling?

10. You are asked to build a multi-environment CI/CD solution that supports Terraform, Kubernetes, and serverless stacks. What’s your high-level design?

11. Your cloud architecture has become overly complex and hard to manage. How do you refactor or simplify it without service disruption?

12. Your application needs low latency for mobile users across continents, but backend processing must remain centralized. How would you architect this?

13. You’ve been asked to enforce tagging policies, naming standards, and budget controls across 50+ teams. What governance model would you use?

14. Your architecture uses managed databases, but regulatory pressure demands full control of backups and failover. How would you rearchitect?

15. A cloud-native microservices system suffers from noisy neighbor problems. How would you isolate and optimize resource consumption?

16. Your customer wants to implement multi-factor authentication (MFA) and conditional access policies across all cloud resources. What’s your implementation plan?

17. You are supporting a multi-tenant SaaS solution where one tenant’s workload is overwhelming shared services. How do you isolate and prioritize critical tenants?

18. You’re tasked with modernizing an ETL pipeline running on legacy servers. What cloud-native services would you propose for scalability and cost-efficiency?

19. You’re leading a cloud migration, but halfway through, a critical security misconfiguration is found. How do you mitigate the risk and regain stakeholder trust?

    # Cloud Migration Risk Mitigation Plan

| Step                        | Action                                                                                       | Purpose                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 1. Immediate Containment    | Isolate affected resources, revoke exposed credentials, and disable misconfigured services.  | Prevent further exploitation and contain the impact.                   |
| 2. Root Cause Analysis      | Conduct a rapid assessment using logs, security tools, and team input.                      | Understand what went wrong and how it occurred.                        |
| 3. Patch & Remediate        | Apply configuration fixes, update IAM policies, enable monitoring and alerts.               | Eliminate the vulnerability and harden defenses.                       |
| 4. Communicate Transparently| Inform stakeholders with facts, scope, mitigation steps, and timelines.                     | Maintain trust through accountability and clear communication.         |
| 5. Security Audit           | Engage a third-party audit or run internal compliance checks.                              | Ensure no residual misconfigurations remain.                          |
| 6. Improve Governance       | Implement automated security checks (e.g., Terraform policies, CI/CD gates).               | Prevent similar issues in future migrations.                          |
| 7. Document & Educate       | Update runbooks and train teams on security best practices and lessons learned.             | Institutionalize learning and build a security-first culture.         |

