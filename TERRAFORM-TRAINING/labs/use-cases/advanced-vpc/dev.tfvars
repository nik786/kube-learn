

environment_name = "gl-dev"
region           = "us-east-1"


vpcs = {
  "gl-dev-01" = {
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

  "gl-dev-02" = {
    cidr = "10.0.0.0/16"
    public_subnets = {
      "public-1a" = { cidr = "10.0.1.0/24", az = "us-east-1a" }
      "public-1b" = { cidr = "10.0.2.0/24", az = "us-east-1b" }
    }
    private_subnets = {
      "private-1a" = { cidr = "10.0.3.0/24", az = "us-east-1a" }
      "private-1b" = { cidr = "10.0.4.0/24", az = "us-east-1b" }
    }
  }

  "gl-dev-03" = {
    cidr = "172.16.0.0/16"
    public_subnets = {
      "public-1a" = { cidr = "172.16.1.0/24", az = "us-east-1a" }
      "public-1b" = { cidr = "172.16.2.0/24", az = "us-east-1b" }
    }
    private_subnets = {
      "private-1a" = { cidr = "172.16.3.0/24", az = "us-east-1a" }
      "private-1b" = { cidr = "172.16.4.0/24", az = "us-east-1b" }
    }
  }
}

