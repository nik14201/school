#!/bin/bash
docker exec -it school_teacher python3 manage.py createsuperuser

docker exec -it school_teacher python3 manage_teacher.py createsuperuser
docker exec -it school_teacher python3 manage_student.py createsuperuser
docker exec -it school_teacher python3 manage_parent.py createsuperuser
