## Compose Steps
Start the App
```
docker compose up -d
```

Scale httpd (Compose Style)
```
docker compose up -d --scale httpd=3
```


## Manul Steps
Create a Docker network
```
docker network create web
```

Start HTTPD Container (Backend)
```
docker run -d \
  --name httpd \
  --network web \
  -v $(pwd)/httpd/httpd.conf:/usr/local/apache2/conf/httpd.conf:ro \
  -v $(pwd)/httpd/index.html:/usr/local/apache2/htdocs/index.html:ro \
  httpd:2.4-alpine
```

Start nginx container (frontend)
```
docker run -d \
  --name nginx \
  --network web \
  -p 80:80 \
  -v $(pwd)/nginx/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx:1.26-alpine
```

Check logs
```
docker ps
docker logs httpd
```

