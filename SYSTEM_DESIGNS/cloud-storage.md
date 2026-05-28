# Cloud CCTV Storage Platform Architecture

## Overview

This architecture is designed to build a:

* Low-cost CCTV cloud storage platform
* Scalable video ingestion system
* Motion/event-based archival solution
* AWS-native surveillance backend
* Future-ready AI-enabled NVR platform

The platform leverages:

* MediaMTX for stream ingestion and distribution
* Frigate for motion/object detection
* Amazon S3 for event clip archival
* Glacier for long-term cold storage
* ECS EC2 ARM infrastructure for cost optimization

---

# High-Level Architecture

```text
Frontend (Next.js)
      |
AWS Amplify Hosting
      |
Cloudflare
      |
Public ALB
      |
ECS EC2 ARM Cluster
------------------------------------------------
| Go API Service                               |
| MediaMTX Service                             |
| Frigate Service                              |
------------------------------------------------
      |
Motion / Object Detection
      |
Event Clip & Snapshot Generation
      |
Upload Event Clips to S3
      |
S3 Lifecycle Policies
      |
Glacier / Deep Archive
```

---

# Component Breakdown

## 1. Frontend Layer

### Technology

* Next.js
* AWS Amplify Hosting
* Cloudflare CDN/WAF

### Responsibilities

* User dashboard
* Camera management
* Playback UI
* Event browsing
* Authentication
* Notifications

### Why Amplify?

* Easy CI/CD
* Cheap hosting
* Managed frontend deployment
* Automatic SSL

### Why Cloudflare?

* CDN acceleration
* DDoS protection
* WAF capabilities
* Bandwidth optimization

---

# 2. Load Balancer Layer

## Public ALB

### Responsibilities

* Route external traffic
* TLS termination
* Health checks
* ECS service integration

### Why Public ALB?

* Simpler architecture
* Avoid NAT Gateway cost
* Lower operational overhead
* Cost efficient for MVP

---

# 3. ECS EC2 ARM Cluster

## Runtime Platform

* Amazon ECS
* EC2 launch type
* ARM/Graviton instances

### Recommended Instances

| Purpose                 | Recommended Instance |
| ----------------------- | -------------------- |
| Small deployment        | t4g.medium           |
| Medium workload         | m7g.large            |
| Heavy AI/video workload | c7g.large            |

### Why ARM/Graviton?

* Lower AWS cost
* Better price-performance ratio
* Excellent Go runtime efficiency
* Efficient video processing

---

# 4. Go API Service

## Responsibilities

* User authentication
* Camera registration
* Playback APIs
* Event metadata APIs
* Tenant management
* S3 signed URL generation
* Retention policy management

## Recommended Stack

* Go
* Gin/Fiber
* JWT Authentication

---

# 5. MediaMTX Service

## Responsibilities

* RTSP ingest
* HLS generation
* WebRTC streaming
* Stream relay
* Multi-camera stream management

## Why MediaMTX?

* Lightweight
* High-performance
* RTSP/WebRTC/HLS support
* Cloud-native friendly
* Efficient for CCTV workloads

---

# 6. Frigate Service

## Responsibilities

* Motion detection
* Object detection
* Event generation
* Snapshot generation
* Smart recording logic

## Recommended Recording Strategy

* Motion-based recording only
* Object-triggered clip generation
* Snapshot extraction

## Benefits

* Massive storage savings
* Intelligent event filtering
* Lower S3 storage cost
* Reduced Glacier usage

---

# 7. Motion/Object Detection Pipeline

## Flow

```text
Camera Stream
      |
MediaMTX
      |
Frigate Analysis
      |
Motion/Object Event
      |
Clip Generation
      |
Upload to S3
```

---

# 8. Amazon S3 Storage

## Purpose

* Event clip archival
* Snapshot storage
* Playback source
* Durable object storage

## Recommended Bucket Structure

```text
s3://cctv-platform/
   tenant-id/
      camera-id/
         YYYY/MM/DD/HH/
```

---

# 9. S3 Lifecycle Policies

## Recommended Lifecycle Rules

| Age        | Storage Class             |
| ---------- | ------------------------- |
| 0–7 days   | S3 Standard               |
| 7–30 days  | Standard-IA               |
| 30–90 days | Glacier Instant Retrieval |
| 90+ days   | Deep Archive              |

## Benefits

* Automatic cost optimization
* Long-term archival
* Minimal operational management

---

# 10. Glacier / Deep Archive

## Purpose

* Long-term CCTV retention
* Regulatory compliance
* Extremely low-cost storage

## Best Practice

* Archive only event clips
* Avoid continuous raw stream archival initially

---

# Recommended Future Enhancements

## 1. SQS + Lambda Workers

### Future Architecture

```text
S3 Upload
      |
S3 Event Notifications
      |
SQS
      |
Lambda Workers
```

### Use Cases

* Thumbnail generation
* AI indexing
* Notifications
* Metadata enrichment
* Analytics pipeline

---

# 2. MQTT Integration

## Suggested Architecture

```text
Frigate
      |
MQTT Broker
      |
Go APIs / Workers
```

## Benefits

* Real-time alerts
* WebSocket notifications
* Event-driven automation
* Future smart-home integrations

---

# 3. AI Expansion

Future capabilities:

* Face recognition
* License plate recognition
* Anomaly detection
* Generative AI summaries
* Bedrock/SageMaker integration

---

# Key Cost Optimization Strategies

## Most Important Optimization

### Upload ONLY motion/object event clips

This reduces:

* S3 storage cost
* Bandwidth usage
* Glacier archival cost
* PUT request count

Potential savings:

* 80–95% reduction in storage usage

---

# Operational Best Practices

## Recommended

* Separate ECS services
* ARM/Graviton instances
* Motion-based recording
* Lifecycle-based archival
* Snapshot generation
* S3 prefix partitioning

## Avoid

* Continuous 24x7 uploads initially
* Giant video files
* Single monolithic ECS task
* Uploading raw streams directly forever

---

# Final Architecture Summary

This architecture provides:

* Low AWS operational cost
* High scalability
* Cloud-native design
* Intelligent event filtering
* Long-term archival capability
* Future AI extensibility
* Production-grade CCTV platform foundation

The design is optimized for:

* MVP development
* Mid-scale production deployments
* Cost-efficient surveillance storage
* Modern cloud NVR workloads

