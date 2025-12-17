FROM mongo:7.0.7

COPY certs/mongodb.pem /etc/ssl/mongodb.pem
COPY mongod.conf /etc/mongod.conf
RUN chmod 600 /etc/ssl/mongodb.pem

EXPOSE 27017
CMD ["mongod", "--config", "/etc/mongod.conf"]

# docker build -t my-custom-mongo:latest .
# docker run -d \
#   -p 27017:27017 \
#   -v mongo-data:/data/db \
#   -e MONGO_INITDB_ROOT_USERNAME=admin \
#   -e MONGO_INITDB_ROOT_PASSWORD=secret \
#   mongo-custom:latest