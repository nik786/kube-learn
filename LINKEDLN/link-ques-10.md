

1. Your application is experiencing intermittent connectivity issues with an external API. How do you troubleshoot and resolve this?

| Step | Description |
|------|-------------|
| 1. **Log and Correlate Failures** | Enable detailed logging of external API calls (status codes, timeouts, error messages) to identify patterns or failure windows. |
| 2. **Add Retry Logic with Backoff** | Implement exponential backoff and circuit breaker patterns in your application to handle transient API failures gracefully. |
| 3. **Monitor DNS Resolution and Latency** | Use tools like `dig`, `nslookup`, or Prometheus Blackbox Exporter to check for DNS flaps or variable response times. |
| 4. **Check Outbound Network Path** | Use `traceroute`, `curl`, or cloud VPC flow logs to inspect packet routes, latency, and possible egress firewall/NAT issues. |
| 5. **Coordinate with API Provider** | Contact the external API provider for service status, rate limits, or planned maintenance that might affect availability. |


3. A new service deployed in Kubernetes cannot communicate with a backend database. What steps would you take to diagnose the issue?

| Step | Description |
|------|-------------|
| 1. **Verify Service Environment Variables and Configs** | Check `ConfigMap`/`Secret` values for correct DB hostname, port, credentials, and ensure they’re mounted into the pod correctly. |
| 2. **Test Network Connectivity from the Pod** | Use `kubectl exec` to run tools like `curl`, `nc`, or `telnet` from the service pod to the database endpoint and port. |
| 3. **Check DNS Resolution** | Confirm the pod can resolve the database hostname using `nslookup`, `dig`, or inspecting the pod's `/etc/resolv.conf`. |
| 4. **Inspect Network Policies or Firewalls** | Review Kubernetes `NetworkPolicy`, security groups, and firewalls for rules that may block traffic between the pod and the database. |
| 5. **Review Database Logs and Connection Limits** | Check if the database is rejecting connections due to errors, timeouts, or exceeding max connection limits. |


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








