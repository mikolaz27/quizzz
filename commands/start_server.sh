#!/bin/bash

echo "hello from docker"
python src/manage.py migrate
python src/manage.py runserver 0:8010
