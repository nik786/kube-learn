
Successfully Built and Deployed a Scalable E-Commerce Application on AWS EKS 🌐
# E-commerce Application Project Overview

| **Category**                       | **Details**                                                                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Application Overview**            |                                                                                                                                                                            |
| Frontend                            | Built with React for a dynamic and responsive UI.                                                                                                                          |
| Backend                             | Node.js + Express handling API requests.                                                                                                                                   |
| Databases                           | 1. **MongoDB**: Stores product data and manages the shopping cart. <br> 2. **MySQL**: Handles user authentication and payment information.                                  |
| **Containerization & Deployment**   |                                                                                                                                                                            |
| Dockerization                       | Dockerized both frontend and backend components.                                                                                                                           |
| Docker Images                       | Pushed Docker images to AWS ECR.                                                                                                                                           |
| EKS Cluster                         | Created an Amazon EKS cluster with node groups to orchestrate container deployment.                                                                                        |
| Load Balancing                      | Exposed the application through AWS ALB Ingress Controller for load balancing and scaling.                                                                                |
| Security                            | Secured the app with SSL certificates via AWS Certificate Manager (ACM).                                                                                                 |
| DNS Configuration                   | Set up DNS records for a seamless user experience on [https://lnkd.in/gVSaz4_6](https://lnkd.in/gVSaz4_6).                                                                 |
| **CI/CD Automation with Jenkins**   |                                                                                                                                                                            |
| Jenkins Pipeline                    | Automated the end-to-end pipeline with Jenkins: Cloned source code, built Docker images, and pushed to ECR.                                                                 |
| Deployment                          | Deployed new images to EKS and dynamically updated deployment-service.yaml with the latest image tags.                                                                    |
| Email Notifications                 | Configured email notifications for Jenkins job success or failure.                                                                                                        |
| **Code Quality & Security**         |                                                                                                                                                                            |
| Code Quality                        | Integrated SonarQube to ensure code quality and maintainability.                                                                                                           |
| Vulnerability Scanning              | Scanned Docker images with Trivy to catch vulnerabilities.                                                                                                                |
| Secrets Management                  | Managed sensitive information with Kubernetes secrets, encoding secrets in base64 for secure environment variable handling.                                                 |
| **Tech Stack & Tools**              |                                                                                                                                                                            |
| Frontend                            | React                                                                                                                                                                      |
| Backend                             | Node.js + Express                                                                                                                                                          |
| Databases                           | MongoDB and MySQL                                                                                                                                                          |
| AWS Services                        | EKS, ECR, ALB Ingress Controller, ACM, Route 53                                                                                                                             |
| CI/CD                               | Jenkins, SonarQube, Trivy for quality and security checks                                                                                                                  |
| **Summary**                         | This project was an incredible opportunity to deepen my skills in AWS, Kubernetes, DevOps automation, and security best practices.                                          |



https://github.com/Madeep9347/ecommerce-three-tier

https://github.com/Madeep9347/ecommerce-three-tier-kubernets-manifest-files
