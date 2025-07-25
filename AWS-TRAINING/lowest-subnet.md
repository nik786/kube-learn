

## 📊 AWS Subnet Size Limitations

| CIDR Block | Total IPs | Usable IPs in AWS | Allowed in AWS? | Notes |
|------------|-----------|-------------------|------------------|-------|
| `/32`      | 1         | 0                 | ❌ No             | Single IP, used for host routes only |
| `/31`      | 2         | 0                 | ❌ No             | Special case for point-to-point links (RFC 3021) |
| `/30`      | 4         | 0                 | ❌ No             | All IPs consumed by AWS reserved + network/broadcast |
| `/29`      | 8         | 3                 | ❌ No             | Not enough usable IPs after AWS reserves 5 |
| `/28`      | 16        | 11                | ✅ Yes            | **Smallest subnet size allowed** in most AWS services |



| **Class**         | **Network Prefix Bits** | **Example IP Address** | **Network Address** | **Host Address** |
|--------------------|-------------------------|-------------------------|---------------------|------------------|
| **Class A**        | 8                      | 48.0.0.2               | 48                  | 0.0.2            |
| **Class B**        | 16                     | 192.16.0.2             | 192.16              | 0.2              |
| **Class C**        | 24                     | 192.168.2.1            | 192.168.2           | 1                |
| **Classless (CIDR)** | Variable (VLSM)       | N/A                    | Based on subnet mask | Remaining bits  |


Can I use all the IP addresses that I assign to a subnet?

No. Amazon reserves the first four (4) IP addresses and the last one (1) IP address of every subnet for IP networking purposes


| **CIDR Block**   | **Subnet**         | **Supported IP Addresses** | **IP Address Range**         |
|-------------------|--------------------|----------------------------|-------------------------------|
| 10.0.0.0/8       | Very Large Network | 16,777,216                 | 10.0.0.0 - 10.255.255.255    |
| 10.0.0.0/16      | Large Network      | 65,536                     | 10.0.0.0 - 10.0.255.255      |
| 10.0.0.0/17      | Medium-Large Network | 32,768                  | 10.0.0.0 - 10.0.127.255      |
| 10.0.0.0/18      | Medium Network     | 16,384                     | 10.0.0.0 - 10.0.63.255       |
| 10.0.0.0/20      | Medium Network     | 4,096                      | 10.0.0.0 - 10.0.15.255       |
| 10.0.0.0/21      | Medium Network     | 2,048                      | 10.0.0.0 - 10.0.7.255        |
| 10.0.0.0/22      | Medium-Small Network | 1,024                    | 10.0.0.0 - 10.0.3.255        |
| 10.0.0.0/23      | Small Network      | 512                        | 10.0.0.0 - 10.0.1.255        |
| 10.0.0.0/24      | Small Network      | 256                        | 10.0.0.0 - 10.0.0.255        |
| 10.0.0.0/25      | Subnet 1           | 128                        | 10.0.0.0 - 10.0.0.127        |
| 10.0.0.128/25    | Subnet 2           | 128                        | 10.0.0.128 - 10.0.0.255      |
| 10.0.0.0/26      | Smaller Subnet     | 64                         | 10.0.0.0 - 10.0.0.63         |
| 10.0.0.0/27      | Very Small Subnet  | 32                         | 10.0.0.0 - 10.0.0.31         |
| 10.0.0.0/30      | Point-to-Point Link| 4                          | 10.0.0.0 - 10.0.0.3          |
| 10.0.0.0/32      | Single IP Address  | 1                          | 10.0.0.0                     |



| **CIDR Block**    | **Allowed Range**                | **Description**                                             |
|--------------------|----------------------------------|-------------------------------------------------------------|
| **VPC CIDR Block** | /16 to /28                     | Allowed IPv4 CIDR block size for creating a VPC.            |
| **Subnet CIDR Block** | /16 to /28                 | Allowed IPv4 CIDR block size for creating subnets in a VPC. |

| **Reserved IP Address** | **IP Address**  | **Purpose**                                                                 |
|--------------------------|-----------------|-----------------------------------------------------------------------------|
| Network Address          | 10.0.0.0       | Identifies the network; cannot be assigned to resources.                   |
| VPC Router               | 10.0.0.1       | Reserved by AWS for the VPC router.                                        |
| DNS Server               | 10.0.0.2       | Reserved by AWS; IP is base CIDR + 2. Used for DNS server and internal purposes. |
| Reserved for Future Use  | 10.0.0.3       | Reserved by AWS for future use.                                            |
| Broadcast Address        | 10.0.0.255     | Reserved as the network broadcast address. Broadcast is not supported in VPC. |

### Notes:
- The first four IP addresses and the last IP address in each subnet CIDR block are reserved and unavailable for resources.
- After creating a VPC, additional IPv4 CIDR blocks can be associated with it to extend the network.
- The allowed block sizes ensure optimal resource allocation and subnetting flexibility.

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html
https://k21academy.com/amazon-web-services/aws-solutions-architect/aws-vpc-and-subnets/


```
azs              = ["us-east-1a", "us-east-1b"]
vpc_cidr         = "10.0.0.0/16"
public_subnets   = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnets  = ["10.0.3.0/24", "10.0.4.0/24"]
vpc_name         = "gl-net"
```


# Recommended IPv4 CIDR Ranges for VPCs

| VPC Name      | CIDR Block      | IP Range              | Notes                            |
|---------------|-----------------|------------------------|----------------------------------|
| VPC-1         | 10.0.0.0/16     | 10.0.0.0 – 10.0.255.255 | Already used                     |
| VPC-2         | 10.1.0.0/16     | 10.1.0.0 – 10.1.255.255 | Safe and contiguous              |
| VPC-3         | 10.2.0.0/16     | 10.2.0.0 – 10.2.255.255 | Separate private space           |
| VPC-4         | 192.168.0.0/16  | 192.168.0.0 – 192.168.255.255 | RFC1918 private range         |






