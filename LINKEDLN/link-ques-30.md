
You notice API server response times are increasing. How would you diagnose and tune it?

| Step / Area                                 | Description                                                                                           |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Check API Server Metrics**                | Use Prometheus and Grafana to analyze API server metrics like `apiserver_request_duration_seconds` and request rates. |
| **Audit etcd Performance**                  | Inspect etcd latency using metrics like `etcd_disk_wal_fsync_duration_seconds` and check for storage IOPS issues. |
| **Review API Server Logs**                  | Analyze logs for slow requests, authentication/authorization issues, or webhook timeouts.             |
| **Optimize Admission Webhooks**            | Ensure any custom admission controllers or validating webhooks are responsive and not bottlenecking requests. |
| **Scale API Server or etcd (HA Setup)**     | Horizontally scale the API server or deploy a multi-member etcd cluster to distribute load and improve availability. |





What tools and practices would you use to benchmark application performance within the cluster?

| Tool / Practice                             | Description                                                                                           |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Apache JMeter / k6**                      | Use load testing tools like **JMeter** or **k6** to simulate real traffic and benchmark application throughput, latency, and error rates. |
| **Prometheus + Grafana Dashboards**         | Collect and visualize application metrics (CPU, memory, response time) to identify performance bottlenecks over time. |
| **Distributed Tracing (Jaeger/Tempo)**      | Trace request flows across services to measure latency and pinpoint slow components or dependencies.  |
| **Custom Metrics via Application Instrumentation** | Expose metrics using libraries like **Prometheus client** to measure domain-specific KPIs (e.g., request count, processing time). |
| **Chaos Engineering Tools (e.g., Litmus)**  | Introduce failures under controlled conditions to benchmark recovery time, system robustness, and stress handling. |
