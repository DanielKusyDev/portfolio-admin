#!/usr/bin/bash
set -e

python manage.py migrate
python manage.py collectstatic
python manage.py runserver $HOST:$PORTU