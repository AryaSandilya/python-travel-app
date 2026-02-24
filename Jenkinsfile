pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/AryaSandilya/python-travel-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build --no-cache -t travel-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop travel-container || true
                docker rm travel-container || true
                docker run -d -p 5000:5000 --name travel-container travel-app
                '''
            }
        }
    }
}