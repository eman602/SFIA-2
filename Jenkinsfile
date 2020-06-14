pipeline {
    agent any
    stages {
        stage('Making sure ownerships are made'){
            //agent {label 'master'}
            steps{
                sh 'chmod +x ./script/*'
                sh 'bash ./script/before_installation.sh'
                sh 'bash ./script/ansible.sh'
            }
        }
        
        stage('Deploying on docker-compose'){
            //agent {label 'manager_node'}
            steps{
                
                sh './script/docker.sh'
            }
        }
    }

}