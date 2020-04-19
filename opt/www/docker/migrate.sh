#!/bin/bash
docker exec -it school_admin python3 manage.py migrate
docker exec -it school_parent python3 manage_parent.py migrate
docker exec -it school_teacher python3 manage_teacher.py migrate
docker exec -it school_student python3 manage_student.py migrate

docker exec -it school_admin python3 manage.py createcachetable