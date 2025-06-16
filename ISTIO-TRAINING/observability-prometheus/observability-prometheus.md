

## Observability Overview

  - Istio supports sidecar and ambient modes observability
  - Sideca mode uses Envoy proxies to collect telemetry at the pod level
  - Ambient mode decouples traffic processing using ztunnel(L4) and waypoint(L7) proxies
  - Istio generates three types of telemetry
      - Metrics
      - Distributed traces
      - Access Logs
        

## Metrics

## Based on the four golden signals:
   - Latency: Time taken to service requests
   - Traffic: System demand measured in HTTP requests per second, concurrent sessions etc
   - Errors: Rate of failed requests
   - Saturation: Utilisation of constrained resources like thread pools

## Collected at different levels:

  - proxy-level metrics
  - service level metrics
  - control plane metrics
  


## Proxy-level(or ztunnel) Metrics

- Sidecar mode: Envoy proxies generate detailed traffic metrics
- Ambient mode: ztunnel and waypoint proxies collect similar telemetry
- Example metrics:

  

```

envoy_cluster_internal_upstream_rq{response_code_class="2xx",cluster_name="xds-grpc"} 7163
envoy_cluster_upstream_rq_completed{cluster_name="xds-grpc"} 7164
envoy_cluster_ssl_connection_error{cluster_name="xds-grpc"} 0
envoy_cluster_lb_subsets_removed{cluster_name="xds-grpc"} 0
envoy_cluster_internal_upstream_rq{response_code="503",cluster_name="xds-grpc"} 1

```

## Service-Level metrics

- Covers the four golden signals

- Enable monitoring of service-to-service communication

- Istio provides dashboards for visualising service behaviour

- Example metrics:



```
istio_requests_total{
    response_code="200",
    reporter="destination",
    source_workload="istio-ingressgateway",
    source_workload_namespace="istio-system",
    destination_workload="web-frontend",
    destination_service="web-frontend.default.svc.cluster.local",
    request_protocol="http",
    response_flags="-",
    connection_security_policy="mutual_tls",
} 9

```


## Control plane Metrics

- Helps monitor Istio's internal components
- Tracks rejected configurations, cluster states and errors
- 


## Prometheus Integration

- Open-source monitoring system used by Istio for metric storage
- Install Prometheus
  

```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/prometheus.yaml

```

## To open the Prometheus dashboard, run:


```
istioctl dashboard prometheus
http://localhost:9090

```


## Deploying a Sample App

- Deploy httbin and sleep in the default namespace
- Use them to simulate service-to-service traffic
- Observe metrics like istio_request_total in Prometheus


```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/sleep/sleep.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/httpbin/httpbin.yaml


kubectl get pods -n default

```

## Simulating more traffic and Observing Metrics

- Run multiple curl requests to create traffic
- Use Prometheus to inspect traffic metrics

```
kubectl exec deploy/sleep -c sleep -- curl -sS http://httpbin:8000/get


for i in {1..20}; do
  kubectl exec deploy/sleep -c sleep -- curl -sS http://httpbin:8000/get
  sleep 0.5
done

```

In Ambient mode, traffic is transparently handled by ztunnel





























