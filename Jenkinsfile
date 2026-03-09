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
        }   }
    }
}