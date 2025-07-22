pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/sampleapp"
        DOCKER_CREDENTIALS_ID = "dockerhub-creds"
        KUBE_CONTEXT = "sampleapp.k8s.local"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Karika09/sample-flask-app.git', branch: 'main' 
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push Docker Image') {
    steps {
        script {
            docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                def image = docker.image('sarikasan94/sampleapp')
                image.push('latest')
            }
        }
    }
}

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl config use-context ${KUBE_CONTEXT}
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Deployment failed!'
        }
    }
}
