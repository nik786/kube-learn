

## Install Istio using Helm

We will install istio on the cluster using helm

1. Add the Istio Helm repository

  ```
   helm repo add istio https://istio-release.storage.googleapis.com/charts
   helm repo update
 ```

2. Install the Istio base chart (CRDs):

```

helm install istio-base istio/base -n istio-system --set defaultRevision=default --create-namespace

```

3. Install an Istio profile (e.g., demo):

   ```
    helm install istiod istio/istiod -n istio-system --set profile=demo
   ```

4. Label the default namespace for automatic sidecar injection:

   ```
   kubectl label namespace default istio-injection=enabled

   ```
5. Verify the installation:

   ```
   kubectl get pod -n istio-system
   ```
6. 




   
