pipeline {
    environment {
        registry = "zoejoyuliao/django-rest-framework-demo"
        registryCredential = 'dockerhub'
    }
    agent any
    stages {
        stage('Building image') {
            steps{
                script {
                    docker.build registry + ":$BUILD_NUMBER"
		}
            }
        }
    }
}
