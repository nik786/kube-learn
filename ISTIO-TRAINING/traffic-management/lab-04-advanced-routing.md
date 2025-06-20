

## Advanced Traffic Routing

In this lab, we will learn how to use request properties to route the traffic between multiple service versions


- [gateway](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/traffic-management/gateway-01.md)

  kubectl apply -f gateway.yml 

Next, we will deploy the Web Frontend, Customers v1, Customers v2, and the corresponding VirtualServices and DestinationRule. 
Once we deploy everything, all traffic gets routed to the Customers v1.




- [web-frontend](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/traffic-management/web-frontend-01.md)

   kubectl apply -f web-frontend.yaml


- [customers](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/traffic-management/customers-01.md)


kubectl apply -f customers.yaml.


To ensure everything is deployed and works correctly, open the GATEWAY_URL and ensure we are getting the responses back from the Customers v1. 
we should only see the NAME column in the response.


We will update the customers VirtualService and update how the traffic is being routed between two versions of the customers service


- [customer-vs](https://github.com/nik786/kube-learn/blob/master/ISTIO-TRAINING/traffic-management/customers-vs.md)


Let's look at a YAML that routes the traffic to Customers v2, if the request contains a header user: debug. 
If the header is not set, we are routed to the Customers v1

If we open the GATEWAY_URL we should still get back the response from the Customers v1. 
If we add the header user: debug to the request we will notice that the customers' response is from the Customers v2

```

You can set the environment variable with the GATEWAY_URL address like this: 
export GATEWAY_URL=$(kubectl get svc -n istio-system istio-ingressgateway -ojsonpath='{.status.loadBalancer.ingress[0].ip}')

```


We can use the ModHeader extension to modify the headers from the browser. 
Alternatively, we can use cURL and add the header to the request like this:


```
curl -H "user: debug" http://$
GATEWAY_URL/
...
<th class="px-4 py-2">CITY</th>
<th class="px-4 py-2">NAME</th>
...
```

If we look through the response, you will notice the two columns - CITY and NAME.


## Cleanup

```

kubectl delete deploy web-frontend customers-{v1,v2}
kubectl delete svc customers web-frontend
kubectl delete vs customers web-frontend
kubectl delete dr customers
kubectl delete gateway gateway


```






















