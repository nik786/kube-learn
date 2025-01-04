

FireStore
----------
| #  | Feature                          | Description                                                                                           |
|----|----------------------------------|-------------------------------------------------------------------------------------------------------|
| 1  | **NoSQL Database**               | Firestore is a fully managed, serverless, NoSQL database designed for mobile, web, and server apps.    |
| 2  | **Document-Collection Model**    | Hierarchical structure of collections and documents, with documents storing key-value pairs.          |
| 3  | **Real-Time Synchronization**    | Supports real-time syncing, reflecting data changes immediately across connected clients.             |
| 4  | **Offline Support**              | Offers offline data persistence, allowing local read/write operations and syncing changes later.      |
| 5  | **Flexible Querying**            | Enables filtering, sorting, and paginating data, with indexed queries for high performance.           |
| 6  | **Horizontal Scalability**       | Automatically scales to handle large datasets and high-throughput applications.                       |
| 7  | **Serverless and Fully Managed** | No need to manage infrastructure; Google Cloud handles scaling, patching, and updates.                |
| 8  | **Strong Consistency**           | Ensures read operations return the latest committed data, avoiding stale data issues.                 |
| 9  | **Security with Firestore Rules**| Integrates with Firebase Authentication and supports fine-grained access control with security rules. |
| 10 | **Multi-Region and Single-Region Support** | Offers data redundancy and disaster recovery for high availability and low latency.               |



| #  | Description                                                                                         | Command                                       |
|----|-----------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 1  | Create a Firestore database.                                                                        | `gcloud firestore databases create --location=REGION` |
| 2  | List all Firestore databases.                                                                       | `gcloud firestore databases list`            |
| 3  | Export Firestore data to a Cloud Storage bucket.                                                    | `gcloud firestore export gs://[BUCKET_NAME]/[EXPORT_PREFIX] --collection-ids=[COLLECTION_ID]` |
| 4  | Import Firestore data from a Cloud Storage bucket.                                                  | `gcloud firestore import gs://[BUCKET_NAME]/[EXPORT_PREFIX]` |
| 5  | Delete a Firestore database.                                                                        | `gcloud firestore databases delete [DATABASE_ID] --location=REGION` |
| 6  | Enable the Firestore API.                                                                           | `gcloud services enable firestore.googleapis.com` |
| 7  | Disable the Firestore API.                                                                          | `gcloud services disable firestore.googleapis.com` |
| 8  | Deploy Firestore security rules from a file.                                                        | `gcloud firestore security-rules deploy firestore.rules` |
| 9  | Retrieve the current Firestore security rules.                                                      | `gcloud firestore security-rules list`       |
| 10 | List ongoing Firestore operations.                                                                  | `gcloud firestore operations list`           |
| 11 | Cancel a specific Firestore operation.                                                              | `gcloud firestore operations cancel [OPERATION_ID]` |
| 12 | Delete Firestore documents or collections using Firebase CLI.                                       | `firebase firestore:delete --collection [COLLECTION_PATH] --recursive` |
| 13 | View Firestore logs.                                                                                | `gcloud logging read 'resource.type="firestore_instance"'` |
| 14 | Check Firestore quotas.                                                                             | `gcloud firestore quotas describe`           |



GCP DataStore
--------------

| #  | Description                                                                                         |
|----|-----------------------------------------------------------------------------------------------------|
| 1  | **NoSQL Database**: Google Cloud Datastore is a fully managed, highly scalable NoSQL database service designed to handle structured and semi-structured data for web, mobile, and IoT applications. |
| 2  | **Document-Based Model**: Data is organized into entities, which are similar to rows in a traditional database, and each entity has properties, which act like fields or columns. |
| 3  | **Supports ACID Transactions**: Datastore supports ACID transactions, allowing you to perform multiple operations on multiple entities in a single, atomic transaction, ensuring data consistency. |
| 4  | **Strong and Eventual Consistency**: Datastore offers both strong consistency for queries within an entity group and eventual consistency for queries across multiple entity groups, providing flexibility for different use cases. |
| 5  | **Automatic Scaling**: Google Cloud Datastore automatically scales to handle large datasets and high traffic, distributing data across multiple servers to ensure performance and availability. |
| 6  | **Indexing and Querying**: Datastore automatically indexes the data, allowing for efficient querying. Users can perform complex queries, including filtering, sorting, and pagination, using GQL (Google Query Language), which is similar to SQL. |
| 7  | **Integration with Other Google Cloud Services**: Datastore integrates seamlessly with other GCP services like App Engine, Cloud Functions, BigQuery, and Google Cloud Firestore, making it easy to build and deploy applications. |
| 8  | **Schema-Less Nature**: Datastore is schema-less, meaning there is no rigid schema enforcement, allowing for flexibility in defining properties for entities and enabling easy changes to your data model over time. |
| 9  | **Security and Access Control**: Google Cloud Datastore uses Identity and Access Management (IAM) for managing permissions, allowing for fine-grained control over access to data at both the project and entity level. |
| 10 | **Firestore in Datastore Mode**: Cloud Datastore can be used in Firestore in Datastore mode, offering Datastore's features with Firestore's more modern capabilities like stronger consistency and improved querying. |


| #  | Description                                    | Command                                                                                     |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------|
| 1  | **Enable Cloud Datastore API**                | `gcloud services enable datastore.googleapis.com`                                           |
| 2  | **Create a Datastore Database**               | `gcloud datastore databases create --region=[REGION]`                                        |
| 3  | **List Datastore Entities**                   | `gcloud datastore entities list --namespace=[NAMESPACE] --kind=[KIND]`                       |
| 4  | **Export Datastore Data**                     | `gcloud datastore export gs://[BUCKET_NAME]/[EXPORT_PREFIX]`                                 |
| 5  | **Import Datastore Data**                     | `gcloud datastore import gs://[BUCKET_NAME]/[EXPORT_PREFIX]`                                 |
| 6  | **Delete a Datastore Entity**                 | `gcloud datastore entities delete --namespace=[NAMESPACE] --kind=[KIND] --id=[ENTITY_ID]`    |
| 7  | **Query Datastore Data**                      | `gcloud datastore entities lookup [ENTITY_KEY]`                                             |
| 8  | **List Datastore Indexes**                    | `gcloud datastore indexes list`                                                             |
| 9  | **Create a Datastore Index**                  | `gcloud datastore indexes create [INDEX_FILE]`                                              |
| 10 | **Delete a Datastore Index**                  | `gcloud datastore indexes cleanup [INDEX_FILE]`                                             |
| 11 | **View Datastore Quotas**                     | `gcloud datastore quotas describe`                                                          |
| 12 | **Cancel Datastore Operations**               | `gcloud datastore operations cancel [OPERATION_ID]`                                         |
| 13 | **List Datastore Operations**                 | `gcloud datastore operations list`                                                          |
| 14 | **Get Datastore Indexes Status**              | `gcloud datastore indexes describe`                                                        |



GCP BIGTABLES
--------------


| #  | Description                                        | Details                                                                                      |
|----|----------------------------------------------------|----------------------------------------------------------------------------------------------|
| 1  | **NoSQL Database for Large Workloads**             | Google Cloud Bigtable is a fully managed NoSQL database designed for large-scale, low-latency workloads. Optimized for high-throughput applications and scalable to petabytes. |
| 2  | **Column-Family Based Data Model**                 | Bigtable uses a wide-column store model, where columns are grouped into column families. Ideal for time-series, analytics, and IoT workloads. |
| 3  | **Low Latency and High Throughput**                | Provides low-latency read and write operations (single-digit milliseconds), suitable for real-time applications like ad tech, financial services, and monitoring systems. |
| 4  | **Horizontal Scalability**                         | Bigtable scales horizontally by adding nodes to handle growing workloads. Scales seamlessly from terabytes to petabytes without manual intervention. |
| 5  | **Integration with GCP Ecosystem**                 | Integrates with BigQuery, Dataflow, and AI/ML models for training and inference, providing a comprehensive ecosystem for data management and processing. |
| 6  | **Strong Consistency Model**                       | Ensures strong consistency for reads and writes. Once a write is acknowledged, subsequent reads reflect the latest data, crucial for transactional applications. |
| 7  | **Ideal for Time-Series Data**                     | Well-suited for storing time-series data such as monitoring metrics, sensor data, and financial data, providing efficient retrieval and storage. |
| 8  | **Managed and Fully Automated**                    | A fully managed service, where Google handles infrastructure management, replication, backups, and patching. |
| 9  | **Customizable Performance**                       | Allows dynamic scaling of nodes in a cluster to optimize performance or cost based on read/write demands. |
| 10 | **Built-In High Availability**                     | Provides high availability through multi-region replication, ensuring resilience and low-latency access across geographies. |

| #  | Description                                         | Command                                                                                         |
|----|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| 1  | **Authenticate**                                    | `gcloud auth login`                                                                               |
| 2  | **Set Active Project**                              | `gcloud config set project [PROJECT_ID]`                                                         |
| 3  | **Create a Bigtable Instance**                      | `gcloud bigtable instances create [INSTANCE_ID] --display-name=[DISPLAY_NAME] --instance-type=PRODUCTION --cluster=[CLUSTER_ID] --cluster-zone=[ZONE] --cluster-num-nodes=[NUM_NODES] --cluster-storage-type=ssd` |
| 4  | **List Bigtable Instances**                         | `gcloud bigtable instances list`                                                                 |
| 5  | **Describe a Bigtable Instance**                    | `gcloud bigtable instances describe [INSTANCE_ID]`                                                |
| 6  | **Update Bigtable Instance**                        | `gcloud bigtable instances update [INSTANCE_ID] --display-name=[NEW_DISPLAY_NAME]`               |
| 7  | **Delete a Bigtable Instance**                      | `gcloud bigtable instances delete [INSTANCE_ID]`                                                 |
| 8  | **Create a Bigtable Table**                         | `gcloud bigtable tables create [TABLE_ID] --instance=[INSTANCE_ID]`                              |
| 9  | **List Bigtable Tables**                            | `gcloud bigtable tables list --instance=[INSTANCE_ID]`                                           |
| 10 | **Delete a Bigtable Table**                         | `gcloud bigtable tables delete [TABLE_ID] --instance=[INSTANCE_ID]`                              |
| 11 | **Add Column Family to a Table**                    | `gcloud bigtable tables add-column-family [TABLE_ID] --instance=[INSTANCE_ID] --family=[COLUMN_FAMILY_NAME]` |
| 12 | **Check Bigtable Cluster States**                   | `gcloud bigtable clusters list --instance=[INSTANCE_ID]`                                         |
| 13 | **Create a Bigtable Cluster**                       | `gcloud bigtable clusters create [CLUSTER_ID] --instance=[INSTANCE_ID] --zone=[ZONE] --num-nodes=[NUM_NODES] --storage-type=ssd` |
| 14 | **Delete a Bigtable Cluster**                       | `gcloud bigtable clusters delete [CLUSTER_ID] --instance=[INSTANCE_ID]`                          |
| 15 | **Resize a Bigtable Cluster (Scale Up/Down)**       | `gcloud bigtable clusters update [CLUSTER_ID] --instance=[INSTANCE_ID] --num-nodes=[NEW_NUM_NODES]` |
| 16 | **Import Data into Bigtable (from Cloud Storage)**  | `gcloud bigtable backups create [BACKUP_ID] --instance=[INSTANCE_ID] --cluster=[CLUSTER_ID] --table=[TABLE_ID] --expiration-date=[DATE] --description="[DESCRIPTION]"` |
| 17 | **Export Data from Bigtable**                       | `gcloud bigtable backups delete [BACKUP_ID] --instance=[INSTANCE_ID] --cluster=[CLUSTER_ID]`     |
| 18 | **Check Bigtable Quotas**                           | `gcloud bigtable operations list --instance=[INSTANCE_ID]`                                       |
| 19 | **View Bigtable Instance IAM Policies**             | `gcloud bigtable instances get-iam-policy [INSTANCE_ID]`                                          |
| 20 | **Set Bigtable Instance IAM Policies**              | `gcloud bigtable instances set-iam-policy [INSTANCE_ID] policy.json`                             |



BigQuery
---------

| #  | Description                                             | Details                                                                                                                                                                                                                                                                 |
|----|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | **Serverless Data Warehouse**                          | Google BigQuery is a fully managed, serverless, scalable data warehouse that allows you to run SQL queries against large datasets without needing to manage infrastructure. Ideal for big data analytics.                                                                 |
| 2  | **Supports SQL Queries**                                | BigQuery uses Standard SQL (ANSI-compliant) for querying data, supporting complex joins, window functions, and aggregations.                                                                                                                                                |
| 3  | **Massive Scalability**                                 | BigQuery scales effortlessly to handle petabyte-scale data and can process vast amounts of data in seconds due to its distributed architecture.                                                                                                                            |
| 4  | **Separation of Storage and Compute**                   | BigQuery separates storage and compute resources, allowing users to scale each independently, paying only for the data stored and the compute resources (queries) used.                                                                                                    |
| 5  | **Real-Time Analytics**                                 | BigQuery supports real-time data ingestion using BigQuery Streaming or BigQuery Data Transfer Service, enabling near-real-time analytics on continuously updating datasets.                                                                                              |
| 6  | **Integration with GCP Ecosystem**                      | BigQuery integrates seamlessly with other Google Cloud services like Cloud Storage, Google Sheets, Dataflow, Pub/Sub, and AI/ML tools, facilitating powerful data pipelines and analysis solutions.                                                                     |
| 7  | **Automatic Backup and Restore**                        | BigQuery has automatic backups and restore capabilities through its Time Travel feature, enabling recovery of data up to 7 days in the past.                                                                                                                            |
| 8  | **Highly Secure and Compliant**                         | BigQuery provides IAM-based access control, default encryption, and supports compliance with standards like HIPAA, GDPR, and SOC.                                                                                                                                     |
| 9  | **Built-in Machine Learning (BigQuery ML)**             | BigQuery includes BigQuery ML, allowing users to create, train, and deploy machine learning models using simple SQL queries, without needing to move data to a separate environment.                                                                                   |
| 10 | **Flexible Pricing Model**                              | BigQuery offers on-demand pricing (pay-per-query) and flat-rate pricing for high-volume users. On-demand pricing charges based on the data processed by queries, while flat-rate pricing provides predictable costs.                                                       |
| 11 | **Common Use Cases**                                    | BigQuery is widely used for analytics use cases like business intelligence, customer analytics, log analysis, and data warehousing, due to its powerful querying capabilities and ability to handle massive datasets.                                                      |



| No. | Description                                                                                                     | Command                                                                                          |
|-----|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| 1   | Create a new BigQuery dataset.                                                                                  | `gcloud bigquery datasets create [DATASET_ID]`                                                    |
| 2   | List all BigQuery datasets in the active project.                                                               | `gcloud bigquery datasets list`                                                                   |
| 3   | Delete a BigQuery dataset.                                                                                      | `gcloud bigquery datasets delete [DATASET_ID]`                                                    |
| 4   | Create a BigQuery table in a dataset with a schema.                                                             | `gcloud bigquery tables create [DATASET_ID].[TABLE_ID] --schema=[SCHEMA_FILE]`                     |
| 5   | List all tables in a BigQuery dataset.                                                                          | `gcloud bigquery tables list --dataset=[DATASET_ID]`                                               |
| 6   | Delete a specific table from a dataset.                                                                         | `gcloud bigquery tables delete [DATASET_ID].[TABLE_ID]`                                            |
| 7   | Run a BigQuery SQL query using standard SQL.                                                                    | `gcloud bigquery query --use_legacy_sql=false "SELECT * FROM [DATASET_ID].[TABLE_ID] LIMIT 10"`     |
| 8   | Export a BigQuery table to Cloud Storage in CSV format.                                                          | `gcloud bigquery extract --destination_format=CSV [DATASET_ID].[TABLE_ID] gs://[BUCKET_NAME]/[FILE_NAME].csv` |
| 9   | Load data into a BigQuery table from Cloud Storage in CSV format.                                               | `gcloud bigquery load --source_format=CSV [DATASET_ID].[TABLE_ID] gs://[BUCKET_NAME]/[FILE_NAME].csv --schema=[SCHEMA_FILE]` |
| 10  | Show details of a BigQuery table.                                                                               | `gcloud bigquery tables describe [DATASET_ID].[TABLE_ID]`                                          |
| 11  | Show details of a BigQuery dataset.                                                                             | `gcloud bigquery datasets describe [DATASET_ID]`                                                  |
| 12  | Cancel a running BigQuery job.                                                                                  | `gcloud bigquery jobs cancel [JOB_ID]`                                                            |
| 13  | List all BigQuery jobs in the active project.                                                                   | `gcloud bigquery jobs list`                                                                       |
| 14  | Create a snapshot of a BigQuery table.                                                                          | `gcloud bigquery tables snapshot [SOURCE_DATASET_ID].[SOURCE_TABLE_ID] [TARGET_DATASET_ID].[TARGET_TABLE_ID]` |
| 15  | Set access control on a BigQuery dataset.                                                                       | `gcloud bigquery datasets add-iam-policy-binding [DATASET_ID] --member='user:[EMAIL]' --role='roles/bigquery.dataViewer'` |
| 16  | View access control for a BigQuery dataset.                                                                    | `gcloud bigquery datasets get-iam-policy [DATASET_ID]`                                            |
| 17  | Copy a BigQuery table from one dataset to another.                                                              | `gcloud bigquery cp [SOURCE_DATASET_ID].[SOURCE_TABLE_ID] [TARGET_DATASET_ID].[TARGET_TABLE_ID]`   |
| 18  | Create a partitioned table in BigQuery based on a time field.                                                   | `gcloud bigquery tables create [DATASET_ID].[TABLE_ID] --time_partitioning_field=[FIELD_NAME]`     |
| 19  | Enable table expiration on a BigQuery table.                                                                    | `gcloud bigquery tables update [DATASET_ID].[TABLE_ID] --expiration=[EXPIRATION_TIME_IN_SECONDS]`  |
| 20  | Create a BigQuery dataset with a specified location.                                                            | `gcloud bigquery datasets create [DATASET_ID] --location=[LOCATION]`                              |
| 21  | Check quotas and details for a BigQuery dataset.                                                                | `gcloud bigquery datasets describe [DATASET_ID]`                                                  |
| 22  | Export data from a BigQuery table to Cloud Storage in CSV format.                                               | `gcloud bigquery extract --destination_format=CSV [PROJECT_ID]:[DATASET_ID].[TABLE_ID] gs://[BUCKET_NAME]/[OUTPUT_FILE].csv` |
| 23  | Run a BigQuery query with specific conditions.                                                                  | `gcloud bigquery query --use_legacy_sql=false "SELECT column_name FROM [PROJECT_ID].[DATASET_ID].[TABLE_ID] WHERE condition"` |
| 24  | List BigQuery query jobs.                                                                                       | `gcloud bigquery jobs list --filter="jobType=QUERY"`                                               |
| 25  | Estimate query cost for a BigQuery query (dry run).                                                             | `gcloud bigquery query --dry_run --use_legacy_sql=false "SELECT * FROM [PROJECT_ID].[DATASET_ID].[TABLE_ID]"` |
| 26  | Describe a specific BigQuery table in a dataset.                                                                | `gcloud bigquery tables describe [TABLE_ID] --dataset=[DATASET_ID]`                                |
| 27  | Create a BigQuery view based on a query from an existing table.                                                 | `gcloud bigquery tables create [VIEW_ID] --view="SELECT * FROM [DATASET_ID].[TABLE_ID]"`            |


























