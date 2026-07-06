
17. You need to isolate a set of containers with custom firewall rules. How do you implement this using Docker’s networking capabilities?
    
| Step / Method                          | Description                                                                                 | Command / Action Example                                            | Benefit                                                  |
|----------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------|
| **Create a Custom Docker Network**     | Use Docker’s bridge network to isolate containers from default network.                    | `docker network create --driver bridge isolated_net`               | Logical isolation and scoped communication.              |
| **Run Containers in Custom Network**   | Attach containers to the new isolated network only.                                         | `docker run --network=isolated_net myapp`                          | Prevents default network exposure.                       |
| **Use `iptables` for Firewall Rules**  | Define custom rules to control traffic to/from containers in the custom network.            | `iptables -A FORWARD -i br-<id> -o eth0 -j ACCEPT`                 | Fine-grained control over traffic.                       |
| **Use `--internal` Network Flag**      | Create an internal-only network with no external internet access.                          | `docker network create --internal isolated_internal_net`           | Blocks outbound access for sensitive workloads.          |
| **Expose Only Required Ports**         | Avoid using `-p` to expose ports unless explicitly needed.                                 | `docker run -d myapp` (without `-p`)                               | Reduces attack surface.                                  |
| **Combine with Firewalld / UFW**       | Use host-based firewalls to further restrict traffic to/from Docker bridge interfaces.     | `ufw deny in on docker0`                                            | Host-level network protection.                           |
| **Use Docker Compose with Networks**   | Define multiple networks and restrict services to specific ones.                           | `networks:` block in `docker-compose.yml`                          | Easier management of complex container setups.           |
| **Limit Inter-Container Communication**| Use `--icc=false` to disable default inter-container communication.                        | Add `--icc=false` in Docker daemon settings (`/etc/docker/daemon.json`) | Enforces strict communication paths.                  |
| **Monitor with `docker network inspect`** | Audit network settings and container connections.                                          | `docker network inspect isolated_net`                              | Verifies proper isolation and config.                    |



19. A container exposes multiple ports, but some are not accessible externally. How do you verify and expose the correct ports?

| Step                                 | Description                                                                                  | Command/Tool Example                                                                  |
|--------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **1. Check Dockerfile or Pod Spec**  | Identify all ports exposed by the container.                                                 | Docker: `EXPOSE 80 443` <br>Kubernetes: `kubectl get pod <pod> -o yaml`              |
| **2. Inspect Running Container**     | Confirm which ports are open inside the container.                                           | `docker inspect <container-id>` or `kubectl describe pod <pod-name>`                 |
| **3. Check Service Definition**      | In Kubernetes, ensure a Service maps to the correct container ports.                         | `kubectl get svc <service-name> -o yaml`                                             |
| **4. Verify Network Policy Rules**   | Ensure no NetworkPolicies are restricting access to certain ports.                          | `kubectl get networkpolicy` and inspect rules                                        |
| **5. Check Ingress or Load Balancer**| Confirm Ingress/LoadBalancer is configured to route traffic to desired ports.               | `kubectl get ingress <name> -o yaml`                                                 |
| **6. Test Port Accessibility**       | Test port availability externally using tools like curl, telnet, or nmap.                    | `curl http://<ip>:<port>`, `telnet <ip> <port>`, `nmap <ip>`                         |
| **7. Update Service/Ingress Rules**  | If ports are missing in Service or Ingress, add them.                                        | Update Service YAML: `ports: - port: 8080 targetPort: 8080`                          |
| **8. Restart/Apply Resources**       | Apply updated configuration and restart pods if necessary.                                  | `kubectl apply -f <updated-file>.yaml`                                               |
| **9. Confirm Port Binding**          | Ensure container is actually listening on the port inside.                                   | `kubectl exec <pod> -- netstat -tulnp` or `ss -tulnp`                                |
| **10. Monitor and Audit**            | Continuously monitor service reachability and audit changes in network configurations.       | Prometheus, ELK, Cloud-native tools (CloudWatch, GCP Monitoring, etc.)               |





21. How do you configure Docker for a multi-architecture build (e.g., building for x86 and ARM simultaneously)?

| Step / Method                          | Description                                                                                     | Command / Example                                                                 |
|----------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Enable Docker Buildx**              | Buildx is a Docker CLI plugin that supports multi-arch builds.                                  | `docker buildx create --use`                                                     |
| **Set Up QEMU Emulation**             | Enables building and running images for non-native architectures.                              | `docker run --privileged --rm tonistiigi/binfmt --install all`                  |
| **Use `--platform` Flag**             | Specify target platforms during build.                                                          | `docker buildx build --platform linux/amd64,linux/arm64 .`                       |
| **Push to Registry**                  | Required to export multi-arch manifest; local loading not supported by all formats.             | Add `--push` to buildx command: `--push -t myapp:latest`                         |
| **Use `Dockerfile` Best Practices**   | Ensure dependencies and binaries are available for all target platforms.                        | Use multi-platform base images (e.g., `python`, `node`, `alpine`, etc.).         |
| **Inspect Built Manifest**           | Verify the image supports multiple architectures.                                               | `docker buildx imagetools inspect myapp:latest`                                 |
| **Use `platform:` in Docker Compose**| Specify platform in `docker-compose.yml` for services (for testing).                           | `platform: linux/arm64`                                                          |
| **Install Latest Docker & Buildx**    | Ensure Docker Engine and CLI are up to date (Docker 20.10+ recommended).                       | `docker version` and `docker buildx version`                                     |
| **Use GitHub Actions / CI Tools**     | Automate multi-arch builds in pipelines with official `docker/build-push-action`.              | GitHub Actions: `uses: docker/build-push-action@v5`                              |
| **Cache Builds Efficiently**         | Use `--build-arg`, `--cache-from`, and `--cache-to` to optimize builds for each arch.          | `--cache-to=type=inline --cache-from=type=registry,ref=myapp:cache`              |
