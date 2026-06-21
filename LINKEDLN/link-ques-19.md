
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

| Misconfiguration | Description |
|------------------|-------------|
| 1. **Firewall Rules on Azure SQL Server** | The SQL server's firewall may not allow the VM's outbound IP address; add the VM's IP in the SQL firewall settings. |
| 2. **Incorrect Connection String or Credentials** | Errors in the connection string format, database name, username, or password can prevent successful authentication. |
| 3. **Network Security Group (NSG) Blocking Outbound Traffic** | NSG attached to the VM's subnet or NIC might block outbound traffic to port 1433 (used by Azure SQL). |
| 4. **Private Endpoint Misconfiguration** | If Azure SQL is using a private endpoint, ensure the VM is in the correct VNet/subnet and DNS is resolving to the private IP. |
| 5. **Missing VNet Service Endpoint for SQL** | Without enabling the SQL service endpoint on the VM’s subnet, traffic to Azure SQL may be rejected, especially in secured networks. |


9. You need to establish secure communication between Kubernetes pods running in different cloud regions. What networking solution would you use?

| Solution | Description |
|----------|-------------|
| 1. **Service Mesh with mTLS (e.g., Istio, Linkerd)** | Use a service mesh to automatically encrypt pod-to-pod traffic across regions using mutual TLS (mTLS). |
| 2. **VPN or VPC Peering Between Cloud Regions** | Set up IPsec VPN tunnels or cloud-native VPC peering to establish private, encrypted network paths across regions. |
| 3. **WireGuard or Tailscale Mesh VPN** | Use lightweight, secure mesh VPNs like WireGuard or Tailscale to connect pods or nodes across clouds via encrypted tunnels. |
| 4. **Global Load Balancers with TLS Termination** | Use global load balancers (e.g., AWS Global Accelerator, GCLB) with end-to-end TLS to securely route traffic between regions. |
| 5. **Custom CNI Plugins Supporting Multi-Cluster (e.g., Cilium, Submariner)** | Leverage advanced CNI plugins that support cross-region, encrypted communication between Kubernetes clusters. |


11. Your AWS Lambda function times out when trying to reach a private database. What networking configurations should you check?

| Configuration | Description |
|---------------|-------------|
| 1. **VPC Configuration for Lambda** | Ensure the Lambda function is configured to run in the same VPC (and subnet) as the private database or has proper routing. |
| 2. **Subnet Route Tables and NAT Gateway** | Verify that the subnets have correct routes to access the database, and if needed, include a NAT Gateway for outbound traffic. |
| 3. **Security Group Rules** | Check that the Lambda's security group allows outbound traffic and the database’s security group allows inbound traffic from the Lambda. |
| 4. **Network ACLs (NACLs)** | Ensure NACLs associated with the subnets are not blocking traffic between the Lambda function and the database port. |
| 5. **Database Endpoint and Port** | Confirm the database endpoint is correct and the target port (e.g., 3306 for MySQL, 5432 for PostgreSQL) is open and accepting traffic. |


