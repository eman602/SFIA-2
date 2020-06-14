#!/bin/bash
sudo apt update -y
sudo apt install python3 python3-venv python3-pip -y
python3 -m venv venv
source ~/bashrc
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/bashrc
source ~/bashrc
## install ansible with pip
pip install --user ansible
# check that ansible has been installed
ansible --version