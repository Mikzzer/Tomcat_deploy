pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Mikzzer/Tomcat_deploy.git'
            }
        }
        
        stage('Deploy to Tomcat') {
            environment {
                TOMCAT_HOME = '/opt/tomcat' // ścieżka do katalogu Tomcat
                APP_NAME = 'SampleWebApp.war' // nazwa aplikacji, którą chcemy umieścić w katalogu webapps
            }
            steps {
                sh "cp SampleWebApp.war $TOMCAT_HOME/webapps/$APP_NAME.war"
            }
        }
    }
}
