#!/bin/bash

#docker exec -it school_admin python3 manage.py dumpdata weather --indent 2 --settings=etc.settings.admin > dump.json

python3 manage.py dumpdata youtube weather teacher student profiles --indent 2 --settings=etc.settings.admin > dump.json