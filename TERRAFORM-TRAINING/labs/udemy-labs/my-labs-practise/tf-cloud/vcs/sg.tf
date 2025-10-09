
locals {
    inbound_ports = [80,443,22]
    outbound_ports = [443,1443]
}

resource "aws_security_group" "sg" {
    name = "web-sg"
    vpc_id = module.vpc["ipc-dev-01"].vpc_id
    dynamic "ingress" {
       for_each = local.inbound_ports 
       content {
          to_port = ingress.value 
          from_port = ingress.value 
          protocol =  "tcp"
          cidr_blocks = [ "0.0.0.0/0" ]
          }
        }
   
   dynamic "egress" {
    for_each = local.outbound_ports
    content {
       to_port  = egress.value 
       from_port = egress.value
       protocol = "tcp"
       cidr_blocks = [ "192.168.0.0/16" ] 

   }

}
}
