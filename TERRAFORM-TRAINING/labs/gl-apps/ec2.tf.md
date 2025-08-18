
```
cat /modules/ec2/main.tf

## Variables
variable "ami" {
  description = "AMI ID to use for the instances"
  type        = string
}

variable "instance_types" {
  description = "A map of instance types and their counts"
  type        = map(number)
}

variable "environment_name" {
  description = "Environment name prefix for tagging"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID for fetching subnets"
  type        = string
}

## Data sources
data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_subnets" "public" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }

  filter {
    name   = "tag:Type"
    values = ["public"]
  }
}

## EC2 resource
resource "aws_instance" "this" {
  # Expand the map of instance_types into unique keys per instance
  for_each = {
    for type, count in var.instance_types :
    for i in range(count) :
    "${type}-${i}" => {
      type = type
      idx  = i
    }
  }

  ami           = var.ami
  instance_type = each.value.type

  # Round-robin distribute across public subnets
  subnet_id = data.aws_subnets.public.ids[each.value.idx % length(data.aws_subnets.public.ids)]

  # Round-robin distribute across availability zones
  availability_zone = data.aws_availability_zones.available.names[each.value.idx % length(data.aws_availability_zones.available.names)]

  tags = {
    Name        = "${var.environment_name}-${each.key}"
    Environment = var.environment_name
  }
}

## Outputs (use map instead of flat lists for better traceability)
output "instance_ids" {
  description = "EC2 Instance IDs keyed by name"
  value       = { for k, inst in aws_instance.this : k => inst.id }
}

output "public_ips" {
  description = "Public IPs of EC2 instances keyed by name"
  value       = { for k, inst in aws_instance.this : k => inst.public_ip }
}

output "private_ips" {
  description = "Private IPs of EC2 instances keyed by name"
  value       = { for k, inst in aws_instance.this : k => inst.private_ip }
}



```




## Ec2 module definition in root directory

```

cat ec2. tf


variable "environment_name" {
  type    = string
  default = "gl-dev"
}

variable "region" {
  type    = string
  default = "ap-south-1"
}

variable "vpc_cidr" {
  type    = string
  default = "192.168.0.0/16"
}

variable "instance_types" {
  description = "A map of instance types and their counts"
  type        = map(number)
  default = {
    "t2.small" = 1
    "t2.micro" = 2
  }
}

module "ec2" {
  source           = "../modules/ec2"
  ami              = "ami-0214abac5533f716b"
  instance_types   = var.instance_types
  environment_name = var.environment_name
  vpc_id           = module.vpc.vpc_id
}

```

# 🐘 Terraform EC2 মডিউলের গল্প

একটা সময়ের কথা...  

**Terraform গ্রামে** একটা বিশাল VPC রাজ্য ছিল। এই রাজ্যে অনেকগুলো এলাকা ছিল—কেউ **Public Subnet**, আবার কেউ **Private Subnet**।  
রাজ্যে সবসময় নিয়ম শৃঙ্খলা বজায় রাখতে একজন দারোয়ান ছিল, যার নাম **Availability Zone**।  
সে সবসময় বলত, "সব জিনিস সঠিক জায়গায় ভাগ করে দাও, তাহলে রাজ্য শান্ত থাকবে।"  

---

## ভ্যারিয়েবলরা: রাজ্যের চরিত্র  

- `ami` → রাজ্যের নকশা (Blueprint), নতুন ঘর (EC2 Instance) বানানোর ছাঁচ।  
- `instance_types` → রাজ্যে কত ধরনের ঘর থাকবে, যেমন ছোট কুটির (t2.micro) আর মাঝারি ঘর (t2.small)।  
- `environment_name` → রাজ্যের নামের ট্যাগ, যেন প্রতিটা ঘর নিজের পরিচয় রাখতে পারে।  
- `vpc_id` → কোন রাজ্যে (VPC) ঘরগুলো হবে, তার চাবি।  

---

## ডেটা সোর্স: রাজ্যের মানচিত্র  

- `aws_availability_zones` → দারোয়ান (AZ) বলছে কোন কোন পাড়া (Zone) ব্যবহারযোগ্য।  
- `aws_subnets.public` → Public এলাকা, যেখানে সাধারণ মানুষ (ইন্টারনেট) সহজেই আসতে পারে।  

---

## EC2 ইনস্ট্যান্স: রাজ্যের ঘরবাড়ি  

Terraform বলে দিল:  
"প্রতিটা ঘরের জন্য আলাদা নাম দাও। যেমন — `t2.micro-0`, `t2.micro-1`, `t2.small-0`।  
যাতে গন্ডগোল না হয়।"

- প্রতিটা ঘর বানানোর সময় →  
  - **AMI** থেকে নকশা নেওয়া হলো।  
  - **Instance Type** দিয়ে সাইজ ঠিক করা হলো।  
  - ঘরগুলোকে **round-robin** করে বিভিন্ন Public Subnet-এ ভাগ করা হলো।  
  - আবার Subnet-এর সঙ্গে Availability Zone-ও ঘুরিয়ে দেওয়া হলো।  

---

## ট্যাগ  

সব ঘরে নামের ফলক লাগানো হলো →  
`gl-dev-t2.micro-0`, `gl-dev-t2.micro-1`, `gl-dev-t2.small-0`  

---

## আউটপুট  

Terraform শেষে হাসিমুখে বললো:  
"এই নাও, তোমার রাজ্যের রিপোর্ট —"  

- ঘরের **ID তালিকা** 🏠  
- ঘরের **Public IP ঠিকানা** 🌍  
- ঘরের **Private IP ঠিকানা** 🔒  

---

# 📖 উপসংহার  

এভাবেই Terraform গ্রামে নতুন EC2 ঘর তৈরি হলো।  
প্রতিটা ঘর সঠিক জায়গায় বসলো, ট্যাগ পরলো, আর সবাই খুশি হলো।  

👉 মনে রাখবে:  
AMI হলো নকশা, Instance Type হলো ঘরের সাইজ, Subnet হলো এলাকা, আর Availability Zone হলো দারোয়ান।  

---






👉 এইভাবে রাজা Terraform তার পুরো EC2 সেনাদল গড়ে তুললেন — একেক যোদ্ধা আলাদা নাম, আলাদা মাঠ, আলাদা প্রান্তরে ছড়িয়ে পড়ল।



