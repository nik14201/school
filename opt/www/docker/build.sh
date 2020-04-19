#!/bin/bash
docker build  -t  school_django -f ./dockerfile_django .
#docker build  -t  school_frontend -f ./dockerfile_frontend .
docker-compose up -d