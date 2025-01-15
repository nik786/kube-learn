| **Aspect**              | **Zombie Process**                                         | **Orphan Process**                                   |
|-------------------------|-----------------------------------------------------------|----------------------------------------------------|
| **Definition**          | A process that has completed execution but still has an entry in the process table because its parent hasn’t read its exit status. | A process whose parent has terminated, making `init` (PID 1) or systemd its new parent. |
| **State**               | Exists in a `Z` (zombie) state in the process table.       | Continues to run normally under `init` or `systemd`.|
| **Impact**              | Consumes only a process table entry and no resources; can lead to resource exhaustion if too many zombies accumulate. | No negative impact, as `init`/`systemd` handles it effectively. |
| **Resolution**          | Requires the parent process to read the child's exit status or manual intervention (e.g., killing the parent). | No resolution needed; handled automatically by the system. |



| **Signal**    | **SIGTERM**                                        | **SIGKILL**                                      |
|---------------|----------------------------------------------------|-------------------------------------------------|
| **Definition**| A signal to terminate a process gracefully, allowing it to perform cleanup before exiting. | A signal to forcefully kill a process immediately without cleanup. |
| **Interceptable** | Can be caught or ignored by the process, allowing it to handle termination. | Cannot be intercepted, blocked, or ignored; ensures immediate termination. |


| **Feature**                         | **Description**                                                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TTL (Time to Live)**              | A field in the IP header that determines the maximum number of hops (routers) a packet can pass through before being discarded.                           |
| **Decrement Mechanism**             | Each time a packet is forwarded by a router, the TTL value is decremented by 1.                                                                           |
| **Meaning of `ttl=64`**             | 64 is the initial TTL value set by the operating system (common defaults are 64, 128, or 255).                                                            |
| **Hops Left in `ttl=64`**           | Indicates that the packet has 64 hops remaining before expiration.                                                                                        |
| **Example: Ping `127.0.0.1`**       | Since you're pinging `127.0.0.1` (localhost), the packet doesn't traverse any routers, so the TTL remains at its initial value of 64.                     |









# Zombie, Orphan, and Defunct Processes

### Comparison Table

| **Aspect**        | **Zombie Process**                                                                                                                                 | **Orphan Process**                                                                                                   | **Defunct Process**                                                                                                                                |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**    | A process that has completed execution but remains in the process table because its parent hasn't read its exit status using `wait()`.            | A process whose parent has terminated, leaving it to be adopted by the `init` process (PID 1).                      | Essentially the same as a zombie process, a dead process whose exit status hasn’t been collected by the parent.                                   |
| **Key Feature**   | Consumes no CPU/memory but occupies a slot in the process table.                                                                                  | Continues to execute normally under the supervision of the `init` process.                                          | Marked as `<defunct>` in the process table.                                                                                                       |
| **State**         | Dead but not reaped by the parent.                                                                                                                | Running, adopted by the `init` process.                                                                             | Dead but not reaped (same as Zombie).                                                                                                             |
| **Handled By**    | Original parent process.                                                                                                                          | Adopted and handled by the `init` process.                                                                          | Original parent process.                                                                                                                          |
| **Command to Find** | `ps aux | grep Z`                                                                                                                                | `ps -eo pid,ppid,cmd | awk '$2 == 1 && $1 != 1'`                                                                    | `ps aux | grep '<defunct>'`                                                                                                                        |



# Difference Between Zombie and Defunct Processes

| **Aspect**         | **Zombie Process**                                                                               | **Defunct Process**                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Definition**     | A process that has completed execution but remains in the process table because its parent hasn't read its exit status. | A dead process whose exit status hasn’t been collected by its parent; essentially the same as a zombie process. |
| **State**          | Dead but waiting for the parent process to collect its exit status.                              | Dead, and appears as `<defunct>` in the process table.                                         |
| **Key Feature**    | Consumes no resources but occupies a slot in the process table.                                  | Same as Zombie but explicitly labeled `<defunct>` in the process list.                        |
| **Handled By**     | Original parent process must collect the exit status using `wait()`.                             | Original parent process; state persists until reaped.                                          |
| **Command to Find**| `ps aux  grep Z`                                                                                | `ps aux grep '<defunct>'`                                                                    |
| **Visibility**     | Marked as `Z` in the state column when listed in `ps`.                                           | Explicitly labeled as `<defunct>` in the command output.                                       |



How to Set Grub Password?
--------------------------

```
mkdir /opt/grub-backup
cp /boot/grub/grub.cfg /opt/grub-backup/
vim /etc/grub.d/40_custom
set superuser="nik"
password nik 123456
#password_pbkdf2

grub2-mkpasswd-pbkd2

grub2-mkconfig –o /opt/grub-backup/grub.cfg
cp  /opt/grub-backup/grub.cfg /boot/grub2/
reboot


```

How to RESET GRUB PASSWORD??
-----------------------------

| **Step**                                      | **Description**                                                                                                                                               |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Use Installation Disk**                 | Use the RHEL installation disk for Redhat Linux or CentOS installation disk for CentOS Linux.                                                                |
| **2. Select Rescue Option**                  | From Troubleshooting options, select the option to "Rescue a CentOS/RedHat Linux system."                                                                     |
| **3. Mount System**                          | Choose the first option, which mounts the installed Linux system in the `/mnt/sysimage` directory.                                                            |
| **4. Enter Chroot Environment**              | Run `chroot /mnt/sysimage`. This command creates an environment with root privileges, allowing all subsequent commands to execute as root.                    |
| **5. Edit GRUB Configuration**               | Open the file `/etc/grub.d/40_custom` and remove the directives responsible for setting authentication at the boot loader screen.                              |
| **6. Save Changes**                          | Save the file after removing the authentication directives.                                                                                                   |
| **7. Generate New GRUB Configuration**       | Run `grub2-mkconfig -o /tmp/grub.cfg` to generate a new GRUB configuration file.                                                                              |
| **8. Replace GRUB File**                     | Replace the old GRUB configuration file with the new one using `mv /tmp/grub.cfg /boot/grub2/`.                                                              |
| **9. Exit Chroot Environment**               | Run `exit` to exit the chroot environment.                                                                                                                   |
| **10. Reboot the System**                    | Reboot the system to apply the changes.                                                                                                                      |



How to reset root password
---------------------------




| **Step**                                   | **Description**                                                                                         |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **1. Interrupt GRUB Boot**                | Boot the computer and interrupt the boot process at the GRUB stage by hitting the arrow keys or space bar. |
| **2. Edit GRUB Entry**                    | Press `e` to edit the first GRUB menu option and navigate to the kernel line.                           |
| **3. Modify Kernel Line**                 | Press `e` again to edit the kernel line and remove `quiet splash` and add `init=/bin/bash`.             |
| **4. Boot System**                        | After editing, press `b` to boot the system with the modified GRUB entry.                               |
| **5. Access Bash Prompt**                 | After booting, you will be presented with a bash command prompt.                                        |
| **6. Remount File Systems**               | Run `mount -o remount,rw /`, `mount -o remount,rw /proc`, and `mount /proc` to remount necessary file systems. |
| **7. Reset Root Password**                | Use the `passwd` command to reset the root password.                                                   |
| **8. Reboot System**                      | Reboot the system to apply the changes using the new root password.                                     |


https://www.ostechnix.com/how-to-reset-or-recover-root-user-password-in-linux/
https://www.tecmint.com/reset-forgotten-root-password-in-rhel-centos-and-fedora/
https://linuxconfig.org/recover-reset-forgotten-linux-root-password



Network Bonding
----------------
| **Mode**      | **Name**                             | **Description**                                                                                                                                              | **Features**                                   |
|---------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| **mode=0**    | Balance-rr                          | Follows the round-robin policy, which is the default mode. Transmits packets in sequential order.                                                            | Load balancing and fault tolerance.           |
| **mode=1**    | Active-backup                       | Only one slave in the bond is active. The backup becomes active if the active slave fails. The bond’s MAC address is externally visible on one port only.    | Fault tolerance.                              |
| **mode=2**    | Balance-xor                        | Transmits based on `[(source MAC XOR destination MAC) modulo slave count]`, selecting the same slave for each destination MAC address.                        | Load balancing and fault tolerance.           |
| **mode=3**    | Broadcast                           | Transmits all packets on all slave interfaces.                                                                                                               | Fault tolerance.                              |
| **mode=4**    | IEEE 802.3ad Dynamic link aggregation | Creates aggregation groups sharing the same speed and duplex settings. Utilizes all slaves in the active aggregator per the 802.3ad specification.            | Load balancing and fault tolerance.           |
| **mode=5**    | Adaptive transmit load balancing (TLB) | Distributes outgoing traffic based on current load without requiring special switch support.                                                                 | Load balancing.                               |
| **mode=6**    | Adaptive load balancing (ALB)       | Provides adaptive load balancing without requiring special switch support. Receive load balancing is achieved via ARP negotiation.                           | Load balancing and fault tolerance.           |



```
modprobe bonding

apt-get install ifenslave

ip link add bond0 type bond mode 802.3ad
ip link set eth0 master bond0
ip link set eth1 master bond0


vim /etc/network/interfaces
auto bond0
iface bond0 inet static
	address 192.168.1.150
	netmask 255.255.255.0	
	gateway 192.168.1.1
	dns-nameservers 192.168.1.1 8.8.8.8
	dns-search domain.local
		slaves eth0 eth1
		bond_mode 0
		bond-miimon 100
		bond_downdelay 200
		bound_updelay 200



systemctl restart networking.service
ifup bond0
Details about the bond interface can be obtained by displaying the content of the below kernel file
cat /proc/net/bonding/bond0
To investigate other bond interface messages or to debug the state of the bond physical NICS
tail -f /var/log/messages
Next use mii-tool tool to check Network Interface Controller (NIC) parameters as shown 
mii-tool

```

LINUX AS ROUTER
----------------

```
In this example, we will disable and enable eth1:
ip link show
ip link set eth1 down
ip link show
ip link set eth1 up
ip link show eth1


 ip route show
route -n
netstat -rn
ip route show
ip route add 10.0.0.0/24 via 192.168.0.15 dev enp0s3
ip route add 192.168.0.0/24 via 10.0.0.15 dev enp0s3


echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT


In a LAN with many hosts, the router keeps track of established connections
in /proc/net/ip_conntrack so it knows where to return the response from the Internet to.
Only part of the output of:
# cat /proc/net/ip_conntrack

```


LVM CREATION
--------------

1. Total - 30 G # TOTAL DISK SIZE IS 30G
2. PV -  25G # Create 25G of PV
3. VG -  24G # Create 24G of VG from 25G PV
4. LVM - 22G # Create 22G of of LVM from 24G VG

Use -L followed by a specific size (e.g., gigabytes) to set an exact size.
Use -l followed by a number or percentage to specify the size in terms of logical extents or a percentage of available space.


| **No.** | **Task**                           | **Command**                                                                                   |
|---------|------------------------------------|-----------------------------------------------------------------------------------------------|
| **1**   | Partition Attached Disks          | `fdisk /dev/sdb` <br> `fdisk /dev/sdc`                                                       |
| **2**   | Physical Volume (PV) Creation     | `pvcreate /dev/sdb1` <br> `pvcreate /dev/sdc1`                                               |
| **3**   | Physical Volume (PV) Removal      | `pvremove /dev/sdb5`                                                                         |
| **4**   | Volume Group (VG) Creation        | `vgcreate -s 23G docker_vgs /dev/sdb1` <br> `vgcreate -s 23G docker_vgs /dev/sdc1`           |
| **5**   | Logical Volume (LV) Creation      | `lvcreate -L 22G -n docker_lvm docker_vgs`                                                   |
| **6**   | Format LVM                        | `mkfs.ext4 /dev/docker_vgs/docker_lvm`                                                       |
| **7**   | Mount LVM                         | `mkdir /opt/docker_lib` <br> `mount /dev/docker_vgs/docker_lvm /opt/docker_lib` <br> `df -h` |
| **8**   | Verify in fstab                   | `cat /etc/fstab | grep -i docker` <br> `/dev/mapper/docker_vgs-docker_lvm /opt/docker_lib ext4 defaults 0 0` |

| **No.** | **Task**                          | **Command**                                                                                                   |
|---------|-----------------------------------|---------------------------------------------------------------------------------------------------------------|
| **1**   | Create Physical Volume (PV)      | `pvcreate /dev/sda1`                                                                                         |
| **2**   | Extend Volume Group (VG)         | `vgextend vg_tecmint /dev/sda1`                                                                               |
| **3**   | Check Volume Group (VG) Size     | `vgs`                                                                                                        |
| **4**   | List Physical Volumes in VG      | `pvscan`                                                                                                     |
| **5**   | Check Available Physical Extent (PE) Size | `vgdisplay`                                                                                                  |
| **6**   | Extend Logical Volume (LV)       | `lvextend -l +4607 /dev/vg_tecmint/LogVol01`                                                                 |
| **7**   | Resize the File System           | `resize2fs /dev/vg_tecmint/LogVol01`                                                                         |
| **8**   | Notes                            | - There are 4607 free PEs available, equivalent to 18GB free space. <br> - Use `+` to add space during LV extension. |


| **No.** | **Task**                                | **Command**                                                                                              |
|---------|-----------------------------------------|----------------------------------------------------------------------------------------------------------|
| **1**   | Check Logical Volumes (LVs)            | `lvs`                                                                                                   |
| **2**   | Check File-System Information          | `df -h`                                                                                                 |
| **3**   | Unmount the File System                | `umount -v /mnt/tecmint_reduce_test/`                                                                    |
| **4**   | Check File-System for Errors           | `e2fsck -ff /dev/vg_tecmint_extra/tecmint_reduce_test`                                                   |
| **5**   | Reduce the File-System Size            | `resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10GB`                                               |
| **6**   | Reduce Logical Volume by GB Size       | `lvreduce -L -8G /dev/vg_tecmint_extra/tecmint_reduce_test`                                              |
| **7**   | Reduce Logical Volume by PE Size       | `lvreduce -l -2048 /dev/vg_tecmint_extra/tecmint_reduce_test`                                            |
| **8**   | Verify Logical Volume Size             | `lvdisplay vg_tecmint_extra`                                                                             |
| **9**   | Re-Size the File-System                | `resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test`                                                    |
| **10**  | Mount the File System Back             | `mount /dev/vg_tecmint_extra/tecmint_reduce_test /mnt/tecmint_reduce_test/`                              |
| **11**  | Verify Partition and Files             | `lvdisplay vg_tecmint_extra`                                                                             |


| **No.** | **Task**                                          | **Command**                                                     |
|---------|---------------------------------------------------|-----------------------------------------------------------------|
| **1**   | Convert Linear Logical Volume to Mirrored Volume | `lvconvert -m1 datavg/testlv`                                   |
| **2**   | Show Configuration of Mirrored Volume            | `lvs -a -o name,copy_percent,devices datavg`                    |
| **3**   | Show Detailed Segment Configuration of Volume     | `lvs --all --segments -o +devices`                              |
| **4**   | Convert Mirrored Volume to Linear Volume         | `lvconvert -m0 datavg/testlv /dev/sdc`                          |
| **5**   | Check Status of Volume and Devices               | `lvs -a -o +devices`                                            |
| **6**   | Check Detailed Volume Configuration by Name      | `lvs -a -o name,devices datavg`                                 |


| **No.** | **RAID Level** | **Description**                                                                                      |
|---------|----------------|------------------------------------------------------------------------------------------------------|
| **1**   | General RAID   | 1. Storage technology that combines multiple disk drive components into logical units.              |
|         |                | 2. Data is distributed across the drives.                                                           |
| **2**   | RAID 0         | 1. No redundancy.                                                                                   |
|         |                | 2. Provides improved performance.                                                                   |
|         |                | 3. No fault tolerance.                                                                              |
| **3**   | RAID 1         | 1. Provides disk mirroring.                                                                         |
|         |                | 2. Provides twice the read transaction rate of a single disk and the same write transaction rate.    |
| **4**   | RAID 2         | 1. Stripes data at the bit level rather than the block level.                                       |
|         |                | 2. Includes error-correcting coding.                                                                |
| **5**   | RAID 3         | 1. Provides byte-level striping with dedicated parity.                                              |
| **6**   | RAID 4         | 1. Provides block-level striping with a dedicated parity disk.                                      |
|         |                | 2. Suitable for large sequential reads.                                                             |
| **7**   | RAID 5         | 1. Provides block-level striping with distributed parity.                                           |
|         |                | 2. Can tolerate a single disk failure.                                                              |
|         |                | 3. Balances performance, redundancy, and storage efficiency.                                        |
| **8**   | RAID 10        | 1. Combines RAID 1 (mirroring) and RAID 0 (striping).                                               |
|         |                | 2. Provides high performance and redundancy.                                                        |
|         |                | 3. Requires a minimum of 4 disks.                                                                   |



| **Term**     | **Description**                                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------|
| **Parity**   | Technique of checking whether data has been lost or written correctly when moved in storage.        |
| **Redundancy** | Having multiple components with the same function, ensuring the system continues to work if one fails. |


| **#** | **Task**                                                                                          | **Description**                                                                                                        |
|-------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 1     | **Physical System Security**                                                                      | Configure BIOS to disable booting from CD/DVD, External Devices, Floppy Drive. Enable BIOS password, protect GRUB.     |
| 2     | **Disk Partitions**                                                                                | Create separate partitions to protect data. Ensure third-party apps are installed on separate file systems (/opt).      |
| 3     | **Minimize Packages to Minimize Vulnerability**                                                   | Avoid unnecessary packages. Use `chkconfig` to remove unwanted services and `yum -y remove` to delete packages.         |
| 4     | **Check Listening Network Ports**                                                                 | Ensure no unwanted ports are open.                                                                                      |
| 5     | **Use Secure Shell (SSH)**                                                                         | Avoid Telnet and rlogin. Use SSH with encrypted communication. Modify SSH settings in `/etc/ssh/sshd_config`.           |
| 6     | **Lockdown Cronjobs**                                                                              | Use `/etc/cron.allow` and `/etc/cron.deny` to control cronjob access.                                                   |
| 7     | **Disable USB Stick Detection**                                                                    | Prevent USB storage devices from being detected by adding `install usb-storage /bin/true` in `/etc/modprobe.d/no-usb`.  |
| 8     | **Turn on SELinux**                                                                                | Enable SELinux to enforce security policies. Modes: Enforcing, Permissive, Disabled.                                  |
| 9     | **Remove KDE/GNOME Desktops**                                                                     | Remove unnecessary graphical desktops to increase security and performance using `yum groupremove "X Window System"`.    |
| 10    | **Turn Off IPv6**                                                                                 | Disable IPv6 if not needed, edit `/etc/sysconfig/network` to set `NETWORKING_IPV6=no` and `IPV6INIT=no`.                |
| 11    | **Restrict Users Not to Use Old Passwords**                                                       | Set up PAM to avoid using old passwords with `/etc/pam.d/system-auth` or `/etc/pam.d/common-password`.                |
| 12    | **Enforcing Stronger Passwords**                                                                  | Use `pam_cracklib` to enforce stronger passwords in `/etc/pam.d/system-auth`.                                          |
| 13    | **How to Check Password Expiration of User**                                                      | Use the `chage` command to check and modify user password expiration.                                                  |
| 14    | **Lock and Unlock Account Manually**                                                              | Lock accounts with `passwd -l accountName` instead of removing them.                                                   |
| 15    | **Enable Iptables (Firewall)**                                                                    | Enable firewall with iptables to filter network traffic and prevent unauthorized access.                              |
| 16    | **Disable Ctrl+Alt+Delete in Inittab**                                                             | Disable shutdown with `Ctrl+Alt+Delete` by commenting the relevant line in `/etc/inittab`.                             |
| 17    | **Checking Accounts for Empty Passwords**                                                         | Find accounts with empty passwords using `cat /etc/shadow | awk -F: '($2==""){print $1}'`.                               |
| 18    | **Display SSH Banner Before Login**                                                               | Display legal or security warnings before SSH login by modifying SSH banner settings.                                  |
| 19    | **Monitor User Activities**                                                                        | Use tools like `psacct` and `acct` to track user activities and processes.                                            |
| 20    | **Review Logs Regularly**                                                                          | Regularly check system logs such as `/var/log/message`, `/var/log/auth.log`, `/var/log/kern.log`, etc.                 |
| 21    | **Keep /boot as Read-Only**                                                                        | Set `/boot` as read-only in `/etc/fstab` to prevent unauthorized modification of critical files.                        |
| 22    | **Ignore ICMP or Broadcast Request**                                                               | Ignore ICMP requests or broadcast requests by modifying `/etc/sysctl.conf`.                                            |



 




```

vivek hostname=/etc/init.d/httpd start, /etc/init.d/httpd stop,/etc/init.d/httpd restart, /sbin/services httpd restart
webalizer ALL=NOPASSWD: /sbin/service httpd start, /sbin/service httpd stop, /sbin/service httpd restart
ls *csv | awk -F"." '{print"mv -v "$0" "$1".txt"}' | sh
ps aux  |  grep -i csp_build  |  awk '{print $2}'  |  xargs  kill -9
grep -rl 'apples' /opt | xargs sed -i 's/apples/oranges/g'
for i in *.txt; do mv "$i" "unix$i"; done
top -b -n1 | sed -n '1,/^$/p'
find test9/* -type f -exec chmod 777 {} ";"

```

| **Type**            | **Description**                                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| **Environment Variables** | Allows customization of system behavior and application behavior. These variables are system-wide and inherited by child processes and shells. |
| **Shell Variables** | Applicable only to the current shell instance. Each shell (e.g., zsh, bash) has its own set of internal variables. |


| **Command**  | **Description**                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------|
| **env**      | Allows running a program in a custom environment without modifying the current one. When used without an argument, it prints a list of current environment variables. |
| **printenv** | Prints all or the specified environment variables.                                                      |
| **set**      | Sets or unsets shell variables. When used without an argument, it prints a list of all variables, including environment and shell variables, and shell functions. |
| **unset**    | Deletes shell and environment variables.                                                                 |
| **export**   | Sets environment variables.                                                                               |

| **System Call** | **Description**                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| **fork()**      | Used to create a new process.                                                    |
| **exec()**      | Used to execute a new process.                                                   |
| **wait()**      | Used to make the process wait for a child process to finish.                     |
| **exit()**      | Used to exit or terminate the process.                                           |
| **getpid()**    | Used to find the unique process ID (PID) of the current process.                 |
| **getppid()**   | Used to check the parent process ID (PPID).                                      |
| **nice()**      | Used to bias the priority of the currently running process (adjusts process priority). |


| **Aspect**      | **Process**                                                                 | **Thread**                                                                 |
|-----------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Definition**  | A program in execution, controlled by a Process Control Block (PCB).         | A segment of a process, multiple threads can exist within a single process. |
| **Control Block** | Process Control Block (PCB) holds information like process ID, state, priority, CPU, etc. | Threads are part of a process and share resources such as memory. |
| **Creation**    | A process can create other processes, known as child processes.               | A thread is created within a process and multiple threads can exist in a single process. |
| **Memory Sharing** | Processes are isolated and do not share memory with other processes.        | Threads within a process share memory and resources. |
| **Termination** | A process may take more time to terminate as it involves multiple components. | Threads terminate quickly as they are smaller units of execution. |
| **States**      | A process can have states like new, ready, running, waiting, terminated.     | A thread has three states: running, ready, and blocked. |





| **Property**                        | **Description**                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| **Creation**                        | A single system call can create more than one thread.                                            |
| **Data Sharing**                    | Threads share data and information.                                                            |
| **Memory Sharing**                  | Threads share instructions, global, and heap regions, but each thread has its own register and stack. |
| **Thread Management**               | Thread management consumes very few, or no system calls because communication between threads can be achieved using shared memory. |





## What is the issue behind getting an error “filesystem is full” while there is space available when you check it through “df” command? How will you rectify this problem?

| **Issue**                          | **Explanation**                                                                                                                                             |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Filesystem Full Error**          | The error occurs when a filesystem reports full, even if there is space available according to the `df` command. This can happen due to several reasons, such as:    |
| **Inode Exhaustion**               | Even if there is available space, the filesystem may have run out of inodes, which are needed to store file metadata.                                        |
| **Solution - Check Inodes**        | Use the command `df -i` to check the inode usage. If inodes are exhausted, try deleting unnecessary files or increasing inode allocation during filesystem creation. |
| **Filesystem Reserved Space**      | Some filesystems (like ext4) reserve a portion of space for root or system processes. This reserved space is not available to users.                           |
| **Solution - Check Reserved Space**| Check for reserved space with `tune2fs -l /dev/sdX` (replace `/dev/sdX` with your partition). If necessary, reduce the reserved space using `tune2fs -m <value> /dev/sdX`. |
| **Large Files or Unaccounted Space**| Sometimes, files might be held by deleted processes, or large log files are not accounted for in `df` output.                                                  |
| **Solution - Check for Open Files** | Use `lsof | grep deleted` to find open files that have been deleted but are still using space. You can terminate the processes holding those files.              |


## What is a Swap Space and Swap Partition?
| **Aspect**                  | **Swap Space**                                                                                                                                                            | **Swap Partition**                                                                                                                                                            |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**               | Swap space refers to space on a disk that the system uses as virtual memory when RAM is full. This can be a file or a partition.                                           | A swap partition is a dedicated partition on the hard drive used exclusively for swap space.                                                                                   |
| **Type**                     | Can be a swap file or a swap partition.                                                                                                                                     | Always a partition, not a file.                                                                                                                                                 |
| **Usage**                    | The system uses swap space to move data from RAM to disk to free up memory for other processes.                                                                           | Works the same as swap space but is allocated as a partition. It's often faster due to being a dedicated block.                                                                 |
| **Creation**                 | Can be created as a swap file using a normal file system (e.g., `/swapfile`).                                                                                             | Requires partitioning the disk (e.g., using `fdisk` or `parted`) and creating a separate partition specifically for swap.                                                       |
| **Performance**              | Can be slower than a swap partition due to the overhead of file system access.                                                                                            | Typically faster than a swap file since it’s a dedicated partition and does not require file system overhead.                                                                  |
| **Flexibility**              | More flexible since the size of a swap file can be changed dynamically (increase or decrease in size).                                                                    | Less flexible because the size of a swap partition is fixed at the time of creation and cannot be easily modified without repartitioning.                                        |
| **Management**               | Managed by file system tools and can be resized or deleted like any other file.                                                                                           | Managed by disk partitioning tools and requires reformatting to change size or delete.                                                                                        |
| **Commands for Setup**       | `dd if=/dev/zero of=/swapfile bs=1M count=1024` to create a swap file.<br>`mkswap /swapfile` to format.<br>`swapon /swapfile` to activate.                               | `fdisk /dev/sdX` to create partition.<br>`mkswap /dev/sdX1` to format.<br>`swapon /dev/sdX1` to activate.                                                                     |
| **Storage Efficiency**       | More efficient in terms of space allocation, as it uses available file system space.                                                                                       | Less efficient as it takes up dedicated disk space that cannot be used for anything else.                                                                                      |
| **System Impact**            | Using swap files can lead to fragmentation on the disk, potentially impacting performance.                                                                                | No fragmentation issue as it’s a dedicated partition.                                                                                                                          |
| **Example Use Case**         | Ideal for systems where flexibility and dynamic resizing of swap space are needed.                                                                                       | Ideal for systems where performance and stability are more important, and a fixed swap space allocation is required.                                                            |

| **Aspect**                          | **sar Command**                                                                                         | **Proc File System (procfs)**                                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Definition**                      | `sar` (System Activity Reporter) is a Linux command used for collecting, reporting, and saving system activity information. | `procfs` is a virtual file system that provides information about processes and system resources. It is created at boot time and removed at shutdown. |
| **Purpose**                         | Primarily used for monitoring and analyzing system performance by collecting statistics on CPU, memory, disk I/O, etc. | Provides process information and allows communication between kernel space and user space.                                     |
| **Data Collected**                  | CPU usage, memory usage, disk I/O, network activity, and other system resources.                         | Information about running processes, system performance, kernel statistics, and configurations (e.g., `/proc/cpuinfo`, `/proc/meminfo`). |
| **Location**                        | Typically available as a command-line tool.                                                             | Found in the `/proc` directory on the Linux system.                                                                            |
| **Usage**                           | `sar -u` - To report CPU usage.<br>`sar -r` - To report memory usage.<br>`sar -d` - To report disk I/O. | `/proc/cpuinfo` - Displays processor details.<br>`/proc/meminfo` - Displays memory statistics.<br>`/proc/[pid]` - Information about specific processes. |
| **Data Persistence**                | Data can be saved and stored for later use.                                                               | Data is not persistent, and it is generated dynamically at runtime by the kernel.                                              |
| **Command for Installing**          | `sudo apt install sysstat` (Debian-based systems) or `sudo yum install sysstat` (RedHat-based systems). | `procfs` is typically part of the Linux kernel and does not need to be installed separately. It is always available after system boot. |
| **Real-Time Monitoring**            | Yes, `sar` provides real-time data and can be used for periodic system activity checks.                   | No, `procfs` reflects live system data but does not perform any monitoring by itself.                                          |
| **Output**                          | Provides summary reports on system activity over a time period.                                           | Provides raw, on-demand information about system processes and kernel parameters.                                             |
| **Example Commands**                | `sar -u 1 3` - CPU usage every second for 3 reports.<br>`sar -r 1 3` - Memory usage every second for 3 reports. | `cat /proc/cpuinfo` - Displays CPU information.<br>`cat /proc/meminfo` - Displays memory information.                          |



| **Aspect**                               | **Explanation**                                                                                                                                                          |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is Umask?**                       | Umask is used to determine the default file permissions for newly created files and directories. It helps control the default permissions.                                  |
| **Default Umask for Normal Users**       | The default umask for normal users is `002`, resulting in: <br> Default directory permissions: `775` <br> Default file permissions: `664`                                   |
| **Default Umask for Root User**          | The default umask for the root user is `022`, resulting in: <br> Default directory permissions: `755` <br> Default file permissions: `644`                                |
| **Range of Umask Values for Folders**    | The minimum and maximum UMASK value for a folder is `000` (full permissions) to `777` (no permissions).                                                                |
| **Range of Umask Values for Files**      | The minimum and maximum UMASK value for a file is `000` (full permissions) to `666` (no permissions).                                                                  |
| **Difference Between `0022` and `022`**  | There is no difference between `0022` and `022`; both indicate the same. The preceding `0` simply indicates that no SUID/SGID/Sticky bit information is set.               |
| **Preferred Umask for Security**         | The preferred umask value for security reasons is `027` (or `0027`), which restricts other users from reading, writing, or executing files/folders.                       |
| **Meaning of Umask `022` in vsftpd Config** | In a `vsftpd` config file, umask `022` indicates that files created by users will have permissions `644` (readable by everyone, writable by owner) and directories `755`. |


| **Aspect**                             | **Explanation**                                                                                                                                                                  |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is ulimit?**                    | `ulimit` is a command used to limit the resources that a process can use. It is useful to prevent programs from consuming too many resources and impacting system performance.     |
| **Use Case for Memory Limiting**       | You can use `ulimit -v` to limit the amount of memory that processes in a shell can use, preventing the system from slowing down when a program runs out of memory.                |
| **Checking File Limits**               | Use the command `cat /proc/sys/fs/file-max` to check the system’s limit for the maximum number of open files.                                                                   |
| **ulimit Command Options**             | The `ulimit` command is used to display and set resource limits for the logged-in user. Use `ulimit -a` to print all resource limits for the current user.                      |
| **Fix for Maximum File Limit Reached** | When the limit on the maximum number of open files is reached, run the following command as root to increase the limit: <br> `sysctl -w fs.file-max=100000` <br> Result: `fs.file-max = 100000` |







```
/etc/security/limits.conf
# hard limit for max opened files for linuxtechi user
linuxtechi       hard    nofile          4096
# soft limit for max opened files for linuxtechi user
linuxtechi       soft    nofile          1024
# hard limit for max number of process for oracle user
oracle           hard    nproc          8096
# soft limit for max number of process for oracle user
oracle           soft    nproc          4096
```

| **Feature**                         | **Soft Limit**                                         | **Hard Limit**                                      |
|-------------------------------------|--------------------------------------------------------|----------------------------------------------------|
| **Definition**                      | A user-defined limit that can be modified but cannot exceed the hard limit. | A system-defined limit that cannot be exceeded by the user. |
| **Command to View**                 | `ulimit -S -a`                                          | `ulimit -H -a`                                      |
| **Command to Set Soft Limit**       | `ulimit -S [option] [number]`                           | Not applicable for setting soft limits directly.   |
| **Example of Setting Soft Limit**  | `ulimit -S -s 8192` (sets stack size soft limit to 8192) | Not applicable for setting hard limits directly.   |
| **Minimum Value**                   | 0                                                      | Same as the soft limit, but user cannot set hard limit lower than system-defined value. |
| **Maximum Value**                   | Can be set equal to the hard limit.                     | User cannot exceed the hard limit.                |



| **Aspect**                           | **Explanation**                                                                                                                                                                          |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is MBR?**                     | MBR stands for Master Boot Record. It is the first sector of a bootable disk, typically located at `/dev/hda` or `/dev/sda`.                                                              |
| **Size of MBR**                      | MBR is less than 512 bytes in size.                                                                                                                                                        |
| **Components of MBR**                | MBR contains three components: <br> 1) Primary boot loader information in the first 446 bytes. <br> 2) Partition table information in the next 64 bytes. <br> 3) MBR validation check in the last 2 bytes. |
| **MBR Functionality**                | It contains information about the boot loader (such as GRUB or LILO in older systems). MBR loads and executes the GRUB boot loader, initiating the system boot process.                  |


| **Runlevel** | **Description**                           |
|--------------|-------------------------------------------|
| 0            | Halt                                      |
| 1            | Single user mode                          |
| 2            | Multiuser, without NFS                    |
| 3            | Full multiuser mode                       |
| 4            | Unused                                    |
| 5            | X11 (Graphical mode)                      |
| 6            | Reboot                                    |


| **Step**                             | **Action**                                         |
|--------------------------------------|----------------------------------------------------|
| 1. Init                              | Starts `getty`                                     |
| 2. Getty                             | Displays the login prompt                          |
| 3. Getty                             | Starts `/etc/login`                                |
| 4. Getty                             | Verifies credentials and starts the user's shell   |
| 5. Shell                             | Reads system-wide default files and specific files |
| 6. Shell                             | Reads shell-specific files                         |
| 7. Shell Prompt                      | Displays the shell prompt                          |




[...]
#LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
LogFormat "%{X-Forwarded-For}i %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
[...]


| **Permission Type** | **Description**                                                                 | **Command**                      |
|---------------------|---------------------------------------------------------------------------------|----------------------------------|
| **SUID (Set User ID)** | Temporarily gives the user permissions of the file owner when executing a file. | `chmod u+s file1.txt`            |
| **SGID (Set Group ID)** | Applies to executable files, allowing other users to run the file with the effective permissions of the file's owner. | `chmod 4750 file1.txt`           |
| **SGID (on directories)** | Allows users to inherit the group ID (GID) of the file’s group owner when creating files in a directory. | `chmod g+s freddy`               |
| **Sticky Bit** | Ensures that only the file owner, directory owner, or root can delete or rename files in a directory. | `chmod +t directory_name`        |



| **Type**    | **Description**                                                                 | **Example**                   |
|-------------|---------------------------------------------------------------------------------|-------------------------------|
| **Daemon**  | A process that runs in the background with no association with terminal TTY or pts. | System V init, cron           |
| **Process** | An instance of an executable, which can run in the background or foreground to perform activities. | Shell script, command         |
| **Services**| A type of process that runs in the background to provide services, usually not associated with a terminal. | Apache, x.initd, ftp, rsync   |


| **Feature**            | **Soft Link (Symbolic Link)**                               | **Hard Link**                                      |
|------------------------|-------------------------------------------------------------|----------------------------------------------------|
| **Definition**         | A symbolic link points to a file or directory by its path.   | A hard link points to the actual data blocks of the file. |
| **Command to Create**  | `ln -s source_file link_name`                               | `ln source_file link_name`                         |
| **Link Type**          | Creates a separate inode for the link.                       | Creates another directory entry for the same inode. |
| **File Deletion**      | If the original file is deleted, the link becomes broken.    | The file remains accessible through any existing hard links, even if the original file is deleted. |


| **Variable** | **Description**                                                                 | **Example**                        |
|--------------|---------------------------------------------------------------------------------|------------------------------------|
| `$#`         | Stores the number of command-line arguments passed to the shell program.         | `$#` represents the number of arguments passed. |
| `$?`         | Stores the exit value of the last executed command.                             | `echo $?` will display the exit status of the last command. |
| `$0`         | Stores the name of the script or the first word of the entered command.        | `echo $0` will display the script name or shell program. |
| `$*`         | Stores all the arguments entered on the command line, split by spaces.         | `echo $*` will display all arguments. |
| `"$@"`       | Stores all the arguments entered on the command line, individually quoted.     | `echo "$@"` will display each argument individually, preserving spacing. |
| `$!`         | Shows the process ID (PID) of the last background process.                      | `echo $!` will display the PID of the last background process. |
| `$$`         | Stores the process ID of the current shell.                                    | `echo $$` will display the shell's process ID. |
| `"$0"`       | The name of the script itself.                                                  | `echo "$0"` will display the name of the script. |
| `#!`         | The shebang operator, used to specify the interpreter location for a script.    | `#!/bin/bash` in the first line of a script. |
| `$-`         | Contains the current shell's flags and settings.                               | `echo $-` will display the active shell flags. |



| **#** | **Feature**             | **Nginx**                                                       | **Apache**                                                   |
|-------|-------------------------|-----------------------------------------------------------------|--------------------------------------------------------------|
| 1     | **Architecture**         | Event-driven and asynchronous.                                  | Process-based or thread-based depending on configuration.     |
| 2     | **Performance**          | Handles a large number of simultaneous connections efficiently. | Can be slower under high load due to process spawning.        |
| 3     | **Configuration**        | Uses a simple, declarative configuration format.                | Configuration is more complex with a variety of directives.   |
| 4     | **Resource Usage**       | Uses less memory and CPU due to its event-driven model.         | Higher memory consumption due to process/thread management.   |
| 5     | **Static Content**       | Extremely efficient in serving static content.                  | Not as efficient for serving static content compared to Nginx. |
| 6     | **Dynamic Content**      | Relies on external processors (e.g., PHP-FPM) for dynamic content. | Supports dynamic content natively using mod_php and other modules. |



```
iperf -s

iperf -c 127.0.0.1 -u 100

```

| **Command**     | **Description**                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| `sudo -i`        | Starts a login shell as the target user, applying their environment.                                |
| `sudo su -`      | Switches to the target user with a login shell but may not fully replicate their environment.        |


| **Field**           | **Value**  | **Explanation**                                                                 |
|---------------------|------------|---------------------------------------------------------------------------------|
| **Current Time**    | `13:05:19` | The current system time.                                                       |
| **Uptime**          | `1 day, 2:08` | The time since the system was last started (1 day, 2 hours, and 8 minutes).     |
| **Users Logged In** | `1 user`   | The number of users currently logged into the system.                           |
| **Load Average**    | `1.68, 1.63, 1.29` | Average system load over the last 1, 5, and 15 minutes.                         |

**Note:**
- **System Load** reflects the number of processes waiting for CPU time.
- Load averages below the number of CPU cores indicate the system is not overloaded.



| **Method**                     | **Command**                           | **Explanation**                                                                                     |
|--------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Using `su` Command**         | `su - username`                       | Switches to the target user's session. Prompts for the target user’s password.                     |
| **Using `sudo` Command**       | `sudo -i -u username`                 | Switches to the target user's session with a login shell. Requires `sudo` privileges.              |
| **Using `screen` or `tmux`**   | N/A                                   | Allows switching between sessions (possibly for different users) using a terminal multiplexer.      |
| **Using Virtual Console**      | `Ctrl+Alt+F3` (switch to console)     | Switches to another virtual console where you can log in as a different user.                      |
|                                | `Ctrl+Alt+F2` (return to session)     | Returns to the original session from the virtual console.                                           |




