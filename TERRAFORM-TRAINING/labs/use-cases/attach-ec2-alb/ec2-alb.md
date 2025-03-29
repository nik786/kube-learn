
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
    "us-east-1a" = "subnet-0abcd1234efgh5678"
    "us-east-1b" = "subnet-0wxyz9876klmn5432"
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
