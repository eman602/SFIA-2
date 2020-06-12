#!/bin/bash
source ~/bashrc

docker build -t emmanuelagyapong/service_3:latest Service_3
docker push emmanuelagyapong/service_3
docker stack deploy --compose-file docker-compose.yaml stackdemo