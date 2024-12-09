**DevOps** is a collaborative culture and a set of practices designed to bridge the gap between development and operations teams. Its core focus is on enhancing communication, optimizing workflows, and accelerating software delivery. By leveraging automation, continuous integration and delivery (CI/CD), and infrastructure as code (IaC), DevOps ensures that software is built, tested, and deployed faster and with greater reliability. The ultimate goal is to create a seamless development pipeline that enables more frequent and reliable releases, fostering an environment of continuous improvement.



| **Aspect**               | **Continuous Integration (CI)**                                                                                     | **Continuous Delivery (CD)**                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Focus**                 | Focuses on integrating code frequently into a shared repository.                                                    | Focuses on automating the release process to ensure code is always in a deployable state.                       |
| **Process Involvement**   | Involves automatic testing and integration of code into the main branch.                                            | Extends CI by automating the entire release pipeline, including deployment to staging and production.           |
| **Deployment Frequency**  | CI doesn't deploy code to production, only integrates and tests.                                                    | CD automates deployment, ensuring that the code can be released anytime with minimal manual intervention.       |
| **Goal**                  | To detect integration issues early and improve collaboration between developers.                                     | To ensure that code is always in a deployable state and can be released to production at any time.              |
| **Automation Level**      | Automates integration and testing of code changes.                                                                  | Automates the entire release process from integration to production deployment.                                |
| **Pipeline Stage**        | Typically involves build, test, and integration stages.                                                              | Involves build, test, integration, and automated release stages, with production deployment being automated.    |





| **Phase**    | **Description**                                                               |
|--------------|-------------------------------------------------------------------------------|
| **Plan**     | Define and prioritize development goals and tasks collaboratively.           |
| **Develop**  | Write and integrate code using version control and continuous integration.   |
| **Build**    | Compile and package the application into deployable artifacts.               |
| **Test**     | Automate testing to ensure functionality, security, and performance.         |
| **Release**  | Prepare and stage the application for deployment.                            |
| **Deploy**   | Automate the delivery of applications to production environments.            |
| **Operate**  | Monitor, manage, and maintain applications in production.                    |
| **Monitor**  | Continuously track performance and gather feedback for improvement.          |




A branching strategy defines how code branches are managed in version control to
facilitate collaboration, development, and release cycles.

There are several types of branching strategies, including:





| **Branching Model**        | **Description**                                                                                                    | **Ideal For**                                                                                   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Git Flow**               | A robust branching model with dedicated branches for features, releases, and hotfixes. Uses `master` and `develop` branches. | Complex projects with multiple releases, features, and hotfixes.                               |
| **GitHub Flow**            | A lightweight model with a single main branch; all changes come from feature branches and pull requests.          | Continuous deployment and simpler workflows with fewer release cycles.                         |
| **GitLab Flow**            | Combines aspects of Git Flow and GitHub Flow with environment-specific branches like staging and production.        | Projects that need alignment with deployment environments and continuous integration.           |
| **Trunk-based Development**| Developers commit directly to a single shared branch (trunk) or integrate with short-lived feature branches.       | Continuous integration and fast-paced environments where frequent changes are made.             |
| **Feature Branching**      | Each feature is developed in a separate branch and merged after completion. Promotes isolation and easier code reviews. | Projects that require isolated development and review of individual features.                   |

and hotfixes. It consists of specific branches:

Master: Holds production-ready code.
Develop: The main integration branch where features are merged.
Feature branches: Created from develop to work on new features and merged back into develop.
Release branches: Created from develop when preparing for a new release, 
used for final testing and bug fixes.
Hotfix branches: Created from master to quickly fix issues in production, 
then merged into both master and develop.
Git Flow provides a structured way to manage version control, 
especially for teams with frequent releases and versioning.




How to connect jenkins with kubernetes

create secret
kubectl create secret generic jenkins-token



create service account
kubectl create serviceaccount jenkins
 
Enable automountServiceAccountToken for the jenkins Service Account
kubectl patch serviceaccount jenkins -p '{"automountServiceAccountToken": true}'

Patch the jenkins-token Secret to Associate it with the jenkins Service Account
kubectl patch secret jenkins-token -p '{"metadata": {"annotations": {"kubernetes.io/service-account.name": "jenkins"}}}'


kubectl get secret jenkins-token -o yaml

copy the secret token

switch to jenkins
then switch credentials
add credentials
select secret text
then save it


install k8s plugin

Manage Jenkins - Cloud

Name: Kubernetes
KubernetesUrl: https://192.168.56.8:6443
Kubernetes namespace: default
Credentials: select the created credntials which has service account token
Use Pod Label to identify it


Other option
------------
Use kubeconfig file

kubectl config use-context
kubectl config --kubeconfig=/root/my-kube-config use-context research
kubectl config --kubeconfig=/root/my-kube-config current-context



A stateless app does not retain any client session or data between requests, 
while a stateful app maintains client-specific data or session information across multiple interactions






How to connect S3 bucket in eks cluster

s3 csi driver
service account with iam role
mount utility inside of pod







