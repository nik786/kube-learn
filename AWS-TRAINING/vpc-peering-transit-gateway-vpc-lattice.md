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

Destination                 Target
192.168.0.0/16              local
pl-7865226                  vpce-2273hsgdhs


private_subnet_1b
-------------------
private_subnet_1b_name: retina_vpc-private-1b

private_subnet_1b_cidr: 192.168.15.0/24

az: ap-south-1b

available_ipv4_addresses: 245

retina_vpc-private-route-table

Destination                 Target
192.168.0.0/16              local
pl-7865226                  vpce-2273hsgdhs



public_subnet_1a
-------------------
public_subnet_1a_name: retina_vpc-public-1a

public_subnet_1a_cidr: 192.168.11.0/24

az: ap-south-1a

available_ipv4_addresses: 250

retina_vpc-public-route-table

Destination                 Target
192.168.0.0/16              local
0.0.0.0/0                   igw-0165615361


public_subnet_1b
-------------------
public_subnet_1b_name: retina_vpc-public-1b

public_subnet_1b_cidr: 192.168.12.0/24

az: ap-south-1b

available_ipv4_addresses: 250

retina_vpc-public-route-table

Destination                 Target
192.168.0.0/16              local
0.0.0.0/0                   igw-0165615361















