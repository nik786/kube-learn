

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


| **Step** | **Command/Description**                                                                                             |
|----------|---------------------------------------------------------------------------------------------------------------------|
| 1.       | Deploy a service: `gcloud run deploy SERVICE_NAME --image IMAGE_URL --platform managed --region REGION`            |
| 2.       | List services: `gcloud run services list --platform managed --region REGION`                                        |
| 3.       | Get details of a service: `gcloud run services describe SERVICE_NAME --platform managed --region REGION`            |
| 4.       | Update a service: `gcloud run services update SERVICE_NAME --image IMAGE_URL --platform managed --region REGION`    |
| 5.       | Delete a service: `gcloud run services delete SERVICE_NAME --platform managed --region REGION`                      |
| 6.       | List revisions of a service: `gcloud run revisions list --service SERVICE_NAME --platform managed --region REGION`  |
| 7.       | Get logs of a service: `gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=SERVICE_NAME" --limit 100` |
| 8.       | Set environment variables: `gcloud run services update SERVICE_NAME --update-env-vars KEY1=VALUE1,KEY2=VALUE2 --platform managed --region REGION` |
| 9.       | Update service traffic splitting: `gcloud run services update-traffic SERVICE_NAME --to-revisions REVISION1=PERCENT1,REVISION2=PERCENT2 --platform managed --region REGION` |
| 10.      | Set maximum instances: `gcloud run services update SERVICE_NAME --max-instances NUMBER --platform managed --region REGION` |
| 11.      | Deploy a test service with revision suffix: `gcloud run deploy test --image hello --revision-suffix v1`             |
| 12.      | List all revisions: `gcloud run revision list`                                                                      |
| 13.      | Update traffic splitting: `gcloud run services update-traffic my-svc --to-revision=v2=10,v1=90`                     |








## Cloud SQL / Amazon RDS:
---------------------------

| **Feature**                    | **Description**                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| **Managed Database Service**   | Fully-managed database service supporting MySQL, PostgreSQL, and SQL Server, reducing operational overhead. |
| **Automatic Backups and High Availability** | Automatic backups, point-in-time recovery, and high availability configurations for data reliability and disaster recovery. |
| **Scalability**                | Horizontal and vertical scaling options with dynamic resource adjustments based on workload demands. |
| **Security**                   | Integrated with IAM for secure access control, data encryption at rest and in transit, and private IP support for secure connections. |
| **Replication**                | Supports read replicas and cross-region replication for better read performance and higher availability across regions. |
| **Monitoring and Logging**     | Integrates with Google Cloud Monitoring and Logging for performance insights, query execution analysis, and system health. |
| **No Maintenance Downtime**    | Ensures zero maintenance downtime with live migration support during upgrades and maintenance. |
| **Pricing**                    | Pay-as-you-go model based on CPU, memory, storage, and I/O usage, offering cost efficiency for both small and large workloads. |




```

## Cloud SQL Commands
-----------------------
# Cloud SQL
gcloud sql connect my-first-cloud-sql-instance --user=root --quiet

gcloud config set project glowing-furnace-304608

gcloud sql connect my-first-cloud-sql-instance --user=root --quiet

use todos

create table user (id integer, username varchar(30) );

describe user;

insert into user values (1, 'Ranga');

select * from user;


```

## Cloud Spanner / Amazon Aurora
----------------------------------

| **Feature**                    | **Description**                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| **Horizontally Scalable**      | Offers horizontal scaling across regions and continents without sacrificing consistency, making it ideal for massive scaling applications. |
| **Global Distribution with Strong Consistency** | The only globally distributed database service that provides strong, transactional consistency (ACID properties) across multiple regions for data integrity. |
| **Fully Managed**              | Google handles infrastructure management, including provisioning, replication, and backups, reducing operational overhead. |
| **High Availability and Uptime** | Guarantees 99.999% availability for multi-region instances, ensuring continuous uptime for mission-critical applications. |
| **Relational with SQL Support** | Supports ANSI SQL and provides a familiar relational SQL interface, enabling global scaling with traditional database queries. |
| **Automatic Sharding**         | Automatically shards data across multiple nodes and regions, maintaining low-latency access while evenly distributing load and data. |
| **Schema Changes Without Downtime** | Allows online schema changes without downtime, ensuring application availability during updates or migrations. |
| **Cost-Effective for Large Workloads** | Though more expensive than traditional databases, it offers cost-efficiency for large, globally distributed applications by reducing the complexity of database architecture. |


Spinnaker
----------
It is an open-source, continuous delivery (CD) platform developed by Netflix, designed to facilitate multi-cloud deployments.
It enables developers and DevOps teams to reliably deploy, manage, and scale applications 
across various cloud environments like AWS, Google Cloud, Microsoft Azure, and Kubernetes cluster.


| **Feature**                    | **Description**                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| **Multi-Cloud Support**        | Supports deployments to multiple cloud providers like AWS, Google Cloud, Microsoft Azure, Kubernetes, and others, providing flexibility for multi-cloud infrastructure management. |
| **Automated Deployment Pipelines** | Enables the creation of automated CI/CD pipelines for application deployment, including stages like image baking, running tests, staging deployment, and promotion to production. |
| **Integrated with Popular CI Tools** | Integrates seamlessly with CI tools like Jenkins, Travis CI, and GitLab, ensuring smooth transitions between CI and CD processes. |
| **Canary Deployments**         | Supports canary deployments, deploying new versions of an application to a small user subset first, minimizing the risk of large-scale failures. |
| **Blue/Green Deployments**     | Facilitates blue/green deployments, where the new version runs alongside the old version, enabling quick rollback in case of issues. |
| **Powerful Rollback Capabilities** | Tracks previous application versions and allows automatic or manual rollback to a previous version if the new deployment fails or encounters issues. |
| **Application Management Dashboard** | Provides a centralized dashboard to view and manage all applications, pipelines, and deployments, offering teams a unified place to monitor the health and progress of releases. |
| **Extensibility**              | Highly extensible, supporting custom stages and integrating with external tools for notifications (Slack), monitoring (Prometheus), and security (IAM, OAuth, etc.). |
| **Built-in Security**          | Integrates with identity and access management tools for fine-grained access control, and supports integration with Vault and other secret management tools. |




| **Step** | **Command/Description**                                                                                     |
|----------|-------------------------------------------------------------------------------------------------------------|
| 1.       | Install Spinnaker using Helm: `helm install spinnaker stable/spinnaker --namespace spinnaker`              |
| 2.       | Set up Google Cloud Project: `gcloud config set project [PROJECT_ID]`                                       |
| 3.       | Create a GKE Cluster for Spinnaker: `gcloud container clusters create [CLUSTER_NAME] --zone [COMPUTE_ZONE] --num-nodes=3` |
| 4.       | Grant IAM Roles to Spinnaker Service Account: `gcloud projects add-iam-policy-binding [PROJECT_ID] --member serviceAccount:[SPINNAKER_SERVICE_ACCOUNT] --role roles/storage.admin` |
| 5.       | Create a GCS Bucket for Spinnaker: `gcloud storage buckets create gs://[BUCKET_NAME] --project [PROJECT_ID]` |
| 6.       | Enable Required APIs: `gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com storage.googleapis.com artifactregistry.googleapis.com container.googleapis.com pubsub.googleapis.com` |
| 7.       | Deploy Spinnaker using the hal Command: `hal config provider gcp enable`                                    |
| 8.       | Add GCP Account: `hal config provider gcp account add my-google-account --project [PROJECT_ID] --json-path [PATH_TO_SERVICE_ACCOUNT_JSON]` |
| 9.       | Configure Docker or Artifact Registry: `hal config provider docker-registry account add my-gcr-account --address gcr.io --repositories [PROJECT_ID]/[IMAGE_NAME] --username _json_key --password-file [PATH_TO_SERVICE_ACCOUNT_JSON]` |
| 10.      | Deploy Spinnaker on GKE: `hal config deploy edit --type distributed --account-name my-k8s-account`<br>`hal deploy apply` |
| 11.      | Connect to Spinnaker UI: `kubectl port-forward -n spinnaker svc/spin-deck 9000:9000`<br>`kubectl port-forward -n spinnaker svc/spin-gate 8084:8084` |
| 12.      | Monitor Spinnaker Deployment Status: `kubectl get pods -n spinnaker`                                        |
| 13.      | Check Spinnaker Logs: `kubectl logs -f [POD_NAME] -n spinnaker`                                              |
| 14.      | Deploy New Configuration: `hal deploy apply`                                                                |
| 15.      | Configure Cloud Provider (GCP): `hal config provider gcp enable`                                            |















