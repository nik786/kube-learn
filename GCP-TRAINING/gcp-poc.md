GCP Architecture Overview
Here’s how it all connects:

1️⃣ Frontend (UI)

React App hosted on Cloud Storage + Cloud CDN.
DNS managed by Cloud DNS.
SSL/TLS handled by Certificate Manager.
2️⃣ Backend (API)

Requests go through GCP API Gateway.
API Gateway routes traffic to Cloud Run (Fargate alternative).
Internal Load Balancer distributes traffic between backend services.
3️⃣ Database (Data Layer)

Cloud SQL (PostgreSQL Aurora alternative) stores data.
Secret Manager secures credentials.
4️⃣ Security & Monitoring

Cloud Armor (WAF) protects against attacks.
IAM policies secure access.
Operations Suite (Stackdriver) monitors logs and metrics.
