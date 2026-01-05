## SWARM Steps
Initialize swarm (once)
```
docker swarm init
```

Before starting this stack, ensure that secreats are created 
```
echo "postgresuser" | docker secret create psql_user -
echo "strongpassword" | docker secret create psql_pass -
```

Deploy the stack
```
docker stack deploy -c docker-compose.yml db
```

## Manual Steps:
Create Secrets
```
echo "postgresuser" | docker secret create psql_user -
echo "strongpassword" | docker secret create psql_pass -
```

Create Volumes 
```
docker volume create pgdata
```

Create Overlay Network
```
docker network create \
  --driver overlay \
  --attachable \
  backend
```

Start the SQL Service
```
docker service create \
  --name postgres \
  --network backend \
  --secret source=psql_user,target=psql_user \
  --secret source=psql_pass,target=psql_pass \
  --env POSTGRES_USER_FILE=/run/secrets/psql_user \
  --env POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
  --env POSTGRES_DB=appdb \
  --mount type=volume,source=pgdata,target=/var/lib/postgresql/data \
  --health-cmd="pg_isready -U $(cat /run/secrets/psql_user)" \
  --health-interval=30s \
  --health-timeout=5s \
  --health-retries=5 \
  --limit-cpu=1.0 \
  --limit-memory=1G \
  --reserve-cpu=0.25 \
  --reserve-memory=256M \
  --constraint 'node.role==manager' \
  --restart-condition on-failure \
  --restart-delay 10s \
  --restart-max-attempts 5 \
  --replicas 1 \
  postgres:16.2
```