
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


The default concurrency in Jenkins depends on the number of executors configured for the Jenkins instance. By default:

Default Concurrency:
Jenkins Default Executors: 2
This means Jenkins can run two builds concurrently out of the box.
Explanation:
Executors are the worker threads that Jenkins uses to run builds. Each executor can handle one job at a time.
The number of executors is set at the controller (master) level by default, but can be increased based on your system's capacity.
How to Modify:
Go to Manage Jenkins > Manage Nodes and Clouds > Configure for your node.
Update the # of executors field to the desired value.
Save the changes.
Additional Notes:
Jenkins agents (nodes) can be added to increase overall concurrency.
Limiting concurrency per job can be controlled by plugins like Throttle Concurrent Builds or by configuring a job to use a specific agent label.













