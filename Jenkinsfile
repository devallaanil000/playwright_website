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
            sh '''
            . playenv/bin/activate
            pytest tests/ --alluredir=allure-results
            '''
        }
    }

    stage('Generate Allure Report') {
        steps {
            sh '''
            /opt/homebrew/bin/allure --version
            /opt/homebrew/bin/allure generate allure-results -o allure-report --clean
            '''
        }
    }
}

post {

    always {
        archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true

        publishHTML(target: [
            allowMissing: true,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: 'allure-report',
            reportFiles: 'index.html',
            reportName: 'Allure Report'
        ])
    }

    success {
        echo 'Tests Passed'

        emailext(
            subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """
            <h3>Playwright Automation Execution Successful</h3>

            <p><b>Job:</b> ${env.JOB_NAME}</p>
            <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
            <p><b>Status:</b> SUCCESS</p>

            <p>
            <a href="${env.BUILD_URL}">
            View Build Details
            </a>
            </p>
            """,
            mimeType: 'text/html',
            to: 'devallaanil789@gmail.com'
        )
    }

    failure {
        echo 'Tests Failed'

        emailext(
            subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """
            <h3>Playwright Automation Execution Failed</h3>

            <p><b>Job:</b> ${env.JOB_NAME}</p>
            <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
            <p><b>Status:</b> FAILURE</p>

            <p>
            <a href="${env.BUILD_URL}">
            View Build Details
            </a>
            </p>
            """,
            mimeType: 'text/html',
            to: 'devallaanil789@gmail.com'
        )
    }
}

}