#!/bin/bash
#find . -iname "migrations" | xargs rm -r
docker exec -it school_teacher python3 manage.py  makemigrations teacher
docker exec -it school_teacher python3 manage.py  makemigrations student
docker exec -it school_teacher python3 manage.py  makemigrations parent



