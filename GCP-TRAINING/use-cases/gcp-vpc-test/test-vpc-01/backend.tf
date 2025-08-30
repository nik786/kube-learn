# Terraform configuration block
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"  # You could also try "~> 3.0" if there are compatibility issues
    }
  }
  
  backend "gcs" {
    bucket  = "tf-states-14"  # Replace with your GCS bucket name
    prefix  = "tfstate"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region  # Use the Mumbai region for resources
}
