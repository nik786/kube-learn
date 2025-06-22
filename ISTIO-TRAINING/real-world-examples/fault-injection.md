
## Fault Injection

In this section, we will introduce a 5-second delay to the recommendations service. Envoy will inject a delay for 50% of the requests.

- [delay](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/real-world-examples/delay.md)

 ## Create the VirtualService

  kubectl apply -f delay.yaml


  We can open the INGRESS_HOST in the browser, then click on one of the products.
  The results from the recommendation service are shown at the bottom of the screen in a section titled "Other Products You Might Like

  If we refresh the page a couple of times, we will notice that the page loads right away or there's a delay loading the page.
  This delay is due to the 5-second delay we injected.


  We can open Grafana (istioctl dash grafana) and the Istio Service Dashboard. Make sure to select the recommendation service from the service list.
  Choose the source from the Reporter dropdown and look at the Client Request Duration that shows the delay.


  Similarly, we can inject an abort. In the example below, we inject an HTTP 500 for 50% of the requests sent to the product catalogue service


```

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
    fault:
      abort:
        percentage:
          value: 50
        httpStatus: 500



Update the VirtualService

kubectl apply -f productcatalogservice-abort.yaml

```

Note that the error message says that the cause of the failure is a fault filter abort. 
If we open Grafana (istioctl dash grafana), we will also notice the errors reported in the graphs.



We can delete the VirtualService by running kubectl delete virtualservice productcatalogservice


  
