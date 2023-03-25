import git
import os

to_deploy_path = "/home/vagrant/pliczki/workspace/Diploy_proba/war/SampleWebApp.war"

deploy_path = "/opt/tomcat/webapps"

os.system(f"sudo cp {to_deploy_path} {deploy_path} ")




