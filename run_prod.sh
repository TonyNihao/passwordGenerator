#!/bin/bash

docker stop $(docker ps -qa) &&\
docker rmi $(docker images -qa) &&\
docker-compose -f prod.yml up -d
