pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                bat 'docker build --no-cache -t travel-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                docker stop travel-container || exit 0
                docker rm travel-container || exit 0
                docker run -d -p 5000:5000 --name travel-container travel-app
                '''
            }
        }
    }
}