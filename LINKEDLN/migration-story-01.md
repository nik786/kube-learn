



# 🚀 AWS Migration Project: Hands-On Rehosting to Amazon EC2

I recently conducted a **hands-on migration of sample workloads to AWS**, focusing on **rehosting applications to Amazon EC2** using AWS-native services.  
This project provided valuable exposure to **real-world cloud migration strategies** and deepened my understanding of **best practices** for planning, executing, and optimizing cloud transitions.

---

## 🛠️ Services Used
- ✅ **AWS Application Discovery Service (ADS)**
- ✅ **AWS Application Migration Service (MGN)**
- ✅ **AWS Database Migration Service (DMS)**
- ✅ **Amazon RDS**

---

## 🧭 Phase 1 – Infrastructure Assessment with AWS ADS
Using **AWS ADS**, I deployed discovery agents across servers to automatically gather detailed information on:
- System configurations  
- Resource utilization  
- Network dependencies  

This data helped map application relationships and group dependent servers, enabling accurate **sizing of target EC2 instances** and careful **migration planning**.  
ADS integration with **AWS Migration Hub** provided centralized visibility into all workloads.

---

## ⚙️ Phase 2 – Application Migration with AWS MGN
With infrastructure insights in hand, I migrated applications using **AWS MGN**:
- Enabled **real-time replication** of on-premises servers to AWS  
- Installed lightweight replication agents  
- Monitored replication progress via the MGN dashboard  
- Launched **test instances** in AWS for validation before final cutover  

👉 Result: Smooth, **non-disruptive migration cutover** that was production-ready.

---

## 💾 Phase 3 – Database Migration with AWS DMS
For database workloads, I used **AWS DMS** to securely migrate data with minimal downtime:
- Performed **initial full data load**  
- Enabled **continuous Change Data Capture (CDC)** to keep source & target synchronized  
- Transitioned databases seamlessly to **Amazon RDS**  
- Maintained **data consistency and integrity**  

Parallel operation during migration allowed for **validation before switching production workloads**.

---

## ☁️ Phase 4 – Database Hosting and Management with Amazon RDS
Post-migration, the database was hosted on **Amazon RDS**:
- Fully managed relational database service  
- Built-in **high availability** & **security features**  
- Improved **reliability, performance, and scalability** of the database infrastructure  

---

## 🌟 Benefits & Learnings
- ⏩ Accelerated migration with **minimal downtime and risk**  
- 📊 Improved resource utilization with **data-driven sizing**  
- 🔧 Simplified complex migrations using **AWS-native tools**  
- 📈 Enhanced **scalability, reliability, and operational efficiency**  

👉 **Standout Feature:**  
EC2 instance recommendations from **AWS ADS** are based on **real usage data**.  
This enables effective **rightsizing**, ensuring **optimal performance** while controlling **costs**.

---







# ☁️ AWS Migration Project – Rehosting Applications to Amazon EC2  

আমি সম্প্রতি একটি **হ্যান্ডস-অন মাইগ্রেশন প্রজেক্ট** করেছি যেখানে স্যাম্পল ওয়ার্কলোডগুলোকে **AWS-এ রিহোস্ট (lift-and-shift)** করেছি Amazon EC2-তে, শুধুমাত্র AWS-native সার্ভিস ব্যবহার করে।  
এই প্রজেক্ট আমাকে বাস্তব **ক্লাউড মাইগ্রেশন স্ট্রাটেজি** সম্পর্কে অভিজ্ঞতা দিয়েছে এবং পরিকল্পনা, এক্সিকিউশন ও অপ্টিমাইজেশনের বেস্ট প্র্যাকটিসগুলো আরও ভালোভাবে শিখিয়েছে।  

---

## 🛠️ ব্যবহৃত সার্ভিসসমূহ  
- ✅ **AWS Application Discovery Service (ADS)**  
- ✅ **AWS Application Migration Service (MGN)**  
- ✅ **AWS Database Migration Service (DMS)**  
- ✅ **Amazon RDS**  

---

## 🧭 Phase 1 – Infrastructure Assessment with ADS  
- **AWS ADS** ব্যবহার করে বিভিন্ন সার্ভারে discovery agents ডেপ্লয় করি।  
- এগুলো স্বয়ংক্রিয়ভাবে **সিস্টেম কনফিগারেশন, রিসোর্স ইউটিলাইজেশন, নেটওয়ার্ক ডিপেন্ডেন্সি** সংগ্রহ করে।  
- এই ডেটা দিয়ে অ্যাপ্লিকেশন সম্পর্ক ও ডিপেন্ডেন্ট সার্ভারগুলো ম্যাপ করা যায়।  
- ফলে **EC2 instance rightsizing** এবং সঠিকভাবে মাইগ্রেশন প্ল্যানিং সম্ভব হয়।  
- **Migration Hub**-এর সাথে ADS ইন্টিগ্রেশন সেন্ট্রালাইজড ভিজিবিলিটি দিয়েছে।  

---

## ⚙️ Phase 2 – Application Migration with MGN  
- ইনফ্রাস্ট্রাকচারের ইনসাইট পাওয়ার পর আমি **AWS MGN** ব্যবহার করে অ্যাপ্লিকেশন মাইগ্রেশন শুরু করি।  
- এটি **রিয়েল-টাইম replication** এর মাধ্যমে অন-প্রেম সার্ভারকে AWS-এ কপি করে, ফলে ডাউনটাইম কম হয়।  
- লাইটওয়েট এজেন্ট ইনস্টল করি, MGN ড্যাশবোর্ডে প্রগ্রেস মনিটর করি।  
- কটওভারের আগে **test instances** লঞ্চ করে ভ্যালিডেশন করি।  
- ফাইনাল কটওভার ছিলো মসৃণ, নন-ডিসরাপটিভ এবং প্রোডাকশন-রেডি।  

---

## 💾 Phase 3 – Database Migration with DMS  
- ডাটাবেসের জন্য ব্যবহার করি **AWS DMS**।  
- প্রথমে **ফুল ডাটা লোড**, এরপর **Change Data Capture (CDC)** ব্যবহার করে সোর্স ও টার্গেট ডাটাবেস সিঙ্ক রাখি।  
- এর ফলে **মিনিমাম ডাউনটাইম** এ ডাটা মাইগ্রেশন সম্ভব হয়।  
- প্যারালাল অপারেশন চলার কারণে মাইগ্রেশন চলাকালে টেস্ট ও ভ্যালিডেশন করতে পেরেছি।  
- অবশেষে অন-প্রেম ডাটাবেস থেকে **Amazon RDS**-এ সিমলেস ট্রানজিশন সম্পন্ন হয়।  

---

## ☁️ Phase 4 – Database Hosting on Amazon RDS  
- মাইগ্রেশনের পর ডাটাবেস হোস্ট করা হয় **Amazon RDS**-এ।  
- এটি একটি **ফুলি ম্যানেজড সার্ভিস**, যেখানে high availability, security, performance এবং scalability বিল্ট-ইন।  
- এর ফলে ডাটাবেস ইনফ্রাস্ট্রাকচার আরও **রিলায়েবল ও অপারেশনালি ইফিসিয়েন্ট** হয়েছে।  

---

## 🌟 Benefits & Learnings  
- ⏩ **Accelerated migration** – কম সময়ে, কম ঝুঁকিতে মাইগ্রেশন  
- 📊 **Improved resource utilization** – ডেটা-ড্রিভেন rightsizing  
- 🔧 **Simplified complex migrations** – AWS-native টুল দিয়ে সহজীকরণ  
- 📈 **Enhanced scalability, reliability, efficiency**  

👉 সবচেয়ে ভালো লেগেছে **ADS থেকে EC2 rightsizing recommendations** পাওয়া, কারণ এগুলো রিয়েল ইউজেজ ডেটার ওপর ভিত্তি করে।  
এতে **পারফরম্যান্স অপ্টিমাইজ** হয়, আবার **খরচও নিয়ন্ত্রণে থাকে**।  

---
