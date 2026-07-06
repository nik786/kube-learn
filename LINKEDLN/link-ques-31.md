
4. How would you securely inject secrets into a container without hardcoding them in Dockerfile or exposing them in environment variables?

| Method                                      | Description                                                                                  | Pros                                                   | Cons                                                    |
|--------------------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------|
| **Docker Secrets (Swarm)**                 | Store secrets in Docker Swarm and mount them as files inside containers.                     | Secure, in-memory file system, auto-managed by Docker. | Requires Docker Swarm mode.                            |
| **Kubernetes Secrets**                     | Use Kubernetes to inject secrets as mounted volumes or environment variables.                | Managed at cluster level, supports RBAC and encryption.| Requires Kubernetes setup and correct RBAC policies.    |
| **HashiCorp Vault + Sidecar/Agent Injector** | Secrets pulled at runtime via Vault agent or sidecar pattern.                                | Highly secure, supports dynamic secrets.               | Requires Vault setup, complexity in integration.        |
| **AWS Secrets Manager / Parameter Store**  | Secrets fetched at runtime using SDK/CLI inside the container.                              | Secure, integrates with IAM.                           | Adds latency, requires credentials management.          |
| **Mounted Secret Files (from CI/CD)**      | CI/CD mounts secrets (like `.env`, `.pem`) at runtime and removes after execution.            | No hardcoding, temporary access.                       | Must ensure cleanup and restrict file permissions.      |
| **Docker BuildKit Secrets**                | Inject secrets during build using `--secret` flag (not available in plain Docker).           | Avoids hardcoding, no trace in image layers.           | Requires BuildKit support and updated Docker version.   |
| **Environment Variable Injection via CI/CD** | Inject secrets at runtime via CI/CD platform (e.g., GitHub Actions secrets, GitLab CI vars). | Easy to set up and integrate.                          | Still visible in container env; use carefully.          |


   

6. A container using a volume is not syncing changes back to the host machine. How do you diagnose and resolve this?

| Step                          | Description                                                                                          | Commands/Actions                                                                 |
|-------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Check Volume Type**         | Determine if you're using a named volume or bind mount — only bind mounts sync with host filesystem. | `docker inspect <container>` → check `Mounts` section.                          |
| **Verify Mount Path**         | Ensure the correct host directory is being mounted and not shadowed by an internal path.             | Compare paths in Docker run/compose files: `host_path:container_path`.          |
| **Inspect File Permissions**  | Host directory permissions may prevent file creation or changes from being visible.                  | `ls -l <host_dir>` and `chmod` / `chown` if needed.                             |
| **Container Writing Location**| Confirm that your app writes to the mounted volume path, not somewhere else inside the container.     | Check app config/logs; exec into container to inspect: `docker exec -it <id> sh`|
| **Check for Cached Mounts**   | On macOS/Windows, Docker Desktop may cache volumes for performance, causing delays.                  | Use `:cached` or `:delegated` options, or restart Docker Desktop.               |
| **Restart Container**         | Sometimes Docker needs a restart to properly mount volumes, especially after config changes.         | `docker restart <container>`                                                    |
| **Use Correct Compose Syntax**| In Docker Compose, ensure you're using the correct `volumes:` syntax and indentation.                | Refer to official Compose file reference.                                       |
| **Cross-Platform Paths**      | Windows/macOS paths can cause issues due to OS-specific formatting.                                 | Ensure proper path format: `/c/Users/...` for Windows.                          |





8. You need to migrate your local Docker-based app to Kubernetes. What Docker-specific configurations might cause issues during the migration?

| Docker-Specific Configuration         | Potential Issue in Kubernetes Migration                                           | Resolution/Recommendation                                                       |
|--------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Docker `docker-compose.yml` files**| Kubernetes does not natively understand Compose format.                           | Use `kompose` or manually convert to `Deployment`, `Service`, `Volume`, etc.    |
| **`depends_on` directive**           | Kubernetes does not guarantee container startup order.                            | Use readiness/liveness probes and init containers instead.                      |
| **Port bindings (`ports`)**          | `ports` in Docker map host to container; Kubernetes uses Services for networking. | Define a `Service` (NodePort/ClusterIP/LoadBalancer) to expose container ports. |
| **Named Volumes**                    | Docker-managed volumes don’t map directly to Kubernetes volumes.                  | Use `PersistentVolume` and `PersistentVolumeClaim` in Kubernetes.               |
| **Environment variables (`env_file`)**| Kubernetes doesn’t support `env_file` directly.                                   | Convert variables to `env:` blocks or use `ConfigMap`/`Secret`.                 |
| **Host networking (`network: host`)**| Host networking is discouraged and limited in Kubernetes.                         | Use Kubernetes Services for pod communication.                                  |
| **Dockerfile ENTRYPOINT/CMD logic** | Complex entrypoint scripts may fail or conflict with Kubernetes lifecycle.        | Refactor for container portability; use simpler entrypoints with `args`.        |
| **No health checks in Docker**       | Missing `HEALTHCHECK` in Dockerfile results in pods without liveness probes.      | Define `livenessProbe` and `readinessProbe` in the pod spec.                    |
| **Volume mount paths hardcoded**     | Paths may not match Kubernetes volume mounts or PVCs.                             | Abstract file paths or configure them using environment variables.              |
