

```

terraform {
  required_version = ">= 1.3.0"  # Specify the required version of Terraform

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"  # Specify the version or a version constraint for AWS provider
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0"  # Specify the version or a version constraint for Kubernetes provider
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

data "aws_region" "selected" {}

provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  exec {
    api_version = "client.authentication.k8s.io/v1"
    args        = ["eks", "get-token", "--cluster-name", module.eks.cluster_name, "--region", data.aws_region.selected.name]
    command     = "aws"
  }
}

```
