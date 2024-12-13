
Simple syntax
---------------
```
pipeline {
  agent any 
  stages {
    stage('Build') {
      steps{
         // build description
       }
}
     stage('Test') {
      steps {
        // run tests
         }
      }
    stage('Deploy') {
     steps {
       // deploy
    
      }
}
}
}
```

syntax with docker agent
--------------------------
```
pipeline {
  agent {docker { image 'node:14-alpine'}} 
  stages {
    stage('Build') {
      steps{
         // build description
       }
}
     stage('Test') {
      steps {
        // run tests
         }
      }
    stage('Deploy') {
     steps {
       // deploy
    
      }
}
}
}
```


syntax with parallel
----------------------
```
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        // build description
      }
    }
    stage('Test & Deploy') {
      parallel {
        stage('Test') {
          steps {
            // run tests
          }
        }
        stage('Deploy') {
          steps {
            // deploy
          }
        }
      }
    }
  }
}
```

syntax with when
------------------

```
pipeline {
    agent any
    parameters {
        choice(name: 'STAGES_TO_RUN', choices: ['Stage1', 'Stage2', 'Stage3', 'Stage4', 'Stage5', 'Stage6', 'Stage7', 'Stage8', 'Stage9', 'Stage10'], description: 'Select stages to run', multipleChoice: true)
    }
    stages {
        stage('Stage 1') {
            when {
                expression { 'Stage1' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 1'
            }
        }
        stage('Stage 2') {
            when {
                expression { 'Stage2' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 2'
            }
        }
        stage('Stage 3') {
            when {
                expression { 'Stage3' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 3'
            }
        }
        stage('Stage 4') {
            when {
                expression { 'Stage4' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 4'
            }
        }
        stage('Stage 5') {
            when {
                expression { 'Stage5' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 5'
            }
        }
        stage('Stage 6') {
            when {
                expression { 'Stage6' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 6'
            }
        }
        stage('Stage 7') {
            when {
                expression { 'Stage7' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 7'
            }
        }
        stage('Stage 8') {
            when {
                expression { 'Stage8' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 8'
            }
        }
        stage('Stage 9') {
            when {
                expression { 'Stage9' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 9'
            }
        }
        stage('Stage 10') {
            when {
                expression { 'Stage10' in params.STAGES_TO_RUN }
            }
            steps {
                echo 'Running Stage 10'
            }
        }
    }
}

```


| **Aspect**                      | **Details**                                                                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Default Concurrency**          | Jenkins Default Executors: 2                                                                                                                                 |
| **Explanation**                  | Executors are worker threads that Jenkins uses to run builds. Each executor can handle one job at a time. The default is 2 executors.                       |
| **How to Modify**                | - Go to **Manage Jenkins > Manage Nodes and Clouds > Configure** for your node. <br> - Update the **# of executors** field to the desired value. <br> - Save the changes. |
| **Increase Concurrency**         | You can add Jenkins agents (nodes) to increase overall concurrency.                                                                                        |
| **Limit Concurrency Per Job**   | Plugins like **Throttle Concurrent Builds** or configuring a job to use a specific agent label can help control concurrency for individual jobs.            |

### Additional Notes
- The number of executors is set at the controller (master) level by default but can be adjusted based on system capacity.
- Increasing the number of agents improves overall concurrency by distributing the load.




| **Feature**                                | **Description**                                                                                                                                                              |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Automatic Branch Detection and Builds**  | The pipeline automatically detects new branches in the repository and creates corresponding jobs. This eliminates the need to manually configure jobs for each new branch.     |
| **Isolated Testing and Deployment**        | Each branch has its own pipeline, allowing for independent testing and deployment. This isolation reduces risks before merging changes into the main branch.                   |
| **Reduced Configuration Overhead**         | Jenkins automatically uses the configuration for each branch, reducing the overhead of maintaining separate pipeline jobs for each branch.                                   |
| **Enhanced Collaboration**                 | Developers can work on branches without affecting the main pipeline, allowing multiple team members to work concurrently on different features or fixes, boosting productivity. |
| **Efficient Resource Utilization**         | Multi-branch pipelines ensure that only active branches are built, tested, or deployed, saving resources by not processing inactive or obsolete branches.                       |
| **Streamlined CI/CD Workflow**             | Supports multiple development workflows (e.g., feature branches, hotfix branches, release branches), making the CI/CD process more flexible and efficient.                     |

### Benefits of Multi-Branch Pipelines in Jenkins
- **Enhanced Efficiency**: Facilitates Git branching strategies like Gitflow or feature-based branching.
- **Better Collaboration**: Allows teams to collaborate without affecting the main pipeline.
- **Improved Resource Management**: Only builds active branches, saving resources.



| **Aspect**                        | **Declarative Pipeline**                                                                                         | **Scripted Pipeline**                                                                                         |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Syntax**                         | Structured, fixed syntax (e.g., `pipeline { }`)                                                                   | Groovy-based, free-form (e.g., `node { }`)                                                                     |
| **Error Handling**                 | Built-in post blocks for success, failure, etc.                                                                   | Custom error handling with try-catch blocks                                                                    |
| **Parallel Syntax**                | Simple parallel syntax                                                                                           | Requires custom Groovy syntax                                                                                 |
| **Validation**                     | Built-in checks to prevent errors                                                                                 | No built-in validation in Jenkins UI                                                                          |
| **Stages and Steps**               | Requires blocks for each stage and step                                                                           | Freely allows Groovy code within pipeline                                                                     |
| **Flexibility**                    | More structured and opinionated                                                                                   | More flexible and allows more custom code                                                                      |


| **Aspect**                      | **Jenkins**                                        | **Jenkins X**                                      |
|----------------------------------|----------------------------------------------------|---------------------------------------------------|
| **Deployment**                   | Standalone server                                  | Kubernetes-native, built specifically for K8s      |
| **Platform Support**             | Supports various platforms                         | Kubernetes-only, leveraging cloud-native tools     |
| **Configuration**                | Job and pipeline-based                             | GitOps-based configuration                        |
| **Customization**                | Plugins for custom setups                          | Pre-integrated with Kubernetes, Helm, and GitOps  |




```

#!/bin/bash

# Define variables
JENKINS_URL="http://source-jenkins-server:8080"
REMOTE_JENKINS_URL="http://remote-jenkins-server:8080"
JENKINS_CLI_JAR="jenkins-cli.jar"
JENKINS_AUTH="--username admin --password yourpassword"  # Or use an API token
BACKUP_DIR="plugins_backup"
REMOTE_AUTH="--username remote_admin --password remote_password"

# Ensure the Jenkins CLI jar exists
if [ ! -f "$JENKINS_CLI_JAR" ]; then
    echo "Error: Jenkins CLI jar ($JENKINS_CLI_JAR) not found!"
    exit 1
fi

# Create a backup directory
mkdir -p "$BACKUP_DIR"

# Backup plugins from the source Jenkins server
plugins_list=$(java -jar "$JENKINS_CLI_JAR" -s "$JENKINS_URL" $JENKINS_AUTH list-plugins | awk '{print $1}')

if [ -z "$plugins_list" ]; then
    echo "Error: No plugins found or unable to connect to $JENKINS_URL"
    exit 1
fi

echo "Backing up plugins..."
for plugin in $plugins_list; do
    echo "Downloading plugin: $plugin"
    java -jar "$JENKINS_CLI_JAR" -s "$JENKINS_URL" $JENKINS_AUTH get-plugin "$plugin" > "$BACKUP_DIR/$plugin.hpi"
    if [ $? -ne 0 ]; then
        echo "Failed to download $plugin"
    fi
done

# Compress the backup directory
backup_file="plugins_backup_$(date +%Y%m%d%H%M%S).tar.gz"
tar -czf "$backup_file" -C "$BACKUP_DIR" .

echo "Plugins backed up to $backup_file"

# Restore plugins to the remote Jenkins server
echo "Restoring plugins to the remote server..."
for plugin_file in "$BACKUP_DIR"/*.hpi; do
    plugin_name=$(basename "$plugin_file" .hpi)
    echo "Uploading plugin: $plugin_name"
    java -jar "$JENKINS_CLI_JAR" -s "$REMOTE_JENKINS_URL" $REMOTE_AUTH install-plugin "$plugin_file"
    if [ $? -ne 0 ]; then
        echo "Failed to upload $plugin_name"
    fi
done

# Restart remote Jenkins server
echo "Restarting remote Jenkins server..."
java -jar "$JENKINS_CLI_JAR" -s "$REMOTE_JENKINS_URL" $REMOTE_AUTH safe-restart

# Clean up
rm -rf "$BACKUP_DIR"

echo "Backup and restore process completed."

```


```
Jenkins.instance.pluginManager.plugins.each { plugin ->
    println("${plugin.getShortName()} (${plugin.getVersion()})")
}

```

```
import jenkins.model.Jenkins

def updateCenter = Jenkins.instance.updateCenter
updateCenter.getUpdates().each { update ->
    println("Updating plugin: ${update.plugin.name} to version ${update.version}")
    update.deploy()
}

// Save Jenkins configuration to apply changes
Jenkins.instance.save()

println("Plugin updates initiated. Restart Jenkins to complete the process.")

```

```
java -jar jenkins-cli.jar -s http://<jenkins-url> install-plugin <plugin-name> --latest

```

```

def pluginFile = new File('/var/lib/jenkins/plugin.txt') // Adjust the path as needed
Jenkins.instance.pluginManager.plugins.each { plugin ->
    pluginFile.append("${plugin.getShortName()}:${plugin.getVersion()}\n")
}
println("Plugin list saved to plugin.txt")

```

```
java -jar jenkins-cli.jar -s http://<jenkins-url> -auth <username>:<password_or_token> install-plugin -restart -file plugin.txt


```

```
#!/bin/bash

# Generate plugin.txt via Script Console API
curl -u <username>:<password_or_token> -X POST \
    -d 'script=def pluginFile = new File("/var/lib/jenkins/plugin.txt"); Jenkins.instance.pluginManager.plugins.each { plugin -> pluginFile.append("${plugin.getShortName()}\n"); } println("Generated plugin list")' \
    http://<jenkins-url>/scriptText

# Update plugins using Jenkins CLI
java -jar jenkins-cli.jar -s http://<jenkins-url> -auth <username>:<password_or_token> install-plugin -restart -file /var/lib/jenkins/plugin.txt

```


## A Jenkins executor is one of the basic building blocks which allow a build to run on a node/agent (e.g. build server). Think of an executor as a single “process ID”,
   or as the basic unit of resource that Jenkins executes on your machine to run a build.


## A good value to start with would be the number of CPU cores on the machine.". But of course, depends on environment like RAM, tmp space amount, etc.. We have 8 cores, but only 5 executors at master node.


curl.exe -sO http://192.168.56.8:8080/jnlpJars/agent.jar
java -jar agent.jar -url http://192.168.56.8:8080/ -secret 087a0161713fc40823f172620061c996ce1c5e2b3feb9ad517a5e05e698be30b -name ec2 -webSocket -workDir "/var/lib/jenkins"



curl -sO http://192.168.56.8:8080/jnlpJars/agent.jar
java -jar agent.jar -url http://192.168.56.8:8080/ -secret 087a0161713fc40823f172620061c996ce1c5e2b3feb9ad517a5e05e698be30b -name ec2 -webSocket -workDir "/var/lib/jenkins"


echo 087a0161713fc40823f172620061c996ce1c5e2b3feb9ad517a5e05e698be30b > secret-file
curl -sO http://192.168.56.8:8080/jnlpJars/agent.jar
java -jar agent.jar -url http://192.168.56.8:8080/ -secret @secret-file -name ec2 -webSocket -workDir "/var/lib/jenkins"




---

# Active-Active Jenkins Architecture in AWS

| **Step** | **Description** |
|----------|-----------------|
| **1. Set Up a VPC** | Create a VPC with multiple Availability Zones (AZs) for fault tolerance. Set up public and private subnets. |
| **2. Launch Multiple Jenkins Master EC2 Instances** | Launch at least two EC2 instances in different AZs. Install Jenkins on them or use an AMI with Jenkins pre-installed. |
| **3. Set Up Application Load Balancer (ALB)** | Create an ALB to distribute traffic between Jenkins Masters. Set up health checks and configure SSL if needed. |
| **4. Set Up Shared Jenkins Home Directory** | Use Amazon EFS (Elastic File System) or S3 to store Jenkins' home directory, ensuring data consistency across masters. |
| **5. Set Up Amazon RDS for Jenkins Database** | Set up Amazon RDS (MySQL or PostgreSQL) with Multi-AZ deployment for high availability of Jenkins' database. |
| **6. Configure Jenkins Auto Scaling (for Jenkins Masters)** | Set up an Auto Scaling Group (ASG) for Jenkins Masters with scaling policies based on traffic or CPU utilization. |
| **7. Set Up Jenkins Agents (Optional, for Scalability)** | Set up Jenkins agents on EC2, ECS, or use spot instances to scale Jenkins builds based on demand. |
| **8. Configure Route 53 for DNS Management** | Set up Route 53 DNS records pointing to the ALB for consistent access to Jenkins. |
| **9. Backup and Disaster Recovery Setup** | Regularly back up EFS and RDS data. Use AWS Backup or custom solutions to back up Jenkins configurations and job data. |
| **10. Monitoring and Alerts** | Use CloudWatch to monitor Jenkins instances, RDS, ALB, and Auto Scaling. Set up alarms for critical metrics and send notifications via SNS. |

---

## Diagram of Active-Active Jenkins Architecture in AWS:





## Advantages of Active-Active Jenkins Architecture:
- **No Single Point of Failure:** Both Jenkins Masters are fully operational at all times, ensuring continuous availability.
- **Scalability:** Jenkins Masters and Agents scale horizontally based on demand, allowing you to handle a large number of simultaneous builds.
- **Fault Tolerance:** Multi-AZ setup for Jenkins Masters, ALB, and RDS ensures that if one AZ fails, the other can continue handling requests.
- **Load Balancing:** ALB distributes traffic evenly across Jenkins Masters to ensure optimal performance.
- **High Availability:** Amazon EFS and Multi-AZ RDS ensure that critical data is always available, even if one of the instances or AZs fails.









                    +-------------+
                    |  Route 53   |
                    | (DNS)       |
                    +-------------+
                          |
                          |
                   +--------------+
                   |  ALB (8080)  | <---> Jenkins Masters
                   +--------------+
                   /                \
         +----------------+    +------------------+
         | Jenkins Master |    | Jenkins Master   |
         |   EC2 (AZ 1)   |    |   EC2 (AZ 2)     |
         +----------------+    +------------------+
                   |                    |
             +-------------+    +-------------+
             |   EFS       |    |   RDS       |
             | (Shared     |    | (Database)  |
             | Home)       |    |             |
             +-------------+    +-------------+
                   |
         +----------------------+
         |    Jenkins Agents    |
         | (EC2 / ECS / Containers) |
         +----------------------+



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

