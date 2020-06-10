#!/bin/bash

source ~/bashrc
ansible-playbook -i inventory -v playbook.yaml 
