terraform {
  backend "s3" {
    bucket  = "state-0001"
    key     = "vpc/vpc.tfstate"
    region  = "us-east-1"
    encrypt = true

  }
}
