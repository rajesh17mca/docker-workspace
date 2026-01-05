## SWARM Steps
Initialize swarm (once)
```
docker swarm init
```
Deploy stack
```
docker stack deploy -c docker-compose.yml webstack
```

Check services
```
docker service ls
```

Inspect logs
```
docker service logs webstack_nginx
docker service logs webstack_httpd
```


## Manual Steps
Initialize swarm (once)
```
docker swarm init
docker node ls
```

Create overlay network
```
docker network create \
  --driver overlay \
  --attachable \
  web
```

Create Docker configs (production best practice)
```
docker config create nginx_conf nginx/nginx.conf
docker config create httpd_conf httpd/httpd.conf
docker config ls
```

Start httpd service (backend)
```
docker service create \
  --name httpd \
  --replicas 3 \
  --network web \
  --config-source httpd_conf \
  --config-target /usr/local/apache2/conf/httpd.conf \
  httpd:2.4-alpine
```

Verify
```
docker service ps httpd
docker service logs httpd
```

Start nginx service (frontend)
```
docker service create \
  --name nginx \
  --replicas 2 \
  --publish published=80,target=80 \
  --network web \
  --config-source nginx_conf \
  --config-target /etc/nginx/nginx.conf \
  nginx:1.26-alpine
```

Test
```
curl http://<manager-node-ip>
```

Update config without downtime (Swarm)
```
docker config rm nginx_conf
docker config create nginx_conf nginx/nginx.conf

docker service update \
  --config-rm nginx_conf \
  --config-add source=nginx_conf,target=/etc/nginx/nginx.conf \
  nginx
```

Remove Swarm Stack Manually
```
docker service rm nginx httpd
docker config rm nginx_conf httpd_conf
docker network rm web
docker swarm leave --force
```
