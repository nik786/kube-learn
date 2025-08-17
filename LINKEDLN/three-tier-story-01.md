

- [AWS-3-Tier-Architecture](https://github.com/jaik143/AWS-3-Tier-Architecture)

# 🌐 AWS Classic 3-Tier Architecture – স্কেলেবল, রেজিলিয়েন্ট এবং প্রোডাকশন-রেডি  

এখানে একটি **Well-Architected 3-Tier Web Application Architecture** দেখানো হয়েছে, যা পুরোপুরি AWS-এ হোস্ট করা।  

---

## ১️⃣ Presentation Layer (Web Tier)  
- ব্যবহারকারীরা অ্যাপ অ্যাক্সেস করে **Route 53 DNS** এবং **CloudFront CDN** এর মাধ্যমে, যা গ্লোবাল কন্টেন্ট ডেলিভারি দ্রুত করে।  
- ট্রাফিক প্রথমে যায় **Elastic Load Balancer (ELB)**-এ, যা ট্রাফিককে একাধিক Availability Zone-এ থাকা auto-scaled ওয়েব সার্ভারে পাঠায়।  
- এই লেয়ারটি **stateless** এবং **horizontally scalable**।  

---

## ২️⃣ Application Layer (App Tier)  
- ওয়েব সার্ভারগুলো লজিক-হেভি রিকোয়েস্ট ফরওয়ার্ড করে আরেকটি **ELB**-তে।  
- এই ELB ট্রাফিককে **private subnet**-এ থাকা অ্যাপ সার্ভারগুলোর মধ্যে load balance করে।  
- অ্যাপ লেয়ারটি মূল **business logic** চালায় এবং backend ডাটাবেসের সাথে ইন্টিগ্রেট হয়।  
- এখানে ও auto scaling ব্যবহার হয়, যাতে ডিমান্ড অনুযায়ী elasticity পাওয়া যায়।  

---

## ৩️⃣ Data Layer (Database Tier)  
- ডাটাবেসের জন্য ব্যবহৃত হয় **Amazon RDS (Multi-AZ)** সেটআপ।  
- Primary instance থেকে Standby instance-এ **synchronous replication** হয়, ফলে durability ও disaster resilience পাওয়া যায়।  
- **Automatic failover** নিশ্চিত করে ডাটাবেসের high availability।  

---

## 📦 Static Content Delivery  
- ইমেজ, JS, CSS-এর মতো static assets রাখা হয় **S3 bucket**-এ।  
- এগুলো **CloudFront CDN** দিয়ে গ্লোবালি সার্ভ হয়, যা পারফরম্যান্স অপ্টিমাইজ করে।  

---

## ✅ এই আর্কিটেকচারের মূল সুবিধা  
- **Fault Tolerance** across multiple AZs  
- **Auto Scaling** ওয়েব এবং অ্যাপ লেয়ার উভয় জায়গায়  
- **Optimized Performance** caching ও CDN ব্যবহারের মাধ্যমে  
- **High Availability** RDS Multi-AZ সেটআপের কারণে  
- **Separation of Concerns** – সহজে manage, monitor এবং scale করা যায়  

---

## 🔮 Modernization Ideas  
আরও আধুনিক করতে চাইলে এই আর্কিটেকচারে যোগ করা যেতে পারে:  
- **Containers** → ECS বা EKS  
- **Serverless** → Lambda + API Gateway  
- **Service Mesh** → App Mesh বা Istio  

---
