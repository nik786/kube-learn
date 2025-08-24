
# ⚡ Event-Driven Serverless Architecture with AWS Lambda, SQS, DynamoDB, and API Gateway  

Last week, I built an **Event-Driven Serverless Architecture** on AWS to perform **CRUD operations**.  
This application extracts messages from objects stored in **S3**, queues them to **SQS**, and writes them to **DynamoDB** via **Lambda functions**.  
It also exposes a **RESTful API** (via **API Gateway**) to perform CRUD-like operations on DynamoDB records.  

---

## 🛠️ AWS Services Used
- ✔️ **AWS Lambda**  
- ✔️ **Amazon S3**  
- ✔️ **Amazon DynamoDB**  
- ✔️ **Amazon API Gateway**  
- ✔️ **Amazon Simple Queue Service (SQS)**  
- ✔️ **Amazon CloudWatch**  
- ✔️ **AWS X-Ray**  

---

## 🔄 Step-by-Step Workflow  

1. **S3 → Lambda → SQS**  
   - A file is copied into the target **S3 bucket**.  
   - **S3 Event Notification** triggers a **Lambda**.  
   - Lambda sends the event to the **SQS queue**.  

2. **SQS Event → Lambda**  
   - SQS (Standard or FIFO) supports **dead-letter queues** for faulty messages.  
   - When a message is pushed into SQS, an **SQS event** triggers a Lambda.  
   - This invocation is **synchronous**.  

3. **Lambda → DynamoDB**  
   - Lambda processes the message from SQS.  
   - Lambda writes the message to **DynamoDB** (`PutItem`).  

4. **API Gateway → Lambda → DynamoDB**  
   - End-user makes an **HTTP(S) request** via API Gateway.  
   - API Gateway triggers a Lambda (synchronous).  
   - Based on the HTTP method (POST, GET, DELETE), Lambda performs **CRUD operations** on DynamoDB.  

5. **Monitoring & Observability**  
   - **AWS X-Ray** used for distributed tracing.  
   - **CloudWatch** used for logs and performance monitoring.  

---

## 📊 Performance Observations  
- **API Testing with Postman** showed **significant performance gains** when scaling Lambda memory:  
  - **128 MB → 397 ms avg response time**  
  - **512 MB → 189 ms avg response time**  
- Result: **~52% improvement** in response times.  

---

## 🚀 Benefits of Event-Driven Serverless  
- **Scalability** → Independent scaling of services.  
- **Flexibility** → Decoupled architecture with event routing.  
- **Faster Development** → Quicker time-to-market.  
- **Fault Tolerance** → Dead-letter queues + retries.  
- **Real-Time Responsiveness** → Event-driven workflows.  
- **Efficient Resource Utilization** → Pay-as-you-go compute model.  

This architecture is ideal for **modern, dynamic applications** requiring **resilience, agility, and speed**.  












# 📩 AWS Serverless Event-Driven Architecture for Customer Feedback  

এটি একটি সহজ কিন্তু বাস্তবসম্মত আর্কিটেকচার, যেখানে **AWS Serverless + Event-Driven Architecture** ব্যবহার করা হয়েছে।  
এখানে **SQS, DLQ এবং SNS** ব্যবহৃত হয়েছে কাস্টমার ফিডব্যাক সংগ্রহ ও প্রক্রিয়া করার জন্য।  

---

## 🛠 সিস্টেম যেভাবে কাজ করে  

1. ব্যবহারকারী মোবাইল বা ওয়েব অ্যাপ থেকে ফিডব্যাক সাবমিট করে।  

2. **Amazon API Gateway** একটি **Lambda Function** ট্রিগার করে, যা ইনপুট গ্রহণ ও ভ্যালিডেট করে।  

3. ভ্যালিডেটেড ফিডব্যাক মেসেজটি **Amazon SQS Queue**-তে পাঠানো হয় Lambda দ্বারা।  

4. **Amazon SQS** ফিডব্যাক মেসেজগুলোকে অ্যাসিনক্রোনাসলি সংরক্ষণ করে।  
   - এখানে একটি **Dead Letter Queue (DLQ)** কনফিগার করা আছে, যাতে ফেল হওয়া মেসেজ জমা হয়।  

5. আরেকটি **AWS Lambda** ফিডব্যাককে ডাটাবেসে সংরক্ষণ করে।  
   - যদি ব্যর্থ হয়, তবে নির্দিষ্ট সংখ্যক বার রিট্রাই করে।  

6. যদি মূল কিউতে মেসেজ সর্বোচ্চ রিট্রাইয়ের পরেও ফেল হয়, তবে তা **SQS DLQ**-তে চলে যায়।  

7. **Amazon SNS** DLQ-এর সাথে সাবস্ক্রাইব করা থাকে।  
   - DLQ-তে মেসেজ গেলে **ইমেইল বা SMS নোটিফিকেশন** সাপোর্ট টিমকে পাঠানো হয়।  

---

## ✅ মূল সুবিধাসমূহ  

- **Reliable Queueing** → রিট্রাই এবং ফেল মেসেজ আইসোলেশন সহ।  
- **Automatic Alerting via SNS** → সাপোর্ট টিম রিয়েল-টাইমে এলার্ট পায়।  
- **Serverless Scalability** → কোনো ইন্ফ্রাস্ট্রাকচার ম্যানেজ করতে হয় না।  

---
