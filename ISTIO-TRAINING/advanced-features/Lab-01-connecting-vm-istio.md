
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



## Create the Virtual Machine

1. Create the VM

```
gcloud compute instances create my-mesh-vm --tags=mesh-vm --machine-type=n1-standard-2

```

2. Obtain the cluster's Pod IP address range. Make sure to replace <CLUSTER_NAME> with an actual cluster name and <ZONE> with the zone the cluster is running in

```
CLUSTER_POD_CIDR=$(gcloud container clusters describe <CLUSTER_NAME> --zone <ZONE> --format=json | jq -r '.clusterIpv4Cidr')

```

3. Create a firewall rule to allow ingress on port 80 from the cluster pods to the VM

```

gcloud compute firewall-rules create "cluster-pods-to-vm" \
  --source-ranges=$CLUSTER_POD_CIDR \
  --target-tags=mesh-vm \
  --action=allow \
  --rules=tcp:80

```

4. Configure the Virtual Machine

Copy the files from vm-files folder to the home folder on the instance. Replace USERNAME and INSTANCE_IP accordingly.

In this example, we run a simple Python HTTP server on port 80. You could configure any other service on a different port. 
Just make sure you configure the security and firewall rules accordingly.

```
gcloud compute scp vm-files/* my-mesh-vm:~ --zone=[INSTANCE_ZONE]

gcloud beta compute ssh --zone=[INSTANCE_ZONE] my-mesh-vm

sudo mkdir -p /etc/certs
sudo cp root-cert.pem /etc/certs/root-cert.pem

Copy the istio-token file to /var/run/secrets/tokens folder

sudo mkdir -p /var/run/secrets/tokens
sudo cp istio-token /var/run/secrets/tokens/istio-token

Download and install the Istio sidecar package

curl -LO https://storage.googleapis.com/istio-release/releases/1.24.3/deb/istio-sidecar.deb
sudo dpkg -i istio-sidecar.deb

Copy cluster.env to /var/lib/istio/envoy/:

cp cluster.env /var/lib/istio/envoy/cluster.env


Copy Mesh config (mesh.yaml) to /etc/istio/config/mesh

cp mesh.yaml /etc/istio/config/mesh

Add the istiod host to the /etc/hosts file


sh -c 'cat $(eval echo ~$SUDO_USER)/hosts >> /etc/hosts'


Change the ownership of files in /etc/certs and /var/lib/istio/envoy to the Istio proxy:


sudo mkdir -p /etc/istio/proxy
sudo chown -R istio-proxy /var/lib/istio /etc/certs /etc/istio/proxy /etc/istio/config /var/run/secrets /etc/certs/root-cert.pem


```

Because we used the VM auto-registration, Istio automatically creates the WorkloadEntry resource for us shortly after we start the Istio service on the VM


1. Watch for Workloadentry resources using the --watch flag
   
   kubectl get workloadentry -n vm-namespace --watch

2. On the VM, start the Istio service
   systemctl start istio

3. You should see the WorkloadEntry appear

   ```
    NAME                  AGE   ADDRESS
    hello-vm-10.128.0.7   12m   10.128.0.7

   ```
   

You can check that the istio service is running with systemctl status istio. 
Alternatively, we can look at the contents of the /var/log/istio/istio.log to 
see that the proxy was successfully started.


## Access services from the virtual machine


From a different terminal window, we can now deploy a Hello world application to the Kubernetes cluster. 
First, we need to enable the automatic sidecar injection in the default namespace:


kubectl label namespace default istio-injection=enabled


Next, create the Hello world Deployment and Service.

```
cat hello-world.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
  labels:
    app: hello-world
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - image: gcr.io/tetratelabs/hello-world:1.0.0
          imagePullPolicy: Always
          name: svc
          ports:
            - containerPort: 3000
---
kind: Service
apiVersion: v1
metadata:
  name: hello-world
  labels:
    app: hello-world
spec:
  selector:
    app: hello-world
  ports:
    - port: 80
      name: http
      targetPort: 3000

```

Wait for the Pods to become ready and then go back to the virtual machine and try to access the Kubernetes service:

curl http://hello-world.default


## Run services on the virtual machine


We can also run a workload on the virtual machine. Switch to the virtual machine instance and run a simple Python HTTP server

python3 -m http.server 80


```

cat hello-vm-service.yaml

apiVersion: v1
kind: Service
metadata:
  name: hello-vm
  namespace: vm-namespace
  labels:
    app: hello-vm
spec:
  ports:
  - port: 80
    name: http-vm
    targetPort: 80
  selector:
    app: hello-vm

```

We can now use the Kubernetes service name hello-vm.vm-namespace to access the workload running on the virtual machine

Let's run a Pod inside the cluster and try to access the service from there:

kubectl run curl --image=radial/busyboxplus:curl -i --tty --rm


curl hello-vm.vm-namespace













































