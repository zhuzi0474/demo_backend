pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('UnitTest') {
            steps {
                echo 'unit Testing..'
                sh 'python test_runner.py'
            }
        }
        stage('integrationTest') {
            steps {
                echo 'integration Testing..'
                sh 'pwd'
                sh 'chmod 400 deankeypair.pem'
                sh 'ssh -i "deankeypair.pem" -o StrictHostKeyChecking=no ec2-user@ec2-18-181-168-225.ap-northeast-1.compute.amazonaws.com -tt "pwd ; cd ./demo_backend ; git pull"'
                sh 'python integration_test_runner.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'pwd'
                sh 'chmod 400 deankeypair.pem'
                sh 'ssh -i "deankeypair.pem" -o StrictHostKeyChecking=no ec2-user@ec2-18-181-168-225.ap-northeast-1.compute.amazonaws.com -tt "pwd ; cd ./demo_backend ; git pull"'
            }
        }
    }
}
