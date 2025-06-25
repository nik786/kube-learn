# Get default VPC
data "aws_vpc" "default" {
  default = true
}

module "web_sg" {
  source              = "./modules/sg"
  vpc_id              = data.aws_vpc.default.id
  name                = "eks-sg-09"
  description         = "Security Group for Web Servers"
  inbound_ports       = [80, 443]
  outbound_ports      = [443, 1433]
  ingress_cidr_blocks = ["0.0.0.0/0"]
  egress_cidr_blocks  = ["192.168.0.0/16"]
}

