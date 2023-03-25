pipeline {
    agent any

def http = new groovyx.net.http.HTTPBuilder('http://172.16.1.51:8080/SampleWebApp')


    stages {
        stage("Odpalanie skryptu"){
            steps{
                python3 'skrypt.py'
            }
        }
        stage("Testowanie połączenia"){
            steps{
                @Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.7.1')
                script{
                    http.request(GET, TEXT) { req ->
                        response.succes = { resp, reader ->
                            assert resp.status == 200
                            assert reader.text.contains("DOMENA")
                        }

                    }

                }
            }
        }
    }
}
