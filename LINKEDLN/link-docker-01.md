
 You are running a containerized application that crashes intermittently without logging anything useful. How do you debug this behavior?

2. Your CI/CD pipeline pushes a new Docker image that fails only in production, not in staging. How would you isolate and resolve the discrepancy?

3. Your Docker image builds are inconsistent across developers’ machines. How would you ensure repeatable builds?

4. How would you securely inject secrets into a container without hardcoding them in Dockerfile or exposing them in environment variables?

5. A container using a volume is not syncing changes back to the host machine. How do you diagnose and resolve this?

6. You need to migrate your local Docker-based app to Kubernetes. What Docker-specific configurations might cause issues during the migration?

7. Your container uses a large base image and takes a long time to download in remote environments. What strategies can you apply to improve this?

8. You notice a container has exited with an OOMKilled (Out Of Memory) status. How do you investigate and prevent this?

9. How would you monitor file system usage and inode exhaustion in a running container?

10. Your team needs to run GPU-based containers on a shared host. How do you design a secure and performant setup?

11. You want to roll back to a previous container version but don't have the previous Dockerfile. How do you retrieve and use the old image?

12. You need to isolate a set of containers with custom firewall rules. How do you implement this using Docker’s networking capabilities?

13. A container exposes multiple ports, but some are not accessible externally. How do you verify and expose the correct ports?

14. How do you configure Docker for a multi-architecture build (e.g., building for x86 and ARM simultaneously)?

15. Your Dockerfile uses ADD to fetch remote URLs, but the builds fail due to SSL errors in CI. How do you debug and solve this?

16. You notice layers in your Docker image are not being cached during builds. What could be causing this?

17. You are required to enforce immutability for Docker containers in production. How would you approach this?

18. How would you implement a security scanning workflow integrated with your CI/CD process for Docker containers?

19. What would you do if Docker container logs are rotated too frequently and important logs are being lost?

20. You suspect your container image has been tampered with. How do you validate its authenticity?

21. How do you enforce policy controls such as image whitelisting in a Docker deployment?

22. A base image you use has been deprecated. How do you manage and migrate all dependent services with minimal downtime?
