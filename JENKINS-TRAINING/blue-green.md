



| **Step** | **Stage** | **Tool** | **Action** | **Details** |
|----------|-----------|----------|------------|-------------|
| 1 | Code Commit | Git | Developers commit code | Code is pushed to a Git repository (GitHub, GitLab, Bitbucket). |
| 2 | Webhook Trigger | Jenkins | Start pipeline | Git webhook triggers Jenkins pipeline (via `Jenkinsfile`). |
| 3 | Build Stage | Jenkins | Build application | Jenkins builds the Docker image using a `Dockerfile`. |
| 4 | Push Image | Jenkins + Docker | Push to ECR | Jenkins pushes the built image to AWS Elastic Container Registry (ECR). |
| 5 | Identify Current Color | Jenkins + Kubectl | Get active version | Use `kubectl get svc` or config map to determine if current is `blue` or `green`. |
| 6 | Helm Render | Helm | Prepare chart | Use Helm templates to create manifests for the inactive color (blue or green). |
| 7 | Deploy Inactive Color | Helm | Deploy new version | Deploy new version to EKS under inactive color namespace or label (`blue` or `green`). |
| 8 | Smoke Test | Jenkins + Helm | Health check | Run smoke tests or `kubectl rollout status` to validate new deployment. |
| 9 | Switch Traffic | Jenkins + Kubectl | Update service selector | Change Kubernetes `Service` to route traffic to the new deployment (switch from blue to green or vice versa). |
| 10 | Cleanup (Optional) | Jenkins + Kubectl | Remove old deployment | Delete or scale down old color deployment. Optionally keep for rollback. |
| 11 | Notify | Jenkins | Slack/Email | Send deployment success/failure notification to the team. |

### Notes:
- Use Helm values files like `values-blue.yaml` and `values-green.yaml` for environment-specific configuration.
- Use a Jenkins `choice` parameter or environment variable to dynamically select the deployment color.
- Implement rollback logic in case the smoke test fails after deployment.

