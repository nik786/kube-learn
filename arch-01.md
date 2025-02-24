

Mermaid

PlantUML

Graphviz

Ascii

```

User Request (https://www.ag.com)
↓
Route 53 (routes to CloudFront)
↓
CloudFront (https://d3w0a8frp52y1k.cloudfront.net)
↓ (Uses custom SSL certificate: devapp.ag.com)
CloudFront fetches static content from S3 bucket
↓
S3 Bucket (contains .env file with backend API Gateway
endpoint: https://ftyx5iwztk.execute-api.ap-south-1.amazonaws.com)
↓
API Gateway (routes to the internal ALB through VPC Link)
↓
Internal ALB (internal-ag-alb-dev-14847871.ap-south-1.amazonaws.com)
↓
ECS Service (runs the backend Node.js service)
↓
Backend Node.js Application
↓
RDS (retrieves and stores data)
↓
Secrets Manager (fetches necessary secrets for the backend app)

```

```

                                 +-------------------+
                                 |     User Request  |
                                 |   (https://www.ag.com) |
                                 +-------------------+
                                           ↓
                                    +------------------+
                                    |    Route 53      |
                                    | (DNS Routing)    |
                                    +------------------+
                                           ↓
                           +-------------------------------+
                           |         CloudFront            |
                           | (https://d3w0a8frp52y1k.cloudfront.net) |
                           | (Custom SSL: devapp.ag.com)   |
                           +-------------------------------+
                                           ↓
                          +---------------------------------+
                          |      S3 Bucket                 |
                          | (Contains .env with API Gateway)|
                          +---------------------------------+
                                           ↓
                       +-----------------------------------------------+
                       |     API Gateway                              |
                       | (https://ftyx5iwztk.execute-api.ap-south-1)  |
                       +-----------------------------------------------+
                                           ↓
                       +----------------------------------------------+
                       |    Internal ALB                            |
                       | (internal-ag-alb-dev-14847871.ap-south-1.elb)|
                       +----------------------------------------------+
                                           ↓
                       +----------------------------------------------+
                       |         ECS Service                         |
                       | (Backend Node.js Application)               |
                       +----------------------------------------------+
                                           ↓
                       +----------------------------------------------+
                       |     Backend Node.js Application            |
                       | (API Connected to RDS and Secrets Manager)  |
                       +----------------------------------------------+
                                           ↓
                       +----------------------------------------------+
                       |               RDS                           |
                       | (Database for storing data)                 |
                       +----------------------------------------------+
                                           ↓
                       +----------------------------------------------+
                       |           Secrets Manager                   |
                       | (Fetching secrets for backend app)          |
                       +----------------------------------------------+

```

```mermaid
graph TD
    A[User Request] --> B[Route 53]
    B --> C[CloudFront]
    C --> D[S3 Bucket<br>Contains .env with API Gateway]
    D --> E[API Gateway]
    E --> F[Internal ALB]
    F --> G[ECS Service<br>Backend Node.js App]
    G --> H[Backend Node.js Application]
    H --> I[RDS<br>Stores Data]
    H --> J[Secrets Manager<br>Fetches Secrets]
```





```mermaid
graph TD
    A[User Request] --> B[Cloud DNS]
    B --> C[Cloud CDN]
    C --> D[Cloud Storage<br>Contains .env with API Gateway]
    D --> E[API Gateway]
    E --> F[Internal Load Balancer]
    F --> G[Cloud Run<br>Backend Node.js App]
    G --> H[Backend Node.js Application]
    H --> I[Cloud SQL<br>Stores Data]
    H --> J[Secret Manager<br>Fetches Secrets]


```



