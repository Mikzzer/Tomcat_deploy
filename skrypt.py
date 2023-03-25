import git
import os

repo_path = "/home/vagrant/repo"

to_deploy_path = "/home/vagrant/repo/war/SampleWebApp.war"

deploy_path = "/opt/tomcat/webapps"


repo_url = "https://github.com/Mikzzer/Tomcat_deploy.git"
git.Repo.clone_from(repo_url, repo_path)

os.system(f"cp {to_deploy_path} {deploy_path} ")




