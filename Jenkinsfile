pipeline {
    agent any

    stages {
        stage("Odpalanie skryptu") {
            steps {
                sh 'python3 skrypt.py'
            }
        }
        stage("Testowanie połączenia") {
            steps {
                // Pobranie modułu HTTPBuilder
                @Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.7.1')

                // Wykonanie zapytania GET i sprawdzenie odpowiedzi
                script {
                    def http = new groovyx.net.http.HTTPBuilder('http://172.16.1.51:8080/SampleWebApp')
                    
                    http.request(GET, TEXT) { req ->
                        response.success = { resp, reader ->
                            assert resp.status == 200
                            assert reader.text.contains("DOMENA")
                        }
                    }
                }
            }
        }
    }
}
