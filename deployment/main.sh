#!/usr/bin/env bash

echo -r "Running deployment for zhuhao ..."
ansible-playbook -i inventory/$1 playbook.yml -v
