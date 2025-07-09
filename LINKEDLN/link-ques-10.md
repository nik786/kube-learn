

1. Your application is experiencing intermittent connectivity issues with an external API. How do you troubleshoot and resolve this?

| Step | Description |
|------|-------------|
| 1. **Log and Correlate Failures** | Enable detailed logging of external API calls (status codes, timeouts, error messages) to identify patterns or failure windows. |
| 2. **Add Retry Logic with Backoff** | Implement exponential backoff and circuit breaker patterns in your application to handle transient API failures gracefully. |
| 3. **Monitor DNS Resolution and Latency** | Use tools like `dig`, `nslookup`, or Prometheus Blackbox Exporter to check for DNS flaps or variable response times. |
| 4. **Check Outbound Network Path** | Use `traceroute`, `curl`, or cloud VPC flow logs to inspect packet routes, latency, and possible egress firewall/NAT issues. |
| 5. **Coordinate with API Provider** | Contact the external API provider for service status, rate limits, or planned maintenance that might affect availability. |


3. A new service deployed in Kubernetes cannot communicate with a backend database. What steps would you take to diagnose the issue?

4. You notice high latency when accessing a cloud-based application. What factors could be contributing, and how would you mitigate them?

| Factor | Mitigation Strategy |
|--------|----------------------|
| 1. **Geographic Distance from Users** | Use a CDN (e.g., Cloudflare, AWS CloudFront) or deploy application replicas in multiple regions to serve users closer to their location. |
| 2. **Unoptimized Application Code or DB Queries** | Profile and optimize slow endpoints, SQL queries, and reduce synchronous dependencies using caching and async processing. |
| 3. **Network Bottlenecks or Throttling** | Monitor network traffic (e.g., using VPC Flow Logs), scale up network interfaces, or upgrade to higher-bandwidth instances. |
| 4. **Resource Contention on Cloud Instances** | Monitor CPU, memory, and disk IO; scale vertically or horizontally, and use dedicated instances to avoid noisy neighbors. |
| 5. **Inefficient Load Balancer Configuration** | Ensure load balancer health checks are properly tuned, connection reuse is enabled, and routing policies reduce cross-zone traffic. |


5. Your team reports frequent SSH connection timeouts when accessing production servers. How would you debug this issue?

| Step | Description |
|------|-------------|
| 1. **Check Network Reachability and Latency** | Use `ping`, `traceroute`, or `mtr` from client machines to verify packet loss, latency, or routing issues to the server IP. |
| 2. **Inspect Server-Side SSH Logs** | Review `/var/log/auth.log` or `/var/log/secure` on the server for authentication errors, dropped connections, or rate limits. |
| 3. **Verify Firewall and Security Group Rules** | Ensure port 22 is open and not being throttled or blocked by security groups, NACLs, or host firewalls (e.g., iptables, ufw). |
| 4. **Monitor Server Load and Resource Usage** | Check CPU, memory, and network load (`top`, `vmstat`, `netstat`) to ensure the server isn’t overwhelmed and dropping connections. |
| 5. **Test with Verbose SSH and Increase Client Timeouts** | Use `ssh -vvv user@host` to debug handshake steps and increase `ServerAliveInterval` and `ConnectTimeout` in SSH config. |


7. Your CI/CD pipeline fails due to network timeouts while pulling Docker images. What could be the cause, and how do you fix it?

| Cause | Fix |
|-------|-----|
| 1. **Unstable or Slow Network Connection** | Check network connectivity and bandwidth on the CI runners; switch to a regionally closer image registry if needed. |
| 2. **Docker Hub or Registry Rate Limiting** | Use authenticated access or a mirror registry to avoid hitting pull rate limits (e.g., Docker Hub free-tier limit). |
| 3. **DNS Resolution Failures** | Verify DNS settings in the CI environment; use a reliable DNS resolver like 8.8.8.8 or Cloudflare (1.1.1.1). |
| 4. **Firewall or Proxy Restrictions** | Ensure outbound access to image registries is allowed; configure proxy settings correctly in the pipeline environment. |
| 5. **Large or Unoptimized Image Sizes** | Optimize images by reducing layers and using smaller base images (e.g., `alpine`); use layer caching in CI to reduce pull times. |



Cloud Networking

6. A load balancer in AWS (ALB/ELB) is not distributing traffic evenly. What might be causing this?

| Cause | Description |
|-------|-------------|
| 1. **Sticky Sessions (Session Affinity) Enabled** | If stickiness is enabled, clients are routed to the same target, causing uneven load if some clients are heavier than others. |
| 2. **Unhealthy Targets** | If some targets are failing health checks, traffic is only routed to healthy ones, concentrating the load unevenly. |
| 3. **Improper Target Weighting in Target Groups** | For weighted target groups (especially with Lambda or multi-region), traffic might skew due to incorrect weights. |
| 4. **Imbalanced Target Resource Capacity** | Instances or containers behind the load balancer may differ in CPU/memory, causing slower nodes to respond less frequently. |
| 5. **DNS Caching and Client-Side Load Balancing** | For clients resolving ALB DNS, some DNS resolvers or clients may cache IPs longer, leading to partial traffic distribution. |


8. Your Azure Virtual Machine cannot connect to an Azure SQL Database. What are the possible misconfigurations?

9. You need to establish secure communication between Kubernetes pods running in different cloud regions. What networking solution would you use?

   | Solution | Description |
|----------|-------------|
| 1. **Service Mesh with mTLS (e.g., Istio, Linkerd)** | Use a service mesh to automatically encrypt pod-to-pod traffic across regions using mutual TLS (mTLS). |
| 2. **VPN or VPC Peering Between Cloud Regions** | Set up IPsec VPN tunnels or cloud-native VPC peering to establish private, encrypted network paths across regions. |
| 3. **WireGuard or Tailscale Mesh VPN** | Use lightweight, secure mesh VPNs like WireGuard or Tailscale to connect pods or nodes across clouds via encrypted tunnels. |
| 4. **Global Load Balancers with TLS Termination** | Use global load balancers (e.g., AWS Global Accelerator, GCLB) with end-to-end TLS to securely route traffic between regions. |
| 5. **Custom CNI Plugins Supporting Multi-Cluster (e.g., Cilium, Submariner)** | Leverage advanced CNI plugins that support cross-region, encrypted communication between Kubernetes clusters. |


10. Your AWS Lambda function times out when trying to reach a private database. What networking configurations should you check?

11. An application hosted on GCP is not accessible from the internet, even though it has a public IP. What could be the issue?


DNS & Load Balancing

11. Users report that your website sometimes resolves to the wrong IP address. How would you diagnose this DNS issue?

| Step | Description |
|------|-------------|
| 1. **Verify DNS Records from Authoritative Source** | Use `dig +trace <domain>` or check directly with your DNS provider to confirm the correct A/AAAA records. |
| 2. **Check for Stale or Cached DNS Entries** | Use tools like `nslookup`, `dig`, or online DNS checkers from multiple locations to detect outdated resolver caches. |
| 3. **Inspect TTL Values on DNS Records** | Ensure TTLs are appropriately set; very high values can cause long-lived caching of outdated IP addresses. |
| 4. **Audit DNS Changes and Automation Tools** | Review DNS update logs or automation tools like ExternalDNS, Terraform, or CI pipelines that may have introduced incorrect records. |
| 5. **Test Across ISPs and Devices** | Replicate the issue from different networks to identify if the problem is ISP- or region-specific due to DNS resolver propagation delays. |




12. Your team deployed a DNS change, but some users still resolve to the old IP. How do you ensure a smooth transition?

| Step | Description |
|------|-------------|
| 1. **Lower TTL Before the Change** | Reduce the DNS record TTL (e.g., to 60 seconds) at least 24–48 hours before the planned change to speed up propagation. |
| 2. **Use Dual IP Configuration Temporarily** | Point DNS to both old and new IPs using round-robin A records or a load balancer to avoid disruptions during the transition. |
| 3. **Monitor DNS Resolution Globally** | Use tools like `dnschecker.org` or `dig` from multiple regions to confirm propagation across major DNS resolvers. |
| 4. **Keep the Old IP Functional Post-Change** | Continue serving traffic from the old IP for a grace period to support users with stale DNS caches. |
| 5. **Communicate and Validate Client Behavior** | Inform users and validate that DNS caches are clearing properly on critical systems using tools like `nslookup` or `host`. |


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


Networking Performance & Monitoring

21. Your microservices application has high network latency between services. How do you identify the bottleneck?

    
| Step | Description |
|------|-------------|
| 1. **Enable Distributed Tracing** | Use tools like Jaeger, OpenTelemetry, or Zipkin to trace requests across services and pinpoint latency between hops. |
| 2. **Monitor Service-to-Service Latency Metrics** | Use Prometheus metrics (e.g., `istio_request_duration_seconds` or custom histograms) to detect slow communication paths. |
| 3. **Check Network Policies and DNS Resolution** | Misconfigured `NetworkPolicy` or slow CoreDNS resolution can delay inter-service calls; use `kubectl logs` and DNS metrics to diagnose. |
| 4. **Inspect Node and Pod Resource Pressure** | Use `kubectl top pods/nodes` or Grafana dashboards to check for CPU, memory, or network saturation affecting service performance. |
| 5. **Test with Network Performance Tools** | Run tools like `iperf`, `curl`, or `tcptraceroute` between pods to simulate traffic and measure raw latency manually. |

23. A production system experiences random network outages, but there are no alerts in your monitoring tool. What steps do you take?

| Step | Description |
|------|-------------|
| 1. **Enable Packet Loss and Latency Metrics** | Collect metrics like `node_network_receive_errs_total`, `node_network_transmit_drop_total`, and TCP retransmits to detect silent network issues. |
| 2. **Audit Network Policies, Security Groups, and Firewalls** | Review Kubernetes `NetworkPolicy`, cloud security groups, and firewall rules for misconfigurations or intermittent blocking. |
| 3. **Use Synthetic Probes and Blackbox Exporter** | Deploy tools like Prometheus Blackbox Exporter to simulate traffic and monitor endpoint availability across zones or clusters. |
| 4. **Enable and Analyze VPC Flow Logs** | Check cloud provider VPC flow logs to detect dropped connections, asymmetric routing, or denied traffic not visible in app logs. |
| 5. **Set Up Alerts for Network-Level Anomalies** | Add alerting rules for latency spikes, connection drops, DNS errors, and pod restarts to catch transient issues early. |

    
