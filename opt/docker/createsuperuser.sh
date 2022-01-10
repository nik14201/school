#!/bin/bash
docker exec -it school_admin python3 manage.py createsuperuser --settings=etc.settings.admin


