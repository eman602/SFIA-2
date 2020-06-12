#!/bin/bash
source ~/bashrc
sudo chmod 666 /var/run/docker.sock
docker build -t emmanuelagyapong/service_1:latest ./Service_1
docker build -t emmanuelagyapong/service_2:latest ./Service_2
docker build -t emmanuelagyapong/service_3:latest ./Service_3
docker build -t emmanuelagyapong/service_3:latest ./Service_4


docker push emmanuelagyapong/service_1
docker push emmanuelagyapong/service_2
docker push emmanuelagyapong/service_3
docker push emmanuelagyapong/service_4

docker stack deploy --compose-file docker-compose.yaml stackdemo