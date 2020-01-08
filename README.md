#Web application


## Run

```

docker-compose down

docker system prune -fa


docker-compose run web python app/convertfile/manage.py migrate

docker-compose run web python app/convertfile/manage.py makemigrations

docker-compose run web python app/convertfile/manage.py collectstatic

docker-compose run web python app/convertfile/manage.py createsuperuser
```

# supported file extension.


I had some problems
lient intended to send too large body: 4359797 bytes, client: 172.17.0.1, server

solution
# nano nginx.conf
client_max_body_size 100m;
