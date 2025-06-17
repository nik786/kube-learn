
## Installing Istio with Helm

- Helm, a package manager for kubernetes, provides an alternative method to install istio using helm charts
- Offers greater flexibility, repeatability, and integration with helm based workflows



## Steps to install Istio in Sidecar mode

1. Add the Istio Helm Repository:

```
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update

```

2. Create the Istio Namespace

```
kubectl create namespace istio-system

```

3. Install the Istio Base Chart:

```
helm install istio-base istio/base -n istio-system

```

4. Install the Istiod Control Plane:

```

helm install istiod istio/istiod -n istio-system --set profile=default


```

5. Enable Sidecar Auto-Injection

```

kubectl label namespace default istio-injection=enabled

```

6. Install the Istio Ingress Gateway (Optional):

 ```
  helm install istio-ingressgateway istio/gateway -n istio-system
```

7. Verify the Installation:

```

   kubectl get pods -n istio-system

```

8.  Uninstall Istio

```

helm uninstall istio-ingressgateway -n istio-system
helm uninstall istiod -n istio-system
helm uninstall istio-base -n istio-system
kubectl delete namespace istio-system

```

9. Advantages of Using Helm:

```
Customization: Helm values allow fine-grained control over the installed components.
Repeatability: Helm enables version-controlled and reproducible deployments.
Production Readiness: Helm simplifies Istio upgrades and integration with other Helm-based applications.

```









    



   






  


























