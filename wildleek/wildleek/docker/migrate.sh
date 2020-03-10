#!/bin/bash
docker exec -it wildleek_django python3 manage.py migrate
docker exec -it wildleek_django python3 manage.py createcachetable