pipeline {
    agent any

    environment {
        http = 'http://172.16.1.51:8090/SampleWebApp/'
    }

    stages {
        stage("kopiowanie wara") {
            steps {
                sh 'cp /home/vagrant/workspace/Pipe_dockerorch/war/SampleWebApp.war /home/vagrant/budowa/'
            }
        }
        stage("kopiowanie dockera") {
            steps {
                sh 'cp /home/vagrant/workspace/Pipe_dockerorch/Dockerfile /home/vagrant/budowa/'
            }
        }
        stage("Budowanie obrazu dockera ") {
            steps{
                script {
                    docker.build("tomcatapka:${env.BUILD_NUMBER}", "-f Dockerfile /home/vagrant/budowa/.")
                }
            }
        }
        stage("Startowanie kontenera") {
            steps{
                script {
                    docker.image("tomcatapka:${env.BUILD_NUMBER}").run("-p 8090:8080 -v /home/vagrant/budowa/SampleWebApp.war:/usr/local/tomcat/webapps/SampleWebApp.war")
                }
            }
        }
        stage("Testowanie połączenia z serverem") {
            steps {
                script {
                    def response = sh(returnStdout: true, script: "curl -v --head http://172.16.1.51:8090/SampleWebApp/ | grep HTTP")
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
