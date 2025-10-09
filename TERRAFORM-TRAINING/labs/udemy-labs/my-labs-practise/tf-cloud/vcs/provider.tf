terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0"
    }

    http = {
      source  = "hashicorp/http"
      version = ">= 2.1.0"
    }

    random = {
      source  = "hashicorp/random"
      version = ">= 3.1.0"
    }

    local = {
      source  = "hashicorp/local"
      version = ">= 2.1.0"
    }

    tls = {
      source  = "hashicorp/tls"
      version = ">= 3.1.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  
}

data "aws_region" "selected" {}


