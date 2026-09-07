pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv playenv
                . playenv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . playenv/bin/activate
                pip install -r requirements.txt
                playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh '''
                    . playenv/bin/activate
                    pytest tests/ --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh '''
                    if command -v allure >/dev/null 2>&1
                    then
                        allure generate allure-results -o allure-report --clean
                    else
                        echo "Allure not installed. Skipping report generation."
                    fi
                    '''
                }
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
                archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            }
        }
    }

    post {

        always {
            echo 'Pipeline execution completed'
        }

        success {
            echo 'All stages completed successfully'
        }

        unstable {
            echo 'Pipeline completed with warnings'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}
