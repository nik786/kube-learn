



```

User Request (https://www.ag.com)
↓
Route 53 (routes to CloudFront)
↓
CloudFront (https://d3w0a8frp52y1k.cloudfront.net)
↓ (Uses custom SSL certificate: devapp.ag.com)
CloudFront fetches static content from S3 bucket
↓
S3 Bucket (contains .env file with backend API Gateway endpoint: https://ftyx5iwztk.execute-api.ap-south-1.amazonaws.com)
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
