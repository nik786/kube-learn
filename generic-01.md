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




Master: Holds production-ready code.
Develop: The main integration branch where features are merged.
Feature branches: Created from develop to work on new features and merged back into develop.
Release branches: Created from develop when preparing for a new release, 
used for final testing and bug fixes.
Hotfix branches: Created from master to quickly fix issues in production, 
then merged into both master and develop.
Git Flow provides a structured way to manage version control, 
especially for teams with frequent releases and versioning.












