

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

| **Reserved IP** | **Purpose**                                                                 |
|------------------|------------------------------------------------------------------------------|
| `.0` (first IP)   | **Network address** – Identifies the subnet itself (e.g., 10.0.0.0/24)     |
| `.1`              | **VPC router** – Handles routing within the subnet                         |
| `.2`              | **DNS** – Reserved for Amazon DNS (if enabled)                             |
| `.3`              | **Future use** – Reserved by AWS for potential networking enhancements     |
| `.255` (last IP)  | **Broadcast address** – Reserved though AWS doesn't support broadcasting   |







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


## ✅ How to Use Low-Range IPv4 CIDRs for VPCs

| CIDR Block         | Total IPs | Usable IPs | Recommended Use                  |
|--------------------|-----------|------------|----------------------------------|
| 10.0.0.0/24        | 256       | 251        | Small dev/test VPCs              |
| 10.0.1.0/25        | 128       | 123        | Lab/sandbox environments         |
| 192.168.100.0/26   | 64        | 59         | PoC or single-AZ workloads       |

> **❗Note:** AWS reserves 5 IPs per subnet, so usable IPs = total − 5

---

## ⚠️ Important Notes

- Minimum CIDR block size for a **VPC** is `/28` (16 IPs).
- You **cannot shrink** a VPC CIDR block after creation — plan ahead.
- For **production workloads**, use `/22–/24` per subnet inside a `/20` or `/21` VPC for supporting autoscaling, NAT, etc.
- You can **add secondary CIDR blocks** to the VPC later to expand IP space.

---

## 🔧 Example: Small VPC for Dev (Terraform)

```hcl
# CIDR block with only 256 IPs (great for test/dev)
cidr_block = "10.10.10.0/24"

```

### VPC CIDR Overview /16 and /26 combination

| VPC Name        | CIDR Range     | Total IPs | Usable IPs |
|-----------------|----------------|-----------|------------|
| gl-vpc-01-cidr  | 10.0.0.0/16    | 65,536    | ~65,531    |

### Subnet Breakdown

| Subnet Name             | CIDR Range        | Subnet Type | Total IPs | Usable IPs | AZ           |
|-------------------------|-------------------|-------------|-----------|------------|--------------|
| gl-public-subnet-1a     | 10.0.10.0/26       | Public      | 64        | 59         | ap-south-1a  |
| gl-public-subnet-1b     | 10.0.10.64/26      | Public      | 64        | 59         | ap-south-1b  |
| gl-public-subnet-1c     | 10.0.10.128/26     | Public      | 64        | 59         | ap-south-1c  |
| gl-private-subnet-1a    | 10.0.20.0/26       | Private     | 64        | 59         | ap-south-1a  |
| gl-private-subnet-1b    | 10.0.20.64/26      | Private     | 64        | 59         | ap-south-1b  |
| gl-private-subnet-1c    | 10.0.20.128/26     | Private     | 64        | 59         | ap-south-1c  |







# VPC and Subnet Planning for /24 CIDR and /26 combination

## VPC Details

| VPC Name      | CIDR Block     | Total IPs | Usable IPs | Notes                       |
|---------------|----------------|-----------|------------|-----------------------------|
| gl-vpc-01     | 10.0.0.0/24    | 256       | 251        | Small test/dev environment  |

## Subnet Plan

| Subnet Name             | CIDR Block        | Subnet Type | Total IPs | Usable IPs | Availability Zone |
|-------------------------|-------------------|-------------|-----------|------------|-------------------|
| gl-public-subnet-1a     | 10.0.0.0/26        | Public      | 64        | 59         | ap-south-1a       |
| gl-public-subnet-1b     | 10.0.0.64/26       | Public      | 64        | 59         | ap-south-1b       |
| gl-private-subnet-1a    | 10.0.0.128/26      | Private     | 64        | 59         | ap-south-1a       |
| gl-private-subnet-1b    | 10.0.0.192/26      | Private     | 64        | 59         | ap-south-1b       |




## Common Valid Subnets under /24

| Subnet Mask | Subnet Count | IPs per Subnet | Usable IPs | Example CIDRs                          | Notes                                |
|-------------|---------------|----------------|------------|----------------------------------------|--------------------------------------|
| /25         | 2             | 128            | 126        | 10.0.0.0/25, 10.0.0.128/25             | Largest possible subnets in /24      |
| /26         | 4             | 64             | 62         | 10.0.0.0/26, 10.0.0.64/26, etc.        | Common for public/private subnetting |
| /27         | 8             | 32             | 30         | 10.0.0.0/27, 10.0.0.32/27, etc.        | Good for small isolated services     |
| /28         | 16            | 16             | 14         | 10.0.0.0/28, 10.0.0.16/28, etc.        | Often used for load balancers, etc.  |
| /29         | 32            | 8              | 6          | 10.0.0.0/29, 10.0.0.8/29, etc.         | Minimal services or management nodes |
| /30         | 64            | 4              | 2          | 10.0.0.0/30, 10.0.0.4/30, etc.         | Point-to-point links                 |
| /31         | 128           | 2              | 0 or 2     | 10.0.0.0/31, 10.0.0.2/31, etc.         | Used in router-to-router links (RFC 3021) |
| /32         | 256           | 1              | 0          | 10.0.0.0/32, 10.0.0.1/32, etc.         | Single host routes                   |

### 🔹 Summary

- **Minimum subnet under `/24`**: `/32` — 256 subnets, 1 IP each
- **Maximum subnet under `/24`**: `/25` — 2 subnets, 128 IPs each








### VPC CIDR Overview /16 and /24 combination

| VPC Name        | CIDR Range     | Total IPs | Usable IPs |
|-----------------|----------------|-----------|------------|
| gl-vpc-01-cidr  | 10.0.0.0/16    | 65,536    | ~65,531    |

### Subnet Breakdown

| Subnet Name             | CIDR Range        | Subnet Type | Total IPs | Usable IPs | AZ           |
|-------------------------|-------------------|-------------|-----------|------------|--------------|
| gl-public-subnet-1a     | 10.0.10.0/24       | Public      | 256       | 251        | ap-south-1a  |
| gl-public-subnet-1b     | 10.0.10.64/24      | Public      | 256        | 251         | ap-south-1b  |
| gl-public-subnet-1c     | 10.0.10.128/24    | Public      |  256      | 251         | ap-south-1c  |
| gl-private-subnet-1a    | 10.0.20.0/24       | Private     | 256        | 251         | ap-south-1a  |
| gl-private-subnet-1b    | 10.0.20.64/24      | Private     | 256        | 251         | ap-south-1b  |
| gl-private-subnet-1c    | 10.0.20.128/24    | Private     | 256        | 251         | ap-south-1c  |


```

Number of Subnets = 2ⁿ
n = number of bits borrowed from host portion to create subnets.


subnetting 192.168.1.0/24 into /26

26 - 24 = 2 bits from the host part

Number of Subnets = 2² = 4 subnets


192.168.1.0/26

192.168.1.64/26

192.168.1.128/26

192.168.1.192/26



Usable Host IPs = 2ⁿ - 2 (standard)
                = 2ⁿ - 5 (on AWS)


n = number of bits left for host portion (32 - subnet mask)


The 32 in the formula 32 - subnet mask refers to the total number of bits in an IPv4 address

Example: 192.168.1.1 → Binary: 11000000.10101000.00000001.00000001
                          (8 bits)  (8 bits)  (8 bits)  (8 bits)
                          => 8 × 4 = 32 bits total

The full IPv4 address has 32 bits

A subnet mask (e.g., /24) indicates how many bits are used for the network portion

Subnet mask: /26 → means 26 bits for network


Remaining 6 bits for host:


32 - 26 = 6 (host bits)

2^6 - 2 = 62 usable IPs (or -5 in AWS)



For 192.168.1.0/26:

Host bits = 32 - 26 = 6

Standard usable hosts = 2⁶ - 2 = 62

In AWS, usable = 2⁶ - 5 = 59

172.31.64.0/20 = 4091





```

