

```
sum(container_cpu_usage_seconds_total) by (pod)

sum(container_memory_usage_bytes) by (pod)

node_memory_MemFree_bytes

node_memory_MemTotal_bytes

kube_job_status_succeeded | label_values(job_name)

```

If you're using the Prometheus Blackbox Exporter to monitor website latency, 
you can query the HTTP request duration for the website.

```
probe_http_duration_seconds{job="blackbox", instance="your-website.com"}

avg(probe_http_duration_seconds{job="blackbox", instance="your-website.com"})

histogram_quantile(0.95, rate(probe_http_duration_seconds_bucket{job="blackbox", instance="your-website.com"}[5m]))

max(probe_http_duration_seconds{job="blackbox", instance="your-website.com"})

http_request_duration_seconds{service="frontend", instance="your-website.com"}



```
