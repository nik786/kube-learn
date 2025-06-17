
```

kubectl version

minikube version

minkube start --driver=docker --cpus=1 --memory=4000 --disk-size=20g

minikube addons enable ingress

kubectl version --short

```

## Download Istio

- To install Istio 1.24.3, download the latest release:

  curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.24.3 sh -

## Navigate to the extracted folder:

cd istio-1.24.3<br>
export PATH=$PWD/bin:$PATH

## Verify istioctl is available:

  istioctl version

## Install Istio

istioctl install --set profile=demo --skip-confirmation


## Verify installation:

kubectl get pods -n istio-system


## Expected output:

NAME                                    READY   STATUS    RESTARTS   AGE
istio-egressgateway-5868fcbc58-5t9qj    1/1     Running   0          31s
istio-ingressgateway-5896f57fbb-tcb9v   1/1     Running   0          31s
istiod-6fb9db6b6-2wvqm                  1/1     Running   0          51s



## Enable Sidecar Injection

- To enable sidecar injection, label the namespace:

  kubectl label namespace default istio-injection=enabled

## Check the label:

kubectl get namespace -L istio-injection


## Deploy the bookinfo sample app and confirm sidecar injection:


```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/bookinfo/platform/kube/bookinfo.yaml
kubectl get pods

```


## Expected output:

```

NAME                             READY   STATUS    RESTARTS   AGE
details-v1-54ffdd5947-lkfq5      2/2     Running   0          10m
productpage-v1-d49bb79b4-gr4wx   2/2     Running   0          10m
ratings-v1-856f65bcff-bs2wr      2/2     Running   0          10m
reviews-v1-848b8749df-7v22k      2/2     Running   0          10m
reviews-v2-5fdf9886c7-nv9kb      2/2     Running   0          10m
reviews-v3-bb6b8ddc7-5k4fw       2/2     Running   0          10m

```

## Configure Ingress Access

## Deploy the Istio Ingress Gateway:

kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml

## Retrieve the external IP for Minikube:

minikube tunnel


- Access the Bookinfo sample application in a browser at http://localhost/productpage. You should see the Bookinfo application page.


 Refreshing the page multiple times, you will notice that the book reviews sometimes have a red star, a black star, or no star, </br>
 indicating that traffic is routed across different versions of the reviews service.


# Uninstalling Istio


istioctl uninstall --purge
kubectl delete namespace istio-system



























































  
