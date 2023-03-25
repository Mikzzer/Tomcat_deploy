pipeline {
    agent any

environment{
    def http = 'http://172.16.1.51:8080'
}


    stages {
        stage("Odpalanie skryptu"){
            steps{
                sh 'python3 /home/vagrant/pliczki/workspace/Diploy_proba/skrypt.py'
            }
        }
        stage("Testowanie połączenia z serverem"){
            steps{
                def response = sh(returnStdout: true, script: 'curl --head -w "%{http_code}" http://172.16.1.51:8080/SampleWebApp -o /dev/null')
                echo response
            }
        }
    }
}
