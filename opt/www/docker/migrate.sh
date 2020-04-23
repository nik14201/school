#!/bin/bash

docker exec -it school_admin python3 manage.py migrate sites --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py migrate sites --settings=etc.settings.teacher
docker exec -it school_admin python3 manage.py migrate sites --settings=etc.settings.student
docker exec -it school_admin python3 manage.py migrate sites --settings=etc.settings.parent

docker exec -it school_admin python3 manage.py  makemigrations profiles --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations teacher --settings=etc.settings.teacher
docker exec -it school_admin python3 manage.py  makemigrations student --settings=etc.settings.student
docker exec -it school_admin python3 manage.py  makemigrations parent --settings=etc.settings.parent

docker exec -it school_admin python3 manage.py migrate --settings=etc.settings.admin

docker exec -it school_admin python3 manage.py createcachetable --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py createcachetable --settings=etc.settings.teacher
docker exec -it school_admin python3 manage.py createcachetable --settings=etc.settings.student
docker exec -it school_admin python3 manage.py createcachetable --settings=etc.settings.parent