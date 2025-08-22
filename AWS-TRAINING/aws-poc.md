
# AWS Proof of Concept (PoC) Ideas

This document outlines 8 AWS PoC ideas across governance, networking, containers, serverless, data, and AI.

- [aws-project-list](https://github.com/infra-ops/aws_poc.git)

[projects]

- [alexa-start-stop-instances](https://github.com/infra-ops/aws_poc/tree/master/ai_controller/alexa_ec2_handler)
- [push-notification](https://github.com/infra-ops/aws_poc/tree/master/push_notification)
- [ecs-handler](https://github.com/infra-ops/aws_poc/tree/master/ecs_handler)
- [ec2-handler](https://github.com/infra-ops/aws_poc/tree/master/ec2_handler)
- [ealstic-ip-manager](https://github.com/infra-ops/aws_poc/tree/master/elastic_ip_manager)
- 


---

## 1. Landing Zone (with Service Catalog & CloudFormation)
**PoC:** Build a multi-account landing zone using **AWS Control Tower**, extended with **Service Catalog** and **CloudFormation**.

- **Objective:**
  - Enable Control Tower to set up governance (accounts, guardrails, centralized logging).
  - Publish a **Service Catalog portfolio** (e.g., pre-approved VPC or EC2 stack defined in CloudFormation).
  - Allow teams to self-provision resources within guardrails.
- **Deliverable:**  
  2 accounts (Prod + Dev) with Service Catalog-provisioned VPCs and IAM guardrails.

---

## 2. VPC Lattice
**PoC:** Enable secure cross-VPC service-to-service communication with **VPC Lattice**.

- **Objective:** Deploy two microservices (Orders API in VPC A, Inventory API in VPC B) and connect via Lattice with IAM-based access controls.  
- **Deliverable:** Demonstrate traffic flow across VPCs without peering, TGW, or PrivateLink.




---

## 3. Transit Gateway
**PoC:** Centralized hub-and-spoke networking with **Transit Gateway**.

- **Objective:** Connect 3 VPCs (App, Data, Shared Services) using Transit Gateway for centralized routing.  
- **Deliverable:** Show traffic isolation and controlled routing policies from a single hub.

---

## 4. EKS with Karpenter
**PoC:** Elastic Kubernetes scaling using **Karpenter** on **Amazon EKS**.

- **Objective:** Deploy a sample workload (Nginx or stress pods) and validate Karpenter auto-provisions nodes with optimal instance types.  
- **Deliverable:** Cost-optimized scaling demo compared to Cluster Autoscaler.

---

## 5. App Mesh
**PoC:** Service mesh observability & routing with **App Mesh**.

- **Objective:** Deploy 2 microservices (Frontend + Backend) inside EKS, mesh-enabled with sidecars.  
- **Deliverable:** Show traffic routing (e.g., 50/50 split for canary), TLS encryption, and tracing via X-Ray/CloudWatch.

---

## 6. Serverless
**PoC:** Event-driven image processing pipeline.

- **Objective:**
  - S3 upload triggers Lambda.
  - Lambda resizes images & stores metadata in DynamoDB.
  - SNS sends notification to user.
- **Deliverable:** Fully serverless workflow demonstrating scalability and event-driven design.

---

## 7. Data Engineering (DynamoDB-based)
**PoC:** Real-time data ingestion and query pipeline with **DynamoDB**.

- **Objective:**
  - Ingest JSON data into DynamoDB via **Kinesis Firehose** or **Lambda**.
  - Use **Glue** to crawl DynamoDB tables for schema discovery.
  - Query enriched data using **Athena + DynamoDB connector**.
- **Deliverable:** DynamoDB as the serving layer + Athena queries for analysis, QuickSight dashboard for visualization.

---

## 8. AI Chatbot (Bedrock + SageMaker)
**PoC:** Build an **enterprise FAQ chatbot**.

- **Objective:**
  - Use **Amazon Bedrock** (LLM like Claude or Titan) for natural conversation.
  - Store documents in S3 + index embeddings in OpenSearch (vector DB).
  - Fine-tune embeddings using **SageMaker** for domain-specific Q&A.
- **Deliverable:** A simple web UI chatbot that answers company-specific FAQs using **retrieval-augmented generation (RAG)**.

---
