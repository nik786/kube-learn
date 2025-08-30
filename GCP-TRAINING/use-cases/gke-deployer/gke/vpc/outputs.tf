output "network_name" {
  value = google_compute_network.my_network.name
}

output "public_subnetworks" {
  value = [for subnet in google_compute_subnetwork.my_public_subnetwork : subnet.name]
}

output "private_subnetworks" {
  value = [for subnet in google_compute_subnetwork.my_private_subnetwork : subnet.name]
}

