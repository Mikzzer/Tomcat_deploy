FROM tomcat:9.0

COPY *.war /usr/local/tomcat/webapps/
RUN apt-get update 
RUN apt-get install -y gcc
RUN apt-get install -y curl

CMD ["catalina.sh", "run"]

EXPOSE 8070
