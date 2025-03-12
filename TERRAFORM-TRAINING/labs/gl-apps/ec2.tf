

variable "instance_types" {
  description = "A map of instance types and their counts"
  type        = map(number)
  default     = {}
}


module "ec2" {
  source                = "../modules/ec2/for_v1"
  ami                   = "ami-0214abac5533f716b"
  instance_types        = var.instance_types
  subnet_id             = element(module.vpc.private_subnets, 0)
  
}
