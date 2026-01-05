## Composde Mode
Start PostgreSQL
```
docker compose up -d
```

## Manual Steps:
Prepare Secrets
```
mkdir -p secrets
echo "postgresuser" > secrets/psql_user
echo "strongpassword" > secrets/psql_pass
chmod 600 secrets/*
```

Create volume
```
docker volume create pgdata
```

Create network
```
docker network create backend
```

Run PostgreSQL container
```
docker run -d \
  --name postgres \
  --network backend \
  --restart unless-stopped \
  --memory 1G \
  --cpus 1.0 \
  --health-cmd="pg_isready -U $(cat /run/secrets/psql_user)" \
  --health-interval=30s \
  --health-timeout=5s \
  --health-retries=5 \
  --mount type=volume,source=pgdata,target=/var/lib/postgresql/data \
  --mount type=bind,source=$(pwd)/secrets/psql_user,target=/run/secrets/psql_user,readonly \
  --mount type=bind,source=$(pwd)/secrets/psql_pass,target=/run/secrets/psql_pass,readonly \
  -e POSTGRES_USER_FILE=/run/secrets/psql_user \
  -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
  -e POSTGRES_DB=appdb \
  postgres:16.2
```

