#!/bin/bash
#find . -iname "migrations" | xargs rm -r
docker exec -it wildleek_django  python3 manage.py makemigrations 

