#!/usr/bin/bash
set -e

systemctl enable ssh
systemctl start ssh

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver $HOST:$PORT