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
| **Feature Branching**      | Each feature is developed in a separate branch and merged after completion. Promotes isolation and easier code reviews. | Projects that require isolated development and 



## DevOps CI/CD Workflow

## Continuous Integration and Deployment Process for springboot based microservice api jar 
-----------------------

| **Step**                                   | **Description**                                                                                                                                      |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Versioning and Branching Strategy**      | **Git Tagging**: Used for versioning the application in GitHub. <br> **Development Branch**: The `develop` branch is used for the **dev environment**.<br> **Release Branch**: If tests are successful, a pull request is raised for the `release/1.0` branch. <br> **Multi-Branch Pipeline**: Jenkins **multi-branch pipeline** is used to handle different environments. The `develop` branch manages **dev**, while `release/1.0` is used for **staging/production**. The CI process includes building the JAR file, scanning it, storing it as an artifact, running multiple test cases, building the Docker image, scan the image and push it to ecr. |
| **1. Developer Commits Code to Develop Branch** | The developer commits code changes to the **`develop`** branch in the GitHub repository. This branch is dedicated to the **dev environment** and serves as the main branch for ongoing development. |
| **2. Jenkins Pulls Code from GitHub**      | Jenkins is integrated with GitHub to automatically pull the latest code after each commit via webhook integration, enabling a zero-click process for continuous integration. |
| **3. Run Gradle Build**                    | Jenkins runs `./gradlew build` to compile the code, build the microservice API JAR file, and install the dependencies specified in the `build.gradle` file. |
| **4. Run Unit Tests with JUnit**           | Jenkins triggers **JUnit** to execute unit tests and ensure the correctness of the microservice code.                                                  |
| **5. SonarQube Scan**                      | **SonarQube** is used to analyze the code for quality, maintainability, and security vulnerabilities.                                                  |
| **6. Build Spring Boot JAR**               | Jenkins uses **Gradle** to build the Spring Boot microservice into a JAR file, typically with `./gradlew build` or `./gradlew bootJar`.                 |
| **7. Push App to Nexus Artifactory**       | Once the tests pass, the JAR file is pushed to Nexus Artifactory using `curl` or similar tools to store the build artifacts.                           |
| **8. Create Docker Image**                 | A Docker image is created based on the `Dockerfile`, which includes the Spring Boot JAR file and the required environment configurations.               |
| **9. Trivy Scan on Docker Image**          | The Docker image is scanned using **Trivy** to check for security vulnerabilities.                                                                   |
| **10. Push Docker Image to ECR**           | After passing the scan, the Docker image is pushed to AWS Elastic Container Registry (ECR).                                                           |
| **Continuous Deployment (CD)**            |                                                                                                                                                      |
| **1. Application Name, Version, Docker Image Version** | Jenkins uses parameters for application name, version, and Docker image version to proceed with the deployment.                                           |
| **2. Helm Deployment**                     | Helm deploys the Spring Boot microservice application to the target environment (e.g., dev, staging, or production) once the deployment parameters are set. |









# Continuous Integration and Deployment Process for Node.js Microservice App



| **Step**                                   | **Description**                                                                                                                                      |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Versioning and Branching Strategy**      | **Git Tagging**: Used for versioning the application. <br> **Development Branch**: The `develop` branch is used for the **dev environment**.<br> **Release Branch**: If tests are successful, a pull request is raised for the `release/1.0` branch. <br> **Multi-Branch Pipeline**: We use Jenkins  **multi-branch pipeline** to handle different environments. The `develop` branch handles **dev**, while `release/1.0` is used for **staging/production** continuous integration process which include build jar,scan jar,store jar as artifact , run multiple test cases ,build docker image. |
| **1. Developer Commits Code to Develop Branch**    | The developer commits code changes to the **`develop`** branch in the GitHub repository. This branch is responsible for the **dev environment** and serves as the primary branch for ongoing development.                                                                                             |
| **2. Jenkins Pulls Code from GitHub**      | Jenkins is integrated with GitHub to automatically pull the latest code after each commit as per the webhook integration, following a zero-click process for continuous integration. |
| **3. Run npm install**                     | Jenkins runs `npm install` to install the dependencies from `package.json`.                                                                         |
| **4. Run Unit Tests with Jest**            | Jenkins triggers **Jest** to run unit tests and verify the correctness of the code.                                                                  |
| **5. SonarQube Scan**                      | **SonarQube** is used to analyze the code for quality and security vulnerabilities.                                                                |
| **6. Push App to Nexus Artifactory**       | Once tests pass, the application artifacts (if needed) are pushed to Nexus Artifactory using `curl` or similar tools.                             |
| **7. Create Docker Image**                 | Docker image is created based on the `Dockerfile`, with the application files added.                                                                |
| **8. Trivy Scan on Docker Image**          | Docker image is scanned using **Trivy** for security vulnerabilities.                                                                               |
| **9. Push Docker Image to ECR**            | After the scan passes, the Docker image is pushed to AWS Elastic Container Registry (ECR).                                                           |
| **Continuous Deployment (CD)**            |                                                                                                                                                      |
| **1. Application Name, Version, Docker Image Version** | Jenkins parameters for application name, version, and Docker image version are set to complete the deployment.                                           |
| **2. Helm Deployment**                     | Helm deploys the Node.js application to the target environment in the background once the deployment parameters are provided.                         |

                     
# Continuous Integration and Deployment Process for flask based microservice api
-----------------------------------------------------------------------------------------

| **Step**                                   | **Description**                                                                                                                                      |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Versioning and Branching Strategy**      | **Git Tagging**: Used for versioning the application. <br> **Development Branch**: The `develop` branch is used for the **dev environment**.<br> **Release Branch**: If tests are successful, a pull request is raised for the `release/1.0` branch. <br> **Multi-Branch Pipeline**: We use Jenkins  **multi-branch pipeline** to handle different environments. The `develop` branch handles **dev**, while `release/1.0` is used for **staging/production** continuous integration process which include build jar,scan jar,store jar as artifact , run multiple test cases ,build docker image. |
| **1. Developer Commits Code to Develop Branch**    | The developer commits code changes to the **`develop`** branch in the GitHub repository. This branch is responsible for the **dev environment** and serves as the primary branch for ongoing development.                                                                                             |
| **2. Jenkins Pulls Code from GitHub**      | Jenkins is integrated with GitHub to automatically pull the latest code after each commit as per the webhook integration, following a zero-click process for continuous integration. |
| **3. Create Virtual Environment**          | Jenkins creates a virtual environment for the Flask application using `python -m venv venv`. This isolates the dependencies for the Flask application. |
| **4. Install Dependencies**                | Jenkins runs `pip install -r requirements.txt` to install the necessary dependencies as defined in the `requirements.txt` file. |
| **5. Run Unit Tests with pytest**          | Jenkins triggers **pytest** to run unit tests and verify the correctness of the Flask API code.                                                      |
| **6. SonarQube Scan**                      | **SonarQube** is used to analyze the Python code for quality, maintainability, and security vulnerabilities.                                           |
| **7. Build the Flask App**                 | The Flask application is built and prepared for deployment. This may include any necessary environment setup or pre-deployment tasks.                 |
| **8. Create Docker Image**                 | Docker image is created based on the `Dockerfile`, which includes the Flask application, dependencies, and environment configurations.               |
| **9. Trivy Scan on Docker Image**          | Docker image is scanned using **Trivy** for security vulnerabilities.                                                                               |
| **10. Push Docker Image to ECR**           | After the scan passes, the Docker image is pushed to AWS Elastic Container Registry (ECR).                                                           |
| **Continuous Deployment (CD)**            |                                                                                                                                                      |
| **1. Application Name, Version, Docker Image Version** | Jenkins parameters for application name, version, and Docker image version are set to complete the deployment.                                           |
| **2. Helm Deployment**                     | Helm deploys the Flask microservice application to the target environment (e.g., dev, staging, or production) once the deployment parameters are provided.     

                   




| **Stage**               | **Step**                                                                                  | **Explanation**                                                                                                                                                                         |
|--------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Validate**             | `cd ${TERRAFORM_PATH}`                                                                   | Navigates to the Terraform deployment directory.                                                                                                                                       |
|                          | `terraform init -backend-config=backend.tfvars`                                         | Initializes Terraform with the backend configuration file to set up remote state storage.                                                                                              |
|                          | `terraform validate`                                                                    | Validates the Terraform configuration files for syntax and best practices.                                                                                                             |
|                          | `terraform fmt`                                                                         | Formats the Terraform files to ensure consistency in coding style.                                                                                                                     |
|                          | `terraform workspace select dev \|\| terraform workspace new dev`                       | Switches to the `dev` workspace or creates it if it doesn't exist.                                                                                                                     |
|                          | `tflint --var-file=dev.tfvars`                                                          | Runs `tflint` (a linter for Terraform) to check for configuration errors based on variables in `dev.tfvars`.                                                                            |
| **Terraform Action**     | `cd ${TERRAFORM_PATH}`                                                                   | Navigates to the Terraform deployment directory again.                                                                                                                                 |
|                          | `terraform init -backend-config=backend.tfvars`                                         | Re-initializes Terraform to ensure the backend is properly configured for this stage.                                                                                                  |
|                          | `terraform workspace select dev`                                                        | Ensures the `dev` workspace is active.                                                                                                                                                 |
|                          | `terraform plan -var-file=dev.tfvars -out=devtfplan -input=false -lock=false`            | Generates a Terraform execution plan (`devtfplan`) using variables from `dev.tfvars`, without user input or locking the state file.                                                    |
|                          | `terraform apply -var-file=dev.tfvars -auto-approve`                                    | (Commented out) Automatically applies the Terraform plan to create or update resources.                                                                                                |
|                          | `terraform destroy -var-file=dev.tfvars -input=false -auto-approve`                     | (Commented out) Automatically destroys all resources defined in the Terraform configuration.                                                                                           |
|                          | `aws eks wait cluster-active --region ${REGION} --name ${CLUSTER_NAME}`                 | Waits until the EKS cluster is in an active state.                                                                                                                                     |
|                          | `NODE_GROUP_NAME=$(aws eks list-nodegroups --region ${REGION} --cluster-name ${CLUSTER_NAME} --query 'nodegroups[0]' --output text)` | Retrieves the name of the first node group in the EKS cluster using AWS CLI.                                                                                                          |
|                          | `aws eks wait nodegroup-active --region ${REGION} --cluster-name ${CLUSTER_NAME} --nodegroup-name $NODE_GROUP_NAME` | Waits until the retrieved node group is active, ensuring the cluster is ready for deployment.                                                                                          |
|                          | `echo "EKS cluster is active."`                                                          | Prints a confirmation message when the EKS cluster is active.                                                                                                                          |
|                          | `echo "EKS node group $NODE_GROUP_NAME is active."`                                      | Prints a confirmation message when the EKS node group is active.                                                                                                                       |




```

stage('App Deploy') {
            steps {
                script {
                    sh '''
                    cd ${APP_DEPLOY_PATH}
                    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook \
                        -i ${APP_DEPLOY_PATH}/aws_ec2.yml \
                        ${APP_DEPLOY_PATH}/copy.yml \
                        -e "nodes=tag_Name_eks_bastion_node user=ec2-user ansible_ssh_private_key_file=/var/lib/jenkins/ag-key-us-east-1.pem"
                    
                   ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook \
                                -i ${APP_DEPLOY_PATH}/aws_ec2.yml \
                                   ${APP_DEPLOY_PATH}/app_deploy.yml \
                                -e "nodes=tag_Name_eks_bastion_node user=ec2-user ansible_ssh_private_key_file=/var/lib/jenkins/ag-key-us-east-1.pem \
                                   image_repository=891377203384.dkr.ecr.us-east-1.amazonaws.com/ag-py image_tag=${BUILD_NUMBER}"
                    '''
                }
            }
        }
    }

```


```

- hosts: "{{ nodes }}"
  remote_user: "{{ user }}"
  tasks:

    - name: Check if Helm Diff plugin is installed
      command: helm plugin list
      register: helm_plugin_list
      failed_when: false

    - name: Install Helm Diff plugin if not already installed
      shell: helm plugin install https://github.com/databus23/helm-diff
      when: "'diff' not in helm_plugin_list.stdout"

    - name: Run AWS STS get-caller-identity
      shell: aws sts get-caller-identity
      register: sts

    - name: Debug sts output
      debug:
        var: sts.stdout

    - name: Update kubeconfig for EKS
      shell: aws eks update-kubeconfig --name plato-sit-cluster --region us-east-1
      register: eks_update

    - name: Debug eks_update output
      debug:
        var: eks_update.stdout

    - name: Get contexts
      shell: kubectl config get-contexts

    - name: Set context
      shell: |
        kubectl config set-context cluster1 \
          --cluster=arn:aws:eks:us-east-1:891377203384:cluster/plato-sit-cluster \
          --user=arn:aws:eks:us-east-1:891377203384:cluster/plato-sit-cluster \
          --namespace=default

    - name: Execute Helmfile to deploy app
      shell: helmfile --environment cluster1 apply --set image.repository={{ image_repository }} --set image.tag={{ image_tag }}
      args:
        chdir: /tmp/app-deploy/app-deploy/helm-chart

    - name: Get pod status
      shell: kubectl get pods
      register: kubectl_pod_output

    - name: Debug kubectl pod output
      debug:
         var: kubectl_pod_output.stdout_lines


```
































## Git Flow Branching Model

| Branch Type         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Master**          | Holds production-ready code.                                                 |
| **Develop**         | The main integration branch where features are merged.                       |
| **Feature Branches**| Created from develop to work on new features and merged back into develop.  |
| **Release Branches**| Created from develop when preparing for a new release, used for final testing and bug fixes. |
| **Hotfix Branches** | Created from master to quickly fix issues in production, then merged into both master and develop. |

### Overview
Git Flow provides a structured way to manage version control, especially for teams with frequent releases and versioning.

```

cd $WORKSPACE/properties && mvn clean package -f pom.xml && /
mvn install sonar:sonar -Dsonar.login=sqp_293beeee09048bf228799ea36209901a06c3d62d -f pom.xml




docker run --rm \
    -v /var/lib/jenkins/workspace/sonar-scan/ag-ui:/app \
    -v /var/lib/jenkins/sonar-scanner:/sonar-scanner \
    -v /var/lib/jenkins/workspace/sonar-scan/ag-ui/.git:/app/.git \
    -w /app \
    node:18 bash -c '\
        npm install && \
        npm install --include=optional sharp && \
        npm install --save-dev nyc mocha mocha-junit-reporter && \
        npm install input-otp @radix-ui/react-tabs @radix-ui/react-toast react-hot-toast react-cookie react-icons embla-carousel-autoplay embla-carousel-react @radix-ui/react-dropdown-menu @radix-ui/react-radio-group @radix-ui/react-navigation-menu @radix-ui/react-avatar @radix-ui/react-switch && \
        npm run build --silent && \
        npm run test -- --reporter mocha-junit-reporter && \
        /sonar-scanner/bin/sonar-scanner \
            -Dsonar.projectKey=sample-nodejs-app \
            -Dsonar.sources=/app/src \
            -Dsonar.projectVersion=1.0-SNAPSHOT \
            -Dsonar.sourceEncoding=UTF-8 \
            -Dsonar.host.url=http://sonar-alb-1260171519.ap-south-1.elb.amazonaws.com \
            -Dsonar.token=sqa_91429eb52f70449ab64276bf89a3296a8604d2c5 \
            -Dsonar.exclusions=/node_modules/,/build/,/dist/,/.git/ \
            -Dsonar.nodejs.executable=/usr/local/bin/node \
            -Dsonar.junit.reportPaths=coverage/test-report.xml \
            -Dsonar.coverage.jacoco.xmlReportPaths=coverage/cobertura-coverage.xml'


            
```

# Differences Between SLI, SLA, and SLO

| **Aspect**          | **SLI (Service Level Indicator)**                                            | **SLO (Service Level Objective)**                                           | **SLA (Service Level Agreement)**                                             |
|----------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Definition**       | A quantitative measure of a service's performance (e.g., latency, uptime). | A target or goal for SLIs, defining acceptable service performance levels.  | A formal contract between provider and customer, outlining service expectations. |
| **Purpose**          | Provides metrics to monitor and measure service health.                   | Sets thresholds to ensure service reliability.                              | Ensures accountability and outlines penalties for unmet commitments.           |
| **Scope**            | Focuses on metrics like availability, latency, and throughput.            | Focuses on defining acceptable ranges for SLIs.                             | Focuses on business terms, including remedies and compensations.               |
| **Audience**         | Used by engineers and operations teams for monitoring.                    | Used by internal teams to align on performance goals.                       | Used by both customers and providers to agree on service expectations.         |
| **Binding Nature**   | Non-binding, used for internal tracking.                                  | Non-binding, serves as an internal performance guideline.                   | Legally binding, with enforceable terms and conditions.                        |



| **Term**                | **Description**                                                                                                                                  | **Use Case**                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Service Level Objective (SLO)** | A target level of reliability for a service, often defined as a percentage of uptime or other performance metrics.                                       | Use to define acceptable reliability targets for a service, ensuring the team meets user expectations.               |
| **Service Level Indicator (SLI)** | A metric that measures the reliability of a service, used to track whether the service meets the SLO.                                                      | Use to track metrics like response time, error rate, and availability to evaluate if the service is meeting SLOs.    |
| **Error Budget**        | The amount of downtime or errors that are allowed within the context of the SLO, typically used to balance reliability and feature velocity.        | Use to guide decision-making on how much risk can be taken with deploying new features while staying within SLOs.    |
| **Blameless Postmortem** | A report created after an incident, focusing on what happened, how it can be prevented in the future, and how to improve systems, without assigning blame. | Use to analyze incidents for learning opportunities and to improve system reliability without finger-pointing.       |
| **Incident Management** | The process of detecting, responding to, and resolving incidents that affect the availability, reliability, or performance of a service.           | Use to quickly identify, escalate, and resolve issues, minimizing downtime and impact on users.                     |
| **Availability**        | The proportion of time a system or service is operational and functioning as intended, often expressed as a percentage (e.g., 99.99% uptime).        | Use to measure the operational performance of a system or service to ensure it is available for users.              |
| **Latency**             | The time it takes for a system to respond to a request, typically measured in milliseconds or seconds.                                              | Use to monitor and reduce the time it takes for a user request to be processed by a service.                        |
| **Chaos Engineering**   | The practice of intentionally injecting failures or disruptions into a system to identify weaknesses and improve reliability under stress.            | Use to proactively test how systems respond to failures, improving resilience to unexpected incidents.               |
| **Capacity Planning**   | The process of determining the necessary resources (compute, storage, etc.) needed to support anticipated system load and growth.                   | Use to ensure that systems have enough capacity to handle expected traffic and to plan for future growth.            |
| **Runbook**             | A set of documented procedures for managing and responding to routine operations and incidents.                                                   | Use to provide clear, standardized steps for handling common tasks or incidents, ensuring consistency in responses.  |


| **Term**                | **Description**                                                                                                                                  | **Use Case**                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **CI/CD**               | Continuous Integration/Continuous Deployment. A set of practices to automate the process of code integration and deployment.                      | Use to automate code testing, building, and deployment, ensuring faster and reliable software releases.              |
| **Version Control**     | A system that tracks changes to files over time, allowing multiple team members to work on the same project simultaneously.                        | Use tools like Git to manage source code versions, track changes, and collaborate effectively.                       |
| **Microservices**       | An architectural style that structures an application as a collection of loosely coupled services that are independently deployable.               | Use to build scalable applications by breaking down monolithic code into smaller, manageable services.              |
| **Containerization**    | The process of packaging applications and their dependencies into containers for consistent deployment across environments.                        | Use Docker to create containers for development, testing, and production environments to ensure portability.          |
| **Infrastructure as Code (IaC)** | The practice of managing and provisioning infrastructure through code rather than manual configuration.                                            | Use tools like Terraform, Ansible, or CloudFormation to automate infrastructure provisioning.                        |
| **Orchestration**       | The automation of managing and coordinating multiple containers or services, typically using tools like Kubernetes.                                 | Use Kubernetes to manage containerized applications across clusters and handle tasks like scaling and load balancing. |
| **Monitoring**          | The process of tracking and observing the health and performance of systems, applications, and infrastructure in real-time.                        | Use tools like Prometheus or Grafana to monitor application performance and server health in production environments.  |
| **Logging**             | The practice of collecting and storing log data to track system events, errors, and application performance for debugging and analysis.             | Use ELK Stack (Elasticsearch, Logstash, Kibana) or Splunk to collect and analyze logs.                               |
| **Continuous Testing**  | The practice of continuously testing the software during the development lifecycle to identify issues early.                                          | Use automated testing frameworks like Selenium, Jest, or JUnit to test code continuously in the CI/CD pipeline.      |
| **DevOps Pipeline**     | A set of automated processes and tools that allow developers to compile, build, test, and deploy code quickly and efficiently.                      | Use Jenkins, GitLab CI, or CircleCI to create pipelines that automate the steps from development to deployment.       |



DevOps vs SRE
----------------


| **Attribute**                               | **DevOps**                                                 | **SRE (Site Reliability Engineering)**                           |
|---------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------|
| **Ownership & Oversight**                   | DevOps teams can have ownership and oversight over a number of tools and platforms. | Focus on system health and operational reliability.                |
| **Automation Focus**                        | DevOps is focused on automating deployment, redundancy, and manual tasks to ensure system uptime. | SRE focuses on automating operational processes to maintain system reliability. |
| **Role of Engineers**                       | DevOps Engineers are ops-focused engineers who solve development pipeline problems. | SRE Engineers are development-focused engineers who solve operational, scaling, and reliability problems. |
| **Objective**                               | Increase software delivery velocity, improve service reliability, and build shared ownership among software stakeholders. | Outcome of combining system operations responsibilities with software development and engineering. |



1. Containerization and Orchestration
2. CI/CD Pipeline Implementation
3. Logging and Monitoring Implementation
4. Security and Compliance Integration
5. Scalability and Performance Optimization
6. Configuration Management Implementation
7. Capacity Planning and Resource Management
8. Infrastructure as Code (IaC) Development

 


