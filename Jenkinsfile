pipeline {
    agent any

    environment {
        http = 'http://172.16.1.51:8080'
    }

    stages {
        stage("kopiowanie wara") {
            steps {
                sh 'cp /home/vagrant/pliczki/workspace/Docker_deployTomcat/war/SampleWebApp.war /home/vagrant/budowa/'
            }
        }
        stage("kopiowanie dockera") {
            steps {
                sh 'cp /home/vagrant/pliczki/workspace/Docker_deployTomcat/Dockerfile /home/vagrant/budowa/'
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
                    docker.image("tomcatapka:${env.BUILD_NUMBER}").run("-p 8080:8090 -v /home/vagrant/budowa/SampleWebApp.war:/usr/local/tomcat/webapps/myapp.war")
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
