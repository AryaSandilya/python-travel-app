pipeline {
    agent any

    environment {
        // Defining variables makes the script cleaner and easier to update
        IMAGE_NAME = "travel-app"
        CONTAINER_NAME = "travel-container"
        APP_PORT = "5000"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                echo 'Cleaning up the workspace...'
                deleteDir()
            }
        }

        stage('Checkout Latest Code') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'main', 
                    url: 'https://github.com/AryaSandilya/python-travel-app.git'
            }
        }

        stage('Build Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}..."
                // --no-cache ensures a fresh build every time
                bat "docker build --no-cache -t ${IMAGE_NAME} ."
            }
        }

        stage('Deploy Container') {
            steps {
                echo "Deploying to http://localhost:${APP_PORT}"
                bat """
                @echo off
                :: Stop and remove the container if it already exists
                docker stop ${CONTAINER_NAME} >nul 2>&1 || ver >nul
                docker rm ${CONTAINER_NAME} >nul 2>&1 || ver >nul
                
                :: Run the new container
                docker run -d -p ${APP_PORT}:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                
                :: Show status
                docker ps -f name=${CONTAINER_NAME}
                """
            }
        }
    }
    
    post {
        success {
            echo 'Build and Deployment Successful!'
        }
        failure {
            echo 'Something went wrong. Check the Docker logs or Jenkins console.'
        }
    }
}
