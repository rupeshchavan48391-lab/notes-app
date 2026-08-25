pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/rupeshh7/notes-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t rupeshh7/notes-app:latest .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm rupeshh7/notes-app:latest python manage.py check'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Docker Hub push will be configured with Jenkins credentials'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage will be configured next'
            }
        }
    }
}
