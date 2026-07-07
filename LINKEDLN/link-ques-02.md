1. How do you uncommit the changes that have already been pushed to GitHub? 

```
# Revert the specific commit (replace <commit-hash> with the actual hash)
git revert <commit-hash>

# Push the new revert commit to GitHub
git push

```

2. If there is suddenly the file is deleted in git how do you get it back?

```
# To recover a deleted file that was tracked by Git
git checkout HEAD -- <path-to-deleted-file>


```

4. Can you increase the size of the root volume without shutting down the instance?

```
Yes, you can increase the size of the root volume without shutting down
the instance by modifying the volume in the 
AWS Management Console or using the AWS CLI with the modify-volume command.
After resizing, extend the filesystem inside the running instance to utilise the new space

aws ec2 modify-volume --volume-id <volume-id> --size <new-size-in-GB>
aws ec2 describe-volumes-modifications --volume-id <volume-id>
resize2fs /dev/<root-device>
xfs_growfs /
```

4. If you lost the .pem file then how will you connect to EC2? 

If you lost the .pem file, create a new key pair in AWS, then access the EC2 instance via an existing user with proper access (like another admin). 
Alternatively, use the Systems Manager Session Manager or create a new key pair, update the instance's ~/.ssh/authorized_keys file via another instance or EBS volume attachment

5. S3 bucket having a policy for only read-only but you’re having full access for you? Can you modify s3 objects? 
No, you cannot modify S3 objects because the bucket policy enforces read-only access, and bucket policies override individual user permissions. To modify objects, the bucket policy must explicitly allow write access

6. Difference between Classic ELB and Application ELB?
7. How many subnets are assigned to the routing table? 

A single routing table can be associated with multiple subnets, but each subnet can be associated with only one routing table at a time
a routing table can be associated with up to 200 subnets by default



8. In your VPC all IPS are finished you require resources how to provision it? 

If all IPs in your VPC are used, you can either:

Add a new subnet with a larger or different CIDR block in the same VPC.
Expand the VPC's CIDR block using the VPC CIDR block association feature, if there's available IP space

9. Are you only using cloud watch for monitoring?
10.If your using load balancing in 2 availability zones den which load balancer you should use?


If you're using load balancing across two availability zones, you should use an Application Load Balancer (ALB) or a Network Load Balancer (NLB), depending on your use case:

ALB: Best suited for HTTP/HTTPS traffic with advanced routing, URL path-based routing, and SSL termination.
NLB: Ideal for handling TCP/UDP traffic with high performance and low latency, especially for non-HTTP traffic.




12. Is it possible to run any VM in AWS without creating any EC2 instance ? 

No, it is not possible to run a virtual machine (VM) in AWS without creating an EC2 instance, as EC2 (Elastic Compute Cloud) 
is the service that provides VM-like compute resources in AWS. If you need to run VMs, you must create EC2 instances.

However, you can use services like AWS Lightsail for simpler VM provisioning or AWS Fargate for containerized applications, 
but these still rely on EC2 under the hood

13. I want to create a pipeline in Jenkins which needs to have 10 different stages and based on my input it needs to execute some stages not every stages how you will configure that .



14. What are the Terraform modules? Have used any modules in the project?

15. Is it possible to configure communication between 2 servers those are having private access

16. What happens when you delete /var/lib/docker/overlay?
 deleting /var/lib/docker/overlay removes the filesystems of your containers, leading to potential data loss and failure of containers, 
 so it's advisable to be cautious when performing this action
 
17. Write a simple script that calls with “Foo” prints “bar” and when called with “bar” prints “foo”. Every other option should print “Try 
again”?

def respond(input_value):
    if input_value == "Foo":
        print("bar")
    elif input_value == "bar":
        print("foo")
    else:
        print("Try again")

# Test the function
input_value = input("Enter a value: ")
respond(input_value)








