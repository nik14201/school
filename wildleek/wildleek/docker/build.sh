#!/bin/bash
docker build  -t  wildleek_django -f ./dockerfile_django .
docker build  -t  wildleek_frontend -f ./dockerfile_frontend .
docker-compose up -d