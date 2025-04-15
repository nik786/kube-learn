

What are the security features of Amazon EKS?
-----------------------------------------------
## Security Features of Amazon EKS

| **Security Feature**           | **Description**                                                                                               |
|---------------------------------|---------------------------------------------------------------------------------------------------------------|
| **IAM for Service Accounts**    | Use AWS Identity and Access Management (IAM) roles for Kubernetes service accounts to securely grant access to AWS services. |
| **Pod Security Policies**       | Enforce security standards and define restrictions for pods, such as preventing privileged containers or access to host resources. |
| **Network Policies**            | Control traffic flow between Kubernetes pods by using network policies to define which pods can communicate with each other. |
| **Encryption at Rest and in Transit** | Encrypt data at rest using AWS Key Management Service (KMS) and secure data in transit with TLS encryption between EKS components. |
| **Cluster and Node Security**   | Leverage security groups, VPCs, and private subnets to secure EKS nodes and control access to the Kubernetes control plane. |
