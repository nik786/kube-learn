
1. You are running a containerized application that crashes intermittently without logging anything useful. How do you debug this behavior?
   
| Step                         | Description                                                                                 | Tools / Best Practices                                 |
|------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **Check Container Logs**      | Review container logs (`docker logs` or Kubernetes `kubectl logs`) for any subtle clues.    | Docker CLI, kubectl, centralized logging (ELK, Fluentd)|
| **Enable Debug/Verbose Mode** | Run the application with increased logging verbosity or debug flags to get detailed output. | Application config, environment variables               |
| **Inspect Exit Codes**        | Check container exit codes to identify crash reasons (e.g., OOM, segmentation fault).       | `docker inspect`, `kubectl describe pod`                |
| **Monitor Resource Usage**    | Track CPU, memory, disk, and network usage to detect resource exhaustion or spikes.          | Prometheus, Grafana, `docker stats`, `kubectl top`      |
| **Check Host & Kernel Logs** | Review host OS logs for container-related errors (e.g., kernel OOM killer).                  | `dmesg`, `/var/log/syslog`, journalctl                   |
| **Reproduce with Debug Tools**| Run container interactively or attach debugger inside container for real-time analysis.    | `docker exec -it`, `kubectl exec`, `gdb`, `strace`      |
| **Review Application Code**  | Analyze recent changes for bugs or memory leaks causing crashes.                            | Source control, static code analysis                     |
| **Check Dependencies**       | Verify external services and dependencies are available and responsive.                     | Service monitoring, health checks                        |
| **Isolate Changes**          | Test older image versions or configurations to identify if recent updates introduced the issue.| CI/CD rollback, version control                         |
| **Use Core Dumps & Crash Reports**| Collect and analyze core dumps if available to understand crash root cause.               | Configure core dumps, use debugging tools                |
| **Consult Container Runtime Logs**| Review Docker or Kubernetes runtime logs for runtime errors.                              | Docker daemon logs, kubelet logs                          |

   

3. Your CI/CD pipeline pushes a new Docker image that fails only in production, not in staging. How would you isolate and resolve the discrepancy?

| Step                      | Description                                                                                  | Tools / Best Practices                                     |
|---------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| **Compare Environments**   | Verify differences between staging and production environments (config, secrets, versions). | Infrastructure as Code (IaC), environment variable audits  |
| **Check Logs & Metrics**   | Analyze application and container logs in production for error clues.                        | ELK Stack, Prometheus, Grafana, CloudWatch                  |
| **Validate Configuration**| Confirm config files, environment variables, and secrets are consistent and correct.         | HashiCorp Vault, Kubernetes ConfigMaps and Secrets          |
| **Resource Availability** | Check if production has sufficient CPU, memory, storage, and network access.                 | Monitoring tools, Kubernetes resource metrics                |
| **Network & Firewall**    | Ensure production network policies or firewalls don’t block required communication.          | Network policies, security groups                            |
| **Check Image Tag & Deployment** | Confirm the exact image version deployed matches what was tested in staging.               | Image digest verification, deployment manifests             |
| **Replicate Production Locally** | Try to replicate production environment on local or test clusters for debugging.            | Docker Compose, Minikube, kind                              |
| **Rollback & Compare**    | Roll back to previous stable image in production to verify if issue resolves.                 | CI/CD rollback strategies                                   |
| **Incremental Rollout**    | Use canary or blue-green deployment to isolate issues with new image.                        | Kubernetes Deployment strategies                            |
| **Review Differences in Dependencies** | Check if dependencies or external services differ between environments.                  | Dependency management, service mocks                         |
| **Collaborate with Teams** | Involve dev, ops, and security teams for comprehensive diagnosis.                            | Communication tools, incident management                     |



4. Your Docker image builds are inconsistent across developers’ machines. How would you ensure repeatable builds?

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






          |











