

রোহিত শর্মার Terraform রাজ্য (ফাইনাল সংস্করণ)
🏰 VPC কমপ্লেক্স

রাজ্যের নাম – aws_vpc

বিশাল CIDR Block (চারপাশের দেয়াল)

DNS Support + DNS Hostnames

Instance Tenancy

সাথে Tag: Name = "rohit-vpc"

🏘️ একাধিক Public ও Private পাড়া (Multi-AZ)

Public Subnets

ap-south-1a → Public Subnet A

ap-south-1b → Public Subnet B

প্রতিটা Subnet-এ আছে –

cidr_block

vpc_id

availability_zone

tags

Private Subnets

ap-south-1a → Private Subnet A

ap-south-1b → Private Subnet B

প্রতিটা Subnet-এও একই –

cidr_block

vpc_id

availability_zone

tags

🌉 NAT Gateway (গোপন সেতু)

Public Subnet A → NAT GW A (Elastic IP A সহ)

Public Subnet B → NAT GW B (Elastic IP B সহ)

প্রতিটা NAT GW-তে vpc_id + tags আছে।

🛣️ Public Routes

প্রতিটা Public Subnet-এর জন্য Public Route বানানো হলো –

vpc_id (কার রাজ্যে রাস্তা)

cidr_block (0.0.0.0/0) (সবাই যেতে পারবে)

gateway_id = Internet Gateway

📜 Route Tables ও Associations

Public Route Table A, B

প্রতিটা Public Subnet-এর জন্য আলাদা Route Table

ট্যাগ আছে: Name = "public-rt-a"

Private Route Table A, B

প্রতিটা Private Subnet-এর জন্য আলাদা Route Table

ট্যাগ আছে: Name = "private-rt-b"

Route Table Associations (aws_route_table_association)

Public Subnet A → Public Route Table A

Public Subnet B → Public Route Table B

Private Subnet A → Private Route Table A

Private Subnet B → Private Route Table B

প্রতিটা Association-এ থাকে –

for_each loop (একসাথে অনেক subnet bind করার জন্য)

subnet_id

route_table_id

🌐 Internet Gateway (বিশ্ব দরজা)

রাজ্যে একটাই দরজা বানানো হলো – aws_internet_gateway

এর ভেতরে থাকে –

vpc_id (কোন রাজ্যের জন্য দরজা খোলা)

tags (যেমন: Name = "rohit-igw")

📊 VPC Flow Logs (নজরদারি ব্যবস্থা)

aws_flow_log দিয়ে VPC-তে নজরদারি শুরু হলো।

ভেতরে থাকে –

vpc_id (কোন VPC-এর লগ হচ্ছে)

log_destination (CloudWatch Log Group / S3)

traffic_type = ALL

tags (যেমন: Name = "rohit-vpc-flow-log")

🎉 সারাংশ (Terraform Resource Details সহ)

aws_vpc → cidr_block, dns, tenancy, tags

aws_subnet → vpc_id, cidr_block, availability_zone, tags

aws_nat_gateway → vpc_id, elastic_ip, subnet_id, tags

aws_route → vpc_id, cidr_block, gateway_id

aws_route_table → vpc_id, tags

aws_route_table_association → for_each, subnet_id, route_table_id

aws_internet_gateway → vpc_id, tags

aws_flow_log → vpc_id, log_destination, traffic_type, tags
