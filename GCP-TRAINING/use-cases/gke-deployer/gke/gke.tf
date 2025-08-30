
# GKE Cluster
resource "google_container_cluster" "gke_cluster" {
  name               = "${var.environment}-gke-cluster"
  location           = var.region
  project            = var.project_id
  network            = module.vpc.network_name
  subnetwork         = module.vpc.public_subnetworks[0]  # Use the first public subnet for the cluster

  # Other GKE settings
  initial_node_count = 1
  min_master_version = "1.21" # Use a stable GKE version

  node_config {
    machine_type = "e2-medium"
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }

  # Define regional high-availability
  node_locations = var.zones  # Spread nodes across specified zones
}

# Output the GKE Cluster endpoint and CA certificate to configure `kubectl`
output "gke_endpoint" {
  value = google_container_cluster.gke_cluster.endpoint
}

output "gke_ca_certificate" {
  value = google_container_cluster.gke_cluster.master_auth.0.cluster_ca_certificate
}

