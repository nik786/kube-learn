
23. Your Dockerfile uses ADD to fetch remote URLs, but the builds fail due to SSL errors in CI. How do you debug and solve this?

24. You notice layers in your Docker image are not being cached during builds. What could be causing this?

| Possible Cause                                | Description                                                                 | Resolution / Best Practice                                                    |
|-----------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Changes in Earlier Layers**                 | Docker rebuilds all subsequent layers if an earlier layer changes.         | Place rarely changing instructions (e.g., `apt-get install`) early in Dockerfile. |
| **Missing Build Cache**                       | Build context may not use existing layers if not preserved.                | Use `--build-arg`, `--cache-from`, and proper base image tags consistently.  |
| **Changing `COPY` or `ADD` Timestamp**        | File modifications (even metadata) trigger rebuild of `COPY` layers.       | Use `.dockerignore` to limit context; avoid unnecessary file changes.        |
| **No `--cache-from` in CI/CD**                | CI/CD may not load prior cache layers without explicit cache source.       | Use `--cache-from` flag with a previously built image.                       |
| **Non-deterministic Commands**                | Commands generating different output (e.g., `date`, `random`) break cache. | Avoid non-deterministic logic during build or isolate in final stage only.   |
| **Environment Variable Changes**              | Changing `ARG` or `ENV` values causes cache invalidation.                  | Avoid frequent changes to `ARG` values in early layers.                      |
| **`ADD` Remote URLs**                         | URLs fetched dynamically always re-download, breaking cache.               | Replace `ADD` with `curl/wget` and manage caching manually if needed.        |
| **Inconsistent Dockerfile Formatting**        | Even whitespace or comment changes may affect hash calculations.           | Keep Dockerfile clean and structured for minimal change impact.              |
| **Rebuild with `--no-cache`**                 | Forces Docker to ignore all existing cache layers.                         | Avoid using `--no-cache` unless a clean build is needed.                     |


26. You are required to enforce immutability for Docker containers in production. How would you approach this?

| Strategy                                  | Description                                                                                     | Benefit                                                     |
|-------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **Read-Only Filesystem**                  | Run containers with a read-only root filesystem.                                                 | Prevents unauthorized modifications to the container.       |
| **Immutable Images**                      | Only deploy versioned, tagged, and verified images (e.g., `myapp:1.2.3`).                        | Ensures consistency and traceability of deployments.        |
| **Disable Shell Access**                  | Avoid adding shells (like `bash`) in production images.                                          | Reduces risk of runtime tampering.                          |
| **No `exec` or Interactive Access**       | Disallow `docker exec` or `kubectl exec` in production containers.                              | Prevents in-place changes or debugging in production.        |
| **Kubernetes SecurityContext**            | Set `readOnlyRootFilesystem: true` and drop unnecessary Linux capabilities.                      | Enforces immutability at orchestrator level.                |
| **Immutable Infrastructure Workflow**     | Use CI/CD pipelines to replace (not update) containers when changes are needed.                  | Aligns with declarative, immutable deployment practices.    |
| **Use Digest-Based Image References**     | Deploy using image digests (e.g., `@sha256:...`) instead of tags.                                | Ensures exact image version is used.                        |
| **Use Signed and Verified Images**        | Enforce image signing via tools like Docker Content Trust (DCT) or Sigstore.                    | Prevents tampered or unauthorized image use.                |
| **Mount Volumes as Read-Only**            | Use `:ro` flag for mounted volumes that do not require write access.                            | Preserves data integrity of mounted content.                |
| **Audit and Monitoring**                  | Continuously monitor containers for changes and unauthorized access.                            | Enables detection of policy violations and security issues. |

    

