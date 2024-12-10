## What is Micro Services?

| **Aspect**                       | **Microservices**                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------|
| **Functionality**                 | Isolates software functionality into multiple independent services.               |
| **Deployment**                    | Services are independently deployable, highly maintainable, and organized.        |
| **Communication**                 | Services communicate with each other through accessible APIs.                     |
| **Development**                   | Enables continuous delivery and deployment of complex applications.               |
| **Business Benefits**             | Helps deliver speed, scalability, and flexibility to companies trying to achieve agility. |



**What is Service Mesh?**
-----------------------

| **Aspect**              | **Service Mesh**                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------|
| **Definition**          | A dedicated infrastructure layer that makes service-to-service calls within a microservice architecture reliable, fast, and secure. |
| **Network Abstraction** | A mesh of proxies that services plug into to completely abstract the network.                       |
| **Specifications**      | Provides the following features:                                                                   |
| **Service Discovery**   | Enables services to discover each other within the network.                                         |
| **Load Balancing**      | Distributes network traffic evenly to optimize service performance.                                  |
| **Data Encryption**     | Ensures secure data transmission between services.                                                  |
| **Data Authentication** | Verifies the identity of services communicating with each other.                                     |
| **Data Authorization**  | Controls which services are allowed to interact with each other based on policies.                  |




# The architecture of service mesh is split between two disparate pieces:

## Data Plane:

| **Aspect**                           | **Data Plane**                                                                                          |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| **Definition**                      | A proxy service that handles communications between services.                                          |
| **Deployment**                       | Deployed as a sidecar proxy, a supporting service added to the primary application.                      |
| **Pod Deployment**                  | Proxies are deployed in the same pod as the application with a shared network namespace.                |
| **Observability**                   | Provides observability into microservices, especially through logs and metric aggregation.              |
| **Examples**                        | NGINX, HAProxy, and Envoy all provide data-plane functionality.                                         |



 ## Control Plane:

| **Aspect**                           | **Control Plane**                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| **Definition**                      | Manages policies and configurations for the data plane.                                                    |
| **Data Handling**                   | Does not handle any data.                                                                                  |
| **Tools**                            | Tools like Nelson, SmartStack, and Istio provide control-plane functionality.                              |
| **Kubernetes Integration**          | In Kubernetes, the control plane works with the orchestration system to schedule services, track service discovery, and configure proxies via API. |





## Envoy:
---------
| **Aspect**                                            | **Description**                                                                                              |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Built-in Features**                                | Envoy has features like failure handling (e.g., health checks and bounded retries), dynamic service discovery, and load balancing. |
| **Service Information**                              | Envoy provides detailed information about service requests through attributes.                               |
| **Sidecar Proxies**                                  | Envoy uses sidecar proxies per microservice to handle ingress/egress traffic between services in the cluster and from services to external services. |
| **Microservice Mesh**                                | The proxies form a secure microservice mesh with functions like discovery, layer-7 routing, circuit breakers, policy enforcement, and telemetry recording/reporting. |
| **Standalone Proxy**                                 | Envoy can be used as a standalone proxy, but when combined with Istio, it provides a full-service mesh with traffic management, security, and observability. |


## Mixer: 
----------------
| **Aspect**                            | **Description**                                                                                              |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Authorization and Auditing**       | Management of authorization and auditing within the infrastructure.                                           |
| **Policy Enforcement**               | Enforces policies such as ACLs, rate limits, quotas, authentication, request tracing, and telemetry collection at an infrastructure level. |


## Pilot: 
--------

| **Aspect**                                            | **Description**                                                                                              |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Load Balancing Traffic Control**                   | Pilot helps to manage load balancing traffic controls based on Envoy configurations.                          |
| **Communication with Kubernetes Infrastructure**      | Like Mixer, Pilot can include adapters to communicate with Kubernetes via API about deployment changes affecting traffic. |
| **Authentication Rules Distribution**                 | Pilot distributes authentication rules to proxies for security management.                                   |
| **Service Discovery**                                 | Pilot assists with service discovery and configuring Envoy sidecar proxies.                                  |
| **Distribution of Authentication Policies**           | It distributes authentication policies and secure naming information for better traffic control and security. |


## Citadel: 
---------
Secures service to service communication over TLS. 
Providing a key management system to automate key and certificate generation, distribution, rotation, and revocation

## Ingress/Egress:
----------------
Configure path based routing for inbound and outbound external traffic

## Sidecars: 
------------------
Implementation of secure communication between proxies with support for TLS encryption.

## Sidecar Injection
-------------------
The process of adding sidecars to deployment artifacts and registering them with the service mesh control plane is called “sidecar injection.” Both Istio and Linkerd support 
manual and automatic sidecar injection.

| **#** | **Category**           | **Description**                                                                                      |
|-------|------------------------|------------------------------------------------------------------------------------------------------|
| 1     | **Traffic Management**  | Managing and controlling the flow of traffic between microservices, including load balancing, routing, and retries. |
| 2     | **Security**            | Enforcing security policies, including encryption, authentication, authorization, and access control.  |
| 3     | **Installation / Configuration** | The setup and configuration process for the service mesh or related components, ensuring proper integration and functioning. |
| 4     | **Supported Environments** | Environments where the service mesh or tools are supported (e.g., Kubernetes, AWS, GCP, on-premise).  |
| 5     | **Observability**       | Tracking and monitoring the health and performance of microservices through logs, metrics, and tracing. |
| 6     | **Policy Management**   | Managing policies for routing, security, traffic control, and resource allocation across microservices. |
| 7     | **Performance**         | Ensuring that the service mesh or tool performs optimally, with low latency and high throughput.         |


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
The BookInfo sample application deployed is composed of four microservices:<br><br>
The productpage microservice is the homepage, populated using the details and reviews microservices.<br><br>
The details microservice contains the book information.<br><br>
The reviews microservice contains the book reviews. It uses the ratings microservice for the star rating.<br><br>
The ratings microservice contains the book rating for a book review.<br><br>
The deployment included three versions of the reviewsmicroservice to showcase different behaviour and routing:<br><br>
Version v1 doesn’t call the ratings service.<br><br>
Version v2 calls the ratings service and displays each rating as 1 to 5 black stars.<br><br>
Version v3 calls the ratings service and displays each rating as 1 to 5 red stars.<br><br>
The services communicate over HTTP using DNS for service discovery. An overview of the architecture is shown below.<br><br>

productpage is written in Python and calls details and reviews to populate the page.<br><br>
details is written in Ruby and contains the book information.<br><br>
reviews is written in Java and contains book reviews and calls ratings.<br><br>
ratings is written in Node.js and contains book ratings. There are three versions of this microservice in the application. A different version is called each time the page is refreshed




http://192.168.56.116:31380/productpage



COMMAND TO FORWARD GRAFANA PORT TO ACCESS FROM OUTSIDE

kubectl -n istio-system port-forward  --address 0.0.0.0 $(kubectl -n istio-system get pod -l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000

INSTALLATION OF APACHE BENCHMARK FOR LOADTESTING

Apt-get install apache2-utils

ab -n 500 -c 10 http://192.168.56.116:31380/productpage




## Reference Links:
---------------------

https://medium.com/containerum/managing-service-mesh-on-kubernetes-with-istio-60ee5e8c5efe
https://medium.com/faun/get-started-with-istio-and-kubernetes-386c71f2a61d

https://www.linode.com/docs/kubernetes/how-to-deploy-istio-with-kubernetes/
https://istio.io/docs/examples/bookinfo/
https://www.oreilly.com/library/view/istio-up-and/9781492043775/ch04.html





