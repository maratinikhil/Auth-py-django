pipeline{
    agent {label "Python-Sample-Project"}
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage ("git checkout") {
            steps {
                git url: "https://github.com/maratinikhil/Auth-py-django.git",
                    branch: "main"
           }
        }
        stage ("installing dependencies"){
            steps {
                sh """
                python3 -m venv venv 
                . venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }
        stage ("build & scane") {
            steps {
                withCredentials([string(credentialsId: "sonarcloud_id", variable: "SONAR_TOKEN")]){
                withSonarQubeEnv("SONAR") {
                    sh """sonar:scannerr \
                        -Dsonar.projectKey=maratinikhil_Auth-py-django \
                        -Dsonar.organization=maratinikhil \
                        -Dsonar.host.url=https://sonarcloud.io/
                        -Dsonar.login=$SONAR_TOKEN
                    """
                }
                }
            }
        }
    }
}



