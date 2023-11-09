#!/bin/bash

sudo apt update
sudo apt install git -y
ssh-keygen -t rsa -N "" -f /home/vagrant/.ssh/id_rsa