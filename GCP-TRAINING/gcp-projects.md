# 🚀 GCP Serverless & Microservices Project Ideas

A curated list of **hands-on project ideas** for building serverless, containerized, and secure architectures on **Google Cloud Platform (GCP)**.  
Includes **IAM, security, networking, and multi-tier architectures**.

---

## 📂 Repo
- [gcp-projects](https://github.com/infra-ops/gcp_poc.git)

---

## 📸 1. Serverless Image Processing Pipeline
**Services**: Cloud Storage, Cloud Run Function, Pub/Sub  
**Idea**:  
- Cloud Run Function triggered when an image is uploaded to Cloud Storage.  
- Pub/Sub publishes event and metadata is stored in the Cloud Storage bucket.  

🔗 [serverless-image-processing-pipeline](https://github.com/infra-ops/gcp_poc/tree/main/serverless-image-processing-pipeline)

---

## 📧 2. Serverless Email Notifier
**Services**: Cloud Scheduler, Cloud Functions, Gmail API  
**Idea**:  
- A daily scheduled function sends reminders (weather, news, or Google Sheets tasks).  

---

## 🌍 3. Multi-AZ Deployment on a Single Cluster
**Tech**: GKE, Config Sync (GitOps)  
**Idea**:  
- Use a single GKE cluster in a single region that spans multiple availability zones (AZs).  
- Create separate namespaces (e.g., `az-a`, `az-b`, `az-c`) to simulate deployments across AZs.  
- Deploy the **product catalog API** with slight config variations (replicas, affinity/anti-affinity, node selectors).  

**Learning**: Workload distribution across AZs, GitOps-driven config management, failover simulation.  

---

## 🔄 4. Mini CI/CD with ArgoCD + GKE
**Tech**: GKE, Artifact Registry, ArgoCD (lighter than Spinnaker)  
**Idea**:  
- Build & push a Node.js API to Artifact Registry.  
- Auto-deploy via ArgoCD with canary strategy (e.g., 80/20 traffic split using Kubernetes Service).  

**Learning**: GitOps CD + progressive rollout.  

---

## 🔐 5. Lightweight Service Mesh Security
**Tech**: GKE, Istio (or Anthos Service Mesh lite install)  
**Idea**:  
- Deploy **orders** and **payments** microservices.  
- Enable **mTLS** within the mesh.  
- Use built-in Istio dashboard / Grafana for observability.  

**Learning**: Service-to-service security + basic observability.  
> 💡 Use minimal Istio profile to save resources.  

---

## 📦 6. Helm Deployment for Multi-Service App
**Tech**: GKE, Helm  
**Idea**:  
- Package `frontend`, `catalog`, `checkout` as Helm subcharts.  
- Deploy once, then test upgrades with version bumps.  

**Learning**: Helm templating + controlled rollout on one cluster.  

---

## 🧪 7. A/B Testing with Istio Traffic Split
**Tech**: GKE, Istio  
**Idea**:  
- Deploy `recommendation` service with `v1` and `v2`.  
- Use Istio VirtualService to send **20% → v2, 80% → v1**.  

**Learning**: Canary testing, traffic routing, resilience — all in one cluster.  

---

## 🔒 8. Least Privilege IAM Role Setup for Microservices
**Tech**: IAM Roles, Service Accounts, Cloud Run / GKE  
**Idea**:  
- Deploy two microservices:  
  - `orders-service` → Firestore read/write  
  - `reporting-service` → BigQuery read-only  
- Configure **separate service accounts with custom IAM roles**.  

**Learning**: Principle of least privilege, fine-grained IAM design.  

---

## 🛡️ 9. Secure Service-to-Service Communication with Workload Identity
**Tech**: GKE, Workload Identity, IAM, Pub/Sub  
**Idea**:  
- GKE service publishes to Pub/Sub.  
- Authentication handled via **Workload Identity** (no JSON keys).  

**Learning**: Keyless authentication, IAM ↔ Kubernetes service account mapping.  

---

## 🌐 10. Hub-and-Spoke Networking with Cloud Router + NCC
**Tech**: VPC Networks, Network Connectivity Center (NCC), Cloud Router, Firewall Rules  
**Idea**:  
- Build a **hub-and-spoke network** across 3 projects.  
- Central hub manages all egress/ingress.  
- Enforce firewall + IAM at the networking layer.  

**Learning**: Enterprise networking, transit-style GCP networking, governance.  

---

## 🏛️ 11. Three-Tier Microservice Setup (App Engine + Private VPC)

### **Presentation Tier**
- **Cloud Storage** (private static assets)  
- **Cloud CDN** (global caching, like AWS CloudFront)  
- **Google Cloud DNS** → Custom domain to LB  

### **Application Tier**
- **App Engine microservices**:  
  - `auth-service` (login/signup with Google Identity API)  
  - `order-service` (order lifecycle)  
  - `payment-service` (simulated payments)  
- **Google API Gateway** → Unified entrypoint  
- **Internal Load Balancer (ALB)** → Private routing between services  
- **Private VPC Link** → Secure access to Cloud SQL  

### **Data Tier**
- **Cloud SQL (Postgres/MySQL)** in **private VPC subnet** (no public IP)  
- Accessed via **Private Service Connect** only  
- **Cloud Storage (private bucket)** for uploads with signed URLs  

### **Networking & Security**
- **Custom VPC** with 3 subnets (frontend, app, db)  
- **Firewall rules** → allow only east-west traffic  
- **Cloud NAT** → outbound internet access for workloads  
- **IAM Policies**:  
  - App Engine service accounts with least privilege  
  - Cloud SQL IAM authentication  
- **VPC Service Controls** → prevent data exfiltration  

### **Workflow**
1. User visits `app.example.com` (Cloud DNS).  
2. Request → **External HTTP(S) Load Balancer** with Cloud CDN.  
3. LB → **App Engine frontend**.  
4. Frontend → **App Engine backend microservices (via API Gateway)**.  
5. Backend → **Cloud SQL** via private VPC link.  
6. Static files → **Cloud Storage (signed URLs)**.  

---

✨ With these projects, you’ll cover:  
- Serverless Functions & APIs  
- CI/CD with containers  
- Service Mesh & Helm  
- IAM & Workload Identity security  
- Enterprise networking (hub-spoke)  
- Full 3-tier microservice in private subnet  
