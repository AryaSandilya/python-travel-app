pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/AryaSandilya/python-travel-app.git/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t travel-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker rm -f travel-container || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 --name travel-container travel-app
                '''
            }
        }
    }
}