
```

# Step 6: Create EC2 Instances
resource "aws_instance" "web" {
  count         = 2  # Create 2 EC2 instances
  ami           = "ami-0c55b159cbfafe1f0"  # Replace with a valid AMI ID for your region
  instance_type = "t2.micro"  # Choose the instance type

  subnet_id              = element(data.aws_subnets.public_subnets.ids, count.index)  # Place instances in public subnets
  security_groups        = [aws_security_group.alb_sg.name]  # Attach the security group created above
  associate_public_ip_address = true  # Assign a public IP address

  tags = {
    Name = "WebInstance${count.index + 1}"  # Tag instances uniquely
  }
}


# Define the private subnets and their corresponding availability zones
variable "private_subnets" {
  type = map(string)
  default = {
    "us-east-1a" = "sub-14264"
    "us-east-1b" = "sub-273727"
  }
}

# EC2 instances configuration
resource "aws_instance" "web" {
  for_each = var.private_subnets  # Loop over the private subnets map

  ami                    = "ami-0c55b159cbfafe1f0"  # Replace with a valid AMI ID for your region
  instance_type          = "t2.micro"  # Instance type
  subnet_id              = each.value  # Subnet ID for the instance
  vpc_security_group_ids = [aws_security_group.alb_sg.id]  # Attach the security group
  associate_public_ip_address = false  # Do not assign public IPs (private subnet)

  tags = {
    Name = "WebInstance-${each.key}"  # Tag the instance uniquely based on AZ
  }
}


# Step 7: Attach EC2 Instances to the Target Group using for_each
resource "aws_lb_target_group_attachment" "web" {
  for_each          = toset(aws_instance.web[*].id)  # Iterate over all EC2 instance IDs
  target_group_arn  = aws_lb_target_group.app_tg.arn
  target_id         = each.value
  port              = 80
}


# Attach the Load Balancer to the Auto Scaling Group
resource "aws_autoscaling_attachment" "example" {
  autoscaling_group_name = aws_autoscaling_group.example.name
  lb_target_group_arn   = aws_lb_target_group.example.arn
}

```


```

variable "azs" {
  type = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

data "aws_subnet" "private" {
  for_each = toset(var.azs)

  filter {
    name   = "availability-zone"
    values = [each.key]
  }

  filter {
    name   = "tag:Type"
    values = ["private"]
  }

  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }
}

resource "aws_instance" "web" {
  for_each = data.aws_subnet.private

  ami                         = "ami-0c55b159cbfafe1f0"
  instance_type               = "t2.micro"
  subnet_id                   = each.value.id
  vpc_security_group_ids      = [aws_security_group.alb_sg.id]
  associate_public_ip_address = false

  tags = {
    Name = "WebInstance-${each.key}"
  }
}



resource "aws_lb_target_group_attachment" "web" {
  for_each          = toset(aws_instance.web[*].id)  # Iterate over all EC2 instance IDs
  target_group_arn  = aws_lb_target_group.app_tg.arn
  target_id         = each.value
  port              = 80
}


```



# Terraform গল্প (VPC – EC2 – Load Balancer)

একটা বড়ো **VPC রাজ্য** আছে। সেই রাজ্যের ভেতরে একাধিক **Availability Zone (AZ)** গ্রাম আছে – যেমন `us-east-1a`, `us-east-1b`।

রাজা ঘোষণা করলেন –  
👉 “আমাদের **private subnet** খুঁজে বের করো প্রতিটি গ্রাম (AZ) অনুযায়ী। শর্ত হলো:

- সেটা অবশ্যই আমাদের এই রাজ্যের (**VPC**) ভেতরে হতে হবে,  
- আর তার ট্যাগে লেখা থাকতে হবে `Type = private`।”  

---

## Subnet → EC2 সৈনিকরা

প্রতিটি গ্রামে যখন subnet পাওয়া গেল, তখন রাজার নির্দেশে প্রতিটা subnet-এর ভেতরে একটা করে **ওয়েব সৈনিক (EC2 instance)** বসানো হলো।  

- প্রত্যেক সৈনিক একই **AMI পোশাক** (`ami-125165261`) পরল,  
- তারা সবাই **t2.micro** রূপে দাঁড়িয়ে থাকল,  
- আর সুরক্ষার জন্য তারা রাজার দেওয়া **Security Group (alb_sg)** নিয়ে নিল,  
- সৈনিকরা বাইরে থেকে দেখা যায় না (**public IP নেই**), শুধু ভেতরের কাজে ব্যস্ত।  
- প্রতিটি সৈনিককে একটা করে নাম দেওয়া হলো — `"web-us-east-1a"`, `"web-us-east-1b"` এইভাবে।  

---

## দুর্গ (Load Balancer) এবং Target Group

তারপর রাজার দুর্গের সামনে একটা বড় **Target Group (app_tg)** বানানো হলো।  

রাজা বললেন –  
👉 “আমাদের সব ওয়েব সৈনিকদের এই Target Group-এর সঙ্গে যুক্ত করে দাও, যাতে তারা সবাই মিলে **Load Balancer**-এ আসা অতিথিদের জন্য খাবার (**HTTP request**) পরিবেশন করতে পারে।”  

তাই প্রতিটি সৈনিককে একেকটা **target_id** দিয়ে Target Group-এর সঙ্গে জুড়ে দেওয়া হলো।  
সবাই মিলেমিশে এখন দুর্গের অতিথিদের খাওয়াচ্ছে, আর রাজ্যের ভেতরে শান্তি-শৃঙ্খলা বজায় আছে।  

---

## সহজ মনে রাখার মানচিত্র

- **রাজ্য** = VPC  
- **গ্রাম** = AZ (availability zone)  
- **subnet** = গ্রামের ভেতরের জমি  
- **সৈনিক** = EC2 instance  
- **দুর্গ** = Load Balancer  
- **Target Group** = যেখানে সৈনিকরা যুক্ত হয়ে অতিথিদের সেবা দেয়  





