

```
terraform {
  required_version = "~> 1.3.0" # Specify the required version of Terraform

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0" # Specify the version or a version constraint for AWS provider
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0" # Specify the version or a version constraint for Kubernetes provider
    }

    random = {
      source  = "hashicorp/random"
      version = "3.1.0"
    }



  }
}

provider "aws" {
  region = "us-east-1"
}

```



data "aws_region" "selected" {}
