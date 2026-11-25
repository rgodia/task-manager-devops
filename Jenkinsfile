
pipeline {
    agent {
        label 'python'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies'

                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests'

                sh '''
                    . venv/bin/activate
                    python -m pytest -v
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All CI stages completed!'
        }

        failure {
            echo 'FAILED: Check the console output for errors.'
        }

        always {
            echo 'CI pipeline execution finished.'
        }
    }
}

