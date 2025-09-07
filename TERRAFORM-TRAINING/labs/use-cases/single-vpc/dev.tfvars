

environment_name = "ipc-dev"
region           = "us-east-1"


vpcs = {
  "ipc-dev-01" = {
    cidr = "192.168.0.0/16"
    public_subnets = {
      "public-1a" = { cidr = "192.168.11.0/24", az = "us-east-1a" }
      "public-1b" = { cidr = "192.168.12.0/24", az = "us-east-1b" }
    }
    private_subnets = {
      "private-1a" = { cidr = "192.168.14.0/24", az = "us-east-1a" }
      "private-1b" = { cidr = "192.168.15.0/24", az = "us-east-1b" }
    }
  }
}

