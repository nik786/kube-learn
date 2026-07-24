vpc peering

gl-subnet-1a:

gl-subnet-1b:


transit gw

gl-subnet-1c:

gl-subnet-1d:

gl-subnet-1e:



vpc without natgw, with vpc endpoints:
--------------------------------------

vpc_name: retina_vpc

private_subnet_1a
-------------------
private_subnet_1a_name: retina_vpc-private-1a

private_subnet_1a_cidr: 192.168.14.0/24

az: ap-south-1a

available_ipv4_addresses: 242

retina_vpc-private-route-table



```md
| Destination    | Target          |
|----------------|-----------------|
| 192.168.0.0/16 | local           |
| pl-7865226     | vpce-2273hsgdhs |
```




private_subnet_1b
-------------------
private_subnet_1b_name: retina_vpc-private-1b

private_subnet_1b_cidr: 192.168.15.0/24

az: ap-south-1b

available_ipv4_addresses: 245

retina_vpc-private-route-table



```md
| Destination    | Target          |
|----------------|-----------------|
| 192.168.0.0/16 | local           |
| pl-7865226     | vpce-2273hsgdhs |
```




public_subnet_1a
-------------------
public_subnet_1a_name: retina_vpc-public-1a

public_subnet_1a_cidr: 192.168.11.0/24

az: ap-south-1a

available_ipv4_addresses: 250

retina_vpc-public-route-table



```md
| Destination    | Target          |
|----------------|-----------------|
| 192.168.0.0/16 | local           |
| 0.0.0.0/0      | igw-0165615361 |
```



public_subnet_1b
-------------------
public_subnet_1b_name: retina_vpc-public-1b

public_subnet_1b_cidr: 192.168.12.0/24

az: ap-south-1b

available_ipv4_addresses: 250

retina_vpc-public-route-table



```md
| Destination    | Target          |
|----------------|-----------------|
| 192.168.0.0/16 | local           |
| 0.0.0.0/0      | igw-0165615361 |
```







# transit_gateway_subnets.md


transit gateway architecture:
-----------------------------

vpc_name: retina_vpc

transit_gateway_name: retina_tgw

transit_gateway_id: tgw-0abc123456789xyz

attached_vpcs:
- retina_vpc
- shared_services_vpc
- monitoring_vpc




transit_subnet_1a
-------------------

transit_subnet_1a_name: retina_vpc-transit-1a

transit_subnet_1a_cidr: 192.168.21.0/28

az: ap-south-1a

total_ipv4_addresses: 16

aws_reserved_ipv4_addresses: 5

usable_ipv4_addresses:
2^(32-28) - 5 = 16 - 5 = 11

available_ipv4_addresses: 10

used_ipv4_addresses: 1

purpose:
- Transit Gateway attachment ENI
- Inter-VPC routing
- Shared services communication

associated_route_table:
retina_vpc-transit-route-table



| Destination    | Target               |
|----------------|----------------------|
| 192.168.0.0/16 | local                |
| 10.0.0.0/8     | tgw-0abc123456789xyz |
| 172.16.0.0/12  | tgw-0abc123456789xyz |




transit_subnet_1b
-------------------

transit_subnet_1b_name: retina_vpc-transit-1b

transit_subnet_1b_cidr: 192.168.22.0/28

az: ap-south-1b

total_ipv4_addresses: 16

aws_reserved_ipv4_addresses: 5

usable_ipv4_addresses:
2^(32-28) - 5 = 16 - 5 = 11

available_ipv4_addresses: 10

used_ipv4_addresses: 1

purpose:
- HA Transit Gateway attachment
- Cross-AZ routing
- Shared VPC communication

associated_route_table:
retina_vpc-transit-route-table



| Destination    | Target               |
|----------------|----------------------|
| 192.168.0.0/16 | local                |
| 10.0.0.0/8     | tgw-0abc123456789xyz |
| 172.16.0.0/12  | tgw-0abc123456789xyz |




transit route table notes:
---------------------------

Transit Gateway ENI consumes:
- 1 IP per subnet/AZ

Transit subnets should:
- remain dedicated
- avoid EC2 deployments
- avoid ALB/NLB placement
- avoid EKS node placement

recommended subnet size:
- /28 minimum
- /27 preferred for future scaling

why /28 is usually sufficient:
------------------------------

usable IPs:
11

typical usage:
- 1 TGW ENI
- few future ENIs
- management overhead

remaining free IPs:
~9-10

This keeps IP wastage minimal.



architecture flow:
------------------

Application VPC
      |
      v
Transit Gateway
      |
      +--> Shared Services VPC
      |
      +--> Monitoring VPC
      |
      +--> Security VPC



recommended best practices:
----------------------------

- Dedicated TGW subnets only
- Separate route tables
- No internet routing inside TGW subnets
- No NAT Gateway required
- Keep TGW subnets isolated
- Use centralized inspection/security VPC if scaling
- Enable route propagation carefully
```











