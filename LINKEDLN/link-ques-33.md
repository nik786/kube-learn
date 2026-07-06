
13. Your team needs to run GPU-based containers on a shared host. How do you design a secure and performant setup?

| Consideration                        | Recommendation                                                                                 | Benefit                                                   |
|-------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| **GPU Access Management**           | Use NVIDIA Container Toolkit (`nvidia-docker2`) and specify GPUs using `--gpus` flag.          | Granular GPU allocation; avoids overuse/conflict.          |
| **Resource Isolation**              | Use cgroups and namespaces to isolate CPU, memory, and GPU usage per container.                | Prevents one container from starving others.               |
| **Security Boundaries**            | Avoid `--privileged` mode; use Docker’s `--cap-drop` and `--cap-add` for minimal privilege.    | Reduces attack surface within shared GPU host.             |
| **Kubernetes GPU Scheduling**       | Use device plugins like `nvidia-device-plugin` with Kubernetes for GPU-aware scheduling.       | Automates secure and balanced GPU allocation in clusters.  |
| **Driver Version Control**          | Ensure host NVIDIA drivers match container CUDA versions. Use pre-built CUDA base images.      | Prevents runtime incompatibilities and crashes.            |
| **User Namespace Remapping**        | Enable Docker user namespace isolation (`userns-remap`).                                       | Improves security for multi-user environments.             |
| **Storage Isolation**               | Use separate volumes or namespaces for each workload’s data.                                  | Prevents data leakage or unintended sharing.               |
| **Monitoring and Quotas**           | Use tools like `nvidia-smi`, DCGM, or Prometheus + Node Exporter to monitor usage.             | Ensures fair use and enables proactive management.          |
| **Logging and Audit Trails**        | Enable detailed logging per container and audit GPU usage.                                    | Traceability and accountability for shared access.         |
| **Use Hardened Base Images**        | Prefer minimal and trusted CUDA base images from NVIDIA.                                      | Reduces image size and attack surface.                     |


15. You want to roll back to a previous container version but don't have the previous Dockerfile. How do you retrieve and use the old image?
    
| Step                                 | Description                                                                 | Command / Action                                                       | Benefit                                  |
|--------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------|
| **Check Local Images**               | See if the previous image still exists locally.                             | `docker images`                                                        | Quick rollback if image is available.    |
| **Use Image by Digest**              | Pull a known previous image by its digest if tag has changed.              | `docker pull <image>@<sha256:digest>`                                 | Ensures exact image version.             |
| **Pull by Old Tag (if known)**       | Pull the image using an older tag from the registry.                        | `docker pull myapp:1.2.3`                                              | Restores tagged version easily.          |
| **Check Remote Registry**            | Browse Docker Hub, ECR, or your private registry to find old versions.     | Use registry UI/CLI (`aws ecr list-images`, etc.)                      | Access archived versions.                |
| **Run from Image ID**                | Start container directly using image ID if locally cached.                 | `docker run <image_id>`                                               | No need for Dockerfile.                  |
| **Tag and Use Old Image**            | Tag the retrieved image with a usable tag for clarity.                     | `docker tag <image_id> myapp:rollback`                                | Makes rollback version explicit.         |
| **Export and Archive Image**         | Save image for backup or rollback later.                                   | `docker save -o myapp.tar myapp:rollback`                             | Enables future reuse offline.            |
| **Create Dockerfile from Image**     | Reconstruct a basic Dockerfile using image as base.                        | `FROM myapp:rollback`                                                 | Useful for rebuilding or customization.  |
| **Use CI/CD Artifacts**              | Check if your pipeline archives images or Dockerfiles.                     | Refer CI tool's image repo or logs.                                   | Maintains audit trail for rollbacks.     |
