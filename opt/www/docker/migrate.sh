#!/bin/bash

docker exec -it school_admin python3 manage.py migrate sites --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py    migrate  --settings=etc.settings.admin
docker exec -it school_admin python3 manage.py createcachetable --settings=etc.settings.admin

docker exec -it school_admin   python3 manage.py  migrate profileuser    --settings=etc.settings.admin
docker exec -it school_teacher python3 manage.py  migrate teacher  --settings=etc.settings.teacher
docker exec -it school_student python3 manage.py  migrate student  --settings=etc.settings.student
docker exec -it school_parent  python3 manage.py  migrate parentuser   --settings=etc.settings.parent

#docker exec -it school_admin python3 manage.py migrate account admin homework lesson sessions socialaccount subject weather youtube --settings=etc.settings.admin


