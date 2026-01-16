pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-repo/house-price-prediction.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t house-price-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 house-price-app'
            }
        }
    }
}
