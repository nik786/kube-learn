locals {
  inbound_ports  = [80, 443]
  outbound_ports = [443, 1433]
}


# Get default VPC
data "aws_vpc" "default" {
  default = true
}


# Security Groups
resource "aws_security_group" "sg-webserver" {
  #vpc_id              = module.vpc.vpc_id
  vpc_id      = data.aws_vpc.default.id
  name        = "eks-sg-08"
  description = "Security Group for Web Servers"

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
      cidr_blocks = ["192.168.0.0/16"]
    }
  }
}



