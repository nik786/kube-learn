
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
















