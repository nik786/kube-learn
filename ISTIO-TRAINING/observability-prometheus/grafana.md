
## Grafana Dashboards

 - Grafana is an open platform for analytics and monitoring
 - Connects to various data sources, including Prometheus
 - Visualise data using graphs, tables and heatmaps
 - Helps monitor Istio installation and application in the service mesh.


## Installing Grafana

- Ensure Prometheus is installed before deploying Grafana
- Deploy Grafana with pre-configured Istio dashboards
- kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/grafana.yaml


### Access Grafana Using
  istoctl dashboard grafana
  opens: http://localhost:3000

  
## Istio Control Plane Dashboard

- Monitor Istio control plane health and performance.
- Tracks CPU, memory and disk usage.
- Displays metrics for Pilot, Envoy and Webhooks


## Istio Mesh Dashboard

- Provides an overview of services running in the mesh.
- Tracks request volume, success rate and error trends.


## Istio Performance Dashboard

- Analyse Istios resource utilisation under load
- Helps optimise system performance
  
## Istio Service Dashboard
 
 - Provides detailed metrics for individual services.
 - Tracks request volume, response codes and traffic sources.
   
## Istio Wasm Extension Dashboard

 - Tracks WebAssembly(WASM) Extension performance
 - Monitors active WASM VMs and resource consumption

## Istio Workload Dashboard
 - Monitors per-workload metrics
 - Provides traffic insights and resource utilisation

## Istio Ztunnel Dashboard
  - Introduced in Ambient mode.
  - Tracks ztunnel performance and L4 traffic metrics





    


    




  
