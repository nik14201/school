#!/bin/bash
#find . -iname "migrations" | xargs rm -r
docker exec -it school_admin python3 manage.py    makemigrations profileuser    --settings=etc.settings.admin
docker exec -it school_teacher python3 manage.py  makemigrations teacher  --settings=etc.settings.teacher
docker exec -it school_student python3 manage.py  makemigrations student  --settings=etc.settings.student
docker exec -it school_parent  python3 manage.py  makemigrations parentuser   --settings=etc.settings.parent

docker exec -it school_admin python3 manage.py  makemigrations country --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations city --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations diary --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations homework --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations lesson --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations school --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations sclass --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations subject --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations weather --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py  makemigrations youtube --settings=etc.settings.admin

