

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



OSI involvement:

HTTP/HTTPS → Layer 7
TLS → Layer 6
Session → Layer 5
TCP → Layer 4
IP Routing → Layer 3
Ethernet/VPC Fabric → Layer 2
Physical AWS Infra → Layer 1


Tier	Main OSI Layer
Presentation Tier	Layer 7
Application Tier	Layer 7
Data Tier	Layer 7 + Layer 4


Infrastructure networking between them uses:

Layer 1–4

Application Tier

Example:

ECS
EKS
Lambda
API Gateway
ALB

Mostly operates at:

OSI Layer	Usage
Layer 7	REST APIs, gRPC, backend logic
Layer 4	TCP/UDP load balancing

ALB:

Layer 7

NLB:

Layer 4


Data Tier

Example:

RDS
DynamoDB
Redis
MongoDB

Mostly operates at:

OSI Layer	Usage
Layer 7	SQL/NoSQL protocols
Layer 4	TCP connections

Example:

MySQL → TCP 3306
PostgreSQL → TCP 5432
Redis → TCP 6379



# Three-Tier Architecture vs OSI Layers

| OSI Layer | Three-Tier Relation | Why It Belongs | How It Works | Examples |
|---|---|---|---|---|
| Layer 7 – Application | Presentation / Application / Data Tier | Handles user-facing applications, APIs, and DB communication | Processes HTTP, REST APIs, SQL queries, DNS requests | Browser, ALB, ECS, API Gateway, RDS |
| Layer 6 – Presentation | Presentation Tier | Responsible for encryption, formatting, and encoding | Encrypts/decrypts TLS/SSL traffic and formats data | HTTPS, SSL/TLS, CloudFront |
| Layer 5 – Session | Presentation / Application Tier | Maintains active communication sessions between systems | Manages authentication sessions, cookies, persistent connections | Login Sessions, JWT, WebSocket |
| Layer 4 – Transport | Application / Data Tier | Provides reliable end-to-end communication between services | Uses TCP/UDP ports for data transfer and load balancing | TCP 443, MySQL 3306, NLB |
| Layer 3 – Network | All Tiers | Handles routing and IP communication across networks | Routes packets between subnets, VPCs, and networks | VPC Route Table, Transit Gateway |
| Layer 2 – Data Link | All Tiers | Enables communication between devices in same network segment | Transfers Ethernet frames using MAC addresses | ENI, Switch, MAC Address |
| Layer 1 – Physical | All Tiers | Provides physical infrastructure connectivity | Transfers raw bits through physical/network hardware | AWS Datacenter, Fiber Cable, NIC |




