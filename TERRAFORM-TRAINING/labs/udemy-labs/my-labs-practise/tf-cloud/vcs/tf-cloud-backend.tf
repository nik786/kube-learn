terraform {
  required_version = "~> 1.11.0"

  backend "remote" {
    hostname = "app.terraform.io" 
    organization = "gl-org"

    workspaces {
      name = "gl-dev"
    }
  }
}
