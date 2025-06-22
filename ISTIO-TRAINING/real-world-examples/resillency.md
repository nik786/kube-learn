

## Resiliency

We will add an environment variable called EXTRA_LATENCY to the product catalog service deployment to demonstrate resiliency features. 
This variable injects extra sleep on every call to the service.

Edit the product catalog service deployment

kubectl edit deploy productcatalogservice

Scroll to the section with the environment variables and add the EXTRA_LATENCY environment variable


```
spec:
  containers:
  - env:
    - name: EXTRA_LATENCY
      value: 6s


```



If we refresh the page, we will notice the page takes 6 seconds to load due to the latency we injected

```

```
cat productcatalogservice-timeout.yaml

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: productcatalogservice
spec:
  hosts:
  - productcatalogservice
  http:
  - route:
    - destination:
        host: productcatalogservice
    timeout: 2s


```

kubectl apply -f productcatalogservice-timeout.yaml


If we refresh the page, we will notice an error message show up:

```
rpc error: code = Unavailable desc = upstream request timeout
could not retrieve products

```

```
cat productcatalogservice-retry.yaml

apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: productcatalogservice
spec:
  hosts:
  - productcatalogservice
  http:
  - route:
    - destination:
        host: productcatalogservice
    retries:
      attempts: 3
      perTryTimeout: 1s

kubectl apply -f productcatalogservice-retry.yaml

```


Since we left the extra latency in the product catalogue service deployment, we'll still see errors. 
Let's open Zipkin and look for the traces to see the retry policy in action



Use istioctl dash zipkin to open the Zipkin dashboard


Click the + button, select serviceName and frontend.default.
To only get the responses that took at least one second (our perTryTimeout), 
select minDuration and enter 1s in the text box. Click the search button to show all traces.


Click the Filter button and select productCatalogService.default from the dropdown
You should see traces that took at 1 second. The traces correspond to the perTryTimeout we defined earlier.
















