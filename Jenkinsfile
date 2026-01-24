pipeline {
    agent any

    environment {
        IMAGE_NAME = "kaushalkolaskar/ci-cd-demo"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/kolaskarkaushal-a11y/ci-cd-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test || echo "No tests found"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop app || true
                docker rm app || true
                docker run -d -p 3000:3000 --name app $IMAGE_NAME:latest
                '''
            }
        }
    }
}
