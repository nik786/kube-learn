

# AWS Well-Architected Framework – 6 Pillars (One-Word Summary with Examples)

| Pillar       | One Word        | Example AWS Services                                      |
|--------------|------------------|------------------------------------------------------------|
| Security     | Protect           | IAM, KMS, AWS WAF, GuardDuty, Secrets Manager             |
| Reliability  | Recover           | Route 53, ELB, Auto Scaling, Amazon S3, CloudWatch Alarms |
| Performance  | Optimize          | EC2, Lambda, DynamoDB, CloudFront, Global Accelerator     |
| Cost         | Save              | Cost Explorer, Trusted Advisor, Spot Instances, S3 IA      |
| Operations   | Automate          | CloudWatch, CloudTrail, Systems Manager, CodePipeline      |
| Sustainability | Reduce          | Lambda, Graviton Instances, S3 Lifecycle, AWS Managed Services |



What is Three-Tier Architecture?

Three-tier architecture divides the application into three logical layers:

Presentation Tier – User interface (UI), often the web/mobile frontend.

Application (Logic) Tier – Backend business logic and API handling.

Data Tier – Databases and caching systems that store and manage data.


# Three-Tier Architecture Mapping

| Tier                    | Services Used                                                       | Role / Responsibility                                                |
|-------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| **Presentation Tier**   | Amazon S3 + CloudFront                                               | Hosts the React frontend and serves it globally via CDN             |
|                         | Amazon Route 53                                                      | DNS resolution for frontend URLs                                    |
|                         | API Gateway                                                          | Exposes API endpoints to frontend securely                          |
| **Application Tier**    | API Gateway + VPC Link + ALB                                         | Routes and balances traffic into ECS services                       |
|                         | Amazon ECS (Node.js Backend)                                         | Hosts business logic and handles API requests                       |
| **Data Tier**           | Amazon RDS                                                           | Stores relational (structured) data                                 |
|                         | Amazon DynamoDB                                                     | Stores NoSQL (unstructured or semi-structured) data                 |
|                         | Amazon ElastiCache (Redis)                                           | Speeds up data access via in-memory caching                         |

> 🧩 This architecture enables **scalability, modularity, and separation of concerns**. Each tier can be scaled or secured independently.


# Applying AWS 6 Pillars to Three-Tier Architecture

| Pillar          | Applied To (Tier)         | Best Practices / Strategies                                                                                  |
|-----------------|---------------------------|--------------------------------------------------------------------------------------------------------------|
| **Security**     | All Tiers                 | - Use IAM roles & policies with least privilege<br>- Enable encryption (S3, RDS, DynamoDB, Redis)<br>- Use WAF & Shield for ALB/API Gateway |
| **Reliability**  | Application & Data Tier   | - Use ALB with ECS for high availability<br>- RDS Multi-AZ deployment<br>- Use health checks and Auto Scaling |
| **Performance**  | All Tiers                 | - CloudFront for global frontend delivery<br>- Use Redis (ElastiCache) for low-latency access<br>- Use Graviton2 for ECS tasks (if compatible) |
| **Cost**         | All Tiers                 | - Use S3 lifecycle rules for frontend assets<br>- DynamoDB on-demand or provisioned with auto-scaling<br>- Spot Instances for ECS where feasible |
| **Operational Excellence** | All Tiers     | - Enable CloudWatch Logs and Metrics<br>- Use Systems Manager for config and patching<br>- CI/CD with CodePipeline or GitHub Actions |
| **Sustainability** | All Tiers              | - Use serverless where possible (e.g., Lambda)<br>- Use managed services (API Gateway, DynamoDB)<br>- Right-size compute and storage resources |



# Why It's Called Three-Tier Architecture

| Tier                    | Description                                                                 | Role / Responsibility                                              | Example Services                                                  |
|-------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------------|
| **Presentation Tier**   | The top layer that users interact with (UI/UX layer)                        | Displays UI, handles user input/output                             | Amazon S3 (static hosting), CloudFront (CDN), Route 53 (DNS)     |
| **Application Tier**    | Middle layer that processes data, business logic, and communication         | Executes backend logic, APIs, and orchestrates services            | Amazon ECS (Node.js), ALB, API Gateway, Lambda                   |
| **Data Tier**           | Bottom layer responsible for data storage and management                    | Stores and retrieves structured/unstructured data                  | Amazon RDS, DynamoDB, ElastiCache                                |

> Each tier is logically and often physically separated to ensure modularity, scalability, security, and ease of maintenance.


