13. A global application needs traffic routed based on user location. Which DNS or load balancing solutions would you use?

| Solution | Description |
|----------|-------------|
| 1. **AWS Route 53 with Latency-Based or GeoDNS Routing** | Routes users to the region with the lowest latency or based on geographic location using Route 53 routing policies. |
| 2. **Cloudflare Load Balancing with Geo Steering** | Uses Cloudflare's global edge network to direct users to the nearest healthy origin server with geographic steering and failover. |
| 3. **Google Cloud Load Balancer (GCLB)** | Automatically routes traffic to the closest backend service across regions using Anycast IP and global health checks. |
| 4. **Azure Front Door** | Provides global HTTP/HTTPS routing with latency-based traffic distribution and Web Application Firewall (WAF) integration. |
| 5. **NS1 or Akamai Global Traffic Management** | Offers advanced DNS routing and traffic management capabilities with real-time monitoring and fine-grained geolocation rules. |


15. Your API Gateway is not forwarding requests to backend services correctly. What troubleshooting steps do you follow?

16. A DNS lookup takes too long, impacting API response times. What optimizations can you apply?


Security & Firewalls

16. Your Kubernetes cluster is being targeted by DDoS attacks. What security measures can you implement?

| Step | Description |
|------|-------------|
| 1. **Use Cloud Provider DDoS Protection Services** | Enable services like AWS Shield, Azure DDoS Protection, or GCP Cloud Armor to absorb and mitigate volumetric attacks. |
| 2. **Implement Web Application Firewall (WAF)** | Deploy WAFs (e.g., AWS WAF, Cloudflare, ModSecurity) to filter malicious traffic before it reaches your cluster. |
| 3. **Rate Limit and Throttle Ingress Traffic** | Configure rate limiting on ingress controllers (e.g., NGINX, Istio) to block or slow down abusive IPs or requests. |
| 4. **Use Network Policies and Firewalls** | Apply `NetworkPolicy` to restrict internal traffic and cloud firewalls to block suspicious IP ranges or ports at the edge. |
| 5. **Auto-Scale and Isolate Public-Facing Services** | Use Horizontal Pod Autoscaler and node autoscaling to absorb burst load, and isolate ingress components in dedicated nodes or namespaces. |


18. A DevOps team member cannot SSH into a production server, but the credentials are correct. What could be blocking access?

19. A new cloud-based service is unable to access an on-premises database. How would you diagnose firewall and VPN settings?

| Step | Description |
|------|-------------|
| 1. **Verify VPN Tunnel Status and Routing Tables** | Check if the site-to-site VPN is up and properly routing traffic between the cloud VPC and on-prem network (e.g., AWS VPN metrics or BGP routes). |
| 2. **Test Connectivity with Tools like `telnet`, `nc`, or `traceroute`** | Run network tests from the cloud instance or pod to confirm reachability to the on-prem database IP and port. |
| 3. **Check On-Prem Firewall Rules** | Ensure the firewall allows inbound traffic from the cloud’s IP range to the database port (e.g., TCP 5432 for PostgreSQL). |
| 4. **Validate Security Group and NACL Configurations in Cloud** | Review VPC security groups and network ACLs to allow outbound traffic from cloud workloads to the on-prem target. |
| 5. **Inspect DNS Resolution and NAT Rules** | Confirm that the cloud service resolves the database hostname correctly and that no NAT rules are interfering with the return traffic path. |


20. Your security team asks you to restrict access to a web application based on IP ranges. How do you implement this in AWS, Azure, or GCP?

21. You suspect that an attacker is trying to scan your cloud environment. How do you detect and prevent such activity?

| Step | Description |
|------|-------------|
| 1. **Enable VPC Flow Logs and Network Monitoring** | Capture and analyze VPC traffic using AWS VPC Flow Logs, GCP VPC Flow Logs, or Azure NSG Flow Logs to detect port scanning or unusual access patterns. |
| 2. **Set Up Intrusion Detection Systems (IDS)** | Deploy tools like AWS GuardDuty, Suricata, or Zeek to detect reconnaissance behavior such as port scans, brute force attempts, or anomalies. |
| 3. **Use WAFs and Rate Limiting** | Implement Web Application Firewalls (e.g., AWS WAF, Cloudflare WAF) and configure rate limits to block IPs exhibiting scanning behavior. |
| 4. **Alert on Suspicious Behavior via SIEM** | Aggregate logs into a SIEM (e.g., Splunk, ELK, or AWS Security Hub) and create alerts for scanning signatures or failed login spikes. |
| 5. **Restrict Access with Security Groups and Firewalls** | Apply least privilege rules in Security Groups, NSGs, or firewall policies to limit exposure of services and block unnecessary ports. |
