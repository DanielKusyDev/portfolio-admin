#!/usr/bin/bash
set -e

/usr/sbin/sshd &

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver $HOST:$PORT