

```
minikube status

kubectl version

istioctl version

```

## Install Istio in Ambient Mode


Istio provides multiple configuration profiles. To install Ambient Mode, use the ambient profile:

```

istioctl install --set profile=ambient --skip-confirmation


Verify installation:

kubectl get pods -n istio-system


Expected output:

NAME                            READY   STATUS    RESTARTS   AGE
istiod-6fb9db6b6-2wvqm         1/1     Running   0          51s
ztunnel-abcde-xyz123           1/1     Running   0          31s


```

## Enable Ambient Mode for Workloads

```

Label the namespace to enable Ambient Mode traffic interception:

kubectl label namespace default istio.io/dataplane-mode=ambient

Check the label:

kubectl get namespace -L istio.io/dataplane-mode

Deploy the Bookinfo sample application:

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/bookinfo/platform/kube/bookinfo.yaml

kubectl get pods


NAME                             READY   STATUS    RESTARTS   AGE
details-v1-54ffdd5947-lkfq5      1/1     Running   0          10m
productpage-v1-d49bb79b4-gr4wx   1/1     Running   0          10m
ratings-v1-856f65bcff-bs2wr      1/1     Running   0          10m
reviews-v1-848b8749df-7v22k      1/1     Running   0          10m
reviews-v2-5fdf9886c7-nv9kb      1/1     Running   0          10m
reviews-v3-bb6b8ddc7-5k4fw       1/1     Running   0          10m

```

## Deploy a Waypoint Proxy (Optional)


## Install Kubernetes Gateway API CRDs:

```

kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.1/standard-install.yaml; }

```

## For Layer 7 traffic management, deploy a Waypoint Proxy:

```

istioctl waypoint apply -n default --enroll-namespace


```

## Configure Ingress Access


## Deploy the gateway for the bookinfo application:



```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/bookinfo/gateway-api/bookinfo-gateway.yaml

Retrieve the external IP for Minikube:

minikube tunnel

```

Access the Bookinfo sample application in a browser at http://localhost/productpage.

By refreshing the page multiple times, you will notice different versions of the reviews service, indicating traffic routing.


## Uninstalling Istio

```

istioctl uninstall --purge
kubectl delete namespace istio-system


```




































