
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

        stage('Build Docker Image') {
            steps {
                echo 'Building Task Manager Docker image'

                script {
                    env.GIT_COMMIT_SHORT = sh(
                        script: 'git rev-parse --short=12 HEAD',
                        returnStdout: true
                    ).trim()
                }

                sh '''
                    docker build --pull \
                        -t task-manager:latest \
                        -t task-manager:${GIT_COMMIT_SHORT} \
                        .
                '''
            }
        }

        stage('Verify Docker Image') {
            steps {
                echo 'Verifying Docker image'

                sh '''
                    docker image inspect task-manager:latest

                    docker image inspect \
                        task-manager:${GIT_COMMIT_SHORT}

                    echo "Docker image successfully created!"
                    echo "Commit: ${GIT_COMMIT_SHORT}"
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CI and Docker image build completed!'
        }

        failure {
            echo 'FAILED: Check the console output for errors.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}

