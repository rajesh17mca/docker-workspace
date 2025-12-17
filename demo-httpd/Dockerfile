FROM docker.io/library/httpd:latest
RUN apt-get update 
RUN apt-get install -y curl
COPY ./index.html /usr/local/apache2/htdocs/index.html