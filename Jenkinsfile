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

        stage('Stop Old Container') {
            steps {
                sh 'docker stop house-price-prediction || true'
                sh 'docker rm house-price-prediction || true'
            }


        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8001:8000 house-price-app'
            }
        }
    }
}
