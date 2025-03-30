

- [auto-mode-blog-01](https://devopslearning.medium.com/aws-eks-auto-mode-a-game-changer-or-just-hype-my-unbiased-take-18de17c4484a)

## AWS EKS Auto Mode Overview

| Category          | Description |
|------------------|-------------|
| **Feature**       | EKS Auto Mode automates cluster creation, scaling, security, and OS patching using BottleRocket OS. It provisions compute resources on demand without needing detailed manual configurations. |
| **Pros**          | - One-click cluster setup<br>- Automatic scaling and healing<br>- Cost-optimized resource allocation<br>- Enhanced security with no SSH access<br>- Managed updates and monitoring |
| **Cons**          | - No direct access to nodes (SSH/SSM disabled)<br>- Limited UI-based customization<br>- Must use CLI/API for advanced config<br>- Only supports Kubernetes 1.29+ |
| **Cost**          | Potential cost savings via efficient scaling, but pricing depends on usage. Less control may lead to over-provisioning if not monitored well. |
| **When to Use**   | Ideal for teams wanting fast, hands-off Kubernetes deployments, limited ops teams, startups, and dev/test environments. Not ideal if full node access or advanced tuning is needed. |

👉 [Read the full article here](https://devopslearning.medium.com/aws-eks-auto-mode-a-game-changer-or-just-hype-my-unbiased-take-18de17c4484a)
