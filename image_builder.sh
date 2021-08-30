#!/bin/bash
USERNAME=$1
PASSWORD=$2

docker build -t tonyprilipa/pwdgen_frontend frontend/. &&\
docker build -t tonyprilipa/pwdgen_backend backend/. &&\
docker build -t tonyprilipa/pwdgen_proxy/. 

docker login -u $USERNAME -p $PASSWORD

docker push tonyprilipa/pwdgen_frontend
docker push tonyprilipa/pwdgen_backend
docker push tonyprilipa/pwdgen_proxy

