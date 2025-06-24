terraform {
  required_version = "~> 1.11.0"

  backend "remote" {
    hostname = "app.terraform.io" 
    organization = "tf-cloud-labs"

    workspaces {
      name = "tf-cloud-ws"
    }
  }





 required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0"
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

data "aws_region" "selected" {}

