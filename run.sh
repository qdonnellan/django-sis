#!/bin/bash
export C_FORCE_ROOT="true"
python manage.py celery worker -E -A django_sis --loglevel=INFO &
python manage.py runserver_plus 0.0.0.0:8000

