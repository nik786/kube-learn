variable "region" {
  default = "us-east1"
}

variable "project_id" {
  default = "tensile-nebula-400413"
}

variable "zones" {
  type    = list(string)
  default = ["us-east1-b", "us-east1-c"]
}

variable "network" {
  default = "my-network"
}

variable "public_cidrs" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_cidrs" {
  type    = list(string)
  default = ["10.0.3.0/24", "10.0.4.0/24"]
}

terraform {
  backend "gcs" {
    bucket = "tf-states-09"
    prefix = "tfstate"
  }
}

# VPC Network
resource "google_compute_network" "my_network" {
  name                    = var.network
  project                 = var.project_id
  description             = "Main global VPC"
  auto_create_subnetworks = false
}

# Create Public Subnetworks
resource "google_compute_subnetwork" "my_public_subnetwork" {
  count         = length(var.public_cidrs)
  name          = "${var.network}-public-${count.index + 1}"
  region        = var.region
  project       = var.project_id
  network       = google_compute_network.my_network.self_link
  ip_cidr_range = element(var.public_cidrs, count.index)
}

# Create Private Subnetworks
resource "google_compute_subnetwork" "my_private_subnetwork" {
  count                     = length(var.private_cidrs)
  name                      = "${var.network}-private-${count.index + 1}"
  region                    = var.region
  project                   = var.project_id
  network                   = google_compute_network.my_network.self_link
  ip_cidr_range             = element(var.private_cidrs, count.index)
  private_ip_google_access  = true
}

# Cloud Router for NAT
resource "google_compute_router" "nat_router" {
  name    = "${var.network}-nat-router"
  region  = var.region
  project = var.project_id
  network = google_compute_network.my_network.self_link

  bgp {
    asn = 64512
  }
}

# NAT Gateway
resource "google_compute_router_nat" "nat_gateway" {
  name                          = "${var.network}-nat-gateway"
  router                        = google_compute_router.nat_router.name
  region                        = var.region
  project                       = var.project_id
  nat_ip_allocate_option        = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
}

# Global IP Address for Bastion
resource "google_compute_global_address" "internet_gateway_ip" {
  name       = "${var.network}-ig-ip"
  project    = var.project_id
  ip_version = "IPV4"
}

# Firewall Rule for HTTP/HTTPS Access
resource "google_compute_firewall" "allow_http" {
  name    = "allow-http"
  network = google_compute_network.my_network.name
  project = var.project_id

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
}


# Public Route
resource "google_compute_route" "public_route" {
  count             = length(var.public_cidrs)
  name              = "${var.network}-public-route-${count.index + 1}"
  network           = google_compute_network.my_network.name
  project           = var.project_id
  dest_range        = "0.0.0.0/0"
  next_hop_gateway  = "default-internet-gateway"
  priority          = 1000
}

# Regional IP Address for Internet Gateway
resource "google_compute_address" "internet_gateway_ip" {
  name    = "${var.network}-ig-ip"
  region  = var.region       # Specify the region to make it regional
  project = var.project_id
}

# Bastion Instance
resource "google_compute_instance" "bastion_instance" {
  name         = "bastion-instance"
  machine_type = "n1-standard-1"
  zone         = element(var.zones, 0)
  project      = var.project_id

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network             = google_compute_network.my_network.name
    subnetwork          = google_compute_subnetwork.my_public_subnetwork[0].name
    subnetwork_project  = var.project_id
    access_config {
      nat_ip = google_compute_address.internet_gateway_ip.address  # Reference the regional IP
    }
  }

  tags = ["bastion-instance"]
}
