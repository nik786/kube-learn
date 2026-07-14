
# Technical Questions for Linux, DevOps, and Cloud Infrastructure

1. Securing a Linux Server  
   You are tasked with securing a Linux server that hosts a web application. The server is currently exposed to the internet and has a weak root password. Describe the steps you would take to secure the server.
   ## Securing a Linux Server

| Step | What to Do | Example Command |
|------|------------|-----------------|
| **1. Change the root password** | Set a strong password for the root user. | `passwd root` |
| **2. Disable root SSH login** | Prevent direct SSH login as the root user. | Edit `/etc/ssh/sshd_config` → `PermitRootLogin no` |
| **3. Create a new sudo user** | Create a normal user and give sudo access. | `adduser devops`<br>`usermod -aG sudo devops` |
| **4. Enable the firewall** | Allow only required ports like SSH, HTTP, and HTTPS. | `ufw allow 22,80,443/tcp`<br>`ufw enable` |
| **5. Update the server** | Install the latest security updates. | `apt update && apt upgrade -y` |

### Easy to Remember

```text
Change Password
        ↓
Disable Root Login
        ↓
Create Sudo User
        ↓
Enable Firewall
        ↓
Update Server
```

Interview One-Line Answer:
"Change the root password, disable root SSH login, create a sudo user, enable the firewall, and keep the server updated with the latest security patches."

3. Recovering Data from a Corrupted File System  
   One of your team members accidentally ran a command that corrupted the file system on a critical Linux server. The server is no longer booting, and you need to recover the data. Walk me through the steps you would take to recover the file system.

## Recovering Data from a Corrupted File System

| Step | What to Do | Example Command |
|------|------------|-----------------|
| **1. Boot into Rescue Mode** | Start the server using a Linux Live CD/USB or Rescue Mode. | *(Boot into Rescue Mode)* |
| **2. Identify the disk** | Find the corrupted disk or partition. | `lsblk` or `fdisk -l` |
| **3. Check and repair the file system** | Run a file system check to repair errors. | `fsck -y /dev/sda1` |
| **4. Mount and recover data** | Mount the repaired file system and copy important data to a safe location. | `mount /dev/sda1 /mnt`<br>`cp -r /mnt/data /backup/` |
| **5. Restore and reboot** | Restore from backup if needed and reboot the server. | `reboot` |

### Easy to Remember

```text
Boot Rescue Mode
        ↓
Identify Disk
        ↓
Run fsck
        ↓
Recover Data
        ↓
Restore & Reboot
```

Interview One-Line Answer:
"Boot the server in Rescue Mode, identify the disk, repair the file system using fsck, recover the data, and restore the server from backup if required."


5. Backup Script for Remote Server  
   Your team uses a backup script to download the latest backup file from a remote server. However, the script is currently not working due to changes in the remote server's configuration. Write a script that downloads the latest backup file from the remote server using SSH.

   

7. Terraform Taint and Untaint Commands  
   You are using Terraform to manage your infrastructure, and you notice that one of your resources is not being updated correctly. Describe how you would use Terraform's taint and untaint commands to resolve the issue. Additionally, explain the difference between stateful and stateless resources in Terraform.
