
## Kiali

- It is an observability and management console for Istio service meshes
- Provides visual topology, real-time monitoring, metrics, tracing and Istio configuration management
- Helps users efficiently manage, troubleshoot and optimise their service mesh.



## ServiceMesh Topology Visualisation
- Generates a dynamic service graph showing service-to-service communication
- Updates in real-time with traffic flow and dependencies
- Display request traces, latency and traffic health.


  
## Health Monitoring and Traffic Observability

- Real-time service health status with colour-coded alerts
- Monitors traffic flow, error rates, and request success rates
- Integrates with Prometheus to provide
    - Request rate
    - Success rate
    - Latency metrics


## Istio Configuration Management & Validation
 - Create, edit and validate Istio configurations from the UI.
 - Supports:
     - Traffic Routing
     - Circuit Breaking
     - Fault Injection
     - Request Timeouts
  
- Validates Istio objects, highlighting misconfigurations


## Integration with Jaeger and Grafana

- Jaegar: Distributed tracing to track request flows.
- Grafana: In-depth metrics visualisation
- Direct links to Jaeger and Grafana dashboards for better observability


  
## Installing Kiali

- Deploy Kiali using the official YAML manifest
- kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/kiali.yaml


## Expected output:
-  istioctl dashboard kiali


## Accessing Kiali

Open Kiali using: istoctl dashboard kiali

- Navigate to the graph view to visualise traffic and service dependencies.



## Advanced Istio Configuration with Kiali:

- UI-driven Istio configuration management:
    - Define traffic routing(e.g, weighted routing, canary deployments)
    - Configure fault injection for resiliency testing
    - Set up circuit breakers and retries
    - Apply mutual TLS policies and security settings

- Performs Istio configuration validation      





















   






