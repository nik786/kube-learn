| **Chart Type**         | **Description**                                                                                 | **Examples**                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **Application Charts**  | Define how to deploy specific applications or services on Kubernetes.                         | WordPress, MySQL, Nginx, Redis.                             |
|                         | Include resources like Deployments, Services, ConfigMaps, and Ingress for application management. |                                                             |
| **Library Charts**      | Reusable charts defining shared logic or templates, used in other charts.                     | A chart for PodSecurityPolicy or shared storage volume configurations. |
|                         | Do not create Kubernetes resources directly but provide common functionalities.              |                                                             |
| **Stable Charts**       | Well-maintained and officially supported charts, typically production-ready.                  | Found in the Helm stable repository.                        |
| **Incubating Charts**   | Charts under development or testing, not yet production-ready but available for feedback.     | Used for experimentation and iteration.                     |



| **Command**                                       | **Description**                                                        |
|---------------------------------------------------|------------------------------------------------------------------------|
| **Package a Chart**                               | `helm package my-chart/`                                                |
|                                                   | Packages the Helm chart into a `.tgz` file.                             |
| **Lint a Chart**                                  | `helm lint my-chart/`                                                   |
|                                                   | Lints a Helm chart to check for potential issues and errors.           |
| **Render Chart Templates Locally**                | `helm template my-release nginx --namespace web-apps`                   |
|                                                   | Renders the Kubernetes manifests locally without installing the chart. |
| **History of a Release**                          | `helm history <release-name>`                                           |
|                                                   | Displays the release history of a Helm deployment.                     |
| **Diff a Release**                                | `helm plugin install https://github.com/databus23/helm-diff`            |
|                                                   | Installs the Helm diff plugin, then `helm diff upgrade <release-name> <chart-name>` to compare releases. |
| **Uninstall a Release**                           | `helm uninstall my-release --namespace web-apps`                        |
|                                                   | Uninstalls a specific Helm release from a given namespace.             |
| **Search for Charts**                             | `helm search repo nginx`                                               |
|                                                   | Searches the Helm repository for a chart (e.g., nginx).                |
| **Add a Helm Repository**                         | `helm repo add bitnami https://charts.bitnami.com/bitnami`               |
|                                                   | Adds a Helm repository to your local configuration.                    |
| **Update Helm Repositories**                      | `helm repo update`                                                     |
|                                                   | Updates the Helm repository index to fetch the latest charts.          |
| **Show Chart Details**                            | `helm show chart bitnami/nginx`                                         |
|                                                   | Displays detailed information about a specific chart.                  |
| **View Chart Values**                             | `helm show values bitnami/nginx`                                        |
|                                                   | Displays the default values for a Helm chart.                           |




| **Concept**                        | **Description**                                                                                                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Helm Repositories**               | Collections of Helm charts. Users can add repositories (e.g., Bitnami, JFrog, custom ones) for searching, updating, and installing charts from various sources.                 |
| **Templating Engine**               | Helm uses Go templates to define dynamic and reusable resources, allowing resources to adapt based on installation values. This makes Helm charts flexible and customizable.     |
| **Chart Dependencies**              | Helm charts can depend on other charts, defined in the `Chart.yaml` file. Helm manages dependencies to support complex applications with multiple components (e.g., databases).  |
| **Helm Hooks**                      | Tasks performed at specific points in the release lifecycle, such as before installing or after upgrading. Useful for actions like database migrations or pre/post-deployment.  |
| **Helmfile for Multi-Chart Management** | Helmfile is an open-source tool for managing multiple Helm releases with a single configuration file. Useful for complex deployments requiring multiple charts and configurations.|
| **What is Helm?**                   | Helm is a Kubernetes package manager that simplifies application deployments by defining, installing, and upgrading applications as charts (collections of Kubernetes manifests). |
| **Helm Charts**                     | A collection of files that define a set of Kubernetes resources, including templates, metadata, and values. Charts can be shared or customized and are stored in repositories.   |
| **Values Files**                    | The `values.yaml` file in a Helm chart holds customizable parameters. Users can override values during deployment without modifying the core chart structure.                    |
| **Release Management**              | When a Helm chart is installed, a release is created to represent an instance of that chart. Helm tracks and manages these releases, supporting versioning and rollbacks.        |




Helm Commands
------------------

1. helm install: Deploys a chart as a release to a Kubernetes cluster.
2. helm upgrade: Upgrades a release with updated chart configurations or a new version.
3. helm rollback: Rolls back a release to a previous version.
4. helm list: Lists all Helm releases in the cluster.
5. helm uninstall: Removes a release from the cluster.
6. helm install my-release nginx --namespace web-apps
7. helm list --namespace blue
8. helm upgrade my-release nginx --set replicaCount=3
9. helm rollback <release-name> <revision>



HELM CONFIG FOR TOMCAT
---------------------------

helm fetch  bitnami/tomcat -d tomcat/

docker build -t 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:tom-61 --pull=true --file=/var/lib/jenkins/hello-world/Dockerfiles/tomcat-dockerfile  /var/lib/jenkins/hello-world/Dockerfiles/

docker push 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:tom-60


helm install mytomcat ./tomcat --set image.registry=758637906269.dkr.ecr.us-east-1.amazonaws.com --set image.repository=connector-dev --set image.tag=tom-61  -n testing

helm uninstall tomcat-1585376255 -n testing

helm ls -n testing


HELM CONFIG FOR Nginx
------------------------

docker build -t 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:nginx-60 --pull=true --file=/var/lib/jenkins/hello-world/Dockerfiles/nginx-dockerfile  /var/lib/jenkins/hello-world/Dockerfiles/

docker push 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:nginx-60

helm install mynginx ./nginx --set image.registry=758637906269.dkr.ecr.us-east-1.amazonaws.com --set image.repository=connector-dev --set image.tag=nginx-60  -n testing

kubectl get svc -n testing -o wide

kubectl get po -n testing -o wide

curl  http://192.168.56.145:30080

LOADTESTING
---------------

for i in {1..10};do ab -n 100 -c 2 http://10.233.22.155/;done

ab -n 1000 -c 2 http://10.233.68.224/
for i in {1..1000};do curl -I  http://10.233.119.203/;done
while true; do curl -I http://hpa-nginx/; done
while true; do ab -n 1000 -c 2 http://hpa-nginx/; done


