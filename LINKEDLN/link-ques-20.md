
13. An application hosted on GCP is not accessible from the internet, even though it has a public IP. What could be the issue?


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
