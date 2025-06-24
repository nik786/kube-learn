
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
