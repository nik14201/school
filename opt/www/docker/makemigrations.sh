#!/bin/bash
#find . -iname "migrations" | xargs rm -r
docker exec -it school_teacher python3 manage.py  makemigrations profile  --settings=etc.settings.admin
docker exec -it school_teacher python3 manage.py  makemigrations teacher  --settings=etc.settings.admin
docker exec -it school_teacher python3 manage.py  makemigrations student  --settings=etc.settings.admin
docker exec -it school_teacher python3 manage.py  makemigrations parent  --settings=etc.settings.admin



