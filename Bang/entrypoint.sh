#!/bin/bash

python3 manage.py migrate --no-input


python3 manage.py runbot | gunicorn Bang.wsgi:application --bind 0.0.0.0:8080
