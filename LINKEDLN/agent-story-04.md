

- [GenAI_Healthcare](https://github.com/satispp24/GenAI_Healthcare)


# 🏥🤖 AI-Powered Clinical Workflow: From Audio to SOAP Notes in Minutes  

Built and verified a **fully operational, event-driven Generative AI system** for healthcare — converting medical audio to **structured SOAP notes** using **Amazon Transcribe Medical** and **Claude 3 on Amazon Bedrock**.  

---

## 🧠 AI Services
- **Amazon Transcribe Medical** → Accurate clinical transcription  
- **Amazon Bedrock (Claude 3 Sonnet)** → Structured SOAP note generation  
- **Accuracy**: 95%+  
- **Processing time**: 2–5 minutes  
- **Cost**: ~**$0.13/file**  

---

## 🧱 Architecture (Event-Driven, Scalable)
- **Frontend**: HTML5 + EC2 + Nginx (auto-polling UX)  
- **API Layer**: Amazon API Gateway (HTTP APIs)  
- **Compute**: AWS Lambda (presigned upload, invoke, and Bedrock integration)  
- **Storage**: Amazon S3 (encrypted buckets + event triggers)  
- **Infrastructure as Code**: Terraform-based deployment  

**Security**  
- IAM least-privilege access  
- S3 private access + presigned URLs  
- Full encryption at rest and in transit  

---

## 📥 Workflow
1. **Upload audio** → Presigned URL (S3)  
2. **Trigger** → Amazon Transcribe Medical  
3. **Transcript saved** → Event triggers Lambda  
4. **Lambda** → Calls Claude 3 (Amazon Bedrock)  
5. **Result** → SOAP note stored + rendered in frontend  

---

## ✅ Verified Functionality
- Presigned uploads  
- Event-driven transcription pipeline  
- Claude 3 prompt engineering for structured SOAP output  
- Fully working **frontend UX** with auto-refresh  
- Logs & metrics via **CloudWatch**  

---

## 📁 Repo & Quick Deploy
- GitHub: [Project Repository](https://lnkd.in/eKXihZxM)  
- Deployable via:  
  ```bash
  terraform init
  terraform apply


# 🏥🤖 AI-চালিত ক্লিনিকাল ওয়ার্কফ্লো: অডিও থেকে SOAP নোটস কয়েক মিনিটে  

আমি তৈরি করেছি এবং ভেরিফাই করেছি একটি সম্পূর্ণ কার্যকরী, **ইভেন্ট-ড্রিভেন জেনারেটিভ AI সিস্টেম** হেলথকেয়ারের জন্য – যা মেডিকেল অডিওকে স্ট্রাকচার্ড SOAP নোটে রূপান্তর করে **Amazon Transcribe Medical** এবং **Claude 3 (Amazon Bedrock)** ব্যবহার করে।  

---

## 🧠 AI সার্ভিসেস  
- **Amazon Transcribe Medical** → নির্ভুল ক্লিনিকাল ট্রান্সক্রিপশন  
- **Amazon Bedrock (Claude 3 Sonnet)** → স্ট্রাকচার্ড SOAP নোট জেনারেশন  
- **সঠিকতা:** 95%+  
- **প্রসেসিং সময়:** 2–5 মিনিট  
- **খরচ:** ~ $0.13 / ফাইল  

---

## 🧱 আর্কিটেকচার (Event-Driven, Scalable)  
- **Frontend:** HTML5 + EC2 + Nginx with auto-polling  
- **API Layer:** Amazon API Gateway (HTTP APIs)  
- **Compute:** AWS Lambda (presigned upload, invoke, এবং Bedrock integration)  
- **Storage:** Amazon S3 (এনক্রিপ্টেড বালতি + ইভেন্ট ট্রিগার সহ)  
- **Infra as Code:** Terraform-ভিত্তিক ডিপ্লয়মেন্ট  

**সিকিউরিটি:**  
IAM Least-Privilege, S3 Private Access, Presigned URLs, সম্পূর্ণ এনক্রিপশন (at rest + in transit)  

---

## 📥 ওয়ার্কফ্লো  
1. অডিও আপলোড → Presigned URL (S3)  
2. **Trigger → Amazon Transcribe Medical**  
3. Transcript সংরক্ষণ → Lambda Trigger  
4. **Lambda → Claude 3 (Amazon Bedrock)** কল করে  
5. SOAP Note → সংরক্ষিত + Frontend-এ প্রদর্শিত  

---

## ✅ ভেরিফাইড ফাংশনালিটি  
- Presigned Uploads  
- Event-Driven Transcription  
- Claude 3 Prompt Engineering → স্ট্রাকচার্ড ক্লিনিকাল আউটপুট  
- সম্পূর্ণ কার্যকর Frontend UX + Auto-Refresh  

**Logs & Metrics:** Amazon CloudWatch  

---

## 📁 রিপো ও কুইক ডিপ্লয়  
- GitHub: [https://lnkd.in/eKXihZxM](https://lnkd.in/eKXihZxM)  
- Infra Deploy:  
  ```bash
  terraform init  
  terraform apply




  এক্সটেনসিবিলিটি

➡️ শীঘ্রই আসছে:

FHIR ইন্টিগ্রেশন

Amazon Cognito

Multi-region সাপোর্ট

Batch Mode

Mobile App
