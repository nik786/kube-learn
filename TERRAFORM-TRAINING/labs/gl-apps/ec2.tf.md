
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
