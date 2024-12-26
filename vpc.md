
Question-01:

 ![image](https://github.com/user-attachments/assets/118f60fb-a01e-4ef8-aeff-95da6fe122d2)

Ans-01:   
![image](https://github.com/user-attachments/assets/11dc8816-f637-4377-8876-e311ec34fb7b)


Your organization had a vpc(10.10.0.0/16) setup with one public (10.10.1.0/24) and two private subnets - private subnet1(10.10.2.0/24) and private subnet2(10.10.3.0/24).
The public subnet has the main route table and two private subnets route tables respectively.
Aws Sysops team reports a problem starting the ec2 instance in private subnet1 can not communicate to RDS mysql on private subnet 2.





1. RDS Security group inbund rule is incorrectly configured with 10.10.1.0/24 instead of 10.10.2.0/24
2. 10.10.3.0/24 subnet NACL denies inbound on port 3306 subnet 10.10.2.0/24


