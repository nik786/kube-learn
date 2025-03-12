environment_name = "gl-dev"
region           = "ap-south-1"
vpc_cidr         = "192.168.0.0/16"


public_subnets = {
  "public-1a" = "192.168.11.0/24"
  "public-1b" = "192.168.12.0/24"
}


private_subnets  = {
         "private-1a" = "192.168.14.0/24"
         "private-1b" = "192.168.15.0/24"
}

instance_types = {
  "t2.small" = 1
  "t2.micro" = 1
}


