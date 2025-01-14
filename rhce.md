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






The TTL (Time to Live) in the context of networking is a field in the IP header that determines the maximum number 
of hops (routers) a packet can pass through before being discarded. Each time the packet is forwarded by a router, the TTL value is decremented by 1.


Meaning in ttl=64:
64 is the initial TTL value set by the operating system (common defaults are 64, 128, or 255).
This value indicates how many hops are left before the packet would expire. Since you're pinging 127.0.0.1 (localhost), 
the packet doesn't traverse any routers, so the TTL remains at its initial value.




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

To remove GRUB password from Redhat Linux, use RHEL installation disk. To remove GRUB password from CentOS Linux, use CentOS installation disk.
From Troubleshooting options select Rescue a CentOS/RedHat Linux system option
Now select the first option which mounts the installed Linux in /mnt/sysimage directory.
Now run following commands
chroot /mnt/sysimage
chroot  command creates  environment with root privilege. After this command, whatever command we execute, will be executed as root


Now open the file etc/grub.d/40_custom and remove the directives which set the authentication at boot loader screen.
Once authentication directives are removed, save the file
Now run following commands
grub2-mkconfig –o tmp/grub.cfg
mv tmp/grub.cfg boot/grub2/
exit
reboot


How to recover root password?
-------------------------------


```
STEP 1. Boot Computer and Interrupt while booting at GRUB stage hitting ‘arrow‘ keys or “space bar“.
Press "e" to edit the first grub menu option and navigate to kernel line:

Press "e" key again to edit and remove:
quiet splash
init=/bin/bash

At this point, we have edited grub boot menu, and we are ready to boot. Press "b" key to boot.

After successfully boot you will be presented with bash command prompt:

mount -o remount,rw / mount -o remount,rw /proc
mount /proc
mount -o remount,rw /
passwd
Reboot

https://www.ostechnix.com/how-to-reset-or-recover-root-user-password-in-linux/
https://www.tecmint.com/reset-forgotten-root-password-in-rhel-centos-and-fedora/
https://linuxconfig.org/recover-reset-forgotten-linux-root-password

```

Network Bonding
----------------
mode=0 (balance-rr)
It follows Round-robin policy which is  default mode. 
It transmits packets in sequential order. 
This mode provides load balancing and fault tolerance.
mode=1 (active-backup)
Active-backup policy: 
In this mode, only one slave in the bond is active. 
The other one will become active, only when the active slave fails. 
The bond’s MAC address is externally visible on only one port (network adapter) to avoid confusing the switch. 
This mode provides fault tolerance.


mode=2 (balance-xor)
XOR policy: 
Transmit based on [(source MAC address XOR’d with destination MAC address) modulo slave count]. 
This selects the same slave for each destination MAC address. 
This mode provides load balancing and fault tolerance.
mode=3 (broadcast)
Broadcast policy: 
transmits everything on all slave interfaces. 
This mode provides fault tolerance.


mode=4 (802.3ad)
IEEE 802.3ad Dynamic link aggregation. 
Creates aggregation groups which share the same speed and duplex settings. 
Utilizes all slaves in the active aggregator according to the 802.3ad specification

mode=5 (balance-tlb)
Adaptive transmit load balancing: 
channel bonding which does not require any special switch support.
The outgoing traffic is distributed according to the current load 


mode=6 (balance-alb)
Adaptive load balancing: 
It does not require any special switch support. 
Receive load balancing is achieved by ARP negotiation



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



LINUX AS ROUTER
----------------
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


In a LAN with many hosts, the router keeps track of established connections in /proc/net/ip_conntrack so it knows where to return the response from the Internet to.
Only part of the output of:
# cat /proc/net/ip_conntrack


LVM CREATION
Total - 30 G # TOTAL DISK SIZE IS 30G 
1 PV -  25G # Create 25G of PV
1VG -  24G # Create 24G of VG from 25G PV
1 LVM - 22G # Create 22G of of LVM from 24G VG
Use -L followed by a specific size (e.g., gigabytes) to set an exact size.
Use -l followed by a number or percentage to specify the size in terms of logical extents or a percentage of available space.


Partition of Attached Disks
fdisk  /dev/sdb
fdisk /dev/sdc


PV CREATION

pvcreate /dev/sdb1 
pvcreate /dev/sdc1

PV REMOVE 
pvremove /dev/sdb5

VOLUME GROUP CREATION

vgcreate -s 23G docker_vgs /dev/sdb1
vgcreate -s 23G docker_vgs /dev/sdc1

LVM CREATION

lvcreate -L 22G -n docker_lvm docker_vgs



FORMAT LVM

mkfs.ext4 /dev/docker_vgs/docker_lvm


MOUNT LVM
mkdir /opt/docker_lib
mount /dev/docker_vgs/docker_lvm /opt/docker_lib
df -h


cat /etc/fstab | grep -i docker
/dev/mapper/docker_vgs-docker_lvm        /opt/docker_lib ext4 defaults 0 0


LVEXTEND
pvcreate /dev/sda1

Extending Volume Group
vgextend vg_tecmint /dev/sda1
Let us check the size of a Volume Group now using
vgs
We can even see which PV are used to create particular Volume group using.
pvscan
For getting the available Physical Extend size run.
vgdisplay


There are 4607 free PE available = 18GB Free space available. 
So we can expand our logical volume up-to 18GB more. 
Let us use the PE size to extend.
lvextend -l +4607 /dev/vg_tecmint/LogVol01
Use + to add the more space. After Extending, we need to re-size the file-system using.
resize2fs /dev/vg_tecmint/LogVol01


Let’s see what are the 5 steps below.
unmount the file system for reducing.
Check the file system after unmount.
Reduce the file system.
Reduce the Logical Volume size than Current size.
Recheck the file system for error.
Remount the file-system back to stage.
While reducing size, we need to reduce only 8GB so it will roundup to 10GB after the reduce
lvs
Here we can see the file-system information
df -h
umount -v /mnt/tecmint_reduce_test/


Then check for the file-system error using following command.

e2fsck -ff /dev/vg_tecmint_extra/tecmint_reduce_test
Next, reduce the file-system.

resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10GB
Reduce the Logical volume using GB size.

lvreduce -L -8G /dev/vg_tecmint_extra/tecmint_reduce_test
lvdisplay vg_tecmint_extra


lvreduce -l -2048 /dev/vg_tecmint_extra/tecmint_reduce_test
Re-size the file-system back, In this step if there is any error that means we have messed-up our file-system.
resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test
Mount the file-system back to same point.
mount /dev/vg_tecmint_extra/tecmint_reduce_test /mnt/tecmint_reduce_test/
Check the size of partition and files.
lvdisplay vg_tecmint_extra


The following command converts the linear logical volume ‘datavg/testlv’ to a mirrored logical volume :
lvconvert -m1 datavg/testlv
The below commands shows the configuration of the volume after the lvconvert command changed the volume to a volume with two mirror copies.
lvs -a -o name,copy_percent,devices datavg
lvs --all --segments -o +devices


The following command converts the mirrored logical volume datavg/testlv to a linear logical volume, removing or breaking the mirror copy including the mirrored devices
lvconvert -m0 datavg/testlv /dev/sdc
Check the status of volume and devices again to see the difference :
lvs -a -o +devices
lvs -a -o name,devices datavg


Raid
1. Storage Technology which combine multiple disk drive components in to logical units.
2.Data is distributed across the drive 

Raid 0
1. It has no redundancy
2. provide improved performance
3. It has no fault tolerance


Raid1
1.Provide Disk mirroring
2.Provide twice read transaction rate of single disk and  same write transaction rate of single disk

Raid2
1. Stripes data at bit level rather than block level
2. Error correcting coding

Raid3
1.Provide byte level  striping with dedicated parity


Parity
Technique of checking whether data has been lost or written when it is moved from one place to another place in storage 
Redundancy
Having multiple components with same function so that If one will fail then also entire system can continue to work 


1. Physical System Security
Configure the BIOS to disable booting from CD/DVD, External Devices, Floppy Drive in BIOS. 
enable BIOS password 
protect GRUB with password to restrict physical access of your system.
2. Disk Partitions
By creating different partitions, data can be separated and grouped
When an unexpected accident occurs, only data of that partition will be damaged,
while the data on other partitions survived
Make sure you must have following separate partitions and 
sure that third party applications should be installed on separate file systems under /opt.


3.Minimize Packages to Minimize Vulnerability
It’s recommended to avoid installing useless packages to 
avoid vulnerabilities in packages
Find and remove or disable unwanted services from the server 
to minimize vulnerability. Use the ‘chkconfig‘ command to
find out services which are running on runlevel 3
/sbin/chkconfig --list |grep '3:on'
chkconfig serviceName off
yum -y remove package-name
4.Check Listening Network Ports

5. Use Secure Shell(SSH)
Telnet and rlogin protocols uses plain text, not encrypted format which is the security breaches. SSH is a secure protocol that use encryption technology during communication with server.
Never login directly as root unless necessary. Use “sudo” to execute commands. sudo are specified in /etc/sudoers file also can be edited with the “visudo” utility which opens in VI editor.
It’s also recommended to change default SSH 22 port number with some other higher level port number. Open the main SSH configuration file and make some following parameters to restrict users to access.
# vi /etc/ssh/sshd_config
Use SSH Protocol 2 Version
AllowUsers username
PermitRootLogin no


7. Lockdown Cronjobs
Cron has it’s own built in feature, where it allows to specify who may,
and who may not want to run jobs. This is controlled by the use of files
called /etc/cron.allow and /etc/cron.deny.
8. Disable USB stick to Detect
Create a file ‘/etc/modprobe.d/no-usb‘ and adding below line will not detect USB storage.
install usb-storage /bin/true


9. Turn on SELinux
Security-Enhanced Linux (SELinux) is a compulsory access control 
security mechanism provided in the kernel. Disabling SELinux means removing security mechanism from the system
Enforcing: This is default mode which enable and enforce the SELinux security policy on the machine.
Permissive: In this mode, SELinux will not enforce the security policy on the system,
only warn and log actions. This mode is very useful in term of troubleshooting SELinux related issues.
Disabled: SELinux is turned off.


10. Remove KDE/GNOME Desktops
There is no need to run X Window desktops like KDE or GNOME on your dedicated LAMP server. 
You can remove or disable them to increase security of server and performance. 
To disable simple open the file ‘/etc/inittab‘ and set run level to 3
yum groupremove "X Window System"


11. Turn Off IPv6
If you’re not using a IPv6 protocol, then you should disable
it because most of the applications or policies not required IPv6
protocol and currently it doesn’t required on the server
vi /etc/sysconfig/network
NETWORKING_IPV6=no
IPV6INIT=no


12. Restrict Users not to Use Old Passwords
The old password file is located at /etc/security/opasswd.
This can be achieved by using PAM module.
Open ‘/etc/pam.d/system-auth‘ file under RHEL / CentOS / Fedora.
vi /etc/pam.d/system-auth #centos
vi /etc/pam.d/common-password #ubuntu
#auth        sufficient    pam_unix.so likeauth nullok
password   sufficient    pam_unix.so nullok use_authtok md5 shadow remember=5

15. Enforcing Stronger Passwords
The ‘pam_cracklib‘ module is available in PAM (Pluggable Authentication Modules)
module stack which will force user to set strong passwords.
vi /etc/pam.d/system-auth
/lib/security/$ISA/pam_cracklib.so retry=3 minlen=8 lcredit=-1 ucredit=-2 dcredit=-2 ocredit=-1
vi /etc/pam.d/common-password #ubuntu
#auth        sufficient    pam_unix.so likeauth nullok
password   sufficient    pam_unix.so nullok use_authtok md5 shadow remember=5


13. How to Check Password Expiration of User
In Linux, user’s passwords are stored in ‘/etc/shadow‘ file in encrypted format.
To check password expiration of user’s, you need to use ‘chage‘ command.
It displays information of password expiration details along with last password change date
chage -l username
To change password aging of any user, use the following command.
#chage -M 60 username
#chage -M 60 -m 7 -W 7 userName
-M Set maximum number of days -m Set minimum number of days -W Set the number of days of warning

14. Lock and Unlock Account Manually
The lock and unlock features are very useful, instead of
removing an account from the system, you can lock it for an week or a month.
To lock a specific user, you can use the follow command.
passwd -l accountName


16. Enable Iptables (Firewall)
It’s highly recommended to enable Linux firewall to secure unauthorised access of your servers. Apply rules in iptables to filters incoming, outgoing and forwarding packets. 
17. Disable Ctrl+Alt+Delete in Inittab
This is defined in ‘/etc/inittab‘ file, if you look closely in that file you will see a line similar to below.
# Trap CTRL-ALT-DELETE
#ca::ctrlaltdel:/sbin/shutdown -t3 -r now
By default line is not commented out. We have to comment it out. This particular key sequence signalling will shut-down a system

18. Checking Accounts for Empty Passwords
Empty password accounts are security risks and that can be easily hackable. To check if there were any accounts with empty password, use the following command
cat /etc/shadow | awk -F: '($2==""){print $1}'
19. Display SSH Banner Before Login
It’s always a better idea to have an legal banner or security 
banners with some security warnings before SSH authentication. 
To set such banners read the following article

20. Monitor User Activities
If you are dealing with lots of users, then its important to 
collect the information of each user activities and processes consumed
by them and analyse them at a later time or in case if any kind of performance, security issues
There are two useful tools called ‘psacct‘ and ‘acct‘
are used for monitoring user activities and processes on a system. 


21. Review Logs Regularly
Linux default log files name and their usage:
/var/log/message – Where whole system logs or current activity logs are available.
/var/log/auth.log – Authentication logs.
/var/log/kern.log – Kernel logs.
/var/log/cron.log – Crond logs (cron job).
/var/log/maillog – Mail server logs.
/var/log/boot.log – System boot log.
/var/log/mysqld.log – MySQL database server log file.
/var/log/secure – Authentication log.


24. Keep /boot as read-only
Linux kernel and its related files are in /boot directory which is by default as read-write.
Changing it to read-only reduces the risk of unauthorized modification of 
critical boot files. To do this, open “/etc/fstab” file.
vi /etc/fstab
LABEL=/boot     /boot     ext2     defaults,ro     1 2

25.Ignore ICMP or Broadcast Request
Add following line in “/etc/sysctl.conf” file to ignore ping or broadcast request.
Ignore ICMP request:
net.ipv4.icmp_echo_ignore_all = 1
Ignore Broadcast request:
net.ipv4.icmp_echo_ignore_broadcasts = 1

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

Environment variables
It allows to customize how the system works and the behavior of the applications on the system
These are available system-wide and are inherited by all spawned child processes and shells.
These are set of dynamic named values, stored within the system which are used by applications 
Shell variables 
These are only applicable to the current shell instance. 
Each shell such as zsh and bash, has its own set of internal shell variables.


env – The command allows you to run another program in a custom environment without modifying the current one. When used without an argument it will print a list of the current environment variables.
printenv – The command prints all or the specified environment variables.
set – The command sets or unsets shell variables. When used without an argument it will print a list of all variables including environment and shell variables, and shell functions.
unset – The command deletes shell and environment variables.
export – The command sets environment variables

Explain system calls used for process management?
Answer: There are some system calls used in Linux for process management. These are as follows:
Fork(): It is used to create a new process
Exec(): It is used to execute a new process
Wait(): It is used to make the process to wait
Exit(): It is used to exit or terminate the process
Getpid(): It is used to find the unique process ID
Getppid(): It is used to check the parent process ID
Nice(): It is used to bias the currently running process property


Process:
Process means any program is in execution. Process control block controls the operation of any process. Process control block contains the information about processes for example: Process priority, process id, process state, CPU, register etc. A process can creates other processes which are known as Child Processes. Process takes more time to terminate and it is isolated means it does not share memory with any other process.
Thread:
Thread is the segment of a process means a process can have multiple threads and these multiple threads are contained within a process. A thread have 3 states: running, ready, and blocked.


Properties of Thread
Here are important properties of Thread:
Single system call can create more than one thread
Threads share data and information.
Threads shares instruction, global, and heap regions. However, it has its register and stack.
Thread management consumes very few, or no system calls because of communication between threads that can be achieved using shared memory


What is the issue behind getting an error “filesystem is full” while there is space available when you check it through “df” command? How will you rectify this problem?
When all the inodes are consumed then even though you have free space, you will get the error that filesystem is full. So, to check whether there is space available, we have to use the command df –i.  Sometimes, it may happen file system or storage unit contains the substantial number of small files, and each of the files takes 128 bytes of the inode structure then inode structure fills up, and we will not be able to copy any more file to the disk. So, to rectify the problem, you need to free the space in inode storage, and you will be able to save more files.
What is a Swap Space or Swap Partition?
When we have insufficient RAM space in the system and we need more RAM to process our applications then Linux allows an extra allocation of RAM in the physical hard disk which is called a swap space. It is used to hold current programs that are currently running in the system


The sar (System Activity Reporter) command is a versatile Linux tool used for monitoring and reporting system activity statistics. It helps system administrators track and analyze the performance of various system components

Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down.
It contains the useful information about the processes that are currently running, it is regarded as control and information centre for kernel.
The proc file system also provides communication medium between kernel space and user space.


Umask
It is use to determine the file permission for newly created files. 
It can be used to control the default file permission for new files. 
It is a four-digit octal number
The default umask 002 used for normal user. 
default directory permissions : 775  default file permissions : 664
The default umask for the root user is 022 result 
default directory permissions:755 default file permissions:644
The minimum and maximum UMASK value for a folder is 000 and 777
The minimum and maximum UMASK value for a file is 000 and 666


I see people are using 0022 and 022 as UMASK, is there any difference between them?
There is no difference between these two, both indicates one and the same. The preceding 0 indicates there is no SUID/SGID/Sticky bit information set.
What is the preferred UMASK value for a system for Security reasons?
Preferred is 027 (0027) for security reasons because this will restrict others not to read/write/execute that file/folder
5) I see umask value as 022 in my vsftpd config file? What actually this mean to world?
When you see 022 as umask value in vsftpd config file that indicates that users who are going to create files will get 644  and for folders it’s 755 respectively.


ulimit allows you to limit the resources that a process can use. Two use cases: You have a program that sometimes runs out of memory, slowing your computer down to a crawl. You can use ulimit -v to limit the amount of memory that processes in a shell can use
cat /proc/sys/fs/file-max
ulimit (user limit) is used to display and set resources limit for logged in user.When we run ulimit command with -a option then it will print all resources’ limit for the logged in user
How to fix the problem when limit on number of Maximum Files was reached ?
root@ubuntu~]# sysctl -w fs.file-max=100000
fs.file-max = 100000


/etc/security/limits.conf
# hard limit for max opened files for linuxtechi user
linuxtechi       hard    nofile          4096
# soft limit for max opened files for linuxtechi user
linuxtechi       soft    nofile          1024
# hard limit for max number of process for oracle user
oracle           hard    nproc          8096
# soft limit for max number of process for oracle user
oracle           soft    nproc          4096


A soft limit, however, can be changed by the user but cannot exceed the hard limit i.e. It can have minimum 0 value and maximum value as equal to 'hard limit'.

ulimit -S -a view all soft limits
ulimit -H -a view all hard limits
ulimit -S [option] [number] set a specific soft limit for one variable
e.g. ulimit -S -s 8192 set a new soft stacksize limit, “-s” is for stack
ulimit -H [option] [number] set a specific hard limit for one variable
e.g. ulimit -H -s 8192 see


MBR stands for Master Boot Record.
It is located in the 1st sector of the bootable disk. Typically /dev/hda, or /dev/sda
MBR is less than 512 bytes in size. This has three components 
          1) primary boot loader info in 1st 446 bytes 
          2) partition table info in next 64 bytes 
          3) mbr validation check in last 2 bytes.
It contains information about GRUB (or LILO in old systems).
So, in simple terms MBR loads and executes the GRUB boot loader


0 – halt
1 – Single user mode
2 – Multiuser, without NFS
3 – Full multiuser mode
4 – unused
5 – X11
6 – reboot


Init starts getty
Getty shows login prompt
getty starts /etc/login
getty verifies the credential and starts users shell
Shell reads system wide default files and specific default files
Shell specific file read
Shell Prompt

[...]
#LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
LogFormat "%{X-Forwarded-For}i %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
[...]


SUID is defined as giving temporary permissions to a user to run a program/file with the permissions of the file owner rather that the user who runs it
SGID is a special file permission for executable files which enables other users to run the file with effective permissions of the file owner
chmod u+s file1.txt
chmod 4750 file1.txt
SGID is a special file permission that also applies to executable files and enables other users to inherit the effective GID of file group owner
chmod g+s freddy


Daemon - is a kind of process that runs in background as no association with terminal TTY or pts the example can be System V init etc.
Process - is a instance of an executable, for example a shell script or a command that you can run on background or foreground for performing some activities.
Services - it is a again another kind of process mostly not associated with terminal and runs in background to provide some services 
as Apache , x.initd which contains ftp, rsync etc. It basically to provide user a service as a server


















