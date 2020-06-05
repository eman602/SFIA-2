pipeline {
    agent any
    stages {
        stage('Making sure ownerships are made'){
            
            steps{
                sh 'chmod +x ./script/*'
                sh 'bash ./script/before_installation.sh'
            }
        }
        
        stage('Deploying on docker-compose"'){
            
            steps{
                
                sh './script/docker.sh'
            }
        }
    }

}