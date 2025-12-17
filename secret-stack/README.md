With Swarm Stack
```
docker stack deploy -c docker-compose.yaml my-app
```

Manual steps
```
echo "your_postgres_password" | docker secret create psql-pw -
docker volume create postgres-data
docker volume create nginx-logs


docker service create \
  --name fontend-app \
  --publish published=8080,target=80 \
  --mount type=volume,source=nginx-logs,target=/var/log/nginx \
  nginx:latest

docker service create \
  --name postgres \
  --secret psql-pw \
  --env POSTGRES_PASSWORD_FILE=/run/secrets/psql-pw \
  --mount type=volume,source=postgres-data,target=/var/lib/postgresql/data \
  postgres:14
```
Check the status
```
docker service ls
docker service ps fontend-app
docker service ps postgres
```
Check Logs
```
docker service logs postgres
docker service logs fontend-app
```