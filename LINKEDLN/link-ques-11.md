

# DevOps Interview Questions & Answers

| 🔹 Question                                                                                  | ✅ Answer                                                                                                                                                             |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Git rebase vs. merge                                                                         | `git rebase` rewrites commit history for a linear flow; `git merge` combines histories preserving the original commits and branches.                                 |
| What is Terraform taint?                                                                     | `terraform taint` marks a resource for recreation in the next `apply`, useful when a resource is unhealthy or needs to be rebuilt.                                  |
| Describe your pipeline.                                                                      | CI/CD pipeline with GitHub/GitLab → Jenkins/GitLab CI → Docker → Artifact Repository → Helm → Kubernetes (EKS/AKS) → Monitoring via Prometheus/Grafana.             |
| Describe a DevOps pipeline using YAML.                                                       | A GitLab CI/CD YAML defines stages like `build`, `test`, `deploy`, with each job specifying script, image, tags, and environment using declarative syntax.          |
| Describe a desktop project that produces an artifact.                                        | A Python PyQt desktop app packaged using `pyinstaller`, producing `.exe` or `.dmg` as the deployable artifact.                                                       |
| What is your experience with ARM templates and Terraform?                                    | Strong Terraform expertise across modules, workspaces, remote state; basic exposure to ARM templates for resource provisioning in Azure.                            |
| How would you approach migrating 500+ on-premises systems to AWS or Azure?                   | Assess workloads, use discovery tools, group by complexity, design landing zone, build IaC, migrate in phases, validate, then optimize.                              |
