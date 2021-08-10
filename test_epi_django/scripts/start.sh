#!/bin/bash

cd test_epi_django
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000
