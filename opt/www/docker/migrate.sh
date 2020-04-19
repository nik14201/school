#!/bin/bash

docker exec -it school_teacher python3 manage.py migrate sites
docker exec -it school_teacher python3 manage_teacher.py migrate sites
docker exec -it school_teacher python3 manage_parent.py migrate sites
docker exec -it school_teacher python3 manage_student.py migrate sites

docker exec -it school_teacher python3 manage.py  makemigrations profiles
docker exec -it school_teacher python3 manage.py  makemigrations teacher
docker exec -it school_teacher python3 manage.py  makemigrations student
docker exec -it school_teacher python3 manage.py  makemigrations parent

docker exec -it school_teacher python3 manage.py migrate

docker exec -it school_admin python3 manage.py createcachetable