#!/bin/bash
#find . -iname "migrations" | xargs rm -r
docker exec -it school_django  python3 manage.py makemigrations

