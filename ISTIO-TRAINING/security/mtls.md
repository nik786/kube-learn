## 🔐 Mutual TLS in Istio

### 📦 How mTLS Works in Istio

| **Step** | **Description** |
|----------|------------------|
| **1. Communication Flow** | All communication between workloads is routed through **Envoy sidecars**. |
| **2. Traffic Redirection** | Istio **re-routes** traffic from workloads to the sidecar **Envoy proxies**. |
| **3. Handshake Initiation** | The **client-side Envoy** initiates an **mTLS handshake** with the **server-side Envoy**. |
| **4. Secure Naming Check** | The client validates that the **service account in the server's certificate** is authorized. |
| **5. Traffic Forwarding** | After verification, the server-side Envoy forwards traffic to the **target workload**. |

---

### 🔧 TLS Modes in Destination Rule

| **Mode**         | **Description**                                                                 |
|------------------|----------------------------------------------------------------------------------|
| `DISABLE`        | No TLS connection is used                                                        |
| `SIMPLE`         | TLS connection **without client certificate** (one-way TLS)                      |
| `MUTUAL`         | Mutual TLS connection with client certificates                                   |
| `ISTIO_MUTUAL`   | Same as MUTUAL but uses **Istio-generated certificates** automatically           |

---

### 🧪 Permissive Mode

| **Feature**                | **Details**                                                                 |
|----------------------------|------------------------------------------------------------------------------|
| **Definition**             | Allows services to accept both **mTLS** and **plain-text** traffic           |
| **Purpose**                | Helps with **gradual onboarding** to mTLS                                    |
| **Default Behavior**       | Istio enables **permissive mode** by default                                |
| **Sidecar Detection**      | Istio detects workloads with Envoy sidecars and sends **mTLS** to them       |
| **Fallback for Non-Sidecar** | Sends **plain text** traffic if no sidecar exists                          |
| **Transition Strategy**    | Start in permissive mode → deploy sidecars → switch to **STRICT** mode      |

---

### 🛡️ Enforcing Strict mTLS

| **Step** | **Action**                                                                 |
|----------|------------------------------------------------------------------------------|
| 1        | Deploy Istio sidecars across all workloads                                  |
| 2        | Create `PeerAuthentication` resource with mode `STRICT` at **namespace level** |
| 3        | Gradually enforce policy in each namespace                                  |
| 4        | Finally, enforce **global strict mTLS** by applying policy in `istio-system` |

---

> ✅ Start with **permissive mode** for compatibility  
> 🔒 End with **strict mTLS** for maximum security across the mesh




```

We can create the PeerAuthentication resource and enforce strict mode in each namespace separately at first.
Then, we can create a policy in the root namespace (istio-system in our case) that 
implements the policy globally across the mesh.


apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
    


```




```

Additionally, we can also specify the selector field and apply the policy only to specific workloads in the mesh. 
The example below enables STRICT mode for workloads with the specified label:


apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: my-namespace
spec:
  selector:
    matchLabels:
      app: customers
  mtls:
    mode: STRICT
    
Enable mTLS
   
In this lab, we will deploy the sample application (Web Frontend and Customer service).
The web frontend will be deployed without an Envoy proxy sidecar, 
while the Customer service will have the sidecar injected. 

With this setup, we will see how Istio can send both mTLS and 
plain text traffic and change the TLS mode to STRICT



```



```

Let’s start by deploying a Gateway resource:

apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: gateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - '*'
        
 Save the above YAML to gateway.yaml and deploy the Gateway using kubectl apply -f gateway.yaml

```

If we look at the running Pods, we should see one Pod with a single container running, 
indicated by the 1/1 in the READY column:
 
 kubectl label namespace default istio-injection=enabled
              
```        
   
apiVersion: apps/v1
kind: Deployment
metadata:
  name: customers-v1
  labels:
    app: customers
    version: v1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: customers
      version: v1
  template:
    metadata:
      labels:
        app: customers
        version: v1
    spec:
      containers:
        - image: gcr.io/tetratelabs/customers:1.0.0
          imagePullPolicy: Always
          name: svc
          ports:
            - containerPort: 3000
---
kind: Service
apiVersion: v1
metadata:
  name: customers
  labels:
    app: customers
spec:
  selector:
    app: customers
  ports:
    - port: 80
      name: http
      targetPort: 3000
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: customers
spec:
  hosts:
    - 'customers.default.svc.cluster.local'
  http:
    - route:
        - destination:
            host: customers.default.svc.cluster.local
            port:
              number: 80   
   
    
    
Save the above to customers-v1.yaml and create the deployment and service using kubectl apply -f customers-v1.yaml.

```

Save the above to customers-v1.yaml and create the deployment and service using kubectl apply -f customers-v1.yaml.

We should have both applications deployed and running - the customers’ 
service will have two containers, and the web frontend service will have one:
kubectl get po

If we try and access the web page from the GATEWAY_URL, we will get the web page with the customer service’s response.
Accessing the GATEWAY_URL works because of the permissive mode, 
where plain text traffic gets sent to the services that don’t have the proxy.

In this case, the ingress gateway sends plain text traffic to the Web frontend because there’s no proxy.


If we open Kiali with getmesh istioctl dash kiali and look at the Graph, you will notice that Kiali 
detects calls made from the ingress gateway to web-frontend. However, 
the calls made to the customers service are coming from unknown service.
This is because there’s no proxy next to the web frontend.
Therefore Istio doesn’t know who, where or what that service is.

Let’s update the customers VirtualService and attach the gateway to it. 
Attaching the gateway allows us to make calls directly to the customers service




```

apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: customers
spec:
  hosts:
    - 'customers.default.svc.cluster.local'
  gateways:
    - gateway
  http:
    - route:
        - destination:
            host: customers.default.svc.cluster.local
            port:
              number: 80


```




Save the above to vs-customers-gateway.yaml and update the VirtualService using kubectl apply -f vs-customers-gateway.yaml.

We can now specify the Host header and we’ll be able to send the requests through 
the ingress gateway (GATEWAY_URL) to the customers service:

curl -H "Host: customers.default.svc.cluster.local" http://$GATEWAY_URL;

To generate some traffic to both the Web frontend and Customers service through the ingress, 
open the two terminal windows and run one command in each

// Terminal 1 
$ while true; do curl -H "Host: customers.default.svc.cluster.local" http://$GATEWAY_URL; done

// Terminal 2
$ while true; do curl http://$GATEWAY_URL; done

Open Kiali and look at the Graph. From the Display dropdown, make sure we check the Security option.
You should see a graph similar to the one in the following figure.

Let’s see what happens if we enable mTLS in STRICT mode. We expect the calls from the frontend 
to the customer service to start failing because there’s no proxy injected to do the mTLS communication.
On the other hand, the calls from the ingress gateway to the customer service will continue working.


```

apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: default
spec:
  mtls:
    mode: STRICT
    
```

    
Save the above YAML to strict-mtls.yaml and create the PeerAuthentication resource using kubectl apply -f strict-mtls.yaml.

If we still have the request loop running, we will see the ECONNRESET error message from the web frontend. 
This error indicates that the customers side closed the connection. 
In our case, it was because it was expecting an mTLS connection.

On the other hand, the requests we’re making directly to the customers service continue to work because
the customer service has an Envoy proxy running next to it and can do mutual TLS.

If we delete the PeerAuthentication resource deployed earlier (kubectl delete peerauthentication default), 
Istio returns to its default (PERMISSIVE mode), and the errors will disappear.

Delete the Deployments, Services, VirtualServices, and the Gateway:



```

kubectl delete deploy web-frontend customers-v1
kubectl delete svc customers web-frontend
kubectl delete vs customers web-frontend
kubectl delete gateway gateway

```










