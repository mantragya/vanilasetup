pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the Git repository
                git(url: 'https://github.com/EqualExperts-Assignments/equal-experts-observant-sleek-regal-understanding-0c448b80d1d7.git', branch: 'solution')
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
                //TODO install test depdendecies
                // Activate the virtual environment and run Flake8
                bat 'venv\\Scripts\\Activate && flake8 src --exit-zero'
            }
        }
        
        stage('Run Tests and Coverage') {
            steps {
                // Activate the virtual environment
                bat 'venv\\Scripts\\Activate'
                
                // Run tests using pytest
                bat 'pytest --cov=your_module tests/'
                
                // Generate coverage report
                bat 'coverage html -d coverage_html'
            }
        }
    }
    
    post {
        always {
            // Deactivate the virtual environment
            sh 'deactivate'
        }
    }
}
