
28. How would you implement a security scanning workflow integrated with your CI/CD process for Docker containers?

| Step                      | Description                                                       | Tools / Best Practices                                          |
|---------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------|
| **Integrate Scanning in CI** | Add automated image scanning as a build step in the CI pipeline.  | Trivy, Clair, Anchore, Aqua Security integrated in Jenkins/GitHub Actions/GitLab CI |
| **Scan Base and Final Images** | Scan both base images and final built images for vulnerabilities. | Use multi-stage scans; verify base image trustworthiness.       |
| **Fail Builds on Critical Issues** | Configure pipeline to fail if high or critical vulnerabilities are found. | Define vulnerability severity thresholds for build failure.    |
| **Use Cached Scan Results** | Cache scan results for unchanged layers to speed up the pipeline. | Utilize scanning tools’ cache features or CI caching mechanisms.|
| **Generate Scan Reports**   | Produce detailed security reports for audit and review.          | Generate HTML/JSON reports; publish in pipeline artifacts.      |
| **Implement Image Signing** | Sign images post-scan to ensure integrity and provenance.         | Cosign, Notary, Docker Content Trust                            |
| **Push to Trusted Registry**| Push only scanned and signed images to trusted registries.        | Use private registries with access control (Harbor, AWS ECR).   |
| **Enforce Runtime Policies** | Enforce runtime security by allowing only scanned/signed images.  | Kubernetes Admission Controllers, OPA Gatekeeper, Falco.        |
| **Continuous Monitoring**  | Monitor deployed containers for new vulnerabilities post-deployment.| Vulnerability scanners integrated with orchestration platforms.|
| **Update and Re-scan Regularly** | Regularly update scanning databases and re-scan images.           | Schedule periodic rescans in CI or via registry hooks.          |


30. What would you do if Docker container logs are rotated too frequently and important logs are being lost?

| Issue / Cause                         | Description                                                          | Solution / Mitigation                                                                                |
|-------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **Log Rotation Frequency Too High** | Logs rotate before enough data is collected or analyzed.             | Adjust log rotation settings (`max-size`, `max-file`) in Docker daemon or container logging driver config. |
| **Small Log File Size Limits**       | `max-size` is set too low, causing frequent rotations.               | Increase `max-size` value to allow larger log files before rotation.                                   |
| **Low Number of Retained Files**     | `max-file` limits how many rotated files are kept.                    | Increase `max-file` to retain more rotated logs for longer.                                            |
| **Inappropriate Logging Driver**     | Using `json-file` driver with default or aggressive rotation.        | Consider switching to centralized logging (e.g., `fluentd`, `syslog`, `gelf`) to offload logs.         |
| **Log Volume Too High**               | Application produces excessive logs causing frequent rotation.       | Optimize application logging level to reduce verbosity (e.g., INFO -> WARN).                           |
| **No Centralized Log Aggregation**   | Logs only stored locally and lost on rotation or container removal.   | Implement centralized log storage and monitoring (e.g., ELK stack, Prometheus + Grafana, Splunk).      |
| **Disk Space Constraints**           | Limited disk space causes aggressive log rotation to free space.     | Allocate more disk space or clean old logs regularly via automated scripts.                            |
| **Misconfigured Logrotate**          | External logrotate tools conflicting with Docker’s internal rotation.| Ensure only one log rotation method is managing logs to avoid conflicts.                              |
