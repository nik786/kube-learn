

Article-01
-----------
### Gist: Kubernetes Ingress is not being deprecated


- Kubernetes **Ingress is not being deprecated** — only the community-led **Ingress-NGINX controller** retires in March 2026.
- Ingress remains supported, and many other controllers like Traefik, HAProxy, AWS LBC, and F5 NGINX continue to work.
- You can safely keep using Ingress; nothing in Kubernetes itself is going away.
- Gateway API is the future, so learn it — but no urgent migration or panic is needed.



Article-02
-----------
### Gist: Decoupling with SQS Queues

- SQS allows asynchronous task processing, reducing API wait times and improving scalability.  
- Incoming requests land in SQS while Lambda processes them independently and stores results in DynamoDB.  
- Failed messages are routed to a Dead-Letter Queue (DLQ) for retries and debugging.  
- Overall benefits: higher scalability, better resilience, and easier maintenance with no API blocking.  



k api-resources

Article-03
-----------
### Gist: API Best Practices

- Clear Resources Names
- Standard Methods
- Idempotency
- Api Versioning 
- Correct Status Codes
- Pagination
- Filtering and Sorting
- Security
- Rate Limiting
- Caching
- API Docs
- Pragmatic
