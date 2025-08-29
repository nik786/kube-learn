


- [VPC-TRANSIT-GW-GUIDE](https://www.youtube.com/watch?v=GV4KreiF_D4&t=1207s)

- [VPC-PEERING](https://www.youtube.com/watch?v=36qsohuPzMQ&t=1119s)


Transit Gateway
----------------


vpc-01
------

vpc-cidr: 192.168.0.0/16

public-subnet-us-east-1a: 192.168.11.0/24
public-subnet-us-east-1b: 192.168.12.0/24


connect vpc-01 to vpc-02 and vpc-03
------------------------------------

Route Table
------------

192.168.0.0/16     local
0.0.0.0            Internet Gateway
10.0.0.0/16        Transit Gateway ID
172.16.0.0/16      Transit Gateway ID





vpc-02
--------
Route Table
------------

vpc-cidr: 10.0.0.0/16

public-subnet-us-east-1a: 10.0.1.0/24
public-subnet-us-east-1b: 10.0.2.0/24



connect vpc-02 to vpc-01 and vpc-03
------------------------

Route Table
------------

10.0.0.0/16         local
0.0.0.0             Internet Gateway
192.168.0.0/16      Transit Gateway ID
172.16.0.0/16       Transit Gateway ID


vpc-03
--------
Route Table
------------

vpc-cidr: 172.16.0.0/16

public-subnet-us-east-1a: 172.16.1.0/24
public-subnet-us-east-1b: 172.16.2.0/24



connect 
------------------------

Route Table
------------

172.16.0.0/16      local
0.0.0.0            Internet Gateway
192.168.0.0/16      Transit Gateway ID
172.16.0.0/16       Transit Gateway ID
                  



Testing
-------
Install nginx on ec2 nodes


vpc-01
------

curl private ip of ec2 node which locates in vpc-02

curl private ip of ec2 node which locates in vpc-03

vpc-02
------

curl private ip of ec2 node which locates in vpc-01

curl private ip of ec2 node which locates in vpc-03


vpc-03
------

curl private ip of ec2 node which locates in vpc-01

curl private ip of ec2 node which locates in vpc-02




/16 → 65,536 total → 65,531 usable

/20 → 4,096 total → 4,091 usable

/22 → 1,024 total → 1,019 usable

/24 → 256 total → 251 usable

/25 → 128 total → 123 usable


vpc-cidr: 10.0.0.0/16  -  2^(32-n) - 5 = 65531 usable

public-subnet-us-east-1a: 10.0.1.0/24 => (256-5) =  251 host
public-subnet-us-east-1b: 10.0.2.0/24 => (256-5) =  251 host

Total host = 502

case-01(find total ips): 2^(32-n)
-----------------
n=/24,/21,/23,/25,/26

usable hosts = 2^(32-24) = 2^8 = 256


case-02(find usable ips): (2^n) -2 
------------------------------------

x=subnet=/24,/21,/23,/25,/26

n = hostbits = (32-x) = (32-24) = 8

usable hosts = (2^n) -2 = (2^8) -2= 256-2 = 254


Where 2^n is used?
------------------

To get the total number of IP addresses in a subnet.

Example: /24 → 2^(32-24) = 2^8 = 256 total IPs.


Where 2^n – 2 is used
---------------------
In traditional networking to calculate usable hosts (excluding network + broadcast).

Example: /24 → 256 total – 2 = 254 usable hosts






--------



vpc-cidr: 10.0.0.0/20 - 2^(32-20) - 5 = 4091 usable

public-subnet-us-east-1a: 10.0.1.0/21 => (2048-5) = 2043  host
public-subnet-us-east-1b: 10.0.2.0/21 => (2048-5) = 2043 host

Total host = 4086



vpc-cidr: 10.0.0.0/22 - 2^(32-22) - 5 = 1019 usable

public-subnet-us-east-1a: 10.0.1.0/23 => (512-5)=507  host
public-subnet-us-east-1b: 10.0.2.0/23 => (512-5)=507  host

Total host = 1014


vpc-cidr: 10.0.0.0/24 - 2^(32-24) - 5 = 251 usable

public-subnet-us-east-1a: 10.0.1.0/25 => (128-5)=123 host
public-subnet-us-east-1b: 10.0.2.0/25 => (128-5)=123 host

Total host = 246


- I used 2^n to find the total IPs.

- Then applied 2^n – 2 (standard) OR 2^n – 5 (AWS).





vpc-peering
------------

vpc-01
------
Requester vpc

vpc-cidr: 192.168.0.0/16

public-subnet-us-east-1a: 192.168.11.0/24
public-subnet-us-east-1b: 192.168.12.0/24


connect vpc-01 to vpc-02 and vpc-03
------------------------------------

Route Table
------------

192.168.0.0/16     local
0.0.0.0            Internet Gateway
10.0.0.0/16        Peering Connection(pcx-2398648323)





vpc-02
--------
Route Table
------------

Acceptor vpc

Accept Request

vpc-cidr: 10.0.0.0/16

public-subnet-us-east-1a: 10.0.1.0/24
public-subnet-us-east-1b: 10.0.2.0/24



10.0.0.0/16         local
0.0.0.0             Internet Gateway
192.168.0.0/16      Peering Connection(pcx-2398648323)






