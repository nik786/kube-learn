variable "region" {}
variable "project_id" {}
variable "network" {}
variable "environment" {}
variable "zones" {
  type = list(string)
}

variable "public_cidrs" {
  type = list(string)
}
variable "private_cidrs" {
  type = list(string)
}
