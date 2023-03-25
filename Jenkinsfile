pipeline {
    agent any

    environment {
        http = 'http://172.16.1.51:8080'
    }

    stages {
        stage("kopiowanie wara") {
            steps {
                sh 'sudo cp /home/vagrant/pliczki/workspace/Diploy_proba/war/* /home/vagrant/budowa'
            }
        }
        stage("Budowanie obrazu dockera ") {
            steps{
                script {
                    docker.build("TomcatApka:${env.BUILD_NUMBER}", "-f Dockerfile .")
                }
            }
        }
        stage("Startowanie kontenera") {
            steps{
                script {
                    docker.image("TomcatApka:${env.BUILD_NUMBER}").run("-p 8080:8090 -v /home/vagrant/war:/usr/local/tomcat/webapps/myapp.war")
                }
            }
        }
        stage("Testowanie połączenia z serverem") {
            steps {
                script {
                    def response = sh(returnStdout: true, script: "curl --head ${http}/SampleWebApp | grep HTTP")
                    def obcieta = response.trim()
                    if(obcieta =~ /200/) {
                        echo "Gituwa połączenie Kod: ${obcieta}"
                    }else {
                        echo "Chujówka kod błędu ${obcieta} "
                    }
                    
                }
            }
        }
    }
}
