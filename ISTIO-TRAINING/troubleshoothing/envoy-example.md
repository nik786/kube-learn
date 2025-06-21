
## Envoy Example

- Demonstrates how envoy routes traffic from the web frontend to customer service customers.default.svc.cluster.local
- Based on resources from Lab3 in the traffic management module





## Step 1: Deploy Resources

  ```

  kubectl apply -f customers-50-50.yaml

  kubectl apply -f customers-dr.yaml

  kubectl apply -f customers-v1.yaml

  kubectl apply -f customers-v2.yaml

  kubectl apply -f customers-vs.yaml

  kubectl apply -f gateway.yaml

  kubectl apply -f web-frontend-vs.yaml

  kubectl apply -f web-frontend.yaml

```

## Step 2: Inspect Envoy Listeners


Use the istioctl proxy-config command to inspect the listeners configured in the web frontend’s Envoy proxy:

```

istioctl proxy-config listeners web-frontend-<pod-id>


```

Since the web frontend sends an HTTP request to port 80, traffic gets routed through the listener on 0.0.0.0:80. To filter the listener for that port:

```
istioctl proxy-config listeners web-frontend-<pod-id> --address 0.0.0.0 --port 80 -o json

```

## Look for the RDS (Route Discovery Service) configuration:



```

"rds": {
  "configSource": {
    "ads": {},
    "resourceApiVersion": "V3"
  },
  "routeConfigName": "80"
}

```

This means the listener fetches route configuration named 80 via RDS.



## Step 3: Inspect Envoy Routes


- Routes map virtual hosts (domains) to clusters. Check the route config for name 80:


```
 istioctl proxy-config routes web-frontend-<pod-id> --name 80 -o json

```


You’ll find a virtualHost for customers.default.svc.cluster.local and its associated domains and routes:


````

{
  "virtualHosts": [
    {
      "name": "customers.default.svc.cluster.local:80",
      "domains": ["customers.default.svc.cluster.local", "customers", ...],
      "routes": [
        {
          "match": { "prefix": "/" },
          "route": {
            "cluster": "outbound|80|v1|customers.default.svc.cluster.local"
          }
        }
      ]
    }
  ]
}

````



Since no advanced routing logic is used, the route with prefix / matches all traffic and forwards it to the v1 subset of the customer service




## Step 4: Inspect Clusters

Now that we know the cluster name, use the following command to get more details:

```

istioctl proxy-config clusters web-frontend-<pod-id> --fqdn customers.default.svc.cluster.local

```



```

SERVICE FQDN                            PORT     SUBSET     DIRECTION     TYPE     DESTINATION RULE
customers.default.svc.cluster.local     80       -          outbound      EDS      customers.default
customers.default.svc.cluster.local     80       v1         outbound      EDS      customers.default

```
The v1 subset exists because of the DestinationRule configuration.





## Step 5: Inspect Endpoints


To find the actual endpoint IP address and port that the request reaches:


```

istioctl proxy-config endpoints web-frontend-<pod-id> --cluster "outbound|80|v1|customers.default.svc.cluster.local"


Sample output:

ENDPOINT              STATUS      OUTLIER CHECK     CLUSTER
10.244.1.122:3000     HEALTHY     OK                outbound|80|v1|customers.default.svc.cluster.local



```

This tells us the Envoy proxy will forward traffic to 10.244.1.122:3000 as part of the v1 subset.




























