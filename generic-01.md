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

1. **Developer commits code to GitHub**  
   A developer commits their changes to a GitHub repository.

2. **Jenkins pulls code from GitHub**  
   Jenkins is integrated with GitHub and automatically pulls the latest code upon each commit.

3. **Maven builds the WAR file**  
   Jenkins triggers Maven to build the WAR (Web Application Archive) file from the source code.

4. **SonarQube scan**  
   The WAR file is scanned by SonarQube to assess code quality and security vulnerabilities.

5. **Push WAR to Nexus Artifactory**  
   Once the SonarQube scan passes, the WAR file is pushed to Nexus Artifactory using a `curl` command.

6. **Download WAR from Nexus**  
   A `curl` download command retrieves the WAR file from the Nexus repository.

7. **Create Docker image**  
   A Docker image is created from the `Dockerfile`, and the downloaded WAR file is added to the Docker image.

8. **Anchor scan on Docker image**  
   An anchor scanning utility scans the Docker image for vulnerabilities, ensuring its integrity before moving forward.

9. **Push Docker image to ECR**  
   After the scan passes, the Docker image is pushed to the AWS Elastic Container Registry (ECR) repository.

10. **Ansible pulls Docker image from ECR**  
    Ansible pulls the latest Docker image from the ECR repository.

11. **Update Kubernetes deployment config**  
    A `sed` command is used to inject the latest Docker image name into the Kubernetes deployment configuration file.

12. **Deploy to Kubernetes**  
    Ansible deploys the updated Kubernetes deployment configuration to the Kubernetes cluster.

13. **Smoke test via curl**  
    A smoke test is conducted using `curl` to validate the deployment of the application in the Kubernetes cluster.

## Scaling Down Traffic for Compliance
To increase compliant numbers, scale down non-essential APIs (no traffic APIs) based on respective CRs (Compliance Rules) to optimize the system and improve performance.




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







