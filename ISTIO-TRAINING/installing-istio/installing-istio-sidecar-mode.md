
## Installing Istio in Sidecar Mode

- Use istioctl to install Istio with the demo profile
- Label the namespace to enable automatic sidecar injection
- Verify Istiod and Istio-ingress gateway pods are running



 1. Install Istio with istioctl:
   - For testing and development, use the demo profile:

  ```
  istioctl install --set profile=demo --skip-confirmation

  ```

The demo profile installs the control plane and gateways, making it suitable for learning.

Note: For production environments, it is recommended to use the default profile instead.

2. Enable Sidecar Auto-Injection:

  ```
  kubectl label namespace default istio-injection=enabled
 ```
This labels the default namespace to automatically inject sidecars into workloads.

3. Verify the Installation:
   
kubectl get pods -n istio-system

Ensure istiod and istio-ingressgateway pods are in a Running state



## Installing Istio in Ambient Mode

- No sidecars, uses node-level ztunnel and optional waypoint proxies
- Start by meeting platform-specific prerequisites
- Install kubernetes Gateway API CRDS
- Install Istio with an ambient profile
- Label namespaces for ambient enrollment
- Optionally deploy a waypoint proxy



## Platform Prerequisites for Ambient Mode

 - GKE: Needs a ResourceQuota for system-node-critical pods in istio-system
 - AKS: No Extra steps, but ensure network policies are enabled
 - EKS: Works by default, CALICO CNI  Recommended
 - Kind/k3d/minikube: Check CNI and network policy support

  ## Installing and Enabling Ambient Mode
 
 - Install Gateway API CRDS if not already present
 - Run the ambient profile installation with istioctl
 - Label the namespace for ambient mode
 - Optionally apply a waypoint proxy
 - Confirms istiod and ztunnel pods are running

  

## GKE:

- Pods with the system-node-critical priorityClassName require a namespace with a ResourceQuota. By default, only kube-system has this quota.
- To use istio-system, create a ResourceQuota


```
 apiVersion: v1
kind: ResourceQuota
metadata:
  name: gcp-critical-pods
  namespace: istio-system
spec:
  hard:
    pods: 1000
  scopeSelector:
    matchExpressions:
    - operator: In
      scopeName: PriorityClass
      values:
      - system-node-critical

```
## Use the gke platform profile for installation

  helm install istio-cni istio/cni -n istio-system --set profile=ambient --set global.platform=gke --wait

1. Install Kubernetes Gateway API CRDs:

 kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.1/standard-install.yaml; }


2. Install Istio with the Ambient Profile:

- istioctl install --set profile=ambient --skip-confirmation

- This installs istiod, ztunnel, and CNI components.


 3. Configure Namespace for Ambient Mode

 - kubectl label namespace default istio.io/dataplane-mode=ambient

 - This enrolls the namespace in ambient mode without requiring sidecar injection.


 4. Deploy a Waypoint Proxy (Optional):

```
     istioctl waypoint apply -n default --service-account default

     This creates a waypoint proxy for the default service account in the default namespace. For namespace-wide deployment:

     istioctl waypoint apply -n default --enroll-namespace

    You can verify waypoint deployment with:

    kubectl get waypoint -n default


```

5. Verify the Installation:
    
    kubectl get pods -n istio-system

   Check that istiod and ztunnel pods are running.


    










 



   
## Canary upgrades with revisions

- Installs a specific revision using istioctl
- Label the namespace with the revision
- Restart pods to apply the new version
- Use revision tags to manage versions
- Allow gradual migration and rollback


## Installing with a Revision Tag

1. Install a Specific Revision:
   
   istioctl install --set revision=1-24-3 --set profile=default --skip-confirmation

   This installs Istio with a revision label "1-24-3".

2. Label Namespaces with the Revision:

    kubectl label namespace default istio.io/rev=1-24-3 --overwrite

   This tells Istio to use the specified revision for this namespace.

3. Restart Pods to Pick up the New Revision:

   kubectl rollout restart deployment -n default

4. Managing Multiple Revisions

   You can use revision tags to manage different versions:

   istioctl tag set prod-stable --revision=1-24-3

   Then reference the tag in your namespace:

   kubectl label namespace default istio.io/rev=prod-stable --overwrite
 
   This approach allows for:

   - Testing new Istio versions in specific namespaces
   - Easily rolling back if issues are discovered
   - Gradual migration of workloads to new versions
   - When ready to remove the old revision:

   istioctl uninstall --revision=<old-revision>


   


  

   
## Managing Istio Revisions

- Use Istioctl tag to assign friendly names to revisions
- Label namespaces with the tag
- Remove old revisions when no longer needed
  













 
