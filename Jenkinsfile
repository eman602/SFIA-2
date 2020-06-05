pipeline {
    agent none
    stages {
        stage('Making sure ownerships are made'){
            agent {label 'master'}
            steps{
                sh 'chmod +x ./script/*'
                sh 'bash ./script/before_installation.sh'
            }
        }
        
        stage('Deploying on docker-compose"'){
            agent {label 'manager_node'}
            steps{
                sh 'chmod +x ./script/*'
                sh './script/docker.sh'
            }
        }
    }

}