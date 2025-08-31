# ===============================
# GKE Cluster (Regional, HA, Cost-Effective)
# ===============================
resource "google_container_cluster" "gke_cluster" {
  name     = "${var.environment}-gke-cluster"
  location = var.region
  project  = var.project_id

  network    = module.vpc.network_name
  subnetwork = module.vpc.public_subnetworks[0] # Use first public subnet for control plane

  # Disable default node pool (best practice: manage custom pools separately)
  remove_default_node_pool = true
  initial_node_count       = 1

  # Auto-updated GKE version via release channel
  release_channel {
    channel = "REGULAR"
  }

  # Regional cluster with HA (nodes spread across multiple zones)
  node_locations = var.zones

  # Allow Terraform destroy without manual intervention
  deletion_protection = false

  # Security: enable Shielded nodes
  enable_shielded_nodes = true

}

# ===============================
# Node Pool (Cost-Optimized)
# ===============================
resource "google_container_node_pool" "gke_nodes" {
  name     = "${var.environment}-node-pool"
  cluster  = google_container_cluster.gke_cluster.name
  location = var.region
  project  = var.project_id

  # Node autoscaling
  autoscaling {
    min_node_count = 1
    max_node_count = 2
  }

  node_config {
    # Cost-effective machine type (good balance for dev/test)
    machine_type = "e2-small" # 2 vCPU, 2 GB RAM

    # Use Spot (Preemptible) instances — ~70% cheaper
    preemptible = true

    # Cheaper disk option
    disk_type    = "pd-standard"
    disk_size_gb = 30

    # Enable shielded nodes
    shielded_instance_config {
      enable_secure_boot          = true
      enable_integrity_monitoring = true
    }

    # Grant only required scopes (least privilege principle)
    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]

    # Labels & tags for billing & policies
    labels = {
      env     = var.environment
      spot    = "true"
      purpose = "gke-workload"
    }

    tags = ["gke-node", "${var.environment}-cluster"]
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}

# ===============================
# Outputs
# ===============================
output "gke_endpoint" {
  value = google_container_cluster.gke_cluster.endpoint
}

output "gke_ca_certificate" {
  value = google_container_cluster.gke_cluster.master_auth[0].cluster_ca_certificate
}
