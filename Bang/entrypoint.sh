#!/bin/bash

python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py createcachetable
python3 manage.py runbot

exec gunicorn Bang.wsgi:application -b 0.0.0.0:8000 --reload
