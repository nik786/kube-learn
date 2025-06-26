

```

terraform {
  required_version = "~> 1.11.0"

  backend "s3" {
    bucket  = "state-0001"
    key     = "dev/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }


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
      version = "~> 4.0"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

```

data "aws_region" "selected" {}

```
