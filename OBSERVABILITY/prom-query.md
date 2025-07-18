

```
sum(container_cpu_usage_seconds_total) by (pod)

sum(container_memory_usage_bytes) by (pod)

node_memory_MemFree_bytes

node_memory_MemTotal_bytes

kube_job_status_succeeded | label_values(job_name)

node_network_transmit_queue_length

container_network_latency_seconds

container_cpu_cfs_throttled_seconds_total

docker run --rm --network gt_monitoring_bridge ghcr.io/equinix-labs/otel-cli:latest \
  --endpoint http://172.32.23.6:4318 \
  span --name "test-span" \
       --force-trace-id "$(uuidgen | tr -d '-' | cut -c1-32)" \
       --force-span-id "$(uuidgen | tr -d '-' | cut -c1-16)" \
       --tp-print


```


If you're using the Prometheus Blackbox Exporter to monitor website latency, 

you can query the HTTP request duration for the website.


```
probe_http_duration_seconds{job="blackbox", instance="your-website.com"}

avg(probe_http_duration_seconds{job="blackbox", instance="your-website.com"})

histogram_quantile(0.95, rate(probe_http_duration_seconds_bucket{job="blackbox",
instance="your-website.com"}[5m]))

max(probe_http_duration_seconds{job="blackbox", instance="your-website.com"})

http_request_duration_seconds{service="frontend", instance="your-website.com"}



```

- terraform plan -var cloud=aws -var no_caps=training -var ip_address=1.1.1.1  -var character_limit=rpt

/home/nik/Desktop/ansible/gp/grafana-prome


## Grafana-Dashboard Codes

- 315
- 11398
- 551
- 1860
- 12740
- 19792
- 6417
- 3119






- [monitor-kubernetes](https://github.com/nik786/monitor/tree/master/monitor-kubernetes)
- [grafana-prometheus](https://github.com/monitor-ops/gp/blob/master/grafana-prome/docker-compose.yml)
