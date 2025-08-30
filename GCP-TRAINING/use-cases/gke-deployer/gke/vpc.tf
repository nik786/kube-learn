module "vpc" {
  source       = "./vpc"  # Path to the VPC module directory
  region       = var.region
  project_id   = var.project_id
  network      = var.network
  public_cidrs = var.public_cidrs
  private_cidrs = var.private_cidrs
}
