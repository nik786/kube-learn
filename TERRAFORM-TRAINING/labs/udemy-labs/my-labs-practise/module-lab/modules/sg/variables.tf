# modules/sg/variables.tf

variable "vpc_id" {
  type        = string
  description = "VPC ID where the SG will be created"
}

variable "name" {
  type        = string
  description = "Name of the security group"
}

variable "description" {
  type        = string
  description = "Description for the security group"
  default     = "Managed by Terraform"
}

variable "inbound_ports" {
  type        = list(number)
  description = "List of inbound TCP ports"
  default     = [80, 443]
}

variable "outbound_ports" {
  type        = list(number)
  description = "List of outbound TCP ports"
  default     = [443, 1433]
}

variable "ingress_cidr_blocks" {
  type        = list(string)
  description = "CIDR blocks allowed for ingress"
  default     = ["0.0.0.0/0"]
}

variable "egress_cidr_blocks" {
  type        = list(string)
  description = "CIDR blocks allowed for egress"
  default     = ["192.168.0.0/16"]
}

