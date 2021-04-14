#!/bin/bash

echo "Pull latest code from GH"
git pull

echo "Enter venv"
source .venv/bin/activate

echo "Collect static"
./manage.py collectstatic --settings codemarmalad.settings_prod

echo "Run gunicorn"
./.venv/bin/gunicorn --bind unix:codemarmalad.sock codemarmalad.wsgi --workers 2
