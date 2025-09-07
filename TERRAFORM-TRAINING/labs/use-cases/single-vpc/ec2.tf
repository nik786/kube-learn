#####################################
####### Security Group for Spot #####
#####################################

locals {
  inbound_ports  = [22, 80, 443]
  outbound_ports = [443, 1433]
}

# One SG per VPC
resource "aws_security_group" "sg" {
  for_each    = module.vpc
  vpc_id      = each.value.vpc_id
  name        = "${each.key}-sg"
  description = "Security Group for testing in ${each.key}"

  dynamic "ingress" {
    for_each = local.inbound_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  dynamic "egress" {
    for_each = local.outbound_ports
    content {
      from_port   = egress.value
      to_port     = egress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}

#####################################
####### Spot Instance in Public Subnet
#####################################

resource "aws_instance" "spot_instance" {
  for_each = module.vpc

  ami           = "ami-04124ccb971ba0bd6"   # Amazon Linux 2 ARM64 AMI
  instance_type = "t3.micro"

  instance_market_options {
    market_type = "spot"
  }

  # Launch in the first available public subnet of this VPC
  subnet_id                   = element(each.value.public_subnets, 0)
  associate_public_ip_address = true

  vpc_security_group_ids = [aws_security_group.sg[each.key].id]

  tags = {
    Name = "${each.key}-spot"
  }
}

#####################################
####### Outputs #####################
#####################################

output "spot_instance_public_ips" {
  value       = { for k, inst in aws_instance.spot_instance : k => inst.public_ip }
  description = "Public IPs of one spot instance per VPC"
}

