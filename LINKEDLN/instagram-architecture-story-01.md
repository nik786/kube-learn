


# 📸 How Would You Build Instagram from Scratch?

Instagram looks simple on the surface, but under the hood, it’s a **highly complex distributed system** handling **millions of users, images, and interactions** every second.  
Here’s a breakdown of how such a system could be designed.

---

## 🔹 Functional Requirements
- Users can upload and view **images and videos**.  
- Users can **like, comment, and search** posts by title.  
- Users can **follow/unfollow** others and view feeds from followed accounts.  
- Messaging is **not** part of this system.  

---

## 🔹 Non-Functional Requirements
- **High availability** and **low latency** for a seamless experience.  
- **Eventual consistency** is acceptable for feeds.  
- **Reliable storage** to prevent data loss.  
- **Horizontal scalability** to handle read-heavy workloads and viral events (e.g., 1 post → 1M+ views).  

---

## 🔹 Traffic & Storage Estimation
- **500M total users**  
- **100M daily active users**  
- **1M daily uploaders → ~5M uploads/day (~57 uploads/sec)**  

**Photos:**  
- Avg size: **200KB**  
- ~1TB/day → ~350TB/year (x3 replication for redundancy).  

**Videos:**  
- Avg size: **50MB**  
- ~50TB/day.  

---

## 🔹 Core System Components
- **Client Apps** → iOS, Android, Web.  
- **API Gateway** → Handles authentication & routing.  
- **Load Balancer** → Spreads incoming traffic.  
- **Application Servers** → Handle reads/writes for posts, likes, profiles.  
- **CDN (e.g., CloudFront)** → Speeds up image/video delivery.  
- **Cache (Redis/Memcached)** → Reduces read latency.  
- **Message Queue (SNS + SQS)** → Handles async post distribution.  
- **Object Storage (S3 / HDFS)** → Stores photos/videos.  
- **Databases** →  
  - MySQL → User data.  
  - DynamoDB (or Cassandra) → Metadata.  
  - Redis → Caching layer.  
- **Push Notifications** → Alerts followers of new activity.  

---

## 🔹 Modular Services
- **User Service** → Manages user profiles (Redis + MySQL fallback).  
- **Post Service** → Create, read, manage posts.  
- **Comment & Like Service** → Engagement tracking.  
- **Feed Service** → Builds user timelines (mix of push & pull).  
- **Follower Service** → Manages graph of relationships.  
- **URL Shortener** → Stores compact links to media in metadata.  

---

## 🔹 Database Architecture
- **Read-heavy system** → ~80% reads vs. 20% writes.  
- **Object Storage (S3)** → Stores photos & videos.  
- **DynamoDB** → Stores post metadata (post_id, URL, likes).  
- **MySQL** → Stores user info & relationships.  
- **Redis** → Hot cache for feeds & sessions.  
- **Sharding + Replication** → Ensures scale and fault tolerance.  

---

## 🔹 Execution Flow

### 1️⃣ Synchronous Flow (User Uploads a Post)
1. User logs in → Auth server verifies.  
2. Upload request hits **Write Server**.  
3. Photo/video stored in **S3**.  
4. **URL Shortener** creates compact link.  
5. Metadata stored in **DynamoDB**.  
6. **Feed Service** notified via **SNS**.  
7. **SQS** distributes message to follower feeds.  
8. **Push Notification Service** alerts online followers.  

---

### 2️⃣ Asynchronous Flow (Feed Generation)
- **Regular users** → System **precomputes feeds** by pushing new posts to each follower’s timeline.  
- **Celebrity users** → To avoid fan-out explosion, followers **pull content on demand**.  

➡️ Final feed is a **hybrid push-pull model**:  
- Push for normal users.  
- Pull for celebrities.  

---

## 🚀 Key Takeaways
- Instagram requires a **read-optimized, distributed architecture**.  
- **Object storage + CDN** for media delivery.  
- **Decoupled microservices + queues** for scalability.  
- **Hybrid feed generation** for handling different user types.  
- Built to support **millions of concurrent users with low latency**.  





# কিভাবে শূন্য থেকে Instagram তৈরি করবেন?

Instagram দেখতে সহজ মনে হলেও, ভেতরে এটি একটি জটিল সিস্টেম যা লক্ষ লক্ষ ব্যবহারকারী, ছবি এবং ইন্টারঅ্যাকশন সামলায়। আসুন দেখি, এমন একটি সিস্টেম কীভাবে কাজ করে।  

---

## 🔹 ফাংশনাল রিকোয়ারমেন্টস
- ব্যবহারকারীরা ছবি ও ভিডিও আপলোড এবং দেখতে পারবেন।  
- তারা লাইক, কমেন্ট করতে পারবেন এবং শিরোনাম দ্বারা পোস্ট সার্চ করতে পারবেন।  
- তারা অন্যদের ফলো করতে পারবেন এবং ফলো করা অ্যাকাউন্টগুলির ফিড দেখতে পারবেন।  

🚫 নোট: এই সিস্টেমে মেসেজিং অন্তর্ভুক্ত নয়।  

---

## 🔹 নন-ফাংশনাল রিকোয়ারমেন্টস
- হাই অ্যাভেইলেবিলিটি এবং লো লেটেন্সি একটি নিরবচ্ছিন্ন অভিজ্ঞতার জন্য জরুরি।  
- ফিডের জন্য eventual consistency গ্রহণযোগ্য।  
- ডাটা লস এড়াতে নির্ভরযোগ্য স্টোরেজ।  
- সিস্টেমকে স্কেলযোগ্য হতে হবে যাতে রিড-হেভি ট্রাফিক এবং সেলিব্রিটি-লেভেলের ভাইরালিটি সামলাতে পারে (যেমন ১টি ছবি ১M ব্যবহারকারী দেখছে)।  

---

## 🔹 ট্রাফিক ও স্টোরেজ হিসাব
- মোট ব্যবহারকারী: **500M**, দৈনিক সক্রিয় ব্যবহারকারী: **100M**  
- দৈনিক আপলোডার: **1M** → ~5M আপলোড/দিন (~57 আপলোড/সেকেন্ড)  

📷 **ফটো:**  
- গড় সাইজ: **200KB** → 1TB/দিন → 350TB/বছর (x3 রিডানড্যান্সির জন্য)  

🎥 **ভিডিও:**  
- গড় সাইজ: **50MB** → 50TB/দিন  

---

## 🔹 কোর সিস্টেম কম্পোনেন্টস
- **ক্লায়েন্ট অ্যাপস** (iOS/Android/Web)  
- **API Gateway** অথেন্টিকেশন হ্যান্ডেল করে  
- **Load Balancer** ট্রাফিক ভাগ করে  
- **Read/Write Servers** (পোস্ট, লাইক, প্রোফাইলের জন্য)  
- **CDN (CloudFront)** দ্রুত মিডিয়া ডেলিভারির জন্য  
- **Cache (Redis/Memcached)** লেটেন্সি কমায়  
- **SNS + SQS** পোস্ট ইভেন্ট ডিস্ট্রিবিউশনের জন্য  
- **S3 / HDFS + Replicas** ছবি/ভিডিও স্টোরেজ  
- **SQL/NoSQL** (MySQL = ইউজার, DynamoDB = মেটাডাটা)  
- **Push Notifications** অনলাইন ফলোয়ারদের জানাতে  

---

## 🔹 মডুলার সার্ভিসেস
- **User Service** (Redis cache + MySQL fallback)  
- **Post Service** (পোস্ট তৈরি, দেখা ও ম্যানেজ করা)  
- **Comment & Like Services**  
- **Feed Generator** (SQS + follower graph ব্যবহার করে টাইমলাইন আপডেট করে)  
- **Follower Service**  
- **URL Shortener** (S3 URL গুলো কমপ্যাক্ট আকারে সংরক্ষণের জন্য)  

---

## 🔹 ডাটাবেস আর্কিটেকচার
- 80% রিড বনাম 20% রাইট = রিড-অপ্টিমাইজড সিস্টেম  
- **Object Storage (S3)** মিডিয়ার জন্য  
- **DynamoDB** মেটাডাটার জন্য  
- **MySQL** ইউজার ইনফোর জন্য  
- **Redis** স্পিডের জন্য  
- **Sharding + 3x Replication** স্কেল ও রেজিলিয়েন্সের জন্য  

---

## 🔹 এক্সিকিউশন ফ্লো  

### 1️⃣ Synchronous Flow (ব্যবহারকারী একটি পোস্ট আপলোড করলে):  
- ব্যবহারকারী লগইন → Auth Server ভেরিফাই করে → Write Server আপলোড প্রক্রিয়া করে  
- ছবি S3-এ পাঠানো হয় → URL Shortener একটি শর্ট লিঙ্ক রিটার্ন করে  
- মেটাডাটা স্টোর হয় → Feed Service SNS এর মাধ্যমে নোটিফাই হয়  
- SQS মেসেজ ডিস্ট্রিবিউট করে → Notification Server push alert পাঠায়  

### 2️⃣ Asynchronous Flow (Feed Generation):  
- **সাধারণ ব্যবহারকারীদের জন্য:** সিস্টেম প্রি-কম্পিউটেড ফিড তৈরি করে এবং ফলোয়ারদের দিকে পুশ করে।  
- **সেলিব্রিটি ব্যবহারকারীদের জন্য:** ফলোয়াররা অন-ডিমান্ডে কনটেন্ট পুল করে, কারণ স্কেলেবিলিটি ইস্যু থাকতে পারে।  

---
