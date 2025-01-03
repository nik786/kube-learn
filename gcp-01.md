

## CloudRun/Fargate
-------------

| **Feature**                    | **Description**                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| **Serverless Platform**        | Cloud Run is a fully managed, serverless computing platform that runs containerized applications without managing infrastructure. |
| **Container-Based Deployment** | Ensures portability and ease of deployment across different environments through containerization. |
| **Scalability**                | Automatically scales applications up or down based on demand.                                     |
| **Integration with Google Cloud Services** | Seamlessly integrates with services like Firestore, Cloud SQL, Pub/Sub, and more for building cloud-native applications. |
| **Fully Managed and GKE-Managed Options** | Available in fully managed mode or Cloud Run for Anthos, enabling container execution in Kubernetes clusters. |
| **Simple Request-Based Billing** | Billing is based on the exact amount of computing resources used while processing requests for cost-efficiency. |
| **Custom Domain Mapping**      | Supports custom domain mapping to use your own domain names for routing traffic to Cloud Run services. |
| **HTTP and HTTPS Support**     | Allows exposing containerized applications via HTTP/HTTPS endpoints to easily serve web-based applications and APIs. |
| **Security**                   | Automatically provides HTTPS encryption, integrates with Google Cloud IAM for access control, and supports VPC for network-level isolation when required. |



```
##Deploy a service:
gcloud run deploy SERVICE_NAME --image IMAGE_URL --platform managed --region REGION

##List services:
gcloud run services list --platform managed --region REGION

##Get details of a service:
gcloud run services describe SERVICE_NAME --platform managed --region REGION

##Update a service:
gcloud run services update SERVICE_NAME --image IMAGE_URL --platform managed --region REGION

##Delete a service:
gcloud run services delete SERVICE_NAME --platform managed --region REGION

##List revisions of a service:
gcloud run revisions list --service SERVICE_NAME --platform managed --region REGION

##Get logs of a service:
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=SERVICE_NAME" --limit 100

##Set environment variables:
gcloud run services update SERVICE_NAME --update-env-vars KEY1=VALUE1,KEY2=VALUE2 --platform managed --region REGION

##Update service traffic splitting:
gcloud run services update-traffic SERVICE_NAME --to-revisions REVISION1=PERCENT1,REVISION2=PERCENT2 --platform managed --region REGION

##Set maximum instances:
gcloud run services update SERVICE_NAME --max-instances NUMBER --platform managed --region REGION

gcloud run deploy test –image hello –revision-suffix v1

gcloud run revision list

gcloud run services update-traffic my-svc –to-revision=v2=10,v1=90


```


