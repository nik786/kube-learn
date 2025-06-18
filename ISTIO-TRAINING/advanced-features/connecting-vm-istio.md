
## Connecting a VM to Istio ServiceMesh

- Connect a VM Workload to Istio servicemesh on kubernetes
- Use WorkloadEntry auto-registration
- Deploy an istio east-west gateway for vm connectivity
- Run services on both kubernetes and the VM


## Installing Istio on a Kubernetes cluster

curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.24.3 sh -


We can now create an IstioOperator resource we'll use to install Istio. One of the differences between 
regular Istio installation and one that supports VM workloads is in setting cluster name and network. In this lab we'll 
set the network name to an empty string because we'll only use a single network. 
For multi-network scenario we'd set the VM and the cluster network name separately.


```
cat istio-vm-install.yaml

apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: istio
spec:
  values:
    global:
      meshID: mesh1
      multiCluster:
        clusterName: Kubernetes
      network: ""

```



We'll use istioctl to install Istio on the cluster. Additionally, we'll set the 
PILOT_ENABLE_WORKLOAD_ENTRY_AUTOREGISTRATION and PILOT_ENABLE_WORKLOAD_ENTRY_HEALTHCHECKS to true 
note that these features are in being actively developed and are considered experimental.




Let's deploy the IstioOperator resource:


```
istioctl install -f istio-vm-install.yaml \
  --set values.pilot.env.PILOT_ENABLE_WORKLOAD_ENTRY_AUTOREGISTRATION=true \
  --set values.pilot.env.PILOT_ENABLE_WORKLOAD_ENTRY_HEALTHCHECKS=true

```


Once the installation completes, we can deploy a separate ingress gateway that will be used to expose 
the Istio's control plane to the virtual machine.

The Istio package we downloaded contains a script we can use to generate the YAML that will deploy 
an Istio operator that creates the new gateway called istio-eastwestgateway.


```

samples/multicluster/gen-eastwest-gateway.sh --single-cluster | istioctl install -y -f -

kubectl get po -n istio-system

NAME                                     READY   STATUS    RESTARTS   AGE
istio-eastwestgateway-59cc6fcdb6-b64rs   1/1     Running   0          34s
istio-ingressgateway-69b7dd67d6-5pj6b    1/1     Running   0          7m58s
istiod-58596b9585-rq8f5                  1/1     Running   0          8m11s


```


For virtual machines to access the Istio's control plane, we need to create a Gateway resource to 
configure the istio-eastwestgateway, and a VirtualService that has the Gateway attached



We can use another script from the Istio package to create these resources and expose the control plane


```
kubectl apply -f samples/multicluster/expose-istiod.yaml

```


## Preparing virtual machine namespace and files


Let's create a separate folder called vm-files to store these files. 
We can also save the full path to the folder in the WORK_DIR environment variable:

```
mkdir -p vm-files
export WORK_DIR="$PWD/vm-files"

```

We also set a couple of environment variables before continuing, so we don't have to re-type the values each time:

```
export VM_APP="hello-vm"
export VM_NAMESPACE="vm-namespace"
export SERVICE_ACCOUNT="vm-sa"

```

Let's create the VM namespace and the service account we will use for VM workloads in the same namespace:

```
kubectl create ns "${VM_NAMESPACE}"

kubectl create serviceaccount "${SERVICE_ACCOUNT}" -n "${VM_NAMESPACE}"

```

create the WorkloadGroup resource using Istio CLI

```

istioctl x workload group create --name "${VM_APP}" --namespace "${VM_NAMESPACE}" --labels app="${VM_APP}" --serviceAccount "${SERVICE_ACCOUNT}" > workloadgroup.yaml

cat workloadgroup.yaml

apiVersion: networking.istio.io/v1alpha3
kind: WorkloadGroup
metadata:
  name: hello-vm
  namespace: vm-namespace
spec:
  metadata:
    annotations: {}
    labels:
      app: hello-vm
  template:
    ports: {}
    serviceAccount: vm-sa

kubectl apply -f workloadgroup.yaml.

kubectl apply -f workloadgroup.yaml -n ${VM_NAMESPACE}

```

Virtual machine needs information about the cluster and Istio's control plane to connect to it. To generate the required files, we can run istioctl x workload entry command


```

istioctl x workload entry configure -f workloadgroup.yaml -o "${WORK_DIR}" --autoregister --clusterID "Kubernetes"

```


## The above command generates the following files


- cluster.env: Contains metadata that identifies what namespace, service account, network CIDR and (optionally) what inbound ports to capture.
- istio-token: A Kubernetes token used to get certs from the CA.
- mesh.yaml: Provides ProxyConfig to configure discoveryAddress, health-checking probes, and some authentication options.
- root-cert.pem: The root certificate used to authenticate.
- hosts: An addendum to /etc/hosts that the proxy will use to reach istiod for xDS




































































