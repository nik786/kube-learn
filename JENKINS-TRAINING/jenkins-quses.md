
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
#!/bin/bash

# Generate plugin.txt via Script Console API
curl -u <username>:<password_or_token> -X POST \
    -d 'script=def pluginFile = new File("/var/lib/jenkins/plugin.txt"); Jenkins.instance.pluginManager.plugins.each { plugin -> pluginFile.append("${plugin.getShortName()}\n"); } println("Generated plugin list")' \
    http://<jenkins-url>/scriptText

# Update plugins using Jenkins CLI
--------------------------------------
java -jar jenkins-cli.jar -s http://<jenkins-url> -auth <username>:<password_or_token> install-plugin -restart -file /var/lib/jenkins/plugin.txt

```


## A Jenkins executor is one of the basic building blocks which allow a build to run on a node/agent (e.g. build server). Think of an executor as a single “process ID”, or as the basic unit of resource that Jenkins executes on your machine to run a build.


## A good value to start with would be the number of CPU cores on the machine.". But of course, depends on environment like RAM, tmp space amount, etc.. We have 8 cores, but only 5 executors at master node.

```
curl.exe -sO http://192.168.56.8:8080/jnlpJars/agent.jar <br></br>
java -jar agent.jar -url http://192.168.56.8:8080/ -secret 087a0161713fc40823f172620061c996ce1c5e2b3feb9ad517a5e05e698be30b -name ec2 -webSocket -workDir "/var/lib/jenkins"



curl -sO http://192.168.56.8:8080/jnlpJars/agent.jar <br></br>
java -jar agent.jar -url http://192.168.56.8:8080/ -secret 087a0161713fc40823f172620061c996ce1c5e2b3feb9ad517a5e05e698be30b -name ec2 -webSocket -workDir "/var/lib/jenkins"


echo 087a0161713fc40823f172620061c996ce1c5e2b3feb9ad517a5e05e698be30b > secret-file <br></br>
curl -sO http://192.168.56.8:8080/jnlpJars/agent.jar <br></br>
java -jar agent.jar -url http://192.168.56.8:8080/ -secret @secret-file -name ec2 -webSocket -workDir "/var/lib/jenkins"

```





| Feature    | Replay                                                                 | Retrigger                                     |
|------------|------------------------------------------------------------------------|----------------------------------------------|
| Definition | Reruns a pipeline with the option to edit the Groovy script before execution. | Reruns the pipeline with the same configuration as the original build. |
| Use Case   | Useful for testing or modifying pipeline logic without committing changes. | Useful for re-executing an identical build without modifications. |











                 



# Blue-Green Deployment Jenkins Pipeline
-----------------------------------------

| **Step**                         | **Description**                                                                                         | **Jenkins Implementation**                                                                                      |
|----------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **1. Configure Jenkins**         | Set up a Jenkins pipeline for Blue-Green deployment.                                                    | Create a Jenkinsfile with stages for building, testing, and deploying.                                          |
| **2. Build and Test Application**| Build the application and perform tests to ensure quality.                                              | Use pipeline steps to build the app (e.g., Docker) and run tests.                                               |
| **3. Deploy to Green Environment** | Deploy the new version to the Green environment in the EKS cluster.                                     | Use `kubectl` or Helm commands in Jenkins to deploy to the Green environment: <br> `kubectl apply -f green-deployment.yaml`  |
| **4. Smoke Testing**             | Perform smoke tests on the Green environment to ensure the application is running correctly.            | Trigger test scripts or monitoring tools using Jenkins pipeline stages.                                         |
| **5. Switch Traffic**            | Update the service to route traffic from Blue (current) to Green (new) by modifying Kubernetes services.| Use Jenkins to execute a `kubectl` command to update the Kubernetes service selector to point to Green pods: <br> `kubectl set selector service <service-name> app=green` |
| **6. Monitor the Deployment**    | Continuously monitor the application for errors or performance issues after switching traffic.          | Integrate monitoring tools (e.g., Prometheus, Grafana) and alert if any issues arise.                           |
| **7. Rollback if Needed**        | Revert to the Blue environment if issues are detected in the Green environment.                        | Use a Jenkins stage to revert the Kubernetes service selector to Blue pods if required: <br> `kubectl set selector service <service-name> app=blue` |
| **8. Clean Up**                  | Remove unused resources (e.g., old Blue pods) after successful deployment.                             | Automate cleanup tasks using a Jenkins pipeline stage: <br> `kubectl delete pods -l app=blue`                   |




- Role-based Authorization Strategy

manage/role-strategy/

manage and assign roles


## Token Generation for webhook

Jenkins - Manage Jenkins - Users - nik - configure - generate api token

## Jenkins job

GitHub hook trigger for GITScm polling


Payload URL * http://<jenkins_server>/github-webhook/

Content type *

Secret







```

pipeline {
    agent any

    environment {
        git_url = "git@github.com:ardhangini32/ag-app.git"
        sshKey = credentials('ag-git-01')
        AWS_REGION = 'ap-south-1'
        ECR_REPO_URI = '891377203384.dkr.ecr.ap-south-1.amazonaws.com'
        DOCKERFILE_PATH = "${WORKSPACE}/${params.app}"
        fullTag = "${BUILD_NUMBER}" // Declare fullTag as a global variable
    }

    parameters {
        choice(name: 'git_branches', choices: ['ag-dev', 'release/1.0'], description: 'Branch to build')
        choice(name: 'dockerfile', choices: ['devagdockerfile', 'prodagdockerfile'], description: 'Dockerfile to use')
        choice(name: 'image_names', choices: ['ag-repo', 'ag-dev-repo'], description: 'Docker image name')
        choice(name: 'app_path', choices: ['dev', 'prod'], description: 'folder path')
        string(name: 'app', defaultValue: 'ag-be', description: 'App folder name')
        choice(name: 'stack_name', choices: ['ag-ecs-service-stack-dev', 'ag-ecs-service-stack-prod'], description: 'cf name')
        choice(name: 'action', choices: ['create-stack', 'update-stack'], description: 'cf action')
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', 
                        branches: [[name: params.git_branches]],
                        doGenerateSubmoduleConfigurations: false, 
                        extensions: [], 
                        submoduleCfg: [], 
                        userRemoteConfigs: [[credentialsId: 'ag-git-01', url: git_url]]
                    ])
                }
            }
        }

        stage('Login to AWS ECR') {
            steps {
                script {
                    sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO_URI}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${params.image_names}:${fullTag} -f ${DOCKERFILE_PATH}/${params.dockerfile} ${DOCKERFILE_PATH}"
                }
            }
        }

        stage('Tag Docker Image') {
            steps {
                script {
                    sh "docker tag ${params.image_names}:${fullTag} ${ECR_REPO_URI}/${params.image_names}:${fullTag}"
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    sh "docker push ${ECR_REPO_URI}/${params.image_names}:${fullTag}"
                }
            }
        }

        stage('Deploy to ECS') {
            steps {
                script {
                    // Update the CloudFormation parameter with the new image tag
                    sh """
                    sed -i '/\"ParameterKey\": \"Image\"/!b;n;s|\"ParameterValue\": \".*\"|\"ParameterValue\": \"${ECR_REPO_URI}/${params.image_names}:${fullTag}\"|' $WORKSPACE/infrastructure/templates/${params.app_path}/ag-app-parameter.json
                    """
                    // Deploy CloudFormation stack
                    sh """
                    aws cloudformation ${params.action} --stack-name ${params.stack_name} --template-body file://$WORKSPACE/infrastructure/templates/${params.app_path}/ag-app-cf.yaml --parameters file://$WORKSPACE/infrastructure/templates/${params.app_path}/ag-app-parameter.json --capabilities CAPABILITY_NAMED_IAM
                    """
                }
            }
        }
    }
}

```




