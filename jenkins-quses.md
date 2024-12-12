
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





