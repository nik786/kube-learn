
9. Your container uses a large base image and takes a long time to download in remote environments. What strategies can you apply to improve this?

| Strategy                                | Description                                                                                  | Benefit                                                |
|-----------------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **Use Minimal Base Images**             | Replace large base images (e.g., `ubuntu`, `node`) with slim or alpine variants.             | Reduces image size drastically.                       |
| **Multi-Stage Builds**                  | Separate build and runtime stages to copy only necessary artifacts to the final image.       | Smaller, cleaner final image.                         |
| **Layer Caching Optimization**          | Reorder Dockerfile instructions to leverage layer caching (e.g., install dependencies first).| Faster rebuilds; reduces bandwidth usage.             |
| **Remove Unnecessary Dependencies**     | Eliminate unused packages, files, or tools in the final image.                               | Reduces image bloat.                                  |
| **Compress Static Assets Before COPY**  | Minify and compress files (e.g., JS/CSS) during build stage.                                | Smaller image, faster to pull.                        |
| **Use `.dockerignore` File**            | Exclude files not needed in the container (e.g., `.git`, `node_modules`).                    | Avoids transferring unnecessary data into the image.  |
| **Use Distroless Images**               | Build final image with a distroless base to remove shell/package manager from runtime image. | Minimal, secure, and fast to download.                |
| **Use Private Registries with Caching** | Host images in geographically closer registries or use a proxy cache (e.g., Harbor).         | Reduces download latency in remote environments.      |
| **Use OCI Image Optimization Tools**    | Tools like `docker-slim` can shrink image size without changing functionality.               | Automated size reduction.                             |


11. You notice a container has exited with an OOMKilled (Out Of Memory) status. How do you investigate and prevent this?

| Step                          | Description                                                                                     | Command/Tool Example                                                                 |
|-------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **1. Identify the Container** | Check which container exited with `OOMKilled` status.                                           | `kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[*].state}'`     |
| **2. Check Pod Events**       | View events to confirm `OOMKilled` and get additional context.                                  | `kubectl describe pod <pod-name>`                                                   |
| **3. Review Logs**            | Look at the logs to understand what the container was doing before it exited.                   | `kubectl logs <pod-name> --previous`                                                |
| **4. Inspect Resource Usage** | Analyze memory usage using metrics if available.                                                | Use Prometheus/Grafana, `kubectl top pod <pod-name>`                                |
| **5. Check Resource Limits**  | Examine if `resources.limits.memory` is too low for the workload.                              | `kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].resources}'`          |
| **6. Tune Memory Limits**     | Increase the memory limit based on observed usage and workload needs.                          | Update deployment YAML: `resources: limits: memory: 512Mi`                          |
| **7. Optimize Application**   | Check for memory leaks or inefficient memory usage in the application code.                     | Use profiling tools (e.g., Valgrind, pprof) depending on the language               |
| **8. Enable Requests Properly** | Set `requests.memory` to allow appropriate scheduling and QoS classification.                  | `resources: requests: memory: 256Mi`                                                |
| **9. Consider HPA/VPA**       | Use Horizontal/Vertical Pod Autoscaler for dynamic scaling if applicable.                       | `kubectl autoscale deployment <name> --min=1 --max=5 --cpu-percent=80`              |
| **10. Monitor Proactively**   | Implement monitoring/alerting to catch memory issues early.                                     | Prometheus Alerts, CloudWatch Alarms, Datadog, etc.                                 |


13. How would you monitor file system usage and inode exhaustion in a running container?

| Method                               | Description                                                                 | Command/Tool Example                                              | Benefit                                         |
|--------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------|
| **Using `docker exec` + `df`**       | Check disk space usage inside the container.                               | `docker exec <container> df -h`                                   | Shows human-readable disk usage.               |
| **Using `docker exec` + `df -i`**    | Check inode usage inside the container.                                    | `docker exec <container> df -i`                                   | Helps detect inode exhaustion.                 |
| **Monitor from host (`/var/lib/docker`)** | Check underlying Docker filesystem usage.                                  | `du -sh /var/lib/docker/*`                                        | Helps trace which layers consume space.        |
| **Using container monitoring tools** | Tools like Prometheus + cAdvisor can monitor fs usage in containers.       | Deploy Prometheus with node_exporter and cAdvisor.                | Real-time metrics, alerting support.           |
| **Custom script inside container**   | Run cron or background task to log or alert on high usage.                 | `df -h > /tmp/disk_usage.log && df -i >> /tmp/inode_usage.log`    | Automates detection internally.                |
| **Use `--mount` and monitor host**   | Mount volumes from host and monitor them externally.                       | Monitor host path with tools like `iostat`, `du`, `inotify`.      | Greater control, host-level visibility.        |
| **Filesystem alerts via tools**      | Integrate with tools like Nagios, Zabbix, or Grafana Loki/Tempo.           | Setup alerts for inode/disk thresholds.                           | Proactive monitoring and alerting.   
