# Sentinel policy configuration file
policy "allow-only-web-ports" {
  source = "policies/allow-only-web-ports.sentinel"
  enforcement_level = "hard-mandatory"
}
