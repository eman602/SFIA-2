#!/bin/bash

source ~/bashrc
ansible-playbook -i inventory.cfg -v playbook.yaml 
