#!/bin/bash
docker exec -it school_admin python3 manage.py createsuperuser --settings=etc.settings.admin

#docker exec -it school_teacher python3 manage_teacher.py createsuperuser --settings=etc.settings.teacher
#docker exec -it school_teacher python3 manage_student.py createsuperuser --settings=etc.settings.student
#docker exec -it school_teacher python3 manage_parent.py createsuperuser --settings=etc.settings.parent
