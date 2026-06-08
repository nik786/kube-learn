36. What is Helm and how does it help in Kubernetes application management?

| # | Point | Description |
|---|-------|-------------|
| 1 | Package Manager | Helm is the package manager for Kubernetes. |
| 2 | Uses Charts | Applications are packaged as reusable Helm Charts. |
| 3 | Simplifies Deployment | Deploy complex applications with a single command. |
| 4 | Configuration Management | Manage environment-specific settings using values files. |
| 5 | Release Management | Supports upgrades, rollbacks, and version tracking. |
| 6 | Reusability & Automation | Promotes reusable templates and CI/CD automation. |

38. How do you manage secrets in Helm charts?
| # | Approach | Description |
|---|----------|-------------|
| 1 | Avoid Plain Text | Never store passwords or tokens directly in `values.yaml`. |
| 2 | Kubernetes Secrets | Store sensitive data in Kubernetes Secrets and reference them in Helm charts. |
| 3 | Encrypted Secrets | Use tools like SOPS or Helm Secrets to encrypt secret files in Git. |
| 4 | External Secret Stores | Integrate with secret managers such as :contentReference[oaicite:0]{index=0} or :contentReference[oaicite:1]{index=1}. |
| 5 | Secure Access | Restrict secret access using RBAC and least-privilege permissions. |
  

39. How do you roll back a Helm release?

| # | Step | Description |
|---|------|-------------|
| 1 | Check History | View release revisions using `helm history <release-name>`. |
| 2 | Identify Revision | Find the stable revision number to roll back to. |
| 3 | Roll Back Release | Run `helm rollback <release-name> <revision-number>`. |
| 4 | Verify Status | Check deployment status using `helm status <release-name>`. |
| 5 | Confirm Application | Validate pods, services, and application functionality after rollback. |

40. What are Helm hooks and how are they used?

| # | Point | Description |
|---|-------|-------------|
| 1 | What are Hooks? | Helm hooks are actions that run at specific points in a release lifecycle. |
| 2 | Common Hooks | `pre-install`, `post-install`, `pre-upgrade`, `post-upgrade`, and `pre-delete`. |
| 3 | Why Use Them? | Automate tasks before or after deployments. |
| 4 | Common Use Cases | Database migrations, backups, health checks, and notifications. |
| 5 | How They Work | Defined using annotations in Kubernetes manifests, e.g., `helm.sh/hook: pre-install`. |

41. How do you handle multi-environment Helm chart deployments?

| # | Approach | Description |
|---|----------|-------------|
| 1 | Reusable Helm Chart | Use one Helm chart for all environments. |
| 2 | Environment Values | Keep separate values files for Dev, QA, and Prod. |
| 3 | Helmfile | Manage all releases and environments centrally. |
| 4 | GitOps | Deploy automatically from Git repositories. |
| 5 | CI/CD | Automate validation and deployments. |
