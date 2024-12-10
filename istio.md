What is Micro Services?
It  isolates software functionality into multiple independent services 
These services are independently deployable, highly maintainable and organized 
These services communicate with each other through accessible APIs. 
Microservices enable continuous delivery and deployment of complex applications. 
On a higher business level, microservices help to deliver speed, scalability, and flexibility to companies trying to achieve agility .


What is Service Mesh
A service mesh is a dedicated infrastructure layer which makes service-to-service calls within a microservice architecture, reliable, fast and secure. 
It is a mesh of proxies which services can plug into to completely abstract the network away.
It provides below mentioned specifications:
Service Discovery
Load balancing
Data encryption
Data Authentication
Data Authorization


The architecture of service mesh is split between two disparate pieces: 
Data Plane:
It is essentially a proxy service which handles communications between services
Data plane is deployed as a sidecar proxy ,a supporting service added to the primary application
Proxies are deployed in the same pod as an application with a shared network namespace 
Data planes provide observability into microservices, particularly in the form of logs and metric aggregation
NGINX, HAProxy, and Envoy all provide data-plane functionality.


 Control Plane:
It manages policies and configurations for data plane.
It does not handle any data. 
Tools like Nelson, SmartStack, and Istio all provide control-plane functionality.
In Kubernetes, for example, the control plane works in conjunction with the orchestration system to schedule services and their proxies, track service discovery, and configure proxies via API.


Envoy as a standalone proxy without a control plane, but it’s Istio’s unique approach to the control plane/data plane workflow, as well as its core features (traffic management, security, observability) that, 
when combined with Envoy, makes it increasingly appealing to many users as a fully functional service mesh



Envoy: 
i. Built-in features such as failure handling (for example, health checks and bounded retries), 
Ii. dynamic service discovery, and load balancing make Envoy a powerful tool. 
Iii. Envoy also provides information about service requests through attributes.
iv. Sidecar proxies per microservice to handle ingress/egress traffic between services in the cluster and from service to external services.
V. The proxies form a secure microservice mesh providing a rich set of functions like discovery, rich layer-7 routing, circuit breakers, policy enforcement, and telemetry recording/reporting functions.

Mixer: 
Management of authorization and auditing.
Enforce policies such as ACLs, rate limits, quotas, authentication, request tracing and telemetry collection at an infrastructure level

Pilot: 
It helps to manage load balancing traffic controls based on  Envoy configurations. 
As with Mixer, we can include adapters so Pilot can communicate via API with your Kubernetes infrastructure about deployment changes affecting traffic. 
Also Pilot  distributes authentication rules to proxies.
Service discovery and for configuring the Envoy sidecar proxies
Distribution of authentication policies and secure naming information.

Citadel: 
Secures service to service communication over TLS. 
Providing a key management system to automate key and certificate generation, distribution, rotation, and revocation
Ingress/Egress:

Configure path based routing for inbound and outbound external traffic

Sidecars: 
 Implementation of secure communication between proxies with support for TLS encryption.

Sidecar Injection
The process of adding sidecars to deployment artifacts and registering them with the service mesh control plane is called “sidecar injection.” Both Istio and Linkerd support manual and automatic sidecar injection.

Traffic Management
Security
Installation / Configuration
Supported Environments
Observability
Policy Management
Performance

Configuration of ISTIO:

This Configuration has been tested with kubernetes v1.13.5 and istio-1.0.6



Download of  ISTIO:

https://github.com/istio/istio/releases/download/1.0.6/istio-1.0.6-linux.tar.gz
https://github.com/istio/istio/releases/download/1.4.3/istio-1.4.3-linux.tar.gz

export PATH=/opt/istio/istio-1.0.6/bin:$PATH




sed -i 's/LoadBalancer/NodePort/;s/31380/30080/' ./install/kubernetes/istio-demo.yaml


ClusterIP need to be replaced by NodePort Type
Loadbalancer Type need to be replaced by NodePort Type
In istio-demo.yaml




INSTALLATION OF ISTIO-SYSTEM

kubectl apply -f install/kubernetes/istio-demo.yaml


VERIFICATION OF ISTIO SERVICES

kubectl get service -n istio-system

VERIFICATION OF ISTIO PODS

kubectl get pods -n istio-system

DEPLOYMENT OF SAMPLE APP

kubectl create -f <(istioctl kube-inject -f samples/bookinfo/platform/kube/bookinfo.yaml)

VERIFICATION OF SAMPLE APP SERVICES

kubectl get service 

VERIFICATION OF SAMPLE APP PODS
kubectl get pods 

DEPLOYMENT OF GATEWAY TO ACCESS APP FROM OUTSIDE

kubectl create -f samples/bookinfo/networking/bookinfo-gateway.yaml

kubectl get gateway

kubectl get svc istio-ingressgateway -n istio-system


Bookinfo Architecture
The BookInfo sample application deployed is composed of four microservices:
The productpage microservice is the homepage, populated using the details and reviews microservices.
The details microservice contains the book information.
The reviews microservice contains the book reviews. It uses the ratings microservice for the star rating.
The ratings microservice contains the book rating for a book review.
The deployment included three versions of the reviewsmicroservice to showcase different behaviour and routing:
Version v1 doesn’t call the ratings service.
Version v2 calls the ratings service and displays each rating as 1 to 5 black stars.
Version v3 calls the ratings service and displays each rating as 1 to 5 red stars.
The services communicate over HTTP using DNS for service discovery. An overview of the architecture is shown below.

productpage is written in Python and calls details and reviews to populate the page.
details is written in Ruby and contains the book information.
reviews is written in Java and contains book reviews and calls ratings.
ratings is written in Node.js and contains book ratings. There are three versions of this microservice in the application. A different version is called each time the page is refreshed




http://192.168.56.116:31380/productpage



COMMAND TO FORWARD GRAFANA PORT TO ACCESS FROM OUTSIDE

kubectl -n istio-system port-forward  --address 0.0.0.0 $(kubectl -n istio-system get pod -l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000

INSTALLATION OF APACHE BENCHMARK FOR LOADTESTING

Apt-get install apache2-utils

ab -n 500 -c 10 http://192.168.56.116:31380/productpage




Reference Links:

https://medium.com/containerum/managing-service-mesh-on-kubernetes-with-istio-60ee5e8c5efe
https://medium.com/faun/get-started-with-istio-and-kubernetes-386c71f2a61d

https://www.linode.com/docs/kubernetes/how-to-deploy-istio-with-kubernetes/
https://istio.io/docs/examples/bookinfo/
https://www.oreilly.com/library/view/istio-up-and/9781492043775/ch04.html





