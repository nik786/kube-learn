
 You are running a containerized application that crashes intermittently without logging anything useful. How do you debug this behavior?

2. Your CI/CD pipeline pushes a new Docker image that fails only in production, not in staging. How would you isolate and resolve the discrepancy?

3. Your Docker image builds are inconsistent across developers’ machines. How would you ensure repeatable builds?

| Problem Area                       | Recommended Solution                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------------|
| **Base Image Variability**        | Pin to a specific image version (e.g., `python:3.10.4-slim`) to avoid latest tag drift. |
| **Build Context Differences**     | Use a clean and minimal `.dockerignore` to avoid accidental inclusion of local files. |
| **Dependencies Inconsistency**    | Use lock files (e.g., `requirements.txt`, `package-lock.json`) to pin exact versions. |
| **Different Docker Versions**     | Standardize Docker Engine and Docker Compose versions using tools like `asdf` or `nvm`. |
| **Local Changes Affecting Builds**| Use CI/CD pipeline for canonical builds; enforce `docker build --no-cache` locally.   |
| **Missing Build Arguments**       | Document and standardize `ARG` and `ENV` values in Dockerfiles and README.            |
| **Reproducibility Guarantee**     | Use Docker BuildKit or `docker buildx` with `--provenance=true` for better traceability. |
| **Tooling Consistency**           | Use tools like `Makefile`, `Justfile`, or `taskfile.yml` to standardize build commands. |



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

7. You need to migrate your local Docker-based app to Kubernetes. What Docker-specific configurations might cause issues during the migration?

8. Your container uses a large base image and takes a long time to download in remote environments. What strategies can you apply to improve this?

9. You notice a container has exited with an OOMKilled (Out Of Memory) status. How do you investigate and prevent this?

10. How would you monitor file system usage and inode exhaustion in a running container?

11. Your team needs to run GPU-based containers on a shared host. How do you design a secure and performant setup?

12. You want to roll back to a previous container version but don't have the previous Dockerfile. How do you retrieve and use the old image?

13. You need to isolate a set of containers with custom firewall rules. How do you implement this using Docker’s networking capabilities?

14. A container exposes multiple ports, but some are not accessible externally. How do you verify and expose the correct ports?

15. How do you configure Docker for a multi-architecture build (e.g., building for x86 and ARM simultaneously)?

16. Your Dockerfile uses ADD to fetch remote URLs, but the builds fail due to SSL errors in CI. How do you debug and solve this?

17. You notice layers in your Docker image are not being cached during builds. What could be causing this?

18. You are required to enforce immutability for Docker containers in production. How would you approach this?

19. How would you implement a security scanning workflow integrated with your CI/CD process for Docker containers?

20. What would you do if Docker container logs are rotated too frequently and important logs are being lost?

21. You suspect your container image has been tampered with. How do you validate its authenticity?

22. How do you enforce policy controls such as image whitelisting in a Docker deployment?

23. A base image you use has been deprecated. How do you manage and migrate all dependent services with minimal downtime?
