pipeline {
    agent any

    environment {
        def http = 'http://172.16.1.52'
    }

    stages {
        stage("Odpalanie skryptu") {
            steps {
                sh 'python3 /home/vagrant/pliczki/workspace/Diploy_proba/skrypt.py'
            }
        }
        stage("Testowanie połączenia z serverem") {
            steps {
                script {
                    def response = sh(returnStdout: true, script: "curl --head ${http} | grep HTTP")
                    def obcieta = response.trim()
                    if(obcieta =~ /200/) {
                        echo "Gituwa połączenie Kod: ${obcieta}"
                    }else {
                        echo "Chujówka kod błędu ${obcieta}"
                    }
                    
                }
            }
        }
    }
}
