

Manual server monitoring is slow. What if it could be fully automated without logging into a single machine?
Over the past few days, I built an Ansible-powered automation that monitors and manages AWS EC2 instances delivering daily health reports right to my inbox.

🔍 The Scenario
Imagine managing 100+ servers running critical workloads.
 Every day at exactly 3:00 PM, you need to know:
Which servers have high CPU usage?
Is any server low on RAM?
Is disk space running out?
Without this visibility, issues can go unnoticed until it’s too late.
I implemented this setup for 10 Dev environment servers, but it can scale to hundreds with just a few configuration tweaks.

💡 The Solution
Using Ansible + AWS EC2 Dynamic Inventory + Gmail SMTP, I created a Daily Server Health Reporting System:
1️⃣ Dynamic Inventory Fetches EC2 instances tagged Environment=dev.
 2️⃣ Secure Access Automatically injects my public SSH key for passwordless login.
 3️⃣ Health Check Playbook Gathers:
CPU usage (mpstat)
RAM usage (free -m)
Disk usage (df -h)
 Formats into a human-readable report.
 4️⃣ Email Integration Sends the report via Gmail SMTP using an App Password.
 5️⃣ Scheduled Execution Runs every day at 3:00 PM via Cron.

🛠 Tech Stack
Ansible Automation & Orchestration
AWS EC2 Cloud Infrastructure
Ansible Dynamic Inventory Plugin (aws_ec2) Auto-fetch server list
Cron Module Scheduled Tasks
Linux Shell Scripting Custom Integrations
Gmail SMTP Email Delivery
📂 GitHub Repository: 
🔗 https://lnkd.in/gJMsgHiJ

🙏 Special thanks to Aditya Jaiswal(DevOps Shack) for the amazing tutorials that guided me through this implementation truly bridging the gap between theory and real-world DevOps challenges.
