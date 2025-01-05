
| **Feature**                     | **Description**                                                                                                                                         |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Asynchronous Messaging Service** | Fully managed, real-time messaging service for sending and receiving messages asynchronously between independent systems.                             |
| **Publisher-Subscriber Model**  | Follows the publish-subscribe messaging pattern where publishers send messages to topics and subscribers receive messages from those topics.             |
| **Scalability**                  | Horizontally scalable to handle millions of messages per second globally, supporting small-scale applications to massive data streams.                   |
| **Push and Pull Delivery Models**| Supports two models: <br>**Push**: Messages are pushed to a subscriber’s endpoint (e.g., HTTP server). <br>**Pull**: Subscribers pull messages at their own pace. |
| **Durable Message Storage**      | Messages are persisted until acknowledged by subscribers, ensuring no loss. Default retention period is 7 days, customizable as needed.                  |
| **Real-Time Event-Driven Architectures** | Enables event-driven architectures, suitable for event logging, stream processing, IoT data collection, and microservices communication.             |
| **Guaranteed Message Delivery**  | Provides at-least-once delivery with retries and acknowledgment mechanisms. Unacknowledged messages are retried.                                        |
| **Global, Low-Latency Infrastructure** | Global service with low-latency message delivery, enabling routing and processing across regions with minimal delay.                                   |
| **Integration with Google Cloud Services** | Seamlessly integrates with Cloud Functions, Cloud Dataflow, BigQuery, Cloud Run, App Engine, and more for event-driven workflows.                     |
| **Common Use Cases**             | Log streaming, event distribution, microservices communication, real-time analytics, providing a reliable and scalable messaging backbone.              |



| **#** | **Description**                                                                                              | **Command**                                       |
|-------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| 1     | Create a Pub/Sub topic.                                                                                      | `gcloud pubsub topics create [TOPIC_NAME]`       |
| 2     | List all Pub/Sub topics.                                                                                     | `gcloud pubsub topics list`                      |
| 3     | Delete a specific Pub/Sub topic.                                                                             | `gcloud pubsub topics delete [TOPIC_NAME]`       |
| 4     | Create a Pub/Sub subscription for a topic.                                                                   | `gcloud pubsub subscriptions create [SUBSCRIPTION_NAME] --topic=[TOPIC_NAME]` |
| 5     | List all Pub/Sub subscriptions.                                                                              | `gcloud pubsub subscriptions list`               |
| 6     | Pull messages from a subscription (limited to 10 and auto-acknowledge).                                      | `gcloud pubsub subscriptions pull [SUBSCRIPTION_NAME] --limit=10 --auto-ack` |
| 7     | Delete a specific subscription.                                                                              | `gcloud pubsub subscriptions delete [SUBSCRIPTION_NAME]` |
| 8     | Publish a message to a Pub/Sub topic.                                                                        | `gcloud pubsub topics publish [TOPIC_NAME] --message="[MESSAGE_TEXT]"` |
| 9     | View detailed information about a subscription.                                                              | `gcloud pubsub subscriptions describe [SUBSCRIPTION_NAME]` |
| 10    | Modify a subscription’s acknowledgment deadline.                                                             | `gcloud pubsub subscriptions update [SUBSCRIPTION_NAME] --ack-deadline=[SECONDS]` |
| 11    | Create a push subscription with a specified endpoint.                                                        | `gcloud pubsub subscriptions create [SUBSCRIPTION_NAME] --topic=[TOPIC_NAME] --push-endpoint=[ENDPOINT_URL]` |
| 12    | List messages in a topic via Pub/Sub Lite.                                                                   | `gcloud pubsub lite-subscriptions list --location=[ZONE] --topic=[TOPIC_NAME]` |
| 13    | Seek a subscription to a specific timestamp.                                                                 | `gcloud pubsub subscriptions seek [SUBSCRIPTION_NAME] --time=[TIMESTAMP]` |
| 14    | Modify the push configuration of a subscription.                                                             | `gcloud pubsub subscriptions update [SUBSCRIPTION_NAME] --push-endpoint=[NEW_ENDPOINT_URL]` |
| 15    | Set the IAM policy for a topic.                                                                              | `gcloud pubsub topics set-iam-policy [TOPIC_NAME] policy.json` |
| 16    | View the IAM policy of a topic.                                                                              | `gcloud pubsub topics get-iam-policy [TOPIC_NAME]` |
| 17    | Simulate publishing a message with attributes (for testing).                                                 | `gcloud pubsub topics publish [TOPIC_NAME] --message="Test message" --attribute="key=value"` |
| 18    | Create a snapshot of a subscription.                                                                         | `gcloud pubsub snapshots create [SNAPSHOT_NAME] --subscription=[SUBSCRIPTION_NAME]` |
| 19    | Delete a Pub/Sub snapshot.                                                                                   | `gcloud pubsub snapshots delete [SNAPSHOT_NAME]` |
| 20    | Seek to a snapshot in a subscription.                                                                        | `gcloud pubsub subscriptions seek [SUBSCRIPTION_NAME] --snapshot=[SNAPSHOT_NAME]` |





| **Feature/Capability**                           | **Description**                                                                                                                                                       |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unified Batch and Stream Processing**         | Dataflow provides a unified model for both batch and stream processing, enabling users to write a single pipeline for both types of data processing.                  |
| **Apache Beam Integration**                     | Built on Apache Beam, allowing developers to create data pipelines that can run on various distributed processing engines, including Dataflow.                        |
| **Fully Managed Service**                       | Abstracts infrastructure management, so users can focus on writing pipelines instead of managing clusters, networking, or scaling.                                    |
| **Autoscaling**                                  | Automatically scales compute resources up or down based on workload, optimizing performance and cost.                                                                |
| **Real-Time Processing**                        | Native support for stream processing, making it ideal for real-time analytics and pipelines that process data as it arrives.                                          |
| **Fault Tolerance**                              | Built-in fault tolerance and stateful processing ensure data consistency and recovery in case of failures.                                                           |
| **Event-Time Processing**                       | Supports event-time processing, ensuring accurate results in stream workflows, even with out-of-order or late-arriving events.                                       |
| **Support for Windowing and Triggers**          | Provides powerful windowing and triggering mechanisms for time-based aggregations and streaming data analysis.                                                        |
| **Security and Compliance**                     | Integrates with Google Cloud's security features, including data encryption (at rest and in transit), IAM policies, and compliance certifications like HIPAA and GDPR.|
| **Common Use Cases**                             | Ideal for ETL pipelines, real-time analytics, log analysis, fraud detection, IoT data processing, and machine learning data preparation.                              |




| **Feature/Capability**                  | **Description**                                                                                                                                               |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Managed Hadoop and Spark**            | Provides fully managed Hadoop and Spark clusters, enabling users to process and analyze large datasets without complex cluster management.                     |
| **Fast Cluster Provisioning**           | Clusters can be provisioned in as little as 90 seconds, enabling quick setup for both short-lived jobs and persistent workloads.                              |
| **Scalability and Flexibility**         | Allows dynamic scaling of clusters by adding or removing nodes based on workload demands, ensuring optimal performance and cost management.                   |
| **Cost-Effective**                      | Charges per second of use, with the ability to use preemptible VMs, making it a cost-effective solution for big data processing.                              |
| **Open-Source Ecosystem**               | Supports open-source big data tools like Hadoop, Spark, Hive, Pig, and Presto, allowing users to leverage familiar tools without adapting to proprietary systems.|
| **Integrated with Google Cloud**        | Seamlessly integrates with GCP services like Cloud Storage, BigQuery, Bigtable, and Stackdriver for end-to-end data pipelines and analytics workflows.         |
| **Customizability**                     | Allows users to configure and customize clusters with initialization actions, enabling installation of additional libraries or software as needed.            |
| **Job and Workflow Automation**         | Supports automation of job workflows, including recurring jobs, chaining, and event-triggered pipelines, simplifying big data operations and pipeline management.|
| **Data Security**                       | Offers encryption of data in transit and at rest, IAM integration, and support for VPC Service Controls to secure data access.                                |
| **Common Use Cases**                    | Used for data mining, machine learning, ETL processes, log analysis, and large-scale data processing with distributed frameworks like Spark or Hadoop.         |



| **Feature/Capability**                        | **Description**                                                                                                                                                   |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fully Managed Kubernetes Service**          | GKE is a managed Kubernetes service by Google Cloud that simplifies the deployment, management, and scaling of containerized applications.                        |
| **High Availability**                         | Provides high availability with multi-zonal and regional clusters, ensuring redundancy and failover across zones or regions.                                      |
| **Automatic Scaling**                         | Supports horizontal pod autoscaling, vertical pod autoscaling, and cluster autoscaling, adjusting resources dynamically based on workload demands.                |
| **Integrated with Google Cloud**              | Integrates seamlessly with services such as Cloud Logging, Cloud Monitoring, Cloud Build, and IAM, offering enhanced operational capabilities.                   |
| **Cost Optimization**                         | Offers optimized cost management through preemptible VMs and auto-provisioning of resources, making it suitable for both production and development workloads.    |
| **Istio and Anthos Support**                  | Supports Istio for service mesh functionality, offering advanced networking, security, and observability. Part of Anthos for hybrid and multi-cloud deployments.  |
| **Security and Compliance**                   | Includes features like GKE Sandbox, node auto-upgrades, role-based access control (RBAC), and workload identity for enhanced security and compliance.             |
| **Multi-Cluster Management**                  | Enables deployment and management of multiple clusters across regions, achieving high availability, disaster recovery, and distributed computing needs.           |
| **Support for Custom and Prebuilt Machine Types** | Supports a wide range of machine types, allowing customization of nodes for application requirements, including custom CPU, memory configurations, and GPU support for ML workloads. |
| **Serverless Kubernetes (GKE Autopilot)**     | Offers an Autopilot mode, abstracting most infrastructure management, focusing on application deployment and scaling without directly managing nodes.             |



| **#** | **Task**                             | **Command**                                                                                                                                                                    |
|-------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | **Create a Regional (High Availability) GKE Cluster** | `gcloud container clusters create [CLUSTER_NAME] \`<br>`  --region [REGION] \`<br>`  --num-nodes 3 \`<br>`  --node-locations [ZONE_1],[ZONE_2],[ZONE_3] \`<br>`  --enable-autoscaling \`<br>`  --min-nodes 1 \`<br>`  --max-nodes 5 \`<br>`  --enable-ip-alias \`<br>`  --enable-private-nodes \`<br>`  --master-ipv4-cidr 172.16.0.0/28 \`<br>`  --enable-stackdriver-kubernetes` |
| 2     | **Get Credentials for the Cluster** | `gcloud container clusters get-credentials [CLUSTER_NAME] --region [REGION]`                                                                                                 |
| 3     | **Enable Node Auto-upgrades and Auto-repair** | `gcloud container clusters update [CLUSTER_NAME] \`<br>`  --region [REGION] \`<br>`  --enable-autoupgrade \`<br>`  --enable-autorepair`                                      |
| 4     | **Scale the Cluster Nodes**         | `gcloud container clusters resize [CLUSTER_NAME] \`<br>`  --region [REGION] \`<br>`  --num-nodes [NODE_COUNT]`                                                              |
| 5     | **Upgrade the Cluster’s Control Plane** | `gcloud container clusters upgrade [CLUSTER_NAME] \`<br>`  --region [REGION] \`<br>`  --master`                                                                             |
| 6     | **Set Maintenance Window**          | `gcloud container clusters update [CLUSTER_NAME] \`<br>`  --region [REGION] \`<br>`  --maintenance-window "22:00-00:00"`                                                   |
| 7     | **Monitor the Cluster Using Stackdriver** | `gcloud container clusters update [CLUSTER_NAME] \`<br>`  --region [REGION] \`<br>`  --enable-stackdriver-kubernetes`                                                      |
| 8     | **Set Node Pool Auto-scaling**      | `gcloud container clusters update [CLUSTER_NAME] \`<br>`  --region [REGION] \`<br>`  --enable-autoscaling \`<br>`  --min-nodes 1 \`<br>`  --max-nodes 5 \`<br>`  --node-pool [NODE_POOL_NAME]` |
| 9     | **Delete the Cluster**              | `gcloud container clusters delete [CLUSTER_NAME] --region [REGION]`                                                                                                         |






















