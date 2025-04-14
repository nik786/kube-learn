

5 More DevOps Automation Scripts You Need! (Part 11) 🔥


5️⃣1️⃣ Check SSL Certificate Expiry for a Domain 🔒

Avoid downtime by monitoring SSL certificate expiration.

#!/bin/bash
DOMAIN="example.com"
echo | openssl s_client -servername $DOMAIN -connect $DOMAIN:443 2>/dev/null | openssl x509 -noout -enddate

5️⃣2️⃣ Identify Large Log Files Consuming Disk Space 💾

Find and manage oversized log files before they fill up your disk.

#!/bin/bash
echo "Finding log files larger than 500MB..."
find /var/log -type f -size +500M -exec ls -lh {} \;

5️⃣3️⃣ Restart Kubernetes Pods with High Memory Usage ☸️

Ensure stability by restarting pods that consume excessive memory.

#!/bin/bash
echo "Restarting pods with high memory usage..."
kubectl top pods --all-namespaces | awk '$3 > 500 {print $2}' | xargs kubectl delete pod

5️⃣4️⃣ Check Unused Security Groups in AWS ☁️

Identify security groups that are not attached to any instances.

aws ec2 describe-security-groups --query "SecurityGroups[*].GroupId" --output text | while read SG; do
 aws ec2 describe-instances --filters "Name=instance.group-id,Values=$SG" --query "Reservations[*].Instances[*].InstanceId" --output text | grep -q . || echo "Unused: $SG"
done

5️⃣5️⃣ Automate Daily Backup for a Directory 🔄

Keep your critical files safe by scheduling daily backups.

#!/bin/bash
SRC_DIR="/important/data"
BACKUP_DIR="/backup"
mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/backup_$(date +%F).tar.gz $SRC_DIR
