

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










