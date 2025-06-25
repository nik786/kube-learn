# modules/sg/main.tf

resource "aws_security_group" "this" {
  vpc_id      = var.vpc_id
  name        = var.name
  description = var.description

  dynamic "ingress" {
    for_each = var.inbound_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = var.ingress_cidr_blocks
    }
  }

  dynamic "egress" {
    for_each = var.outbound_ports
    content {
      from_port   = egress.value
      to_port     = egress.value
      protocol    = "tcp"
      cidr_blocks = var.egress_cidr_blocks
    }
  }
}

output "security_group_id" {
  value = aws_security_group.this.id
}
