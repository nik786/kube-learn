
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

# 🏰 গল্প – EC2 মডিউলের কাহিনি

একদিন এক রাজ্য ছিলো — নাম **Cloudland**।  
এই রাজ্যে নতুন নতুন **যোদ্ধা (EC2 instance)** তৈরি করার দায়িত্ব ছিলো **Terraform রাজার**।

---

## 📜 রাজার মানচিত্র (Variables)

- **ami** → এটা হলো যোদ্ধাদের **বর্ম** (AMI image)।  
- **instance_types** → কোন ধরনের যোদ্ধা কতজন তৈরি হবে তার হিসেব।  
  যেমন: `"t2.micro" = 2`, `"t2.small" = 1`  
- **environment_name** → রাজ্যের নাম, যেটা প্রতিটি যোদ্ধার সাথে ট্যাগ হবে।  
- **vpc_id** → রাজ্যের সীমারেখা (VPC), যেখানে এরা ঘুরবে।  



---


## 🌉 রাজ্যের সেতু ও রাস্তা (Data Sources)

যোদ্ধাদের মাঠে নামাতে আগে রাজাকে জানতে হয়:

- **availability_zones** → কোন কোন প্রান্তরে (AZs) রাস্তা খোলা আছে।
  
- **subnets** → কোন কোন মাঠ (subnet) জনসাধারণের জন্য উন্মুক্ত

- (`tag:Type = public`)।  




---

## ⚔️ যোদ্ধা তৈরি (aws_instance)

রাজা একটা যাদুর তালিকা বানালেন:

```hcl
for_each = {
  "t2.micro-0" => { type = "t2.micro", idx = 0 }
  "t2.micro-1" => { type = "t2.micro", idx = 1 }
  "t2.small-0" => { type = "t2.small", idx = 0 }
}

```


মানে, প্রত্যেক যোদ্ধার একটা আলাদা নাম (key) হলো, যাতে কাউকে গুলিয়ে না ফেলে।

প্রতিটি যোদ্ধা তার নিজের বর্ম (AMI) পরে।

তার নিজের ধরন (Instance Type) নেয়।

রাজা তাদেরকে পাবলিক মাঠে (Subnet) পাঠান → রাউন্ড রবিন পদ্ধতিতে ঘুরিয়ে।

আবার তাদেরকে বিভিন্ন প্রান্তরে (AZ) ছড়িয়ে দেন → যাতে এক জায়গায় দুর্ঘটনা হলে বাকিরা বেঁচে যায়।

শেষে রাজা প্রতিটি যোদ্ধার কপালে লিখে দেন:


```
Name        = "gl-dev-t2.micro-0"
Environment = "gl-dev"

```




📜 দরবারে প্রতিবেদন (Outputs)

রাজা তার সভাসদদের সামনে একটা প্রতিবেদন দিলেন:

instance_ids → কোন যোদ্ধার ID কী।

public_ips → কোন যোদ্ধা রাজ্যের বাইরে যোগাযোগের জন্য কোন ডাকঘর নম্বর (Public IP) পেল।

private_ips → রাজ্যের ভেতরে তাদের আস্তানার ঠিকানা (Private IP)।

সবকিছু নাম ধরে সুন্দর করে সাজানো হলো:



```
"t2.micro-0" = "i-0abc123"
"t2.micro-1" = "i-0def456"
"t2.small-0" = "i-012345"

```




🏰 মূল রাজদরবারে (Root Module)

রাজা যখন দরবার (Root) বসালেন, তখন ঘোষণা করলেন:

রাজ্যের নাম হবে → gl-dev

রাজ্য থাকবে → ap-south-1 অঞ্চলে

রাজ্যের সীমা হবে → 192.168.0.0/16

যোদ্ধাদের হিসেব:

১ জন t2.small

২ জন t2.micro



তারপর তিনি EC2 সেনাদল তৈরি করতে আদেশ দিলেন:



```
module "ec2" {
  source           = "../modules/ec2"
  ami              = "ami-0214abac5533f716b"
  instance_types   = var.instance_types
  environment_name = var.environment_name
  vpc_id           = module.vpc.vpc_id
}

```


📖 উপসংহার


👉 এইভাবে রাজা Terraform তার পুরো EC2 সেনাদল গড়ে তুললেন — একেক যোদ্ধা আলাদা নাম, আলাদা মাঠ, আলাদা প্রান্তরে ছড়িয়ে পড়ল।



