#!/bin/bash
cd /home/openschool/www
git pull origin master
#docker restart nvkot_redactor  nvkot_author nvkot_admin  nvkot_reader
#docker exec -it nvkot_admin python3 manage.py migrate
#docker restart nvkot_admin
