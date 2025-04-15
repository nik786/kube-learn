
**How can you integrate Amazon EKS with AWS IAM for Service Accounts (IRSA) to manage pod-level AWS permissions? Provide a use case.**

| **Point** | **Description** |
|-----------|-----------------|
| 1. **IRSA Overview** | AWS IAM for Service Accounts (IRSA) enables Kubernetes pods running on Amazon EKS to securely access AWS services using IAM roles. This eliminates the need for managing AWS credentials within the pod. |
| 2. **Service Account Creation** | Create a Kubernetes service account and associate it with an IAM role using an OpenID Connect (OIDC) identity provider. This role grants specific AWS permissions to pods that use this service account. |
| 3. **OIDC Identity Provider Setup** | Enable the OIDC identity provider in the EKS cluster to authenticate and authorize Kubernetes service accounts. The provider allows Kubernetes to map the service account to an IAM role. |
| 4. **IAM Role Association** | Attach IAM policies to the role that define the necessary AWS service permissions (e.g., S3 access, DynamoDB). The service account will inherit these permissions when pods use it. |
| 5. **Pod-Level Role Assignment** | When deploying pods, specify the Kubernetes service account in the pod specification. Pods using the service account inherit the IAM role's permissions, allowing them to interact with AWS services securely. |
| 6. **Use Case Example** | A pod running a data processing application requires access to an S3 bucket to read and write files. By associating the pod's service account with an IAM role that has the necessary S3 permissions, the pod can securely interact with the bucket without embedding AWS credentials. |
