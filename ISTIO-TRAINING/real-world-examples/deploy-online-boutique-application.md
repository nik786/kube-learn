
## Deploy Online Boutique Application

With cluster and Istio ready, we can clone the Online Boutique Application repository

1. Clone the repository

git clone https://github.com/GoogleCloudPlatform/microservices-demo.git

2. Go to the microservices-demo folder:

cd microservices-demo

3. Create the Kubernetes resources:

kubectl apply -f release/kubernetes-manifests.yaml

4. Check that all Pods are running:

```

kubectl get pods
NAME                                     READY   STATUS    RESTARTS   AGE
adservice-997b6fc95-rnszr                2/2     Running   0          11m
cartservice-59d7459964-f89js             2/2     Running   0          12m
checkoutservice-855ff8d99-fc9vr          2/2     Running   0          12m
currencyservice-b7dcd96f5-x26r2          2/2     Running   0          11m
emailservice-69cfd9755c-8sbnc            2/2     Running   0          12m
frontend-c48bb8c56-hglmw                 2/2     Running   0          12m
loadgenerator-d7c89d8f7-chfj5            2/2     Running   0          11m
paymentservice-7c56f54965-8wpd5          2/2     Running   0          12m
productcatalogservice-69878b7d5c-ldq86   2/2     Running   0          12m
recommendationservice-7d59447ccc-tzhlw   2/2     Running   0          12m
redis-cart-558f8d8d44-zdq98              2/2     Running   0          12m
shippingservice-fb69f4985-xmlxl          2/2     Running   0          11m

```

5. Create the Istio resources

```
   kubectl apply -f ./istio-manifests
```

6. Visit the online boutique UI

  ```
   INGRESS_HOST="$(kubectl -n istio-system get service istio-ingressgateway \
   -o jsonpath='{.status.loadBalancer.ingress[0].ip}')"
echo "$INGRESS_HOST"

```

7. Delete the frontend-external service

```
 
The last thing we need to do is to delete the frontend-external service. The frontend-external service is a LoadBalancer
service that exposes the frontend. Since we are using Istio's ingress gateway, we don't need this LoadBalancer service anymore.

To delete the service, run:

```
kubectl delete svc frontend-external

```















