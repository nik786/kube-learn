



data "aws_availability_zones" "available" {}

variable "vpcs" {
  type = map(object({
    cidr            = string
    public_subnets  = map(object({
      cidr = string
      az   = string
    }))
    private_subnets = map(object({
      cidr = string
      az   = string
    }))
  }))
}




module "vpc" {
  source               = "./modules/vpc"
  for_each             = var.vpcs
  #source               = "git@github.com:nik786/kube-learn.git//TERRAFORM-TRAINING/labs/modules/vpc?ref=master"
  environment_name     = each.key
  enable_dns_hostnames = true
  enable_nat_gateway   = true
  cidr                 = each.value.cidr
  azs                  = data.aws_availability_zones.available.names
  public_subnets       = each.value.public_subnets
  private_subnets      = each.value.private_subnets

  public_subnet_tags = {
    "kubernetes.io/cluster/${each.key}" = "shared"
    "kubernetes.io/role/elb"            = "1"
  }

  private_subnet_tags = {
    "kubernetes.io/cluster/${each.key}" = "shared"
    "kubernetes.io/role/internal-elb"   = "1"
  }
}
