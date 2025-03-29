
```

# Data blocks to reference existing VPCs
data "aws_vpc" "vpc_a" {
  filter {
    name   = "cidr"
    values = ["10.0.1.0/16"]
  }
}

data "aws_vpc" "vpc_b" {
  filter {
    name   = "cidr"
    values = ["10.0.2.0/16"]
  }
}

# Define private subnets for each VPC
variable "vpc_a_private_subnets" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "vpc_b_private_subnets" {
  type    = list(string)
  default = ["10.0.4.0/24", "10.0.5.0/24"]
}

# Availability Zones
variable "azs" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

# Select VPC Type
variable "vpc_type" {
  type    = string
  default = "vpc_a"
}

# Conditional selection of private subnets based on VPC type
locals {
  selected_vpc_subnets = var.vpc_type == "vpc_a" ? var.vpc_a_private_subnets : var.vpc_b_private_subnets
  selected_vpc_id      = var.vpc_type == "vpc_a" ? data.aws_vpc.vpc_a.id : data.aws_vpc.vpc_b.id
}

# Create AWS Subnets based on the selected VPC type
resource "aws_subnet" "private_subnets" {
  count             = length(local.selected_vpc_subnets)
  vpc_id            = local.selected_vpc_id
  cidr_block        = local.selected_vpc_subnets[count.index]
  availability_zone = var.azs[count.index % length(var.azs)]
}

#terraform apply -var="vpc_type=vpc_a" -auto-approve "devtfplan"
#terraform plan -var-file="dev.tfvars" -out="devtfplan"

```
