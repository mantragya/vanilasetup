pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'mantragya/githubapi'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        HELM_RELEASE_NAME = 'github-gists-api'
        HELM_CHART_PATH = './helm'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the Git repository
                git(url: 'https://github.com/mantragya/vanilasetup.git', branch: 'develop')
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // You may need to install Python and virtual environment if not already installed
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\Activate && pip install -r requirements.txt'
            }
        }
        
        stage('Run Flake8') {
            steps {
                // Activate the virtual environment and run Flake8
                bat 'venv\\Scripts\\Activate && flake8 src --exit-zero'
            }
        }
        
        stage('Run Tests and Coverage') {
            steps {
                // Activate the virtual environment
                bat 'venv\\Scripts\\Activate'
                
                // Run tests using pytest
                bat 'pytest --cov=src tests/'
                
                // Generate coverage report
                bat 'coverage html -d coverage_html'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                bat "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }
        
        stage('Push Docker Image') {
            steps {
                // Login to Docker registry (assuming credentials are configured)
                // bat 'docker login -u username -p password'
                
                // Push the image
                bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                bat "docker push ${IMAGE_NAME}:latest"
            }
        }
        
        stage('Deploy with Helm') {
            steps {
                // Update Helm values with new image tag
                bat "helm upgrade --install ${HELM_RELEASE_NAME} ${HELM_CHART_PATH} --set image.tag=${IMAGE_TAG} --namespace default"
            }
        }
    }
    
    post {
        always {
            // Clean up
            bat 'docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true'
        }
    }
}
