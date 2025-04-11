
```

data "aws_availability_zones" "available" {}

module "vpc" {
  source               = "git@github.com:nik786/kube-learn.git//TERRAFORM-TRAINING/labs/modules/vpc?ref=master"
  environment_name     = var.environment_name
  enable_dns_hostnames = true
  enable_nat_gateway   = true
  vpc_cidr             = var.vpc_cidr
  azs                  = data.aws_availability_zones.available.names
  public_subnets       = var.public_subnets
  private_subnets      = var.private_subnets

  public_subnet_tags = {
    "kubernetes.io/cluster/${var.environment_name}" = "shared"
    "kubernetes.io/role/elb"                         = "1"
  }

  private_subnet_tags = {
    "kubernetes.io/cluster/${var.environment_name}" = "shared"
    "kubernetes.io/role/internal-elb"               = "1"
  }
}

```
